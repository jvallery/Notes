#!/usr/bin/env python3
"""
Migration Scanner: Phase 1 of migrate.py

Scans vault for entity folders, detects compliance issues, outputs manifest.json.
Does NOT modify any files - read-only analysis.

Usage:
    python scripts/migration/scanner.py --scope "VAST/People" -o manifest.json
    python scripts/migration/scanner.py --scope "all" -o manifest.json
"""

import re
import sys
from datetime import datetime
from pathlib import Path

import click

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from scripts.migration.models import (
    Manifest,
    EntityFolder,
    NoteInfo,
    Issue,
    IssueType,
    IssueSeverity,
    ScanStatistics,
)
from scripts.utils.frontmatter import parse_frontmatter
from scripts.utils.config import vault_root as get_vault_root


# Entity type detection based on path patterns
ENTITY_PATTERNS = {
    "VAST/People": "people",
    "VAST/Customers and Partners": "customer",
    "VAST/Projects": "projects",
    "VAST/ROB": "rob",
    "Personal/People": "people",
    "Personal/Projects": "projects",
}

# Required frontmatter keys by entity type (for README.md)
README_REQUIRED_KEYS = {
    "people": ["type", "person"],
    "customer": ["type", "account"],
    "projects": ["type", "project"],
    "rob": ["type"],
    "partners": ["type", "partner"],
}

# Expected type values by entity category
EXPECTED_TYPES = {
    "people": ["people", "person", "1-1"],
    "customer": ["customer", "account"],
    "projects": ["projects", "project"],
    "rob": ["rob"],
    "partners": ["partners", "partner"],
}

# Date pattern for inferring dates from filenames
DATE_PATTERN = re.compile(r"^(\d{4}-\d{2}-\d{2})")

# Placeholder pattern (e.g., {{DATE}})
PLACEHOLDER_PATTERN = re.compile(r"\{\{[A-Z_]+\}\}")


def vault_relative(vault_root: Path, path: Path) -> str:
    """Get vault-relative path as string."""
    try:
        return str(path.relative_to(vault_root))
    except ValueError:
        return str(path)


def detect_entity_type(path: Path, vault_root: Path) -> str | None:
    """Detect entity type from path location."""
    rel = vault_relative(vault_root, path)
    for pattern, etype in ENTITY_PATTERNS.items():
        if rel.startswith(pattern):
            return etype
    return None


def infer_date_from_filename(filename: str) -> str | None:
    """Extract date from filename if present."""
    match = DATE_PATTERN.match(filename)
    if match:
        return match.group(1)
    return None


def scan_note(note_path: Path, vault_root: Path, entity_type: str) -> NoteInfo:
    """Scan a single note file for issues."""
    rel_path = vault_relative(vault_root, note_path)
    
    info = NoteInfo(
        path=rel_path,
        filename=note_path.name,
        inferred_date=infer_date_from_filename(note_path.name),
    )
    
    try:
        content = note_path.read_text()
    except Exception as e:
        info.issues.append(Issue(
            type=IssueType.BAD_FRONTMATTER,
            file=note_path.name,
            details=f"Could not read file: {e}",
            severity=IssueSeverity.ERROR,
        ))
        return info
    
    fm, _ = parse_frontmatter(content)
    
    if fm is None:
        info.has_frontmatter = False
        info.issues.append(Issue(
            type=IssueType.NO_FRONTMATTER,
            file=note_path.name,
            details="Note has no valid frontmatter",
            severity=IssueSeverity.WARNING,
        ))
    else:
        info.has_frontmatter = True
        info.frontmatter = fm
        info.current_type = fm.get("type")
        
        # Check for placeholder values
        for key, value in fm.items():
            if isinstance(value, str) and PLACEHOLDER_PATTERN.search(value):
                info.issues.append(Issue(
                    type=IssueType.PLACEHOLDER,
                    file=note_path.name,
                    details=f"{key}: {value}",
                    severity=IssueSeverity.WARNING,
                ))
        
        # Check type matches expected for location
        if info.current_type:
            expected = EXPECTED_TYPES.get(entity_type, [])
            if expected and info.current_type not in expected:
                info.issues.append(Issue(
                    type=IssueType.WRONG_TYPE,
                    file=note_path.name,
                    details=f"Type '{info.current_type}' unexpected for {entity_type} folder",
                    severity=IssueSeverity.INFO,
                ))
    
    return info


def scan_readme(readme_path: Path, entity_type: str, vault_root: Path) -> list[Issue]:
    """Scan README.md for compliance issues."""
    issues = []
    
    try:
        content = readme_path.read_text()
    except Exception as e:
        issues.append(Issue(
            type=IssueType.BAD_FRONTMATTER,
            file="README.md",
            details=f"Could not read file: {e}",
            severity=IssueSeverity.ERROR,
        ))
        return issues
    
    fm, _ = parse_frontmatter(content)
    
    if fm is None:
        issues.append(Issue(
            type=IssueType.BAD_FRONTMATTER,
            file="README.md",
            details="README.md has no valid frontmatter",
            severity=IssueSeverity.ERROR,
        ))
        return issues
    
    # Check required keys
    required = README_REQUIRED_KEYS.get(entity_type, ["type"])
    for key in required:
        if key not in fm:
            issues.append(Issue(
                type=IssueType.MISSING_KEY,
                file="README.md",
                details=f"Missing required key: {key}",
                severity=IssueSeverity.WARNING,
            ))
    
    # Check type value
    current_type = fm.get("type")
    if current_type:
        expected = EXPECTED_TYPES.get(entity_type, [])
        # Also accept "{type}-root" format
        valid = expected + [f"{t}-root" for t in expected]
        if current_type not in valid:
            issues.append(Issue(
                type=IssueType.WRONG_TYPE,
                file="README.md",
                details=f"Type '{current_type}' unexpected for {entity_type}",
                severity=IssueSeverity.WARNING,
            ))
    
    # Check for placeholders
    for key, value in fm.items():
        if isinstance(value, str) and PLACEHOLDER_PATTERN.search(value):
            issues.append(Issue(
                type=IssueType.PLACEHOLDER,
                file="README.md",
                details=f"{key}: {value}",
                severity=IssueSeverity.WARNING,
            ))
    
    return issues


def scan_entity(entity_dir: Path, vault_root: Path) -> EntityFolder:
    """Scan a single entity folder for issues."""
    rel_path = vault_relative(vault_root, entity_dir)
    entity_type = detect_entity_type(entity_dir, vault_root) or "unknown"
    
    entity = EntityFolder(
        path=rel_path,
        entity_type=entity_type,
        entity_name=entity_dir.name,
    )
    
    # Check for README
    readme = entity_dir / "README.md"
    if readme.exists():
        entity.has_readme = True
        entity.readme_issues = scan_readme(readme, entity_type, vault_root)
    else:
        entity.readme_issues.append(Issue(
            type=IssueType.MISSING_README,
            details="Entity folder has no README.md",
            severity=IssueSeverity.ERROR,
        ))
    
    # Scan notes
    notes = []
    latest_date = None
    
    for f in sorted(entity_dir.glob("*.md")):
        if f.name == "README.md":
            continue
        
        note = scan_note(f, vault_root, entity_type)
        notes.append(note)
        
        # Track most recent date
        if note.inferred_date:
            if latest_date is None or note.inferred_date > latest_date:
                latest_date = note.inferred_date
    
    entity.notes = notes
    entity.note_count = len(notes)
    entity.last_contact = latest_date
    
    return entity


def scan_scope(vault_root: Path, scope: str) -> Manifest:
    """
    Scan a scope for entity folders.
    
    Args:
        vault_root: Path to vault root
        scope: "all", "VAST", "Personal", or specific path like "VAST/People"
    
    Returns:
        Manifest with all entities and issues
    """
    manifest = Manifest(
        scope=scope,
        vault_root=str(vault_root),
        scan_date=datetime.now(),
    )
    
    # Determine scan directories
    if scope == "all":
        scan_dirs = [vault_root / "VAST", vault_root / "Personal"]
    elif "/" in scope:
        # Specific type path like "VAST/People"
        scan_dirs = [vault_root / scope]
    else:
        # Top-level like "VAST"
        scan_dirs = [vault_root / scope]
    
    entities = []
    stats = ScanStatistics()
    
    for scan_dir in scan_dirs:
        if not scan_dir.exists():
            continue
        
        # Check if this is already at entity folder depth (e.g., VAST/People)
        # Entity folders are at depth 2 from VAST/Personal
        # e.g., VAST/People/Jeff Denworth is an entity folder
        
        # If scope is like "VAST/People", iterate direct children
        if "/" in scope:
            for entity_dir in scan_dir.iterdir():
                if entity_dir.is_dir() and not entity_dir.name.startswith("_"):
                    entity = scan_entity(entity_dir, vault_root)
                    entities.append(entity)
        else:
            # Scope is "VAST" or "Personal" - go two levels deep
            for type_dir in scan_dir.iterdir():
                if not type_dir.is_dir() or type_dir.name.startswith("_"):
                    continue
                
                for entity_dir in type_dir.iterdir():
                    if entity_dir.is_dir() and not entity_dir.name.startswith("_"):
                        entity = scan_entity(entity_dir, vault_root)
                        entities.append(entity)
    
    # Build statistics
    stats.total_entities = len(entities)
    stats.entities_with_readme = sum(1 for e in entities if e.has_readme)
    stats.entities_missing_readme = stats.total_entities - stats.entities_with_readme
    stats.total_notes = sum(e.note_count for e in entities)
    stats.notes_with_frontmatter = sum(
        sum(1 for n in e.notes if n.has_frontmatter) for e in entities
    )
    stats.notes_missing_frontmatter = stats.total_notes - stats.notes_with_frontmatter
    
    # Count issues by type
    issue_counts: dict[str, int] = {}
    total_issues = 0
    
    for entity in entities:
        for issue in entity.readme_issues:
            issue_counts[issue.type.value] = issue_counts.get(issue.type.value, 0) + 1
            total_issues += 1
        for note in entity.notes:
            for issue in note.issues:
                issue_counts[issue.type.value] = issue_counts.get(issue.type.value, 0) + 1
                total_issues += 1
    
    stats.issues_by_type = issue_counts
    stats.total_issues = total_issues
    
    manifest.entities = entities
    manifest.statistics = stats
    
    return manifest


class ScanManifest:
    """Legacy wrapper for compatibility."""
    pass


class EntityInfo:
    """Legacy wrapper for compatibility."""
    pass


class EntityIssue:
    """Legacy wrapper for compatibility."""
    pass


@click.command()
@click.option("--scope", default="all", help="Scope: all, VAST, Personal, or VAST/People")
@click.option("-o", "--output", default="manifest.json", help="Output file path")
@click.option("-v", "--verbose", is_flag=True, help="Show detailed output")
def main(scope: str, output: str, verbose: bool):
    """Scan vault for migration issues."""
    
    click.echo(click.style("Migration Scanner", fg="blue", bold=True))
    click.echo("=" * 40)
    
    vault = get_vault_root()
    manifest = scan_scope(vault, scope)
    
    # Write manifest
    output_path = Path(output)
    output_path.write_text(manifest.model_dump_json(indent=2))
    
    # Summary
    stats = manifest.statistics
    click.echo(f"\nScope: {click.style(scope, bold=True)}")
    click.echo(f"Entities: {stats.total_entities}")
    click.echo(f"  With README: {stats.entities_with_readme}")
    click.echo(f"  Missing README: {click.style(str(stats.entities_missing_readme), fg='red' if stats.entities_missing_readme else 'green')}")
    click.echo(f"Notes: {stats.total_notes}")
    click.echo(f"  With frontmatter: {stats.notes_with_frontmatter}")
    click.echo(f"  Missing frontmatter: {stats.notes_missing_frontmatter}")
    click.echo(f"\nTotal issues: {click.style(str(stats.total_issues), fg='yellow' if stats.total_issues else 'green')}")
    
    if stats.issues_by_type and verbose:
        click.echo("\nIssues by type:")
        for issue_type, count in sorted(stats.issues_by_type.items()):
            click.echo(f"  {issue_type}: {count}")
    
    click.echo(f"\nManifest written to: {click.style(str(output_path), fg='cyan')}")


if __name__ == "__main__":
    main()
