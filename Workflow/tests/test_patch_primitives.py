"""
Tests for patch primitive operations.

These test the core file manipulation functions without AI calls.
"""

import pytest
from scripts.utils.patch_primitives import (
    upsert_frontmatter,
    append_under_heading,
    ensure_wikilinks,
)


class TestUpsertFrontmatter:
    """Tests for frontmatter manipulation."""

    def test_update_existing_key(self, sample_readme: str):
        """Should update an existing frontmatter key."""
        patches = [{"key": "last_contact", "value": "2025-01-15"}]
        result = upsert_frontmatter(sample_readme, patches)
        
        assert "last_contact: '2025-01-15'" in result or "last_contact: 2025-01-15" in result

    def test_add_new_key(self, sample_readme: str):
        """Should add a new frontmatter key."""
        patches = [{"key": "status", "value": "active"}]
        result = upsert_frontmatter(sample_readme, patches)
        
        assert "status: active" in result

    def test_remove_key_with_none(self, sample_readme: str):
        """Should remove a key when value is None."""
        patches = [{"key": "last_contact", "value": None}]
        result = upsert_frontmatter(sample_readme, patches)
        
        assert "last_contact:" not in result

    def test_preserves_body(self, sample_readme: str):
        """Should preserve body content after frontmatter."""
        patches = [{"key": "last_contact", "value": "2025-01-15"}]
        result = upsert_frontmatter(sample_readme, patches)
        
        assert "# Jeff Denworth" in result
        assert "Co-founder and CMO at VAST Data." in result

    def test_content_without_frontmatter(self):
        """Should create frontmatter if none exists."""
        content = "# Simple Note\n\nSome content here."
        patches = [{"key": "type", "value": "journal"}]
        result = upsert_frontmatter(content, patches)
        
        assert result.startswith("---\n")
        assert "type: journal" in result
        assert "# Simple Note" in result

    def test_list_value(self, sample_readme: str):
        """Should handle list values."""
        patches = [{"key": "tags", "value": ["tag1", "tag2", "tag3"]}]
        result = upsert_frontmatter(sample_readme, patches)
        
        assert "tag1" in result
        assert "tag2" in result


class TestAppendUnderHeading:
    """Tests for heading content manipulation."""

    def test_append_to_existing_heading(self, sample_readme: str):
        """Should append content under existing heading."""
        result = append_under_heading(
            sample_readme,
            "## Recent Context",
            "- 2025-01-15: New meeting note"
        )
        
        assert "- 2025-01-15: New meeting note" in result
        # Original content should be preserved
        assert "- 2025-01-10: Discussed Q1 marketing priorities" in result

    def test_create_new_heading(self, sample_readme: str):
        """Should create heading if it doesn't exist."""
        result = append_under_heading(
            sample_readme,
            "## Action Items",
            "- [ ] Follow up on deal"
        )
        
        assert "## Action Items" in result
        assert "- [ ] Follow up on deal" in result

    def test_respects_heading_level(self):
        """Should match heading level correctly."""
        content = "# Title\n\n## Section A\n\nContent A\n\n## Section B\n\nContent B"
        result = append_under_heading(content, "## Section A", "New line")
        
        # Should add under Section A, not Section B
        lines = result.split("\n")
        section_a_idx = next(i for i, l in enumerate(lines) if "## Section A" in l)
        section_b_idx = next(i for i, l in enumerate(lines) if "## Section B" in l)
        new_line_idx = next(i for i, l in enumerate(lines) if "New line" in l)
        
        assert section_a_idx < new_line_idx < section_b_idx


class TestEnsureWikilinks:
    """Tests for wikilink insertion."""

    def test_adds_missing_links(self, sample_readme: str):
        """Should add missing wikilinks."""
        result = ensure_wikilinks(sample_readme, ["[[Google]]", "[[Walmart]]"])
        
        assert "[[Google]]" in result
        assert "[[Walmart]]" in result

    def test_skips_existing_links(self):
        """Should not duplicate existing links."""
        content = "# Note\n\n## Related\n\n- [[Google]]\n"
        result = ensure_wikilinks(content, ["[[Google]]", "[[Walmart]]"])
        
        # Should only have one [[Google]]
        assert result.count("[[Google]]") == 1
        assert "[[Walmart]]" in result

    def test_case_insensitive_match(self):
        """Should match links case-insensitively."""
        content = "Mentioned [[google]] in the meeting."
        result = ensure_wikilinks(content, ["[[Google]]"])
        
        # Should not add duplicate
        assert result.count("google") + result.count("Google") == 1

    def test_creates_related_section(self):
        """Should create Related section if needed."""
        content = "# Note\n\nSome content.\n"
        result = ensure_wikilinks(content, ["[[New Link]]"])
        
        assert "## Related" in result
        assert "[[New Link]]" in result
