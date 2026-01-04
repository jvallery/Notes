#!/usr/bin/env python3
"""
Fix broken source_ref frontmatter by finding actual file locations.

source_refs point to expected archive paths like:
  Inbox/_archive/2025-10-22/2025-10-22 - Summary.md
  
But files were actually archived to:
  Inbox/_archive/2026-01-04/2025-10-22 - Summary.md

This script:
1. Finds all files with source_ref in frontmatter
2. Checks if the target exists
3. If missing, searches for matching filename in archive
4. Updates source_ref to actual location or removes if not found
"""

import re
from pathlib import Path
import yaml

VAULT_ROOT = Path(__file__).parent.parent.parent
ARCHIVE_DIR = VAULT_ROOT / "Inbox" / "_archive"

def load_frontmatter(path: Path) -> tuple[dict | None, str]:
    """Extract frontmatter dict and body text from markdown file."""
    content = path.read_text(encoding='utf-8')
    
    if not content.startswith('---'):
        return None, content
    
    # Find end of frontmatter
    end_match = re.search(r'\n---\n', content[3:])
    if not end_match:
        return None, content
    
    end_pos = end_match.end() + 3
    fm_text = content[4:end_pos - 4]
    body = content[end_pos:]
    
    try:
        fm = yaml.safe_load(fm_text) or {}
        return fm, body
    except yaml.YAMLError:
        return None, content

def save_file(path: Path, frontmatter: dict, body: str):
    """Save file with updated frontmatter."""
    fm_text = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True, sort_keys=False)
    content = f"---\n{fm_text}---\n{body}"
    path.write_text(content, encoding='utf-8')

def find_matching_archive_file(source_ref: str) -> Path | None:
    """Search archive for file matching the filename portion of source_ref."""
    ref_path = Path(source_ref)
    filename = ref_path.name
    
    # Search recursively in archive
    for archive_file in ARCHIVE_DIR.rglob("*.md"):
        if archive_file.name == filename:
            return archive_file
    
    # Try partial match (some filenames were truncated)
    # Extract date prefix and first ~50 chars
    if filename.startswith("20"):
        date_part = filename[:10]
        for archive_file in ARCHIVE_DIR.rglob(f"{date_part}*.md"):
            # Check if beginning matches
            if archive_file.name.startswith(filename[:50]):
                return archive_file
    
    return None

def process_file(path: Path, dry_run: bool = True) -> str:
    """Process a single file. Returns status string."""
    fm, body = load_frontmatter(path)
    if not fm or 'source_ref' not in fm:
        return "no_source_ref"
    
    source_ref = fm['source_ref']
    if isinstance(source_ref, str):
        source_ref = source_ref.strip('"\'')
    
    # Check if target exists
    target_path = VAULT_ROOT / source_ref
    if target_path.exists():
        return "valid"
    
    # Try to find actual location
    actual_file = find_matching_archive_file(source_ref)
    if actual_file:
        new_ref = str(actual_file.relative_to(VAULT_ROOT))
        if not dry_run:
            fm['source_ref'] = new_ref
            save_file(path, fm, body)
        return f"fixed:{source_ref} -> {new_ref}"
    
    # File not found anywhere - remove the broken ref
    if not dry_run:
        del fm['source_ref']
        save_file(path, fm, body)
    return f"removed:{source_ref}"

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Fix broken source_ref frontmatter")
    parser.add_argument("--dry-run", action="store_true", help="Don't actually modify files")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show all files")
    args = parser.parse_args()
    
    # Find all markdown files in VAST and Personal
    search_dirs = [VAULT_ROOT / "VAST", VAULT_ROOT / "Personal"]
    
    stats = {"valid": 0, "fixed": 0, "removed": 0, "no_source_ref": 0}
    
    for search_dir in search_dirs:
        for md_file in search_dir.rglob("*.md"):
            result = process_file(md_file, dry_run=args.dry_run)
            
            if result == "valid":
                stats["valid"] += 1
                if args.verbose:
                    print(f"✓ {md_file.relative_to(VAULT_ROOT)}")
            elif result == "no_source_ref":
                stats["no_source_ref"] += 1
            elif result.startswith("fixed:"):
                stats["fixed"] += 1
                print(f"{'[DRY] ' if args.dry_run else ''}FIX: {md_file.relative_to(VAULT_ROOT)}")
                print(f"      {result[6:]}")
            elif result.startswith("removed:"):
                stats["removed"] += 1
                print(f"{'[DRY] ' if args.dry_run else ''}DEL: {md_file.relative_to(VAULT_ROOT)}")
                print(f"      {result[8:]}")
    
    print(f"\n{'DRY RUN - ' if args.dry_run else ''}Summary:")
    print(f"  Valid source_refs: {stats['valid']}")
    print(f"  Fixed source_refs: {stats['fixed']}")
    print(f"  Removed (not found): {stats['removed']}")
    print(f"  No source_ref: {stats['no_source_ref']}")
    
    if args.dry_run and (stats['fixed'] > 0 or stats['removed'] > 0):
        print("\nRun without --dry-run to apply changes.")

if __name__ == "__main__":
    main()
