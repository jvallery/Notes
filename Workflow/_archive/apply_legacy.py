#!/usr/bin/env python3
"""
Apply Phase: ChangePlan JSON → File Updates

DETERMINISTIC EXECUTION - NO AI CALLS

Executes operations from ChangePlan files:
- create: Create new file from template
- append: Append content to existing file
- patch: Apply regex or section-based patches
- link: Insert wikilinks into file
- archive: Move source file to archive

All writes are atomic (temp file + rename).
"""

import json
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

import click
from jinja2 import Environment
from rich.console import Console

sys.path.insert(0, str(Path(__file__).parent))
from utils import vault_root, workflow_root, commit_batch, get_template_env, load_config


console = Console()


def find_pending_changeplans() -> list[Path]:
    """Find changeplan files that haven't been applied."""

    extraction_dir = vault_root() / "Inbox" / "_extraction"

    if not extraction_dir.exists():
        return []

    pending = []

    for changeplan_file in extraction_dir.glob("*.changeplan.json"):
        # Check if already applied (marker file exists)
        applied_marker = changeplan_file.with_suffix(".applied")

        if not applied_marker.exists():
            pending.append(changeplan_file)

    return sorted(pending, key=lambda p: p.name)


def atomic_write(path: Path, content: str):
    """Write content atomically using temp file + rename."""

    path.parent.mkdir(parents=True, exist_ok=True)

    temp_path = path.with_suffix(path.suffix + ".tmp")
    temp_path.write_text(content, encoding="utf-8")
    temp_path.rename(path)


def apply_create(op: dict, jinja_env: Environment, root: Path) -> Path:
    """Create a new file from template."""

    template_name = op.get("template")
    context = op.get("context", {})
    target_path = root / op["path"]

    if target_path.exists():
        console.print(
            f"[yellow]  Warning: File exists, skipping create: {op['path']}[/yellow]"
        )
        return target_path

    template = jinja_env.get_template(template_name)
    content = template.render(**context)

    atomic_write(target_path, content)

    return target_path


def apply_append(op: dict, root: Path) -> Path:
    """Append content to an existing file."""

    target_path = root / op["path"]
    content_to_append = op.get("content", "")

    if not target_path.exists():
        # Create with just the appended content
        atomic_write(target_path, content_to_append)
    else:
        existing = target_path.read_text()

        # Ensure newline between existing and new content
        if existing and not existing.endswith("\n"):
            existing += "\n"

        atomic_write(target_path, existing + content_to_append)

    return target_path


def apply_patch(op: dict, root: Path) -> Path:
    """Apply patches to an existing file using structured primitives."""
    from utils.patch_primitives import upsert_frontmatter, append_under_heading, ensure_wikilinks

    target_path = root / op["path"]
    patches = op.get("patches", [])

    if not target_path.exists():
        console.print(
            f"[red]  Error: Cannot patch non-existent file: {op['path']}[/red]"
        )
        return target_path

    content = target_path.read_text()

    for patch in patches:
        primitive = patch.get("primitive")
        
        if primitive == "upsert_frontmatter":
            fm_patches = patch.get("frontmatter", [])
            content = upsert_frontmatter(content, fm_patches)
        
        elif primitive == "append_under_heading":
            heading_data = patch.get("heading")
            if isinstance(heading_data, dict):
                heading = heading_data.get("heading", "")
                text = heading_data.get("content", "")
            else:
                heading = heading_data or ""
                text = patch.get("content", "")
            if heading and text:
                content = append_under_heading(content, heading, text)
        
        elif primitive == "ensure_wikilinks":
            wikilinks = patch.get("wikilinks", [])
            content = ensure_wikilinks(content, wikilinks)
        
        else:
            # Fallback to legacy regex-based patching
            find_pattern = patch.get("find")
            replace_text = patch.get("replace", "")
            section = patch.get("section")

            if find_pattern:
                content = re.sub(find_pattern, replace_text, content)
            elif section:
                content = _append_to_section(content, section, replace_text)

    atomic_write(target_path, content)

    return target_path


def _append_to_section(content: str, section: str, text: str) -> str:
    """Append text to a markdown section or YAML key."""

    lines = content.split("\n")
    result = []
    found = False

    for i, line in enumerate(lines):
        result.append(line)

        # Check for section header (## heading)
        if line.strip().startswith(section) and line.strip().startswith("#"):
            # Find next section or end
            for j in range(i + 1, len(lines)):
                if lines[j].strip().startswith("#") and not lines[j].strip().startswith(
                    section
                ):
                    break
                result.append(lines[j])

            # Insert before next section
            result.append(text.rstrip())
            found = True
            continue

        # Check for YAML-style key in frontmatter
        if line.startswith(section + ":"):
            result.append(text.rstrip())
            found = True

    if not found:
        # Section not found, append at end
        result.append(f"\n{section}\n{text.rstrip()}")

    return "\n".join(result)


def apply_link(op: dict, root: Path) -> Path:
    """Insert wikilinks into a file."""

    target_path = root / op["path"]
    links = op.get("links", [])

    if not target_path.exists():
        console.print(
            f"[red]  Error: Cannot add links to non-existent file: {op['path']}[/red]"
        )
        return target_path

    content = target_path.read_text()

    # Find or create Links section
    if "## Related" not in content and "## Links" not in content:
        content += "\n\n## Related\n"

    # Add links
    links_text = "\n".join(f"- {link}" for link in links)
    content = _append_to_section(content, "## Related", links_text)

    atomic_write(target_path, content)

    return target_path


def apply_archive(op: dict, root: Path) -> Path:
    """Move source file to archive."""

    source_path = root / op["path"]
    destination = op.get("destination", "Inbox/_archive/")

    if not source_path.exists():
        console.print(
            f"[yellow]  Warning: Source file not found: {op['path']}[/yellow]"
        )
        return source_path

    # Ensure destination includes date folder
    if not destination.endswith("/"):
        destination += "/"

    archive_dir = root / destination / datetime.now().strftime("%Y-%m-%d")
    archive_dir.mkdir(parents=True, exist_ok=True)

    dest_path = archive_dir / source_path.name
    shutil.move(str(source_path), str(dest_path))

    return dest_path


def apply_changeplan(
    changeplan: dict, root: Path, jinja_env: Environment
) -> list[Path]:
    """Execute all operations in a changeplan."""

    modified_files = []

    operations = changeplan.get("operations", [])

    for op in operations:
        op_type = op.get("op")

        try:
            if op_type == "create":
                path = apply_create(op, jinja_env, root)
            elif op_type == "append":
                path = apply_append(op, root)
            elif op_type == "patch":
                path = apply_patch(op, root)
            elif op_type == "link":
                path = apply_link(op, root)
            elif op_type == "archive":
                path = apply_archive(op, root)
            else:
                console.print(f"[yellow]  Unknown operation type: {op_type}[/yellow]")
                continue

            modified_files.append(path)

        except Exception as e:
            console.print(f"[red]  Error in {op_type} for {op.get('path')}: {e}[/red]")

    return modified_files


def mark_applied(changeplan_path: Path):
    """Mark a changeplan as applied."""
    marker = changeplan_path.with_suffix(".applied")
    marker.write_text(datetime.now().isoformat())


@click.command()
@click.option(
    "--file",
    "-f",
    "single_file",
    type=click.Path(exists=True),
    help="Apply a single changeplan file",
)
@click.option(
    "--dry-run", is_flag=True, help="Show what would be done without doing it"
)
@click.option("--no-commit", is_flag=True, help="Skip git commit after applying")
@click.option("--verbose", "-v", is_flag=True, help="Show detailed output")
def main(single_file: Optional[str], dry_run: bool, no_commit: bool, verbose: bool):
    """Apply ChangePlans to the vault."""

    console.print("[bold blue]Apply Phase[/bold blue]")
    console.print("=" * 40)

    root = vault_root()
    jinja_env = get_template_env()

    # Find files to process
    if single_file:
        files = [Path(single_file)]
    else:
        files = find_pending_changeplans()

    if not files:
        console.print("[yellow]No pending changeplans found.[/yellow]")
        return

    console.print(f"Found [bold]{len(files)}[/bold] changeplans to apply")

    all_modified = []
    results = {"success": [], "failed": []}

    for file in files:
        try:
            if verbose:
                console.print(f"\n[dim]Applying: {file.name}[/dim]")

            # Load changeplan
            with open(file, "r") as f:
                changeplan = json.load(f)

            # Check validation
            validation = changeplan.get("validation", {})
            if not validation.get("schema_valid", True):
                warnings = validation.get("warnings", [])
                console.print(
                    f"[yellow]  Skipping invalid changeplan: {warnings}[/yellow]"
                )
                continue

            if dry_run:
                ops = changeplan.get("operations", [])
                for op in ops:
                    console.print(f"  Would {op.get('op')}: {op.get('path')}")
                continue

            # Apply operations
            modified = apply_changeplan(changeplan, root, jinja_env)
            all_modified.extend(modified)

            if verbose:
                for path in modified:
                    console.print(f"  [green]✓[/green] {path.name}")

            # Mark as applied
            mark_applied(file)
            results["success"].append(str(file))

        except Exception as e:
            results["failed"].append({"file": str(file), "error": str(e)})
            console.print(f"[red]Failed: {file.name} - {e}[/red]")

    # Git commit
    if not dry_run and not no_commit and all_modified:
        commit_hash = commit_batch([str(p) for p in all_modified], prefix="[auto]")
        if commit_hash:
            console.print(f"\n[green]Committed: {commit_hash}[/green]")

    # Summary
    if not dry_run:
        console.print("\n" + "=" * 40)
        console.print(f"[green]Success: {len(results['success'])}[/green]")
        console.print(f"[red]Failed: {len(results['failed'])}[/red]")
        console.print(f"[blue]Files modified: {len(all_modified)}[/blue]")


if __name__ == "__main__":
    main()
