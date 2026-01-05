from pathlib import Path

from scripts.dedupe_notes_by_source_ref import dedupe_by_source_ref


def test_dedupe_by_source_ref_merges_tasks_and_updates_links(tmp_path):
    vault = tmp_path
    people_root = vault / "VAST" / "People" / "Alice Example"
    people_root.mkdir(parents=True)

    src = "/abs/Sources/Email/2026/2026-01-01_example.md"

    note_a = people_root / "2026-01-01 - Note A.md"
    note_a.write_text(
        f"""---
type: "people"
title: "Note A"
date: "2026-01-01"
participants: ["Alice Example", "Myself"]
source_ref: "{src}"
tags:
  - "type/people"
---

# Note A

## Summary

One summary.

## Action Items

- [?] Task one. @Myself #task #proposed #auto

## Decisions

- Decision A
"""
    )

    note_b = people_root / "2026-01-01 - Note B.md"
    note_b.write_text(
        f"""---
type: "people"
title: "Note B"
date: "2026-01-01"
participants: ["Alice Example", "Myself"]
source_ref: "{src}"
tags:
  - "type/people"
---

# Note B

## Summary

Another (longer) summary that should win.

## Action Items

- [?] Task two. @Myself #task #proposed #auto
"""
    )

    readme = people_root / "README.md"
    # Make Note A the canonical by giving it more inbound links than Note B.
    readme.write_text(
        f"""# Alice Example

- [[{note_a.stem}]]
- [[{note_a.stem}]]
- [[{note_b.stem}]]
"""
    )

    summary = dedupe_by_source_ref(
        vault_root=vault,
        roots=[Path("VAST/People")],
        within_folder_only=True,
        apply=True,
        update_links=True,
    )

    assert summary["groups"] == 1
    assert summary["files_removed"] == 1
    assert note_a.exists()
    assert not note_b.exists()

    merged = note_a.read_text()
    assert "Task one" in merged
    assert "Task two" in merged
    # Summary should be the longer version
    assert "Another (longer) summary" in merged

    updated_readme = readme.read_text()
    assert f"[[{note_b.stem}]]" not in updated_readme
    assert updated_readme.count(f"[[{note_a.stem}]]") == 3

