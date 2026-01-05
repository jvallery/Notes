"""
Unified Extraction Model - Single schema for all content types.

This replaces the separate ExtractionV1 (transcripts) and EmailExtraction (emails)
with a unified model that works for all content types.
"""

from datetime import datetime
from typing import Optional, Literal, Any
from pydantic import BaseModel, Field, ConfigDict


class EntityRef(BaseModel):
    """Reference to an entity (person, company, or project)."""
    
    model_config = ConfigDict(extra="ignore")
    
    entity_type: Literal["person", "company", "project"]
    name: str
    confidence: float = 0.8


class ContactInfo(BaseModel):
    """Contact information for a person."""
    
    model_config = ConfigDict(extra="ignore")
    
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    title: Optional[str] = None
    company: Optional[str] = None
    linkedin: Optional[str] = None


class Fact(BaseModel):
    """A key fact discovered in the content.
    
    Facts are attached to the entity they're ABOUT (not just mentioned).
    """
    
    model_config = ConfigDict(extra="ignore")
    
    text: str
    about_entity: Optional[EntityRef] = None  # Who/what is this fact about?
    fact_type: str = "general"  # preference, background, technical, relationship, etc.
    confidence: float = 0.8


class TaskItem(BaseModel):
    """A task or action item extracted from content."""
    
    model_config = ConfigDict(extra="ignore")
    
    text: str
    owner: Optional[str] = None  # "Myself" for first-person, else person's name
    due: Optional[str] = None  # YYYY-MM-DD
    priority: str = "medium"  # highest, high, medium, low, lowest
    
    # Related entities
    related_person: Optional[str] = None
    related_project: Optional[str] = None
    related_customer: Optional[str] = None


class MentionedEntity(BaseModel):
    """An entity mentioned in the content with associated facts.
    
    This enables smart patching: we patch entities when we learn facts ABOUT them,
    not just because they're mentioned.
    """
    
    model_config = ConfigDict(extra="ignore")
    
    entity_type: Literal["person", "company", "project"]
    name: str
    role: Optional[str] = None  # How they relate to the content (e.g., "discussed", "action owner")
    facts_about: list[str] = Field(default_factory=list)  # Facts discovered about this entity
    confidence: float = 0.8


class DiscoveredAlias(BaseModel):
    """An alias discovered for a person (to update People manifest).
    
    Example: "LG" is an alias for "Lior Genzel" 
    """
    
    model_config = ConfigDict(extra="ignore")
    
    alias: str  # The short name/nickname/initials (e.g., "LG")
    canonical_name: str  # The full name (e.g., "Lior Genzel")
    confidence: float = 0.8


class DiscoveredAcronym(BaseModel):
    """An acronym discovered for a project/term (to update Projects manifest).
    
    Example: "DASE" = "Data Application Storage Engine"
    """
    
    model_config = ConfigDict(extra="ignore")
    
    acronym: str  # The acronym (e.g., "DASE")
    expansion: str  # The expanded form (e.g., "Data Application Storage Engine")
    project_name: Optional[str] = None  # If this is a project acronym, which project?
    confidence: float = 0.8


class CalendarSuggestion(BaseModel):
    """Suggested calendar invite from content."""
    
    model_config = ConfigDict(extra="ignore")
    
    title: str
    proposed_date: Optional[str] = None  # YYYY-MM-DD
    proposed_time: Optional[str] = None  # HH:MM
    duration_minutes: int = 30
    attendees: list[str] = Field(default_factory=list)
    description: Optional[str] = None


class ReminderSuggestion(BaseModel):
    """Suggested follow-up reminder."""
    
    model_config = ConfigDict(extra="ignore")
    
    text: str
    remind_date: str  # YYYY-MM-DD
    related_entity: Optional[str] = None


class SuggestedOutputs(BaseModel):
    """AI-suggested outputs based on content analysis."""
    
    model_config = ConfigDict(extra="ignore")
    
    needs_reply: bool = False
    reply_urgency: str = "normal"  # urgent, normal, low
    reply_context: Optional[str] = None  # Key points to address
    
    calendar_invite: Optional[CalendarSuggestion] = None
    follow_up_reminder: Optional[ReminderSuggestion] = None


class UnifiedExtraction(BaseModel):
    """Unified extraction schema for all content types.
    
    This single schema works for emails, transcripts, documents, etc.
    """
    
    model_config = ConfigDict(extra="ignore")
    
    # Version and source
    version: str = "2.0"
    source_file: str
    content_type: str  # email, transcript, document, voice
    processed_at: datetime
    
    # Classification
    note_type: Literal["customer", "people", "projects", "rob", "journal", "partners", "travel"]
    primary_entity: Optional[EntityRef] = None  # Main subject of the content
    
    # Basic metadata
    date: str  # YYYY-MM-DD
    title: str
    summary: str
    
    # Participants/contacts
    participants: list[str] = Field(default_factory=list)
    contacts: list[ContactInfo] = Field(default_factory=list)  # Detailed contact info
    
    # Extracted knowledge
    facts: list[Fact] = Field(default_factory=list)
    decisions: list[str] = Field(default_factory=list)
    topics: list[str] = Field(default_factory=list)
    
    # Actionable items
    tasks: list[TaskItem] = Field(default_factory=list)
    questions: list[str] = Field(default_factory=list)  # Questions that need answers
    commitments: list[str] = Field(default_factory=list)  # Commitments made by anyone
    
    # Entity mentions with facts (enables smart patching)
    mentioned_entities: list[MentionedEntity] = Field(default_factory=list)
    
    # Discovered aliases and acronyms (for manifest updates)
    discovered_aliases: list[DiscoveredAlias] = Field(default_factory=list)
    discovered_acronyms: list[DiscoveredAcronym] = Field(default_factory=list)
    
    # Legacy compatibility (will be removed)
    mentions: dict[str, list[str]] = Field(
        default_factory=lambda: {"people": [], "projects": [], "accounts": []}
    )
    
    # Email-specific
    email_requires_response: bool = False
    email_urgency: str = "medium"
    email_type: str = "other"
    
    # Suggested outputs
    suggested_outputs: SuggestedOutputs = Field(default_factory=SuggestedOutputs)
    
    # Confidence
    confidence: float = 0.8
    
    def get_entities_with_facts(self) -> list[MentionedEntity]:
        """Get entities that have facts associated with them.
        
        These are the entities we should patch (we learned something about them).
        """
        return [e for e in self.mentioned_entities if e.facts_about]
    
    def get_all_mentioned_people(self) -> list[str]:
        """Get all mentioned people names (for context patches)."""
        people = set(self.participants)
        
        # From contacts
        for contact in self.contacts:
            if contact.name:
                people.add(contact.name)
        
        # From mentioned entities
        for entity in self.mentioned_entities:
            if entity.entity_type == "person":
                people.add(entity.name)
        
        # Legacy format
        people.update(self.mentions.get("people", []))
        
        return list(people)
    
    def get_all_mentioned_companies(self) -> list[str]:
        """Get all mentioned company names."""
        companies = set()
        
        # From contacts
        for contact in self.contacts:
            if contact.company:
                companies.add(contact.company)
        
        # From mentioned entities
        for entity in self.mentioned_entities:
            if entity.entity_type == "company":
                companies.add(entity.name)
        
        # Legacy format
        companies.update(self.mentions.get("accounts", []))
        
        return list(companies)
    
    def get_all_mentioned_projects(self) -> list[str]:
        """Get all mentioned project names."""
        projects = set()
        
        # From mentioned entities
        for entity in self.mentioned_entities:
            if entity.entity_type == "project":
                projects.add(entity.name)
        
        # Legacy format
        projects.update(self.mentions.get("projects", []))
        
        return list(projects)
