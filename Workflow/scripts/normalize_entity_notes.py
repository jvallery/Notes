#!/usr/bin/env python3
"""
Normalize note frontmatter in entity folders.

Fixes common ingest artifacts:
- `type` mismatches with folder location (people/projects/customer/rob)
- blank entity keys (`person`, `project`, `account`, `rob_forum`)
- empty tags like `person/`, `account/`, `project/`
- stale `type/*` tags that don't match the normalized type

This is intended as a safe, idempotent cleanup step after imports.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import click

sys.path.insert(0, str(Path(__file__).parent))
from utils import load_config, vault_root
from utils.frontmatter import parse_frontmatter, render_frontmatter


@dataclass(frozen=True)
class EntityScope:
    name: str
    base_dir: Path
    entity_key: str
    note_type: str


def _ensure_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [str(v) for v in value]
    return []


def normalize_frontmatter_dict(
    fm: dict[str, Any],
    *,
    entity_key: str,
    entity_name: str,
    note_type: str,
) -> dict[str, Any]:
    """Return a normalized copy of a frontmatter dict for an entity note."""
    out = dict(fm or {})

    out["type"] = note_type
    out[entity_key] = entity_name

    # Remove blank strings for common keys (keeps README stubs intact by skipping READMEs).
    for key in ["person", "project", "account", "rob_forum"]:
        if out.get(key) == "":
            out.pop(key, None)

    tags = _ensure_list(out.get("tags"))
    cleaned: list[str] = []
    for tag in tags:
        t = str(tag).strip()
        if not t:
            continue
        if t.endswith("/"):
            continue
        cleaned.append(t)

    # Normalize type tags to exactly one.
    cleaned = [t for t in cleaned if not t.startswith("type/")]
    cleaned.insert(0, f"type/{note_type}")

    # De-dupe, preserving order.
    deduped: list[str] = []
    seen: set[str] = set()
    for t in cleaned:
        if t in seen:
            continue
        seen.add(t)
        deduped.append(t)

    if deduped:
        out["tags"] = deduped
    else:
        out.pop("tags", None)

    return out


def _iter_entity_notes(scope: EntityScope) -> Iterable[tuple[str, Path]]:
    if not scope.base_dir.exists():
        return
    for entity_dir in sorted(scope.base_dir.iterdir()):
        if not entity_dir.is_dir() or entity_dir.name.startswith(("_", ".")):
            continue
        for md in sorted(entity_dir.glob("*.md")):
            if md.name == "README.md" or md.name.startswith("_"):
                continue
            yield entity_dir.name, md


def normalize_entity_notes(scope: EntityScope, *, dry_run: bool = False) -> tuple[int, int]:
    """Normalize notes in a single entity scope. Returns (changed, skipped)."""
    changed = 0
    skipped = 0
    for entity_name, note_path in _iter_entity_notes(scope):
        text = note_path.read_text(errors="ignore")
        fm, body = parse_frontmatter(text)
        if fm is None:
            skipped += 1
            continue

        normalized_fm = normalize_frontmatter_dict(
            fm,
            entity_key=scope.entity_key,
            entity_name=entity_name,
            note_type=scope.note_type,
        )
        updated = render_frontmatter(normalized_fm) + body
        if updated == text:
            continue

        changed += 1
        if not dry_run:
            note_path.write_text(updated)

    return changed, skipped


def _scopes_from_config(vault: Path) -> dict[str, EntityScope]:
    cfg = load_config(vault_root_override=vault)
    work_paths = cfg.get("paths", {}).get("work", {})
    return {
        "people": EntityScope(
            name="people",
            base_dir=vault / work_paths.get("people", "VAST/People"),
            entity_key="person",
            note_type="people",
        ),
        "projects": EntityScope(
            name="projects",
            base_dir=vault / work_paths.get("projects", "VAST/Projects"),
            entity_key="project",
            note_type="projects",
        ),
        "customers": EntityScope(
            name="customers",
            base_dir=vault / work_paths.get("accounts", "VAST/Customers and Partners"),
            entity_key="account",
            note_type="customer",
        ),
        "rob": EntityScope(
            name="rob",
            base_dir=vault / work_paths.get("rob", "VAST/ROB"),
            entity_key="rob_forum",
            note_type="rob",
        ),
    }


@click.command()
@click.option(
    "--scope",
    "scopes",
    type=click.Choice(["people", "projects", "customers", "rob", "all"]),
    default=["all"],
    multiple=True,
    help="Which entity areas to normalize (default: all).",
)
@click.option("--dry-run", is_flag=True, help="Report changes without writing files.")
def main(scopes: tuple[str, ...], dry_run: bool) -> None:
    vault = vault_root()
    available = _scopes_from_config(vault)

    selected = set(scopes)
    if "all" in selected:
        selected = {"people", "projects", "customers", "rob"}

    total_changed = 0
    total_skipped = 0
    for name in ["people", "projects", "customers", "rob"]:
        if name not in selected:
            continue
        changed, skipped = normalize_entity_notes(available[name], dry_run=dry_run)
        total_changed += changed
        total_skipped += skipped
        click.echo(f"{name}: changed={changed} skipped_invalid_frontmatter={skipped}")

    click.echo(f"total: changed={total_changed} skipped_invalid_frontmatter={total_skipped}")


if __name__ == "__main__":
    main()
