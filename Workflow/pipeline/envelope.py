"""
Content Envelope - Normalized container for all content types.

Each adapter converts raw content to a ContentEnvelope for unified processing.
"""

from enum import Enum
from datetime import datetime
from pathlib import Path
from typing import Optional, Any
from pydantic import BaseModel, Field, ConfigDict


class ContentType(str, Enum):
    """Supported content types."""
    EMAIL = "email"
    TRANSCRIPT = "transcript"
    DOCUMENT = "document"
    VOICE = "voice"
    SMS = "sms"


class ContentEnvelope(BaseModel):
    """Normalized container for all content types.
    
    Adapters convert raw content (email, transcript, etc.) to this format,
    allowing unified downstream processing.
    """
    
    model_config = ConfigDict(extra="ignore")
    
    # Identity
    source_path: Path
    content_type: ContentType
    
    # Content
    raw_content: str
    
    # Common metadata (extracted by adapter)
    date: str  # YYYY-MM-DD
    title: str
    participants: list[str] = Field(default_factory=list)
    
    # Type-specific metadata
    metadata: dict[str, Any] = Field(default_factory=dict)
    
    # Processing state
    created_at: datetime = Field(default_factory=datetime.now)
    content_hash: Optional[str] = None
    
    def __str__(self) -> str:
        return f"{self.content_type.value}: {self.source_path.name}"


class EmailMetadata(BaseModel):
    """Email-specific metadata."""
    
    sender_name: Optional[str] = None
    sender_email: Optional[str] = None
    recipients: list[str] = Field(default_factory=list)
    recipients_emails: list[str] = Field(default_factory=list)
    recipients_detail: list[dict] = Field(default_factory=list)
    cc: list[str] = Field(default_factory=list)
    subject: str = ""
    thread_id: Optional[str] = None
    in_reply_to: Optional[str] = None
    is_reply: bool = False
    

class TranscriptMetadata(BaseModel):
    """Transcript-specific metadata."""
    
    speakers: list[str] = Field(default_factory=list)
    duration_estimate: Optional[str] = None
    source_app: str = "MacWhisper"
    has_diarization: bool = True
    

class DocumentMetadata(BaseModel):
    """Document-specific metadata."""
    
    document_type: str = "general"  # article, spec, proposal, report, etc.
    author: Optional[str] = None
    source_url: Optional[str] = None
    file_type: str = "markdown"  # pdf, docx, markdown, etc.
