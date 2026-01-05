"""
Email Adapter - Parse exported emails into ContentEnvelope.

Handles emails exported from Apple Mail (markdown format).
"""

import re
from datetime import datetime
from pathlib import Path
from typing import Optional

from .base import BaseAdapter
from ..envelope import ContentEnvelope, ContentType, EmailMetadata


class EmailAdapter(BaseAdapter):
    """Parse emails exported from Apple Mail."""
    
    @property
    def content_type(self) -> ContentType:
        return ContentType.EMAIL
    
    def can_handle(self, path: Path) -> bool:
        """Detect if this is an email file.
        
        Email files are:
        - In Inbox/Email/ directory
        - Named with pattern: YYYY-MM-DD_HHMMSS_NNNN_Subject.md
        """
        if not path.is_file() or path.suffix != ".md":
            return False
        
        # Check path
        if "Email" in path.parts:
            return True
        
        # Check filename pattern
        if re.match(r"^\d{4}-\d{2}-\d{2}_\d{6}_\d{4}_", path.name):
            return True
        
        return False
    
    def parse(self, path: Path) -> ContentEnvelope:
        """Parse email file into ContentEnvelope."""
        content = path.read_text()
        
        # Extract metadata
        date = self._extract_date(content, path.name)
        subject = self._extract_subject(content)
        sender_name, sender_email = self._extract_sender(content)
        recipients_detail = self._extract_recipients(content)
        recipient_names = [r.get("name") for r in recipients_detail if r.get("name")]
        recipient_emails = [r.get("email") for r in recipients_detail if r.get("email")]
        is_reply = self._is_reply(subject)
        
        # Build participants list
        participants = []
        if sender_name:
            participants.append(sender_name)
        participants.extend(recipient_names)
        
        return ContentEnvelope(
            source_path=path,
            content_type=ContentType.EMAIL,
            raw_content=content,
            date=date,
            title=subject,
            participants=participants,
            content_hash=self.compute_hash(content),
            metadata={
                "email": EmailMetadata(
                    sender_name=sender_name,
                    sender_email=sender_email,
                    recipients=recipient_names,
                    recipients_emails=recipient_emails,
                    recipients_detail=recipients_detail,
                    subject=subject,
                    is_reply=is_reply,
                ).model_dump()
            }
        )
    
    def _extract_date(self, content: str, filename: str) -> str:
        """Extract date from email content or filename."""
        # Try content (## YYYY-MM-DD format)
        date_match = re.search(r"##\s*(\d{4}-\d{2}-\d{2})", content)
        if date_match:
            return date_match.group(1)
        
        # Try filename (YYYY-MM-DD_HHMMSS_...)
        filename_match = re.match(r"^(\d{4}-\d{2}-\d{2})", filename)
        if filename_match:
            return filename_match.group(1)
        
        return datetime.now().strftime("%Y-%m-%d")
    
    def _extract_subject(self, content: str) -> str:
        """Extract subject from email content."""
        lines = content.split("\n")
        if lines and lines[0].startswith("# "):
            return lines[0][2:].strip()
        return "Unknown Subject"
    
    def _extract_sender(self, content: str) -> tuple[Optional[str], Optional[str]]:
        """Extract sender name and email from email content."""
        # Look for "From:" line
        from_match = re.search(r"(?:^|\n)\*?\*?From\*?\*?:\s*([^\n<]+?)(?:\s*<([^>]+)>)?(?:\n|$)", content)
        if from_match:
            name = from_match.group(1).strip()
            # Strip markdown bold markers
            name = re.sub(r'^\*\*\s*|\s*\*\*$', '', name)
            email = from_match.group(2) if from_match.group(2) else None
            return (name, email)
        return (None, None)
    
    def _extract_recipients(self, content: str) -> list[dict]:
        """Extract recipient names + emails from email content."""
        recipients: list[dict] = []
        
        # Look for "To:" line
        to_match = re.search(r"(?:^|\n)\*?\*?To\*?\*?:\s*([^\n]+)", content)
        if to_match:
            to_line = to_match.group(1)
            # Parse comma-separated names
            for part in to_line.split(","):
                name = None
                email = None
                name_match = re.match(r"([^<]+?)(?:\s*<([^>]+)>)?$", part.strip())
                if name_match:
                    name = name_match.group(1).strip()
                    email = name_match.group(2).strip() if name_match.group(2) else None
                    # Strip markdown bold markers
                    name = re.sub(r'^\*\*\s*|\s*\*\*$', '', name)
                if name or email:
                    recipients.append({"name": name, "email": email})
        
        return recipients
    
    def _is_reply(self, subject: str) -> bool:
        """Check if this is a reply email."""
        return subject.lower().startswith(("re:", "re[", "fwd:", "fw:"))
