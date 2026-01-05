#!/usr/bin/env python3
"""
Normalize the header lines in generated notes.

After imports, some notes can have correct frontmatter but still contain
placeholder header links like:
  **Account**: [[]]
  **Project**: [[]]

This script rewrites those header lines to match the entity folder name.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import click

sys.path.insert(0, str(Path(__file__).parent))
from utils import load_config, vault_root
from utils.frontmatter import parse_frontmatter, render_frontmatter


@dataclass(frozen=True)
class HeaderScope:
    name: str
    base_dir: Path
    entity_key: str
    header_label: str  # "Account" or "Project"


def _iter_notes(scope: HeaderScope) -> Iterable[tuple[str, Path]]:
    if not scope.base_dir.exists():
        return
    for entity_dir in sorted(scope.base_dir.iterdir()):
        if not entity_dir.is_dir() or entity_dir.name.startswith(("_", ".")):
            continue
        for md in sorted(entity_dir.glob("*.md")):
            if md.name == "README.md" or md.name.startswith("_"):
                continue
            yield entity_dir.name, md


def normalize_body_header(body: str, *, header_label: str, entity_name: str) -> str:
    """Replace the first `**{header_label}**:` line with a wikilink to entity_name."""
    pattern = re.compile(rf"^(\*\*{re.escape(header_label)}\*\*:\s*).*$", flags=re.MULTILINE)
    return pattern.sub(rf"\1[[{entity_name}]]", body, count=1)


def normalize_headers(scope: HeaderScope, *, dry_run: bool = False) -> tuple[int, int]:
    changed = 0
    skipped = 0
    for entity_name, note_path in _iter_notes(scope):
        text = note_path.read_text(errors="ignore")
        fm, body = parse_frontmatter(text)
        if fm is None:
            skipped += 1
            continue

        expected_entity = entity_name
        updated_body = normalize_body_header(body, header_label=scope.header_label, entity_name=expected_entity)
        if updated_body == body:
            continue

        changed += 1
        if dry_run:
            continue

        note_path.write_text(render_frontmatter(fm) + updated_body)

    return changed, skipped


def _scopes_from_config(vault: Path) -> dict[str, HeaderScope]:
    cfg = load_config(vault_root_override=vault)
    work_paths = cfg.get("paths", {}).get("work", {})
    return {
        "projects": HeaderScope(
            name="projects",
            base_dir=vault / work_paths.get("projects", "VAST/Projects"),
            entity_key="project",
            header_label="Project",
        ),
        "customers": HeaderScope(
            name="customers",
            base_dir=vault / work_paths.get("accounts", "VAST/Customers and Partners"),
            entity_key="account",
            header_label="Account",
        ),
    }


@click.command()
@click.option(
    "--scope",
    "scopes",
    type=click.Choice(["projects", "customers", "all"]),
    default=["all"],
    multiple=True,
    help="Which areas to normalize (default: all).",
)
@click.option("--dry-run", is_flag=True, help="Report changes without writing files.")
def main(scopes: tuple[str, ...], dry_run: bool) -> None:
    vault = vault_root()
    available = _scopes_from_config(vault)

    selected = set(scopes)
    if "all" in selected:
        selected = {"projects", "customers"}

    total_changed = 0
    total_skipped = 0
    for name in ["projects", "customers"]:
        if name not in selected:
            continue
        changed, skipped = normalize_headers(available[name], dry_run=dry_run)
        total_changed += changed
        total_skipped += skipped
        click.echo(f"{name}: changed={changed} skipped_invalid_frontmatter={skipped}")

    click.echo(f"total: changed={total_changed} skipped_invalid_frontmatter={total_skipped}")


if __name__ == "__main__":
    main()
