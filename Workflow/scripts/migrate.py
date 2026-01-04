#!/usr/bin/env python3
"""
Migrate: CLI wrapper for vault migration pipeline.

Brings existing vault content into compliance with STANDARDS.md.
NO AI CALLS - all operations are deterministic and rule-based.

Usage:
    # Full workflow
    python scripts/migrate.py scan --scope "VAST/People" -o manifest.json
    python scripts/migrate.py analyze -m manifest.json -o plan.json
    python scripts/migrate.py apply -p plan.json --dry-run
    python scripts/migrate.py apply -p plan.json
    python scripts/migrate.py verify --scope "VAST/People"
    
    # Quick commands
    python scripts/migrate.py status                    # Show vault status
    python scripts/migrate.py run --scope "VAST/People" # Full pipeline
"""

import sys
from pathlib import Path

import click

sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.migration.scanner import scan_scope, main as scanner_main
from scripts.migration.analyzer import analyze_manifest, main as analyzer_main
from scripts.migration.executor import MigrationExecutor, main as executor_main
from scripts.migration.verifier import verify_compliance, main as verifier_main
from scripts.utils.config import vault_root as get_vault_root


@click.group()
@click.version_option(version="1.0.0")
def cli():
    """Vault migration tool - bring content into STANDARDS.md compliance."""
    pass


@cli.command()
@click.option("--scope", default="all", help="Scope: all, VAST, Personal, or path like VAST/People")
@click.option("-o", "--output", default="manifest.json", help="Output manifest file")
@click.option("-v", "--verbose", is_flag=True, help="Show detailed output")
@click.pass_context
def scan(ctx, scope: str, output: str, verbose: bool):
    """Phase 1: Scan vault for compliance issues."""
    ctx.invoke(scanner_main, scope=scope, output=output, verbose=verbose)


@cli.command()
@click.option("-m", "--manifest", required=True, help="Manifest JSON from scan phase")
@click.option("-o", "--output", default="migration-plan.json", help="Output plan file")
@click.option("-v", "--verbose", is_flag=True, help="Show detailed output")
@click.pass_context
def analyze(ctx, manifest: str, output: str, verbose: bool):
    """Phase 2: Generate migration plan from manifest."""
    ctx.invoke(analyzer_main, manifest=manifest, output=output, verbose=verbose)


@cli.command()
@click.option("-p", "--plan", "plan_path", required=True, help="Migration plan JSON")
@click.option("--dry-run", is_flag=True, help="Show changes without applying")
@click.option("--allow-dirty", is_flag=True, help="Allow dirty git working tree")
@click.option("-v", "--verbose", is_flag=True, help="Show detailed output")
@click.pass_context
def apply(ctx, plan_path: str, dry_run: bool, allow_dirty: bool, verbose: bool):
    """Phase 3: Apply migration plan (transactional)."""
    ctx.invoke(executor_main, plan_path=plan_path, dry_run=dry_run, allow_dirty=allow_dirty, verbose=verbose)


@cli.command()
@click.option("--scope", default="all", help="Scope: all, VAST, Personal, or path like VAST/People")
@click.option("-o", "--output", help="Output report file")
@click.option("--format", "output_format", default="text", type=click.Choice(["text", "json"]))
@click.option("-v", "--verbose", is_flag=True, help="Show all issues")
@click.pass_context
def verify(ctx, scope: str, output: str | None, output_format: str, verbose: bool):
    """Phase 4: Verify compliance after migration."""
    ctx.invoke(verifier_main, scope=scope, output=output, output_format=output_format, verbose=verbose)


@cli.command()
@click.option("--scope", default="all", help="Scope to check")
def status(scope: str):
    """Quick status check - show vault compliance overview."""
    click.echo(click.style("Vault Status", fg="blue", bold=True))
    click.echo("=" * 40)
    
    vault = get_vault_root()
    manifest = scan_scope(vault, scope)
    stats = manifest.statistics
    
    click.echo(f"\nScope: {click.style(scope, bold=True)}")
    click.echo(f"\nEntities: {stats.total_entities}")
    
    # README status
    if stats.entities_missing_readme == 0:
        click.echo(click.style(f"  ✓ All have README.md", fg="green"))
    else:
        click.echo(click.style(f"  ✗ {stats.entities_missing_readme} missing README.md", fg="red"))
    
    # Notes status
    click.echo(f"\nNotes: {stats.total_notes}")
    if stats.notes_missing_frontmatter == 0:
        click.echo(click.style(f"  ✓ All have frontmatter", fg="green"))
    else:
        click.echo(click.style(f"  ⚠ {stats.notes_missing_frontmatter} missing frontmatter", fg="yellow"))
    
    # Issues
    if stats.total_issues == 0:
        click.echo(click.style(f"\n✓ No issues found!", fg="green", bold=True))
    else:
        click.echo(f"\nIssues: {click.style(str(stats.total_issues), fg='yellow')}")
        for issue_type, count in sorted(stats.issues_by_type.items()):
            click.echo(f"  {issue_type}: {count}")
        
        click.echo(click.style("\nRun 'migrate.py scan' to generate full manifest", fg="cyan"))


@cli.command()
@click.option("--scope", required=True, help="Scope to migrate")
@click.option("--dry-run", is_flag=True, help="Show plan without applying")
@click.option("--allow-dirty", is_flag=True, help="Allow dirty git working tree")
@click.option("-v", "--verbose", is_flag=True, help="Show detailed output")
def run(scope: str, dry_run: bool, allow_dirty: bool, verbose: bool):
    """Run full migration pipeline: scan -> analyze -> apply -> verify."""
    from datetime import datetime
    
    click.echo(click.style("Full Migration Pipeline", fg="blue", bold=True))
    click.echo("=" * 50)
    click.echo(f"Scope: {scope}")
    click.echo(f"Mode: {'DRY RUN' if dry_run else 'LIVE'}")
    click.echo("")
    
    vault = get_vault_root()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Phase 1: Scan
    click.echo(click.style("Phase 1: Scanning...", bold=True))
    manifest = scan_scope(vault, scope)
    
    if manifest.statistics.total_issues == 0:
        click.echo(click.style("✓ No issues found - vault is already compliant!", fg="green"))
        return
    
    click.echo(f"  Found {manifest.statistics.total_entities} entities, {manifest.statistics.total_issues} issues")
    
    # Phase 2: Analyze
    click.echo(click.style("\nPhase 2: Analyzing...", bold=True))
    plan = analyze_manifest(manifest)
    click.echo(f"  Generated {len(plan.operations)} operations")
    
    if plan.warnings:
        click.echo(click.style(f"  {len(plan.warnings)} warnings (manual fixes needed)", fg="yellow"))
    
    if len(plan.operations) == 0:
        click.echo(click.style("  No automated fixes possible", fg="yellow"))
        if plan.warnings and verbose:
            for w in plan.warnings:
                click.echo(f"    - {w}")
        return
    
    # Phase 3: Apply
    click.echo(click.style("\nPhase 3: Applying...", bold=True))
    run_id = timestamp
    executor = MigrationExecutor(vault, run_id)
    
    try:
        commit_hash = executor.execute(plan, allow_dirty=allow_dirty, dry_run=dry_run)
        
        if dry_run:
            click.echo("  (Dry run - no changes made)")
        else:
            click.echo(f"  Created: {len(executor.created_files)} files")
            click.echo(f"  Modified: {len(executor.modified_files)} files")
            if commit_hash:
                click.echo(f"  Commit: {commit_hash[:8]}")
    except Exception as e:
        click.echo(click.style(f"  ✗ Failed: {e}", fg="red"))
        raise SystemExit(1)
    
    # Phase 4: Verify (only if not dry-run)
    if not dry_run:
        click.echo(click.style("\nPhase 4: Verifying...", bold=True))
        result = verify_compliance(vault, scope)
        click.echo(f"  Compliance: {result.compliance_percentage}%")
        
        if result.compliance_percentage == 100:
            click.echo(click.style("\n✓ Migration complete - vault is fully compliant!", fg="green", bold=True))
        else:
            click.echo(click.style(f"\n⚠ {len(result.remaining_issues)} issues remain", fg="yellow"))
    else:
        click.echo(click.style("\n✓ Dry run complete - run without --dry-run to apply", fg="cyan"))


if __name__ == "__main__":
    cli()
