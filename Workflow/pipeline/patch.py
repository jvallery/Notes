"""
Patch Generator - Generate vault patches from extractions.

Key insight: We patch entities when we LEARN something about them (facts),
not just because they're mentioned.
"""

import sys
from datetime import datetime
from pathlib import Path
from typing import Optional
from pydantic import BaseModel, Field

sys.path.insert(0, str(Path(__file__).parent.parent))

from .models import UnifiedExtraction, MentionedEntity, TaskItem
from .entities import EntityIndex


class PatchOperation(BaseModel):
    """A single patch operation to apply to the vault."""
    
    operation: str  # create, patch, link
    target_path: str  # Relative path in vault
    target_entity: str  # Entity name for logging
    
    # For create operations
    template: Optional[str] = None
    template_context: Optional[dict] = None
    
    # For patch operations
    add_frontmatter: Optional[dict] = None
    add_facts: Optional[list[str]] = None
    add_topics: Optional[list[str]] = None
    add_decisions: Optional[list[str]] = None
    add_context: Optional[str] = None
    add_tasks: Optional[list[dict]] = None
    
    # For link operations
    add_wikilinks: Optional[list[str]] = None


class ChangePlan(BaseModel):
    """Complete change plan for a content extraction."""
    
    version: str = "2.0"
    source_file: str
    extraction_file: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.now)
    
    # Meeting note creation
    meeting_note_path: Optional[str] = None
    meeting_note: Optional[dict] = None
    
    # Entity patches
    patches: list[PatchOperation] = Field(default_factory=list)
    
    # Entities to create (for new entities)
    entities_to_create: list[dict] = Field(default_factory=list)
    
    # Warnings
    warnings: list[str] = Field(default_factory=list)
    
    def validate_plan(self) -> list[str]:
        """Validate the change plan and return a list of issues.
        
        Returns:
            List of validation issues (empty if plan is valid)
        """
        issues = []
        
        # 1. Check source file is set
        if not self.source_file:
            issues.append("source_file is required")
        
        # 2. Check meeting note path is valid if set
        if self.meeting_note_path:
            if ".." in self.meeting_note_path:
                issues.append(f"meeting_note_path contains invalid path traversal: {self.meeting_note_path}")
            if not self.meeting_note:
                issues.append("meeting_note_path is set but meeting_note context is missing")
        
        # 3. Validate each patch operation
        patch_targets = set()
        for i, patch in enumerate(self.patches):
            # Check for duplicate targets
            if patch.target_path in patch_targets:
                issues.append(f"Duplicate patch target: {patch.target_path}")
            patch_targets.add(patch.target_path)
            
            # Validate operation type
            if patch.operation not in ("create", "patch", "link"):
                issues.append(f"Patch {i}: Invalid operation '{patch.operation}'")
            
            # Check target path validity
            if ".." in patch.target_path:
                issues.append(f"Patch {i}: target_path contains invalid path traversal")
            
            # Check that patch operations have something to patch
            if patch.operation == "patch":
                has_changes = any([
                    patch.add_frontmatter,
                    patch.add_facts,
                    patch.add_topics,
                    patch.add_decisions,
                    patch.add_context,
                    patch.add_tasks,
                ])
                if not has_changes:
                    issues.append(f"Patch {i}: patch operation has no changes for {patch.target_entity}")
        
        return issues
    
    def is_valid(self) -> bool:
        """Check if the change plan is valid."""
        return len(self.validate_plan()) == 0


class PatchGenerator:
    """Generate vault patches from extractions.
    
    Patching rules:
    1. Primary entity always gets patched (context, tasks)
    2. Entities with facts_about get patched (we learned something)
    3. Participants get context updates (lighter touch)
    4. Companies get patched if facts are discovered (not just mentions)
    """
    
    # Companies to skip (internal/obvious)
    SKIP_COMPANIES = {
        "vast data", "vast", "microsoft", "google", "amazon", "aws",
        "openai", "anthropic", "nvidia"  # Can be configured
    }
    
    def __init__(self, vault_root: Path, entity_index: Optional[EntityIndex] = None):
        self.vault_root = vault_root
        self.entity_index = entity_index or EntityIndex(vault_root)
    
    def generate(self, extraction: UnifiedExtraction) -> ChangePlan:
        """Generate change plan from extraction.
        
        Uses EntityIndex for alias resolution and duplicate detection.
        
        Args:
            extraction: UnifiedExtraction with all extracted knowledge
        
        Returns:
            ChangePlan with all operations
        """
        plan = ChangePlan(source_file=extraction.source_file)
        
        # Track patched targets to avoid duplicates
        patched_paths: set[str] = set()
        
        # Track entity names we've processed (for dedup warnings)
        processed_entities: dict[str, str] = {}  # normalized name -> original name
        
        # 1. Meeting note creation
        note_path, note_context = self._generate_meeting_note(extraction)
        if note_path:
            plan.meeting_note_path = note_path
            plan.meeting_note = note_context
        
        # 2. Primary entity patches
        if extraction.primary_entity:
            normalized = self.entity_index.normalize_name(extraction.primary_entity.name)
            if normalized != extraction.primary_entity.name:
                plan.warnings.append(f"Resolved alias: '{extraction.primary_entity.name}' → '{normalized}'")
            processed_entities[normalized.lower()] = extraction.primary_entity.name
            self._warn_duplicate(extraction.primary_entity.name, extraction.primary_entity.entity_type, plan)
            
            patches = self._generate_primary_patches(extraction)
            for patch in patches:
                if patch.target_path not in patched_paths:
                    plan.patches.append(patch)
                    patched_paths.add(patch.target_path)
        
        # 3. Entities with facts (we learned something)
        for entity in extraction.get_entities_with_facts():
            normalized = self.entity_index.normalize_name(entity.name)
            norm_lower = normalized.lower()
            
            # Check for potential duplicates
            if norm_lower in processed_entities and processed_entities[norm_lower] != entity.name:
                plan.warnings.append(
                    f"Potential duplicate: '{entity.name}' may be same as '{processed_entities[norm_lower]}' (consider merge)"
                )
                continue  # Skip to avoid double-patching
            
            if normalized != entity.name:
                plan.warnings.append(f"Resolved alias: '{entity.name}' → '{normalized}'")
            processed_entities[norm_lower] = entity.name
            self._warn_duplicate(entity.name, entity.entity_type, plan)
            
            patches = self._generate_fact_patches(entity, extraction)
            for patch in patches:
                if patch.target_path not in patched_paths:
                    plan.patches.append(patch)
                    patched_paths.add(patch.target_path)
        
        # 4. Participant context updates
        for participant in extraction.participants:
            normalized = self.entity_index.normalize_name(participant)
            norm_lower = normalized.lower()
            
            # Check for potential duplicates
            if norm_lower in processed_entities:
                continue  # Already processed
            
            processed_entities[norm_lower] = participant
            
            patches = self._generate_participant_patches(participant, extraction)
            for patch in patches:
                if patch.target_path not in patched_paths:
                    plan.patches.append(patch)
                    patched_paths.add(patch.target_path)
        
        # 5. Company patches (only if facts discovered)
        for entity in extraction.mentioned_entities:
            if entity.entity_type == "company" and entity.facts_about:
                company_lower = entity.name.lower()
                if company_lower not in self.SKIP_COMPANIES:
                    patches = self._generate_company_patches(entity, extraction)
                    for patch in patches:
                        if patch.target_path not in patched_paths:
                            plan.patches.append(patch)
                            patched_paths.add(patch.target_path)
        
        return plan
    
    def _generate_meeting_note(self, extraction: UnifiedExtraction) -> tuple[Optional[str], Optional[dict]]:
        """Generate meeting note path and context."""
        
        # Determine destination folder
        if extraction.primary_entity:
            folder = self._get_entity_folder(extraction.primary_entity, extraction)
        else:
            # Default to first participant
            if extraction.participants:
                first_participant = extraction.participants[0]
                email = self._get_email_for_participant(first_participant, extraction)
                folder = self.entity_index.find_person(first_participant, email=email)
            else:
                folder = None
        
        if not folder:
            return None, None
        
        # Sanitize title for filename
        from scripts.utils.templates import sanitize_path_name
        safe_title = sanitize_path_name(extraction.title)
        
        note_path = f"{folder.relative_to(self.vault_root)}/{extraction.date} - {safe_title}.md"
        
        # Build context for template
        context = {
            "title": extraction.title,
            "date": extraction.date,
            "type": extraction.note_type,
            "participants": extraction.participants,
            "summary": extraction.summary,
            "topics": extraction.topics,
            "decisions": extraction.decisions,
            "tasks": [t.model_dump() for t in extraction.tasks],
            "facts": [f.text for f in extraction.facts],
            "source_ref": extraction.source_file,
        }
        
        return note_path, context
    
    def _generate_primary_patches(self, extraction: UnifiedExtraction) -> list[PatchOperation]:
        """Generate patches for the primary entity."""
        patches = []
        
        if not extraction.primary_entity:
            return patches
        
        folder = self._get_entity_folder(extraction.primary_entity, extraction)
        if not folder:
            return patches
        
        readme_path = folder / "README.md"
        if not readme_path.exists():
            return patches
        
        # Context entry
        context_entry = f"- {extraction.date}: {extraction.summary[:100]}..."
        
        # Facts from extraction
        facts = [f.text for f in extraction.facts 
                 if f.about_entity and f.about_entity.name == extraction.primary_entity.name]
        
        patches.append(PatchOperation(
            operation="patch",
            target_path=str(readme_path.relative_to(self.vault_root)),
            target_entity=extraction.primary_entity.name,
            add_frontmatter={"last_contact": extraction.date},
            add_facts=facts if facts else None,
            add_topics=extraction.topics[:5] if extraction.topics else None,
            add_decisions=extraction.decisions if extraction.decisions else None,
            add_context=context_entry,
        ))
        
        return patches
    
    def _generate_fact_patches(self, entity: MentionedEntity, extraction: UnifiedExtraction) -> list[PatchOperation]:
        """Generate patches for entities we learned facts about."""
        patches = []
        
        folder = self._get_entity_folder(entity, extraction)
        
        if not folder:
            return patches
        
        readme_path = folder / "README.md"
        if not readme_path.exists():
            return patches
        
        patches.append(PatchOperation(
            operation="patch",
            target_path=str(readme_path.relative_to(self.vault_root)),
            target_entity=entity.name,
            add_facts=entity.facts_about,
            add_context=f"- {extraction.date}: Mentioned in: {extraction.title}",
        ))
        
        return patches
    
    def _generate_participant_patches(self, participant: str, extraction: UnifiedExtraction) -> list[PatchOperation]:
        """Generate light-touch patches for participants."""
        patches = []
        
        # Skip myself
        if participant.lower() in ["myself", "jason", "jason vallery"]:
            return patches
        
        # Find person folder
        email = self._get_email_for_participant(participant, extraction)
        folder = self.entity_index.find_person(participant, email=email)
        if not folder:
            return patches
        
        readme_path = folder / "README.md"
        if not readme_path.exists():
            return patches
        
        # Just add context entry (no facts or topics)
        context_entry = f"- {extraction.date}: {extraction.title}"
        
        patches.append(PatchOperation(
            operation="patch",
            target_path=str(readme_path.relative_to(self.vault_root)),
            target_entity=participant,
            add_frontmatter={"last_contact": extraction.date},
            add_context=context_entry,
        ))
        
        return patches
    
    def _generate_company_patches(self, entity: MentionedEntity, extraction: UnifiedExtraction) -> list[PatchOperation]:
        """Generate patches for companies we learned facts about."""
        patches = []
        
        folder = self.entity_index.find_company(entity.name)
        if not folder:
            return patches
        
        readme_path = folder / "README.md"
        if not readme_path.exists():
            return patches
        
        patches.append(PatchOperation(
            operation="patch",
            target_path=str(readme_path.relative_to(self.vault_root)),
            target_entity=entity.name,
            add_facts=entity.facts_about,
            add_context=f"- {extraction.date}: {extraction.title}",
        ))
        
        return patches
    
    def _get_email_for_participant(self, name: str, extraction: UnifiedExtraction) -> Optional[str]:
        """Attempt to find an email address for a participant from contacts."""
        if not extraction.contacts:
            return None
        
        normalized_target = self.entity_index.normalize_name(name).lower()
        for contact in extraction.contacts:
            if not contact.email:
                continue
            contact_name = contact.name or ""
            normalized_contact = self.entity_index.normalize_name(contact_name).lower() if contact_name else ""
            if contact_name and normalized_contact == normalized_target:
                return contact.email
        if "@" in name:
            return name
        return None

    def _get_entity_folder(self, entity, extraction: Optional[UnifiedExtraction] = None) -> Optional[Path]:
        """Get folder path for an entity reference."""
        email = None
        if extraction and entity.entity_type == "person":
            email = self._get_email_for_participant(entity.name, extraction)
        if entity.entity_type == "person":
            return self.entity_index.find_person(entity.name, email=email)
        elif entity.entity_type == "company":
            return self.entity_index.find_company(entity.name)
        elif entity.entity_type == "project":
            return self.entity_index.find_project(entity.name)
        return None

    def _warn_duplicate(self, name: str, entity_type: str, plan: ChangePlan):
        """Warn when a similar entity already exists (merge guidance)."""
        similar: list[str] = []
        if entity_type == "person":
            similar = self.entity_index.find_similar_people(name)
        elif entity_type == "company":
            similar = self.entity_index.find_similar_companies(name)
        elif entity_type == "project":
            similar = self.entity_index.find_similar_projects(name)
        
        if similar:
            plan.warnings.append(
                f"Potential duplicate for '{name}': similar to {', '.join(similar[:2])} (consider merge)"
            )


class PatchCollector:
    """Collect and merge patches from multiple extractions.
    
    Used in parallel processing to:
    1. Collect all patches from concurrent extractions
    2. Group by target path
    3. Merge patches for same targets (dedup facts, combine context)
    4. Return a single merged ChangePlan for atomic apply
    """
    
    def __init__(self, dedupe_facts: bool = True, dedupe_tasks: bool = True, combine_context: bool = True):
        self.dedupe_facts = dedupe_facts
        self.dedupe_tasks = dedupe_tasks
        self.combine_context = combine_context
        
        # Collected data
        self._patches_by_target: dict[str, list[PatchOperation]] = {}
        self._meeting_notes: list[tuple[str, dict]] = []  # (path, context)
        self._source_files: list[str] = []
        self._warnings: list[str] = []
    
    @property
    def has_patches(self) -> bool:
        """Check if any patches have been collected."""
        return bool(self._patches_by_target)
    
    @property
    def patch_count(self) -> int:
        """Get total number of patches across all targets."""
        return sum(len(patches) for patches in self._patches_by_target.values())
    
    def collect(self, plan: ChangePlan):
        """Collect patches from a single ChangePlan."""
        self._source_files.append(plan.source_file)
        
        # Collect meeting note
        if plan.meeting_note_path and plan.meeting_note:
            self._meeting_notes.append((plan.meeting_note_path, plan.meeting_note))
        
        # Collect patches by target
        for patch in plan.patches:
            target = patch.target_path
            if target not in self._patches_by_target:
                self._patches_by_target[target] = []
            self._patches_by_target[target].append(patch)
        
        # Collect warnings
        self._warnings.extend(plan.warnings)
    
    def merge(self) -> ChangePlan:
        """Merge all collected patches into a single ChangePlan."""
        merged_patches: list[PatchOperation] = []
        
        for target_path, patches in self._patches_by_target.items():
            if len(patches) == 1:
                merged_patches.append(patches[0])
            else:
                merged = self._merge_patches_for_target(patches)
                merged_patches.append(merged)
        
        # Create merged plan
        plan = ChangePlan(
            source_file=", ".join(self._source_files[:3]) + (f" (+{len(self._source_files) - 3} more)" if len(self._source_files) > 3 else ""),
            patches=merged_patches,
            warnings=self._warnings,
        )
        
        # Set first meeting note (others are created separately)
        if self._meeting_notes:
            plan.meeting_note_path = self._meeting_notes[0][0]
            plan.meeting_note = self._meeting_notes[0][1]
        
        return plan
    
    def get_meeting_notes(self) -> list[tuple[str, dict]]:
        """Get all collected meeting notes for creation."""
        return self._meeting_notes
    
    def _merge_patches_for_target(self, patches: list[PatchOperation]) -> PatchOperation:
        """Merge multiple patches targeting the same file."""
        first = patches[0]
        
        merged = PatchOperation(
            operation="patch",
            target_path=first.target_path,
            target_entity=first.target_entity,
            add_frontmatter={},
            add_facts=[],
            add_topics=[],
            add_decisions=[],
            add_context="",
            add_tasks=[],
            add_wikilinks=[],
        )
        
        seen_facts: set[str] = set()
        seen_tasks: set[str] = set()
        context_parts: list[str] = []
        
        for patch in patches:
            # Merge frontmatter
            if patch.add_frontmatter:
                for key, value in patch.add_frontmatter.items():
                    # Later values overwrite (e.g., last_contact date)
                    merged.add_frontmatter[key] = value
            
            # Merge facts (dedup if enabled)
            if patch.add_facts:
                for fact in patch.add_facts:
                    fact_key = fact.lower().strip() if self.dedupe_facts else fact
                    if fact_key not in seen_facts:
                        merged.add_facts.append(fact)
                        seen_facts.add(fact_key)
            
            # Merge topics
            if patch.add_topics:
                for topic in patch.add_topics:
                    if topic not in merged.add_topics:
                        merged.add_topics.append(topic)
            
            # Merge decisions
            if patch.add_decisions:
                for decision in patch.add_decisions:
                    if decision not in merged.add_decisions:
                        merged.add_decisions.append(decision)
            
            # Merge context
            if patch.add_context:
                if self.combine_context:
                    if patch.add_context not in context_parts:
                        context_parts.append(patch.add_context)
                else:
                    merged.add_context = patch.add_context  # Last wins
            
            # Merge tasks (dedup by text if enabled)
            if patch.add_tasks:
                for task in patch.add_tasks:
                    task_key = task.get("text", "").lower().strip() if self.dedupe_tasks else str(task)
                    if task_key not in seen_tasks:
                        merged.add_tasks.append(task)
                        seen_tasks.add(task_key)
            
            # Merge wikilinks
            if patch.add_wikilinks:
                for link in patch.add_wikilinks:
                    if link not in merged.add_wikilinks:
                        merged.add_wikilinks.append(link)
        
        # Combine context parts
        if context_parts:
            merged.add_context = "\n".join(context_parts)
        
        return merged
