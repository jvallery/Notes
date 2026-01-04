#!/usr/bin/env python3
"""
Find duplicate meeting notes - notes from the same person on the same date.

These typically occur when the same transcript is exported multiple times
from MacWhisper with slightly different content.
"""

from pathlib import Path
from collections import defaultdict
import yaml
import re

VAULT_ROOT = Path(__file__).parent.parent.parent

def load_frontmatter(path: Path) -> dict | None:
    """Extract frontmatter dict from markdown file."""
    content = path.read_text(encoding='utf-8')
    
    if not content.startswith('---'):
        return None
    
    end_match = re.search(r'\n---\n', content[3:])
    if not end_match:
        return None
    
    end_pos = end_match.end() + 3
    fm_text = content[4:end_pos - 4]
    
    try:
        return yaml.safe_load(fm_text) or {}
    except yaml.YAMLError:
        return None

def get_content_summary(path: Path) -> tuple[int, str]:
    """Get content length and first 100 chars of body (not frontmatter)."""
    content = path.read_text(encoding='utf-8')
    
    # Skip frontmatter
    if content.startswith('---'):
        end_match = re.search(r'\n---\n', content[3:])
        if end_match:
            content = content[end_match.end() + 3:]
    
    return len(content), content[:100].strip()

def find_duplicates():
    """Find notes with same person+date combination."""
    
    # Group notes by (person, date)
    notes_by_key = defaultdict(list)
    
    for people_dir in [VAULT_ROOT / "VAST" / "People", VAULT_ROOT / "Personal" / "People"]:
        if not people_dir.exists():
            continue
            
        for person_dir in people_dir.iterdir():
            if not person_dir.is_dir():
                continue
                
            for note_path in person_dir.glob("*.md"):
                if note_path.name == "README.md":
                    continue
                    
                fm = load_frontmatter(note_path)
                if not fm:
                    continue
                    
                date = fm.get('date', '')
                person = person_dir.name
                
                if date:
                    key = (person, str(date)[:10])  # Normalize date to YYYY-MM-DD
                    notes_by_key[key].append(note_path)
    
    # Find groups with duplicates
    duplicates = {k: v for k, v in notes_by_key.items() if len(v) > 1}
    
    return duplicates

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Find duplicate meeting notes")
    parser.add_argument("--consolidate", action="store_true", help="Consolidate duplicates (keep first, remove rest)")
    parser.add_argument("--dry-run", action="store_true", help="Don't actually delete files")
    args = parser.parse_args()
    
    duplicates = find_duplicates()
    
    if not duplicates:
        print("No duplicates found!")
        return
    
    total_duplicates = sum(len(v) - 1 for v in duplicates.values())
    print(f"Found {len(duplicates)} groups with {total_duplicates} duplicate notes:\n")
    
    files_to_remove = []
    
    for (person, date), notes in sorted(duplicates.items()):
        print(f"📁 {person} - {date} ({len(notes)} notes)")
        
        # Sort by content length descending to keep most complete
        notes_with_size = [(n, get_content_summary(n)) for n in notes]
        notes_with_size.sort(key=lambda x: x[1][0], reverse=True)
        
        for i, (note, (size, preview)) in enumerate(notes_with_size):
            marker = "✓ KEEP" if i == 0 else "✗ REMOVE"
            print(f"  {marker}: {note.name} ({size} chars)")
            if i > 0:
                files_to_remove.append(note)
        print()
    
    if args.consolidate:
        print(f"\n{'[DRY RUN] ' if args.dry_run else ''}Removing {len(files_to_remove)} duplicate files...")
        
        for f in files_to_remove:
            if not args.dry_run:
                f.unlink()
            print(f"  {'[DRY] ' if args.dry_run else ''}Removed: {f.relative_to(VAULT_ROOT)}")
        
        if not args.dry_run:
            print(f"\n✅ Removed {len(files_to_remove)} duplicates")
        else:
            print(f"\n[DRY RUN] Would remove {len(files_to_remove)} files. Run without --dry-run to apply.")

if __name__ == "__main__":
    main()
