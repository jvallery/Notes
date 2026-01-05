#!/usr/bin/env python3
"""
Unified Ingest CLI - Process all content types through unified pipeline.

Usage:
    python ingest.py --all                        # Process all pending Inbox content
    python ingest.py --type email                 # Process only emails
    python ingest.py --type transcript            # Process only transcripts
    python ingest.py --file path/to/file          # Process single file
    python ingest.py --source --type email --force  # Re-process archived sources
    python ingest.py --dry-run                    # Preview without changes
    python ingest.py --verbose                    # Show extraction details
    python ingest.py --enrich                     # Trigger enrichment for new entities
    python ingest.py --draft-replies              # Generate draft email replies
    python ingest.py --trace-dir /tmp/traces      # Save extraction/changeplan artifacts
"""

import sys
from pathlib import Path
from datetime import datetime

import click
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from pipeline import UnifiedPipeline
from pipeline.envelope import ContentType


console = Console()


@click.command()
@click.option("--type", "content_type", type=click.Choice(["email", "transcript", "document", "voice", "all"]), default="all", help="Content type to process")
@click.option("--file", "file_path", type=click.Path(), help="Process single file")
@click.option("--dry-run", is_flag=True, help="Preview without making changes")
@click.option("--verbose", "-v", is_flag=True, help="Show extraction details")
@click.option("--enrich", is_flag=True, help="Trigger enrichment for new entities")
@click.option("--draft-replies", is_flag=True, help="Generate draft email replies")
@click.option("--source", is_flag=True, help="Re-process from Sources/ directory")
@click.option("--force", is_flag=True, help="Skip duplicate detection, reprocess even if already extracted")
@click.option("--trace-dir", type=click.Path(), help="Persist extraction/changeplan artifacts to this directory")
@click.option("--vault-root", type=click.Path(), help="Override vault root (defaults to repo root)")
def main(content_type: str, file_path: str, dry_run: bool, verbose: bool, enrich: bool, draft_replies: bool, source: bool, force: bool, trace_dir: str, vault_root: str):
    """Unified content ingest pipeline.
    
    Processes emails, transcripts, documents, and voice memos through a unified
    extraction and patching pipeline.
    """
    
    vault_root_path = Path(vault_root).expanduser().resolve() if vault_root else Path(__file__).parent.parent.parent
    type_map = {
        "email": ContentType.EMAIL,
        "transcript": ContentType.TRANSCRIPT,
        "document": ContentType.DOCUMENT,
        "voice": ContentType.VOICE,
    }
    
    console.print(Panel.fit(
        "[bold blue]Unified Ingest Pipeline[/bold blue]",
        subtitle=f"{'DRY RUN' if dry_run else 'LIVE'}"
    ))
    
    # Initialize pipeline
    pipeline = UnifiedPipeline(
        vault_root=vault_root_path,
        dry_run=dry_run,
        verbose=verbose,
        generate_outputs=draft_replies,
        force=force,
        trace_dir=Path(trace_dir) if trace_dir else None,
    )
    
    # Process based on options
    if file_path:
        # Single file
        target_path = Path(file_path)
        if not target_path.is_absolute():
            target_path = vault_root_path / target_path
        if not target_path.exists():
            raise click.ClickException(f"File not found: {target_path}")
        result = pipeline.process_file(target_path)
        _display_result(result, verbose)
        
    elif source:
        # Re-process already archived sources
        selected = type_map.get(content_type) if content_type != "all" else None
        batch = pipeline.process_sources(selected)
        _display_batch(batch, verbose)
    elif content_type == "all":
        # All content types from Inbox
        batch = pipeline.process_all()
        _display_batch(batch, verbose)
    else:
        # Specific content type from Inbox
        selected = type_map[content_type]
        batch = pipeline.process_type(selected)
        _display_batch(batch, verbose)
    
    # Run enrichment if requested
    if enrich and not dry_run:
        _run_enrichment(vault_root_path, verbose)
    
    # Git commit if not dry run
    if not dry_run:
        _git_commit(vault_root_path)


def _display_result(result, verbose: bool):
    """Display single processing result."""
    if result.success:
        console.print(f"[green]✓[/green] {result.source_path}")
        
        if verbose and result.extraction:
            console.print(f"  Type: {result.content_type}")
            console.print(f"  Summary: {result.extraction.get('summary', '')[:80]}...")
            console.print(f"  Facts: {len(result.extraction.get('facts', []))}")
            console.print(f"  Tasks: {len(result.extraction.get('tasks', []))}")
        
        if result.apply_result:
            console.print(f"  Created: {len(result.apply_result.files_created)}")
            console.print(f"  Modified: {len(result.apply_result.files_modified)}")
        
        if result.draft_reply:
            console.print(f"  [blue]Draft reply generated[/blue]")
    else:
        console.print(f"[red]✗[/red] {result.source_path}")
        for error in result.errors:
            console.print(f"  [red]{error}[/red]")


def _display_batch(batch, verbose: bool):
    """Display batch processing results."""
    
    # Summary table
    table = Table(title="Processing Summary")
    table.add_column("Metric", style="cyan")
    table.add_column("Count", justify="right")
    
    table.add_row("Total", str(batch.total))
    table.add_row("Success", f"[green]{batch.success}[/green]")
    table.add_row("Failed", f"[red]{batch.failed}[/red]" if batch.failed else "0")
    table.add_row("Skipped", f"[yellow]{batch.skipped}[/yellow]" if batch.skipped else "0")
    
    console.print(table)
    
    # Individual results
    if verbose or batch.failed > 0:
        console.print("\n[bold]Details:[/bold]")
        for result in batch.results:
            _display_result(result, verbose)


def _run_enrichment(vault_root: Path, verbose: bool):
    """Run enrichment for newly created entities."""
    console.print("\n[bold]Running enrichment...[/bold]")
    
    # Import enrichment module
    try:
        from scripts.enrich_person import enrich_sparse_people
        
        # Find and enrich sparse people
        count = enrich_sparse_people(vault_root, level=2, limit=5, verbose=verbose)
        console.print(f"  Enriched {count} people")
    except ImportError:
        console.print("  [yellow]Enrichment module not available[/yellow]")
    except Exception as e:
        console.print(f"  [red]Enrichment failed: {e}[/red]")


def _git_commit(vault_root: Path):
    """Commit changes to git."""
    import subprocess
    
    try:
        # Check for changes
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=vault_root,
            capture_output=True,
            text=True
        )
        
        if not result.stdout.strip():
            return  # No changes
        
        # Stage and commit
        subprocess.run(["git", "add", "-A"], cwd=vault_root, check=True)
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        message = f"[auto] Unified ingest: {timestamp}"
        
        subprocess.run(
            ["git", "commit", "-m", message],
            cwd=vault_root,
            check=True,
            capture_output=True
        )
        
        console.print(f"\n[green]Committed changes[/green]")
        
    except subprocess.CalledProcessError as e:
        console.print(f"[yellow]Git commit skipped: {e}[/yellow]")


if __name__ == "__main__":
    main()
