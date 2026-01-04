"""Pydantic models for extraction phase output."""

from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Literal


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


class PersonDetails(BaseModel):
    """Rich profile data for a person mentioned in content."""
    
    model_config = ConfigDict(extra="forbid")
    
    role: str | None = Field(default=None, description="Job title or role")
    company: str | None = Field(default=None, description="Company or organization")
    department: str | None = Field(default=None, description="Team or department")
    email: str | None = Field(default=None, description="Email address")
    phone: str | None = Field(default=None, description="Phone number")
    linkedin: str | None = Field(default=None, description="LinkedIn URL")
    location: str | None = Field(default=None, description="City/region")
    background: str | None = Field(default=None, description="Brief background or expertise")
    relationship: str | None = Field(default=None, description="How I interact with them")
    projects: list[str] = Field(default_factory=list, description="Projects they work on")


class ProjectDetails(BaseModel):
    """Metadata for a project mentioned in content."""
    
    model_config = ConfigDict(extra="forbid")
    
    status: Literal["active", "blocked", "on-hold", "complete", "proposed"] | None = Field(
        default=None, description="Current project state"
    )
    description: str | None = Field(default=None, description="Brief project description")
    owner: str | None = Field(default=None, description="Project owner/lead")
    blockers: list[str] = Field(default_factory=list, description="Current blockers")
    next_steps: list[str] = Field(default_factory=list, description="Immediate actions needed")
    collaborators: list[str] = Field(default_factory=list, description="People working on it")
    related_accounts: list[str] = Field(default_factory=list, description="Customers involved")


class AccountDetails(BaseModel):
    """Metadata for a customer/account mentioned in content."""
    
    model_config = ConfigDict(extra="forbid")
    
    industry: str | None = Field(default=None, description="Industry or sector")
    relationship: Literal["prospect", "active", "partner", "at-risk", "churned"] | None = Field(
        default=None, description="Account status"
    )
    key_contacts: list[str] = Field(default_factory=list, description="People at this account")
    opportunities: list[str] = Field(default_factory=list, description="Active deals or projects")
    blockers: list[str] = Field(default_factory=list, description="Issues or concerns")


class CrossLinks(BaseModel):
    """Relationship mappings between entities."""
    
    model_config = ConfigDict(extra="forbid")
    
    person_to_project: dict[str, list[str]] = Field(
        default_factory=dict, description="Map person names to their projects"
    )
    person_to_account: dict[str, list[str]] = Field(
        default_factory=dict, description="Map person names to their accounts"
    )
    project_to_account: dict[str, list[str]] = Field(
        default_factory=dict, description="Map projects to related accounts"
    )


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
    
    # Entity details (optional rich profiles)
    person_details: dict[str, PersonDetails] = Field(
        default_factory=dict,
        description="Rich profiles for people mentioned (name -> details)"
    )
    project_details: dict[str, ProjectDetails] = Field(
        default_factory=dict,
        description="Metadata for projects mentioned (name -> details)"
    )
    account_details: dict[str, AccountDetails] = Field(
        default_factory=dict,
        description="Metadata for accounts mentioned (name -> details)"
    )
    cross_links: CrossLinks = Field(
        default_factory=CrossLinks,
        description="Relationship mappings between entities"
    )
    
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
