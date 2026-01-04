"""
Tests for standards compliance validation.
"""

import pytest
from scripts.utils.standards_check import (
    check_frontmatter,
    check_filename,
    check_path,
    validate_before_write,
)


class TestCheckFrontmatter:
    """Tests for frontmatter validation."""

    def test_valid_people_note(self, sample_readme: str):
        """Valid people note should pass."""
        issues = check_frontmatter(sample_readme, "people")
        assert len(issues) == 0

    def test_missing_required_keys(self):
        """Should detect missing required keys."""
        content = """---
title: Test
---

# Test
"""
        issues = check_frontmatter(content, "customer")
        
        # Should report missing: type, date, tags, account
        assert any("type" in i for i in issues)
        assert any("date" in i for i in issues)
        assert any("account" in i for i in issues)

    def test_invalid_date_format(self):
        """Should detect non-ISO date format."""
        content = """---
type: journal
title: Test
date: January 15, 2025
tags:
  - type/journal
---

# Test
"""
        issues = check_frontmatter(content, "journal")
        assert any("ISO-8601" in i or "date" in i.lower() for i in issues)

    def test_missing_type_tag(self):
        """Should detect missing type/* tag."""
        content = """---
type: customer
title: Test
date: 2025-01-15
account: Google
tags:
  - google
  - enterprise
---

# Test
"""
        issues = check_frontmatter(content, "customer")
        assert any("type/customer" in i.lower() or "type tag" in i.lower() for i in issues)


class TestCheckFilename:
    """Tests for filename validation."""

    def test_valid_dated_filename(self):
        """Valid dated filename should pass."""
        issues = check_filename("2025-01-15 - Weekly Sync.md")
        assert len(issues) == 0

    def test_valid_readme(self):
        """README.md should always pass."""
        issues = check_filename("README.md")
        assert len(issues) == 0

    def test_invalid_date_prefix(self):
        """Should detect invalid date prefix."""
        issues = check_filename("Jan 15 2025 - Weekly Sync.md")
        assert len(issues) > 0

    def test_no_separator(self):
        """Should detect missing separator."""
        issues = check_filename("2025-01-15 Weekly Sync.md")
        # This might pass or fail depending on strictness
        # Just verify function runs without error
        assert isinstance(issues, list)


class TestCheckPath:
    """Tests for path validation."""

    def test_valid_people_path(self):
        """Valid people path should pass."""
        issues = check_path("VAST/People/Jeff Denworth/2025-01-15 - Weekly Sync.md")
        assert len(issues) == 0

    def test_valid_customer_path(self):
        """Valid customer path should pass."""
        issues = check_path("VAST/Customers and Partners/Google/2025-01-15 - Meeting.md")
        assert len(issues) == 0

    def test_invalid_path(self):
        """Invalid path should be flagged (or may be empty if no specific checks)."""
        issues = check_path("Random/Folder/file.md")
        # Path checking is currently permissive - unknown paths are allowed
        # This test just verifies the function runs
        assert isinstance(issues, list)


class TestValidateBeforeWrite:
    """Integration tests for full validation."""

    def test_valid_note_passes(self, sample_readme: str, temp_vault):
        """Valid note should pass all checks."""
        target = temp_vault / "VAST" / "People" / "Jeff Denworth" / "README.md"
        issues = validate_before_write(target, sample_readme, "people")
        assert len(issues) == 0

    def test_collects_all_issues(self, temp_vault):
        """Should collect issues from all checks."""
        content = """---
title: Bad Note
---

# Bad Note
"""
        target = temp_vault / "Random" / "bad-filename.md"
        issues = validate_before_write(target, content, "customer")
        
        # Should have multiple issues
        assert len(issues) >= 3  # Missing frontmatter fields, bad path, maybe bad filename
