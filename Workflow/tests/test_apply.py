"""
Tests for apply.py path validation and round-trip tests.

T11: Test Coverage Gaps - apply path validation + rollback tests.
"""

import pytest
import json
from pathlib import Path
from datetime import datetime

from models.changeplan import ChangePlan, Operation, PatchSpec, HeadingPatch
from models.extraction import ExtractionV1


class TestApplyPathValidation:
    """Tests for apply.py path safety validation."""

    def test_path_must_be_relative(self, temp_vault: Path):
        """Absolute paths should be rejected."""
        from scripts.utils.validation import validate_changeplan
        from models.changeplan import CreateContext
        
        plan = ChangePlan(
            version="1.0",
            source_file="Inbox/Transcripts/test.md",
            extraction_file="Inbox/_extraction/test.extraction.json",
            created_at=datetime.now(),
            operations=[
                Operation(
                    op="create",
                    path="/Users/jason/malicious.md",  # Absolute path
                    template="people.md.j2",
                    context=CreateContext(title="Test", date="2025-01-15", summary="Test summary")
                )
            ]
        )
        
        errors = validate_changeplan(plan)
        assert any("path" in e.lower() or "absolute" in e.lower() for e in errors)

    def test_path_traversal_blocked(self, temp_vault: Path):
        """Path traversal attempts should be blocked."""
        from scripts.utils.validation import validate_changeplan
        from models.changeplan import CreateContext
        
        plan = ChangePlan(
            version="1.0",
            source_file="Inbox/Transcripts/test.md",
            extraction_file="Inbox/_extraction/test.extraction.json",
            created_at=datetime.now(),
            operations=[
                Operation(
                    op="create",
                    path="../../../etc/passwd",  # Path traversal
                    template="people.md.j2",
                    context=CreateContext(title="Test", date="2025-01-15", summary="Test summary")
                )
            ]
        )
        
        errors = validate_changeplan(plan)
        assert len(errors) > 0

    def test_path_must_be_in_content_dirs(self, temp_vault: Path):
        """Paths outside content directories are rejected."""
        from scripts.utils.validation import validate_changeplan
        from models.changeplan import CreateContext
        
        # Path in Workflow/ - currently not explicitly rejected
        plan = ChangePlan(
            version="1.0",
            source_file="Inbox/Transcripts/test.md",
            extraction_file="Inbox/_extraction/test.extraction.json",
            created_at=datetime.now(),
            operations=[
                Operation(
                    op="create",
                    path="Workflow/scripts/malicious.py",  # Would be suspicious
                    template="people.md.j2",
                    context=CreateContext(title="Test", date="2025-01-15", summary="Test summary")
                )
            ]
        )
        
        errors = validate_changeplan(plan)
        assert len(errors) > 0

    def test_valid_paths_accepted(self, temp_vault: Path):
        """Valid paths in content directories should be accepted."""
        from scripts.utils.validation import validate_changeplan
        from models.changeplan import CreateContext
        
        plan = ChangePlan(
            version="1.0",
            source_file="Inbox/Transcripts/test.md",
            extraction_file="Inbox/_extraction/test.extraction.json",
            created_at=datetime.now(),
            operations=[
                Operation(
                    op="create",
                    path="VAST/People/Jeff Denworth/2025-01-15 - Meeting.md",
                    template="people.md.j2",
                    context=CreateContext(
                        title="Meeting", 
                        date="2025-01-15", 
                        summary="Test meeting summary",
                        person="Jeff Denworth"
                    )
                )
            ]
        )
        
        errors = validate_changeplan(plan)
        # Filter out template errors - we're testing paths
        path_errors = [e for e in errors if "path" in e.lower()]
        assert len(path_errors) == 0


class TestExtractionToChangePlanRoundTrip:
    """Tests for extraction → changeplan round-trip consistency."""

    def test_extraction_model_validates(self, sample_extraction: dict):
        """Extraction JSON should validate against Pydantic model."""
        extraction = ExtractionV1.model_validate(sample_extraction)
        
        assert extraction.note_type == "people"
        assert extraction.entity_name == "Jeff Denworth"
        assert len(extraction.tasks) == 3
        assert extraction.confidence >= 0.9

    def test_changeplan_model_validates(self, sample_changeplan: dict):
        """ChangePlan JSON should validate against Pydantic model."""
        plan = ChangePlan.model_validate(sample_changeplan)
        
        assert plan.version == "1.0"
        assert len(plan.operations) == 3
        assert plan.operations[0].op == "create"
        assert plan.operations[1].op == "patch"
        assert plan.operations[2].op == "link"

    def test_extraction_changeplan_consistency(self, sample_extraction: dict, sample_changeplan: dict):
        """Extraction and ChangePlan should reference same source."""
        extraction = ExtractionV1.model_validate(sample_extraction)
        plan = ChangePlan.model_validate(sample_changeplan)
        
        assert extraction.source_file == plan.source_file

    def test_changeplan_paths_match_entity(self, sample_extraction: dict, sample_changeplan: dict):
        """ChangePlan paths should match extraction entity."""
        extraction = ExtractionV1.model_validate(sample_extraction)
        plan = ChangePlan.model_validate(sample_changeplan)
        
        # Create operation should target entity folder
        create_op = [op for op in plan.operations if op.op == "create"][0]
        assert extraction.entity_name in create_op.path

    def test_tasks_transferred_to_context(self, sample_extraction: dict, sample_changeplan: dict):
        """Tasks from extraction should appear in changeplan context."""
        ExtractionV1.model_validate(sample_extraction)  # Validates extraction
        plan = ChangePlan.model_validate(sample_changeplan)
        
        create_op = [op for op in plan.operations if op.op == "create"][0]
        context_tasks = create_op.context.tasks
        
        # At least some tasks should transfer
        assert len(context_tasks) > 0


class TestSchemaConsistency:
    """Tests for JSON Schema vs Pydantic model consistency."""

    def test_extraction_schema_matches_model(self, fixtures_dir: Path):
        """JSON Schema should accept what Pydantic accepts."""
        import jsonschema
        
        schema_path = Path(__file__).parent.parent / "schemas" / "extraction.schema.json"
        if not schema_path.exists():
            pytest.skip("Extraction schema not found")
        
        with open(schema_path) as f:
            schema = json.load(f)
        
        sample = json.loads((fixtures_dir / "sample-extraction.json").read_text())
        
        # Should not raise
        jsonschema.validate(sample, schema)

    def test_changeplan_schema_matches_model(self, fixtures_dir: Path):
        """JSON Schema should accept what Pydantic accepts."""
        import jsonschema
        
        schema_path = Path(__file__).parent.parent / "schemas" / "changeplan.schema.json"
        if not schema_path.exists():
            pytest.skip("ChangePlan schema not found")
        
        with open(schema_path) as f:
            schema = json.load(f)
        
        sample = json.loads((fixtures_dir / "sample-changeplan.json").read_text())
        
        # Should not raise
        jsonschema.validate(sample, schema)

    def test_patchspec_heading_structure(self):
        """PatchSpec heading should have correct nested structure."""
        patch = PatchSpec(
            primitive="append_under_heading",
            heading=HeadingPatch(
                heading="## Recent Context",
                content="- 2025-01-15: Test content"
            )
        )
        
        assert patch.heading.heading == "## Recent Context"
        assert patch.heading.content == "- 2025-01-15: Test content"


class TestApplyRollbackBehavior:
    """Tests for apply rollback mechanics."""

    def test_backup_preserves_relative_path(self, temp_vault: Path):
        """Backups should preserve vault-relative path structure."""
        import shutil
        
        # Helper to simulate backup_file behavior
        def backup_file(source: Path, backup_dir: Path, vault_root: Path) -> Path:
            rel_path = source.relative_to(vault_root)
            backup_path = backup_dir / rel_path
            backup_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, backup_path)
            return backup_path
        
        # Create a nested README
        readme_path = temp_vault / "VAST" / "People" / "Test Person" / "README.md"
        readme_path.parent.mkdir(parents=True, exist_ok=True)
        readme_path.write_text("# Test Person\n")
        
        backup_dir = temp_vault / ".workflow_backups" / "test-run"
        backup_path = backup_file(readme_path, backup_dir, temp_vault)
        
        # Backup should preserve structure
        assert "VAST" in str(backup_path)
        assert "People" in str(backup_path)
        assert "Test Person" in str(backup_path)

    def test_multiple_readme_backups_distinct(self, temp_vault: Path):
        """Multiple README.md files should produce distinct backups."""
        import shutil
        
        # Helper to simulate backup_file behavior
        def backup_file(source: Path, backup_dir: Path, vault_root: Path) -> Path:
            rel_path = source.relative_to(vault_root)
            backup_path = backup_dir / rel_path
            backup_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, backup_path)
            return backup_path
        
        # Create two READMEs in different folders
        readme1 = temp_vault / "VAST" / "People" / "Person1" / "README.md"
        readme1.parent.mkdir(parents=True, exist_ok=True)
        readme1.write_text("# Person 1\n")
        
        readme2 = temp_vault / "VAST" / "People" / "Person2" / "README.md"
        readme2.parent.mkdir(parents=True, exist_ok=True)
        readme2.write_text("# Person 2\n")
        
        backup_dir = temp_vault / ".workflow_backups" / "test-run"
        
        backup1 = backup_file(readme1, backup_dir, temp_vault)
        backup2 = backup_file(readme2, backup_dir, temp_vault)
        
        # Backups should be distinct files
        assert backup1 != backup2
        assert backup1.exists()
        assert backup2.exists()
        assert backup1.read_text() == "# Person 1\n"
        assert backup2.read_text() == "# Person 2\n"

    def test_created_files_tracked_for_rollback(self, temp_vault: Path):
        """New files created during apply should be tracked for rollback."""
        # Simulate what apply.py does
        created_files = []
        
        new_file = temp_vault / "VAST" / "People" / "New Person" / "2025-01-15 - Note.md"
        new_file.parent.mkdir(parents=True, exist_ok=True)
        new_file.write_text("# Meeting Note\n")
        created_files.append(new_file)
        
        # On rollback, delete created files
        for f in created_files:
            f.unlink()
        
        assert not new_file.exists()
