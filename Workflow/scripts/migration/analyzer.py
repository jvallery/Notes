#!/usr/bin/env python3
"""
Migration Analyzer: Phase 2 of migrate.py

Loads manifest from scanner, generates deterministic fix operations.
NO AI CALLS - all operations are rule-based.

Usage:
    python scripts/migration/analyzer.py -m manifest.json -o migration-plan.json
"""

import re
import sys
from datetime import datetime
from pathlib import Path

import click

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from scripts.migration.models import (
    Manifest,
    MigrationPlan,
    MigrationOperation,
    MigrationOpType,
    IssueType,
)


# Entity key field by type
ENTITY_KEY_FIELDS = {
    "people": "person",
    "customer": "account",
    "projects": "project",
    "rob": "rob_forum",
    "partners": "partner",
}

# Canonical type values
CANONICAL_TYPES = {
    "people": "people",
    "customer": "customer",
    "projects": "projects",
    "rob": "rob",
    "partners": "partners",
}

# Type normalization map (old -> canonical)
TYPE_NORMALIZATION = {
    "1-1": "people",
    "person": "people",
    "People": "people",
    "group-meeting": None,  # Resolve by location
    "Customer": "customer",
    "account": "customer",
    "Partners": "partners",
    "partner": "partners",
    "project": "projects",
    "Project": "projects",
}


def slugify(name: str) -> str:
    """Convert name to slug format."""
    slug = name.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug)
    return slug.strip("-")


def get_entity_key(entity_type: str) -> str:
    """Get the entity key field name for a type."""
    return ENTITY_KEY_FIELDS.get(entity_type, "entity")


def get_canonical_type(entity_type: str) -> str:
    """Get canonical type value."""
    return CANONICAL_TYPES.get(entity_type, entity_type)


def analyze_manifest(manifest: Manifest) -> MigrationPlan:
    """
    Generate migration plan from scan manifest.
    
    This is a deterministic, rule-based analysis with NO AI calls.
    """
    operations: list[MigrationOperation] = []
    warnings: list[str] = []
    stats = {
        "readme_creates": 0,
        "frontmatter_fixes": 0,
        "type_fixes": 0,
        "skipped": 0,
    }
    
    for entity in manifest.entities:
        entity_path = entity.path
        entity_type = entity.entity_type
        entity_name = entity.entity_name
        
        # Process README issues
        for issue in entity.readme_issues:
            if issue.type == IssueType.MISSING_README:
                # Create README from template
                operations.append(MigrationOperation(
                    op=MigrationOpType.CREATE_README,
                    path=f"{entity_path}/README.md",
                    template="readme-migration.md.j2",
                    context={
                        "entity_type": get_canonical_type(entity_type),
                        "entity_name": entity_name,
                        "entity_slug": slugify(entity_name),
                        "entity_key": get_entity_key(entity_type),
                        "last_contact": entity.last_contact or datetime.now().strftime("%Y-%m-%d"),
                        "note_count": entity.note_count,
                        "folder_path": entity_path,
                    }
                ))
                stats["readme_creates"] += 1
                
            elif issue.type == IssueType.MISSING_KEY:
                # Parse the key from details
                key = _extract_key_from_details(issue.details)
                if key:
                    value = _infer_value(key, entity_type, entity_name)
                    operations.append(MigrationOperation(
                        op=MigrationOpType.ADD_MISSING_KEY,
                        path=f"{entity_path}/README.md",
                        patches=[{"key": key, "value": value}],
                    ))
                    stats["frontmatter_fixes"] += 1
                    
            elif issue.type == IssueType.WRONG_TYPE:
                # Fix type value
                operations.append(MigrationOperation(
                    op=MigrationOpType.FIX_TYPE,
                    path=f"{entity_path}/README.md",
                    patches=[{"key": "type", "value": get_canonical_type(entity_type)}],
                ))
                stats["type_fixes"] += 1
                
            elif issue.type == IssueType.BAD_FRONTMATTER:
                # Can't auto-fix bad frontmatter structure
                warnings.append(f"Manual fix needed: {entity_path}/README.md - {issue.details}")
                stats["skipped"] += 1
                
            elif issue.type == IssueType.PLACEHOLDER:
                # Fix placeholder values
                key, _ = _parse_placeholder_detail(issue.details)
                if key:
                    value = entity.last_contact or datetime.now().strftime("%Y-%m-%d")
                    operations.append(MigrationOperation(
                        op=MigrationOpType.FIX_FRONTMATTER,
                        path=f"{entity_path}/README.md",
                        patches=[{"key": key, "value": value}],
                    ))
                    stats["frontmatter_fixes"] += 1
        
        # Process note issues (optional - we mainly focus on READMEs)
        for note in entity.notes:
            for issue in note.issues:
                if issue.type == IssueType.PLACEHOLDER:
                    key, _ = _parse_placeholder_detail(issue.details)
                    if key:
                        # Use inferred date from filename if available
                        value = note.inferred_date or entity.last_contact or datetime.now().strftime("%Y-%m-%d")
                        operations.append(MigrationOperation(
                            op=MigrationOpType.FIX_FRONTMATTER,
                            path=note.path,
                            patches=[{"key": key, "value": value}],
                        ))
                        stats["frontmatter_fixes"] += 1
                
                # Note: We don't auto-fix wrong types in notes
                # because they might be intentional (e.g., a customer note in a person folder)
    
    return MigrationPlan(
        source_manifest=f"manifest-{manifest.scope}.json",
        scope=manifest.scope,
        operations=operations,
        warnings=warnings,
        statistics=stats,
    )


def _extract_key_from_details(details: str | None) -> str | None:
    """Extract key name from issue details like 'Missing required key: person'."""
    if not details:
        return None
    if "Missing required key:" in details:
        return details.split(":")[-1].strip()
    return None


def _parse_placeholder_detail(details: str | None) -> tuple[str | None, str | None]:
    """Parse placeholder detail like 'date: {{DATE}}' into (key, placeholder)."""
    if not details or ":" not in details:
        return None, None
    parts = details.split(":", 1)
    return parts[0].strip(), parts[1].strip() if len(parts) > 1 else None


def _infer_value(key: str, entity_type: str, entity_name: str) -> str:
    """Infer a value for a missing frontmatter key."""
    if key in ("person", "account", "project", "rob_forum", "partner"):
        return entity_name
    if key == "type":
        return get_canonical_type(entity_type)
    return ""


@click.command()
@click.option("-m", "--manifest", required=True, help="Manifest JSON from scan")
@click.option("-o", "--output", default="migration-plan.json", help="Output plan file")
@click.option("-v", "--verbose", is_flag=True, help="Show detailed output")
def main(manifest: str, output: str, verbose: bool):
    """Generate migration plan from manifest."""
    
    click.echo(click.style("Migration Analyzer", fg="blue", bold=True))
    click.echo("=" * 40)
    
    # Load manifest
    manifest_path = Path(manifest)
    if not manifest_path.exists():
        click.echo(click.style(f"Manifest not found: {manifest}", fg="red"))
        raise SystemExit(1)
    
    manifest_data = Manifest.model_validate_json(manifest_path.read_text())
    
    # Analyze and generate plan
    plan = analyze_manifest(manifest_data)
    
    # Write plan
    output_path = Path(output)
    output_path.write_text(plan.model_dump_json(indent=2))
    
    # Summary
    stats = plan.statistics
    click.echo(f"\nScope: {click.style(plan.scope, bold=True)}")
    click.echo(f"\nOperations generated: {click.style(str(len(plan.operations)), bold=True)}")
    click.echo(f"  README creates: {stats.get('readme_creates', 0)}")
    click.echo(f"  Frontmatter fixes: {stats.get('frontmatter_fixes', 0)}")
    click.echo(f"  Type fixes: {stats.get('type_fixes', 0)}")
    click.echo(f"  Skipped (manual): {stats.get('skipped', 0)}")
    
    if plan.warnings:
        click.echo(f"\n{click.style('Warnings:', fg='yellow')} {len(plan.warnings)}")
        if verbose:
            for w in plan.warnings:
                click.echo(f"  - {w}")
    
    click.echo(f"\nPlan written to: {click.style(str(output_path), fg='cyan')}")


if __name__ == "__main__":
    main()
