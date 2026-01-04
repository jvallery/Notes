"""Pydantic models for the ChangePlan phase output."""

from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from enum import Enum
from typing import Literal


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
    value: str | list[str] | None  # None = remove key


class HeadingPatch(BaseModel):
    """Content to append under a specific heading."""

    model_config = ConfigDict(extra="forbid")

    heading: str  # e.g., "## Recent Context"
    content: str  # Content to append


class PatchSpec(BaseModel):
    """Specification for a single patch operation."""

    model_config = ConfigDict(extra="forbid")

    primitive: PatchPrimitive
    frontmatter: list[FrontmatterPatch] | None = None
    heading: HeadingPatch | None = None
    wikilinks: list[str] | None = None


class TaskContext(BaseModel):
    """Task item for template context."""
    
    model_config = ConfigDict(extra="forbid")
    
    text: str = Field(description="The task description")
    owner: str | None = Field(default=None, description="Task owner name or 'Myself'")
    due: str | None = Field(default=None, description="Due date in YYYY-MM-DD format")
    priority: str | None = Field(default=None, description="Priority: highest, high, medium, low, lowest")


class CreateContext(BaseModel):
    """Template context for CREATE operations. Populated from extraction."""
    
    model_config = ConfigDict(extra="forbid")
    
    title: str = Field(description="Note title from extraction")
    date: str = Field(description="Date in YYYY-MM-DD format from extraction")
    summary: str = Field(description="Meeting/content summary from extraction")
    participants: list[str] = Field(default_factory=list, description="List of participant names")
    tasks: list[TaskContext] = Field(default_factory=list, description="Tasks from extraction")
    decisions: list[str] = Field(default_factory=list, description="Decisions from extraction")
    facts: list[str] = Field(default_factory=list, description="Key facts from extraction")
    source: str = Field(default="transcript", description="Source type: transcript or email")
    source_ref: str = Field(default="", description="Path to archived source file")
    # Entity-specific fields (populated based on note_type)
    person: str | None = Field(default=None, description="Person name for people notes")
    account: str | None = Field(default=None, description="Account name for customer notes")
    project: str | None = Field(default=None, description="Project name for project notes")
    rob_forum: str | None = Field(default=None, description="ROB forum name for ROB notes")
    partner: str | None = Field(default=None, description="Partner name for partner notes")
    destination: str | None = Field(default=None, description="Destination for travel notes")


class Operation(BaseModel):
    """A single vault operation."""

    model_config = ConfigDict(extra="forbid")

    op: OperationType
    path: str = Field(description="Relative path from vault root")
    template: str | None = Field(default=None, description="Template name for CREATE ops (e.g., 'people.md.j2')")
    context: CreateContext | None = Field(default=None, description="Template variables for CREATE ops - MUST be populated from extraction")
    patches: list[PatchSpec] | None = Field(default=None, description="Patch specs for PATCH ops")
    links: list[str] | None = Field(default=None, description="Wikilinks for LINK ops (e.g., ['[[Person]]'])")


class ChangePlan(BaseModel):
    """Complete plan for vault modifications. NO archive ops - those are deterministic."""

    model_config = ConfigDict(extra="forbid")

    version: Literal["1.0"] = "1.0"
    source_file: str
    extraction_file: str
    created_at: datetime
    operations: list[Operation] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)
