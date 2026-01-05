#!/usr/bin/env python3
"""
Dedupe notes generated from the same `source_ref`.

Why:
- Re-imports / retries can create multiple notes from the same source file.
- These duplicates often differ slightly in extracted tasks/facts.
- Keep one canonical note per `source_ref`, merge high-signal sections, delete the rest.

Default scope:
- `VAST/People`
- `VAST/Projects`
- `VAST/Customers and Partners`

Idempotent once duplicates are removed.
"""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional

import yaml


DEFAULT_ROOTS = [
    Path("VAST/People"),
    Path("VAST/Projects"),
    Path("VAST/Customers and Partners"),
]

WIKILINK_RE = re.compile(r"\[\[([^|\]]+)(?:\|[^\]]+)?\]\]")


@dataclass(frozen=True)
class MarkdownDoc:
    frontmatter: dict[str, Any]
    body: str


def _read_markdown(path: Path) -> MarkdownDoc:
    text = path.read_text(errors="ignore")
    if not text.startswith("---"):
        return MarkdownDoc(frontmatter={}, body=text)

    end = text.find("\n---", 3)
    if end == -1:
        return MarkdownDoc(frontmatter={}, body=text)

    fm_text = text[4:end]
    try:
        fm = yaml.safe_load(fm_text) or {}
        if not isinstance(fm, dict):
            fm = {}
    except Exception:
        fm = {}

    body = text[end + 4 :]
    if body.startswith("\n"):
        body = body[1:]

    return MarkdownDoc(frontmatter=fm, body=body)


def _write_markdown(path: Path, doc: MarkdownDoc) -> None:
    fm = doc.frontmatter or {}
    if not fm:
        path.write_text(doc.body)
        return

    fm_text = yaml.safe_dump(fm, sort_keys=False).strip()
    path.write_text(f"---\n{fm_text}\n---\n\n{doc.body.lstrip()}")


def _split_sections(body: str) -> tuple[str, list[tuple[str, str]]]:
    """Return (preamble, [(heading, content)]). Headings are `## X`."""
    matches = list(re.finditer(r"^##\s+(.+?)\s*$\n", body, flags=re.MULTILINE))
    if not matches:
        return body, []

    preamble = body[: matches[0].start()]
    sections: list[tuple[str, str]] = []
    for i, m in enumerate(matches):
        heading = m.group(1).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        sections.append((heading, body[start:end]))
    return preamble, sections


def _rebuild_body(preamble: str, sections: list[tuple[str, str]]) -> str:
    out: list[str] = []
    pre = preamble.rstrip()
    if pre:
        out.append(pre + "\n\n")
    for heading, content in sections:
        out.append(f"## {heading}\n\n{content.strip()}\n\n")
    return "".join(out).rstrip() + "\n"


def _merge_bullets(section_contents: list[str]) -> str:
    seen: set[str] = set()
    merged: list[str] = []
    for content in section_contents:
        for line in content.splitlines():
            if not line.strip().startswith("-"):
                continue
            key = re.sub(r"\s+", " ", line.strip()).lower()
            if key in seen:
                continue
            seen.add(key)
            merged.append(line.rstrip())
    return "\n\n".join(merged)


def _merge_tasks(section_contents: list[str]) -> str:
    seen: set[str] = set()
    merged: list[str] = []
    for content in section_contents:
        for line in content.splitlines():
            if "#task" not in line:
                continue
            if not line.strip().startswith("-"):
                continue
            key = re.sub(r"\s+", " ", line.strip()).lower()
            if key in seen:
                continue
            seen.add(key)
            merged.append(line.rstrip())
    return "\n\n".join(merged)


def _extract_wikilink_targets(text: str) -> list[str]:
    return [m.group(1).strip() for m in WIKILINK_RE.finditer(text)]


def _build_wikilink_counts(roots: list[Path]) -> dict[str, int]:
    counts: dict[str, int] = defaultdict(int)
    for root in roots:
        if not root.exists():
            continue
        for p in root.rglob("*.md"):
            targets = _extract_wikilink_targets(p.read_text(errors="ignore"))
            for t in targets:
                counts[t] = counts.get(t, 0) + 1
    return counts


def _kind_score(path: Path) -> int:
    """Prefer canonical notes in domain folders over People folders."""
    s = str(path)
    if "/Customers and Partners/" in s:
        return 3
    if "/Projects/" in s:
        return 2
    if "/People/" in s:
        return 1
    return 0


def _score_candidate(path: Path, link_counts: dict[str, int]) -> tuple[int, int, int, int]:
    """Higher is better: (kind_score, reference_count, task_count, body_length)."""
    doc = _read_markdown(path)
    full_text = path.read_text(errors="ignore")
    kind = _kind_score(path)
    ref_count = link_counts.get(path.stem, 0)
    task_count = sum(1 for line in full_text.splitlines() if "#task" in line and line.strip().startswith("-"))
    return (kind, ref_count, task_count, len(doc.body))


def _choose_canonical(files: list[Path], link_counts: dict[str, int]) -> Path:
    return max(files, key=lambda p: _score_candidate(p, link_counts))


def _merge_group(files: list[Path], canonical: Path) -> MarkdownDoc:
    docs = {p: _read_markdown(p) for p in files}
    canonical_doc = docs[canonical]

    # Frontmatter
    fm = dict(canonical_doc.frontmatter or {})

    # participants union
    participants: list[str] = []
    for p in files:
        part = (docs[p].frontmatter or {}).get("participants") or []
        if isinstance(part, str):
            part = [part]
        if isinstance(part, list):
            for x in part:
                s = str(x).strip()
                if s and s not in participants:
                    participants.append(s)
    if participants:
        fm["participants"] = participants

    # tags union
    tags: list[str] = []
    for p in files:
        t = (docs[p].frontmatter or {}).get("tags") or []
        if isinstance(t, str):
            t = [t]
        if isinstance(t, list):
            for x in t:
                s = str(x).strip()
                if s and s not in tags:
                    tags.append(s)
    if tags:
        fm["tags"] = tags

    # Sections
    preamble, canonical_sections = _split_sections(canonical_doc.body)
    canonical_order = [h for h, _ in canonical_sections]

    all_sections: dict[str, list[str]] = defaultdict(list)
    for p in files:
        _pre, secs = _split_sections(docs[p].body)
        for h, c in secs:
            all_sections[h].append(c)

    merged_content: dict[str, str] = {}

    if "Summary" in all_sections:
        merged_content["Summary"] = max(all_sections["Summary"], key=lambda s: len(s.strip())).strip()

    # Action Items / Tasks
    for h in ("Action Items", "Tasks"):
        if h in all_sections:
            merged = _merge_tasks(all_sections[h])
            merged_content[h] = merged

    if "Decisions" in all_sections:
        merged_content["Decisions"] = _merge_bullets(all_sections["Decisions"])

    for h in ("Key Information", "Key Facts"):
        if h in all_sections:
            merged_content[h] = _merge_bullets(all_sections[h])

    rebuilt: list[tuple[str, str]] = []
    for h, c in canonical_sections:
        if h in merged_content:
            rebuilt.append((h, merged_content[h]))
        else:
            rebuilt.append((h, c))

    # If canonical is missing tasks but tasks exist elsewhere, insert after Summary
    has_task_section = any(h in canonical_order for h in ("Action Items", "Tasks"))
    merged_tasks = _merge_tasks(all_sections.get("Action Items", []) + all_sections.get("Tasks", []))
    if merged_tasks and not has_task_section:
        inserted: list[tuple[str, str]] = []
        for h, c in rebuilt:
            inserted.append((h, c))
            if h == "Summary":
                inserted.append(("Action Items", merged_tasks))
        rebuilt = inserted

    body = _rebuild_body(preamble, rebuilt)
    return MarkdownDoc(frontmatter=fm, body=body)


def dedupe_by_source_ref(
    vault_root: Path,
    roots: list[Path],
    within_folder_only: bool = True,
    apply: bool = False,
    update_links: bool = True,
    max_groups: Optional[int] = None,
) -> dict[str, Any]:
    """Dedupe markdown notes by matching `frontmatter.source_ref`."""
    roots_abs = [vault_root / r for r in roots]

    groups: dict[str, list[Path]] = defaultdict(list)
    for root in roots_abs:
        if not root.exists():
            continue
        for p in root.rglob("*.md"):
            if p.name in {"README.md", "_MANIFEST.md"}:
                continue
            doc = _read_markdown(p)
            src = doc.frontmatter.get("source_ref")
            if src:
                groups[str(src)].append(p)

    dup_groups = [(src, files) for src, files in groups.items() if len(files) > 1]
    if within_folder_only:
        dup_groups = [(src, files) for src, files in dup_groups if len({f.parent for f in files}) == 1]

    dup_groups.sort(key=lambda x: (-len(x[1]), x[0]))
    if max_groups is not None:
        dup_groups = dup_groups[:max_groups]

    link_counts = _build_wikilink_counts(roots_abs) if update_links else {}

    removed: list[Path] = []
    canonical_written: list[Path] = []
    link_map: dict[str, str] = {}

    for _src, files in dup_groups:
        files = sorted(files)
        canonical = _choose_canonical(files, link_counts)
        merged_doc = _merge_group(files, canonical)

        if apply:
            _write_markdown(canonical, merged_doc)
            canonical_written.append(canonical)

        for p in files:
            if p == canonical:
                continue
            link_map[p.stem] = canonical.stem
            if apply:
                p.unlink()
            removed.append(p)

    if apply and update_links and link_map:
        patterns = [
            (re.compile(rf"\[\[{re.escape(old)}(\|[^\]]+)?\]\]"), new)
            for old, new in link_map.items()
        ]
        for root in roots_abs:
            for p in root.rglob("*.md"):
                text = p.read_text(errors="ignore")
                updated = text
                for rx, new in patterns:
                    updated = rx.sub(lambda m: f"[[{new}{m.group(1) or ''}]]", updated)
                if updated != text:
                    p.write_text(updated)

    return {
        "groups": len(dup_groups),
        "files_removed": len(removed),
        "canonical_files_written": len(canonical_written),
        "link_updates": len(link_map),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Dedupe notes by frontmatter.source_ref")
    parser.add_argument("--vault-root", default=".", help="Vault root (default: current directory)")
    parser.add_argument("--apply", action="store_true", help="Apply changes (default: dry-run)")
    parser.add_argument("--include-cross-folder", action="store_true", help="Also dedupe cross-folder duplicates")
    parser.add_argument("--no-link-updates", action="store_true", help="Do not rewrite wikilinks")
    parser.add_argument("--max-groups", type=int, default=None, help="Limit groups processed")

    args = parser.parse_args()
    vault_root = Path(args.vault_root).expanduser().resolve()

    summary = dedupe_by_source_ref(
        vault_root=vault_root,
        roots=DEFAULT_ROOTS,
        within_folder_only=not args.include_cross_folder,
        apply=args.apply,
        update_links=not args.no_link_updates,
        max_groups=args.max_groups,
    )

    mode = "APPLIED" if args.apply else "DRY RUN"
    print(
        f"[{mode}] groups={summary['groups']} removed={summary['files_removed']} "
        f"link_updates={summary['link_updates']}"
    )


if __name__ == "__main__":
    main()
