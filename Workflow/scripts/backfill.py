#!/usr/bin/env python3
"""
Backfill CLI: Process historical content into entity READMEs.

This script orchestrates the backfill pipeline:

1. scan    - Find all notes in entity folders
2. extract - Use AI to extract summaries and mentions
3. aggregate - Build README update plan
4. apply   - Apply updates transactionally
5. run     - Execute all phases

Usage:
    python scripts/backfill.py scan --scope VAST
    python scripts/backfill.py extract --manifest manifest.json
    python scripts/backfill.py aggregate --extractions extractions.json
    python scripts/backfill.py apply --plan plan.json --dry-run
    python scripts/backfill.py run --scope VAST --dry-run
"""

import argparse
import sys
from datetime import datetime
from pathlib import Path

# Add scripts and workflow directories to path for imports
SCRIPTS_DIR = Path(__file__).parent
WORKFLOW_DIR = SCRIPTS_DIR.parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))
if str(WORKFLOW_DIR) not in sys.path:
    sys.path.insert(0, str(WORKFLOW_DIR))

# These imports must come after path manipulation
from backfill.scanner import scan_for_backfill, save_manifest, load_manifest  # noqa: E402
from backfill.extractor import extract_batch, save_extractions  # noqa: E402
from backfill.aggregator import aggregate_extractions, save_plan, load_extractions  # noqa: E402
from backfill.applier import TransactionalBackfillApply, load_plan  # noqa: E402
from utils.config import vault_root  # noqa: E402


# ─────────────────────────────────────────────────────────────────────────────
# CLI Commands
# ─────────────────────────────────────────────────────────────────────────────


def cmd_scan(args: argparse.Namespace) -> int:
    """Scan vault for notes to backfill."""
    vault = vault_root()
    
    print(f"Scanning vault for notes in: {args.scope}")
    manifest = scan_for_backfill(args.scope, vault)
    
    print("\nScan Results:")
    print(f"  Entities found: {manifest.total_entities}")
    print(f"  Total notes: {manifest.total_notes}")
    print(f"  Notes with dates: {manifest.notes_with_dates}")
    print(f"  Notes without dates: {manifest.notes_without_dates}")
    
    # Save manifest
    output = Path(args.output) if args.output else vault / "Inbox" / "_extraction" / "backfill-manifest.json"
    save_manifest(manifest, output)
    
    return 0


def cmd_extract(args: argparse.Namespace) -> int:
    """Extract metadata from notes."""
    vault = vault_root()
    
    # Load manifest
    manifest_path = Path(args.manifest)
    manifest = load_manifest(manifest_path)
    
    print(f"Extracting from {manifest.total_notes} notes...")
    
    batch = extract_batch(
        manifest,
        vault=vault,
        limit=args.limit,
        verbose=args.verbose,
    )
    
    print("\nExtraction Results:")
    print(f"  Successful: {batch.successful}")
    print(f"  Failed: {batch.failed}")
    print(f"  Skipped: {batch.skipped}")
    print(f"  Total tokens: {batch.total_tokens}")
    
    # Save extractions
    output = Path(args.output) if args.output else vault / "Inbox" / "_extraction" / "backfill-extractions.json"
    save_extractions(batch, output)
    
    return 0


def cmd_aggregate(args: argparse.Namespace) -> int:
    """Aggregate extractions into README update plan."""
    vault = vault_root()
    
    # Load extractions
    extractions_path = Path(args.extractions)
    batch = load_extractions(extractions_path)
    
    print(f"Aggregating {len(batch.extractions)} extractions...")
    
    plan = aggregate_extractions(batch.extractions, vault)
    
    print("\nAggregation Results:")
    print(f"  Entities with updates: {plan.entities_with_updates}")
    print(f"  Total context entries: {plan.total_context_entries}")
    
    # Save plan
    output = Path(args.output) if args.output else vault / "Inbox" / "_extraction" / "backfill-plan.json"
    save_plan(plan, output)
    
    return 0


def cmd_apply(args: argparse.Namespace) -> int:
    """Apply backfill plan to READMEs."""
    vault = vault_root()
    
    # Load plan
    plan_path = Path(args.plan)
    plan = load_plan(plan_path)
    
    print(f"Applying {len(plan.updates)} README updates...")
    
    applier = TransactionalBackfillApply(vault)
    result = applier.execute(
        plan,
        dry_run=args.dry_run,
        allow_dirty=args.allow_dirty,
    )
    
    print("\nApply Results:")
    print(f"  Success: {result.success}")
    print(f"  READMEs updated: {result.readmes_updated}")
    print(f"  READMEs skipped: {result.readmes_skipped}")
    if result.git_commit:
        print(f"  Git commit: {result.git_commit}")
    if result.errors:
        print(f"  Errors: {result.errors}")
    
    return 0 if result.success else 1


def cmd_run(args: argparse.Namespace) -> int:
    """Run full backfill pipeline."""
    vault = vault_root()
    extraction_dir = vault / "Inbox" / "_extraction"
    extraction_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Phase 1: Scan
    print("=" * 60)
    print("PHASE 1: SCAN")
    print("=" * 60)
    
    manifest = scan_for_backfill(args.scope, vault)
    manifest_path = extraction_dir / f"backfill-manifest-{timestamp}.json"
    save_manifest(manifest, manifest_path)
    
    print(f"  Entities: {manifest.total_entities}")
    print(f"  Notes: {manifest.total_notes}")
    
    if manifest.total_notes == 0:
        print("\nNo notes found to process.")
        return 0
    
    # Phase 2: Extract
    print("\n" + "=" * 60)
    print("PHASE 2: EXTRACT")
    print("=" * 60)
    
    batch = extract_batch(
        manifest,
        vault=vault,
        limit=args.limit,
        verbose=args.verbose,
    )
    extractions_path = extraction_dir / f"backfill-extractions-{timestamp}.json"
    save_extractions(batch, extractions_path)
    
    print(f"  Successful: {batch.successful}")
    print(f"  Failed: {batch.failed}")
    print(f"  Tokens used: {batch.total_tokens}")
    
    if batch.successful == 0:
        print("\nNo successful extractions.")
        return 1
    
    # Phase 3: Aggregate
    print("\n" + "=" * 60)
    print("PHASE 3: AGGREGATE")
    print("=" * 60)
    
    plan = aggregate_extractions(batch.extractions, vault)
    plan_path = extraction_dir / f"backfill-plan-{timestamp}.json"
    save_plan(plan, plan_path)
    
    print(f"  Entities with updates: {plan.entities_with_updates}")
    print(f"  Context entries: {plan.total_context_entries}")
    
    # Phase 4: Apply
    print("\n" + "=" * 60)
    print("PHASE 4: APPLY")
    print("=" * 60)
    
    applier = TransactionalBackfillApply(vault)
    result = applier.execute(
        plan,
        dry_run=args.dry_run,
        allow_dirty=args.allow_dirty,
    )
    
    print(f"  Success: {result.success}")
    print(f"  READMEs updated: {result.readmes_updated}")
    if result.git_commit:
        print(f"  Commit: {result.git_commit}")
    
    # Summary
    print("\n" + "=" * 60)
    print("BACKFILL COMPLETE")
    print("=" * 60)
    
    if result.dry_run:
        print("\n⚠️  DRY RUN - No changes were made")
        print(f"   Review the plan at: {plan_path}")
        print("   Run without --dry-run to apply changes")
    else:
        print(f"\n✅ Updated {result.readmes_updated} READMEs")
        if result.git_commit:
            print(f"   Committed as: {result.git_commit}")
    
    return 0 if result.success else 1


# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Backfill historical content into entity READMEs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # Scan command
    scan_parser = subparsers.add_parser("scan", help="Scan vault for notes")
    scan_parser.add_argument(
        "--scope",
        default="VAST",
        help="Folder scope to scan (default: VAST)",
    )
    scan_parser.add_argument(
        "--output", "-o",
        help="Output path for manifest JSON",
    )
    scan_parser.set_defaults(func=cmd_scan)
    
    # Extract command
    extract_parser = subparsers.add_parser("extract", help="Extract metadata from notes")
    extract_parser.add_argument(
        "--manifest", "-m",
        required=True,
        help="Path to manifest JSON from scan phase",
    )
    extract_parser.add_argument(
        "--output", "-o",
        help="Output path for extractions JSON",
    )
    extract_parser.add_argument(
        "--limit", "-l",
        type=int,
        help="Limit number of notes to extract",
    )
    extract_parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show extraction progress",
    )
    extract_parser.set_defaults(func=cmd_extract)
    
    # Aggregate command
    agg_parser = subparsers.add_parser("aggregate", help="Aggregate extractions into plan")
    agg_parser.add_argument(
        "--extractions", "-e",
        required=True,
        help="Path to extractions JSON from extract phase",
    )
    agg_parser.add_argument(
        "--output", "-o",
        help="Output path for plan JSON",
    )
    agg_parser.set_defaults(func=cmd_aggregate)
    
    # Apply command
    apply_parser = subparsers.add_parser("apply", help="Apply backfill plan")
    apply_parser.add_argument(
        "--plan", "-p",
        required=True,
        help="Path to plan JSON from aggregate phase",
    )
    apply_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without applying",
    )
    apply_parser.add_argument(
        "--allow-dirty",
        action="store_true",
        help="Allow running with uncommitted git changes",
    )
    apply_parser.set_defaults(func=cmd_apply)
    
    # Run command (full pipeline)
    run_parser = subparsers.add_parser("run", help="Run full backfill pipeline")
    run_parser.add_argument(
        "--scope",
        default="VAST",
        help="Folder scope to scan (default: VAST)",
    )
    run_parser.add_argument(
        "--limit", "-l",
        type=int,
        help="Limit number of notes to extract",
    )
    run_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without applying",
    )
    run_parser.add_argument(
        "--allow-dirty",
        action="store_true",
        help="Allow running with uncommitted git changes",
    )
    run_parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show progress details",
    )
    run_parser.set_defaults(func=cmd_run)
    
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
