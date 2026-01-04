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
from backfill.extractor import extract_batch, extract_batch_parallel, save_extractions  # noqa: E402
from backfill.aggregator import aggregate_extractions, save_plan, load_extractions  # noqa: E402
from backfill.applier import TransactionalBackfillApply, load_plan  # noqa: E402
from backfill.entities import (  # noqa: E402
    process_discovered_entities,
    sync_manifests,
    get_known_entities,
    batch_rename_notes,
    enrich_entities_batch,
    apply_enrichment_to_readme,
    propose_merges,
    merge_entities,
)
from utils.config import load_config, vault_root  # noqa: E402


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
    
    # Phase 2: Extract (parallel by default)
    print("\n" + "=" * 60)
    print("PHASE 2: EXTRACT")
    print("=" * 60)
    
    # Use parallel extraction for speed
    workers = getattr(args, 'workers', 5)
    if workers > 1:
        batch = extract_batch_parallel(
            manifest,
            vault=vault,
            limit=args.limit,
            verbose=args.verbose,
            max_workers=workers,
        )
    else:
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
    
    # Phase 2.5: Auto-create discovered entities
    if getattr(args, 'auto_create', True):
        print("\n" + "=" * 60)
        print("PHASE 2.5: AUTO-CREATE ENTITIES")
        print("=" * 60)
        
        created = process_discovered_entities(vault, batch.extractions, auto_create=True)
        total_created = sum(len(v) for v in created.values())
        
        if total_created > 0:
            print(f"  Created {len(created['people'])} people folders")
            print(f"  Created {len(created['customers'])} customer folders")
            print(f"  Created {len(created['projects'])} project folders")
        else:
            print("  No new entities to create")
    
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


def cmd_sync_manifests(args: argparse.Namespace) -> int:
    """Sync manifests with folder structure."""
    vault = vault_root()
    
    print("Syncing manifests with folder structure...")
    
    results = sync_manifests(vault, create_missing_folders=args.create_folders)
    
    print("\nSync Results:")
    
    for entity_type in ["people", "customers", "projects"]:
        added = results["added_to_manifest"][entity_type]
        if added:
            print(f"\n  Added to {entity_type} manifest:")
            for name in added:
                print(f"    + {name}")
        
        if args.create_folders:
            created = results["created_folders"][entity_type]
            if created:
                print(f"\n  Created {entity_type} folders:")
                for name in created:
                    print(f"    + {name}")
        
        orphaned = results["orphaned_manifest_entries"][entity_type]
        if orphaned:
            print(f"\n  ⚠️  Orphaned {entity_type} entries (in manifest, no folder):")
            for name in orphaned:
                print(f"    ? {name}")
    
    total_added = sum(len(v) for v in results["added_to_manifest"].values())
    total_orphaned = sum(len(v) for v in results["orphaned_manifest_entries"].values())
    
    print(f"\nTotal: {total_added} added to manifests, {total_orphaned} orphaned entries")
    
    return 0


def cmd_rename(args: argparse.Namespace) -> int:
    """Rename notes based on extraction data."""
    vault = vault_root()
    
    # Load extractions
    extractions_path = Path(args.extractions)
    batch = load_extractions(extractions_path)
    
    print(f"Renaming notes based on {len(batch.extractions)} extractions...")
    
    results = batch_rename_notes(vault, batch.extractions, dry_run=args.dry_run)
    
    renamed_count = 0
    for old_path, new_path, was_renamed in results:
        if was_renamed:
            renamed_count += 1
            if args.verbose:
                print(f"  {old_path.name}")
                print(f"    → {new_path.name}")
    
    if args.dry_run:
        print(f"\n⚠️  DRY RUN - Would rename {renamed_count} notes")
    else:
        print(f"\n✅ Renamed {renamed_count} notes")
    
    return 0


def cmd_enrich(args: argparse.Namespace) -> int:
    """Enrich entities with web search."""
    vault = vault_root()

    config = load_config()
    if not config.get("features", {}).get("backfill_web_enrichment", False):
        print(
            "Web enrichment is disabled. Set features.backfill_web_enrichment: true "
            "in Workflow/config.yaml to enable."
        )
        return 2
    
    from openai import OpenAI
    client = OpenAI()
    
    known = get_known_entities(vault)
    
    entity_type = args.type
    if entity_type not in known:
        print(f"Unknown entity type: {entity_type}")
        return 1
    
    entities = known[entity_type]
    if args.limit:
        entities = entities[:args.limit]
    
    print(f"Enriching {len(entities)} {entity_type} with web search...")
    
    results = enrich_entities_batch(
        vault,
        entity_type,
        entities,
        client,
        workers=args.workers,
        config=config,
    )
    
    # Apply enrichment to READMEs
    updated_count = 0
    for name, data in results.items():
        if apply_enrichment_to_readme(vault, entity_type, name, data):
            updated_count += 1
    
    print(f"\nEnriched {len(results)} entities, updated {updated_count} READMEs:")
    for name, data in results.items():
        print(f"\n  {name}:")
        for key, value in data.items():
            if key != "confidence" and value:
                print(f"    {key}: {value}")
    
    return 0


def cmd_merge(args: argparse.Namespace) -> int:
    """Propose or execute entity merges for deduplication."""
    vault = vault_root()
    
    if args.propose:
        # Propose merges based on similarity analysis
        print("Analyzing entity names for potential duplicates...\n")
        proposals = propose_merges(vault)
        
        for entity_type, merges in proposals.items():
            if not merges:
                continue
            
            print(f"\n{'='*60}")
            print(f"  {entity_type.upper()}")
            print(f"{'='*60}")
            
            for i, merge in enumerate(merges, 1):
                print(f"\n  {i}. Keep: {merge['canonical']}")
                print(f"     Merge: {', '.join(merge['duplicates'])}")
                print(f"     Confidence: {merge['confidence']:.0%}")
        
        # Print summary
        total = sum(len(m) for m in proposals.values())
        print(f"\n\nFound {total} potential merge groups")
        print("Run with --execute to apply merges")
        return 0
    
    elif args.execute:
        # Execute merges based on proposals
        proposals = propose_merges(vault)
        
        for entity_type, merges in proposals.items():
            for merge in merges:
                print(f"\nMerging {entity_type}: {merge['duplicates']} → {merge['canonical']}")
                result = merge_entities(
                    vault=vault,
                    entity_type=entity_type,
                    canonical=merge["canonical"],
                    duplicates=merge["duplicates"],
                    dry_run=args.dry_run,
                )
                
                if "error" in result:
                    print(f"  ❌ {result['error']}")
                else:
                    print(f"  ✅ Merged {len(result['merged'])} entities")
                    print(f"     Aliases added: {result['aliases_added']}")
                    if not args.dry_run:
                        print(f"     Folders deleted: {len(result['folders_deleted'])}")
        
        if args.dry_run:
            print("\n⚠️  DRY RUN - No changes made. Run without --dry-run to apply.")
        
        return 0
    
    else:
        print("Use --propose to analyze duplicates or --execute to merge")
        return 1


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
        "--workers", "-w",
        type=int,
        default=5,
        help="Number of parallel extraction workers (default: 5)",
    )
    run_parser.add_argument(
        "--no-auto-create",
        action="store_true",
        dest="no_auto_create",
        help="Disable auto-creation of new entity folders",
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
    run_parser.set_defaults(func=cmd_run, auto_create=True)
    
    # Sync manifests command
    sync_parser = subparsers.add_parser("sync-manifests", help="Sync manifests with folder structure")
    sync_parser.add_argument(
        "--create-folders",
        action="store_true",
        help="Create folders for manifest entries without folders",
    )
    sync_parser.set_defaults(func=cmd_sync_manifests)
    
    # Rename command
    rename_parser = subparsers.add_parser("rename", help="Rename notes based on extraction data")
    rename_parser.add_argument(
        "--extractions", "-e",
        required=True,
        help="Path to extractions JSON",
    )
    rename_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview renames without applying",
    )
    rename_parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show rename details",
    )
    rename_parser.set_defaults(func=cmd_rename)
    
    # Enrich command
    enrich_parser = subparsers.add_parser("enrich", help="Enrich entities with web search")
    enrich_parser.add_argument(
        "--type", "-t",
        required=True,
        choices=["people", "customers"],
        help="Entity type to enrich",
    )
    enrich_parser.add_argument(
        "--limit", "-l",
        type=int,
        help="Limit number of entities to enrich",
    )
    enrich_parser.add_argument(
        "--workers", "-w",
        type=int,
        default=3,
        help="Number of parallel workers (default: 3)",
    )
    enrich_parser.set_defaults(func=cmd_enrich)
    
    # Merge command
    merge_parser = subparsers.add_parser("merge", help="Deduplicate entities by merging similar names")
    merge_parser.add_argument(
        "--propose",
        action="store_true",
        help="Propose merges based on name similarity",
    )
    merge_parser.add_argument(
        "--execute",
        action="store_true",
        help="Execute proposed merges",
    )
    merge_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be merged without making changes",
    )
    merge_parser.set_defaults(func=cmd_merge)
    
    args = parser.parse_args()
    
    # Handle no_auto_create flag
    if hasattr(args, 'no_auto_create') and args.no_auto_create:
        args.auto_create = False
    
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
