"""
Structured patch operations - NO REGEX for content modification.

These primitives are safe, deterministic, and testable.
"""

from pathlib import Path
import sys

# Add parent directories to path for imports
_script_dir = Path(__file__).parent
_workflow_dir = _script_dir.parent.parent
if str(_workflow_dir) not in sys.path:
    sys.path.insert(0, str(_workflow_dir))

from scripts.utils.frontmatter import parse_frontmatter, render_frontmatter


def upsert_frontmatter(content: str, patches: list) -> str:
    """
    Update or insert frontmatter fields.

    patches: list of FrontmatterPatch objects or dicts with 'key' and 'value'
    None value = remove key.
    """
    fm, body = parse_frontmatter(content)

    if fm is None:
        fm = {}

    for patch in patches:
        # Handle both FrontmatterPatch objects and dicts
        if hasattr(patch, 'key'):
            key, value = patch.key, patch.value
        else:
            key, value = patch['key'], patch['value']
        
        if value is None:
            fm.pop(key, None)
        else:
            fm[key] = value

    return render_frontmatter(fm) + body


def append_under_heading(content: str, heading: str, text: str) -> str:
    """
    Append text under a specific heading.

    CRITICAL: Requires EXACT heading level match.
    - "## Context" matches only "## Context", not "### Context"
    - Creates heading if not found
    - Ensures proper newline spacing
    """
    lines = content.split("\n")
    heading_prefix = heading.split()[0]  # e.g., "##" from "## Context"
    heading_text = heading[len(heading_prefix):].strip()

    # Find the target heading
    target_line = None
    for i, line in enumerate(lines):
        stripped = line.strip()
        # Must start with exact prefix and have matching text
        if stripped.startswith(heading_prefix + " "):
            line_text = stripped[len(heading_prefix):].strip()
            if line_text.lower() == heading_text.lower():
                target_line = i
                break

    if target_line is None:
        # Heading not found - append at end with the heading
        if not content.endswith("\n"):
            content += "\n"
        content += f"\n{heading}\n\n{text.rstrip()}\n"
        return content

    # Find end of section (next heading of same or higher level, or EOF)
    heading_level = len(heading_prefix)  # Number of #
    end_line = len(lines)

    for i in range(target_line + 1, len(lines)):
        stripped = lines[i].strip()
        if stripped.startswith("#"):
            # Count the heading level
            current_level = 0
            for char in stripped:
                if char == "#":
                    current_level += 1
                else:
                    break
            if current_level <= heading_level:
                end_line = i
                break

    # Insert content before end_line
    # Ensure there's content separation
    insert_text = text.rstrip()

    # Find last non-empty line in section
    last_content_line = target_line
    for i in range(end_line - 1, target_line, -1):
        if lines[i].strip():
            last_content_line = i
            break

    # Insert after last content, with blank line if needed
    new_lines = lines[:last_content_line + 1]
    if new_lines[-1].strip():  # If last line has content, add blank line
        new_lines.append("")
    new_lines.append(insert_text)
    new_lines.extend(lines[end_line:])

    return "\n".join(new_lines)


def ensure_wikilinks(content: str, links: list[str]) -> str:
    """
    Ensure wikilinks exist somewhere in content.

    Only adds links that don't already exist (case-insensitive check).
    Adds to ## Related section if missing, creates section if needed.
    """
    content_lower = content.lower()
    missing_links = []

    for link in links:
        # Normalize the link format
        if not link.startswith("[["):
            link = f"[[{link}]]"
        if not link.endswith("]]"):
            link = f"{link}]]"

        # Check if link exists (case-insensitive)
        if link.lower() not in content_lower:
            missing_links.append(link)

    if not missing_links:
        return content  # All links already present

    # Add missing links to ## Related section
    related_content = "\n".join(f"- {link}" for link in missing_links)

    # Check if ## Related exists
    if "## related" in content_lower:
        return append_under_heading(content, "## Related", related_content)
    else:
        # Add ## Related section
        if not content.endswith("\n"):
            content += "\n"
        content += f"\n## Related\n\n{related_content}\n"
        return content
