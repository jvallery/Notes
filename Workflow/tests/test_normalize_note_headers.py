from scripts.normalize_note_headers import normalize_body_header


def test_normalize_body_header_replaces_account_placeholder():
    body = """# Title

**Date**: 2025-01-01
**Account**: [[]]
**Attendees**: A, B
"""

    updated = normalize_body_header(body, header_label="Account", entity_name="Microsoft")
    assert "**Account**: [[Microsoft]]" in updated


def test_normalize_body_header_replaces_project_placeholder():
    body = """# Title

**Date**: 2025-01-01
**Project**: [[]]
**Attendees**: A, B
"""

    updated = normalize_body_header(body, header_label="Project", entity_name="Cloud")
    assert "**Project**: [[Cloud]]" in updated

