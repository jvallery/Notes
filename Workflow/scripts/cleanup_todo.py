#!/usr/bin/env python3
"""
TODO Cleanup Script

Removes completed items from TODO.md and renumbers remaining items.
Preserves the header/instructions section.
"""

import re
import sys
from pathlib import Path


def parse_sections(content: str) -> tuple[str, list[tuple[int, str, bool]]]:
    """
    Parse TODO.md into header and numbered sections.
    
    Returns:
        (header_text, [(item_num, section_text, is_completed), ...])
    """
    lines = content.split('\n')
    
    # Find where numbered items start (first "## N)")
    header_end = 0
    for i, line in enumerate(lines):
        if re.match(r'^## \d+\)', line):
            header_end = i
            break
    
    header = '\n'.join(lines[:header_end])
    
    # Parse numbered sections
    sections = []
    current_num = None
    current_lines = []
    
    for line in lines[header_end:]:
        match = re.match(r'^## (\d+)\)', line)
        if match:
            # Save previous section
            if current_num is not None:
                section_text = '\n'.join(current_lines)
                is_completed = '✅ COMPLETED' in section_text or '✅' in current_lines[0]
                sections.append((current_num, section_text, is_completed))
            
            current_num = int(match.group(1))
            current_lines = [line]
        elif current_num is not None:
            current_lines.append(line)
    
    # Don't forget last section
    if current_num is not None:
        section_text = '\n'.join(current_lines)
        is_completed = '✅ COMPLETED' in section_text or '✅' in current_lines[0]
        sections.append((current_num, section_text, is_completed))
    
    return header, sections


def renumber_section(section_text: str, old_num: int, new_num: int) -> str:
    """Replace item number in section header."""
    return re.sub(
        rf'^## {old_num}\)',
        f'## {new_num})',
        section_text,
        count=1
    )


def cleanup_todo(todo_path: Path, dry_run: bool = False) -> dict:
    """
    Remove completed items and renumber remaining.
    
    Returns summary dict with counts.
    """
    content = todo_path.read_text()
    header, sections = parse_sections(content)
    
    # Separate completed vs remaining
    completed = [(n, t) for n, t, c in sections if c]
    remaining = [(n, t) for n, t, c in sections if not c]
    
    print(f"\n📊 TODO.md Summary:")
    print(f"   Total items: {len(sections)}")
    print(f"   Completed:   {len(completed)} (will be removed)")
    print(f"   Remaining:   {len(remaining)} (will be renumbered)")
    
    if completed:
        print(f"\n🗑️  Removing completed items:")
        for num, text in completed:
            # Extract title from first line
            first_line = text.split('\n')[0]
            title = re.sub(r'^## \d+\)\s*', '', first_line)
            print(f"   - Item {num}: {title[:60]}...")
    
    # Renumber remaining items
    new_sections = []
    for new_num, (old_num, text) in enumerate(remaining, start=1):
        if old_num != new_num:
            text = renumber_section(text, old_num, new_num)
        new_sections.append(text)
    
    # Reconstruct file
    new_content = header.rstrip() + '\n\n---\n\n' + '\n\n---\n\n'.join(new_sections)
    
    # Clean up excess blank lines
    new_content = re.sub(r'\n{4,}', '\n\n\n', new_content)
    new_content = new_content.rstrip() + '\n'
    
    if dry_run:
        print(f"\n🔍 DRY RUN - no changes written")
        print(f"   Would renumber {len(remaining)} items (1 to {len(remaining)})")
    else:
        todo_path.write_text(new_content)
        print(f"\n✅ Cleaned up TODO.md:")
        print(f"   Removed {len(completed)} completed items")
        print(f"   Renumbered {len(remaining)} remaining items (1 to {len(remaining)})")
    
    return {
        'total': len(sections),
        'removed': len(completed),
        'remaining': len(remaining)
    }


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Clean up completed TODO items')
    parser.add_argument('--dry-run', '-n', action='store_true',
                        help='Show what would be done without making changes')
    parser.add_argument('--todo', type=Path, 
                        default=Path(__file__).parent.parent / 'TODO.md',
                        help='Path to TODO.md file')
    
    args = parser.parse_args()
    
    if not args.todo.exists():
        print(f"❌ TODO.md not found at {args.todo}")
        sys.exit(1)
    
    cleanup_todo(args.todo, dry_run=args.dry_run)


if __name__ == '__main__':
    main()
