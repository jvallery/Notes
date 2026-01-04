"""Pydantic models for the ChangePlan phase output."""

from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from enum import Enum
from typing import Literal, Optional, List, Union, Dict


class OperationType(str, Enum):
    """Allowed operation types for ChangePlan."""

    CREATE = "create"
    PATCH = "patch"
    LINK = "link"


class PatchPrimitive(str, Enum):
    """Allowed patch primitives - no regex, only structured operations."""

    UPSERT_FRONTMATTER = "upsert_frontmatter"
    APPEND_UNDER_HEADING = "append_under_heading"
    ENSURE_WIKILINKS = "ensure_wikilinks"


class FrontmatterPatch(BaseModel):
    """A single frontmatter field update."""

    model_config = ConfigDict(extra="forbid")

    key: str
    value: Union[str, List[str], None]  # None = remove key


class HeadingPatch(BaseModel):
    """Content to append under a specific heading."""

    model_config = ConfigDict(extra="forbid")

    heading: str  # e.g., "## Recent Context"
    content: str  # Content to append


class PatchSpec(BaseModel):
    """Specification for a single patch operation."""

    model_config = ConfigDict(extra="forbid")

    primitive: PatchPrimitive
    frontmatter: Optional[List[FrontmatterPatch]] = None
    heading: Optional[HeadingPatch] = None
    wikilinks: Optional[List[str]] = None


class Operation(BaseModel):
    """A single vault operation."""

    model_config = ConfigDict(extra="forbid")

    op: OperationType
    path: str  # Relative to vault root
    template: Optional[str] = None  # For create ops
    context: Optional[Dict] = None  # Template variables
    patches: Optional[List[PatchSpec]] = None  # For patch ops
    links: Optional[List[str]] = None  # For link ops


class ChangePlan(BaseModel):
    """Complete plan for vault modifications. NO archive ops - those are deterministic."""

    model_config = ConfigDict(extra="forbid")

    version: Literal["1.0"] = "1.0"
    source_file: str
    extraction_file: str
    created_at: datetime
    operations: List[Operation] = Field(default_factory=list)
    warnings: List[str] = Field(default_factory=list)
