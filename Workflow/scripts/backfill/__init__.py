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


class BackfillExtraction(BaseModel):
    """Lightweight extraction result for a single note."""
    
    model_config = ConfigDict(extra="forbid")
    
    # Source info
    note_path: str  # Relative to vault root
    entity_path: str  # Parent entity folder
    
    # Extracted metadata
    date: str  # YYYY-MM-DD
    title: str
    summary: str  # 1-2 sentences
    mentions: Mentions = Field(default_factory=Mentions)
    key_facts: list[str] = Field(default_factory=list)
    has_tasks: bool = False
    
    # Processing metadata
    extracted_at: datetime = Field(default_factory=datetime.now)
    model_used: str = "gpt-4o-mini"
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


class ReadmeUpdate(BaseModel):
    """Planned update for a single README.md."""
    
    model_config = ConfigDict(extra="forbid")
    
    entity_path: str  # e.g., "VAST/People/Jeff Denworth"
    readme_path: str  # e.g., "VAST/People/Jeff Denworth/README.md"
    last_contact: str | None = None  # Most recent date
    context_entries: list[ContextEntry] = Field(default_factory=list)
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
