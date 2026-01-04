#!/usr/bin/env python3
"""
Collect all transcripts into Inbox/Transcripts/ for reprocessing.

Sources:
- Sources/Transcripts/**/*.md - Previously processed transcripts with embedded raw
- Inbox/_archive/**/*.md - Recently processed (restore)
- Personal/Projects/*/YYYY-*.md - Scattered meeting notes

Usage:
    python scripts/collect_transcripts.py --dry-run
    python scripts/collect_transcripts.py
"""

import argparse
import shutil
import re
from pathlib import Path
from datetime import datetime


def is_transcript(filepath: Path) -> bool:
    """Check if a file looks like a transcript (has speaker patterns)."""
    try:
        content = filepath.read_text()
        # Check for speaker patterns
        patterns = [
            r'\*\*[A-Z][a-z]+.*\*\*:',  # **Speaker Name**:
            r'^\*\*Speaker \d+\*\*:',    # **Speaker 1**:
            r'^\[[\d:]+\]',              # [00:01:23] timestamp
            r'^Speaker \d+:',            # Speaker 1:
        ]
        for pattern in patterns:
            if re.search(pattern, content, re.MULTILINE):
                return True
                
        # Check for transcript code block
        if '## Transcript' in content or '```text\n[' in content:
            return True
            
        return False
    except Exception:
        return False


def sanitize_filename(name: str) -> str:
    """Clean up filename for consistency."""
    # Remove characters that cause issues
    cleaned = re.sub(r'[<>:"/\\|?*]', '', name)
    # Collapse multiple spaces
    cleaned = re.sub(r' +', ' ', cleaned)
    # Trim
    return cleaned.strip()


def get_transcript_date(filepath: Path) -> str:
    """Extract date from filename or content."""
    name = filepath.stem
    
    # Try YYYY-MM-DD at start
    match = re.match(r'(\d{4}-\d{2}-\d{2})', name)
    if match:
        return match.group(1)
    
    # Try YYYY-MM-DD with spaces instead of dashes
    match = re.match(r'(\d{4}) (\d{2}) (\d{2})', name)
    if match:
        return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
    
    # Default to today
    return datetime.now().strftime('%Y-%m-%d')


def collect_transcripts(vault_root: Path, dry_run: bool = True) -> dict:
    """Collect all transcripts to Inbox/Transcripts/."""
    
    inbox_transcripts = vault_root / "Inbox" / "Transcripts"
    sources = []
    
    # 1. Sources/Transcripts/**/*.md
    sources_dir = vault_root / "Sources" / "Transcripts"
    if sources_dir.exists():
        for f in sources_dir.rglob("*.md"):
            sources.append(("Sources/Transcripts", f))
    
    # 2. Inbox/_archive/**/*.md (transcripts only)
    archive_dir = vault_root / "Inbox" / "_archive"
    if archive_dir.exists():
        for f in archive_dir.rglob("*.md"):
            if is_transcript(f):
                sources.append(("Inbox/_archive", f))
    
    # 3. Personal/Projects with transcript patterns
    personal_projects = vault_root / "Personal" / "Projects"
    if personal_projects.exists():
        for f in personal_projects.rglob("*.md"):
            if f.name != "README.md" and re.match(r'\d{4}', f.name):
                if is_transcript(f):
                    sources.append(("Personal/Projects", f))
    
    results = {
        "found": [],
        "copied": [],
        "skipped": [],
        "errors": []
    }
    
    for source_type, filepath in sources:
        # Generate target filename
        date = get_transcript_date(filepath)
        
        # Create clean filename
        name = filepath.stem
        # Ensure date is at start with proper format
        if not name.startswith(date):
            # Strip any existing date prefix
            name = re.sub(r'^\d{4}[-\s]\d{2}[-\s]\d{2}\s*[-_]?\s*', '', name)
            name = f"{date} - {name}"
        
        target_name = sanitize_filename(name) + ".md"
        target = inbox_transcripts / target_name
        
        results["found"].append({
            "source": str(filepath.relative_to(vault_root)),
            "target": str(target.relative_to(vault_root)),
            "type": source_type
        })
        
        if target.exists():
            results["skipped"].append({
                "source": str(filepath.relative_to(vault_root)),
                "reason": "target exists"
            })
            continue
        
        if dry_run:
            results["copied"].append({
                "source": str(filepath.relative_to(vault_root)),
                "target": str(target.relative_to(vault_root))
            })
        else:
            try:
                inbox_transcripts.mkdir(parents=True, exist_ok=True)
                shutil.copy2(filepath, target)
                results["copied"].append({
                    "source": str(filepath.relative_to(vault_root)),
                    "target": str(target.relative_to(vault_root))
                })
            except Exception as e:
                results["errors"].append({
                    "source": str(filepath.relative_to(vault_root)),
                    "error": str(e)
                })
    
    return results


def main():
    parser = argparse.ArgumentParser(description="Collect all transcripts for reprocessing")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done")
    parser.add_argument("--vault", type=Path, default=Path(__file__).parent.parent.parent,
                        help="Path to vault root")
    args = parser.parse_args()
    
    vault_root = args.vault.resolve()
    print(f"Vault root: {vault_root}")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'EXECUTE'}")
    print()
    
    results = collect_transcripts(vault_root, args.dry_run)
    
    # Summary by source type
    by_type = {}
    for item in results["found"]:
        t = item["type"]
        by_type[t] = by_type.get(t, 0) + 1
    
    print("=== Sources Found ===")
    for t, count in sorted(by_type.items()):
        print(f"  {t}: {count}")
    print(f"  TOTAL: {len(results['found'])}")
    print()
    
    if results["skipped"]:
        print(f"=== Skipped (already exist): {len(results['skipped'])} ===")
        for item in results["skipped"][:5]:
            print(f"  ⏭ {item['source']}")
        if len(results["skipped"]) > 5:
            print(f"  ... and {len(results['skipped']) - 5} more")
        print()
    
    print(f"=== {'Would Copy' if args.dry_run else 'Copied'}: {len(results['copied'])} ===")
    for item in results["copied"][:10]:
        print(f"  → {item['target']}")
    if len(results["copied"]) > 10:
        print(f"  ... and {len(results['copied']) - 10} more")
    print()
    
    if results["errors"]:
        print(f"=== Errors: {len(results['errors'])} ===")
        for item in results["errors"]:
            print(f"  ✗ {item['source']}: {item['error']}")
        print()
    
    if args.dry_run:
        print("Run without --dry-run to execute.")


if __name__ == "__main__":
    main()
