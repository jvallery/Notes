#!/usr/bin/env python3
"""
Remove empty header entity links like `**Account**: [[]]` or `**Project**: [[]]`.

These placeholders often appear when an extractor couldn't resolve an entity,
but the markdown template still emitted the header line.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Iterable

import click

sys.path.insert(0, str(Path(__file__).parent))
from utils import load_config, vault_root
from utils.frontmatter import parse_frontmatter, render_frontmatter


EMPTY_ENTITY_LINE_RE = re.compile(
    r"^\*\*(Account|Project)\*\*:\s*\[\[\]\]\s*$\n?",
    flags=re.MULTILINE,
)


def remove_empty_entity_links(body: str) -> str:
    # Remove the placeholder lines, then clean up excessive blank lines.
    updated = EMPTY_ENTITY_LINE_RE.sub("", body)
    updated = re.sub(r"\n{3,}", "\n\n", updated)
    return updated


def _iter_people_notes(people_root: Path) -> Iterable[Path]:
    if not people_root.exists():
        return
    for entity_dir in sorted(people_root.iterdir()):
        if not entity_dir.is_dir() or entity_dir.name.startswith(("_", ".")):
            continue
        for md in sorted(entity_dir.glob("*.md")):
            if md.name == "README.md" or md.name.startswith("_"):
                continue
            yield md


@click.command()
@click.option("--dry-run", is_flag=True, help="Report changes without writing files.")
def main(dry_run: bool) -> None:
    vault = vault_root()
    cfg = load_config(vault_root_override=vault)
    people_root = vault / cfg.get("paths", {}).get("work", {}).get("people", "VAST/People")

    changed = 0
    skipped = 0
    for md in _iter_people_notes(people_root):
        text = md.read_text(errors="ignore")
        fm, body = parse_frontmatter(text)
        if fm is None:
            skipped += 1
            continue

        updated_body = remove_empty_entity_links(body)
        if updated_body == body:
            continue

        changed += 1
        if not dry_run:
            md.write_text(render_frontmatter(fm) + updated_body)

    click.echo(f"changed={changed} skipped_invalid_frontmatter={skipped}")


if __name__ == "__main__":
    main()

