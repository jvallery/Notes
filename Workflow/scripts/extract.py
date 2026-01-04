#!/usr/bin/env python3
"""
Extract Phase: Raw content → ExtractionV1 JSON

Scans Inbox folders for unprocessed files, classifies them,
and extracts structured data using OpenAI Structured Outputs.

Usage:
    # Extract single file
    python scripts/extract.py --file "Inbox/Transcripts/meeting.md"
    
    # Extract all pending transcripts
    python scripts/extract.py --all --scope transcripts
    
    # Extract all pending emails
    python scripts/extract.py --all --scope email
    
    # Dry run (show what would be extracted)
    python scripts/extract.py --all --dry-run

CRITICAL: Always uses store=False for privacy compliance.
"""

import sys
from datetime import datetime, date, timedelta
from pathlib import Path

import click

# Add Workflow to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from models.extraction import ExtractionV1
from scripts.utils.config import load_config, workflow_root, vault_root
from scripts.utils.paths import get_extraction_path, ensure_parent_exists
from scripts.utils.fs import safe_read_text, atomic_write
from scripts.utils.profiles import load_profile, select_profile
from scripts.utils.entities import list_all_entity_names
from scripts.utils.openai_client import get_client, parse_structured, check_api_key, OpenAIError
from scripts.utils.templates import get_prompts_env
from scripts.classify import classify


def find_unprocessed(scope: str = "transcripts") -> list[Path]:
    """
    Find files without corresponding .extraction.json and not in archive.
    
    A file is considered "processed" if:
    1. It has a .extraction.json in _extraction/
    2. OR it exists in _archive/ (fully completed)
    
    Args:
        scope: "transcripts" or "email"
        
    Returns:
        List of paths to unprocessed files
    """
    config = load_config()
    vr = vault_root()
    
    # Get scope path from config
    inbox_config = config.get("paths", {}).get("inbox", {})
    scope_paths = {
        "transcripts": inbox_config.get("transcripts", "Inbox/Transcripts"),
        "email": inbox_config.get("email", "Inbox/Email"),
    }
    
    scope_path = vr / scope_paths.get(scope, scope_paths["transcripts"])
    
    if not scope_path.exists():
        return []
    
    # Get archive base for checking already-processed
    archive_base = vr / inbox_config.get("archive", "Inbox/_archive")
    
    unprocessed = []
    for f in scope_path.glob("*.md"):
        # Skip if extraction exists
        extraction_path = get_extraction_path(vr, f)
        if extraction_path.exists():
            continue
        
        # Skip if already in archive (check all date folders)
        if archive_base.exists():
            in_archive = False
            for date_dir in archive_base.iterdir():
                if date_dir.is_dir() and (date_dir / f.name).exists():
                    in_archive = True
                    break
            if in_archive:
                continue
        
        unprocessed.append(f)
    
    return sorted(unprocessed)


def is_already_processed(source: Path) -> bool:
    """
    Check if a source file has already been processed.
    
    A file is considered processed if:
    1. It has a corresponding extraction in _extraction/
    2. OR it exists in _archive/
    
    Args:
        source: Path to the source file
        
    Returns:
        True if already processed, False otherwise
    """
    config = load_config()
    vr = vault_root()
    
    # Check extraction exists
    extraction_path = get_extraction_path(vr, source)
    if extraction_path.exists():
        return True
    
    # Check in any archive folder
    inbox_config = config.get("paths", {}).get("inbox", {})
    archive_base = vr / inbox_config.get("archive", "Inbox/_archive")
    
    if archive_base.exists():
        for date_dir in archive_base.iterdir():
            if date_dir.is_dir() and (date_dir / source.name).exists():
                return True
    
    return False


def build_extraction_prompt(
    source_type: str,
    profile: dict,
    entity_names: dict,
    source_file: str,
    content: str,
) -> tuple[str, str]:
    """
    Build the extraction system and user prompts.
    
    Returns:
        Tuple of (system_prompt, user_content)
    """
    env = get_prompts_env()
    
    today = date.today()
    tomorrow = today + timedelta(days=1)
    next_week = today + timedelta(days=7)
    
    # Build context for prompt
    context = {
        # Date context
        "current_date": today.isoformat(),
        "tomorrow": tomorrow.isoformat(),
        "next_week": next_week.isoformat(),
        
        # Entity context (limit to prevent context explosion)
        "known_entities": {
            "people": entity_names.get("people", [])[:50],
            "accounts": entity_names.get("accounts", [])[:20],
            "projects": entity_names.get("projects", [])[:20],
        },
        
        # Profile context
        "profile_name": profile.get("name", "Default"),
        "profile_description": profile.get("description", ""),
        "profile_focus": profile.get("focus", []),
        "profile_ignore": profile.get("ignore", []),
        "task_rules": profile.get("task_rules", {}),
        
        # Source context
        "source_file": source_file,
        "content_type": source_type,
        "content": content,
    }
    
    template = env.get_template("system-extractor.md.j2")
    system_prompt = template.render(**context)
    
    # User content is just the raw content (already in prompt via template)
    # But we need to return it for the API call format
    user_content = "Please extract structured information from the content provided above."
    
    return system_prompt, user_content


def extract_file(source: Path, client) -> tuple[ExtractionV1, dict]:
    """
    Extract structured data from a single file.
    
    Args:
        source: Path to source file
        client: OpenAI client
        
    Returns:
        Tuple of (ExtractionV1, metadata)
    """
    config = load_config()
    vr = vault_root()
    
    # Read content
    content = safe_read_text(source)
    if not content:
        raise ValueError(f"Empty or unreadable file: {source}")
    
    # Determine source type
    source_str = str(source)
    source_type = "transcript" if "Transcripts" in source_str else "email"
    
    # Classify to select profile
    classification = classify(source_str, content)
    profile_name = select_profile(
        classification.get("likely_domain_path_prefix", source_str),
        note_type=classification.get("note_type")
    )
    profile = load_profile(profile_name)
    
    # Get entity context
    entity_names = list_all_entity_names()
    
    # Build prompts
    relative_path = str(source.relative_to(vr)) if source.is_absolute() else str(source)
    system_prompt, user_content = build_extraction_prompt(
        source_type=source_type,
        profile=profile,
        entity_names=entity_names,
        source_file=relative_path,
        content=content,
    )
    
    # Get model config
    models_config = config.get("models", {})
    model_key = f"extract_{source_type}"
    model_config = models_config.get(model_key, models_config.get("extract_transcript", {}))
    model_name = model_config.get("model", "gpt-4o")
    temperature = model_config.get("temperature", 0.0)
    
    # Call OpenAI with structured output
    extraction, metadata = parse_structured(
        client=client,
        model=model_name,
        system_prompt=system_prompt,
        user_content=user_content,
        response_model=ExtractionV1,
        temperature=temperature,
    )
    
    # Set system fields
    extraction.source_file = relative_path
    extraction.processed_at = datetime.now()
    
    # Add profile info to metadata
    metadata["profile"] = profile_name
    metadata["classification"] = classification
    
    return extraction, metadata


def save_extraction(extraction: ExtractionV1, output_path: Path) -> None:
    """Save extraction JSON to disk."""
    ensure_parent_exists(output_path)
    json_str = extraction.model_dump_json(indent=2)
    atomic_write(output_path, json_str)


@click.command()
@click.option(
    "--file", "file_path",
    type=click.Path(exists=True),
    help="Extract single file"
)
@click.option(
    "--all", "extract_all",
    is_flag=True,
    help="Extract all pending files"
)
@click.option(
    "--scope",
    default="transcripts",
    type=click.Choice(["transcripts", "email"]),
    help="Scope for --all (default: transcripts)"
)
@click.option(
    "--dry-run",
    is_flag=True,
    help="Show what would be extracted without processing"
)
@click.option(
    "--verbose", "-v",
    is_flag=True,
    help="Show detailed output"
)
def main(
    file_path: str | None,
    extract_all: bool,
    scope: str,
    dry_run: bool,
    verbose: bool
):
    """Extract structured data from inbox content using OpenAI."""
    
    # Determine files to process
    if file_path:
        files = [Path(file_path)]
    elif extract_all:
        files = find_unprocessed(scope)
    else:
        click.echo("Error: Specify --file <path> or --all", err=True)
        click.echo("Run with --help for usage.", err=True)
        sys.exit(1)
    
    if not files:
        click.echo("No files to process.")
        return
    
    click.echo(f"Found {len(files)} file(s) to extract")
    
    if dry_run:
        click.echo("\nDry run - would extract:")
        for f in files:
            click.echo(f"  • {f.name}")
        return
    
    # Check API key
    if not check_api_key():
        click.echo(
            "Error: OPENAI_API_KEY not set.\n"
            "Set it with: export OPENAI_API_KEY=sk-...",
            err=True
        )
        sys.exit(1)
    
    # Create client
    try:
        client = get_client()
    except OpenAIError as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)
    
    # Process files
    success_count = 0
    error_count = 0
    
    for f in files:
        try:
            click.echo(f"\nExtracting: {f.name}")
            
            extraction, metadata = extract_file(f, client)
            
            output_path = get_extraction_path(vault_root(), f)
            save_extraction(extraction, output_path)
            
            success_count += 1
            
            # Show results
            latency = metadata.get("latency_ms", "?")
            tokens = metadata.get("total_tokens", "?")
            profile = metadata.get("profile", "?")
            
            click.echo(f"  ✓ {output_path.name}")
            click.echo(f"    Type: {extraction.note_type}, Entity: {extraction.entity_name or 'N/A'}")
            click.echo(f"    Tasks: {len(extraction.tasks)}, Decisions: {len(extraction.decisions)}")
            
            if verbose:
                click.echo(f"    Profile: {profile}")
                click.echo(f"    Latency: {latency}ms, Tokens: {tokens}")
                if extraction.warnings:
                    for w in extraction.warnings:
                        click.echo(f"    ⚠ {w}")
                        
        except Exception as e:
            error_count += 1
            click.echo(f"  ✗ Error: {e}", err=True)
            if verbose:
                import traceback
                traceback.print_exc()
    
    # Summary
    click.echo(f"\n{'='*40}")
    click.echo(f"Completed: {success_count} success, {error_count} errors")


if __name__ == "__main__":
    main()
