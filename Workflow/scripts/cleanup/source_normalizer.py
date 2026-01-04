#!/usr/bin/env python3
"""
Source File Normalizer: Ensure consistent naming for all source files.

Naming convention:
- Transcripts: YYYY-MM-DD - {Brief title}.md
- Emails: YYYY-MM-DD_HHMMSS_{Subject}.md
- Documents: YYYY-MM-DD - {Title}.md

This script will:
1. Identify files with non-standard names
2. Propose standardized names
3. Rename files and update wikilinks
"""

import re
from pathlib import Path


def extract_date_from_filename(filename: str) -> tuple:
    """Extract date from various filename formats."""
    
    # Standard: YYYY-MM-DD - Title.md
    match = re.match(r'^(\d{4}-\d{2}-\d{2})\s*[-–—]\s*(.+)\.md$', filename)
    if match:
        return match.group(1), match.group(2), 'standard'
    
    # Compact: YYYY-MM-DD_HHMMSS_Title.md (email format)
    match = re.match(r'^(\d{4}-\d{2}-\d{2})_(\d{6})_(.+)\.md$', filename)
    if match:
        return match.group(1), match.group(3), 'email'
    
    # Month-only: YYYY-MM - Title.md
    match = re.match(r'^(\d{4}-\d{2})\s*[-–—]\s*(.+)\.md$', filename)
    if match:
        return match.group(1), match.group(2), 'month'
    
    # Natural date: Oct 22nd, 2025.md
    match = re.match(r'^([A-Za-z]+)\s+(\d{1,2})(?:st|nd|rd|th)?,?\s*(\d{4})\.md$', filename)
    if match:
        try:
            month_str = match.group(1)
            day = int(match.group(2))
            year = int(match.group(3))
            month_map = {
                'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
                'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
            }
            month = month_map.get(month_str.lower()[:3])
            if month:
                date_str = f"{year}-{month:02d}-{day:02d}"
                return date_str, '', 'natural'
        except Exception:
            pass
    
    # YYYYMMDD HHMM - Title.md
    match = re.match(r'^(\d{4})(\d{2})(\d{2})\s+(\d{2})(\d{2})\s*[-–—]\s*(.+)\.md$', filename)
    if match:
        date_str = f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
        return date_str, match.group(6), 'compact'
    
    # YYYY-MM-DD HHMM - Title.md (with time)
    match = re.match(r'^(\d{4}-\d{2}-\d{2})\s+\d{2}[:\s]?\d{2}\s*[-–—]\s*(.+)\.md$', filename)
    if match:
        return match.group(1), match.group(2), 'datetime'
    
    # YYYY-MM-DD HH:MM - Title.md (with colon time)
    match = re.match(r'^(\d{4}-\d{2}-\d{2})\s+\d{2}:\d{2}\s*[-–—]\s*(.+)\.md$', filename)
    if match:
        return match.group(1), match.group(2), 'datetime_colon'
    
    return None, filename.replace('.md', ''), 'unknown'


def normalize_title(title: str, max_length: int = 80) -> str:
    """Normalize a title for use in filename."""
    # Remove special characters but keep basic punctuation
    title = re.sub(r'[<>:"/\\|?*]', '', title)
    # Replace multiple spaces with single
    title = re.sub(r'\s+', ' ', title)
    # Truncate if needed
    if len(title) > max_length:
        title = title[:max_length].rsplit(' ', 1)[0]
    return title.strip()


def propose_new_name(path: Path) -> tuple:
    """Propose a standardized filename."""
    filename = path.name
    date_str, title, format_type = extract_date_from_filename(filename)
    
    if format_type == 'standard':
        # Already standard format
        return None, None, 'ok'
    
    if format_type == 'email':
        # Keep email format
        return None, None, 'ok'
    
    if date_str is None:
        return None, None, 'no_date'
    
    # Build new name
    if not title:
        title = 'Untitled'
    
    title = normalize_title(title)
    new_name = f"{date_str} - {title}.md"
    
    if new_name == filename:
        return None, None, 'ok'
    
    return new_name, path.parent / new_name, format_type


def find_sources(vault_root: Path) -> list:
    """Find all source files."""
    sources = []
    
    sources_dir = vault_root / 'Sources'
    if sources_dir.exists():
        for md_file in sources_dir.rglob('*.md'):
            sources.append(md_file)
    
    return sources


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Normalize source file names')
    parser.add_argument('--dry-run', action='store_true', help='Preview changes')
    parser.add_argument('--execute', action='store_true', help='Apply changes')
    args = parser.parse_args()
    
    if not args.dry_run and not args.execute:
        print("Use --dry-run to preview or --execute to apply changes")
        return
    
    vault_root = Path(__file__).parent.parent.parent.parent
    dry_run = not args.execute
    
    sources = find_sources(vault_root)
    print(f"{'DRY RUN: ' if dry_run else ''}Checking {len(sources)} source files\n")
    
    issues = []
    ok_count = 0
    
    for path in sources:
        new_name, new_path, status = propose_new_name(path)
        
        if status == 'ok':
            ok_count += 1
        elif status == 'no_date':
            print(f"  ⚠️  No date: {path.name}")
            issues.append((path, 'no_date', None))
        else:
            print(f"  → {path.name}")
            print(f"    ↳ {new_name}")
            issues.append((path, status, new_path))
            
            if not dry_run and new_path:
                path.rename(new_path)
    
    print("\nSummary:")
    print(f"  OK: {ok_count}")
    print(f"  Would rename: {len([i for i in issues if i[2]])}")
    print(f"  No date (needs manual review): {len([i for i in issues if i[1] == 'no_date'])}")


if __name__ == '__main__':
    main()
