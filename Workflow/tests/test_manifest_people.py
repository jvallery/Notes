from scripts import manifest_sync


def test_generate_people_manifest_includes_aliases_column():
    entries = [
        manifest_sync.PersonEntry(
            name="Alice Example",
            role="PM",
            company="Acme",
            email="alice@acme.com",
            my_relationship="peer",
            aliases=["Al", "Alice"],
            context="Example person",
            last_contact="2026-01-01",
        )
    ]
    manifest = manifest_sync.generate_people_manifest(entries)
    assert "| Name | Role | Company | Email | My Relationship | Aliases | Context |" in manifest
    assert "| Alice Example | PM | Acme | alice@acme.com | peer | Al; Alice |" in manifest


def test_scan_people_folder_falls_back_to_frontmatter_and_aliases(tmp_path, monkeypatch):
    people_root = tmp_path / "VAST" / "People"
    person_dir = people_root / "Alice Example"
    person_dir.mkdir(parents=True)
    readme = person_dir / "README.md"
    readme.write_text(
        """---
type: people
title: Alice Example
company: Acme
email: alice@acme.com
aliases:
  - Al
  - Alice
last_contact: 2026-01-01
---
# Alice Example

## Key Facts
- Placeholder
"""
    )

    monkeypatch.setattr(manifest_sync, "VAST_PEOPLE", people_root)
    entries = manifest_sync.scan_people_folder()

    assert len(entries) == 1
    entry = entries[0]
    assert entry.name == "Alice Example"
    # Role falls back to frontmatter title when Profile section missing
    assert entry.role == "Alice Example"
    assert entry.company == "Acme"
    assert entry.email == "alice@acme.com"
    assert entry.aliases == ["Al", "Alice"]
    assert entry.last_contact == "2026-01-01"

