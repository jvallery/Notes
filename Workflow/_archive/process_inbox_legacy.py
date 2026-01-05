#!/usr/bin/env python3
"""
Process Inbox: Orchestrator for Extract → Plan → Apply pipeline.

Runs all three phases in sequence with proper error handling.
Supports various run modes: full, extract-only, plan-only, apply-only.
"""

import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

import click
from rich.console import Console
from rich.logging import RichHandler

sys.path.insert(0, str(Path(__file__).parent))
from utils import vault_root, workflow_root, is_dirty, stash_changes, pop_stash


console = Console()


def setup_logging(verbose: bool = False) -> logging.Logger:
    """Configure logging with file and console handlers."""

    logs_dir = workflow_root() / "logs"
    logs_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    log_file = logs_dir / f"{timestamp}_run.log"

    # Create logger
    logger = logging.getLogger("process_inbox")
    logger.setLevel(logging.DEBUG if verbose else logging.INFO)

    # File handler (always verbose)
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(
        logging.Formatter(
            "%(asctime)s %(levelname)-5s %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )
    )

    # Console handler
    console_handler = RichHandler(console=console, show_time=False, show_path=False)
    console_handler.setLevel(logging.DEBUG if verbose else logging.INFO)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.info(f"Log file: {log_file}")

    return logger


def run_extract(logger: logging.Logger, dry_run: bool = False) -> bool:
    """Run the extract phase."""

    logger.info("Starting Extract phase")

    try:
        from extract import find_unprocessed_files, classify_content, extract_content
        from extract import save_extraction, get_openai_client, get_jinja_env

        files = find_unprocessed_files()

        if not files:
            logger.info("No files to extract")
            return True

        logger.info(f"Found {len(files)} files to extract")

        if dry_run:
            for f in files:
                logger.info(f"  Would extract: {f.name}")
            return True

        client = get_openai_client()
        jinja_env = get_jinja_env()

        success = 0
        failed = 0

        for file in files:
            try:
                logger.debug(f"Extracting: {file.name}")

                content = file.read_text()
                classification = classify_content(content, file.name, client)
                extraction = extract_content(
                    content, file.name, classification, client, jinja_env
                )
                save_extraction(file, classification, extraction)

                success += 1
                logger.info(f"  ✓ {file.name} → {classification.get('note_type')}")

            except Exception as e:
                failed += 1
                logger.error(f"  ✗ {file.name}: {e}")

        logger.info(f"Extract complete: {success} success, {failed} failed")
        return failed == 0

    except Exception as e:
        logger.exception(f"Extract phase failed: {e}")
        return False


def run_plan(logger: logging.Logger, dry_run: bool = False) -> bool:
    """Run the plan phase."""

    logger.info("Starting Plan phase")

    try:
        from plan import find_pending_extractions, generate_changeplan, save_changeplan
        from plan import get_openai_client, get_jinja_env

        files = find_pending_extractions()

        if not files:
            logger.info("No extractions to plan")
            return True

        logger.info(f"Found {len(files)} extractions to plan")

        if dry_run:
            for f in files:
                logger.info(f"  Would plan: {f.name}")
            return True

        client = get_openai_client()
        jinja_env = get_jinja_env()

        import json

        success = 0
        failed = 0

        for file in files:
            try:
                logger.debug(f"Planning: {file.name}")

                with open(file, "r") as f:
                    extraction = json.load(f)

                changeplan = generate_changeplan(extraction, client, jinja_env)
                save_changeplan(file, changeplan)

                ops = len(changeplan.get("operations", []))
                success += 1
                logger.info(f"  ✓ {file.name} → {ops} operations")

            except Exception as e:
                failed += 1
                logger.error(f"  ✗ {file.name}: {e}")

        logger.info(f"Plan complete: {success} success, {failed} failed")
        return failed == 0

    except Exception as e:
        logger.exception(f"Plan phase failed: {e}")
        return False


def run_apply(
    logger: logging.Logger, dry_run: bool = False, no_commit: bool = False
) -> bool:
    """Run the apply phase."""

    logger.info("Starting Apply phase")

    try:
        from apply import find_pending_changeplans, apply_changeplan, mark_applied
        from apply import get_jinja_env
        from utils import commit_batch

        import json

        root = vault_root()
        jinja_env = get_jinja_env()

        files = find_pending_changeplans()

        if not files:
            logger.info("No changeplans to apply")
            return True

        logger.info(f"Found {len(files)} changeplans to apply")

        if dry_run:
            for f in files:
                logger.info(f"  Would apply: {f.name}")
            return True

        all_modified = []
        success = 0
        failed = 0

        for file in files:
            try:
                logger.debug(f"Applying: {file.name}")

                with open(file, "r") as f:
                    changeplan = json.load(f)

                # Check validation
                if not changeplan.get("validation", {}).get("schema_valid", True):
                    logger.warning(f"  ⚠ Skipping invalid: {file.name}")
                    continue

                modified = apply_changeplan(changeplan, root, jinja_env)
                all_modified.extend(modified)

                mark_applied(file)
                success += 1
                logger.info(f"  ✓ {file.name} → {len(modified)} files")

            except Exception as e:
                failed += 1
                logger.error(f"  ✗ {file.name}: {e}")

        # Git commit
        if not no_commit and all_modified:
            commit_hash = commit_batch([str(p) for p in all_modified], prefix="[auto]")
            if commit_hash:
                logger.info(f"Committed: {commit_hash}")

        logger.info(
            f"Apply complete: {success} success, {failed} failed, {len(all_modified)} files modified"
        )
        return failed == 0

    except Exception as e:
        logger.exception(f"Apply phase failed: {e}")
        return False


@click.command()
@click.option("--extract-only", is_flag=True, help="Run only the extract phase")
@click.option("--plan-only", is_flag=True, help="Run only the plan phase")
@click.option("--apply-only", is_flag=True, help="Run only the apply phase")
@click.option(
    "--dry-run", is_flag=True, help="Show what would be done without doing it"
)
@click.option("--no-commit", is_flag=True, help="Skip git commit after applying")
@click.option(
    "--stash", is_flag=True, help="Stash uncommitted changes before processing"
)
@click.option("--verbose", "-v", is_flag=True, help="Show detailed output")
def main(
    extract_only: bool,
    plan_only: bool,
    apply_only: bool,
    dry_run: bool,
    no_commit: bool,
    stash: bool,
    verbose: bool,
):
    """Process Inbox: Extract → Plan → Apply pipeline."""

    console.print("[bold magenta]Process Inbox Pipeline[/bold magenta]")
    console.print("=" * 50)

    logger = setup_logging(verbose)

    start_time = datetime.now()
    logger.info(f"Starting processing run at {start_time.isoformat()}")

    # Handle stashing
    stashed = False
    if stash and is_dirty():
        logger.info("Stashing uncommitted changes")
        stashed = stash_changes()

    try:
        # Determine which phases to run
        run_all = not (extract_only or plan_only or apply_only)

        results = {"extract": None, "plan": None, "apply": None}

        # Extract phase
        if run_all or extract_only:
            results["extract"] = run_extract(logger, dry_run)

        # Plan phase
        if run_all or plan_only:
            results["plan"] = run_plan(logger, dry_run)

        # Apply phase
        if run_all or apply_only:
            results["apply"] = run_apply(logger, dry_run, no_commit)

        # Summary
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()

        console.print("\n" + "=" * 50)
        console.print(f"[bold]Run complete in {duration:.1f}s[/bold]")

        for phase, success in results.items():
            if success is None:
                continue
            status = "[green]✓[/green]" if success else "[red]✗[/red]"
            console.print(f"  {status} {phase.capitalize()}")

        logger.info(f"Run complete in {duration:.1f}s")

    finally:
        # Restore stashed changes
        if stashed:
            logger.info("Restoring stashed changes")
            pop_stash()


if __name__ == "__main__":
    main()
