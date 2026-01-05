"""
Unified Pipeline - Main orchestrator for content processing.

Combines:
- Adapters (normalize content)
- Context (load manifests, persona, glossary)
- Extraction (LLM structured output)
- Patching (generate patches)
- Apply (transactional execution)
- Enrichment (trigger for new entities)
"""

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional
from dataclasses import dataclass, field

sys.path.insert(0, str(Path(__file__).parent.parent))

from .envelope import ContentEnvelope, ContentType
from .adapters import AdapterRegistry
from .context import ContextBundle
from .extract import UnifiedExtractor
from .patch import PatchGenerator, ChangePlan
from .apply import TransactionalApply, ApplyResult
from .entities import EntityIndex
from .outputs import OutputGenerator


@dataclass
class ProcessingResult:
    """Result of processing a single content item."""
    
    source_path: str
    content_type: str
    success: bool = True
    
    # Artifacts
    envelope: Optional[ContentEnvelope] = None
    extraction: Optional[dict] = None
    plan: Optional[ChangePlan] = None
    apply_result: Optional[ApplyResult] = None
    
    # Output suggestions
    draft_reply: Optional[str] = None
    calendar_invite: Optional[dict] = None
    
    # Errors
    errors: list[str] = field(default_factory=list)
    
    def __str__(self):
        if self.success:
            return f"✓ {self.source_path}"
        else:
            return f"✗ {self.source_path}: {', '.join(self.errors)}"


@dataclass
class BatchResult:
    """Result of processing a batch of content."""
    
    total: int = 0
    success: int = 0
    failed: int = 0
    skipped: int = 0
    results: list[ProcessingResult] = field(default_factory=list)
    
    def __str__(self):
        return f"Processed {self.total}: {self.success} success, {self.failed} failed, {self.skipped} skipped"


class UnifiedPipeline:
    """Unified content processing pipeline.
    
    Usage:
        pipeline = UnifiedPipeline(vault_root)
        
        # Process single file
        result = pipeline.process_file(Path("Inbox/Email/..."))
        
        # Process all pending content
        batch = pipeline.process_all()
        
        # Process specific content type
        batch = pipeline.process_type(ContentType.EMAIL)
    """
    
    def __init__(
        self,
        vault_root: Path,
        dry_run: bool = False,
        verbose: bool = False,
        generate_outputs: bool = True,
        force: bool = False,
    ):
        self.vault_root = vault_root
        self.dry_run = dry_run
        self.verbose = verbose
        self.generate_outputs = generate_outputs
        self.force = force
        
        # Initialize components
        self.registry = AdapterRegistry.default()
        self.entity_index = EntityIndex(vault_root)
        self.extractor = UnifiedExtractor(vault_root, verbose=verbose)
        self.patch_generator = PatchGenerator(vault_root, self.entity_index)
        self.output_generator = OutputGenerator(vault_root, dry_run=dry_run, verbose=verbose)
        
        # Shared context (loaded once)
        self._context: Optional[ContextBundle] = None
    
    @property
    def context(self) -> ContextBundle:
        """Get or load shared context."""
        if self._context is None:
            self._context = ContextBundle.load(self.vault_root)
        return self._context
    
    def process_file(self, path: Path) -> ProcessingResult:
        """Process a single content file.
        
        Args:
            path: Path to content file
        
        Returns:
            ProcessingResult with all details
        """
        result = ProcessingResult(
            source_path=str(path),
            content_type="unknown"
        )
        
        try:
            # 1. Parse with adapter
            envelope = self.registry.parse(path)
            if not envelope:
                result.success = False
                result.errors.append(f"No adapter found for {path}")
                return result
            
            result.content_type = envelope.content_type.value
            result.envelope = envelope
            
            # 2. Check for duplicates (skip if --force)
            if not self.force and self._is_duplicate(envelope):
                result.success = True
                result.errors.append("Skipped: duplicate content")
                return result
            
            # 3. Extract with LLM
            extraction = self.extractor.extract(envelope, self.context)
            result.extraction = extraction.model_dump()
            
            if self.verbose:
                self._log_extraction(extraction)
            
            # 4. Generate patches
            plan = self.patch_generator.generate(extraction)
            result.plan = plan
            
            # 5. Apply changes
            if not self.dry_run:
                applier = TransactionalApply(self.vault_root, dry_run=False)
                apply_result = applier.apply(plan, path)
                result.apply_result = apply_result
                
                if not apply_result.success:
                    result.success = False
                    result.errors.extend(apply_result.errors)
            
            # 6. Generate outputs (if enabled and extraction suggests needs_reply)
            suggested = extraction.suggested_outputs
            if self.generate_outputs and suggested and suggested.needs_reply:
                outputs = self.output_generator.generate_all(
                    extraction, 
                    self.context,
                    envelope.raw_content if envelope else ""
                )
                result.draft_reply = str(outputs.get("reply")) if outputs.get("reply") else None
                result.calendar_invite = {"path": str(outputs.get("calendar"))} if outputs.get("calendar") else None
            
            return result
            
        except Exception as e:
            result.success = False
            result.errors.append(str(e))
            return result
    
    def process_all(self) -> BatchResult:
        """Process all pending content in Inbox.
        
        Returns:
            BatchResult with all processing results
        """
        batch = BatchResult()
        
        # Collect all pending files
        inbox = self.vault_root / "Inbox"
        pending: list[Path] = []
        
        for subdir in ["Email", "Transcripts", "Voice", "Attachments"]:
            subpath = inbox / subdir
            if subpath.exists():
                pending.extend(subpath.glob("*.md"))
        
        batch.total = len(pending)
        
        for path in pending:
            result = self.process_file(path)
            batch.results.append(result)
            
            if result.success:
                if "Skipped" in str(result.errors):
                    batch.skipped += 1
                else:
                    batch.success += 1
            else:
                batch.failed += 1
        
        # Invalidate entity index (new entities may have been created)
        self.entity_index.invalidate()
        
        return batch
    
    def process_type(self, content_type: ContentType) -> BatchResult:
        """Process all pending content of a specific type.
        
        Args:
            content_type: Type of content to process
        
        Returns:
            BatchResult with processing results
        """
        batch = BatchResult()
        
        # Map content type to inbox subdirectory
        type_dirs = {
            ContentType.EMAIL: "Email",
            ContentType.TRANSCRIPT: "Transcripts",
            ContentType.VOICE: "Voice",
            ContentType.DOCUMENT: "Attachments",
        }
        
        subdir = type_dirs.get(content_type, "Attachments")
        inbox_path = self.vault_root / "Inbox" / subdir
        
        if not inbox_path.exists():
            return batch
        
        pending = list(inbox_path.glob("*.md"))
        batch.total = len(pending)
        
        for path in pending:
            result = self.process_file(path)
            batch.results.append(result)
            
            if result.success:
                if "Skipped" in str(result.errors):
                    batch.skipped += 1
                else:
                    batch.success += 1
            else:
                batch.failed += 1
        
        return batch
    
    def _is_duplicate(self, envelope: ContentEnvelope) -> bool:
        """Check if content has already been processed."""
        # Check extraction directory for existing extraction
        extraction_dir = self.vault_root / "Inbox" / "_extraction"
        if not extraction_dir.exists():
            return False
        
        # Look for matching extraction file
        stem = envelope.source_path.stem
        for ext_file in extraction_dir.glob(f"{stem}.*extraction.json"):
            return True
        
        return False
    
    def _log_extraction(self, extraction):
        """Log extraction summary in verbose mode."""
        from rich.console import Console
        console = Console()
        
        console.print(f"  Note type: {extraction.note_type}")
        console.print(f"  Summary: {extraction.summary[:80]}...")
        console.print(f"  Facts: {len(extraction.facts)}")
        console.print(f"  Tasks: {len(extraction.tasks)}")
        console.print(f"  Entities with facts: {len(extraction.get_entities_with_facts())}")
