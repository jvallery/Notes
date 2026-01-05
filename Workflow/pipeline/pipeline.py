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
import time
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
from scripts.utils.ai_client import log_pipeline_stats


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
    
    # Metrics
    metrics: dict = field(default_factory=dict)
    
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
    metrics: dict = field(default_factory=dict)
    
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
        trace_dir: Optional[Path] = None,
        show_cache_stats: bool = False,
        log_metrics: bool = True,
    ):
        self.vault_root = vault_root
        self.dry_run = dry_run
        self.verbose = verbose
        self.generate_outputs = generate_outputs
        self.force = force
        self.trace_dir = trace_dir
        self.show_cache_stats = show_cache_stats
        self.log_metrics = log_metrics
        
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
        phase_timings: dict[str, int] = {}
        run_start = time.time()
        
        try:
            # 1. Parse with adapter
            parse_start = time.time()
            envelope = self.registry.parse(path)
            phase_timings["adapter_ms"] = int((time.time() - parse_start) * 1000)
            if not envelope:
                result.success = False
                result.errors.append(f"No adapter found for {path}")
                result.metrics = {"timings": phase_timings, "cache": {}}
                return result
            
            result.content_type = envelope.content_type.value
            result.envelope = envelope
            
            # 2. Check for duplicates (skip if --force)
            if not self.force and self._is_duplicate(envelope):
                result.success = True
                result.errors.append("Skipped: duplicate content")
                result.metrics = {"timings": phase_timings, "cache": {}}
                return result
            
            # 3. Extract with LLM
            ctx_start = time.time()
            context = self.context
            phase_timings["context_ms"] = int((time.time() - ctx_start) * 1000)
            
            extract_start = time.time()
            extraction = self.extractor.extract(envelope, context)
            phase_timings["extract_ms"] = int((time.time() - extract_start) * 1000)
            result.extraction = extraction.model_dump()
            
            if self.verbose:
                self._log_extraction(extraction)
            
            # 4. Generate patches
            patch_start = time.time()
            plan = self.patch_generator.generate(extraction)
            phase_timings["patch_ms"] = int((time.time() - patch_start) * 1000)
            result.plan = plan
            
            # 5. Apply changes
            apply_ms = 0
            if not self.dry_run:
                apply_start = time.time()
                applier = TransactionalApply(self.vault_root, dry_run=False)
                apply_result = applier.apply(plan, path)
                result.apply_result = apply_result
                apply_ms = int((time.time() - apply_start) * 1000)
                
                if not apply_result.success:
                    result.success = False
                    result.errors.extend(apply_result.errors)
            phase_timings["apply_ms"] = apply_ms
            
            # 6. Generate outputs (if enabled and extraction suggests needs_reply)
            outputs_ms = 0
            suggested = extraction.suggested_outputs
            if self.generate_outputs and suggested and suggested.needs_reply:
                outputs_start = time.time()
                outputs = self.output_generator.generate_all(
                    extraction, 
                    self.context,
                    envelope.raw_content if envelope else ""
                )
                result.draft_reply = str(outputs.get("reply")) if outputs.get("reply") else None
                result.calendar_invite = {"path": str(outputs.get("calendar"))} if outputs.get("calendar") else None
                outputs_ms = int((time.time() - outputs_start) * 1000)
            phase_timings["outputs_ms"] = outputs_ms
            
            # 7. Persist trace artifacts if requested
            if self.trace_dir:
                self._persist_trace(envelope, extraction, plan)
            
            result.metrics = {
                "timings": phase_timings,
                "cache": getattr(self.extractor, "last_usage", {}),
                "run_ms": int((time.time() - run_start) * 1000),
            }
            
            return result
            
        except Exception as e:
            result.success = False
            result.errors.append(str(e))
            result.metrics = {
                "timings": phase_timings,
                "cache": getattr(self.extractor, "last_usage", {}),
            }
            return result
    
    def process_all(self) -> BatchResult:
        """Process all pending content in Inbox.
        
        Returns:
            BatchResult with all processing results
        """
        inbox = self.vault_root / "Inbox"
        pending: list[Path] = []
        
        for subdir in ["Email", "Transcripts", "Voice", "Attachments"]:
            subpath = inbox / subdir
            if subpath.exists():
                pending.extend(subpath.glob("*.md"))
        
        return self._process_paths(pending)
    
    def process_type(self, content_type: ContentType) -> BatchResult:
        """Process all pending content of a specific type.
        
        Args:
            content_type: Type of content to process
        
        Returns:
            BatchResult with processing results
        """
        # Map content type to inbox subdirectory
        type_dirs = {
            ContentType.EMAIL: "Email",
            ContentType.TRANSCRIPT: "Transcripts",
            ContentType.VOICE: "Voice",
            ContentType.DOCUMENT: "Attachments",
        }
        
        subdir = type_dirs.get(content_type, "Attachments")
        inbox_path = self.vault_root / "Inbox" / subdir
        
        pending = list(inbox_path.glob("*.md"))
        return self._process_paths(pending)
    
    def process_sources(self, content_type: Optional[ContentType] = None) -> BatchResult:
        """Re-process archived sources from the Sources/ directory."""
        sources_root = self.vault_root / "Sources"
        type_dirs = {
            ContentType.EMAIL: "Email",
            ContentType.TRANSCRIPT: "Transcripts",
            ContentType.VOICE: "Voice",
            ContentType.DOCUMENT: "Documents",
        }
        
        pending: list[Path] = []
        
        if content_type:
            dir_name = type_dirs.get(content_type)
            if dir_name:
                pending.extend((sources_root / dir_name).rglob("*.md"))
        else:
            for dir_name in type_dirs.values():
                path = sources_root / dir_name
                if path.exists():
                    pending.extend(path.rglob("*.md"))
        
        return self._process_paths(pending)
    
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
    
    def _process_paths(self, paths: list[Path]) -> BatchResult:
        """Process a list of paths and return aggregated results."""
        batch = BatchResult()
        batch.total = len(paths)
        batch_start = time.time()
        
        timings_accum: dict[str, int] = {}
        cache_calls = cache_hits = 0
        cached_tokens = prompt_tokens = total_tokens = 0
        
        for path in paths:
            result = self.process_file(path)
            batch.results.append(result)
            
            if result.success:
                if any("Skipped" in str(err) for err in result.errors):
                    batch.skipped += 1
                else:
                    batch.success += 1
            else:
                batch.failed += 1
            
            # Aggregate metrics
            metrics = result.metrics or {}
            timings = metrics.get("timings") or {}
            for phase, ms in timings.items():
                timings_accum[phase] = timings_accum.get(phase, 0) + ms
            
            cache = metrics.get("cache") or {}
            if cache:
                cache_calls += 1
                if cache.get("cache_hit"):
                    cache_hits += 1
                cached_tokens += cache.get("cached_tokens", 0)
                prompt_tokens += cache.get("prompt_tokens", 0)
                total_tokens += cache.get("total_tokens", 0)
        
        count = len(batch.results)
        phase_avg = {k: int(v / count) for k, v in timings_accum.items()} if count else {}
        cache_summary = {
            "calls": cache_calls,
            "hits": cache_hits,
            "hit_rate": (cache_hits / cache_calls * 100) if cache_calls else 0,
            "cached_tokens": cached_tokens,
            "prompt_tokens": prompt_tokens,
            "total_tokens": total_tokens,
        }
        
        batch.metrics = {
            "run_ms": int((time.time() - batch_start) * 1000),
            "phase_ms_avg": phase_avg,
            "cache": cache_summary,
        }
        
        if self.log_metrics and batch.total > 0:
            try:
                log_pipeline_stats({
                    "timestamp": datetime.now().isoformat(),
                    "total": batch.total,
                    "success": batch.success,
                    "failed": batch.failed,
                    "skipped": batch.skipped,
                    **batch.metrics,
                })
            except Exception:
                # Metrics logging should never break the pipeline
                pass
        
        # Invalidate entity index (new entities may have been created)
        self.entity_index.invalidate()
        
        return batch
    
    def _log_extraction(self, extraction):
        """Log extraction summary in verbose mode."""
        from rich.console import Console
        console = Console()
        
        console.print(f"  Note type: {extraction.note_type}")
        console.print(f"  Summary: {extraction.summary[:80]}...")
        console.print(f"  Facts: {len(extraction.facts)}")
        console.print(f"  Tasks: {len(extraction.tasks)}")
        console.print(f"  Entities with facts: {len(extraction.get_entities_with_facts())}")

    def _persist_trace(self, envelope: ContentEnvelope, extraction, plan: ChangePlan):
        """Persist extraction and changeplan artifacts for audit/traceability."""
        if not self.trace_dir:
            return
        
        trace_root = self.trace_dir
        trace_root.mkdir(parents=True, exist_ok=True)
        
        stem = envelope.source_path.stem
        extraction_path = trace_root / f"{stem}.extraction.json"
        changeplan_path = trace_root / f"{stem}.changeplan.json"
        
        try:
            extraction_path.write_text(json.dumps(extraction.model_dump(mode="json"), indent=2))
        except Exception:
            pass
        
        try:
            changeplan_path.write_text(json.dumps(plan.model_dump(mode="json", exclude_none=True), indent=2))
        except Exception:
            pass
