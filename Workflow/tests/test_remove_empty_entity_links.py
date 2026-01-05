from scripts.remove_empty_entity_links import remove_empty_entity_links


def test_remove_empty_entity_links_removes_account_and_project_placeholders():
    body = """# Title

**Date**: 2025-01-01
**Account**: [[]]
**Project**: [[]]
**Attendees**: A, B

## Summary
Hello
"""

    updated = remove_empty_entity_links(body)
    assert "**Account**: [[]]" not in updated
    assert "**Project**: [[]]" not in updated
    assert "**Attendees**: A, B" in updated

