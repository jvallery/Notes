"""
Pydantic models for Notes Vault automation.

These models enforce schema validation for all AI outputs.
Used with OpenAI's Structured Outputs via client.responses.parse().
"""

from .extraction import ExtractionV1, TaskItem
from .changeplan import (
    ChangePlan,
    Operation,
    OperationType,
    PatchSpec,
    PatchPrimitive,
    FrontmatterPatch,
    HeadingPatch,
)

__all__ = [
    # Extraction
    "ExtractionV1",
    "TaskItem",
    # ChangePlan
    "ChangePlan",
    "Operation",
    "OperationType",
    "PatchSpec",
    "PatchPrimitive",
    "FrontmatterPatch",
    "HeadingPatch",
]
