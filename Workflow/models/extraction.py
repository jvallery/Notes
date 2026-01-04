"""Pydantic models for extraction phase output."""

from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Literal, Optional


class TaskItem(BaseModel):
    """A single extracted task/action item."""

    model_config = ConfigDict(extra="forbid")

    text: str = Field(description="The action item text")
    owner: str | None = Field(default=None, description="Person responsible, use 'Myself' for first-person")
    due: str | None = Field(default=None, description="Due date in YYYY-MM-DD format")
    priority: Literal["highest", "high", "medium", "low", "lowest"] = Field(
        default="medium",
        description="Task priority level"
    )
    # Optional cross-references for task context
    related_person: str | None = Field(default=None, description="Person this task is about")
    related_project: str | None = Field(default=None, description="Project this task belongs to")
    related_account: str | None = Field(default=None, description="Account this task is for")
    confidence: float = Field(default=1.0, ge=0.0, le=1.0, description="Confidence in this task extraction")


class Mentions(BaseModel):
    """Entities mentioned in the content."""
    
    model_config = ConfigDict(extra="forbid")
    
    people: list[str] = Field(default_factory=list, description="Names of people mentioned")
    projects: list[str] = Field(default_factory=list, description="Projects referenced")
    accounts: list[str] = Field(default_factory=list, description="Companies/accounts referenced")


# NOTE: The following classes have been removed due to OpenAI Structured Outputs
# incompatibility with dict[str, Model] types which causes "Extra required key" errors:
# - PersonDetails, ProjectDetails, AccountDetails, CrossLinks
# These can be re-added in a future version using a list-based approach instead of dict.


class ExtractionV1(BaseModel):
    """
    Schema for extracted meeting/email content. Version 1.0.
    
    Used with OpenAI Structured Outputs to guarantee schema adherence.
    """

    model_config = ConfigDict(extra="forbid")

    # Metadata (set by system, not LLM)
    version: Literal["1.0"] = Field(default="1.0", description="Schema version")
    source_file: str = Field(default="", description="Path to source file (set by system)")
    processed_at: datetime = Field(
        default_factory=datetime.now,
        description="Processing timestamp (set by system)"
    )
    
    # Classification
    note_type: Literal[
        "customer", "people", "projects", "rob", "journal", "partners", "travel"
    ] = Field(description="Type of note this content represents")
    entity_name: str | None = Field(
        default=None,
        description="Primary entity (person name, account name, project name)"
    )
    
    # Core content
    title: str = Field(description="Brief descriptive title (3-7 words)")
    date: str = Field(description="Date of the meeting/email in YYYY-MM-DD format")
    participants: list[str] = Field(
        default_factory=list,
        description="List of participant names"
    )
    summary: str = Field(description="2-3 sentence summary of key points")
    
    # Extracted items
    tasks: list[TaskItem] = Field(default_factory=list, description="Action items extracted")
    decisions: list[str] = Field(default_factory=list, description="Decisions made")
    facts: list[str] = Field(default_factory=list, description="Key facts to remember")
    topics: list[str] = Field(default_factory=list, description="Topics discussed")
    mentions: Mentions = Field(
        default_factory=Mentions,
        description="Entities mentioned in content"
    )
    
    # NOTE: Rich entity details (person_details, project_details, account_details, cross_links)
    # have been removed due to OpenAI Structured Outputs incompatibility with dict[str, Model] types.
    # These can be re-added in a future version using a different schema approach.
    
    # Confidence and warnings
    confidence: float = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
        description="Overall confidence in extraction (0.0-1.0)"
    )
    warnings: list[str] = Field(
        default_factory=list,
        description="Any concerns or ambiguities to flag for review"
    )
