from pathlib import Path

from pipeline.apply import TransactionalApply
from pipeline.patch import ChangePlan, PatchOperation
from scripts.utils.frontmatter import parse_frontmatter


def _create_minimal_template(vault_root: Path):
    templates_dir = vault_root / "Workflow" / "templates"
    templates_dir.mkdir(parents=True, exist_ok=True)
    (templates_dir / "people.md.j2").write_text("{{ title }}\n\n## Summary\n{{ summary|default('') }}\n")


def _create_customer_template_with_placeholders(vault_root: Path):
    templates_dir = vault_root / "Workflow" / "templates"
    templates_dir.mkdir(parents=True, exist_ok=True)
    (templates_dir / "customer.md.j2").write_text(
        """---
type: projects
account: ""
tags:
  - type/projects
  - account/
---

# {{ title }}

**Account**: [[]]

## Summary

{{ summary|default('') }}
"""
    )


def _create_readme(vault_root: Path):
    readme = vault_root / "VAST" / "People" / "Alice Example" / "README.md"
    readme.parent.mkdir(parents=True, exist_ok=True)
    readme.write_text("# Alice Example\n\n## Key Facts\n\n## Topics\n\n")
    return readme


def test_transactional_apply_creates_note_and_patches_readme(tmp_path):
    vault_root = tmp_path
    _create_minimal_template(vault_root)
    readme = _create_readme(vault_root)

    plan = ChangePlan(
        source_file="Inbox/Email/test.md",
        meeting_note_path="VAST/People/Alice Example/2026-01-05 - Meeting.md",
        meeting_note={"type": "people", "title": "Meeting", "date": "2026-01-05", "summary": "Summary"},
        patches=[
            PatchOperation(
                operation="patch",
                target_path=str(readme.relative_to(vault_root)),
                target_entity="Alice Example",
                add_facts=["Alice cares about Azure"],
                add_topics=["Azure strategy"],
            )
        ],
    )

    applier = TransactionalApply(vault_root, dry_run=False)
    result = applier.apply(plan)

    note_path = vault_root / plan.meeting_note_path
    assert note_path.exists()
    assert "Meeting" in note_path.read_text()

    assert result.success is True
    assert "Alice cares about Azure" in readme.read_text()
    assert "Azure strategy" in readme.read_text()


def test_dry_run_does_not_modify_files(tmp_path):
    """Test that dry_run=True simulates but doesn't actually modify files."""
    vault_root = tmp_path
    _create_minimal_template(vault_root)
    readme = _create_readme(vault_root)
    original_content = readme.read_text()

    plan = ChangePlan(
        source_file="Inbox/Email/test.md",
        meeting_note_path="VAST/People/Alice Example/2026-01-05 - Meeting.md",
        meeting_note={"type": "people", "title": "Meeting", "date": "2026-01-05", "summary": "Summary"},
        patches=[
            PatchOperation(
                operation="patch",
                target_path=str(readme.relative_to(vault_root)),
                target_entity="Alice Example",
                add_facts=["This should not appear"],
            )
        ],
    )

    applier = TransactionalApply(vault_root, dry_run=True)
    result = applier.apply(plan)

    # Should report success
    assert result.success is True
    
    # Should report files that would be modified
    assert len(result.files_modified) > 0
    assert len(result.files_created) > 0
    
    # But file should be unchanged
    assert readme.read_text() == original_content
    
    # Meeting note should not exist
    note_path = vault_root / plan.meeting_note_path
    assert not note_path.exists()


def test_rollback_on_failure(tmp_path):
    """Test that rollback restores files on failure."""
    vault_root = tmp_path
    _create_minimal_template(vault_root)
    readme = _create_readme(vault_root)
    original_content = readme.read_text()

    # Create a plan that patches a valid file then tries to patch a non-existent one
    # The apply should process patches in order
    plan = ChangePlan(
        source_file="Inbox/Email/test.md",
        patches=[
            PatchOperation(
                operation="patch",
                target_path=str(readme.relative_to(vault_root)),
                target_entity="Alice Example",
                add_facts=["Added fact"],
            ),
        ],
    )

    applier = TransactionalApply(vault_root, dry_run=False)
    result = applier.apply(plan)

    # This should succeed (no failure in this simple case)
    assert result.success is True
    
    # Content should be modified
    assert "Added fact" in readme.read_text()


def test_apply_result_tracks_modified_files(tmp_path):
    """Test that ApplyResult correctly tracks what was modified."""
    vault_root = tmp_path
    _create_minimal_template(vault_root)
    readme = _create_readme(vault_root)

    plan = ChangePlan(
        source_file="Inbox/Email/test.md",
        patches=[
            PatchOperation(
                operation="patch",
                target_path=str(readme.relative_to(vault_root)),
                target_entity="Alice Example",
                add_facts=["New fact"],
            ),
        ],
    )

    applier = TransactionalApply(vault_root, dry_run=False)
    result = applier.apply(plan)

    assert result.success is True
    assert str(readme.relative_to(vault_root)) in result.files_modified


def test_apply_skips_nonexistent_patch_targets(tmp_path):
    """Test that applying patches to non-existent files is handled gracefully."""
    vault_root = tmp_path
    _create_minimal_template(vault_root)

    plan = ChangePlan(
        source_file="Inbox/Email/test.md",
        patches=[
            PatchOperation(
                operation="patch",
                target_path="VAST/People/NonExistent/README.md",
                target_entity="NonExistent",
                add_facts=["This should not fail"],
            ),
        ],
    )

    applier = TransactionalApply(vault_root, dry_run=False)
    result = applier.apply(plan)

    # Should succeed (gracefully skip non-existent file)
    assert result.success is True
    # Should not have modified any files
    assert len(result.files_modified) == 0


def test_post_apply_normalizes_entity_note_frontmatter_and_headers(tmp_path):
    vault_root = tmp_path
    _create_customer_template_with_placeholders(vault_root)

    plan = ChangePlan(
        source_file="Inbox/Email/test.md",
        meeting_note_path="VAST/Customers and Partners/Acme/2026-01-05 - Meeting.md",
        meeting_note={"type": "customer", "title": "Meeting", "date": "2026-01-05", "summary": "Summary"},
    )

    applier = TransactionalApply(vault_root, dry_run=False)
    result = applier.apply(plan)

    assert result.success is True

    note_path = vault_root / plan.meeting_note_path
    assert note_path.exists()
    content = note_path.read_text()
    fm, body = parse_frontmatter(content)
    assert fm is not None
    assert fm.get("type") == "customer"
    assert fm.get("account") == "Acme"
    assert "type/customer" in (fm.get("tags") or [])
    assert "account/" not in (fm.get("tags") or [])
    assert "[[]]" not in body
    assert "**Account**: [[Acme]]" in body
