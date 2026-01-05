"""Pydantic models for email extraction and vault patching."""

from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Literal, Optional, List


class ContactInfo(BaseModel):
    """Contact information extracted from an email."""
    
    model_config = ConfigDict(extra="ignore")  # Allow extra fields from LLM
    
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    title: Optional[str] = None
    company: Optional[str] = None
    linkedin: Optional[str] = None


class TaskItem(BaseModel):
    """A task or action item extracted from email."""
    
    model_config = ConfigDict(extra="ignore")  # Allow extra fields from LLM
    
    text: str
    owner: Optional[str] = None  # "Myself" for first-person
    due: Optional[str] = None  # YYYY-MM-DD
    priority: str = "medium"  # highest, high, medium, low, lowest
    related_person: Optional[str] = None  # Person this task relates to
    related_project: Optional[str] = None  # Project this task relates to


class KeyFact(BaseModel):
    """A key fact or piece of information about a person/company."""
    
    model_config = ConfigDict(extra="ignore")  # Allow extra fields from LLM
    
    fact: str
    about: str  # Who/what this fact is about (person name or company)
    fact_type: str = "general"  # preference, background, relationship, project, general, etc.


class EmailExtraction(BaseModel):
    """Structured extraction from an email for vault updates."""
    
    model_config = ConfigDict(extra="ignore")  # Allow extra fields from LLM
    
    # Source metadata
    source_file: str
    processed_at: datetime
    email_date: str  # YYYY-MM-DD
    subject: str
    
    # Sender info (always extract)
    sender: ContactInfo
    
    # Other contacts mentioned
    contacts_mentioned: List[ContactInfo] = Field(default_factory=list)
    
    # Content extraction
    summary: str  # 1-2 sentence summary of the email
    topics: List[str] = Field(default_factory=list)  # Main topics discussed
    
    # Actionable items
    tasks: List[TaskItem] = Field(default_factory=list)
    questions: List[str] = Field(default_factory=list)  # Questions asked
    decisions: List[str] = Field(default_factory=list)  # Decisions made
    commitments: List[str] = Field(default_factory=list)  # Commitments made by anyone
    
    # Knowledge extraction
    key_facts: List[KeyFact] = Field(default_factory=list)
    
    # Entity mentions for cross-linking
    people_mentioned: List[str] = Field(default_factory=list)
    companies_mentioned: List[str] = Field(default_factory=list)
    projects_mentioned: List[str] = Field(default_factory=list)
    
    # Classification (flexible strings to handle LLM variation)
    requires_response: bool = False
    urgency: str = "medium"  # low, medium, high, critical
    email_type: str = "other"  # request, information, follow_up, introduction, scheduling, etc.


class VaultPatch(BaseModel):
    """A single patch operation to apply to the vault."""
    
    model_config = ConfigDict(extra="forbid")
    
    # Target
    target_path: str  # Relative path in vault (e.g., "VAST/People/John Smith/README.md")
    target_entity: str  # Entity name for logging
    
    # Operation type
    operation: Literal["upsert_frontmatter", "append_under_heading", "add_task", "ensure_wikilinks"]
    
    # Operation-specific data
    frontmatter: Optional[dict] = None  # For upsert_frontmatter
    heading: Optional[str] = None  # For append_under_heading
    content: Optional[str] = None  # For append_under_heading
    task: Optional[TaskItem] = None  # For add_task
    wikilinks: Optional[List[str]] = None  # For ensure_wikilinks


class EmailChangePlan(BaseModel):
    """A set of patches to apply based on email extraction."""
    
    model_config = ConfigDict(extra="forbid")
    
    version: str = "1.0"
    source_file: str
    extraction_file: str
    created_at: datetime
    
    # Patches to apply
    patches: List[VaultPatch] = Field(default_factory=list)
    
    # Entities that should be created (don't exist yet)
    entities_to_create: List[dict] = Field(default_factory=list)
    
    # Warnings
    warnings: List[str] = Field(default_factory=list)
