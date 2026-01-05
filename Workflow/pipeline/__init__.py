"""
Unified Content Pipeline

This package provides a unified ETL pipeline for processing various content types
(email, transcript, document, voice) into the Obsidian vault.

Architecture:
    adapters/   - Content type adapters (normalize to ContentEnvelope)
    context.py  - Context loading (manifests, persona, glossary)
    extract.py  - Unified extraction (LLM + schema)
    patch.py    - Patch generation (deterministic)
    enrich.py   - Enrichment triggers
    outputs.py  - Output generation (drafts, tasks)
    apply.py    - Transactional apply

Usage:
    from pipeline import UnifiedPipeline
    
    pipeline = UnifiedPipeline()
    result = pipeline.process("Inbox/Email/2026-01-04_*.md")
"""

from .envelope import ContentEnvelope, ContentType
from .context import ContextBundle
from .entities import EntityIndex
from .extract import UnifiedExtractor
from .patch import PatchGenerator
from .apply import TransactionalApply
from .pipeline import UnifiedPipeline

__all__ = [
    "ContentEnvelope",
    "ContentType",
    "ContextBundle",
    "EntityIndex",
    "UnifiedExtractor",
    "PatchGenerator",
    "TransactionalApply",
    "UnifiedPipeline",
]
