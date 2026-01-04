"""YAML frontmatter parsing and manipulation."""

from __future__ import annotations

import yaml
from typing import Any


def parse_frontmatter(content: str) -> tuple[dict | None, str]:
    """
    Extract frontmatter dict and body from markdown content.

    Returns (frontmatter_dict, body_content).
    If no frontmatter, returns (None, original_content).
    """
    if not content.startswith("---"):
        return None, content

    # Find the closing ---
    lines = content.split("\n")
    end_index = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_index = i
            break

    if end_index is None:
        # No closing ---, treat as no frontmatter
        return None, content

    fm_text = "\n".join(lines[1:end_index])
    body = "\n".join(lines[end_index + 1:])

    # Handle empty frontmatter
    if not fm_text.strip():
        return {}, body

    try:
        fm = yaml.safe_load(fm_text)
        if fm is None:
            fm = {}
    except yaml.YAMLError:
        # Invalid YAML, return as-is
        return None, content

    return fm, body


def render_frontmatter(fm: dict) -> str:
    """Convert dict to YAML frontmatter block."""
    if not fm:
        return "---\n---\n"

    yaml_content = yaml.dump(
        fm,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,  # Preserve insertion order
        width=1000,  # Prevent line wrapping
    )
    return f"---\n{yaml_content}---\n"


def update_frontmatter(content: str, updates: dict[str, Any]) -> str:
    """
    Merge updates into existing frontmatter.

    Creates frontmatter if none exists.
    Set value to None to remove a key.
    """
    fm, body = parse_frontmatter(content)

    if fm is None:
        fm = {}

    for key, value in updates.items():
        if value is None:
            fm.pop(key, None)
        else:
            fm[key] = value

    return render_frontmatter(fm) + body
