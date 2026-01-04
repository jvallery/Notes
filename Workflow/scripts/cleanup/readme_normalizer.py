#!/usr/bin/env python3
"""
README Normalizer: Standardize README structure across all entity types.

Target structure for PEOPLE:
1. Frontmatter
2. # Title
3. ## Profile (Role, Location, Relationship, Contact Info)
4. ## Open Tasks
5. ## Recent Context (reverse chronological, deduplicated)
6. ## Key Facts
7. ## Related

Target structure for CUSTOMERS:
1. Frontmatter
2. # Title
3. ## Account Status (Industry, Stage, etc.)
4. ## Key Contacts
5. ## Open Tasks
6. ## Recent Context
7. ## Key Facts
8. ## Opportunities / Blockers
9. ## Related

Target structure for PROJECTS:
1. Frontmatter
2. # Title
3. ## Status (Owner, Stage, etc.)
4. ## Overview
5. ## Open Tasks
6. ## Recent Context
7. ## Key Facts
8. ## Blockers
9. ## Related
"""

import re
import yaml
from pathlib import Path
from datetime import datetime
from collections import OrderedDict


def parse_readme(content: str) -> dict:
    """Parse README into frontmatter and sections."""
    result = {
        'frontmatter': {},
        'frontmatter_raw': '',
        'title': '',
        'sections': OrderedDict()
    }
    
    # Extract frontmatter
    if content.startswith('---'):
        end = content.find('\n---', 3)
        if end != -1:
            result['frontmatter_raw'] = content[4:end]
            try:
                result['frontmatter'] = yaml.safe_load(result['frontmatter_raw']) or {}
            except Exception:
                result['frontmatter'] = {}
            content = content[end+4:].strip()
    
    # Extract title
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if line.startswith('# ') and not line.startswith('## '):
            result['title'] = line[2:].strip()
            content = '\n'.join(lines[i+1:]).strip()
            break
    
    # Extract sections
    current_section = None
    current_content = []
    
    for line in content.split('\n'):
        if line.startswith('## '):
            if current_section:
                result['sections'][current_section] = '\n'.join(current_content).strip()
            current_section = line[3:].strip()
            current_content = []
        else:
            current_content.append(line)
    
    if current_section:
        result['sections'][current_section] = '\n'.join(current_content).strip()
    
    return result


def parse_ledger_entry(line: str) -> tuple:
    """Parse a ledger entry line and extract date for sorting."""
    line = line.strip()
    if not line.startswith('- '):
        return None, line
    
    # Pattern: - YYYY-MM-DD: [[...]] — ...
    # Or: - unknown: [[...]] — ...
    date_match = re.match(r'^- (\d{4}-\d{2}-\d{2}|unknown):', line)
    if date_match:
        date_str = date_match.group(1)
        if date_str == 'unknown':
            return datetime(1900, 1, 1), line
        try:
            return datetime.strptime(date_str, '%Y-%m-%d'), line
        except Exception:
            pass
    
    return datetime(1900, 1, 1), line


def deduplicate_and_sort_ledger(content: str) -> str:
    """Deduplicate ledger entries and sort reverse chronologically."""
    lines = content.split('\n')
    entries = []
    other_lines = []
    
    for line in lines:
        if line.strip().startswith('- ') and ('[[' in line or ']]' in line):
            date, entry = parse_ledger_entry(line)
            # Extract the wikilink target for deduplication
            link_match = re.search(r'\[\[([^\]|]+)', entry)
            link_target = link_match.group(1) if link_match else entry
            entries.append((date, link_target, entry))
        elif line.strip():
            other_lines.append(line)
    
    # Deduplicate by link target, keeping the entry with the most recent date
    seen = {}
    for date, target, entry in entries:
        target_key = target.lower().strip()
        if target_key not in seen or date > seen[target_key][0]:
            seen[target_key] = (date, entry)
    
    # Sort by date descending
    sorted_entries = sorted(seen.values(), key=lambda x: x[0], reverse=True)
    
    result_lines = [entry for _, entry in sorted_entries]
    
    return '\n'.join(result_lines)


def normalize_person_readme(parsed: dict) -> str:
    """Normalize a person README to the standard structure."""
    sections = parsed['sections']
    
    # Build Profile section
    profile_content = sections.get('Profile', '')
    
    # Ensure we have key profile fields
    if not profile_content:
        profile_content = """**Role**: _Unknown_
**Organization**: _Unknown_
**Location**: _Unknown_
**Relationship**: _Unknown_"""
    
    # Build the new structure
    ordered_sections = OrderedDict()
    
    # 1. Profile (first)
    ordered_sections['Profile'] = profile_content
    
    # 2. Contact Info (if exists, merge into Profile or keep separate)
    if 'Contact Info' in sections:
        ordered_sections['Contact Info'] = sections['Contact Info']
    
    # 3. Open Tasks
    tasks = sections.get('Open Tasks', '')
    if not tasks:
        tasks = """```tasks
path includes {title}
not done
```""".replace('{title}', parsed['title'])
    ordered_sections['Open Tasks'] = tasks
    
    # 4. Recent Context (sorted and deduplicated)
    context = sections.get('Recent Context', '')
    if context:
        context = deduplicate_and_sort_ledger(context)
    ordered_sections['Recent Context'] = context
    
    # 5. Key Facts
    if 'Key Facts' in sections:
        ordered_sections['Key Facts'] = sections['Key Facts']
    
    # 6. Background (if separate from Profile)
    if 'Background' in sections:
        ordered_sections['Background'] = sections['Background']
    
    # 7. Topics
    if 'Topics' in sections:
        ordered_sections['Topics'] = sections['Topics']
    
    # 8. Key Decisions
    if 'Key Decisions' in sections:
        ordered_sections['Key Decisions'] = sections['Key Decisions']
    
    # 9. Related sections
    for key in ['Related Customers', 'Related Projects', 'Related']:
        if key in sections:
            ordered_sections[key] = sections[key]
    
    return build_readme(parsed, ordered_sections)


def normalize_customer_readme(parsed: dict) -> str:
    """Normalize a customer README to the standard structure."""
    sections = parsed['sections']
    
    ordered_sections = OrderedDict()
    
    # 1. Account Status (first)
    status = sections.get('Account Status', '')
    if not status:
        status = """| Field | Value |
|-------|-------|
| **Status** | _Unknown_ |
| **Industry** | _Unknown_ |"""
    ordered_sections['Account Status'] = status
    
    # 2. Key Contacts
    if 'Key Contacts' in sections:
        ordered_sections['Key Contacts'] = sections['Key Contacts']
    
    # 3. Open Tasks
    tasks = sections.get('Open Tasks', '')
    if not tasks:
        tasks = """```tasks
path includes {title}
not done
```""".replace('{title}', parsed['title'])
    ordered_sections['Open Tasks'] = tasks
    
    # 4. Recent Context (sorted and deduplicated)
    context = sections.get('Recent Context', '')
    if context:
        context = deduplicate_and_sort_ledger(context)
    ordered_sections['Recent Context'] = context
    
    # 5. Key Facts
    if 'Key Facts' in sections:
        ordered_sections['Key Facts'] = sections['Key Facts']
    
    # 6. Topics
    if 'Topics' in sections:
        ordered_sections['Topics'] = sections['Topics']
    
    # 7. Opportunities
    if 'Opportunities' in sections:
        ordered_sections['Opportunities'] = sections['Opportunities']
    
    # 8. Blockers
    if 'Blockers' in sections:
        ordered_sections['Blockers'] = sections['Blockers']
    
    # 9. Collaborators
    if 'Collaborators' in sections:
        ordered_sections['Collaborators'] = sections['Collaborators']
    
    # 10. Related
    if 'Related' in sections:
        ordered_sections['Related'] = sections['Related']
    
    return build_readme(parsed, ordered_sections)


def normalize_project_readme(parsed: dict) -> str:
    """Normalize a project README to the standard structure."""
    sections = parsed['sections']
    
    ordered_sections = OrderedDict()
    
    # 1. Status (first)
    status = sections.get('Status', '')
    if not status:
        status = """| Field | Value |
|-------|-------|
| **Status** | active |
| **Owner** | _Unknown_ |"""
    ordered_sections['Status'] = status
    
    # 2. Overview
    if 'Overview' in sections:
        ordered_sections['Overview'] = sections['Overview']
    
    # 3. Open Tasks
    tasks = sections.get('Open Tasks', '')
    if not tasks:
        tasks = """```tasks
path includes {title}
not done
```""".replace('{title}', parsed['title'])
    ordered_sections['Open Tasks'] = tasks
    
    # 4. Recent Context (sorted and deduplicated)
    context = sections.get('Recent Context', '')
    if context:
        context = deduplicate_and_sort_ledger(context)
    ordered_sections['Recent Context'] = context
    
    # 5. Key Facts
    if 'Key Facts' in sections:
        ordered_sections['Key Facts'] = sections['Key Facts']
    
    # 6. Topics
    if 'Topics' in sections:
        ordered_sections['Topics'] = sections['Topics']
    
    # 7. Blockers
    if 'Blockers' in sections:
        ordered_sections['Blockers'] = sections['Blockers']
    
    # 8. Related
    if 'Related' in sections:
        ordered_sections['Related'] = sections['Related']
    
    return build_readme(parsed, ordered_sections)


def build_readme(parsed: dict, ordered_sections: OrderedDict) -> str:
    """Build the final README content."""
    lines = []
    
    # Frontmatter
    if parsed['frontmatter']:
        lines.append('---')
        lines.append(yaml.dump(parsed['frontmatter'], default_flow_style=False, allow_unicode=True, sort_keys=False).strip())
        lines.append('---')
        lines.append('')
    
    # Title
    if parsed['title']:
        lines.append(f"# {parsed['title']}")
        lines.append('')
    
    # Sections
    for section_name, content in ordered_sections.items():
        if content and content.strip():
            lines.append(f"## {section_name}")
            lines.append('')
            lines.append(content)
            lines.append('')
    
    return '\n'.join(lines)


def normalize_readme(path: Path, entity_type: str, dry_run: bool = True) -> dict:
    """Normalize a single README file."""
    content = path.read_text()
    parsed = parse_readme(content)
    
    # Skip if no frontmatter (not a proper README)
    if not parsed['frontmatter']:
        return {'status': 'skipped', 'reason': 'no frontmatter'}
    
    # Normalize based on type
    if entity_type == 'people':
        new_content = normalize_person_readme(parsed)
    elif entity_type == 'customer':
        new_content = normalize_customer_readme(parsed)
    elif entity_type == 'projects':
        new_content = normalize_project_readme(parsed)
    else:
        return {'status': 'skipped', 'reason': f'unknown type: {entity_type}'}
    
    # Check if content changed
    if content.strip() == new_content.strip():
        return {'status': 'unchanged'}
    
    if not dry_run:
        path.write_text(new_content)
        return {'status': 'updated'}
    
    return {'status': 'would_update', 'old_len': len(content), 'new_len': len(new_content)}


def find_all_readmes(vault_root: Path) -> list:
    """Find all README files and their entity types."""
    readmes = []
    
    # People
    people_dir = vault_root / 'VAST' / 'People'
    if people_dir.exists():
        for readme in people_dir.glob('*/README.md'):
            readmes.append((readme, 'people'))
    
    # Customers
    customers_dir = vault_root / 'VAST' / 'Customers and Partners'
    if customers_dir.exists():
        for readme in customers_dir.glob('*/README.md'):
            readmes.append((readme, 'customer'))
        # Also check subdirectories (MAI, Apollo, etc.)
        for readme in customers_dir.glob('*/*/README.md'):
            readmes.append((readme, 'customer'))
    
    # Projects
    projects_dir = vault_root / 'VAST' / 'Projects'
    if projects_dir.exists():
        for readme in projects_dir.glob('*/README.md'):
            readmes.append((readme, 'projects'))
        for readme in projects_dir.glob('*/*/README.md'):
            readmes.append((readme, 'projects'))
    
    return readmes


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Normalize README structure')
    parser.add_argument('--dry-run', action='store_true', help='Preview changes without writing')
    parser.add_argument('--execute', action='store_true', help='Apply changes')
    parser.add_argument('--path', type=str, help='Normalize a specific README')
    parser.add_argument('--type', type=str, choices=['people', 'customer', 'projects'], 
                        help='Entity type (required with --path)')
    args = parser.parse_args()
    
    if not args.dry_run and not args.execute:
        print("Use --dry-run to preview or --execute to apply changes")
        return
    
    vault_root = Path(__file__).parent.parent.parent.parent
    dry_run = not args.execute
    
    if args.path:
        if not args.type:
            print("--type required with --path")
            return
        readmes = [(Path(args.path), args.type)]
    else:
        readmes = find_all_readmes(vault_root)
    
    print(f"{'DRY RUN: ' if dry_run else ''}Normalizing {len(readmes)} READMEs\n")
    
    stats = {'updated': 0, 'unchanged': 0, 'skipped': 0, 'would_update': 0}
    
    for path, entity_type in readmes:
        result = normalize_readme(path, entity_type, dry_run)
        status = result['status']
        stats[status] = stats.get(status, 0) + 1
        
        if status in ('updated', 'would_update'):
            print(f"  {'✓' if status == 'updated' else '→'} {path.parent.name}/{path.name}")
    
    print("\nSummary:")
    if dry_run:
        print(f"  Would update: {stats.get('would_update', 0)}")
    else:
        print(f"  Updated: {stats.get('updated', 0)}")
    print(f"  Unchanged: {stats.get('unchanged', 0)}")
    print(f"  Skipped: {stats.get('skipped', 0)}")


if __name__ == '__main__':
    main()
