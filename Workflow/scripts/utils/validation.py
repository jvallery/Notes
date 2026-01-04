"""
ChangePlan validation utilities.

Consolidated validation logic for ChangePlan objects.
Used by both plan.py (post-generation validation) and apply.py (pre-apply validation).
"""

from models.changeplan import ChangePlan, OperationType, PatchPrimitive
from scripts.utils.templates import ALLOWED_TEMPLATES


def validate_changeplan(plan: ChangePlan) -> list[str]:
    """
    Strict validation of ChangePlan before any disk writes.
    
    This is the SINGLE SOURCE OF TRUTH for changeplan validation.
    Used by both planning phase (to flag issues) and apply phase (to reject invalid plans).
    
    Returns list of issues (empty if valid).
    """
    issues = []
    
    for i, op in enumerate(plan.operations):
        # Validate paths - no absolute, no traversal
        if (
            op.path.startswith("/")
            or "\\" in op.path
            or ":" in op.path
            or ".." in op.path
        ):
            issues.append(f"Operation {i}: invalid path '{op.path}'")
        
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
