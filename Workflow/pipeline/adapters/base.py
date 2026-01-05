"""
Base Adapter - Abstract interface for content adapters.
"""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Optional, Type
import hashlib

from ..envelope import ContentEnvelope, ContentType


class BaseAdapter(ABC):
    """Abstract base class for content adapters.
    
    Each adapter knows how to:
    1. Detect if a file matches its content type
    2. Parse the file into a ContentEnvelope
    """
    
    @property
    @abstractmethod
    def content_type(self) -> ContentType:
        """The content type this adapter handles."""
        pass
    
    @abstractmethod
    def can_handle(self, path: Path) -> bool:
        """Check if this adapter can handle the given file."""
        pass
    
    @abstractmethod
    def parse(self, path: Path) -> ContentEnvelope:
        """Parse the file into a ContentEnvelope."""
        pass
    
    def compute_hash(self, content: str) -> str:
        """Compute content hash for deduplication."""
        # Strip frontmatter
        if content.startswith("---"):
            end = content.find("\n---", 3)
            if end != -1:
                content = content[end + 4:]
        
        # Normalize and hash first 2000 chars
        normalized = content.strip()[:2000]
        return hashlib.md5(normalized.encode()).hexdigest()[:12]


class AdapterRegistry:
    """Registry of content adapters.
    
    Tries adapters in order to find one that can handle each file.
    """
    
    def __init__(self):
        self._adapters: list[BaseAdapter] = []
    
    def register(self, adapter: BaseAdapter) -> None:
        """Register an adapter."""
        self._adapters.append(adapter)
    
    def get_adapter(self, path: Path) -> Optional[BaseAdapter]:
        """Find an adapter that can handle the given file."""
        for adapter in self._adapters:
            if adapter.can_handle(path):
                return adapter
        return None
    
    def parse(self, path: Path) -> Optional[ContentEnvelope]:
        """Parse a file using the appropriate adapter."""
        adapter = self.get_adapter(path)
        if adapter:
            return adapter.parse(path)
        return None
    
    @classmethod
    def default(cls) -> "AdapterRegistry":
        """Create registry with all default adapters."""
        from .email import EmailAdapter
        from .transcript import TranscriptAdapter
        from .document import DocumentAdapter
        
        registry = cls()
        registry.register(EmailAdapter())
        registry.register(TranscriptAdapter())
        registry.register(DocumentAdapter())
        return registry
