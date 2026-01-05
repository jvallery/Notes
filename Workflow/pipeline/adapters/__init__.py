"""
Content Adapters - Parse raw content into ContentEnvelope.

Each content type has an adapter that:
1. Detects if a file matches the content type
2. Parses metadata from the content
3. Returns a ContentEnvelope for unified processing
"""

from .base import BaseAdapter, AdapterRegistry
from .email import EmailAdapter
from .transcript import TranscriptAdapter
from .document import DocumentAdapter

__all__ = [
    "BaseAdapter",
    "AdapterRegistry",
    "EmailAdapter",
    "TranscriptAdapter",
    "DocumentAdapter",
]
