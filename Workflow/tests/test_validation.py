"""
Tests for changeplan validation.
"""

import pytest
from pydantic import ValidationError
from models.changeplan import ChangePlan, Operation, PatchSpec
from scripts.utils.validation import validate_changeplan


class TestChangePlanValidation:
    """Tests for changeplan schema validation."""

    def test_valid_changeplan(self, sample_changeplan: dict):
        """Valid changeplan should parse without errors."""
        plan = ChangePlan.model_validate(sample_changeplan)
        
        assert plan.version == "1.0"
        assert len(plan.operations) == 3
        assert plan.operations[0].op == "create"
        assert plan.operations[1].op == "patch"
        assert plan.operations[2].op == "link"

    def test_invalid_operation_type(self, sample_changeplan: dict):
        """Should reject invalid operation types."""
        sample_changeplan["operations"][0]["op"] = "invalid_op"
        
        with pytest.raises(ValidationError):
            ChangePlan.model_validate(sample_changeplan)

    def test_create_requires_template(self, sample_changeplan: dict):
        """Create operation should require template."""
        sample_changeplan["operations"][0]["template"] = None
        
        # validate_changeplan should catch this
        plan = ChangePlan.model_validate(sample_changeplan)
        errors = validate_changeplan(plan)
        
        assert len(errors) > 0
        assert any("template" in e.lower() for e in errors)

    def test_patch_requires_patches(self, sample_changeplan: dict):
        """Patch operation should require patches list."""
        sample_changeplan["operations"][1]["patches"] = None
        
        plan = ChangePlan.model_validate(sample_changeplan)
        errors = validate_changeplan(plan)
        
        assert len(errors) > 0
        assert any("patch" in e.lower() for e in errors)

    def test_link_requires_links(self, sample_changeplan: dict):
        """Link operation should require links list."""
        sample_changeplan["operations"][2]["links"] = None
        
        plan = ChangePlan.model_validate(sample_changeplan)
        errors = validate_changeplan(plan)
        
        assert len(errors) > 0
        assert any("link" in e.lower() for e in errors)

    def test_path_traversal_rejected(self, sample_changeplan: dict):
        """Should reject path traversal attempts."""
        sample_changeplan["operations"][0]["path"] = "../../../etc/passwd"
        
        plan = ChangePlan.model_validate(sample_changeplan)
        errors = validate_changeplan(plan)
        
        assert len(errors) > 0
        assert any("path" in e.lower() or "traversal" in e.lower() for e in errors)

    def test_absolute_path_rejected(self, sample_changeplan: dict):
        """Should reject absolute paths."""
        sample_changeplan["operations"][0]["path"] = "/Users/jason/malicious.md"
        
        plan = ChangePlan.model_validate(sample_changeplan)
        errors = validate_changeplan(plan)
        
        assert len(errors) > 0

    def test_invalid_template_rejected(self, sample_changeplan: dict):
        """Should reject templates not in allowed list."""
        sample_changeplan["operations"][0]["template"] = "malicious.j2"
        
        plan = ChangePlan.model_validate(sample_changeplan)
        errors = validate_changeplan(plan)
        
        assert len(errors) > 0
        assert any("template" in e.lower() for e in errors)


class TestOperationModel:
    """Tests for Operation Pydantic model."""

    def test_create_operation(self):
        """Create operation should have required fields."""
        op = Operation(
            op="create",
            path="VAST/People/Test/2025-01-15 - Note.md",
            template="people.md.j2",
            context={
                "title": "Test",
                "date": "2025-01-15",
                "person": "Test",
                "summary": "Test summary for meeting",
                "participants": ["Test Person"],
                "source": "transcript",
                "source_ref": ""
            }
        )
        
        assert op.op == "create"
        assert op.template == "people.md.j2"

    def test_patch_operation(self):
        """Patch operation should have patches."""
        op = Operation(
            op="patch",
            path="VAST/People/Test/README.md",
            patches=[
                PatchSpec(
                    primitive="upsert_frontmatter",
                    frontmatter=[{"key": "last_contact", "value": "2025-01-15"}]
                )
            ]
        )
        
        assert op.op == "patch"
        assert len(op.patches) == 1

    def test_link_operation(self):
        """Link operation should have links."""
        op = Operation(
            op="link",
            path="VAST/People/Test/2025-01-15 - Note.md",
            links=["[[Google]]", "[[Walmart]]"]
        )
        
        assert op.op == "link"
        assert len(op.links) == 2
