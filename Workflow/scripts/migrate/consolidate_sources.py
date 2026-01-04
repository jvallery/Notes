#!/usr/bin/env python3
"""
Consolidate Sources Migration

Moves existing dated notes from entity folders to Sources/Transcripts/YYYY/
and updates entity READMEs with wikilinks.

Usage:
    python scripts/migrate/consolidate_sources.py --dry-run
    python scripts/migrate/consolidate_sources.py --execute
"""

import argparse
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

import yaml

# Add parent directories to path
SCRIPTS_DIR = Path(__file__).parent.parent
WORKFLOW_DIR = SCRIPTS_DIR.parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))
if str(WORKFLOW_DIR) not in sys.path:
    sys.path.insert(0, str(WORKFLOW_DIR))

from utils.config import vault_root


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Parse YAML frontmatter from markdown content."""
    if not content.startswith("---"):
        return {}, content
    
    end = content.find("\n---", 3)
    if end == -1:
        return {}, content
    
    fm_text = content[4:end]
    body = content[end + 4:].lstrip("\n")
    
    try:
        fm = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError:
        fm = {}
    
    return fm, body


def serialize_frontmatter(fm: dict) -> str:
    """Serialize frontmatter dict to YAML string."""
    return "---\n" + yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False) + "---\n"


def extract_date_from_filename(filename: str) -> str | None:
    """Extract date from filename like '2025-10-28 - Title.md'."""
    match = re.match(r"(\d{4}-\d{2}-\d{2})", filename)
    if match:
        return match.group(1)
    
    # Try YYYY-MM format
    match = re.match(r"(\d{4}-\d{2})\s*-", filename)
    if match:
        return match.group(1) + "-01"  # Assume first of month
    
    return None


def extract_year_from_date(date_str: str) -> str:
    """Extract year from date string."""
    if date_str and len(date_str) >= 4:
        return date_str[:4]
    return str(datetime.now().year)


def find_dated_notes(vault: Path, scope: str = "VAST") -> list[dict]:
    """Find all dated notes in entity folders."""
    notes = []
    scope_path = vault / scope
    
    if not scope_path.exists():
        return notes
    
    # Pattern for dated files: 2024-*, 2025-*, 2026-*, etc.
    for md_file in scope_path.rglob("*.md"):
        # Skip README files
        if md_file.name == "README.md":
            continue
        
        # Skip manifest files
        if md_file.name.startswith("_"):
            continue
        
        # Check if filename starts with a date pattern
        if not re.match(r"\d{4}", md_file.name):
            continue
        
        date = extract_date_from_filename(md_file.name)
        if not date:
            continue
        
        # Determine entity type from path
        rel_path = md_file.relative_to(scope_path)
        parts = list(rel_path.parts)
        
        entity_type = None
        entity_name = None
        
        if parts[0] == "People":
            entity_type = "people"
            entity_name = parts[1] if len(parts) > 1 else None
        elif parts[0] == "Customers and Partners":
            entity_type = "customers"
            entity_name = parts[1] if len(parts) > 1 else None
        elif parts[0] == "Projects":
            entity_type = "projects"
            entity_name = parts[1] if len(parts) > 1 else None
        
        notes.append({
            "path": md_file,
            "filename": md_file.name,
            "date": date,
            "year": extract_year_from_date(date),
            "entity_type": entity_type,
            "entity_name": entity_name,
            "scope": scope,
        })
    
    return notes


def generate_source_path(vault: Path, note: dict) -> Path:
    """Generate the destination path in Sources/."""
    # Determine source type (assume transcript for now)
    source_type = "Transcripts"
    
    return vault / "Sources" / source_type / note["year"] / note["filename"]


def add_entity_wikilinks(fm: dict, note: dict) -> dict:
    """Add entity wikilinks to frontmatter."""
    # Ensure entities dict exists
    if "entities" not in fm:
        fm["entities"] = {}
    
    # Add the primary entity
    if note["entity_type"] and note["entity_name"]:
        entity_key = note["entity_type"]
        if entity_key not in fm["entities"]:
            fm["entities"][entity_key] = []
        
        wikilink = f"[[{note['entity_name']}]]"
        if wikilink not in fm["entities"][entity_key]:
            fm["entities"][entity_key].append(wikilink)
    
    # Mark as source document
    fm["type"] = "transcript"
    fm["source_type"] = fm.get("source_type", "unknown")
    
    # Ensure date is set
    if "date" not in fm:
        fm["date"] = note["date"]
    
    return fm


def generate_readme_entry(source_path: Path, vault: Path, summary: str = "") -> str:
    """Generate a one-liner for README Recent Context."""
    rel_path = source_path.relative_to(vault)
    
    # Extract date from filename
    date_match = re.match(r"(\d{4}-\d{2}-\d{2})", source_path.name)
    date = date_match.group(1) if date_match else "unknown"
    
    # Create display title (filename without date prefix and extension)
    display_title = re.sub(r"^\d{4}-\d{2}(-\d{2})?\s*-?\s*", "", source_path.stem)
    if not display_title:
        display_title = source_path.stem
    
    # Truncate summary
    if summary:
        summary = summary[:100] + "..." if len(summary) > 100 else summary
        return f"- {date}: [[{rel_path}|{display_title}]] — {summary}\n"
    else:
        return f"- {date}: [[{rel_path}|{display_title}]]\n"


def extract_summary_from_content(content: str) -> str:
    """Extract summary from note content."""
    # Look for ## Summary section
    match = re.search(r"## Summary\s*\n+([^\n#]+)", content)
    if match:
        return match.group(1).strip()
    
    # Fallback: first non-empty line after frontmatter
    lines = content.split("\n")
    for line in lines:
        line = line.strip()
        if line and not line.startswith("#") and not line.startswith(">"):
            return line[:150]
    
    return ""


def update_readme_with_link(
    readme_path: Path,
    source_path: Path,
    vault: Path,
    summary: str,
    dry_run: bool = True,
) -> bool:
    """Add a wikilink entry to README's Recent Context section."""
    if not readme_path.exists():
        return False
    
    content = readme_path.read_text()
    entry = generate_readme_entry(source_path, vault, summary)
    
    # Find Recent Context section
    if "## Recent Context" not in content:
        # Add section if missing
        content += "\n\n## Recent Context\n\n"
    
    # Check if this source is already linked
    rel_path = source_path.relative_to(vault)
    if str(rel_path) in content:
        return False  # Already linked
    
    # Insert entry after "## Recent Context" header
    insert_point = content.find("## Recent Context") + len("## Recent Context")
    # Find end of line
    newline_point = content.find("\n", insert_point)
    if newline_point == -1:
        newline_point = len(content)
    
    new_content = content[:newline_point + 1] + "\n" + entry + content[newline_point + 1:]
    
    if not dry_run:
        readme_path.write_text(new_content)
    
    return True


def migrate_note(
    vault: Path,
    note: dict,
    dry_run: bool = True,
) -> dict:
    """Migrate a single dated note to Sources."""
    result = {
        "source": note["path"],
        "destination": None,
        "readme_updated": False,
        "error": None,
    }
    
    try:
        # Read note content
        content = note["path"].read_text()
        fm, body = parse_frontmatter(content)
        
        # Add entity wikilinks to frontmatter
        fm = add_entity_wikilinks(fm, note)
        
        # Generate destination path
        dest_path = generate_source_path(vault, note)
        result["destination"] = dest_path
        
        # Check for conflicts
        if dest_path.exists():
            # Add suffix
            stem = dest_path.stem
            suffix = 1
            while dest_path.exists():
                dest_path = dest_path.parent / f"{stem} ({suffix}).md"
                suffix += 1
            result["destination"] = dest_path
        
        # Extract summary
        summary = extract_summary_from_content(body)
        if not summary and fm.get("summary"):
            summary = fm["summary"]
        
        # Prepare new content
        new_content = serialize_frontmatter(fm) + "\n" + body
        
        if not dry_run:
            # Ensure destination directory exists
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Write to destination
            dest_path.write_text(new_content)
            
            # Delete original
            note["path"].unlink()
        
        # Update README with link
        if note["entity_name"]:
            scope_path = vault / note["scope"]
            
            if note["entity_type"] == "people":
                readme_path = scope_path / "People" / note["entity_name"] / "README.md"
            elif note["entity_type"] == "customers":
                readme_path = scope_path / "Customers and Partners" / note["entity_name"] / "README.md"
            elif note["entity_type"] == "projects":
                readme_path = scope_path / "Projects" / note["entity_name"] / "README.md"
            else:
                readme_path = None
            
            if readme_path and readme_path.exists():
                result["readme_updated"] = update_readme_with_link(
                    readme_path, dest_path, vault, summary, dry_run
                )
    
    except Exception as e:
        result["error"] = str(e)
    
    return result


def main():
    parser = argparse.ArgumentParser(
        description="Migrate dated notes to Sources/ folder structure"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without making changes",
    )
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Execute the migration",
    )
    parser.add_argument(
        "--scope",
        default="VAST",
        help="Scope to migrate (default: VAST)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Limit number of notes to process",
    )
    
    args = parser.parse_args()
    
    if not args.dry_run and not args.execute:
        print("Use --dry-run to preview or --execute to run")
        return 1
    
    dry_run = not args.execute
    vault = vault_root()
    
    print(f"{'DRY RUN: ' if dry_run else ''}Migrating dated notes to Sources/\n")
    print(f"Scope: {args.scope}")
    print(f"Vault: {vault}\n")
    
    # Find dated notes
    notes = find_dated_notes(vault, args.scope)
    
    if args.limit:
        notes = notes[:args.limit]
    
    print(f"Found {len(notes)} dated notes to migrate\n")
    
    if not notes:
        print("No notes to migrate.")
        return 0
    
    # Group by entity type
    by_type = {"people": 0, "customers": 0, "projects": 0, "other": 0}
    for note in notes:
        key = note["entity_type"] or "other"
        by_type[key] = by_type.get(key, 0) + 1
    
    print("By entity type:")
    for etype, count in by_type.items():
        if count > 0:
            print(f"  {etype}: {count}")
    print()
    
    # Migrate
    migrated = 0
    readmes_updated = 0
    errors = []
    
    for i, note in enumerate(notes, 1):
        result = migrate_note(vault, note, dry_run)
        
        if result["error"]:
            errors.append(f"{note['path'].name}: {result['error']}")
            print(f"  [{i}/{len(notes)}] ❌ {note['filename']}: {result['error']}")
        else:
            migrated += 1
            if result["readme_updated"]:
                readmes_updated += 1
            
            if dry_run:
                dest_rel = result["destination"].relative_to(vault)
                print(f"  [{i}/{len(notes)}] {note['filename']}")
                print(f"           → {dest_rel}")
            else:
                print(f"  [{i}/{len(notes)}] ✅ {note['filename']}")
    
    print(f"\n{'Would migrate' if dry_run else 'Migrated'}: {migrated} notes")
    print(f"{'Would update' if dry_run else 'Updated'}: {readmes_updated} READMEs")
    
    if errors:
        print(f"\nErrors: {len(errors)}")
        for err in errors[:5]:
            print(f"  - {err}")
    
    if dry_run:
        print("\n⚠️  DRY RUN - No changes made. Run with --execute to apply.")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
