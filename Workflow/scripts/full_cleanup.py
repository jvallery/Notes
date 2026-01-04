#!/usr/bin/env python3
"""
Full vault cleanup for reprocessing.

1. Delete all generated dated notes (YYYY-MM-DD - *.md)
2. Reset all READMEs (clear accumulated sections)
3. Restore archived transcripts to Inbox/Transcripts/
4. Clear extraction artifacts

Usage:
    python scripts/full_cleanup.py --dry-run    # Preview
    python scripts/full_cleanup.py              # Execute
"""

import argparse
import re
import shutil
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).parent
WORKFLOW_DIR = SCRIPTS_DIR.parent
if str(WORKFLOW_DIR) not in sys.path:
    sys.path.insert(0, str(WORKFLOW_DIR))

from scripts.utils.config import vault_root
from scripts.reset_readmes import reset_readme, find_readmes


# Pattern for dated notes: YYYY-MM-DD - Title.md
DATED_NOTE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2} - .+\.md$")


def find_dated_notes(vault: Path) -> list[Path]:
    """Find all generated dated notes (not READMEs)."""
    dated_notes = []
    
    # Search in entity folders
    search_paths = [
        vault / "VAST" / "People",
        vault / "VAST" / "Customers and Partners",
        vault / "VAST" / "Projects",
        vault / "VAST" / "ROB",
        vault / "VAST" / "rob",
        vault / "Personal" / "People",
        vault / "Personal" / "Projects",
    ]
    
    for search_path in search_paths:
        if not search_path.exists():
            continue
        for entity_folder in search_path.iterdir():
            if entity_folder.is_dir():
                for file in entity_folder.iterdir():
                    if file.is_file() and DATED_NOTE_PATTERN.match(file.name):
                        dated_notes.append(file)
    
    return dated_notes


def find_archived_transcripts(vault: Path) -> list[Path]:
    """Find all transcripts in archive folders."""
    archive_root = vault / "Inbox" / "_archive"
    transcripts = []
    
    if not archive_root.exists():
        return transcripts
    
    for date_folder in archive_root.iterdir():
        if date_folder.is_dir() and date_folder.name != "legacy_bins":
            for file in date_folder.iterdir():
                if file.is_file() and file.suffix == ".md":
                    transcripts.append(file)
    
    return transcripts


def main():
    parser = argparse.ArgumentParser(description="Full vault cleanup for reprocessing")
    parser.add_argument("--dry-run", action="store_true", help="Preview without changes")
    parser.add_argument("--skip-reset", action="store_true", help="Skip README reset")
    parser.add_argument("--skip-restore", action="store_true", help="Skip transcript restore")
    args = parser.parse_args()
    
    vault = vault_root()
    dry_run = args.dry_run
    
    if dry_run:
        print("DRY RUN - no changes will be made\n")
    
    # Step 1: Find and delete dated notes
    print("=== Step 1: Delete Generated Notes ===")
    dated_notes = find_dated_notes(vault)
    print(f"Found {len(dated_notes)} dated notes to delete:")
    for note in sorted(dated_notes):
        rel = note.relative_to(vault)
        print(f"  ✗ {rel}")
        if not dry_run:
            note.unlink()
    print()
    
    # Step 2: Reset READMEs
    if not args.skip_reset:
        print("=== Step 2: Reset READMEs ===")
        readmes = find_readmes(vault)
        modified = 0
        for readme in readmes:
            result = reset_readme(readme, dry_run=dry_run)
            if result["modified"]:
                modified += 1
                rel = readme.relative_to(vault)
                print(f"  ✓ {rel}")
        print(f"Reset {modified} READMEs\n")
    
    # Step 3: Restore archived transcripts
    if not args.skip_restore:
        print("=== Step 3: Restore Archived Transcripts ===")
        transcripts = find_archived_transcripts(vault)
        dest_folder = vault / "Inbox" / "Transcripts"
        print(f"Found {len(transcripts)} transcripts to restore:")
        for transcript in sorted(transcripts):
            dest = dest_folder / transcript.name
            print(f"  → {transcript.name}")
            if not dry_run:
                shutil.copy2(transcript, dest)
        print()
    
    # Step 4: Clear extraction artifacts
    print("=== Step 4: Clear Extraction Artifacts ===")
    extraction_dir = vault / "Inbox" / "_extraction"
    if extraction_dir.exists():
        artifacts = list(extraction_dir.glob("*.json"))
        print(f"Found {len(artifacts)} artifacts to delete")
        for artifact in artifacts:
            if not dry_run:
                artifact.unlink()
    print()
    
    # Summary
    print("=== Summary ===")
    action = "Would delete" if dry_run else "Deleted"
    print(f"  {action} {len(dated_notes)} dated notes")
    if not args.skip_reset:
        print(f"  {'Would reset' if dry_run else 'Reset'} READMEs")
    if not args.skip_restore:
        print(f"  {'Would restore' if dry_run else 'Restored'} {len(transcripts)} transcripts")
    print()
    
    if dry_run:
        print("Run without --dry-run to execute.")
    else:
        print("Cleanup complete. Run process_inbox.py to reprocess.")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
