"""
ChangePlan validation utilities.

Consolidated validation logic for ChangePlan objects.
Used by both plan.py (post-generation validation) and apply.py (pre-apply validation).
"""

import re
from models.changeplan import ChangePlan, OperationType, PatchPrimitive
from scripts.utils.templates import ALLOWED_TEMPLATES
from scripts.utils.fs import sanitize_path


# Valid top-level path prefixes
VALID_PATH_PREFIXES = [
    "VAST/Customers and Partners/",
    "VAST/People/",
    "VAST/Projects/",
    "VAST/ROB/",
    "VAST/Journal/",
    "VAST/Travel/",
    "Personal/People/",
    "Personal/Projects/",
    "Personal/Journal/",
    "Personal/Travel/",
    "Personal/Homelab/",
]

# Invalid path patterns with explanations
INVALID_PATH_PATTERNS = [
    (r"VAST/Accounts/", "Use 'VAST/Customers and Partners/' not 'VAST/Accounts/'"),
    (r"VAST/Customers/", "Use 'VAST/Customers and Partners/' not 'VAST/Customers/'"),
    (r"Personal/Accounts/", "Use 'Personal/People/' or proper folder structure"),
    (r"^/", "Paths should not be absolute (start with /)"),
]


def validate_path_correctness(path: str) -> list[str]:
    """
    Validate that a path follows vault structure conventions.
    
    Returns list of issues (empty if valid).
    """
    issues = []
    
    # Check for invalid patterns
    for pattern, message in INVALID_PATH_PATTERNS:
        if re.search(pattern, path):
            issues.append(f"Invalid path '{path}': {message}")
    
    # Check path has valid prefix (for content paths, not READMEs)
    if not path.endswith("README.md"):
        has_valid_prefix = any(path.startswith(prefix) for prefix in VALID_PATH_PREFIXES)
        if not has_valid_prefix and not path.startswith("Inbox/"):
            issues.append(f"Path '{path}' doesn't start with valid prefix (VAST/, Personal/)")
    
    return issues


def validate_changeplan(plan: ChangePlan) -> list[str]:
    """
    Strict validation of ChangePlan before any disk writes.
    
    This is the SINGLE SOURCE OF TRUTH for changeplan validation.
    Used by both planning phase (to flag issues) and apply phase (to reject invalid plans).
    
    Paths are sanitized before validation - colons in filenames are automatically
    converted to dashes (e.g., "1:1" → "1-1").
    
    Returns list of issues (empty if valid).
    """
    issues = []
    
    for i, op in enumerate(plan.operations):
        # Sanitize path first (handles colons, etc.)
        sanitized = sanitize_path(op.path)
        
        # Validate path correctness (structure, naming conventions)
        path_issues = validate_path_correctness(sanitized)
        for issue in path_issues:
            issues.append(f"Operation {i}: {issue}")
        
        # Validate sanitized paths - no absolute, no traversal
        if (
            sanitized.startswith("/")
            or "\\" in sanitized
            or ".." in sanitized
        ):
            issues.append(f"Operation {i}: invalid path '{op.path}' (sanitized: '{sanitized}')")
        
        # Check for forbidden operations (archive is deterministic, not LLM-generated)
        if op.op.value not in ["create", "patch", "link"]:
            issues.append(f"Operation {i}: forbidden op type '{op.op.value}'")
        
        # Validate by operation type
        if op.op == OperationType.CREATE:
            if not op.template:
                issues.append(f"Operation {i}: CREATE requires template")
            elif op.template not in ALLOWED_TEMPLATES:
                issues.append(f"Operation {i}: forbidden template '{op.template}'")
            if not op.context:
                issues.append(f"Operation {i}: CREATE requires context")
            if op.patches or op.links:
                issues.append(f"Operation {i}: CREATE cannot include patches/links")
        
        elif op.op == OperationType.PATCH:
            if not op.patches:
                issues.append(f"Operation {i}: PATCH requires patches list")
            else:
                for j, patch in enumerate(op.patches):
                    allowed_primitives = [
                        PatchPrimitive.UPSERT_FRONTMATTER,
                        PatchPrimitive.APPEND_UNDER_HEADING,
                        PatchPrimitive.PREPEND_UNDER_HEADING,
                        PatchPrimitive.ENSURE_WIKILINKS,
                    ]
                    if patch.primitive not in allowed_primitives:
                        issues.append(f"Operation {i}.{j}: forbidden primitive '{patch.primitive}'")
                    if patch.primitive == PatchPrimitive.APPEND_UNDER_HEADING and not patch.heading:
                        issues.append(f"Operation {i}.{j}: append_under_heading requires heading")
                    if patch.primitive == PatchPrimitive.UPSERT_FRONTMATTER and not patch.frontmatter:
                        issues.append(f"Operation {i}.{j}: upsert_frontmatter requires frontmatter")
        
        elif op.op == OperationType.LINK:
            if not op.links:
                issues.append(f"Operation {i}: LINK requires links list")
    
    return issues
