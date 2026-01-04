#!/usr/bin/env python3
"""
Migrate old-format People READMEs to new format.

Old format:
## Contact Information
| Field | Value |
| **Role** | _Unknown_ |
...

New format:
## Profile
**Role**: _Unknown_
**Company**: _Unknown_
...
"""

import re
from pathlib import Path

VAULT_ROOT = Path(__file__).parent.parent.parent

OLD_FORMAT_PEOPLE = [
    "Jack Kabat",
    "Kanchan Mehrotra", 
    "Kishore Inampudi",
    "Kurt Niebuhr",
    "Rick Haselton",
    "Rob Banga",
    "Rob Benoit",
    "Rosanne Kincaid–Smith",
    "Vishnu Charan TJ",
    "Yogev Vankin",
]

def migrate_readme(person_name: str, dry_run: bool = True) -> bool:
    """Migrate a single README from old to new format."""
    
    readme_path = VAULT_ROOT / "VAST" / "People" / person_name / "README.md"
    if not readme_path.exists():
        print(f"  ⚠️  README not found: {readme_path}")
        return False
    
    content = readme_path.read_text(encoding='utf-8')
    
    # Check if already migrated
    if "## Profile" in content and "## Contact Information" not in content:
        print(f"  ✓ Already migrated: {person_name}")
        return True
    
    if "## Contact Information" not in content:
        print(f"  ⚠️  No Contact Information section found: {person_name}")
        return False
    
    # Extract values from the table
    role = extract_field(content, "Role")
    company = extract_field(content, "Company")
    location = extract_field(content, "Location")
    
    # Build new Profile section
    new_profile = f"""## Profile

**Role**: {role}
**Company**: {company}
**Location**: {location}
**Relationship**: _How do you work with this person?_

**Background**:
_Career history, expertise, interests..._
"""
    
    # Replace old section with new
    # Find the old Contact Information section and everything until next ##
    old_section_pattern = r'## Contact Information\n.*?(?=\n## |\n---|\Z)'
    
    new_content = re.sub(old_section_pattern, new_profile.strip(), content, flags=re.DOTALL)
    
    # Remove Relationship and Background sections if they exist (merged into Profile)
    new_content = re.sub(r'\n## Relationship\n.*?(?=\n## |\n---|\Z)', '', new_content, flags=re.DOTALL)
    new_content = re.sub(r'\n## Background\n.*?(?=\n## |\n---|\Z)', '', new_content, flags=re.DOTALL)
    
    if not dry_run:
        readme_path.write_text(new_content, encoding='utf-8')
    
    print(f"  {'[DRY] ' if dry_run else ''}Migrated: {person_name}")
    return True

def extract_field(content: str, field: str) -> str:
    """Extract a field value from the old table format."""
    # Match pattern like | **Role** | _Unknown_ |
    pattern = rf'\|\s*\*\*{field}\*\*\s*\|\s*([^|]+)\|'
    match = re.search(pattern, content)
    if match:
        value = match.group(1).strip()
        # Remove _italics_ wrapper if just _Unknown_
        if value == "_Unknown_":
            return "_Unknown_"
        return value
    return "_Unknown_"

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Migrate old-format People READMEs")
    parser.add_argument("--dry-run", action="store_true", help="Don't modify files")
    args = parser.parse_args()
    
    print(f"Migrating {len(OLD_FORMAT_PEOPLE)} READMEs...\n")
    
    migrated = 0
    for person in OLD_FORMAT_PEOPLE:
        if migrate_readme(person, dry_run=args.dry_run):
            migrated += 1
    
    print(f"\n{'[DRY RUN] ' if args.dry_run else ''}Migrated {migrated}/{len(OLD_FORMAT_PEOPLE)} READMEs")

if __name__ == "__main__":
    main()
