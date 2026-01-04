#!/usr/bin/env python3
"""
Process Inbox: Full pipeline orchestrator.

Runs: Extract → Plan → Apply in staged batch mode.

Usage:
    # Process everything
    python scripts/process_inbox.py
    
    # Process specific subfolder
    python scripts/process_inbox.py --scope transcripts
    
    # Dry run
    python scripts/process_inbox.py --dry-run
    
    # Skip extraction/planning (apply existing changeplans only)
    python scripts/process_inbox.py --apply-only
    
    # Allow dirty git tree
    python scripts/process_inbox.py --allow-dirty

CRITICAL: The Apply phase is atomic across ALL files.
"""

from __future__ import annotations

import shutil
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

import click

sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.utils import (
    vault_root,
    load_config,
    require_clean,
    get_client,
    check_api_key,
    OpenAIError,
    get_extraction_path,
    setup_logging,
    log_event,
    close_logging,
)
from scripts.extract import find_unprocessed, extract_file, save_extraction
from scripts.plan import generate_plan, save_plan, load_extraction
from scripts.apply import (
    TransactionalApply,
    find_pending_changeplans,
    load_changeplan,
)


@dataclass
class ProcessResult:
    """Results of inbox processing."""

    extracted: int = 0
    planned: int = 0
    applied: int = 0
    failed: int = 0
    errors: list[str] = field(default_factory=list)
    commit_hash: str = ""


def move_to_failed(source: Path, error: str) -> Path:
    """
    Move failed file to _failed/ directory with error log.
    
    Args:
        source: Path to the failed source file
        error: Error message to record
        
    Returns:
        Path to the moved file in _failed/
    """
    vr = vault_root()
    failed_dir = vr / "Inbox" / "_failed" / datetime.now().strftime("%Y-%m-%d")
    failed_dir.mkdir(parents=True, exist_ok=True)

    # Move source file
    dest = failed_dir / source.name
    
    # Handle duplicate names
    counter = 1
    while dest.exists():
        stem = source.stem
        suffix = source.suffix
        dest = failed_dir / f"{stem}_{counter}{suffix}"
        counter += 1
    
    shutil.move(str(source), str(dest))

    # Write error log
    error_path = failed_dir / f"{dest.stem}.error.txt"
    error_path.write_text(
        f"Error: {error}\n\n"
        f"Original file: {source}\n"
        f"Timestamp: {datetime.now().isoformat()}\n"
    )

    return dest


def extract_all(
    files: list[Path],
    client,
    config: dict,
    verbose: bool = False,
) -> tuple[list[Path], list[Path]]:
    """
    Extract all files.
    
    Returns:
        Tuple of (successful extraction paths, failed source paths)
    """
    vr = vault_root()
    successes = []
    failures = []

    for f in files:
        try:
            log_event("extract", "start", {"file": f.name})
            
            if verbose:
                click.echo(f"  Extracting: {f.name}")
            
            extraction, metadata = extract_file(f, client)

            output_path = get_extraction_path(vr, f)
            save_extraction(extraction, output_path)

            log_event("extract", "success", {
                "file": f.name,
                "output": output_path.name,
                "note_type": extraction.note_type,
                "tasks": len(extraction.tasks),
                **{k: v for k, v in metadata.items() if k in ["latency_ms", "total_tokens"]}
            })
            
            successes.append(output_path)
            
            if verbose:
                click.echo(f"    ✓ {extraction.note_type}, {len(extraction.tasks)} tasks")

        except Exception as e:
            log_event("extract", "failed", {"file": f.name, "error": str(e)})
            click.echo(click.style(f"  ✗ {f.name}: {e}", fg="red"))
            
            try:
                move_to_failed(f, str(e))
            except Exception as move_err:
                log_event("extract", "move_failed", {"file": f.name, "error": str(move_err)})
            
            failures.append(f)

    return successes, failures


def plan_all(
    extractions: list[Path],
    client,
    config: dict,
    verbose: bool = False,
) -> tuple[list[Path], list[Path]]:
    """
    Plan all extractions.
    
    Returns:
        Tuple of (successful changeplan paths, failed extraction paths)
    """
    vr = vault_root()
    successes = []
    failures = []

    for f in extractions:
        try:
            log_event("plan", "start", {"file": f.name})
            
            if verbose:
                click.echo(f"  Planning: {f.name}")
            
            plan, metadata = generate_plan(f, client, config)

            output_path = f.parent / f.name.replace(".extraction.json", ".changeplan.json")
            save_plan(plan, output_path)

            log_event("plan", "success", {
                "file": f.name,
                "output": output_path.name,
                "operations": len(plan.operations),
                **{k: v for k, v in metadata.items() if k in ["latency_ms", "total_tokens"]}
            })
            
            successes.append(output_path)
            
            if verbose:
                ops_summary = ", ".join(op.op.value for op in plan.operations)
                click.echo(f"    ✓ {len(plan.operations)} ops: {ops_summary}")

        except Exception as e:
            log_event("plan", "failed", {"file": f.name, "error": str(e)})
            click.echo(click.style(f"  ✗ {f.name}: {e}", fg="red"))
            
            # Try to move the original source to failed
            try:
                extraction = load_extraction(f)
                source_path = vr / extraction.source_file
                if source_path.exists():
                    move_to_failed(source_path, f"Planning failed: {e}")
            except Exception:
                pass
            
            failures.append(f)

    return successes, failures


@click.command()
@click.option(
    "--scope",
    type=click.Choice(["transcripts", "email", "all"]),
    default="all",
    help="Which inbox folders to process",
)
@click.option(
    "--dry-run",
    is_flag=True,
    help="Show what would be processed without doing it",
)
@click.option(
    "--apply-only",
    is_flag=True,
    help="Skip extract/plan, apply existing changeplans only",
)
@click.option(
    "--allow-dirty",
    is_flag=True,
    help="Allow processing with uncommitted git changes",
)
@click.option(
    "--allow-overwrite",
    is_flag=True,
    help="Allow overwriting existing destination files",
)
@click.option(
    "-v", "--verbose",
    is_flag=True,
    help="Show detailed output",
)
def main(
    scope: str,
    dry_run: bool,
    apply_only: bool,
    allow_dirty: bool,
    allow_overwrite: bool,
    verbose: bool,
):
    """Process all pending items in the inbox."""
    
    vr = vault_root()
    config = load_config()
    run_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Setup logging
    log_path = setup_logging(run_id)
    
    click.echo(click.style("Process Inbox", fg="blue", bold=True))
    click.echo("=" * 50)
    log_event("process", "start", {"scope": scope, "run_id": run_id})

    result = ProcessResult()
    changeplans: list[Path] = []

    try:
        # Check git cleanliness early (unless dry run)
        if not dry_run and not apply_only:
            try:
                require_clean(vr, allow_dirty=allow_dirty)
            except RuntimeError as e:
                if not allow_dirty:
                    click.echo(click.style(f"\n✗ {e}", fg="red"))
                    click.echo("  Use --allow-dirty to override")
                    raise SystemExit(1)

        if apply_only:
            # Just apply existing changeplans
            changeplans = find_pending_changeplans()
            click.echo(f"Found {len(changeplans)} existing changeplan(s) to apply")
            
            if not changeplans:
                click.echo(click.style("Nothing to apply.", fg="yellow"))
                return
                
        else:
            # Find unprocessed files
            scopes = ["transcripts", "email"] if scope == "all" else [scope]
            
            all_files: list[Path] = []
            for s in scopes:
                found = find_unprocessed(s)
                all_files.extend(found)
                if verbose:
                    click.echo(f"  {s}: {len(found)} file(s)")

            click.echo(f"Found {len(all_files)} unprocessed file(s)")

            if dry_run:
                click.echo(click.style("\nDry run - would process:", fg="yellow"))
                for f in all_files:
                    click.echo(f"  • {f.name}")
                return

            if not all_files:
                click.echo(click.style("Nothing to process.", fg="yellow"))
                return

            # Check API key
            if not check_api_key():
                click.echo(click.style(
                    "\n✗ OPENAI_API_KEY not set.\n"
                    "  Set it with: export OPENAI_API_KEY=sk-...",
                    fg="red"
                ))
                raise SystemExit(1)

            # Get OpenAI client
            try:
                client = get_client()
            except OpenAIError as e:
                click.echo(click.style(f"\n✗ OpenAI error: {e}", fg="red"))
                raise SystemExit(1)

            # STAGE 1: Extract all
            click.echo(click.style("\n=== EXTRACT ===", fg="cyan", bold=True))
            extractions, extract_failures = extract_all(all_files, client, config, verbose)
            result.extracted = len(extractions)
            result.failed += len(extract_failures)
            click.echo(f"Extracted: {len(extractions)}, Failed: {len(extract_failures)}")

            if not extractions:
                click.echo(click.style("No successful extractions, stopping.", fg="yellow"))
                log_event("process", "early_exit", {"reason": "no_extractions"})
                return

            # STAGE 2: Plan all
            click.echo(click.style("\n=== PLAN ===", fg="cyan", bold=True))
            changeplans, plan_failures = plan_all(extractions, client, config, verbose)
            result.planned = len(changeplans)
            result.failed += len(plan_failures)
            click.echo(f"Planned: {len(changeplans)}, Failed: {len(plan_failures)}")

            if not changeplans:
                click.echo(click.style("No successful plans, stopping.", fg="yellow"))
                log_event("process", "early_exit", {"reason": "no_plans"})
                return

        # STAGE 3: Apply batch (atomic)
        click.echo(click.style("\n=== APPLY ===", fg="cyan", bold=True))
        log_event("apply", "start", {"changeplans": len(changeplans)})

        # Load all plans
        plans = [load_changeplan(p) for p in changeplans]
        source_files = [
            vr / p.source_file
            for p in plans
            if (vr / p.source_file).exists()
        ]

        if verbose:
            for plan in plans:
                click.echo(f"\n  {plan.source_file}:")
                for op in plan.operations:
                    click.echo(f"    {op.op.value}: {op.path}")

        executor = TransactionalApply(vr, run_id)
        commit_hash = executor.execute_batch(
            plans,
            source_files,
            allow_dirty=allow_dirty,
            allow_overwrite=allow_overwrite,
        )

        result.applied = len(plans)
        result.commit_hash = commit_hash

        log_event("apply", "success", {
            "changeplans": len(plans),
            "created": len(executor.created_files),
            "modified": len(executor.modified_files),
            "archived": len(executor.moved_sources),
            "commit": commit_hash[:8] if commit_hash else "",
        })

        click.echo(f"Applied: {len(plans)} changeplan(s)")
        click.echo(f"  Created: {len(executor.created_files)} files")
        click.echo(f"  Modified: {len(executor.modified_files)} files")
        click.echo(f"  Archived: {len(executor.moved_sources)} sources")
        if commit_hash:
            click.echo(f"  Commit: {commit_hash[:8]}")

        # Cleanup changeplan and extraction files
        for p in changeplans:
            try:
                p.unlink()
                # Also remove corresponding extraction file
                extraction_file = p.with_name(
                    p.name.replace(".changeplan.json", ".extraction.json")
                )
                if extraction_file.exists():
                    extraction_file.unlink()
            except Exception:
                pass

        log_event("process", "complete", {
            "extracted": result.extracted,
            "planned": result.planned,
            "applied": result.applied,
            "failed": result.failed,
            "commit": commit_hash[:8] if commit_hash else "",
        })

        # Final summary
        click.echo(click.style("\n" + "=" * 50, fg="green"))
        click.echo(click.style("✓ Processing complete", fg="green", bold=True))
        
        if result.failed > 0:
            click.echo(click.style(
                f"  ⚠ {result.failed} file(s) failed → Inbox/_failed/",
                fg="yellow"
            ))
        
        click.echo(f"  Log: {log_path}")

    except Exception as e:
        log_event("process", "error", {"error": str(e)})
        click.echo(click.style(f"\n✗ Error: {e}", fg="red"))
        
        if verbose:
            import traceback
            traceback.print_exc()
        
        raise SystemExit(1)
    
    finally:
        close_logging()


if __name__ == "__main__":
    main()
