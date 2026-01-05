"""
Unified Pipeline - Main orchestrator for content processing.

Combines:
- Adapters (normalize content)
- Context (load manifests, persona, glossary)
- Extraction (LLM structured output)
- Patching (generate patches)
- Apply (transactional execution)
- Enrichment (trigger for new entities)

Supports parallel extraction with deferred patch application.
"""

import json
import sys
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path
from typing import Optional, Any
from dataclasses import dataclass, field

sys.path.insert(0, str(Path(__file__).parent.parent))

from .envelope import ContentEnvelope, ContentType
from .adapters import AdapterRegistry
from .context import ContextBundle
from .extract import UnifiedExtractor
from .patch import PatchGenerator, ChangePlan, PatchCollector
from .apply import TransactionalApply, ApplyResult
from .entities import EntityIndex
from .outputs import OutputGenerator
from .models import ContactInfo
from scripts.utils.ai_client import log_pipeline_stats
from scripts.utils.config import load_config


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
        config: Optional[dict[str, Any]] = None,
        max_workers: Optional[int] = None,
    ):
        self.vault_root = vault_root
        self.dry_run = dry_run
        self.verbose = verbose
        self.generate_outputs = generate_outputs
        self.force = force
        self.trace_dir = trace_dir
        self.show_cache_stats = show_cache_stats
        self.log_metrics = log_metrics
        self.config = config or load_config(vault_root_override=vault_root)
        
        # Parallel processing settings
        parallel_cfg = self.config.get("parallel", {})
        self.max_workers = max_workers if max_workers is not None else parallel_cfg.get("max_workers", 1)
        self.parallel_enabled = parallel_cfg.get("enabled", False) and self.max_workers > 1
        rate_limit_cfg = parallel_cfg.get("rate_limit", {})
        self.requests_per_minute = rate_limit_cfg.get("requests_per_minute", 50)
        path_cfg = self.config.get("paths", {})
        self.inbox_paths = {
            k: Path(v) for k, v in path_cfg.get("inbox", {}).items() if isinstance(v, str)
        }
        self.source_paths = {
            k: Path(v) for k, v in path_cfg.get("sources", {}).items() if isinstance(v, str)
        }
        inbox_root = Path(self.inbox_paths.get("root", self.vault_root / "Inbox"))
        sources_root = Path(self.source_paths.get("root", self.vault_root / "Sources"))
        self.default_inbox = {
            "email": inbox_root / "Email",
            "transcripts": inbox_root / "Transcripts",
            "voice": inbox_root / "Voice",
            "attachments": inbox_root / "Attachments",
        }
        self.default_sources = {
            "email": sources_root / "Email",
            "transcripts": sources_root / "Transcripts",
            "documents": sources_root / "Documents",
            "voice": sources_root / "Voice",
        }
        
        # Initialize components
        self.registry = AdapterRegistry.default()
        self.entity_index = EntityIndex(vault_root, config=self.config)
        self.extractor = UnifiedExtractor(vault_root, verbose=verbose)
        self.patch_generator = PatchGenerator(vault_root, self.entity_index)
        self.output_generator = OutputGenerator(vault_root, dry_run=dry_run, verbose=verbose)
        
        # Shared context (loaded once)
        self._context: Optional[ContextBundle] = None
    
    @property
    def context(self) -> ContextBundle:
        """Get or load shared context."""
        if self._context is None:
            self._context = ContextBundle.load(self.vault_root, config=self.config, entity_index=self.entity_index)
        return self._context
    
    def process_file(self, path: Path, apply: bool = True) -> ProcessingResult:
        """Process a single content file.
        
        Args:
            path: Path to content file
            apply: If False, only extract + plan (no filesystem changes)
        
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
            context = ContextBundle.load(self.vault_root, envelope, self.entity_index)
            phase_timings["context_ms"] = int((time.time() - ctx_start) * 1000)
            
            extract_start = time.time()
            extraction = self.extractor.extract(envelope, context)
            phase_timings["extract_ms"] = int((time.time() - extract_start) * 1000)
            self._augment_extraction_with_headers(extraction, envelope)
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
            if apply and not self.dry_run:
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
            if apply and self.generate_outputs and suggested and suggested.needs_reply:
                outputs_start = time.time()
                outputs = self.output_generator.generate_all(
                    extraction, 
                    context,
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
        pending: list[Path] = []
        
        for key in ["email", "transcripts", "voice", "attachments"]:
            subpath = Path(self.inbox_paths.get(key, self.default_inbox[key]))
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
            ContentType.EMAIL: "email",
            ContentType.TRANSCRIPT: "transcripts",
            ContentType.VOICE: "voice",
            ContentType.DOCUMENT: "attachments",
        }
        
        subdir_key = type_dirs.get(content_type, "attachments")
        inbox_path = Path(self.inbox_paths.get(subdir_key, self.default_inbox[subdir_key]))
        
        pending = list(inbox_path.glob("*.md")) if inbox_path.exists() else []
        return self._process_paths(pending)
    
    def process_sources(self, content_type: Optional[ContentType] = None) -> BatchResult:
        """Re-process archived sources from the Sources/ directory."""
        type_dirs = {
            ContentType.EMAIL: "email",
            ContentType.TRANSCRIPT: "transcripts",
            ContentType.VOICE: "voice",
            ContentType.DOCUMENT: "documents",
        }
        
        pending: list[Path] = []
        
        if content_type:
            dir_name = type_dirs.get(content_type)
            if dir_name:
                base = Path(self.source_paths.get(dir_name, self.default_sources[dir_name]))
                if base.exists():
                    pending.extend(base.rglob("*.md"))
        else:
            for dir_name in type_dirs.values():
                path = Path(self.source_paths.get(dir_name, self.default_sources[dir_name]))
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
    
    def _augment_extraction_with_headers(self, extraction, envelope: ContentEnvelope):
        """Ensure sender/recipient emails are preserved in contacts/participants."""
        email_meta = (envelope.metadata or {}).get("email") if envelope.metadata else {}
        if not email_meta:
            return
        
        header_contacts = []
        sender_email = email_meta.get("sender_email")
        sender_name = email_meta.get("sender_name") or sender_email
        if sender_email:
            header_contacts.append(ContactInfo(name=sender_name, email=sender_email))
        
        for rec in email_meta.get("recipients_detail", []) or []:
            name = rec.get("name") or rec.get("email")
            header_contacts.append(ContactInfo(name=name, email=rec.get("email")))
        
        existing_emails = {c.email.lower() for c in extraction.contacts if c.email}
        for contact in header_contacts:
            if contact.email and contact.email.lower() in existing_emails:
                continue
            extraction.contacts.append(contact)
        
        # Ensure participants includes header names when extraction omits them
        if not extraction.participants and envelope.participants:
            extraction.participants = envelope.participants
    
    def _process_paths(self, paths: list[Path]) -> BatchResult:
        """Process a list of paths and return aggregated results.
        
        Uses parallel processing when max_workers > 1 and parallel is enabled.
        """
        if self.parallel_enabled and self.max_workers > 1 and len(paths) > 1:
            return self._process_paths_parallel(paths)
        return self._process_paths_sequential(paths)
    
    def _process_paths_parallel(self, paths: list[Path]) -> BatchResult:
        """Process paths in parallel with rate limiting and patch collection.
        
        Uses ThreadPoolExecutor with a semaphore to respect rate limits.
        Collects all patches, merges by target, then applies atomically.
        """
        batch = BatchResult()
        batch.total = len(paths)
        batch_start = time.time()
        
        timings_accum: dict[str, int] = {}
        cache_calls = cache_hits = 0
        cached_tokens = prompt_tokens = total_tokens = 0
        
        # Rate limiting semaphore (max concurrent LLM calls)
        semaphore = threading.Semaphore(self.max_workers)
        
        # Collect patches for deferred merge
        patch_collector = PatchCollector()
        source_files: list[Path] = []
        
        def process_with_semaphore(path: Path) -> ProcessingResult:
            """Process a single file with rate limiting."""
            with semaphore:
                return self.process_file(path, apply=False)
        
        # Submit all tasks
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_path = {executor.submit(process_with_semaphore, p): p for p in paths}
            
            for future in as_completed(future_to_path):
                path = future_to_path[future]
                try:
                    result = future.result()
                    batch.results.append(result)
                    
                    should_apply = result.success and not any("Skipped" in str(err) for err in result.errors)
                    if should_apply and result.plan:
                        patch_collector.collect(result.plan)
                        source_files.append(path)
                    
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
                
                except Exception as e:
                    batch.results.append(ProcessingResult(
                        source_path=str(path),
                        content_type="unknown",
                        success=False,
                        errors=[f"Parallel processing error: {e}"]
                    ))
        
        # Merge all patches and apply atomically (single-writer)
        meeting_notes = patch_collector.get_meeting_notes()
        needs_apply = (patch_collector.has_patches or bool(meeting_notes)) and not self.dry_run and bool(source_files)
        if needs_apply:
            try:
                merged_plan = patch_collector.merge()
                applier = TransactionalApply(self.vault_root, dry_run=False)
                primary_source = source_files[0]
                extra_sources = source_files[1:] if len(source_files) > 1 else None
                extra_notes = meeting_notes[1:] if len(meeting_notes) > 1 else None
                apply_result = applier.apply(
                    merged_plan,
                    primary_source,
                    extra_meeting_notes=extra_notes,
                    extra_source_paths=extra_sources,
                )

                # Propagate apply result to individual items
                for r in batch.results:
                    if r.success and not any("Skipped" in str(err) for err in r.errors):
                        r.apply_result = apply_result
                        if not apply_result.success:
                            r.success = False
                            r.errors.extend(apply_result.errors)
            except Exception as e:
                for r in batch.results:
                    if r.success and not any("Skipped" in str(err) for err in r.errors):
                        r.success = False
                        r.errors.append(f"Batch merge/apply error: {e}")

        # Recompute counts after batch apply
        batch.success = batch.failed = batch.skipped = 0
        for r in batch.results:
            if r.success:
                if any("Skipped" in str(err) for err in r.errors):
                    batch.skipped += 1
                else:
                    batch.success += 1
            else:
                batch.failed += 1
        
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
            "parallel": {
                "workers": self.max_workers,
                "files_processed": len(paths),
                "patches_merged": patch_collector.patch_count,
            }
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
                pass
        
        self.entity_index.invalidate()
        return batch
    
    def _process_paths_sequential(self, paths: list[Path]) -> BatchResult:
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
