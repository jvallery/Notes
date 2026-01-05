#!/usr/bin/env python3
"""
Email Deduplication Script

Identifies and handles duplicate email exports in Inbox/Email.

Strategy:
- Group emails by normalized subject (strip Re:, Fwd:, [EXTERNAL], etc.)
- Within each group, keep the most complete export (highest message count)
- If same message count, keep most recent export timestamp
- Archive duplicates to Inbox/_archive/duplicates/

Usage:
    python scripts/dedupe_emails.py              # Report duplicates
    python scripts/dedupe_emails.py --apply      # Actually remove duplicates
    python scripts/dedupe_emails.py --verbose    # Show detailed analysis
"""

import re
import shutil
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional

import click
from rich.console import Console
from rich.table import Table

import sys
sys.path.insert(0, str(Path(__file__).parent))
from utils import vault_root


console = Console()


@dataclass
class EmailFile:
    """Represents an exported email file with parsed metadata."""
    path: Path
    export_timestamp: str  # From filename: YYYY-MM-DD_HHMMSS
    random_id: str  # 4-digit suffix
    subject_slug: str  # Slugified subject from filename
    raw_subject: str  # First line of file (actual subject)
    message_count: int  # "Messages: N" from header
    export_datetime: Optional[datetime]  # Parsed from file header
    
    def __post_init__(self):
        """Parse export datetime from file content."""
        try:
            content = self.path.read_text()[:500]
            # Look for "- Exported: YYYY-MM-DD HH:MM:SS"
            match = re.search(r'Exported:\s*(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})', content)
            if match:
                self.export_datetime = datetime.strptime(match.group(1), "%Y-%m-%d %H:%M:%S")
            else:
                self.export_datetime = None
        except Exception:
            self.export_datetime = None


def parse_email_filename(path: Path) -> Optional[EmailFile]:
    """Parse email filename into components.
    
    Format: YYYY-MM-DD_HHMMSS_XXXX_Subject-slug.md
    """
    filename = path.stem
    
    # Pattern: date_time_id_subject
    match = re.match(r'^(\d{4}-\d{2}-\d{2})_(\d{6})_(\d{4})_(.+)$', filename)
    if not match:
        return None
    
    date, time, random_id, subject_slug = match.groups()
    
    # Parse message count from file
    message_count = 1
    raw_subject = ""
    try:
        content = path.read_text()[:1000]
        
        # First line is raw subject (# Subject)
        first_line = content.split('\n')[0]
        if first_line.startswith('# '):
            raw_subject = first_line[2:].strip()
        else:
            raw_subject = first_line.strip()
        
        # Look for "- Messages: N"
        msg_match = re.search(r'Messages:\s*(\d+)', content)
        if msg_match:
            message_count = int(msg_match.group(1))
    except Exception:
        pass
    
    return EmailFile(
        path=path,
        export_timestamp=f"{date}_{time}",
        random_id=random_id,
        subject_slug=subject_slug,
        raw_subject=raw_subject,
        message_count=message_count,
        export_datetime=None,  # Will be set in __post_init__
    )


def normalize_subject(subject: str) -> str:
    """Normalize email subject for grouping.
    
    Strips: Re:, Fwd:, FW:, [EXTERNAL], [EXTERNAL RE], etc.
    """
    s = subject.strip()
    
    # Remove common prefixes (case-insensitive, possibly repeated)
    patterns = [
        r'^\s*\[EXTERNAL\s*RE?\]\s*',
        r'^\s*RE:\s*',
        r'^\s*Re:\s*',
        r'^\s*FW:\s*',
        r'^\s*Fwd:\s*',
        r'^\s*\[EXTERNAL\]\s*',
    ]
    
    changed = True
    while changed:
        changed = False
        for pattern in patterns:
            new_s = re.sub(pattern, '', s, flags=re.IGNORECASE)
            if new_s != s:
                s = new_s
                changed = True
    
    # Normalize whitespace
    s = re.sub(r'\s+', ' ', s).strip()
    
    return s.lower()


def find_email_files() -> list[EmailFile]:
    """Find all email files in Inbox/Email."""
    email_dir = vault_root() / "Inbox" / "Email"
    if not email_dir.exists():
        return []
    
    emails = []
    for path in email_dir.glob("*.md"):
        email = parse_email_filename(path)
        if email:
            emails.append(email)
    
    return emails


def group_by_thread(emails: list[EmailFile]) -> dict[str, list[EmailFile]]:
    """Group emails by normalized subject (thread key)."""
    groups = defaultdict(list)
    
    for email in emails:
        # Use normalized raw_subject as the thread key
        key = normalize_subject(email.raw_subject)
        if not key:
            key = normalize_subject(email.subject_slug.replace('-', ' '))
        groups[key].append(email)
    
    # Sort each group by message_count (desc), then export_datetime (desc)
    for key in groups:
        groups[key].sort(
            key=lambda e: (
                e.message_count,
                e.export_datetime or datetime.min
            ),
            reverse=True
        )
    
    return dict(groups)


def identify_duplicates(groups: dict[str, list[EmailFile]]) -> tuple[list[EmailFile], list[EmailFile]]:
    """Identify which emails to keep vs archive.
    
    Returns:
        (keep_list, archive_list)
    """
    keep = []
    archive = []
    
    for thread_key, emails in groups.items():
        if len(emails) == 1:
            keep.append(emails[0])
        else:
            # Keep first (best - most messages, most recent)
            keep.append(emails[0])
            # Archive the rest
            archive.extend(emails[1:])
    
    return keep, archive


def archive_duplicates(duplicates: list[EmailFile], dry_run: bool = True) -> list[Path]:
    """Move duplicate emails to archive folder.
    
    Returns list of paths that were (or would be) moved.
    """
    archive_dir = vault_root() / "Inbox" / "_archive" / "duplicates"
    
    if not dry_run:
        archive_dir.mkdir(parents=True, exist_ok=True)
    
    moved = []
    for email in duplicates:
        dest = archive_dir / email.path.name
        if not dry_run:
            shutil.move(str(email.path), str(dest))
        moved.append(dest)
    
    return moved


@click.command()
@click.option('--apply', is_flag=True, help='Actually archive duplicates (default is dry-run)')
@click.option('--verbose', '-v', is_flag=True, help='Show detailed analysis')
def main(apply: bool, verbose: bool):
    """Deduplicate email exports in Inbox/Email."""
    
    console.print("[bold blue]Email Deduplication[/bold blue]")
    console.print("=" * 50)
    
    # Find all email files
    emails = find_email_files()
    console.print(f"Found [bold]{len(emails)}[/bold] email files")
    
    if not emails:
        return
    
    # Group by thread
    groups = group_by_thread(emails)
    console.print(f"Identified [bold]{len(groups)}[/bold] unique threads")
    
    # Find duplicates
    keep, archive = identify_duplicates(groups)
    
    duplicate_count = len(archive)
    if duplicate_count == 0:
        console.print("[green]No duplicates found![/green]")
        return
    
    console.print(f"\n[yellow]Found {duplicate_count} duplicate(s) to archive[/yellow]")
    
    if verbose:
        # Show duplicate groups
        table = Table(title="Duplicate Groups")
        table.add_column("Thread Subject", style="cyan", max_width=50)
        table.add_column("Keep", style="green")
        table.add_column("Archive", style="red")
        
        for thread_key, emails in groups.items():
            if len(emails) > 1:
                keep_email = emails[0]
                archive_emails = emails[1:]
                
                table.add_row(
                    thread_key[:50] + "..." if len(thread_key) > 50 else thread_key,
                    f"{keep_email.path.name}\n(msgs: {keep_email.message_count})",
                    "\n".join(f"{e.path.name} (msgs: {e.message_count})" for e in archive_emails),
                )
        
        console.print(table)
    
    # Show summary
    console.print(f"\n[bold]Summary:[/bold]")
    console.print(f"  Keep: {len(keep)} files")
    console.print(f"  Archive: {len(archive)} files")
    
    if not apply:
        console.print("\n[dim]Run with --apply to actually archive duplicates[/dim]")
        return
    
    # Actually archive
    console.print("\n[bold]Archiving duplicates...[/bold]")
    moved = archive_duplicates(archive, dry_run=False)
    
    console.print(f"[green]Archived {len(moved)} files to Inbox/_archive/duplicates/[/green]")


if __name__ == "__main__":
    main()
