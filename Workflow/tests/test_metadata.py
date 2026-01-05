from scripts.utils.cached_prompts import parse_manifest_table
from scripts.utils.frontmatter import parse_frontmatter, render_frontmatter, update_frontmatter
from scripts.utils.patch_primitives import upsert_frontmatter, append_under_heading, ensure_wikilinks


def test_parse_manifest_table_extracts_rows():
    table = """| Name | Role | Company |
| --- | --- | --- |
| [[Alice Example]] | PM | VAST |
| [[Bob Example]] | SE | Partner |
"""
    rows = parse_manifest_table(table)
    # parse_manifest_table preserves raw cell; strip brackets in assertion
    assert "Alice Example" in rows[0]["name"]
    assert rows[0]["role"] == "PM"
    assert rows[1]["company"] == "Partner"


def test_frontmatter_parse_render_roundtrip():
    content = """---
title: Sample
type: people
---

Body
"""
    fm, body = parse_frontmatter(content)
    assert fm["title"] == "Sample"
    assert "Body" in body
    rendered = render_frontmatter(fm)
    assert rendered.startswith("---")
    assert "title: Sample" in rendered


def test_update_frontmatter_creates_when_missing():
    content = "No frontmatter yet\n"
    updated = update_frontmatter(content, {"title": "Test", "type": "people"})
    fm, body = parse_frontmatter(updated)
    assert fm["title"] == "Test"
    assert fm["type"] == "people"
    assert "No frontmatter yet" in body


def test_upsert_frontmatter_adds_and_removes_keys():
    content = """---
title: Old
owner: remove_me
---
Body
"""
    patched = upsert_frontmatter(content, [
        {"key": "title", "value": "New"},
        {"key": "owner", "value": None},
        {"key": "priority", "value": "P1"},
    ])
    fm, _ = parse_frontmatter(patched)
    assert fm["title"] == "New"
    assert "owner" not in fm
    assert fm["priority"] == "P1"


def test_append_under_heading_creates_heading_when_missing():
    content = "# Title\n\nBody"
    updated = append_under_heading(content, "## Key Facts", "- fact one")
    assert "## Key Facts" in updated
    assert "- fact one" in updated


def test_ensure_wikilinks_adds_missing_links():
    content = "# Note\n\nSome text"
    updated = ensure_wikilinks(content, ["Alice Example", "[[Bob Example]]"])
    assert "[[Alice Example]]" in updated
    assert "[[Bob Example]]" in updated
