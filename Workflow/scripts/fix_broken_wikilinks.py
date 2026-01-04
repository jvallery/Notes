#!/usr/bin/env python3
"""
Fix broken wikilinks that point to non-existent notes.

Two types of broken links:
1. Date-title links like [[2025-09-03 - Summary text]] that don't exist
2. Truncated archive filenames that look like note titles

This script:
1. Finds all date-prefixed wikilinks
2. Checks if the linked note exists anywhere in the vault
3. If not found, removes the wikilink but keeps the text
"""

import re
from pathlib import Path
from collections import defaultdict

VAULT_ROOT = Path(__file__).parent.parent.parent

# Pattern for date-prefixed wikilinks
WIKILINK_PATTERN = re.compile(r'\[\[(20\d{2}-\d{2}-\d{2} - [^\]]+)\]\]')

def find_all_notes() -> set[str]:
    """Build set of all note basenames (without .md) for quick lookup."""
    notes = set()
    for md_file in VAULT_ROOT.rglob("*.md"):
        if "Inbox/_archive" in str(md_file):
            continue  # Skip archive
        notes.add(md_file.stem)
    return notes

def find_broken_links(existing_notes: set[str]) -> dict[Path, list[tuple[str, str]]]:
    """Find files containing broken wikilinks.
    
    Returns dict of file -> list of (full_match, link_target)
    """
    broken_by_file = defaultdict(list)
    
    for md_file in VAULT_ROOT.rglob("*.md"):
        if "Inbox/_archive" in str(md_file) or "_archive" in str(md_file):
            continue
            
        try:
            content = md_file.read_text(encoding='utf-8')
        except Exception:
            continue
            
        for match in WIKILINK_PATTERN.finditer(content):
            link_target = match.group(1)
            # Check if target exists
            if link_target not in existing_notes:
                broken_by_file[md_file].append((match.group(0), link_target))
    
    return broken_by_file

def fix_broken_links(file_path: Path, broken_links: list[tuple[str, str]], dry_run: bool = True) -> int:
    """Remove broken wikilinks, keeping just the text.
    
    [[2025-09-03 - Summary]] -> 2025-09-03 - Summary
    """
    content = file_path.read_text(encoding='utf-8')
    fixed_count = 0
    
    for full_match, link_target in broken_links:
        # Replace [[link]] with just link (no brackets)
        # But for these long hallucinated links, just remove them entirely
        if len(link_target) > 60:  # Truncated/hallucinated - remove entirely
            content = content.replace(full_match, '')
        else:
            # Keep the text but remove the brackets
            content = content.replace(full_match, link_target)
        fixed_count += 1
    
    if not dry_run:
        file_path.write_text(content, encoding='utf-8')
    
    return fixed_count

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Fix broken date-title wikilinks")
    parser.add_argument("--dry-run", action="store_true", help="Don't modify files")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show all broken links")
    args = parser.parse_args()
    
    print("Scanning vault for existing notes...")
    existing_notes = find_all_notes()
    print(f"Found {len(existing_notes)} notes\n")
    
    print("Finding broken wikilinks...")
    broken = find_broken_links(existing_notes)
    
    if not broken:
        print("No broken wikilinks found!")
        return
    
    total_broken = sum(len(v) for v in broken.values())
    print(f"Found {total_broken} broken wikilinks in {len(broken)} files\n")
    
    total_fixed = 0
    for file_path, links in sorted(broken.items()):
        rel_path = file_path.relative_to(VAULT_ROOT)
        print(f"{'[DRY] ' if args.dry_run else ''}Fixing {len(links)} links in {rel_path}")
        
        if args.verbose:
            for full_match, target in links:
                action = "REMOVE" if len(target) > 60 else "UNLINK"
                print(f"  {action}: {target[:60]}...")
        
        fixed = fix_broken_links(file_path, links, dry_run=args.dry_run)
        total_fixed += fixed
    
    print(f"\n{'[DRY RUN] ' if args.dry_run else ''}Fixed {total_fixed} broken wikilinks")
    
    if args.dry_run:
        print("\nRun without --dry-run to apply changes.")

if __name__ == "__main__":
    main()
