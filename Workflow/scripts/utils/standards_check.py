"""
Standards compliance validation.

Validates output files against STANDARDS.md requirements before writing.
Used by apply phase to ensure all generated content meets vault standards.
"""

from __future__ import annotations

import re
from pathlib import Path

from scripts.utils.frontmatter import parse_frontmatter


# ─────────────────────────────────────────────────────────────────────────────
# Required Frontmatter Keys by Note Type
# ─────────────────────────────────────────────────────────────────────────────

# Base required keys for all notes
BASE_REQUIRED_KEYS = ["type", "title", "date", "tags"]

# Additional required keys by note type
TYPE_REQUIRED_KEYS = {
    "people": ["person"],
    "customer": ["account"],
    "projects": ["project"],
    "rob": ["rob_forum"],
    "partners": ["partner"],
    "travel": [],  # destination is optional
    "journal": [],
}

# Keys required for automation-generated notes
AUTOMATION_KEYS = ["source", "source_ref"]


# ─────────────────────────────────────────────────────────────────────────────
# Pattern Definitions
# ─────────────────────────────────────────────────────────────────────────────

# Tag format: lowercase letters, numbers, hyphens, optional single slash
TAG_PATTERN = re.compile(r"^[a-z0-9-]+(/[a-z0-9-]+)?$")

# Date format: YYYY-MM-DD
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")

# Dated note filename: YYYY-MM-DD - Title.md
DATED_NOTE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2} - .+\.md$")

# Email filename: YYYY-MM-DD_HHMMSS_NNNN_Subject.md or .eml
EMAIL_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{6}_\d{4}_.+\.(md|eml)$")

# README files
README_PATTERN = re.compile(r"^README\.md$", re.IGNORECASE)

# Forbidden characters in filenames
FORBIDDEN_CHARS = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']


# ─────────────────────────────────────────────────────────────────────────────
# Validation Functions
# ─────────────────────────────────────────────────────────────────────────────

def check_frontmatter(
    content: str,
    note_type: str,
    is_generated: bool = True,
) -> list[str]:
    """
    Check frontmatter for required keys and valid values.
    
    Args:
        content: Full file content with frontmatter
        note_type: Expected note type (people, customer, etc.)
        is_generated: Whether this is an automation-generated note
        
    Returns:
        List of validation issues (empty if valid)
    """
    issues = []
    
    fm, _ = parse_frontmatter(content)
    if fm is None:
        return ["Missing frontmatter"]
    
    # Check base required keys
    for key in BASE_REQUIRED_KEYS:
        if key not in fm:
            issues.append(f"Missing required key: {key}")
    
    # Check type-specific required keys
    type_keys = TYPE_REQUIRED_KEYS.get(note_type, [])
    for key in type_keys:
        if key not in fm:
            issues.append(f"Missing required key for {note_type}: {key}")
    
    # Check automation keys for generated notes
    if is_generated:
        for key in AUTOMATION_KEYS:
            if key not in fm:
                issues.append(f"Missing automation key: {key}")
    
    # Validate type value matches expected
    if fm.get("type") != note_type:
        issues.append(f"Type mismatch: expected '{note_type}', got '{fm.get('type')}'")
    
    # Validate date format
    date_val = fm.get("date", "")
    if date_val:
        if not DATE_PATTERN.match(str(date_val)):
            issues.append(f"Invalid date format: {date_val} (expected YYYY-MM-DD)")
    
    # Validate tags
    tags = fm.get("tags", [])
    if not tags:
        issues.append("No tags found")
    else:
        if not isinstance(tags, list):
            issues.append(f"Tags must be a list, got {type(tags).__name__}")
        else:
            for tag in tags:
                if not isinstance(tag, str):
                    issues.append(f"Tag must be string: {tag}")
                elif not TAG_PATTERN.match(tag):
                    issues.append(f"Invalid tag format: {tag} (must be lowercase, hyphens, optional slash)")
    
    # Check for type tag
    type_tag = f"type/{note_type}"
    if isinstance(tags, list) and type_tag not in tags:
        issues.append(f"Missing type tag: {type_tag}")
    
    return issues


def check_filename(
    filename: str,
    context: str = "note",
) -> list[str]:
    """
    Check filename against standards.
    
    Args:
        filename: Just the filename (not full path)
        context: "note" for dated notes, "email" for email imports, "readme" for READMEs
        
    Returns:
        List of validation issues (empty if valid)
    """
    issues = []
    
    # Check for forbidden characters
    for char in FORBIDDEN_CHARS:
        if char in filename:
            issues.append(f"Forbidden character in filename: '{char}'")
    
    # Context-specific pattern checks
    if context == "note":
        if not DATED_NOTE_PATTERN.match(filename) and not README_PATTERN.match(filename):
            issues.append(
                f"Invalid note filename: {filename} "
                "(expected 'YYYY-MM-DD - Title.md' or 'README.md')"
            )
    elif context == "email":
        if not EMAIL_PATTERN.match(filename):
            issues.append(
                f"Invalid email filename: {filename} "
                "(expected 'YYYY-MM-DD_HHMMSS_NNNN_Subject.md')"
            )
    elif context == "readme":
        if not README_PATTERN.match(filename):
            issues.append(f"Invalid README filename: {filename} (expected 'README.md')")
    
    return issues


def check_path(
    path: str | Path,
    vault_root: Path | None = None,
) -> list[str]:
    """
    Check path for safety and validity.
    
    Args:
        path: Relative path from vault root
        vault_root: Optional vault root to check path resolves within
        
    Returns:
        List of validation issues (empty if valid)
    """
    issues = []
    path_str = str(path)
    
    # Check for path traversal
    if ".." in path_str:
        issues.append("Path contains '..' traversal")
    
    # Check for absolute paths
    if path_str.startswith("/") or (len(path_str) > 1 and path_str[1] == ":"):
        issues.append("Path must be relative, not absolute")
    
    # Check for backslashes (Windows paths)
    if "\\" in path_str:
        issues.append("Path contains backslash (use forward slashes)")
    
    # Check path resolves within vault
    if vault_root:
        try:
            resolved = (vault_root / path).resolve()
            if not str(resolved).startswith(str(vault_root.resolve())):
                issues.append("Path resolves outside vault root")
        except Exception as e:
            issues.append(f"Path resolution error: {e}")
    
    return issues


def validate_before_write(
    path: Path,
    content: str,
    note_type: str,
) -> list[str]:
    """
    Run all validations before writing a file.
    
    This is the main entry point for pre-write validation.
    
    Args:
        path: Full path where file will be written
        content: Content to be written
        note_type: Expected note type
        
    Returns:
        List of issues (empty if valid)
    """
    issues = []
    
    # Check filename
    filename = path.name
    if filename.lower() == "readme.md":
        issues.extend(check_filename(filename, context="readme"))
    else:
        issues.extend(check_filename(filename, context="note"))
    
    # Check content/frontmatter
    issues.extend(check_frontmatter(content, note_type, is_generated=True))
    
    return issues


def validate_for_apply(
    path: Path,
    content: str,
    note_type: str,
    vault_root: Path,
    strict: bool = True,
) -> list[str]:
    """
    Full validation for apply phase.
    
    Args:
        path: Relative path from vault root
        content: Content to be written
        note_type: Expected note type
        vault_root: Vault root directory
        strict: If True, all issues are errors; if False, some are warnings
        
    Returns:
        List of issues (empty if valid)
    """
    issues = []
    
    # Path validation
    issues.extend(check_path(path, vault_root))
    
    # File validation (if we have content)
    if content:
        full_path = vault_root / path
        issues.extend(validate_before_write(full_path, content, note_type))
    
    return issues
