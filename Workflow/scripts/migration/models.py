"""Pydantic models for migration operations."""

from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from enum import Enum


class IssueType(str, Enum):
    """Types of issues detected during scan."""
    
    MISSING_README = "missing_readme"
    BAD_FRONTMATTER = "bad_frontmatter"
    WRONG_TYPE = "wrong_type"
    MISSING_KEY = "missing_key"
    BAD_FILENAME = "bad_filename"
    PLACEHOLDER = "placeholder"
    NO_FRONTMATTER = "no_frontmatter"


class IssueSeverity(str, Enum):
    """Severity levels for issues."""
    
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


class Issue(BaseModel):
    """A detected issue with an entity or note."""
    
    model_config = ConfigDict(extra="forbid")
    
    type: IssueType
    file: str | None = None
    details: str | None = None
    severity: IssueSeverity = IssueSeverity.WARNING


class NoteInfo(BaseModel):
    """Information about a note file within an entity folder."""
    
    model_config = ConfigDict(extra="forbid")
    
    path: str  # Relative to vault root
    filename: str
    has_frontmatter: bool = False
    frontmatter: dict | None = None
    current_type: str | None = None
    inferred_date: str | None = None  # YYYY-MM-DD from filename
    issues: list[Issue] = Field(default_factory=list)


class EntityFolder(BaseModel):
    """Information about an entity folder."""
    
    model_config = ConfigDict(extra="forbid")
    
    path: str  # Relative to vault root (e.g., "VAST/People/Jeff Denworth")
    entity_type: str  # people, customer, projects, rob, partners
    entity_name: str  # e.g., "Jeff Denworth"
    has_readme: bool = False
    readme_issues: list[Issue] = Field(default_factory=list)
    notes: list[NoteInfo] = Field(default_factory=list)
    note_count: int = 0
    last_contact: str | None = None  # YYYY-MM-DD from most recent note


class ScanStatistics(BaseModel):
    """Statistics from a vault scan."""
    
    model_config = ConfigDict(extra="forbid")
    
    total_entities: int = 0
    entities_with_readme: int = 0
    entities_missing_readme: int = 0
    total_notes: int = 0
    notes_with_frontmatter: int = 0
    notes_missing_frontmatter: int = 0
    total_issues: int = 0
    issues_by_type: dict[str, int] = Field(default_factory=dict)


class Manifest(BaseModel):
    """Output of migration scan - full vault inventory."""
    
    model_config = ConfigDict(extra="forbid")
    
    version: str = "1.0"
    scan_date: datetime = Field(default_factory=datetime.now)
    scope: str = "all"
    vault_root: str = ""
    statistics: ScanStatistics = Field(default_factory=ScanStatistics)
    entities: list[EntityFolder] = Field(default_factory=list)


# Migration-specific operation types (extends main ChangePlan ops)
class MigrationOpType(str, Enum):
    """Operation types specific to migration."""
    
    CREATE_README = "create_readme"
    FIX_FRONTMATTER = "fix_frontmatter"
    FIX_TYPE = "fix_type"
    RENAME_FILE = "rename_file"
    ADD_MISSING_KEY = "add_missing_key"


class MigrationOperation(BaseModel):
    """A single migration operation."""
    
    model_config = ConfigDict(extra="forbid")
    
    op: MigrationOpType
    path: str  # Target file (relative to vault root)
    new_path: str | None = None  # For rename operations
    template: str | None = None  # For create operations
    context: dict | None = None  # Template variables
    patches: list[dict] | None = None  # Frontmatter patches


class MigrationPlan(BaseModel):
    """Plan for migrating vault content."""
    
    model_config = ConfigDict(extra="forbid")
    
    version: str = "1.0"
    source_manifest: str = ""
    scope: str = "all"
    created_at: datetime = Field(default_factory=datetime.now)
    operations: list[MigrationOperation] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)
    statistics: dict = Field(default_factory=dict)


class VerificationResult(BaseModel):
    """Result of compliance verification."""
    
    model_config = ConfigDict(extra="forbid")
    
    scope: str
    verified_at: datetime = Field(default_factory=datetime.now)
    total_entities: int = 0
    compliant_entities: int = 0
    non_compliant_entities: int = 0
    remaining_issues: list[str] = Field(default_factory=list)
    compliance_percentage: float = 0.0
