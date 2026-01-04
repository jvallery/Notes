"""
Backfill Models: Pydantic schemas for historical content processing.

These models define the data structures for:
- Scanning existing notes in entity folders
- Extracting lightweight metadata from notes
- Aggregating context for README updates
- Planning and executing patches
"""

from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


# ─────────────────────────────────────────────────────────────────────────────
# Scan Phase Models
# ─────────────────────────────────────────────────────────────────────────────


class NoteMetadata(BaseModel):
    """Metadata about a note file (before extraction)."""
    
    model_config = ConfigDict(extra="forbid")
    
    path: str  # Relative to vault root
    filename: str
    date: str | None = None  # YYYY-MM-DD from frontmatter or filename
    title: str | None = None  # From frontmatter or H1
    has_frontmatter: bool = False
    frontmatter_type: str | None = None  # type: field value


class EntityInfo(BaseModel):
    """Information about an entity folder."""
    
    model_config = ConfigDict(extra="forbid")
    
    path: str  # e.g., "VAST/People/Jeff Denworth"
    entity_type: str  # people, accounts, projects, rob
    entity_name: str  # e.g., "Jeff Denworth"
    readme_exists: bool
    readme_path: str | None = None
    notes: list[NoteMetadata] = Field(default_factory=list)
    note_count: int = 0


class BackfillManifest(BaseModel):
    """Output of the scan phase."""
    
    model_config = ConfigDict(extra="forbid")
    
    version: str = "1.0"
    scanned_at: datetime
    scope: str  # e.g., "VAST" or "VAST/People"
    entities: list[EntityInfo] = Field(default_factory=list)
    total_entities: int = 0
    total_notes: int = 0
    notes_with_dates: int = 0
    notes_without_dates: int = 0


# ─────────────────────────────────────────────────────────────────────────────
# Extract Phase Models
# ─────────────────────────────────────────────────────────────────────────────


class Mentions(BaseModel):
    """Entities mentioned in a note."""
    
    model_config = ConfigDict(extra="forbid")
    
    people: list[str] = Field(default_factory=list)
    projects: list[str] = Field(default_factory=list)
    accounts: list[str] = Field(default_factory=list)


class PersonDetails(BaseModel):
    """Rich details about a person extracted from notes."""
    
    model_config = ConfigDict(extra="ignore")  # Allow extra fields for flexibility
    
    role: str | None = None
    company: str | None = None
    department: str | None = None
    email: str | None = None
    phone: str | None = None
    linkedin: str | None = None
    location: str | None = None
    background: str | None = None
    relationship: str | None = None
    projects: list[str] = Field(default_factory=list)  # Projects this person works on


class ProjectDetails(BaseModel):
    """Details about a project extracted from notes."""
    
    model_config = ConfigDict(extra="ignore")
    
    status: str | None = None  # active, blocked, on-hold, complete, proposed
    description: str | None = None
    owner: str | None = None
    blockers: list[str] = Field(default_factory=list)
    next_steps: list[str] = Field(default_factory=list)
    collaborators: list[str] = Field(default_factory=list)
    related_customers: list[str] = Field(default_factory=list)


class CustomerDetails(BaseModel):
    """Details about a customer/account extracted from notes."""
    
    model_config = ConfigDict(extra="ignore")
    
    industry: str | None = None
    relationship: str | None = None  # Prospect, Active, Partner, At Risk
    key_contacts: list[str] = Field(default_factory=list)
    opportunities: list[str] = Field(default_factory=list)
    blockers: list[str] = Field(default_factory=list)


class ExtractedTask(BaseModel):
    """A task extracted from a note."""
    
    model_config = ConfigDict(extra="ignore")
    
    text: str
    owner: str | None = None
    due: str | None = None
    related_person: str | None = None
    related_project: str | None = None
    related_customer: str | None = None
    priority: str | None = None  # high, medium, low
    status: str = "open"


class CrossLinks(BaseModel):
    """Cross-references between entities."""
    
    model_config = ConfigDict(extra="ignore")
    
    person_to_project: dict[str, list[str]] = Field(default_factory=dict)
    person_to_customer: dict[str, list[str]] = Field(default_factory=dict)
    project_to_customer: dict[str, list[str]] = Field(default_factory=dict)


class BackfillExtractionLite(BaseModel):
    """
    Lightweight extraction model for OpenAI structured outputs.
    
    This minimal schema is what the LLM returns. It gets transformed
    into the full BackfillExtraction with metadata by the extractor.
    Designed to minimize token usage while capturing essential data.
    """
    
    model_config = ConfigDict(extra="forbid")
    
    summary: str = Field(description="1-2 sentence summary of the note content")
    suggested_title: str | None = Field(
        default=None, 
        description="Better title for the note if current is generic like 'New Recording'"
    )
    note_type: str | None = Field(
        default=None,
        description="Type: meeting, 1-1, project, email, call, etc."
    )
    mentions: Mentions = Field(default_factory=Mentions)
    key_facts: list[str] = Field(
        default_factory=list,
        description="Key facts, decisions, or insights from the note"
    )
    topics_discussed: list[str] = Field(
        default_factory=list,
        description="Main topics covered in the note"
    )
    tasks: list[ExtractedTask] = Field(
        default_factory=list,
        description="Action items extracted from the note"
    )
    decisions: list[str] = Field(
        default_factory=list,
        description="Decisions made in the note"
    )


class BackfillExtraction(BaseModel):
    """Rich extraction result for a single note."""
    
    model_config = ConfigDict(extra="ignore")  # Allow extra fields
    
    # Source info
    note_path: str  # Relative to vault root
    entity_path: str  # Parent entity folder
    
    # Extracted metadata
    date: str  # YYYY-MM-DD
    title: str
    suggested_title: str | None = None  # AI-suggested title for renaming
    note_type: str | None = None  # meeting, 1-1, project, email, etc.
    summary: str  # 1-2 sentences
    mentions: Mentions = Field(default_factory=Mentions)
    key_facts: list[str] = Field(default_factory=list)
    
    # Rich entity data
    person_details: dict[str, PersonDetails] = Field(default_factory=dict)
    project_details: dict[str, ProjectDetails] = Field(default_factory=dict)
    customer_details: dict[str, CustomerDetails] = Field(default_factory=dict)
    
    # Tasks and decisions
    tasks: list[ExtractedTask] = Field(default_factory=list)
    decisions: list[str] = Field(default_factory=list)
    topics_discussed: list[str] = Field(default_factory=list)
    
    # Cross-links for wikilink generation
    cross_links: CrossLinks = Field(default_factory=CrossLinks)
    
    # Legacy field (kept for compatibility)
    has_tasks: bool = False
    
    # Processing metadata
    extracted_at: datetime = Field(default_factory=datetime.now)
    model_used: str = "gpt-5.2"
    tokens_used: int = 0


class ExtractionBatch(BaseModel):
    """Collection of extractions from a batch run."""
    
    model_config = ConfigDict(extra="forbid")
    
    version: str = "1.0"
    extracted_at: datetime
    scope: str
    extractions: list[BackfillExtraction] = Field(default_factory=list)
    total_notes: int = 0
    successful: int = 0
    failed: int = 0
    skipped: int = 0
    total_tokens: int = 0


# ─────────────────────────────────────────────────────────────────────────────
# Aggregate Phase Models
# ─────────────────────────────────────────────────────────────────────────────


class ContextEntry(BaseModel):
    """A single entry for the Recent Context section."""
    
    model_config = ConfigDict(extra="forbid")
    
    date: str  # YYYY-MM-DD
    title: str  # Note title
    note_path: str  # For wikilink
    summary: str  # Brief summary
    via_entity: str | None = None  # If cross-referenced from another entity


class AggregatedPersonDetails(BaseModel):
    """Merged person details from all extractions."""
    
    model_config = ConfigDict(extra="ignore")
    
    role: str | None = None
    company: str | None = None
    department: str | None = None
    email: str | None = None
    phone: str | None = None
    linkedin: str | None = None
    location: str | None = None
    background: list[str] = Field(default_factory=list)  # Multiple snippets
    relationship: str | None = None
    projects: list[str] = Field(default_factory=list)  # Projects this person works on
    related_customers: list[str] = Field(default_factory=list)  # Customers they're associated with
    related_people: list[str] = Field(default_factory=list)  # Other people they work with


class AggregatedProjectDetails(BaseModel):
    """Merged project details from all extractions."""
    
    model_config = ConfigDict(extra="ignore")
    
    status: str | None = None
    description: str | None = None
    owner: str | None = None
    blockers: list[str] = Field(default_factory=list)
    next_steps: list[str] = Field(default_factory=list)
    collaborators: list[str] = Field(default_factory=list)
    related_customers: list[str] = Field(default_factory=list)
    decisions: list[str] = Field(default_factory=list)


class AggregatedCustomerDetails(BaseModel):
    """Merged customer details from all extractions."""
    
    model_config = ConfigDict(extra="ignore")
    
    industry: str | None = None
    status: str | None = None  # relationship status
    key_contacts: list[str] = Field(default_factory=list)
    opportunities: list[str] = Field(default_factory=list)
    blockers: list[str] = Field(default_factory=list)
    active_projects: list[str] = Field(default_factory=list)
    related_people: list[str] = Field(default_factory=list)


class Collaborator(BaseModel):
    """A person who collaborates on a project or account."""
    
    model_config = ConfigDict(extra="ignore")
    
    name: str
    role: str | None = None
    company: str | None = None


class ReadmeUpdate(BaseModel):
    """Planned update for a single README.md."""
    
    model_config = ConfigDict(extra="ignore")  # Changed to allow extra fields
    
    entity_path: str  # e.g., "VAST/People/Jeff Denworth"
    readme_path: str  # e.g., "VAST/People/Jeff Denworth/README.md"
    entity_type: str = "people"  # people, accounts, projects
    last_contact: str | None = None  # Most recent date
    
    # Rich profile data (type-specific)
    profile: AggregatedPersonDetails | None = None  # For people
    project_profile: AggregatedProjectDetails | None = None  # For projects
    customer_profile: AggregatedCustomerDetails | None = None  # For customers
    
    # Collaborators (for projects and customers)
    collaborators: list[Collaborator] = Field(default_factory=list)
    
    # Cross-linked entities
    linked_projects: list[str] = Field(default_factory=list)
    linked_customers: list[str] = Field(default_factory=list)
    linked_people: list[str] = Field(default_factory=list)
    
    # Context and tasks
    context_entries: list[ContextEntry] = Field(default_factory=list)
    open_tasks: list[ExtractedTask] = Field(default_factory=list)
    key_facts: list[str] = Field(default_factory=list)
    topics: list[str] = Field(default_factory=list)
    decisions: list[str] = Field(default_factory=list)
    
    interaction_count: int = 0


class BackfillPlan(BaseModel):
    """Complete plan for all README updates."""
    
    model_config = ConfigDict(extra="forbid")
    
    version: str = "1.0"
    created_at: datetime
    scope: str
    updates: list[ReadmeUpdate] = Field(default_factory=list)
    total_entities: int = 0
    entities_with_updates: int = 0
    total_context_entries: int = 0


# ─────────────────────────────────────────────────────────────────────────────
# Apply Phase Models
# ─────────────────────────────────────────────────────────────────────────────


class ApplyResult(BaseModel):
    """Result of applying the backfill plan."""
    
    model_config = ConfigDict(extra="forbid")
    
    success: bool
    applied_at: datetime
    readmes_updated: int = 0
    readmes_skipped: int = 0
    errors: list[str] = Field(default_factory=list)
    git_commit: str | None = None
    dry_run: bool = False
