#!/usr/bin/env python3
"""
Cleanup _NEW_* entity folders by merging into correct destinations.

This script:
1. Identifies _NEW_* folders and their contents
2. Maps them to correct destinations (existing or new)
3. Moves notes to correct locations
4. Cleans up empty folders

Run with --dry-run to preview changes.
"""

import argparse
import shutil
from pathlib import Path
from typing import NamedTuple


class MoveOperation(NamedTuple):
    src: Path
    dst: Path
    action: str  # 'move', 'merge', 'delete', 'manual'


# Mapping of _NEW_* folders to their correct destinations
# Format: (_NEW_ folder name, destination path, action notes)
FOLDER_MAPPINGS = {
    # Customers and Partners/_NEW_* → People (these are people, not customers)
    "VAST/Customers and Partners/_NEW_Jai Menon": ("VAST/People/Jai Menon", "merge"),
    "VAST/Customers and Partners/_NEW_Jeff Denworth": ("VAST/People/Jeff Denworth", "merge"),
    "VAST/Customers and Partners/_NEW_Maneesh Sah": ("VAST/People/Maneesh Sah", "merge"),
    "VAST/Customers and Partners/_NEW_Timo Pervane": ("VAST/People/Timo Pervane", "merge"),
    "VAST/Customers and Partners/_NEW_Deandre Jackson": ("VAST/People/Deandre Jackson", "merge"),
    "VAST/Customers and Partners/_NEW_Yogev Vankin": ("VAST/People/Yogev Vankin", "merge"),
    "VAST/Customers and Partners/_NEW_/Jonsi Stephenson": ("VAST/People/Jonsi Stephenson", "merge"),
    "VAST/Customers and Partners/_NEW_/Asaf Levy": ("VAST/People/Asaf Levy", "merge"),
    
    # _NEW_VAST is invalid - VAST is the company itself
    "VAST/Customers and Partners/_NEW_VAST": (None, "delete"),
    
    # _NEW_Pricing → Projects
    "VAST/Customers and Partners/_NEW_Pricing": ("VAST/Projects/Pricing", "merge"),
    
    # _NEW_Dhammak - appears to be new customer, needs review
    "VAST/Customers and Partners/_NEW_Dhammak": ("VAST/Customers and Partners/Dhammak", "create"),
    
    # People/_NEW_* mappings
    "VAST/People/_NEW_Tomer": ("VAST/People/Tomer Hagay", "merge"),
    "VAST/People/_NEW_Roy": ("VAST/People/Roy Sterman", "merge"),
    "VAST/People/_NEW_JB": ("VAST/People/JB", "create"),  # Unknown person
    "VAST/People/_NEW_John": ("VAST/People/John Mao", "merge"),  # Best guess - needs review
    "VAST/People/_NEW_Nidhi": ("VAST/People/Nidhi", "create"),  # New person
    "VAST/People/_NEW_/Aaron Chaisson": ("VAST/People/Aaron Chaisson", "create"),
    
    # Projects misplaced in People
    "VAST/People/_NEW_Cloud Marketplace MVP": ("VAST/Projects/Cloud Marketplace MVP", "create"),
    "VAST/People/_NEW_Longmont Public Media": ("Personal/Projects/LPM", "merge"),
}


def get_vault_root() -> Path:
    """Get vault root from script location."""
    return Path(__file__).parent.parent.parent


def find_new_folders(vault_root: Path) -> list[Path]:
    """Find all _NEW_* folders in the vault."""
    folders = []
    for pattern in ["VAST/**/_NEW_*", "Personal/**/_NEW_*"]:
        folders.extend(vault_root.glob(pattern))
    # Also find bare _NEW_ folders (not _NEW_Name)
    for pattern in ["VAST/**/_NEW_", "Personal/**/_NEW_"]:
        for f in vault_root.glob(pattern):
            if f.is_dir():
                folders.append(f)
    return sorted(set(folders))


def get_files_in_folder(folder: Path) -> list[Path]:
    """Get all markdown files in a folder (non-recursive for notes, recursive for subfolders)."""
    files = []
    for f in folder.iterdir():
        if f.is_file() and f.suffix == ".md":
            files.append(f)
        elif f.is_dir():
            # This handles nested _NEW_/Person/ structure
            files.extend(get_files_in_folder(f))
    return files


def plan_operations(vault_root: Path, new_folders: list[Path], dry_run: bool = True) -> list[MoveOperation]:
    """Plan all move/merge/delete operations."""
    ops = []
    processed_folders = set()  # Track folders we've handled
    
    for folder in new_folders:
        rel_path = str(folder.relative_to(vault_root))
        
        # Handle bare _NEW_ folders with subfolders first
        if rel_path.endswith("_NEW_"):
            processed_folders.add(rel_path)
            for subfolder in folder.iterdir():
                if subfolder.is_dir():
                    sub_rel = str(subfolder.relative_to(vault_root))
                    if sub_rel in FOLDER_MAPPINGS:
                        dest_path, action = FOLDER_MAPPINGS[sub_rel]
                        if dest_path and action != "delete":
                            dest = vault_root / dest_path
                            files = get_files_in_folder(subfolder)
                            for f in files:
                                if f.name == "README.md":
                                    if (dest / "README.md").exists():
                                        ops.append(MoveOperation(f, Path(""), "skip-readme"))
                                    else:
                                        ops.append(MoveOperation(f, dest / "README.md", action))
                                else:
                                    ops.append(MoveOperation(f, dest / f.name, "move"))
                    else:
                        print(f"⚠️  No mapping for nested: {sub_rel}")
                        ops.append(MoveOperation(subfolder, Path(""), "manual"))
            continue
        
        # Skip if already processed as part of parent (direct children only)
        parent_rel = str(folder.parent.relative_to(vault_root))
        if parent_rel in processed_folders:
            continue
        
        # Check if we have a mapping
        if rel_path in FOLDER_MAPPINGS:
            dest_path, action = FOLDER_MAPPINGS[rel_path]
            
            if action == "delete":
                ops.append(MoveOperation(folder, Path(""), "delete"))
                continue
                
            if dest_path is None:
                continue
                
            dest = vault_root / dest_path
            
            # Get all files to move
            files = get_files_in_folder(folder)
            for f in files:
                if f.name == "README.md":
                    # Don't move stub READMEs over existing ones
                    if (dest / "README.md").exists():
                        ops.append(MoveOperation(f, Path(""), "skip-readme"))
                    else:
                        ops.append(MoveOperation(f, dest / "README.md", action))
                else:
                    # Move note files
                    ops.append(MoveOperation(f, dest / f.name, "move"))
        else:
            # Unknown mapping - needs manual review
            print(f"⚠️  No mapping for: {rel_path}")
            ops.append(MoveOperation(folder, Path(""), "manual"))
    
    return ops


def execute_operations(vault_root: Path, ops: list[MoveOperation], dry_run: bool = True):
    """Execute the planned operations."""
    for op in ops:
        if op.action == "manual":
            print(f"⚠️  MANUAL: {op.src}")
            continue
            
        if op.action == "skip-readme":
            print(f"⏭️  SKIP (exists): {op.src}")
            if not dry_run:
                op.src.unlink()
            continue
            
        if op.action == "delete":
            print(f"🗑️  DELETE: {op.src}")
            if not dry_run:
                if op.src.is_dir():
                    shutil.rmtree(op.src)
                else:
                    op.src.unlink()
            continue
        
        # move or merge
        print(f"📦 {op.action.upper()}: {op.src} → {op.dst}")
        if not dry_run:
            op.dst.parent.mkdir(parents=True, exist_ok=True)
            if op.dst.exists():
                print(f"   ⚠️  Destination exists, skipping: {op.dst}")
            else:
                shutil.move(str(op.src), str(op.dst))


def cleanup_empty_folders(vault_root: Path, dry_run: bool = True):
    """Remove empty _NEW_* folders after moves."""
    for folder in find_new_folders(vault_root):
        if folder.exists() and not any(folder.iterdir()):
            print(f"🧹 EMPTY: {folder}")
            if not dry_run:
                folder.rmdir()
    
    # Also check for empty parent _NEW_ folders
    for pattern in ["VAST/**/_NEW_", "Personal/**/_NEW_"]:
        for folder in vault_root.glob(pattern):
            if folder.is_dir() and not any(folder.iterdir()):
                print(f"🧹 EMPTY: {folder}")
                if not dry_run:
                    folder.rmdir()


def delete_vast_accounts(vault_root: Path, dry_run: bool = True):
    """Delete the invalid VAST/Accounts/ folder."""
    accounts_folder = vault_root / "VAST" / "Accounts"
    if accounts_folder.exists():
        print(f"\n🗑️  DELETE INVALID: {accounts_folder}")
        for f in accounts_folder.rglob("*"):
            print(f"   - {f.relative_to(vault_root)}")
        if not dry_run:
            shutil.rmtree(accounts_folder)


def main():
    parser = argparse.ArgumentParser(description="Cleanup _NEW_* entity folders")
    parser.add_argument("--dry-run", action="store_true", default=True,
                        help="Preview changes without executing (default)")
    parser.add_argument("--execute", action="store_true",
                        help="Actually execute the changes")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Show detailed output")
    args = parser.parse_args()
    
    dry_run = not args.execute
    
    vault_root = get_vault_root()
    print(f"Vault root: {vault_root}")
    print(f"Mode: {'DRY RUN' if dry_run else '⚡ EXECUTING'}\n")
    
    # Find all _NEW_* folders
    new_folders = find_new_folders(vault_root)
    print(f"Found {len(new_folders)} _NEW_* folders:\n")
    for f in new_folders:
        print(f"  {f.relative_to(vault_root)}")
    print()
    
    # Plan operations
    ops = plan_operations(vault_root, new_folders, dry_run)
    
    # Execute
    print("\n--- Operations ---\n")
    execute_operations(vault_root, ops, dry_run)
    
    # Cleanup empty folders
    print("\n--- Cleanup ---\n")
    cleanup_empty_folders(vault_root, dry_run)
    
    # Delete invalid VAST/Accounts
    delete_vast_accounts(vault_root, dry_run)
    
    if dry_run:
        print("\n✅ Dry run complete. Run with --execute to apply changes.")
    else:
        print("\n✅ Cleanup complete!")


if __name__ == "__main__":
    main()
