from datetime import datetime

from pipeline.entities import EntityIndex
from pipeline.models import UnifiedExtraction
from pipeline.patch import PatchGenerator
from scripts.audit_import import VaultAuditor
from scripts.utils.frontmatter import parse_frontmatter
from scripts.utils.patch_primitives import upsert_frontmatter


def test_upsert_frontmatter_repairs_invalid_yaml_without_duplication():
    # Unescaped inner quotes make this YAML invalid.
    content = """---
title: "Alice "The Boss" Example"
---
# Body
"""

    fm, body = parse_frontmatter(content)
    assert fm == {}
    assert body.lstrip().startswith("# Body")

    updated = upsert_frontmatter(content, [{"key": "last_contact", "value": "2026-01-05"}])
    updated_fm, updated_body = parse_frontmatter(updated)

    assert updated_fm is not None
    assert updated_fm.get("last_contact") == "2026-01-05"
    assert not updated_body.lstrip().startswith("---")
    assert updated_body.lstrip().startswith("# Body")


def test_generate_readme_content_quotes_are_yaml_safe(tmp_path):
    gen = PatchGenerator(tmp_path, EntityIndex(tmp_path))
    extraction = UnifiedExtraction(
        source_file=str(tmp_path / "Inbox" / "Email" / "test.md"),
        content_type="email",
        processed_at=datetime.now(),
        note_type="customer",
        date="2026-01-05",
        title="Test",
        summary="Summary",
    )

    name = 'ACME "Widgets" Co.'
    content = gen._generate_readme_content(name, "company", email=None, extraction=extraction)
    fm, body = parse_frontmatter(content)

    assert fm is not None
    assert fm.get("title") == name
    assert body.lstrip().startswith(f"# {name}")


def test_audit_flags_duplicate_readme_frontmatter_blocks(tmp_path):
    readme = tmp_path / "VAST" / "People" / "Alice Example" / "README.md"
    readme.parent.mkdir(parents=True, exist_ok=True)
    readme.write_text(
        """---
type: people
title: Alice Example
---
---
type: people
title: Alice Example
---
# Alice Example
"""
    )

    auditor = VaultAuditor(tmp_path, verbose=False)
    auditor._check_readme_frontmatter_integrity()

    assert any("multiple yaml frontmatter" in f.message.lower() for f in auditor.findings)

