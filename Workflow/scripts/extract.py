#!/usr/bin/env python3
"""
Extract Phase: Raw content → Structured JSON

Scans Inbox folders for unprocessed files, classifies them,
and extracts structured data using OpenAI API.

Uses OpenAI Responses API with store=False for privacy.
"""

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

import click
from jinja2 import Environment, FileSystemLoader
from openai import OpenAI
from rich.console import Console
from rich.progress import track

sys.path.insert(0, str(Path(__file__).parent))
from utils import load_config, get_model_config, get_persona, vault_root, workflow_root


def get_glossary_context() -> str:
    """Load the people/projects/customers glossary for prompt context."""
    try:
        from utils.cached_prompts import get_glossary_context as _get_glossary
        return _get_glossary(compact=True)  # Compact for extraction (less tokens)
    except ImportError:
        return ""


console = Console()


def get_openai_client():
    """Get configured OpenAI client with logging instrumentation."""
    from utils.ai_client import get_openai_client as get_instrumented_client
    return get_instrumented_client("extract")


def get_jinja_env() -> Environment:
    """Get Jinja2 environment for prompts."""
    return Environment(
        loader=FileSystemLoader(workflow_root() / "prompts"),
        trim_blocks=True,
        lstrip_blocks=True,
    )


def _content_hash(file_path: Path) -> str:
    """
    Generate a content hash for duplicate detection.
    
    Uses first 2000 chars after stripping frontmatter and whitespace.
    This catches transcripts that were exported multiple times.
    """
    import hashlib
    
    content = file_path.read_text()
    
    # Strip frontmatter if present
    if content.startswith("---"):
        end = content.find("\n---", 3)
        if end != -1:
            content = content[end + 4:]
    
    # Normalize: strip whitespace, take first 2000 chars
    normalized = content.strip()[:2000]
    
    return hashlib.md5(normalized.encode()).hexdigest()[:12]


def _build_content_hash_index(extraction_dir: Path, inbox_root: Path) -> dict[str, str]:
    """
    Build index of content hashes for already-processed files.
    
    Returns: {hash: original_filename, ...}
    """
    if not extraction_dir.exists():
        return {}
    
    index = {}
    
    for extraction_file in extraction_dir.glob("*.extraction.json"):
        # Find the original source file
        source_stem = extraction_file.stem.replace(".extraction", "")
        
        # Check all inbox folders
        for folder in ["Transcripts", "Email", "Voice", "Attachments"]:
            source_path = inbox_root / folder / f"{source_stem}.md"
            if source_path.exists():
                content_hash = _content_hash(source_path)
                index[content_hash] = source_stem
                break
    
    return index


def find_unprocessed_files() -> list[Path]:
    """
    Find files in Inbox that haven't been processed.
    
    Uses two checks:
    1. Already extracted: extraction JSON exists for this file
    2. Content duplicate: same content already processed (different filename)
    """

    config = load_config()
    root = vault_root()

    inbox_folders = [
        root / "Inbox" / "Transcripts",
        root / "Inbox" / "Email",
        root / "Inbox" / "Voice",
        root / "Inbox" / "Attachments",
    ]

    extraction_dir = root / "Inbox" / "_extraction"
    
    # Build content hash index
    processed_hashes = _build_content_hash_index(extraction_dir, root / "Inbox")

    unprocessed = []
    duplicates = []

    for folder in inbox_folders:
        if not folder.exists():
            continue

        for file in folder.glob("*.md"):
            # Skip if extraction already exists
            extraction_file = extraction_dir / f"{file.stem}.extraction.json"
            if extraction_file.exists():
                continue

            # Check if content is a duplicate
            content_hash = _content_hash(file)
            if content_hash in processed_hashes:
                duplicates.append((file, processed_hashes[content_hash]))
                continue

            unprocessed.append(file)
    
    # Report duplicates (silent unless verbose mode is enabled elsewhere)
    if duplicates:
        logger = logging.getLogger(__name__)
        logger.info(f"Skipping {len(duplicates)} duplicate files")
        for dup, original in duplicates[:5]:
            logger.debug(f"  {dup.name} = {original}")

    return sorted(unprocessed, key=lambda p: p.name)


def classify_content(content: str, filename: str, client: OpenAI) -> dict:
    """Classify content to determine note type."""

    model_config = get_model_config("classification")

    system_prompt = """You are a content classifier for a personal knowledge management system.
    
Analyze the content and filename to determine:
1. note_type: One of [customer, people, projects, rob, journal, partners, travel]
2. sub_type: Optional subcategory (e.g., "technical" or "leadership" for rob)
3. entities: Detected mentions of people, accounts, and projects
4. confidence: Your confidence in the classification (0.0-1.0)

Return valid JSON only, no markdown fencing."""

    user_prompt = f"""Filename: {filename}

Content (first 4000 chars):
{content[:4000]}"""

    try:
        response = client.chat.completions.create(
            model=model_config["model"],
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            response_format={"type": "json_object"},
            temperature=model_config["temperature"],
        )

        return json.loads(response.choices[0].message.content)

    except Exception as e:
        console.print(f"[red]Classification failed: {e}[/red]")
        return {
            "note_type": "journal",  # Safe fallback
            "sub_type": None,
            "entities": {"people": [], "accounts": [], "projects": []},
            "confidence": 0.0,
            "error": str(e),
        }


def extract_content(
    content: str,
    filename: str,
    classification: dict,
    client: OpenAI,
    jinja_env: Environment,
) -> dict:
    """Extract structured data from content."""

    config = load_config()
    model_config = get_model_config("extraction")

    # Get profile for this note type
    from utils import select_profile, load_profile, get_task_rules
    note_type = classification.get("note_type", "journal")
    profile_name = select_profile("", note_type)
    profile = load_profile(profile_name)

    # Build extraction prompt
    template = jinja_env.get_template("system-extractor.md.j2")
    tomorrow = (datetime.now() + __import__('datetime').timedelta(days=1)).strftime("%Y-%m-%d")
    next_week = (datetime.now() + __import__('datetime').timedelta(days=7)).strftime("%Y-%m-%d")
    
    # Get glossary context for entity resolution
    glossary = get_glossary_context()
    
    system_prompt_template = template.render(
        current_date=datetime.now().strftime("%Y-%m-%d"),
        tomorrow=tomorrow,
        next_week=next_week,
        profile_name=profile.get("name", profile_name),
        profile_description=profile.get("description", ""),
        profile_focus=profile.get("focus", []),
        profile_ignore=profile.get("ignore", []),
        task_rules=profile.get("task_rules", {}),
        known_entities=classification.get("entities", {}),
    )
    
    # Build final system prompt with glossary first (for prompt caching)
    if glossary:
        system_prompt = f"""## ENTITY GLOSSARY
{glossary}

{system_prompt_template}"""
    else:
        system_prompt = system_prompt_template

    user_prompt = f"""Source file: {filename}
Classification: {json.dumps(classification)}

Content:
{content}"""

    try:
        response = client.chat.completions.create(
            model=model_config["model"],
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            response_format={"type": "json_object"},
            temperature=model_config["temperature"],
        )

        return json.loads(response.choices[0].message.content)

    except Exception as e:
        console.print(f"[red]Extraction failed: {e}[/red]")
        return {
            "error": str(e),
            "summary": "",
            "tasks": [],
            "decisions": [],
            "follow_ups": [],
            "participants": [],
            "key_facts": [],
        }


def save_extraction(source_file: Path, classification: dict, extraction: dict) -> Path:
    """Save extraction result to JSON file."""

    extraction_dir = vault_root() / "Inbox" / "_extraction"
    extraction_dir.mkdir(parents=True, exist_ok=True)

    output = {
        "version": "1.0",
        "source_file": str(source_file.relative_to(vault_root())),
        "processed_at": datetime.now().isoformat(),
        "classification": classification,
        "extraction": extraction,
    }

    output_path = extraction_dir / f"{source_file.stem}.extraction.json"

    with open(output_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    return output_path


@click.command()
@click.option(
    "--file",
    "-f",
    "single_file",
    type=click.Path(exists=True),
    help="Process a single file instead of scanning Inbox",
)
@click.option(
    "--dry-run", is_flag=True, help="Show what would be processed without doing it"
)
@click.option("--verbose", "-v", is_flag=True, help="Show detailed output")
def main(single_file: Optional[str], dry_run: bool, verbose: bool):
    """Extract structured data from Inbox files."""

    console.print("[bold blue]Extract Phase[/bold blue]")
    console.print("=" * 40)

    # Find files to process
    if single_file:
        files = [Path(single_file)]
    else:
        files = find_unprocessed_files()

    if not files:
        console.print("[yellow]No unprocessed files found.[/yellow]")
        return

    console.print(f"Found [bold]{len(files)}[/bold] files to process")

    if dry_run:
        for f in files:
            console.print(f"  Would process: {f.name}")
        return

    # Initialize clients
    client = get_openai_client()
    jinja_env = get_jinja_env()

    # Process files
    results = {"success": [], "failed": []}

    for file in track(files, description="Extracting..."):
        try:
            content = file.read_text()

            if verbose:
                console.print(f"\n[dim]Processing: {file.name}[/dim]")

            # Classify
            classification = classify_content(content, file.name, client)
            if verbose:
                console.print(f"  Type: {classification.get('note_type')}")

            # Extract
            extraction = extract_content(
                content, file.name, classification, client, jinja_env
            )

            # Save
            output_path = save_extraction(file, classification, extraction)
            results["success"].append(str(output_path))

            if verbose:
                console.print(f"  [green]→ {output_path.name}[/green]")

        except Exception as e:
            results["failed"].append({"file": str(file), "error": str(e)})
            console.print(f"[red]Failed: {file.name} - {e}[/red]")

    # Summary
    console.print("\n" + "=" * 40)
    console.print(f"[green]Success: {len(results['success'])}[/green]")
    console.print(f"[red]Failed: {len(results['failed'])}[/red]")


if __name__ == "__main__":
    main()
