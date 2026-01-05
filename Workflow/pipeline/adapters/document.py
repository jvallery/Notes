"""
Document Adapter - Parse documents and articles into ContentEnvelope.

Handles general documents dropped into the vault.
"""

import re
from datetime import datetime
from pathlib import Path
from typing import Optional

from .base import BaseAdapter
from ..envelope import ContentEnvelope, ContentType, DocumentMetadata


class DocumentAdapter(BaseAdapter):
    """Parse general documents and articles."""
    
    @property
    def content_type(self) -> ContentType:
        return ContentType.DOCUMENT
    
    def can_handle(self, path: Path) -> bool:
        """Detect if this is a document file.
        
        Documents are:
        - In Inbox/Attachments/ directory
        - Markdown files not matching email/transcript patterns
        - PDF/DOCX files (future: after text extraction)
        """
        if not path.is_file():
            return False
        
        # Check path
        if "Attachments" in path.parts:
            return path.suffix in [".md", ".txt"]
        
        # Default handler for markdown files
        if path.suffix == ".md":
            return True
        
        return False
    
    def parse(self, path: Path) -> ContentEnvelope:
        """Parse document file into ContentEnvelope."""
        content = path.read_text()
        
        # Extract metadata
        title = self._extract_title(content, path.name)
        date = self._extract_date(content, path)
        author = self._extract_author(content)
        doc_type = self._infer_document_type(content, path)
        
        return ContentEnvelope(
            source_path=path,
            content_type=ContentType.DOCUMENT,
            raw_content=content,
            date=date,
            title=title,
            participants=[author] if author else [],
            content_hash=self.compute_hash(content),
            metadata={
                "document": DocumentMetadata(
                    document_type=doc_type,
                    author=author,
                    file_type=path.suffix[1:] if path.suffix else "unknown",
                ).model_dump()
            }
        )
    
    def _extract_title(self, content: str, filename: str) -> str:
        """Extract title from document."""
        # Check for H1 heading
        lines = content.split("\n")
        for line in lines[:10]:
            if line.startswith("# "):
                return line[2:].strip()
        
        # Fall back to filename
        return filename.replace(".md", "").replace("_", " ").strip()
    
    def _extract_date(self, content: str, path: Path) -> str:
        """Extract date from document."""
        # Check frontmatter
        if content.startswith("---"):
            date_match = re.search(r"date:\s*[\"']?(\d{4}-\d{2}-\d{2})", content[:500])
            if date_match:
                return date_match.group(1)
        
        # Check filename
        date_match = re.match(r"^(\d{4}-\d{2}-\d{2})", path.name)
        if date_match:
            return date_match.group(1)
        
        # Use file modification time
        mtime = path.stat().st_mtime
        return datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")
    
    def _extract_author(self, content: str) -> Optional[str]:
        """Extract author from document."""
        # Check frontmatter
        if content.startswith("---"):
            author_match = re.search(r"author:\s*[\"']?([^\n\"']+)", content[:500])
            if author_match:
                return author_match.group(1).strip()
        
        return None
    
    def _infer_document_type(self, content: str, path: Path) -> str:
        """Infer document type from content and path."""
        content_lower = content.lower()
        
        if "proposal" in content_lower or "proposal" in path.name.lower():
            return "proposal"
        if "spec" in content_lower or "specification" in content_lower:
            return "specification"
        if "report" in content_lower:
            return "report"
        if "article" in path.parts or "articles" in path.parts:
            return "article"
        
        return "general"
