#!/usr/bin/env python3
"""
Email Processing Pipeline - 6-Step Unified Workflow

Processes emails from Inbox through knowledge extraction to draft responses:

1. DEDUPE   - Remove duplicate email exports (same thread, different exports)
2. EXTRACT  - Pull structured data from emails (contacts, tasks, facts, topics)
3. PATCH    - Update/create vault READMEs with extracted knowledge
4. GATHER   - Collect related READMEs for context (people, projects, customers)
5. DRAFT    - Generate AI response using email + gathered vault context
6. ARCHIVE  - Move source email to Sources/Email/YYYY/ and link context

Usage:
    python scripts/process_emails.py              # Run all phases
    python scripts/process_emails.py --phase 1-3  # Run phases 1-3 only (knowledge capture)
    python scripts/process_emails.py --phase 4-6  # Run phases 4-6 only (response gen)
    python scripts/process_emails.py --phase extract  # Run single phase
    python scripts/process_emails.py --dry-run   # Preview without changes
    python scripts/process_emails.py --limit 5   # Process only 5 emails
"""

import json
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional, List, Dict

import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

sys.path.insert(0, str(Path(__file__).parent))
from utils import vault_root, workflow_root


console = Console()


# =============================================================================
# PHASE 1: DEDUPE
# =============================================================================

def phase_dedupe(dry_run: bool = False, verbose: bool = False) -> dict:
    """Remove duplicate email exports from the same thread."""
    
    from dedupe_emails import (
        find_email_files, group_by_thread, 
        identify_duplicates, archive_duplicates
    )
    
    emails = find_email_files()
    groups = group_by_thread(emails)
    keep, archive = identify_duplicates(groups)
    
    results = {
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
    
    return results


# =============================================================================
# PHASE 2: EXTRACT
# =============================================================================

def phase_extract(emails: List[Path], client, dry_run: bool = False, verbose: bool = False) -> Dict[Path, dict]:
    """Extract structured data from emails using AI."""
    
    from ingest_emails import extract_from_email
    
    extraction_dir = vault_root() / "Inbox" / "_extraction"
    extraction_dir.mkdir(parents=True, exist_ok=True)
    
    extractions = {}
    
    for i, email_path in enumerate(emails):
        try:
            content = email_path.read_text()
            subject = email_path.stem[:40]
            
            if verbose:
                console.print(f"  [{i+1}/{len(emails)}] {subject}")
            
            # Check if already extracted
            extraction_file = extraction_dir / f"{email_path.stem}.email_extraction.json"
            if extraction_file.exists():
                # Load existing extraction
                extraction_data = json.loads(extraction_file.read_text())
                extractions[email_path] = extraction_data
                if verbose:
                    console.print(f"    [dim]Using cached extraction[/dim]")
                continue
            
            if dry_run:
                console.print(f"    [dim]Would extract[/dim]")
                continue
            
            # Extract
            extraction = extract_from_email(email_path, content, client)
            extraction_file.write_text(extraction.model_dump_json(indent=2))
            extractions[email_path] = extraction.model_dump()
            
            if verbose:
                console.print(f"    Sender: {extraction.sender.name} <{extraction.sender.email or 'n/a'}>")
                console.print(f"    Topics: {', '.join(extraction.topics[:3])}")
            
        except Exception as e:
            console.print(f"  [red]✗ {email_path.name}: {e}[/red]")
            continue
    
    return extractions


# =============================================================================
# PHASE 3: PATCH
# =============================================================================

def phase_patch(extractions: Dict[Path, dict], dry_run: bool = False, verbose: bool = False, openai_client = None) -> dict:
    """Update vault READMEs with extracted knowledge (with entity classification)."""
    
    from ingest_emails import generate_patches, apply_patches, get_openai_client
    from models.email_extraction import EmailExtraction
    
    # Get client if not provided
    if openai_client is None:
        try:
            openai_client = get_openai_client()
        except Exception:
            pass  # Will fall back to heuristic classification
    
    results = {
        "patches_applied": 0,
        "entities_created": 0,
        "files_updated": set()
    }
    
    extraction_dir = vault_root() / "Inbox" / "_extraction"
    
    for email_path, extraction_data in extractions.items():
        try:
            # Reconstruct EmailExtraction from dict
            if isinstance(extraction_data, dict):
                extraction = EmailExtraction(**extraction_data)
            else:
                extraction = extraction_data
            
            # Generate patches (with entity discovery/classification)
            plan = generate_patches(extraction, openai_client=openai_client)
            
            # Save plan
            plan_file = extraction_dir / f"{email_path.stem}.email_changeplan.json"
            if not dry_run:
                plan_file.write_text(plan.model_dump_json(indent=2))
            
            if verbose and plan.warnings:
                for warning in plan.warnings[:3]:
                    console.print(f"    [yellow]⚠ {warning}[/yellow]")
            
            # Apply patches
            apply_results = apply_patches(plan, dry_run=dry_run)
            
            results["patches_applied"] += apply_results["applied"]
            results["entities_created"] += len(plan.entities_to_create)
            
            for patch in plan.patches:
                results["files_updated"].add(patch.target_path)
            
        except Exception as e:
            console.print(f"  [red]✗ Patch failed for {email_path.name}: {e}[/red]")
            continue
    
    results["files_updated"] = list(results["files_updated"])
    return results


# =============================================================================
# PHASE 4: GATHER
# =============================================================================

def phase_gather(emails: List[Path], verbose: bool = False) -> Dict[Path, dict]:
    """Gather related READMEs for context before drafting."""
    
    from draft_responses import search_vault_context, format_vault_context
    
    gathered = {}
    vault = vault_root()
    extraction_dir = vault / "Inbox" / "_extraction"
    
    for email_path in emails:
        try:
            # Load extraction if available
            extraction_file = extraction_dir / f"{email_path.stem}.email_extraction.json"
            if extraction_file.exists():
                extraction_data = json.loads(extraction_file.read_text())
            else:
                extraction_data = {}
            
            # Convert extraction to format expected by search_vault_context
            extracted = {
                "people": extraction_data.get("people_mentioned", []),
                "companies": extraction_data.get("companies_mentioned", []),
                "topics": extraction_data.get("topics", []),
                "questions": extraction_data.get("questions", []),
                "action_items": [t.get("text", "") for t in extraction_data.get("tasks", [])]
            }
            
            # Add sender to people
            sender = extraction_data.get("sender", {})
            if sender.get("name"):
                extracted["people"].append(sender["name"])
            
            # Search vault for context
            vault_context = search_vault_context(extracted)
            
            # Format for draft generation
            context_str = format_vault_context(vault_context)
            
            gathered[email_path] = {
                "vault_context": vault_context,
                "context_str": context_str,
                "extraction": extraction_data
            }
            
            if verbose:
                people_count = len(vault_context.get("people", []))
                customer_count = len(vault_context.get("customers", []))
                console.print(f"    {email_path.stem[:30]}: {people_count} people, {customer_count} customers")
            
        except Exception as e:
            console.print(f"  [red]✗ Gather failed for {email_path.name}: {e}[/red]")
            gathered[email_path] = {"vault_context": {}, "context_str": "", "extraction": {}}
    
    return gathered


# =============================================================================
# PHASE 5: DRAFT
# =============================================================================

def phase_draft(gathered: Dict[Path, dict], client, dry_run: bool = False, verbose: bool = False) -> dict:
    """Generate AI response drafts using email + vault context."""
    
    from draft_responses import (
        parse_email_metadata, should_draft_response,
        generate_draft_response, save_draft
    )
    
    results = {
        "analyzed": len(gathered),
        "needs_response": 0,
        "created": 0,
        "skipped": []
    }
    
    for email_path, context_data in gathered.items():
        try:
            content = email_path.read_text()
            metadata = parse_email_metadata(content)
            
            # Check if we should draft a response
            should_draft, reason = should_draft_response(metadata, content)
            
            if not should_draft:
                if verbose:
                    console.print(f"    [dim]{email_path.stem[:30]}: Skip - {reason}[/dim]")
                results["skipped"].append((email_path.name, reason))
                continue
            
            results["needs_response"] += 1
            
            if dry_run:
                console.print(f"    [dim]Would draft: {metadata.get('subject', 'unknown')[:40]}[/dim]")
                continue
            
            # Generate draft with full context
            extraction = context_data.get("extraction", {})
            vault_context_str = context_data.get("context_str", "")
            
            draft_result = generate_draft_response(
                content, metadata, client,
                extracted_context=extraction,
                vault_context=vault_context_str if vault_context_str else None
            )
            
            # Save draft
            save_draft(
                email_path, metadata, draft_result, reason,
                extracted_context=extraction,
                vault_context_summary=vault_context_str if vault_context_str else None
            )
            
            results["created"] += 1
            
            if verbose:
                console.print(f"    [green]✓ Drafted: {metadata.get('subject', 'unknown')[:40]}[/green]")
            
        except Exception as e:
            console.print(f"  [red]✗ Draft failed for {email_path.name}: {e}[/red]")
            continue
    
    return results


# =============================================================================
# PHASE 6: ARCHIVE
# =============================================================================

def phase_archive(emails: List[Path], dry_run: bool = False, verbose: bool = False) -> dict:
    """Move source emails to Sources/Email/YYYY/ and link context."""
    
    vault = vault_root()
    results = {
        "archived": 0,
        "skipped": 0,
        "errors": []
    }
    
    for email_path in emails:
        try:
            # Determine archive destination based on email date
            date_match = re.match(r'^(\d{4})-(\d{2})-(\d{2})', email_path.name)
            if date_match:
                year = date_match.group(1)
            else:
                year = datetime.now().strftime("%Y")
            
            archive_dir = vault / "Sources" / "Email" / year
            archive_dir.mkdir(parents=True, exist_ok=True)
            
            dest_path = archive_dir / email_path.name
            
            # Check for extraction files
            extraction_dir = vault / "Inbox" / "_extraction"
            extraction_file = extraction_dir / f"{email_path.stem}.email_extraction.json"
            
            if dry_run:
                console.print(f"    [dim]Would archive: {email_path.name} → Sources/Email/{year}/[/dim]")
                results["archived"] += 1
                continue
            
            # Check if already processed (has extraction)
            if not extraction_file.exists():
                if verbose:
                    console.print(f"    [yellow]Skipping {email_path.name} - not yet extracted[/yellow]")
                results["skipped"] += 1
                continue
            
            # Move email
            shutil.move(str(email_path), str(dest_path))
            
            # Update extraction file with new source_ref
            if extraction_file.exists():
                extraction_data = json.loads(extraction_file.read_text())
                extraction_data["source_file"] = str(dest_path.relative_to(vault))
                extraction_data["archived_at"] = datetime.now().isoformat()
                extraction_file.write_text(json.dumps(extraction_data, indent=2, default=str))
            
            results["archived"] += 1
            
            if verbose:
                console.print(f"    [green]✓ Archived: {email_path.name}[/green]")
            
        except Exception as e:
            console.print(f"  [red]✗ Archive failed for {email_path.name}: {e}[/red]")
            results["errors"].append((email_path.name, str(e)))
    
    return results


# =============================================================================
# UTILITIES
# =============================================================================

def get_openai_client():
    """Get configured OpenAI client with logging instrumentation."""
    from utils.ai_client import get_openai_client as get_instrumented_client
    return get_instrumented_client("process_emails")


def find_pending_emails() -> List[Path]:
    """Find emails in Inbox/Email that haven't been processed."""
    
    email_dir = vault_root() / "Inbox" / "Email"
    if not email_dir.exists():
        return []
    
    return sorted(email_dir.glob("*.md"), key=lambda p: p.name)


# =============================================================================
# MAIN PIPELINE
# =============================================================================


@click.command()
@click.option(
    "--phase", "-p",
    type=click.Choice(["dedupe", "extract", "patch", "gather", "draft", "archive", "1-3", "4-6", "all"]),
    default="all",
    help="Which phase(s) to run"
)
@click.option("--dry-run", is_flag=True, help="Preview without making changes")
@click.option("--verbose", "-v", is_flag=True, help="Show detailed output")
@click.option("--limit", "-n", type=int, default=None, help="Limit emails to process")
@click.option("--skip-archive", is_flag=True, help="Skip archiving (keep emails in Inbox)")
def main(phase: str, dry_run: bool, verbose: bool, limit: Optional[int], skip_archive: bool):
    """Run the 6-step email processing pipeline."""
    
    console.print(Panel.fit(
        "[bold blue]Email Processing Pipeline[/bold blue]\n"
        "[dim]DEDUPE → EXTRACT → PATCH → GATHER → DRAFT → ARCHIVE[/dim]",
        border_style="blue"
    ))
    
    # Determine which phases to run
    phases_to_run = []
    if phase == "all":
        phases_to_run = ["dedupe", "extract", "patch", "gather", "draft", "archive"]
    elif phase == "1-3":
        phases_to_run = ["dedupe", "extract", "patch"]
    elif phase == "4-6":
        phases_to_run = ["gather", "draft", "archive"]
    else:
        phases_to_run = [phase]
    
    if skip_archive and "archive" in phases_to_run:
        phases_to_run.remove("archive")
    
    if dry_run:
        console.print("[yellow]DRY RUN - no changes will be made[/yellow]")
    
    console.print(f"Running phases: {' → '.join(phases_to_run)}")
    
    # Get emails to process
    emails = find_pending_emails()
    if limit:
        emails = emails[:limit]
    
    console.print(f"Found [bold]{len(emails)}[/bold] emails in Inbox/Email/")
    
    if not emails and "dedupe" not in phases_to_run:
        console.print("[yellow]No emails in Inbox/Email to process.[/yellow]")
        return
    
    results = {}
    extractions = {}
    gathered = {}
    
    # Initialize OpenAI client if needed
    client = None
    if any(p in phases_to_run for p in ["extract", "draft"]):
        client = get_openai_client()
    
    # Phase 1: DEDUPE
    if "dedupe" in phases_to_run:
        console.print("\n[bold cyan]Phase 1: DEDUPE[/bold cyan]")
        console.print("-" * 40)
        results["dedupe"] = phase_dedupe(dry_run, verbose)
        
        # Refresh email list after deduplication
        emails = find_pending_emails()
        if limit:
            emails = emails[:limit]
    
    # Phase 2: EXTRACT
    if "extract" in phases_to_run and emails:
        console.print("\n[bold cyan]Phase 2: EXTRACT[/bold cyan]")
        console.print("-" * 40)
        extractions = phase_extract(emails, client, dry_run, verbose)
        results["extract"] = {"count": len(extractions)}
        console.print(f"  [green]Extracted: {len(extractions)} emails[/green]")
    
    # Phase 3: PATCH
    if "patch" in phases_to_run and extractions:
        console.print("\n[bold cyan]Phase 3: PATCH[/bold cyan]")
        console.print("-" * 40)
        results["patch"] = phase_patch(extractions, dry_run, verbose)
        console.print(f"  [green]Applied {results['patch']['patches_applied']} patches[/green]")
        console.print(f"  [green]Created {results['patch']['entities_created']} new entities[/green]")
    
    # Phase 4: GATHER
    if "gather" in phases_to_run and emails:
        console.print("\n[bold cyan]Phase 4: GATHER[/bold cyan]")
        console.print("-" * 40)
        gathered = phase_gather(emails, verbose)
        results["gather"] = {"count": len(gathered)}
        console.print(f"  [green]Gathered context for {len(gathered)} emails[/green]")
    
    # Phase 5: DRAFT
    if "draft" in phases_to_run:
        console.print("\n[bold cyan]Phase 5: DRAFT[/bold cyan]")
        console.print("-" * 40)
        
        # If we didn't gather, do it now
        if not gathered and emails:
            gathered = phase_gather(emails, verbose=False)
        
        if gathered:
            results["draft"] = phase_draft(gathered, client, dry_run, verbose)
            console.print(f"  [green]Created {results['draft']['created']} drafts[/green]")
            if results["draft"]["skipped"]:
                console.print(f"  [dim]Skipped {len(results['draft']['skipped'])} (no response needed)[/dim]")
    
    # Phase 6: ARCHIVE
    if "archive" in phases_to_run and emails:
        console.print("\n[bold cyan]Phase 6: ARCHIVE[/bold cyan]")
        console.print("-" * 40)
        results["archive"] = phase_archive(emails, dry_run, verbose)
        console.print(f"  [green]Archived {results['archive']['archived']} emails to Sources/Email/[/green]")
        if results["archive"]["skipped"]:
            console.print(f"  [yellow]Skipped {results['archive']['skipped']} (not yet extracted)[/yellow]")
    
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
        table.add_row("1. Dedupe", status, f"{r['kept']} unique emails")
    
    if "extract" in results:
        r = results["extract"]
        table.add_row("2. Extract", f"[green]✓ {r['count']}[/green]", "Structured data extracted")
    
    if "patch" in results:
        r = results["patch"]
        table.add_row("3. Patch", f"[green]✓ {r['patches_applied']}[/green]", 
                     f"{r['entities_created']} new entities, {len(r['files_updated'])} files")
    
    if "gather" in results:
        r = results["gather"]
        table.add_row("4. Gather", f"[green]✓ {r['count']}[/green]", "Related READMEs collected")
    
    if "draft" in results:
        r = results["draft"]
        if r["created"] > 0:
            table.add_row("5. Draft", f"[green]✓ {r['created']}[/green]", f"{r['needs_response']} needed response")
        else:
            table.add_row("5. Draft", "[dim]—[/dim]", f"{len(r['skipped'])} skipped (no response needed)")
    
    if "archive" in results:
        r = results["archive"]
        if r["archived"] > 0:
            table.add_row("6. Archive", f"[green]✓ {r['archived']}[/green]", "Moved to Sources/Email/")
        else:
            table.add_row("6. Archive", "[dim]—[/dim]", f"{r['skipped']} skipped")
    
    console.print(table)
    
    if dry_run:
        console.print("\n[dim]This was a dry-run. Use without --dry-run to apply changes.[/dim]")


if __name__ == "__main__":
    main()
