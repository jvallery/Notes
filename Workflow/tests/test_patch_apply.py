from pathlib import Path

from pipeline.apply import TransactionalApply
from pipeline.patch import ChangePlan, PatchOperation


def _create_minimal_template(vault_root: Path):
    templates_dir = vault_root / "Workflow" / "templates"
    templates_dir.mkdir(parents=True, exist_ok=True)
    (templates_dir / "people.md.j2").write_text("{{ title }}\n\n## Summary\n{{ summary|default('') }}\n")


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
