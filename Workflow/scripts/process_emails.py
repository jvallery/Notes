#!/usr/bin/env python3
"""
Email Processing Pipeline

Unified pipeline for processing emails from import to action:

1. DEDUPE - Remove duplicate email exports (same thread, different exports)
2. INGEST - Extract knowledge and patch vault (contacts, tasks, facts → READMEs)
3. DRAFT - Generate response drafts for emails needing replies

Usage:
    python scripts/process_emails.py              # Run all phases
    python scripts/process_emails.py --phase dedupe  # Run single phase
    python scripts/process_emails.py --phase ingest  # Extract → Patch vault
    python scripts/process_emails.py --dry-run   # Preview without changes
"""

import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

sys.path.insert(0, str(Path(__file__).parent))
from utils import vault_root


console = Console()


@click.command()
@click.option(
    "--phase", "-p",
    type=click.Choice(["dedupe", "ingest", "draft", "all"]),
    default="all",
    help="Which phase(s) to run"
)
@click.option("--dry-run", is_flag=True, help="Preview without making changes")
@click.option("--verbose", "-v", is_flag=True, help="Show detailed output")
@click.option("--limit", "-n", type=int, default=None, help="Limit emails to process")
def main(phase: str, dry_run: bool, verbose: bool, limit: Optional[int]):
    """Run the email processing pipeline."""
    
    console.print(Panel.fit(
        "[bold blue]Email Processing Pipeline[/bold blue]",
        subtitle=f"Phase: {phase} | Dry-run: {dry_run}"
    ))
    
    email_dir = vault_root() / "Inbox" / "Email"
    if not email_dir.exists():
        console.print("[yellow]No Inbox/Email folder found.[/yellow]")
        return
    
    initial_count = len(list(email_dir.glob("*.md")))
    console.print(f"Starting with [bold]{initial_count}[/bold] emails in Inbox/Email/")
    
    results = {}
    
    # Phase 1: Dedupe
    if phase in ["dedupe", "all"]:
        console.print("\n[bold cyan]Phase 1: Deduplication[/bold cyan]")
        console.print("-" * 40)
        
        from dedupe_emails import (
            find_email_files, group_by_thread, 
            identify_duplicates, archive_duplicates
        )
        
        emails = find_email_files()
        groups = group_by_thread(emails)
        keep, archive = identify_duplicates(groups)
        
        results["dedupe"] = {
            "total": len(emails),
            "unique_threads": len(groups),
            "duplicates": len(archive),
            "kept": len(keep)
        }
        
        console.print(f"  Found {len(emails)} files in {len(groups)} threads")
        console.print(f"  Duplicates to archive: [yellow]{len(archive)}[/yellow]")
        
        if archive and not dry_run:
            archive_duplicates(archive, dry_run=False)
            console.print(f"  [green]Archived {len(archive)} duplicates[/green]")
    
    # Phase 2: Ingest (Extract → Plan → Patch vault)
    if phase in ["ingest", "all"]:
        console.print("\n[bold cyan]Phase 2: Ingest (Extract → Patch Vault)[/bold cyan]")
        console.print("-" * 40)
        
        from ingest_emails import (
            find_pending_emails, extract_from_email, 
            generate_patches, apply_patches, get_openai_client
        )
        
        pending = find_pending_emails()
        if limit:
            pending = pending[:limit]
        
        results["ingest"] = {
            "pending": len(pending),
            "processed": 0,
            "patches_applied": 0,
            "entities_created": 0
        }
        
        if pending:
            console.print(f"  [yellow]{len(pending)} emails pending ingest[/yellow]")
            
            if not dry_run:
                client = get_openai_client()
                extraction_dir = vault_root() / "Inbox" / "_extraction"
                extraction_dir.mkdir(parents=True, exist_ok=True)
                
                for i, email_path in enumerate(pending):
                    content = email_path.read_text()
                    subject = email_path.stem[:40]
                    
                    if verbose:
                        console.print(f"  [{i+1}/{len(pending)}] {subject}")
                    
                    # Extract
                    extraction = extract_from_email(email_path, content, client)
                    extraction_file = extraction_dir / f"{email_path.stem}.email_extraction.json"
                    extraction_file.write_text(extraction.model_dump_json(indent=2))
                    
                    # Plan
                    plan = generate_patches(extraction)
                    plan_file = extraction_dir / f"{email_path.stem}.email_changeplan.json"
                    plan_file.write_text(plan.model_dump_json(indent=2))
                    
                    # Apply
                    apply_results = apply_patches(plan, dry_run=False)
                    
                    results["ingest"]["processed"] += 1
                    results["ingest"]["patches_applied"] += apply_results["applied"]
                    results["ingest"]["entities_created"] += len(plan.entities_to_create)
                
                console.print(f"  [green]Ingested {results['ingest']['processed']} emails[/green]")
                console.print(f"  [green]Applied {results['ingest']['patches_applied']} patches[/green]")
            else:
                console.print("  [dim]Would process these emails[/dim]")
                if verbose:
                    for f in pending[:5]:
                        console.print(f"    • {f.name}")
                    if len(pending) > 5:
                        console.print(f"    ... and {len(pending) - 5} more")
        else:
            console.print("  [green]All emails already ingested[/green]")
    
    # Phase 3: Draft Responses (with vault context)
    if phase in ["draft", "all"]:
        console.print("\n[bold cyan]Phase 3: Draft Responses (Context-Aware)[/bold cyan]")
        console.print("-" * 40)
        
        from draft_responses import (
            find_emails_needing_response, parse_email_metadata,
            should_draft_response, get_openai_client,
            extract_email_context, search_vault_context,
            format_vault_context, generate_draft_response, save_draft
        )
        
        emails = find_emails_needing_response()
        needs_response = []
        
        for email_path in emails:
            content = email_path.read_text()
            metadata = parse_email_metadata(content)
            should_draft, reason = should_draft_response(metadata, content)
            if should_draft:
                needs_response.append((email_path, metadata, reason))
        
        results["draft"] = {
            "analyzed": len(emails),
            "needs_response": len(needs_response)
        }
        
        console.print(f"  Analyzed {len(emails)} emails")
        console.print(f"  Need responses: [yellow]{len(needs_response)}[/yellow]")
        
        if needs_response and not dry_run:
            client = get_openai_client()
            drafts_created = 0
            
            for email_path, metadata, reason in needs_response:
                content = email_path.read_text()
                subject = metadata.get('subject', 'email')[:40]
                
                console.print(f"  [{drafts_created + 1}/{len(needs_response)}] {subject}...")
                
                # Step 1: Extract email context
                extracted = extract_email_context(content, metadata, client)
                
                # Step 2: Search vault for relevant notes
                vault_context = search_vault_context(extracted)
                vault_context_str = format_vault_context(vault_context)
                
                # Step 3: Generate draft with full context
                draft_body = generate_draft_response(
                    content, metadata, client,
                    extracted_context=extracted,
                    vault_context=vault_context_str if vault_context_str else None
                )
                
                save_draft(
                    email_path, metadata, draft_body, reason,
                    extracted_context=extracted,
                    vault_context_summary=vault_context_str if vault_context_str else None
                )
                drafts_created += 1
            
            console.print(f"  [green]Created {drafts_created} context-aware draft(s) in Outbox/[/green]")
            results["draft"]["created"] = drafts_created
        elif needs_response:
            console.print("  [dim]Would create drafts for these emails[/dim]")
            if verbose:
                for path, meta, reason in needs_response[:5]:
                    console.print(f"    • {meta.get('subject', path.name)[:40]}")
    
    # Summary
    console.print("\n" + "=" * 50)
    console.print("[bold]Pipeline Summary[/bold]")
    
    table = Table(show_header=True, header_style="bold")
    table.add_column("Phase")
    table.add_column("Status")
    table.add_column("Details")
    
    if "dedupe" in results:
        r = results["dedupe"]
        status = "[green]✓[/green]" if r["duplicates"] == 0 else f"[yellow]Archived {r['duplicates']}[/yellow]"
        table.add_row("Dedupe", status, f"{r['kept']} unique emails")
    
    if "ingest" in results:
        r = results["ingest"]
        if r["processed"] > 0:
            status = f"[green]✓ {r['processed']} emails[/green]"
            details = f"{r['patches_applied']} patches, {r['entities_created']} new entities"
        elif r["pending"] > 0:
            status = f"[yellow]{r['pending']} pending[/yellow]"
            details = "Run without --dry-run"
        else:
            status = "[green]Up to date[/green]"
            details = "No pending emails"
        table.add_row("Ingest", status, details)
    
    if "draft" in results:
        r = results["draft"]
        created = r.get("created", 0)
        if created:
            status = f"[green]Created {created}[/green]"
        elif r["needs_response"] > 0:
            status = f"[yellow]{r['needs_response']} to draft[/yellow]"
        else:
            status = "[green]None needed[/green]"
        table.add_row("Draft", status, f"{r['analyzed']} analyzed")
    
    console.print(table)
    
    if dry_run:
        console.print("\n[dim]This was a dry-run. Use without --dry-run to apply changes.[/dim]")


if __name__ == "__main__":
    main()
