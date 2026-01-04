#!/usr/bin/env python3
"""
Clean up TODO.md by removing completed items and reorganizing structure.

Removes:
- All items with "Status: ✅ COMPLETED" 
- Items with ✅ in the header (already fixed)
- Unnumbered "Post-Run Cleanup" sections that are completed
- Priority Matrix (outdated)
- Summary Statistics (stale data)
- Vault Analysis Findings header (items moved inline)
- Planner Improvements header (items moved inline)
- Notes section
"""

import re
from pathlib import Path

TODO_PATH = Path(__file__).parent.parent / "TODO.md"

def load_todo():
    """Load TODO.md content."""
    return TODO_PATH.read_text()

def extract_sections(content: str) -> list[dict]:
    """Parse TODO.md into sections."""
    lines = content.split('\n')
    sections = []
    current_section = None
    current_lines = []
    current_start = 0
    
    for i, line in enumerate(lines):
        # Check for section headers (## or #)
        if line.startswith('## ') or line.startswith('# '):
            if current_section is not None:
                sections.append({
                    'header': current_section,
                    'content': '\n'.join(current_lines),
                    'line_start': current_start,
                })
            current_section = line
            current_lines = []
            current_start = i
        else:
            current_lines.append(line)
    
    # Don't forget the last section
    if current_section is not None:
        sections.append({
            'header': current_section,
            'content': '\n'.join(current_lines),
            'line_start': current_start,
        })
    
    return sections

def is_completed_item(section: dict) -> bool:
    """Check if a section is marked as completed."""
    header = section['header']
    content = section['content']
    
    # Check for ✅ in header
    if '✅' in header:
        return True
    
    # Check for completed status in content
    if 'Status: ✅ COMPLETED' in content:
        return True
    
    return False

def is_meta_section(section: dict) -> bool:
    """Check if section is a meta/reference section to remove."""
    header = section['header']
    meta_patterns = [
        '# Priority Matrix',
        '# Summary Statistics',
        '# Vault Statistics Summary',
        '# Vault Analysis Findings',
        '# Planner Improvements',
        '# Post-Run Cleanup',
        '# Notes',
    ]
    return any(pattern in header for pattern in meta_patterns)

def is_numbered_item(header: str) -> bool:
    """Check if header is a numbered item like ## 1) or ## 42)"""
    return bool(re.match(r'^## \d+\)', header))

def get_item_number(header: str) -> int | None:
    """Extract item number from header."""
    match = re.match(r'^## (\d+)\)', header)
    return int(match.group(1)) if match else None

def clean_todo(content: str) -> str:
    """Clean up TODO.md content."""
    lines = content.split('\n')
    
    # Find header section (everything before first ## numbered item)
    header_end = 0
    for i, line in enumerate(lines):
        if re.match(r'^## \d+\)', line):
            header_end = i
            break
    
    header_section = '\n'.join(lines[:header_end])
    body = '\n'.join(lines[header_end:])
    
    # Parse body into sections
    sections = extract_sections(body)
    
    # Filter out completed items and meta sections
    kept_sections = []
    removed_count = 0
    
    for section in sections:
        if is_completed_item(section):
            print(f"  Removing completed: {section['header'][:60]}...")
            removed_count += 1
            continue
        if is_meta_section(section):
            print(f"  Removing meta section: {section['header'][:60]}...")
            removed_count += 1
            continue
        kept_sections.append(section)
    
    print(f"\nRemoved {removed_count} sections")
    print(f"Kept {len(kept_sections)} sections")
    
    # Renumber remaining items
    item_num = 1
    renumbered_sections = []
    
    for section in kept_sections:
        header = section['header']
        if is_numbered_item(header):
            old_num = get_item_number(header)
            # Replace old number with new number
            new_header = re.sub(r'^## \d+\)', f'## {item_num})', header)
            section['header'] = new_header
            if old_num != item_num:
                print(f"  Renumbered: {old_num} → {item_num}")
            item_num += 1
        renumbered_sections.append(section)
    
    # Reconstruct file
    output_lines = [header_section]
    
    for section in renumbered_sections:
        output_lines.append('')
        output_lines.append('---')
        output_lines.append('')
        output_lines.append(section['header'])
        output_lines.append(section['content'].rstrip())
    
    result = '\n'.join(output_lines)
    
    # Clean up excess blank lines
    result = re.sub(r'\n{4,}', '\n\n\n', result)
    
    return result

def main():
    print("Loading TODO.md...")
    content = load_todo()
    print(f"Original: {len(content.splitlines())} lines")
    
    print("\nCleaning up...")
    cleaned = clean_todo(content)
    print(f"Cleaned: {len(cleaned.splitlines())} lines")
    
    # Write back
    TODO_PATH.write_text(cleaned)
    print(f"\nWrote cleaned TODO.md")

if __name__ == "__main__":
    main()
