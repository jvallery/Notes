"""
Backfill Scanner: Find all notes in entity folders.

Scans the vault for existing notes that need to be processed
for README context population.
"""

import re
from datetime import datetime
from pathlib import Path

from . import (
    BackfillManifest,
    EntityInfo,
    NoteMetadata,
)

# Import from existing utils
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from utils.frontmatter import parse_frontmatter
from utils.config import vault_root


# ─────────────────────────────────────────────────────────────────────────────
# Entity Type Detection
# ─────────────────────────────────────────────────────────────────────────────

ENTITY_PATTERNS = {
    "people": [
        r"VAST/People/[^/]+$",
        r"Personal/People/[^/]+$",
    ],
    "accounts": [
        r"VAST/Customers and Partners/[^/]+$",
    ],
    "projects": [
        r"VAST/Projects/[^/]+$",
        r"Personal/Projects/[^/]+$",
    ],
    "rob": [
        r"VAST/ROB/[^/]+$",
    ],
}


def detect_entity_type(folder_path: str) -> str | None:
    """Detect entity type from folder path."""
    for entity_type, patterns in ENTITY_PATTERNS.items():
        for pattern in patterns:
            if re.match(pattern, folder_path):
                return entity_type
    return None


def get_entity_name(folder_path: str) -> str:
    """Extract entity name from folder path."""
    return Path(folder_path).name


# ─────────────────────────────────────────────────────────────────────────────
# Date Extraction
# ─────────────────────────────────────────────────────────────────────────────

DATE_PATTERNS = [
    r"^(\d{4}-\d{2}-\d{2})",  # 2025-11-14 at start
    r"^(\d{4}-\d{2}-\d{2})\s",  # 2025-11-14 followed by space
    r"(\d{4}-\d{2}-\d{2})",  # Anywhere in filename
]


def extract_date_from_filename(filename: str) -> str | None:
    """Try to extract a date from the filename."""
    for pattern in DATE_PATTERNS:
        match = re.search(pattern, filename)
        if match:
            return match.group(1)
    return None


def extract_date_from_frontmatter(fm: dict) -> str | None:
    """Try to extract a date from frontmatter."""
    if not fm:
        return None
    
    # Try common date fields
    for key in ["date", "created", "created_at", "meeting_date"]:
        if key in fm:
            value = str(fm[key])
            # Validate it looks like a date
            if re.match(r"^\d{4}-\d{2}-\d{2}", value):
                return value[:10]
    
    return None


# ─────────────────────────────────────────────────────────────────────────────
# Note Scanning
# ─────────────────────────────────────────────────────────────────────────────

SKIP_FILES = {"README.md", ".DS_Store"}
SKIP_FOLDERS = {"_Tasks", "_archive", "_bins", "_extraction", "_failed", "docs", "archive"}


def scan_note(note_path: Path, vault: Path) -> NoteMetadata | None:
    """Scan a single note file for metadata."""
    
    if note_path.name in SKIP_FILES:
        return None
    
    if not note_path.suffix == ".md":
        return None
    
    # Check if in a skip folder
    for parent in note_path.relative_to(vault).parts:
        if parent in SKIP_FOLDERS:
            return None
    
    try:
        content = note_path.read_text(encoding="utf-8")
    except Exception:
        return None
    
    # Parse frontmatter
    fm, _ = parse_frontmatter(content)
    
    # Extract date
    date = extract_date_from_frontmatter(fm)
    if not date:
        date = extract_date_from_filename(note_path.name)
    
    # Extract title
    title = None
    if fm and "title" in fm:
        title = str(fm["title"])
    else:
        # Try to get from H1
        h1_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        if h1_match:
            title = h1_match.group(1).strip()
        else:
            title = note_path.stem
    
    return NoteMetadata(
        path=str(note_path.relative_to(vault)),
        filename=note_path.name,
        date=date,
        title=title,
        has_frontmatter=bool(fm),
        frontmatter_type=fm.get("type") if fm else None,
    )


def find_entity_folders(vault: Path, scope: str) -> list[Path]:
    """Find all entity folders within scope."""
    scope_path = vault / scope
    
    if not scope_path.exists():
        return []
    
    entity_folders = []
    
    # Check if scope itself is an entity folder
    rel_scope = str(scope_path.relative_to(vault))
    if detect_entity_type(rel_scope):
        return [scope_path]
    
    # Walk the scope looking for entity folders
    for folder in scope_path.rglob("*"):
        if not folder.is_dir():
            continue
        
        # Skip hidden folders and system folders
        if folder.name.startswith(".") or folder.name.startswith("_"):
            continue
        
        rel_path = str(folder.relative_to(vault))
        entity_type = detect_entity_type(rel_path)
        
        if entity_type:
            entity_folders.append(folder)
    
    return sorted(entity_folders)


def scan_entity(entity_folder: Path, vault: Path) -> EntityInfo:
    """Scan a single entity folder for notes."""
    
    rel_path = str(entity_folder.relative_to(vault))
    entity_type = detect_entity_type(rel_path) or "unknown"
    entity_name = get_entity_name(rel_path)
    
    # Check for README
    readme_path = entity_folder / "README.md"
    readme_exists = readme_path.exists()
    
    # Scan for notes (direct children only, not recursing into subfolders)
    notes = []
    for file in entity_folder.iterdir():
        if file.is_file() and file.suffix == ".md" and file.name != "README.md":
            note = scan_note(file, vault)
            if note:
                notes.append(note)
    
    # Sort by date (newest first)
    notes.sort(key=lambda n: n.date or "0000-00-00", reverse=True)
    
    return EntityInfo(
        path=rel_path,
        entity_type=entity_type,
        entity_name=entity_name,
        readme_exists=readme_exists,
        readme_path=str(readme_path.relative_to(vault)) if readme_exists else None,
        notes=notes,
        note_count=len(notes),
    )


# ─────────────────────────────────────────────────────────────────────────────
# Main Scanner
# ─────────────────────────────────────────────────────────────────────────────


def scan_for_backfill(scope: str = "VAST", vault: Path | None = None) -> BackfillManifest:
    """
    Scan the vault for notes that need backfill processing.
    
    Args:
        scope: Folder scope to scan (e.g., "VAST", "VAST/People", "Personal")
        vault: Path to vault root (defaults to config)
    
    Returns:
        BackfillManifest with all entities and notes found
    """
    if vault is None:
        vault = Path(vault_root())
    
    entities = []
    total_notes = 0
    notes_with_dates = 0
    notes_without_dates = 0
    
    # Find all entity folders
    entity_folders = find_entity_folders(vault, scope)
    
    for folder in entity_folders:
        entity = scan_entity(folder, vault)
        entities.append(entity)
        total_notes += entity.note_count
        
        for note in entity.notes:
            if note.date:
                notes_with_dates += 1
            else:
                notes_without_dates += 1
    
    return BackfillManifest(
        version="1.0",
        scanned_at=datetime.now(),
        scope=scope,
        entities=entities,
        total_entities=len(entities),
        total_notes=total_notes,
        notes_with_dates=notes_with_dates,
        notes_without_dates=notes_without_dates,
    )


# ─────────────────────────────────────────────────────────────────────────────
# Save/Load Functions
# ─────────────────────────────────────────────────────────────────────────────


def save_manifest(manifest: BackfillManifest, path: Path) -> None:
    """Save BackfillManifest to JSON file."""
    import json
    
    path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(path, "w") as f:
        json.dump(manifest.model_dump(mode="json"), f, indent=2, default=str)
    
    print(f"Saved manifest to: {path}")


def load_manifest(path: Path) -> BackfillManifest:
    """Load BackfillManifest from JSON file."""
    import json
    
    with open(path) as f:
        data = json.load(f)
    
    return BackfillManifest.model_validate(data)


# ─────────────────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse
    import json
    
    parser = argparse.ArgumentParser(description="Scan vault for backfill candidates")
    parser.add_argument("--scope", default="VAST", help="Folder scope to scan")
    parser.add_argument("-o", "--output", help="Output JSON file")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    
    args = parser.parse_args()
    
    manifest = scan_for_backfill(args.scope)
    
    if args.verbose:
        print(f"Scanned: {args.scope}")
        print(f"Entities: {manifest.total_entities}")
        print(f"Notes: {manifest.total_notes}")
        print(f"  With dates: {manifest.notes_with_dates}")
        print(f"  Without dates: {manifest.notes_without_dates}")
        print()
        for entity in manifest.entities[:5]:
            print(f"  {entity.path}: {entity.note_count} notes")
    
    if args.output:
        with open(args.output, "w") as f:
            json.dump(manifest.model_dump(mode="json"), f, indent=2, default=str)
        print(f"Wrote manifest to {args.output}")
    else:
        print(manifest.model_dump_json(indent=2))
