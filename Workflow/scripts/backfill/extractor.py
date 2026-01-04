"""
Backfill Extractor: AI extraction for existing notes.

Uses the model specified in config.yaml (models.backfill) to extract
summaries and mentions from existing notes for populating README context.

Supports parallel extraction for faster processing.
"""

import hashlib
import json
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path
from typing import Callable

from openai import OpenAI

from . import (
    BackfillExtraction,
    BackfillExtractionLite,
    BackfillManifest,
    ExtractionBatch,
    NoteMetadata,
    CrossLinks,
)

# Import from existing utils
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from utils.config import vault_root


# ─────────────────────────────────────────────────────────────────────────────
# Prompt Loading
# ─────────────────────────────────────────────────────────────────────────────


def get_prompt_template() -> str:
    """Load the backfill extraction prompt template."""
    workflow_root = Path(__file__).parent.parent.parent
    prompts_dir = workflow_root / "prompts"
    
    template_path = prompts_dir / "backfill-extractor.md.j2"
    if template_path.exists():
        return template_path.read_text()
    
    # Fallback inline prompt
    return """
You are extracting structured metadata from an existing note for indexing.

## Output Format
Return valid JSON only. No markdown fences, no explanations.

```json
{
  "summary": "1-2 sentence summary",
  "mentions": {
    "people": ["Name1"],
    "projects": ["Project1"],
    "accounts": ["Company1"]
  },
  "key_facts": ["Fact 1", "Fact 2"]
}
```

## Note Content
{{ content }}
"""


def load_manifests(vault: Path) -> dict[str, str]:
    """Load entity manifests for injection into extraction prompt."""
    manifests = {}
    
    # People manifest
    people_manifest = vault / "VAST" / "People" / "_MANIFEST.md"
    if people_manifest.exists():
        manifests["people"] = people_manifest.read_text()
    
    # Customers manifest
    customers_manifest = vault / "VAST" / "Customers and Partners" / "_MANIFEST.md"
    if customers_manifest.exists():
        manifests["customers"] = customers_manifest.read_text()
    
    # Projects manifest
    projects_manifest = vault / "VAST" / "Projects" / "_MANIFEST.md"
    if projects_manifest.exists():
        manifests["projects"] = projects_manifest.read_text()
    
    return manifests


def format_manifests_for_prompt(manifests: dict[str, str]) -> str:
    """Format manifests as a single block for the prompt."""
    if not manifests:
        return ""
    
    sections = []
    
    if "people" in manifests:
        sections.append("### Known People\n" + manifests["people"])
    
    if "customers" in manifests:
        sections.append("### Known Customers/Partners\n" + manifests["customers"])
    
    if "projects" in manifests:
        sections.append("### Known Projects\n" + manifests["projects"])
    
    return "\n\n---\n\n".join(sections)


def render_prompt(
    note_path: str,
    note_date: str | None,
    entity_name: str,
    content: str,
    manifests: dict[str, str] | None = None,
) -> str:
    """Render the extraction prompt with note context and entity manifests."""
    template_str = get_prompt_template()
    
    # Simple string replacement (not full Jinja for speed)
    prompt = template_str.replace("{{ note_path }}", note_path)
    prompt = prompt.replace("{{ note_date | default('Unknown') }}", note_date or "Unknown")
    prompt = prompt.replace("{{ entity_name | default('Unknown') }}", entity_name)
    prompt = prompt.replace("{{ content }}", content)
    
    # Inject manifests if provided
    if manifests:
        manifest_text = format_manifests_for_prompt(manifests)
        prompt = prompt.replace("{{ manifests }}", manifest_text)
    else:
        prompt = prompt.replace("{{ manifests }}", "")
    
    return prompt


# ─────────────────────────────────────────────────────────────────────────────
# OpenAI Client
# ─────────────────────────────────────────────────────────────────────────────


def get_client() -> OpenAI:
    """Get OpenAI client with API key from environment."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set")
    return OpenAI(api_key=api_key)


def extract_from_content(
    client: OpenAI,
    note_path: str,
    note_date: str | None,
    entity_name: str,
    content: str,
    model: str = "gpt-4o-mini",
    manifests: dict[str, str] | None = None,
) -> tuple[BackfillExtractionLite, int]:
    """
    Call OpenAI to extract metadata from note content using structured outputs.
    
    Uses Pydantic model parsing for guaranteed schema adherence.
    
    Args:
        client: OpenAI client
        note_path: Path to the note being extracted
        note_date: Date of the note if known
        entity_name: Name of the parent entity
        content: Note content
        model: Model to use (must support structured outputs)
        manifests: Entity manifests for context
    
    Returns:
        Tuple of (BackfillExtractionLite, tokens_used)
    """
    prompt = render_prompt(note_path, note_date, entity_name, content, manifests)
    
    # Use structured outputs with Pydantic model parsing
    response = client.responses.parse(
        model=model,
        instructions="You extract structured metadata from notes for indexing. Extract only what is clearly present.",
        input=prompt,
        text_format=BackfillExtractionLite,
        temperature=0.1,
        store=False,  # CRITICAL: Privacy - never store
    )
    
    tokens_used = response.usage.total_tokens if response.usage else 0
    
    # Get parsed result (guaranteed to match schema)
    parsed = response.output_parsed
    
    if parsed is None:
        # Fallback on refusal or parse failure
        parsed = BackfillExtractionLite(summary="")
    
    return parsed, tokens_used


# ─────────────────────────────────────────────────────────────────────────────
# Note Processing
# ─────────────────────────────────────────────────────────────────────────────

# Cache for manifests (loaded once per run)
_manifest_cache: dict[str, str] | None = None


def get_manifests(vault: Path) -> dict[str, str]:
    """Get cached manifests or load them."""
    global _manifest_cache
    if _manifest_cache is None:
        _manifest_cache = load_manifests(vault)
    return _manifest_cache


def clear_manifest_cache() -> None:
    """Clear the manifest cache (for testing or after updates)."""
    global _manifest_cache
    _manifest_cache = None


def extract_note(
    client: OpenAI,
    note: NoteMetadata,
    entity_path: str,
    vault: Path,
    model: str = "gpt-4o-mini",
    manifests: dict[str, str] | None = None,
) -> BackfillExtraction | None:
    """
    Extract metadata from a single note.
    
    Uses structured outputs for guaranteed schema adherence.
    
    Args:
        client: OpenAI client
        note: Note metadata from scan
        entity_path: Parent entity folder path
        vault: Path to vault root
        model: Model to use (must support structured outputs)
        manifests: Entity manifests (loaded automatically if not provided)
    
    Returns:
        BackfillExtraction or None on failure
    """
    # Load manifests if not provided
    if manifests is None:
        manifests = get_manifests(vault)
    
    note_path = vault / note.path
    
    try:
        content = note_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"  Error reading {note.path}: {e}")
        return None
    
    # Skip very short notes
    if len(content.strip()) < 50:
        print(f"  Skipping {note.filename} (too short)")
        return None
    
    try:
        lite_result, tokens = extract_from_content(
            client=client,
            note_path=note.path,
            note_date=note.date,
            entity_name=Path(entity_path).name,
            content=content,
            model=model,
            manifests=manifests,
        )
    except Exception as e:
        print(f"  Error extracting {note.path}: {e}")
        return None
    
    # Check for tasks in content (legacy detection)
    has_tasks = "- [ ]" in content or "- [x]" in content or len(lite_result.tasks) > 0
    
    # Transform BackfillExtractionLite → BackfillExtraction with metadata
    return BackfillExtraction(
        note_path=note.path,
        entity_path=entity_path,
        date=note.date or "unknown",
        title=note.title or note.filename,
        suggested_title=lite_result.suggested_title,
        note_type=lite_result.note_type,
        summary=lite_result.summary,
        mentions=lite_result.mentions,
        key_facts=lite_result.key_facts,
        person_details={},  # Not in lite model
        project_details={},  # Not in lite model
        customer_details={},  # Not in lite model
        tasks=lite_result.tasks,
        decisions=lite_result.decisions,
        topics_discussed=lite_result.topics_discussed,
        cross_links=CrossLinks(),  # Not in lite model
        has_tasks=has_tasks,
        extracted_at=datetime.now(),
        model_used=model,
        tokens_used=tokens,
    )


# ─────────────────────────────────────────────────────────────────────────────
# Batch Processing
# ─────────────────────────────────────────────────────────────────────────────


def extract_batch(
    manifest: BackfillManifest,
    vault: Path | None = None,
    model: str = "gpt-4o-mini",
    limit: int | None = None,
    skip_existing: bool = False,
    output_dir: Path | None = None,
    verbose: bool = False,
) -> ExtractionBatch:
    """
    Extract metadata from all notes in a manifest.
    
    Args:
        manifest: Scan manifest with entities and notes
        vault: Path to vault root
        model: Model to use
        limit: Maximum notes to process (for testing)
        skip_existing: Skip notes already extracted
        output_dir: Directory to write individual extractions
    
    Returns:
        ExtractionBatch with all extractions
    """
    if vault is None:
        vault = Path(vault_root())
    
    client = get_client()
    
    extractions = []
    total_tokens = 0
    successful = 0
    failed = 0
    skipped = 0
    processed = 0
    
    # Collect all notes
    all_notes = []
    for entity in manifest.entities:
        for note in entity.notes:
            all_notes.append((entity.path, note))
    
    print(f"Processing {len(all_notes)} notes...")
    
    for entity_path, note in all_notes:
        if limit and processed >= limit:
            break
        
        # Check if already extracted
        if skip_existing and output_dir:
            note_hash = hashlib.md5(note.path.encode()).hexdigest()[:8]
            extraction_file = output_dir / f"{note_hash}.json"
            if extraction_file.exists():
                skipped += 1
                continue
        
        print(f"  [{processed + 1}/{len(all_notes)}] {note.filename}...")
        
        extraction = extract_note(
            client=client,
            note=note,
            entity_path=entity_path,
            vault=vault,
            model=model,
        )
        
        if extraction:
            extractions.append(extraction)
            total_tokens += extraction.tokens_used
            successful += 1
            
            # Write individual extraction if output dir specified
            if output_dir:
                output_dir.mkdir(parents=True, exist_ok=True)
                note_hash = hashlib.md5(note.path.encode()).hexdigest()[:8]
                extraction_file = output_dir / f"{note_hash}.json"
                with open(extraction_file, "w") as f:
                    json.dump(extraction.model_dump(mode="json"), f, indent=2, default=str)
        else:
            failed += 1
        
        processed += 1
    
    print("\nExtraction complete:")
    print(f"  Successful: {successful}")
    print(f"  Failed: {failed}")
    print(f"  Skipped: {skipped}")
    print(f"  Total tokens: {total_tokens}")
    
    return ExtractionBatch(
        version="1.0",
        extracted_at=datetime.now(),
        scope=manifest.scope,
        extractions=extractions,
        total_notes=len(all_notes),
        successful=successful,
        failed=failed,
        skipped=skipped,
        total_tokens=total_tokens,
    )


def extract_batch_parallel(
    manifest: BackfillManifest,
    vault: Path | None = None,
    model: str = "gpt-4o-mini",
    limit: int | None = None,
    skip_existing: bool = False,
    output_dir: Path | None = None,
    verbose: bool = False,
    max_workers: int = 5,
    progress_callback: Callable[[int, int, str], None] | None = None,
) -> ExtractionBatch:
    """
    Extract metadata from notes in parallel using ThreadPoolExecutor.
    
    Args:
        manifest: BackfillManifest with notes to process
        vault: Path to vault root (uses config if not provided)
        model: Model to use for extraction
        limit: Maximum notes to process
        skip_existing: Skip notes already extracted
        output_dir: Directory to save individual extractions
        verbose: Print detailed progress
        max_workers: Number of parallel extraction threads (default: 5)
        progress_callback: Optional callback(current, total, note_name)
    
    Returns:
        ExtractionBatch with all extractions
    """
    if vault is None:
        vault = vault_root()
    
    client = get_client()
    manifests = get_manifests(vault)
    
    # Collect all notes
    all_notes: list[tuple[str, NoteMetadata]] = []
    for entity in manifest.entities:
        for note in entity.notes:
            all_notes.append((entity.path, note))
    
    if limit:
        all_notes = all_notes[:limit]
    
    # Filter existing if needed
    if skip_existing and output_dir:
        filtered = []
        for entity_path, note in all_notes:
            note_hash = hashlib.md5(note.path.encode()).hexdigest()[:8]
            extraction_file = output_dir / f"{note_hash}.json"
            if not extraction_file.exists():
                filtered.append((entity_path, note))
        skipped_count = len(all_notes) - len(filtered)
        all_notes = filtered
    else:
        skipped_count = 0
    
    print(f"Processing {len(all_notes)} notes with {max_workers} parallel workers...")
    
    # Thread-safe counters
    results: list[BackfillExtraction | None] = [None] * len(all_notes)
    
    def extract_one(idx: int, entity_path: str, note: NoteMetadata) -> tuple[int, BackfillExtraction | None]:
        """Extract a single note (runs in thread)."""
        try:
            extraction = extract_note(
                client=client,
                note=note,
                entity_path=entity_path,
                vault=vault,
                model=model,
                manifests=manifests,
            )
            return idx, extraction
        except Exception as e:
            if verbose:
                print(f"  Error extracting {note.filename}: {e}")
            return idx, None
    
    successful = 0
    failed = 0
    total_tokens = 0
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all tasks
        futures = {
            executor.submit(extract_one, i, ep, n): (i, ep, n)
            for i, (ep, n) in enumerate(all_notes)
        }
        
        # Process as completed
        completed = 0
        for future in as_completed(futures):
            i, entity_path, note = futures[future]
            completed += 1
            
            try:
                idx, extraction = future.result()
                results[idx] = extraction
                
                if extraction:
                    successful += 1
                    total_tokens += extraction.tokens_used
                    
                    # Write individual extraction if output dir specified
                    if output_dir:
                        output_dir.mkdir(parents=True, exist_ok=True)
                        note_hash = hashlib.md5(note.path.encode()).hexdigest()[:8]
                        extraction_file = output_dir / f"{note_hash}.json"
                        with open(extraction_file, "w") as f:
                            json.dump(extraction.model_dump(mode="json"), f, indent=2, default=str)
                else:
                    failed += 1
                
                if verbose:
                    status = "✓" if extraction else "✗"
                    print(f"  [{completed}/{len(all_notes)}] {status} {note.filename}")
                
                if progress_callback:
                    progress_callback(completed, len(all_notes), note.filename)
                    
            except Exception as e:
                failed += 1
                if verbose:
                    print(f"  [{completed}/{len(all_notes)}] ✗ {note.filename}: {e}")
    
    # Filter None results
    extractions = [r for r in results if r is not None]
    
    print("\nParallel extraction complete:")
    print(f"  Successful: {successful}")
    print(f"  Failed: {failed}")
    print(f"  Skipped: {skipped_count}")
    print(f"  Total tokens: {total_tokens}")
    
    return ExtractionBatch(
        version="1.0",
        extracted_at=datetime.now(),
        scope=manifest.scope,
        extractions=extractions,
        total_notes=len(all_notes) + skipped_count,
        successful=successful,
        failed=failed,
        skipped=skipped_count,
        total_tokens=total_tokens,
    )


def save_extractions(batch: ExtractionBatch, path: Path) -> None:
    """Save ExtractionBatch to JSON file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(path, "w") as f:
        json.dump(batch.model_dump(mode="json"), f, indent=2, default=str)
    
    print(f"Saved {len(batch.extractions)} extractions to: {path}")


def load_extractions(extraction_dir: Path) -> list[BackfillExtraction]:
    """Load all extractions from a directory."""
    extractions = []
    
    for file in extraction_dir.glob("*.json"):
        try:
            with open(file) as f:
                data = json.load(f)
            extractions.append(BackfillExtraction(**data))
        except Exception as e:
            print(f"Warning: Could not load {file}: {e}")
    
    return extractions


# ─────────────────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Extract metadata from notes")
    parser.add_argument("--manifest", required=True, help="Input manifest JSON")
    parser.add_argument("-o", "--output", required=True, help="Output directory for extractions")
    parser.add_argument("--model", default="gpt-4o-mini", help="Model to use (default: gpt-4o-mini)")
    parser.add_argument("--limit", type=int, help="Limit number of notes to process")
    parser.add_argument("--skip-existing", action="store_true", help="Skip already extracted")
    
    args = parser.parse_args()
    
    # Load manifest
    with open(args.manifest) as f:
        manifest_data = json.load(f)
    manifest = BackfillManifest(**manifest_data)
    
    # Extract
    batch = extract_batch(
        manifest=manifest,
        model=args.model,
        limit=args.limit,
        skip_existing=args.skip_existing,
        output_dir=Path(args.output),
    )
    
    # Write batch summary
    summary_file = Path(args.output) / "_batch_summary.json"
    with open(summary_file, "w") as f:
        json.dump(batch.model_dump(mode="json"), f, indent=2, default=str)
    
    print(f"\nWrote batch summary to {summary_file}")
