"""Pydantic models for extraction phase output."""

from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Literal, Optional, List, Dict


class TaskItem(BaseModel):
    """A single extracted task/action item."""

    model_config = ConfigDict(extra="forbid")

    text: str
    owner: Optional[str] = None  # "Myself" for first-person
    due: Optional[str] = None  # YYYY-MM-DD
    priority: Literal["highest", "high", "medium", "low", "lowest"] = "medium"


class ExtractionV1(BaseModel):
    """Schema for extracted meeting/email content. Version 1.0."""

    model_config = ConfigDict(extra="forbid")

    version: Literal["1.0"] = "1.0"
    source_file: str
    processed_at: datetime
    note_type: Literal[
        "customer", "people", "projects", "rob", "journal", "partners", "travel"
    ]
    entity_name: Optional[str] = None  # Matched or inferred entity
    title: str
    date: str  # YYYY-MM-DD (meeting/email date)
    participants: List[str] = Field(default_factory=list)
    summary: str
    tasks: List[TaskItem] = Field(default_factory=list)
    decisions: List[str] = Field(default_factory=list)
    facts: List[str] = Field(default_factory=list)
    mentions: Dict[str, List[str]] = Field(
        default_factory=lambda: {"people": [], "projects": [], "accounts": []}
    )
    confidence: float = Field(default=1.0, ge=0.0, le=1.0)
