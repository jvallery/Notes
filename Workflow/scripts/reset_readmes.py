#!/usr/bin/env python3
"""
Reset README.md files to clean state.

Clears accumulated sections while preserving structure:
- Open Tasks → cleared (Dataview query preserved)
- Recent Context → cleared to empty list
- Key Facts → cleared to empty list
- Topics → removed entirely
- Key Decisions → cleared to empty list

Usage:
    python scripts/reset_readmes.py --dry-run          # Preview changes
    python scripts/reset_readmes.py                    # Execute
    python scripts/reset_readmes.py --entity-type people  # Only people
"""

import argparse
import re
import sys
from pathlib import Path

# Ensure imports work
SCRIPTS_DIR = Path(__file__).parent
WORKFLOW_DIR = SCRIPTS_DIR.parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))
if str(WORKFLOW_DIR) not in sys.path:
    sys.path.insert(0, str(WORKFLOW_DIR))

from scripts.utils.config import vault_root


def reset_readme(readme_path: Path, dry_run: bool = False) -> dict:
    """
    Reset a README to clean state.
    
    Returns dict with:
        - modified: bool
        - sections_cleared: list of section names
        - errors: list of error messages
    """
    result = {
        "modified": False,
        "sections_cleared": [],
        "errors": []
    }
    
    try:
        content = readme_path.read_text(encoding="utf-8")
    except Exception as e:
        result["errors"].append(f"Failed to read: {e}")
        return result
    
    original = content
    
    # Sections to clear (preserve heading, clear content until next heading)
    sections_to_clear = [
        "## Recent Context",
        "## Key Facts", 
        "## Topics",
        "## Key Decisions",
        "## Related Customers",
        "## Related Projects",
        "## Related People",
    ]
    
    for section in sections_to_clear:
        # Pattern: heading + everything until next ## heading or end
        pattern = rf"({re.escape(section)})\n(.*?)(?=\n## |\n---|\Z)"
        match = re.search(pattern, content, re.DOTALL)
        
        if match:
            old_content = match.group(2).strip()
            if old_content:  # Only clear if there's content
                # Replace with just the heading and empty line
                content = re.sub(
                    pattern,
                    rf"\1\n\n",
                    content,
                    flags=re.DOTALL
                )
                result["sections_cleared"].append(section)
    
    # Special handling for Open Tasks - preserve Dataview query, clear manual tasks
    open_tasks_pattern = r"(## Open Tasks\n)(.*?)(```dataview.*?```)"
    match = re.search(open_tasks_pattern, content, re.DOTALL)
    if match:
        manual_tasks = match.group(2).strip()
        if manual_tasks and not manual_tasks.startswith("```"):
            # There are manual task items before the Dataview block
            content = re.sub(
                open_tasks_pattern,
                r"\1\n\3",
                content,
                flags=re.DOTALL
            )
            result["sections_cleared"].append("## Open Tasks (manual items)")
    
    # Also handle Open Tasks without Dataview query
    open_tasks_simple = r"(## Open Tasks\n)(- \[.\].*?)(?=\n## |\Z)"
    if re.search(open_tasks_simple, content, re.DOTALL):
        content = re.sub(
            open_tasks_simple,
            r"\1\n",
            content,
            flags=re.DOTALL
        )
        if "## Open Tasks" not in str(result["sections_cleared"]):
            result["sections_cleared"].append("## Open Tasks")
    
    # Clean up multiple blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    if content != original:
        result["modified"] = True
        if not dry_run:
            readme_path.write_text(content, encoding="utf-8")
    
    return result


def find_readmes(vault: Path, entity_type: str = None) -> list[Path]:
    """Find all entity README.md files."""
    readmes = []
    
    # Entity folder patterns
    patterns = {
        "people": [
            vault / "VAST" / "People",
            vault / "Personal" / "People",
        ],
        "customers": [
            vault / "VAST" / "Customers and Partners",
        ],
        "projects": [
            vault / "VAST" / "Projects",
            vault / "Personal" / "Projects",
        ],
    }
    
    # Filter by type if specified
    if entity_type:
        if entity_type not in patterns:
            print(f"Unknown entity type: {entity_type}")
            print(f"Valid types: {list(patterns.keys())}")
            return []
        patterns = {entity_type: patterns[entity_type]}
    
    for type_name, folders in patterns.items():
        for folder in folders:
            if not folder.exists():
                continue
            # Each subfolder is an entity
            for entity_folder in folder.iterdir():
                if entity_folder.is_dir():
                    readme = entity_folder / "README.md"
                    if readme.exists():
                        readmes.append(readme)
    
    return readmes


def main():
    parser = argparse.ArgumentParser(description="Reset README files to clean state")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without modifying files"
    )
    parser.add_argument(
        "--entity-type",
        choices=["people", "customers", "projects"],
        help="Only reset specific entity type"
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Show detailed output"
    )
    
    args = parser.parse_args()
    vault = vault_root()
    
    print(f"Vault: {vault}")
    if args.dry_run:
        print("DRY RUN - no files will be modified\n")
    
    readmes = find_readmes(vault, args.entity_type)
    print(f"Found {len(readmes)} README files\n")
    
    modified_count = 0
    error_count = 0
    
    for readme in sorted(readmes):
        rel_path = readme.relative_to(vault)
        result = reset_readme(readme, dry_run=args.dry_run)
        
        if result["errors"]:
            error_count += 1
            print(f"✗ {rel_path}")
            for err in result["errors"]:
                print(f"  Error: {err}")
        elif result["modified"]:
            modified_count += 1
            print(f"✓ {rel_path}")
            if args.verbose:
                for section in result["sections_cleared"]:
                    print(f"  Cleared: {section}")
        elif args.verbose:
            print(f"○ {rel_path} (no changes)")
    
    print(f"\n{'Would modify' if args.dry_run else 'Modified'}: {modified_count} files")
    if error_count:
        print(f"Errors: {error_count}")
    
    return 0 if error_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
