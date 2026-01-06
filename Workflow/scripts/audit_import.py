#!/usr/bin/env python3
"""
Post-Import Audit Script

Validates vault state after processing imports. Reports violations that should
be fixed before considering the import complete.

Usage:
    python scripts/audit_import.py [--fix] [--verbose]

Checks:
    - blank FROM "" in README dataview blocks
    - missing last_updated in READMEs
    - missing README.md in entity folders
    - _NEW_* directories (should use triage instead)
    - Untitled*.md files
    - broken source_ref targets
    - note type ↔ destination mismatches
    - empty participants in transcript notes
    - invalid tag patterns
    - unsafe characters in folder names
"""

import sys
import re
import json
from pathlib import Path
from datetime import datetime
from typing import Optional

import click
import yaml
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

sys.path.insert(0, str(Path(__file__).parent))
from utils import vault_root, workflow_root


console = Console()


class AuditFinding:
    """A single audit finding."""
    
    def __init__(
        self,
        severity: str,  # critical, warning, info
        category: str,
        path: str,
        message: str,
        fix_hint: Optional[str] = None
    ):
        self.severity = severity
        self.category = category
        self.path = path
        self.message = message
        self.fix_hint = fix_hint
    
    def __repr__(self):
        return f"[{self.severity.upper()}] {self.category}: {self.path} - {self.message}"


class VaultAuditor:
    """Audits vault for post-import issues."""
    
    def __init__(self, vault: Path, verbose: bool = False):
        self.vault = vault
        self.verbose = verbose
        self.findings: list[AuditFinding] = []
    
    def add_finding(self, severity: str, category: str, path: str, message: str, fix_hint: Optional[str] = None):
        self.findings.append(AuditFinding(severity, category, path, message, fix_hint))
    
    def run_all_checks(self):
        """Run all audit checks."""
        self._check_readme_frontmatter_integrity()
        self._check_readme_dataview_blocks()
        self._check_missing_last_updated()
        self._check_missing_readmes()
        self._check_new_directories()
        self._check_untitled_files()
        self._check_broken_source_refs()
        self._check_type_destination_mismatch()
        self._check_empty_participants()
        self._check_invalid_tags()
        self._check_unsafe_folder_names()

    def _check_readme_frontmatter_integrity(self):
        """Ensure READMEs start with exactly one valid YAML frontmatter block."""
        for readme in self._all_readmes():
            content = readme.read_text(errors="ignore")
            rel = str(readme.relative_to(self.vault))

            if not content.startswith("---"):
                self.add_finding(
                    "warning",
                    "frontmatter",
                    rel,
                    "README missing YAML frontmatter at start",
                    "Add a YAML frontmatter block at the top of the file",
                )
                continue

            lines = content.split("\n")
            end_index = None
            for i, line in enumerate(lines[1:], start=1):
                if line.strip() == "---":
                    end_index = i
                    break

            if end_index is None:
                self.add_finding(
                    "critical",
                    "frontmatter",
                    rel,
                    "README frontmatter missing closing '---'",
                    "Fix the YAML frontmatter block (add closing delimiter)",
                )
                continue

            fm_text = "\n".join(lines[1:end_index])
            try:
                fm = yaml.safe_load(fm_text) or {}
                if not isinstance(fm, dict):
                    raise yaml.YAMLError("Frontmatter must be a mapping")
            except yaml.YAMLError as e:
                self.add_finding(
                    "critical",
                    "frontmatter",
                    rel,
                    f"Invalid YAML frontmatter: {e}",
                    "Fix YAML quoting/escaping so frontmatter parses cleanly",
                )
                continue

            remainder = "\n".join(lines[end_index + 1 :])
            first_nonempty = None
            for line in remainder.split("\n"):
                if line.strip():
                    first_nonempty = line.strip()
                    break
            if first_nonempty == "---":
                self.add_finding(
                    "warning",
                    "frontmatter",
                    rel,
                    "README contains multiple YAML frontmatter blocks",
                    "Remove the duplicated frontmatter block so only one remains at the top",
                )
    
    def _check_readme_dataview_blocks(self):
        """Check for blank FROM "" in README dataview blocks."""
        for readme in self._all_readmes():
            content = readme.read_text()
            if 'FROM ""' in content:
                self.add_finding(
                    "warning",
                    "dataview",
                    str(readme.relative_to(self.vault)),
                    'Contains blank FROM "" query',
                    "Replace with FROM this.file.folder"
                )
    
    def _check_missing_last_updated(self):
        """Check for missing or blank last_updated in READMEs."""
        for readme in self._all_readmes():
            content = readme.read_text()
            
            # Check frontmatter for last_updated
            fm = self._parse_frontmatter(content)
            if not fm:
                continue
            
            last_updated = fm.get("last_updated") or fm.get("last_contact")
            
            if not last_updated or last_updated in ["", "unknown", "''"]:
                self.add_finding(
                    "info",
                    "frontmatter",
                    str(readme.relative_to(self.vault)),
                    "Missing or blank last_updated",
                    "Set last_updated to most recent interaction date"
                )
    
    def _check_missing_readmes(self):
        """Check for entity folders without README.md."""
        entity_dirs = [
            self.vault / "VAST" / "People",
            self.vault / "VAST" / "Customers and Partners",
            self.vault / "VAST" / "Projects",
            self.vault / "VAST" / "ROB",
            self.vault / "Personal" / "People",
            self.vault / "Personal" / "Projects",
        ]
        
        for base_dir in entity_dirs:
            if not base_dir.exists():
                continue
            
            for entity_folder in base_dir.iterdir():
                if not entity_folder.is_dir():
                    continue
                if entity_folder.name.startswith("."):
                    continue
                if entity_folder.name.startswith("_"):
                    continue
                
                readme = entity_folder / "README.md"
                if not readme.exists():
                    self.add_finding(
                        "warning",
                        "structure",
                        str(entity_folder.relative_to(self.vault)),
                        "Entity folder missing README.md",
                        f"Create README from template"
                    )
    
    def _check_new_directories(self):
        """Check for _NEW_* directories (should use triage)."""
        for path in self.vault.rglob("*"):
            if path.is_dir() and "_NEW_" in path.name:
                self.add_finding(
                    "critical",
                    "structure",
                    str(path.relative_to(self.vault)),
                    "_NEW_* directory exists (should use triage)",
                    "Route unknowns to Inbox/_triage/entities.yaml"
                )
    
    def _check_untitled_files(self):
        """Check for Untitled*.md files."""
        for path in self.vault.rglob("Untitled*.md"):
            self.add_finding(
                "warning",
                "naming",
                str(path.relative_to(self.vault)),
                "Untitled file needs proper name",
                "Rename with descriptive title or delete if empty"
            )
    
    def _check_broken_source_refs(self):
        """Check for broken source_ref targets."""
        for md_file in self._all_notes():
            content = md_file.read_text()
            fm = self._parse_frontmatter(content)
            if not fm:
                continue
            
            source_ref = fm.get("source_ref")
            if not source_ref:
                continue
            
            # Resolve path
            ref_path = self.vault / source_ref
            if not ref_path.exists():
                self.add_finding(
                    "warning",
                    "source_ref",
                    str(md_file.relative_to(self.vault)),
                    f"source_ref target missing: {source_ref}",
                    "Update source_ref or locate archive file"
                )
            elif ref_path.stat().st_size == 0:
                self.add_finding(
                    "warning",
                    "source_ref",
                    str(md_file.relative_to(self.vault)),
                    f"source_ref target is 0 bytes: {source_ref}",
                    "Archive file may be corrupt"
                )
    
    def _check_type_destination_mismatch(self):
        """Check for note type ↔ destination mismatches."""
        type_path_rules = {
            "people": ["VAST/People/", "Personal/People/"],
            "customer": ["VAST/Customers and Partners/"],
            "partners": ["VAST/Customers and Partners/"],
            "projects": ["VAST/Projects/", "Personal/Projects/"],
            "rob": ["VAST/ROB/"],
            "journal": ["VAST/Journal/", "Personal/Journal/"],
        }
        
        for md_file in self._all_notes():
            content = md_file.read_text()
            fm = self._parse_frontmatter(content)
            if not fm:
                continue
            
            note_type = fm.get("type")
            if not note_type:
                continue
            
            # Clean up type (may be quoted)
            note_type = note_type.strip('"').strip("'")
            
            rel_path = str(md_file.relative_to(self.vault))
            
            if note_type in type_path_rules:
                valid_paths = type_path_rules[note_type]
                if not any(rel_path.startswith(p) for p in valid_paths):
                    self.add_finding(
                        "warning",
                        "type_mismatch",
                        rel_path,
                        f"type '{note_type}' but path is {rel_path.split('/')[0]}",
                        "Update type or move file to correct location"
                    )
    
    def _check_empty_participants(self):
        """Check for empty participants in transcript notes."""
        for md_file in self._all_notes():
            content = md_file.read_text()
            fm = self._parse_frontmatter(content)
            if not fm:
                continue
            
            source = fm.get("source")
            participants = fm.get("participants", [])
            
            # Only check transcripts/meetings
            if source not in ["transcript", "meeting"]:
                continue
            
            if not participants or participants == []:
                self.add_finding(
                    "warning",
                    "participants",
                    str(md_file.relative_to(self.vault)),
                    "Transcript/meeting note has empty participants",
                    "Add participant names from content"
                )
    
    def _check_invalid_tags(self):
        """Check for invalid tag patterns."""
        invalid_patterns = [
            re.compile(r"[A-Z]"),  # Uppercase letters
            re.compile(r"[\"'()]"),  # Quotes and parens in tags
            re.compile(r"/[^/]+/[^/]+/[^/]+/"),  # More than 3 levels deep
        ]
        
        for md_file in self._all_notes():
            content = md_file.read_text()
            fm = self._parse_frontmatter(content)
            if not fm:
                continue
            
            tags = fm.get("tags", [])
            if isinstance(tags, str):
                tags = [tags]
            
            for tag in tags:
                if not tag:
                    continue
                
                for pattern in invalid_patterns:
                    if pattern.search(tag):
                        self.add_finding(
                            "info",
                            "tags",
                            str(md_file.relative_to(self.vault)),
                            f"Invalid tag format: {tag}",
                            "Use lowercase, no special chars, max 3 levels"
                        )
                        break
    
    def _check_unsafe_folder_names(self):
        """Check for unsafe characters in folder names."""
        unsafe_chars = ['"', "'", "(", ")", "[", "]", ":", "&", "/"]
        
        for path in self.vault.rglob("*"):
            if not path.is_dir():
                continue
            if ".git" in str(path) or ".obsidian" in str(path):
                continue
            
            folder_name = path.name
            
            for char in unsafe_chars:
                if char in folder_name:
                    self.add_finding(
                        "warning",
                        "naming",
                        str(path.relative_to(self.vault)),
                        f"Folder name contains '{char}'",
                        "Rename to remove unsafe characters"
                    )
                    break
    
    def _all_readmes(self) -> list[Path]:
        """Get all README.md files in entity folders."""
        return list(self.vault.rglob("README.md"))
    
    def _all_notes(self) -> list[Path]:
        """Get all markdown files (excluding READMEs and special files)."""
        notes = []
        for md_file in self.vault.rglob("*.md"):
            if ".git" in str(md_file) or ".obsidian" in str(md_file):
                continue
            if md_file.name == "README.md":
                continue
            if md_file.name.startswith("_"):
                continue
            notes.append(md_file)
        return notes
    
    def _parse_frontmatter(self, content: str) -> Optional[dict]:
        """Parse YAML frontmatter from content."""
        if not content.startswith("---"):
            return None
        
        end = content.find("\n---", 3)
        if end == -1:
            return None
        
        try:
            return yaml.safe_load(content[4:end]) or {}
        except yaml.YAMLError:
            return None
    
    def print_report(self):
        """Print audit report to console."""
        
        # Group by severity
        critical = [f for f in self.findings if f.severity == "critical"]
        warnings = [f for f in self.findings if f.severity == "warning"]
        info = [f for f in self.findings if f.severity == "info"]
        
        # Summary table
        summary = Table(title="Audit Summary", show_header=True)
        summary.add_column("Severity", style="bold")
        summary.add_column("Count", justify="right")
        summary.add_row("[red]Critical[/red]", str(len(critical)))
        summary.add_row("[yellow]Warning[/yellow]", str(len(warnings)))
        summary.add_row("[blue]Info[/blue]", str(len(info)))
        summary.add_row("[bold]Total[/bold]", str(len(self.findings)))
        
        console.print(summary)
        
        # Detailed findings by category
        if self.findings:
            console.print("\n[bold]Findings by Category:[/bold]")
            
            categories = {}
            for f in self.findings:
                if f.category not in categories:
                    categories[f.category] = []
                categories[f.category].append(f)
            
            for cat, findings in sorted(categories.items()):
                console.print(f"\n[cyan]{cat}[/cyan] ({len(findings)} issues)")
                for f in findings[:10]:  # Limit to 10 per category
                    severity_color = {"critical": "red", "warning": "yellow", "info": "blue"}.get(f.severity, "white")
                    console.print(f"  [{severity_color}]●[/{severity_color}] {f.path}")
                    console.print(f"    {f.message}")
                if len(findings) > 10:
                    console.print(f"  [dim]... and {len(findings) - 10} more[/dim]")
        
        # Overall status
        if critical:
            console.print(Panel.fit("[red]❌ AUDIT FAILED[/red] - Critical issues found", border_style="red"))
        elif warnings:
            console.print(Panel.fit("[yellow]⚠ AUDIT PASSED WITH WARNINGS[/yellow]", border_style="yellow"))
        else:
            console.print(Panel.fit("[green]✅ AUDIT PASSED[/green]", border_style="green"))
    
    def exit_code(self) -> int:
        """Return exit code (non-zero if critical issues found)."""
        critical = [f for f in self.findings if f.severity == "critical"]
        return 1 if critical else 0


@click.command()
@click.option("--verbose", "-v", is_flag=True, help="Show detailed output")
@click.option("--json", "output_json", is_flag=True, help="Output JSON instead of human-readable")
def main(verbose: bool, output_json: bool):
    """Run post-import audit checks on the vault."""
    
    vault = vault_root()
    
    if not output_json:
        console.print(Panel.fit(
            "[bold blue]Vault Audit[/bold blue]\n"
            f"[dim]{vault}[/dim]",
            border_style="blue"
        ))
    
    auditor = VaultAuditor(vault, verbose=verbose)
    auditor.run_all_checks()
    
    if output_json:
        findings = [
            {
                "severity": f.severity,
                "category": f.category,
                "path": f.path,
                "message": f.message,
                "fix_hint": f.fix_hint
            }
            for f in auditor.findings
        ]
        print(json.dumps({
            "total": len(findings),
            "critical": len([f for f in findings if f["severity"] == "critical"]),
            "warning": len([f for f in findings if f["severity"] == "warning"]),
            "info": len([f for f in findings if f["severity"] == "info"]),
            "findings": findings
        }, indent=2))
    else:
        auditor.print_report()
    
    sys.exit(auditor.exit_code())


if __name__ == "__main__":
    main()
