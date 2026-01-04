#!/usr/bin/env python3
"""
Migration Verifier: Phase 4 of migrate.py

Re-scans vault after migration to verify compliance with STANDARDS.md.
Produces a compliance report.

Usage:
    python scripts/migration/verifier.py --scope "VAST/People"
    python scripts/migration/verifier.py --scope "all" -o report.json
"""

import sys
from datetime import datetime
from pathlib import Path

import click

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from scripts.migration.scanner import scan_scope
from scripts.migration.models import VerificationResult, IssueType
from scripts.utils.config import vault_root as get_vault_root


def verify_compliance(vault_root: Path, scope: str) -> VerificationResult:
    """
    Verify vault compliance after migration.
    
    Returns verification result with compliance statistics.
    """
    # Re-scan the vault
    manifest = scan_scope(vault_root, scope)
    
    result = VerificationResult(
        scope=scope,
        verified_at=datetime.now(),
        total_entities=manifest.statistics.total_entities,
    )
    
    remaining_issues = []
    
    for entity in manifest.entities:
        has_issues = False
        
        # Check README issues
        for issue in entity.readme_issues:
            if issue.type in (IssueType.MISSING_README, IssueType.BAD_FRONTMATTER):
                # Critical issues
                remaining_issues.append(f"[{entity.path}] {issue.type.value}: {issue.details or ''}")
                has_issues = True
            elif issue.type in (IssueType.MISSING_KEY, IssueType.WRONG_TYPE):
                # Fixable issues that should have been fixed
                remaining_issues.append(f"[{entity.path}/README.md] {issue.type.value}: {issue.details or ''}")
                has_issues = True
        
        # Check note issues (less critical for compliance)
        for note in entity.notes:
            for issue in note.issues:
                if issue.type == IssueType.NO_FRONTMATTER:
                    # Notes without frontmatter are a concern
                    remaining_issues.append(f"[{note.path}] Missing frontmatter")
                    has_issues = True
        
        if has_issues:
            result.non_compliant_entities += 1
        else:
            result.compliant_entities += 1
    
    result.remaining_issues = remaining_issues
    
    # Calculate compliance percentage
    if result.total_entities > 0:
        result.compliance_percentage = round(
            (result.compliant_entities / result.total_entities) * 100, 1
        )
    
    return result


def generate_report(result: VerificationResult, output_format: str = "text") -> str:
    """Generate human-readable report from verification result."""
    if output_format == "json":
        return result.model_dump_json(indent=2)
    
    lines = [
        "=" * 50,
        "MIGRATION VERIFICATION REPORT",
        "=" * 50,
        "",
        f"Scope: {result.scope}",
        f"Verified at: {result.verified_at.strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "SUMMARY",
        "-" * 50,
        f"Total entities: {result.total_entities}",
        f"Compliant: {result.compliant_entities}",
        f"Non-compliant: {result.non_compliant_entities}",
        f"Compliance: {result.compliance_percentage}%",
        "",
    ]
    
    if result.remaining_issues:
        lines.extend([
            "REMAINING ISSUES",
            "-" * 50,
        ])
        for issue in result.remaining_issues[:50]:  # Limit output
            lines.append(f"  • {issue}")
        
        if len(result.remaining_issues) > 50:
            lines.append(f"  ... and {len(result.remaining_issues) - 50} more")
    else:
        lines.append("✓ No issues found - vault is fully compliant!")
    
    lines.append("")
    lines.append("=" * 50)
    
    return "\n".join(lines)


@click.command()
@click.option("--scope", default="all", help="Scope: all, VAST, Personal, or VAST/People")
@click.option("-o", "--output", help="Output file (optional)")
@click.option("--format", "output_format", default="text", type=click.Choice(["text", "json"]))
@click.option("-v", "--verbose", is_flag=True, help="Show all issues")
def main(scope: str, output: str | None, output_format: str, verbose: bool):
    """Verify vault compliance after migration."""
    
    click.echo(click.style("Migration Verifier", fg="blue", bold=True))
    click.echo("=" * 40)
    
    vault = get_vault_root()
    result = verify_compliance(vault, scope)
    
    # Generate report
    report = generate_report(result, output_format)
    
    if output:
        Path(output).write_text(report)
        click.echo(f"\nReport written to: {click.style(output, fg='cyan')}")
    else:
        click.echo("\n" + report)
    
    # Summary with color coding
    if result.compliance_percentage == 100:
        click.echo(click.style("\n✓ Vault is fully compliant!", fg="green", bold=True))
    elif result.compliance_percentage >= 80:
        click.echo(click.style(f"\n⚠ {result.compliance_percentage}% compliant - some issues remain", fg="yellow"))
    else:
        click.echo(click.style(f"\n✗ {result.compliance_percentage}% compliant - significant issues remain", fg="red"))
    
    # Exit with appropriate code
    if result.non_compliant_entities > 0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
