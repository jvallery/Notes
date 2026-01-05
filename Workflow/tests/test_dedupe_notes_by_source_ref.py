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


def test_dedupe_cross_domain_only_prefers_project_over_people(tmp_path):
    vault = tmp_path
    people_root = vault / "VAST" / "People" / "Alice Example"
    project_root = vault / "VAST" / "Projects" / "My Project"
    people_root.mkdir(parents=True)
    project_root.mkdir(parents=True)

    src = "/abs/Sources/Transcripts/2026/2026-01-01_example.md"

    people_note = people_root / "2026-01-01 - People Note.md"
    people_note.write_text(
        f"""---
type: "people"
title: "People Note"
date: "2026-01-01"
source_ref: "{src}"
---

# People Note

## Summary

People copy.
"""
    )

    project_note = project_root / "2026-01-01 - Project Note.md"
    project_note.write_text(
        f"""---
type: "projects"
title: "Project Note"
date: "2026-01-01"
source_ref: "{src}"
---

# Project Note

## Summary

Project copy.
"""
    )

    readme = people_root / "README.md"
    readme.write_text(f"- [[{people_note.stem}]]\n")

    summary = dedupe_by_source_ref(
        vault_root=vault,
        roots=[Path("VAST/People"), Path("VAST/Projects")],
        within_folder_only=False,
        cross_domain_only=True,
        apply=True,
        update_links=True,
    )

    assert summary["groups"] == 1
    assert not people_note.exists()
    assert project_note.exists()
    assert f"[[{project_note.stem}]]" in readme.read_text()
