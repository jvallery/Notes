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
        
        Args:
            extraction: UnifiedExtraction with all extracted knowledge
        
        Returns:
            ChangePlan with all operations
        """
        plan = ChangePlan(source_file=extraction.source_file)
        
        # 1. Meeting note creation
        note_path, note_context = self._generate_meeting_note(extraction)
        if note_path:
            plan.meeting_note_path = note_path
            plan.meeting_note = note_context
        
        # 2. Primary entity patches
        if extraction.primary_entity:
            patches = self._generate_primary_patches(extraction)
            plan.patches.extend(patches)
        
        # 3. Entities with facts (we learned something)
        for entity in extraction.get_entities_with_facts():
            patches = self._generate_fact_patches(entity, extraction)
            plan.patches.extend(patches)
        
        # 4. Participant context updates
        for participant in extraction.participants:
            # Skip if already patched as primary or via facts
            patched_names = {p.target_entity for p in plan.patches}
            if participant not in patched_names:
                patches = self._generate_participant_patches(participant, extraction)
                plan.patches.extend(patches)
        
        # 5. Company patches (only if facts discovered)
        for entity in extraction.mentioned_entities:
            if entity.entity_type == "company" and entity.facts_about:
                company_lower = entity.name.lower()
                if company_lower not in self.SKIP_COMPANIES:
                    patches = self._generate_company_patches(entity, extraction)
                    plan.patches.extend(patches)
        
        return plan
    
    def _generate_meeting_note(self, extraction: UnifiedExtraction) -> tuple[Optional[str], Optional[dict]]:
        """Generate meeting note path and context."""
        
        # Determine destination folder
        if extraction.primary_entity:
            folder = self._get_entity_folder(extraction.primary_entity)
        else:
            # Default to first participant
            if extraction.participants:
                folder = self.entity_index.find_person(extraction.participants[0])
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
        
        folder = self._get_entity_folder(extraction.primary_entity)
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
        
        # Find entity folder
        folder = None
        if entity.entity_type == "person":
            folder = self.entity_index.find_person(entity.name)
        elif entity.entity_type == "company":
            folder = self.entity_index.find_company(entity.name)
        elif entity.entity_type == "project":
            folder = self.entity_index.find_project(entity.name)
        
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
        folder = self.entity_index.find_person(participant)
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
    
    def _get_entity_folder(self, entity) -> Optional[Path]:
        """Get folder path for an entity reference."""
        if entity.entity_type == "person":
            return self.entity_index.find_person(entity.name)
        elif entity.entity_type == "company":
            return self.entity_index.find_company(entity.name)
        elif entity.entity_type == "project":
            return self.entity_index.find_project(entity.name)
        return None
