"""
Transcript Adapter - Parse meeting transcripts into ContentEnvelope.

Handles MacWhisper transcripts with speaker diarization.
"""

import re
from datetime import datetime
from pathlib import Path

from .base import BaseAdapter
from ..envelope import ContentEnvelope, ContentType, TranscriptMetadata


class TranscriptAdapter(BaseAdapter):
    """Parse MacWhisper transcripts."""
    
    @property
    def content_type(self) -> ContentType:
        return ContentType.TRANSCRIPT
    
    def can_handle(self, path: Path) -> bool:
        """Detect if this is a transcript file.
        
        Transcript files are:
        - In Inbox/Transcripts/ or Sources/Transcripts/ directory
        - Named with pattern: YYYY-MM-DD HH MM - Title.md
        - Or contain speaker labels (Speaker 1:, [Speaker]:, etc.)
        """
        if not path.is_file() or path.suffix != ".md":
            return False
        
        # Check path
        if "Transcripts" in path.parts:
            return True
        
        # Check filename pattern (date + time)
        if re.match(r"^\d{4}-\d{2}-\d{2}\s+\d{2}[\s:]\d{2}", path.name):
            return True
        
        # Check for speaker labels in content
        try:
            content = path.read_text()[:1000]
            if re.search(r"(?:Speaker \d+:|^\[[^\]]+\]:)", content, re.MULTILINE):
                return True
        except Exception:
            pass
        
        return False
    
    def parse(self, path: Path) -> ContentEnvelope:
        """Parse transcript file into ContentEnvelope."""
        content = path.read_text()
        
        # Extract metadata
        date = self._extract_date_from_filename(path.name)
        title = self._extract_title_from_filename(path.name)
        speakers = self._extract_speakers(content)
        
        return ContentEnvelope(
            source_path=path,
            content_type=ContentType.TRANSCRIPT,
            raw_content=content,
            date=date,
            title=title,
            participants=speakers,
            content_hash=self.compute_hash(content),
            metadata={
                "transcript": TranscriptMetadata(
                    speakers=speakers,
                    source_app="MacWhisper",
                    has_diarization=len(speakers) > 0,
                ).model_dump()
            }
        )
    
    def _extract_date_from_filename(self, filename: str) -> str:
        """Extract date from transcript filename."""
        # Patterns: "2025-12-15 16 10 - Title.md" or "2025-12-15 - Title.md"
        date_match = re.match(r"^(\d{4}-\d{2}-\d{2})", filename)
        if date_match:
            return date_match.group(1)
        return datetime.now().strftime("%Y-%m-%d")
    
    def _extract_title_from_filename(self, filename: str) -> str:
        """Extract title from transcript filename."""
        # Remove date and time patterns
        title = re.sub(r"^\d{4}-\d{2}-\d{2}\s*\d*:?\d*\s*-?\s*", "", filename)
        title = title.replace(".md", "").strip()
        
        # Handle emoji titles (e.g., "G24 Flight School 🧑‍🚀:  VAST Story")
        title = re.sub(r"\s+", " ", title)
        
        return title if title else "Meeting"
    
    def _extract_speakers(self, content: str) -> list[str]:
        """Extract speaker names from transcript."""
        speakers = set()
        
        # Pattern 1: "Speaker 1:", "Speaker 2:", etc.
        for match in re.finditer(r"(Speaker \d+):", content):
            speakers.add(match.group(1))
        
        # Pattern 2: "[Name]:" format
        for match in re.finditer(r"\[([^\]]+)\]:", content):
            name = match.group(1).strip()
            if name and len(name) < 50:  # Sanity check
                speakers.add(name)
        
        # Pattern 3: "**Name:** text" format (MacWhisper with names)
        for match in re.finditer(r"\*\*([^*]+)\*\*:", content):
            name = match.group(1).strip()
            if name and len(name) < 50:
                speakers.add(name)
        
        return list(speakers)
