"""
Backfill Extractor: AI extraction for existing notes.

Uses the model specified in config.yaml (models.backfill) to extract
summaries and mentions from existing notes for populating README context.
"""

import hashlib
import json
import os
from datetime import datetime
from pathlib import Path

from openai import OpenAI

from . import (
    BackfillExtraction,
    BackfillManifest,
    ExtractionBatch,
    Mentions,
    NoteMetadata,
    PersonDetails,
    ExtractedTask,
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


def render_prompt(note_path: str, note_date: str | None, entity_name: str, content: str) -> str:
    """Render the extraction prompt with note context."""
    template_str = get_prompt_template()
    
    # Simple string replacement (not full Jinja for speed)
    prompt = template_str.replace("{{ note_path }}", note_path)
    prompt = prompt.replace("{{ note_date | default('Unknown') }}", note_date or "Unknown")
    prompt = prompt.replace("{{ entity_name | default('Unknown') }}", entity_name)
    prompt = prompt.replace("{{ content }}", content)
    
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
    model: str = "gpt-5.2",
) -> tuple[dict, int]:
    """
    Call OpenAI to extract metadata from note content.
    
    Returns:
        Tuple of (extraction_dict, tokens_used)
    """
    prompt = render_prompt(note_path, note_date, entity_name, content)
    
    # Truncate very long content
    max_content_chars = 8000
    if len(content) > max_content_chars:
        content = content[:max_content_chars] + "\n\n[Content truncated...]"
        prompt = render_prompt(note_path, note_date, entity_name, content)
    
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You extract rich structured data from notes. Return valid JSON only."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.1,
        max_completion_tokens=2000,  # Increased for rich extraction
        # CRITICAL: Privacy - don't store
        store=False,
    )
    
    # Parse response
    response_text = response.choices[0].message.content.strip()
    
    # Handle markdown code fences
    if response_text.startswith("```"):
        lines = response_text.split("\n")
        # Remove first and last lines (fences)
        response_text = "\n".join(lines[1:-1])
    
    tokens_used = response.usage.total_tokens if response.usage else 0
    
    try:
        result = json.loads(response_text)
    except json.JSONDecodeError:
        # Return empty extraction on parse failure
        result = {
            "summary": "",
            "mentions": {"people": [], "projects": [], "accounts": []},
            "person_details": {},
            "tasks": [],
            "decisions": [],
            "key_facts": [],
            "topics_discussed": [],
        }
    
    return result, tokens_used


# ─────────────────────────────────────────────────────────────────────────────
# Note Processing
# ─────────────────────────────────────────────────────────────────────────────


def extract_note(
    client: OpenAI,
    note: NoteMetadata,
    entity_path: str,
    vault: Path,
    model: str = "gpt-5.2",
) -> BackfillExtraction | None:
    """
    Extract metadata from a single note.
    
    Args:
        client: OpenAI client
        note: Note metadata from scan
        entity_path: Parent entity folder path
        vault: Path to vault root
        model: Model to use
    
    Returns:
        BackfillExtraction or None on failure
    """
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
        result, tokens = extract_from_content(
            client=client,
            note_path=note.path,
            note_date=note.date,
            entity_name=Path(entity_path).name,
            content=content,
            model=model,
        )
    except Exception as e:
        print(f"  Error extracting {note.path}: {e}")
        return None
    
    # Build mentions
    mentions_data = result.get("mentions", {})
    mentions = Mentions(
        people=mentions_data.get("people", []),
        projects=mentions_data.get("projects", []),
        accounts=mentions_data.get("accounts", []),
    )
    
    # Parse person details
    person_details_raw = result.get("person_details", {})
    person_details = {}
    for name, details in person_details_raw.items():
        if isinstance(details, dict):
            person_details[name] = PersonDetails(**details)
    
    # Parse tasks
    tasks_raw = result.get("tasks", [])
    tasks = []
    for task_data in tasks_raw:
        if isinstance(task_data, dict) and task_data.get("text"):
            tasks.append(ExtractedTask(**task_data))
    
    # Check for tasks in content (legacy)
    has_tasks = "- [ ]" in content or "- [x]" in content or len(tasks) > 0
    
    return BackfillExtraction(
        note_path=note.path,
        entity_path=entity_path,
        date=note.date or "unknown",
        title=note.title or note.filename,
        summary=result.get("summary", ""),
        mentions=mentions,
        key_facts=result.get("key_facts", []),
        person_details=person_details,
        tasks=tasks,
        decisions=result.get("decisions", []),
        topics_discussed=result.get("topics_discussed", []),
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
    model: str = "gpt-5.2",
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
    parser.add_argument("--model", default="gpt-5.2", help="Model to use (default: gpt-5.2)")
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
