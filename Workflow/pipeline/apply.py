"""
Transactional Apply - Execute change plans atomically.

Features:
- Backup before modification
- Rollback on failure
- Archive sources after success
- Git commit with summary
"""

import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).parent.parent))

from .patch import ChangePlan, PatchOperation, ManifestPatch


class ApplyResult:
    """Result of applying a change plan."""
    
    def __init__(self):
        self.success = True
        self.files_created: list[str] = []
        self.files_modified: list[str] = []
        self.files_archived: list[str] = []
        self.errors: list[str] = []
    
    def __str__(self):
        if self.success:
            return f"Applied: {len(self.files_created)} created, {len(self.files_modified)} modified"
        else:
            return f"Failed: {', '.join(self.errors)}"


class TransactionalApply:
    """Apply change plans transactionally.
    
    Either all changes succeed (git commit) or all fail (rollback).
    """
    
    def __init__(self, vault_root: Path, dry_run: bool = False):
        self.vault_root = vault_root
        self.dry_run = dry_run
        self.backup_dir = vault_root / ".workflow_backups" / datetime.now().strftime("%Y%m%d_%H%M%S")
        self._backed_up: dict[Path, Path] = {}
        self._created: list[Path] = []
    
    def apply(self, plan: ChangePlan, source_path: Optional[Path] = None) -> ApplyResult:
        """Apply a change plan.
        
        Args:
            plan: ChangePlan to apply
            source_path: Original source file (for archiving)
        
        Returns:
            ApplyResult with details
        """
        result = ApplyResult()
        
        if self.dry_run:
            return self._dry_run_apply(plan, result)
        
        try:
            # 1. Create meeting note
            if plan.meeting_note_path and plan.meeting_note:
                self._create_meeting_note(plan, result)
            
            # 2. Apply patches
            for patch in plan.patches:
                self._apply_patch(patch, result)
            
            # 3. Apply manifest patches (aliases and acronyms)
            for manifest_patch in plan.manifest_patches:
                self._apply_manifest_patch(manifest_patch, result)
            
            # 4. Archive source
            if source_path and source_path.exists():
                self._archive_source(source_path, result)
            
            # 5. Cleanup backups on success
            if self.backup_dir.exists():
                shutil.rmtree(self.backup_dir)
            
            return result
            
        except Exception as e:
            result.success = False
            result.errors.append(str(e))
            self._rollback()
            return result
    
    def _dry_run_apply(self, plan: ChangePlan, result: ApplyResult) -> ApplyResult:
        """Simulate applying a plan (dry run)."""
        
        if plan.meeting_note_path:
            result.files_created.append(plan.meeting_note_path)
        
        for patch in plan.patches:
            result.files_modified.append(patch.target_path)
        
        for manifest_patch in plan.manifest_patches:
            result.files_modified.append(manifest_patch.manifest_path)
        
        return result
    
    def _create_meeting_note(self, plan: ChangePlan, result: ApplyResult):
        """Create the meeting note from plan."""
        from jinja2 import Environment, FileSystemLoader
        import re
        import os
        
        note_path = self.vault_root / plan.meeting_note_path
        
        # Skip if exists
        if note_path.exists():
            return
        
        # Ensure parent directory exists
        note_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Load template
        templates_dir = self.vault_root / "Workflow" / "templates"
        env = Environment(loader=FileSystemLoader(str(templates_dir)))
        
        # Add custom filters
        def slugify(text):
            """Convert text to slug format for tags."""
            if not text:
                return ""
            text = text.lower()
            text = re.sub(r'[^\w\s-]', '', text)
            text = re.sub(r'[\s_]+', '-', text)
            return text.strip('-')
        
        def strip_extension(path):
            """Remove file extension from path."""
            if not path:
                return ""
            return os.path.splitext(str(path))[0]
        
        def basename(path):
            """Get basename of path."""
            if not path:
                return ""
            return os.path.basename(str(path))
        
        env.filters['slugify'] = slugify
        env.filters['strip_extension'] = strip_extension
        env.filters['basename'] = basename
        
        # Select template based on note type
        note_type = plan.meeting_note.get("type", "people")
        template_name = f"{note_type}.md.j2"
        
        try:
            template = env.get_template(template_name)
        except Exception:
            template = env.get_template("people.md.j2")  # Fallback
        
        # Render
        content = template.render(**plan.meeting_note)
        
        # Write
        note_path.write_text(content)
        self._created.append(note_path)
        result.files_created.append(plan.meeting_note_path)
    
    def _apply_patch(self, patch: PatchOperation, result: ApplyResult):
        """Apply a single patch operation."""
        target = self.vault_root / patch.target_path
        
        if not target.exists():
            return
        
        # Backup
        self._backup(target)
        
        # Read current content
        content = target.read_text()
        
        # Apply patch primitives
        from scripts.utils.patch_primitives import (
            upsert_frontmatter, 
            append_under_heading,
            ensure_wikilinks
        )
        
        # Frontmatter updates - convert dict to list of {key, value} patches
        if patch.add_frontmatter:
            fm_patches = [{"key": k, "value": v} for k, v in patch.add_frontmatter.items()]
            content = upsert_frontmatter(content, fm_patches)
        
        # Add facts under ## Key Facts
        if patch.add_facts:
            for fact in patch.add_facts:
                if fact not in content:
                    content = append_under_heading(content, "## Key Facts", f"- {fact}")
        
        # Add topics under ## Topics
        if patch.add_topics:
            for topic in patch.add_topics:
                if topic not in content:
                    content = append_under_heading(content, "## Topics", f"- {topic}")
        
        # Add decisions under ## Key Decisions
        if patch.add_decisions:
            for decision in patch.add_decisions:
                if decision not in content:
                    content = append_under_heading(content, "## Key Decisions", f"- {decision}")
        
        # Add context under ## Recent Context
        if patch.add_context:
            if patch.add_context not in content:
                content = append_under_heading(content, "## Recent Context", patch.add_context)
        
        # Add wikilinks
        if patch.add_wikilinks:
            content = ensure_wikilinks(content, patch.add_wikilinks)
        
        # Write
        self._atomic_write(target, content)
        result.files_modified.append(patch.target_path)
    
    def _apply_manifest_patch(self, patch: ManifestPatch, result: ApplyResult):
        """Apply a manifest patch (add aliases or acronyms).
        
        For People manifest: Adds aliases to the Aliases column
        For Projects manifest: Adds acronym/definition to appropriate columns
        """
        target = self.vault_root / patch.manifest_path
        
        if not target.exists():
            return
        
        # Backup
        self._backup(target)
        
        # Read current content
        content = target.read_text()
        lines = content.split("\n")
        
        if patch.manifest_type == "people" and patch.person_name:
            # Find the row for this person and update Aliases column
            lines = self._update_people_manifest_row(lines, patch.person_name, patch.aliases_to_add)
        elif patch.manifest_type == "projects" and patch.project_name:
            # Find or add project row with acronym/definition
            lines = self._update_projects_manifest_row(lines, patch.project_name, patch.acronym, patch.definition)
        
        # Write
        new_content = "\n".join(lines)
        self._atomic_write(target, new_content)
        result.files_modified.append(patch.manifest_path)
    
    def _update_people_manifest_row(self, lines: list[str], person_name: str, aliases_to_add: list[str]) -> list[str]:
        """Update a row in the People manifest to add aliases."""
        # Find header row to get column indices
        header_idx = None
        alias_col_idx = None
        
        for i, line in enumerate(lines):
            if line.strip().startswith("|") and "Name" in line and "Role" in line:
                header_idx = i
                cols = [c.strip() for c in line.split("|")]
                for j, col in enumerate(cols):
                    if "Alias" in col:
                        alias_col_idx = j
                        break
                break
        
        if header_idx is None or alias_col_idx is None:
            return lines  # Can't find manifest structure
        
        # Find the person's row
        person_name_lower = person_name.lower()
        for i in range(header_idx + 2, len(lines)):  # Skip header and separator
            line = lines[i]
            if not line.strip().startswith("|"):
                continue
            
            cols = line.split("|")
            if len(cols) <= alias_col_idx:
                continue
            
            # Check if this row matches the person
            name_col = cols[1].strip() if len(cols) > 1 else ""
            if name_col.lower() == person_name_lower or person_name_lower in name_col.lower():
                # Found the person - update aliases
                current_aliases = cols[alias_col_idx].strip() if alias_col_idx < len(cols) else ""
                
                # Parse existing aliases
                existing = set(a.strip() for a in current_aliases.split(",") if a.strip())
                
                # Add new aliases
                existing.update(aliases_to_add)
                
                # Update the column
                new_aliases = ", ".join(sorted(existing))
                cols[alias_col_idx] = f" {new_aliases} "
                
                lines[i] = "|".join(cols)
                break
        
        return lines
    
    def _update_projects_manifest_row(self, lines: list[str], project_name: str, acronym: str, definition: str) -> list[str]:
        """Update or add a row in the Projects manifest with acronym/definition."""
        # Find header row to get column indices
        header_idx = None
        acronym_col_idx = None
        definition_col_idx = None
        
        for i, line in enumerate(lines):
            if line.strip().startswith("|") and "Name" in line:
                header_idx = i
                cols = [c.strip() for c in line.split("|")]
                for j, col in enumerate(cols):
                    if "Acronym" in col:
                        acronym_col_idx = j
                    if "Definition" in col:
                        definition_col_idx = j
                break
        
        if header_idx is None:
            return lines  # Can't find manifest structure
        
        # Find the project's row
        project_name_lower = project_name.lower()
        for i in range(header_idx + 2, len(lines)):  # Skip header and separator
            line = lines[i]
            if not line.strip().startswith("|"):
                continue
            
            cols = line.split("|")
            if len(cols) < 2:
                continue
            
            # Check if this row matches the project
            name_col = cols[1].strip() if len(cols) > 1 else ""
            if name_col.lower() == project_name_lower or project_name_lower in name_col.lower():
                # Found the project - update acronym and definition
                if acronym_col_idx and acronym_col_idx < len(cols):
                    current = cols[acronym_col_idx].strip()
                    if not current or current == "-":
                        cols[acronym_col_idx] = f" {acronym} "
                
                if definition_col_idx and definition_col_idx < len(cols):
                    current = cols[definition_col_idx].strip()
                    if not current or current == "-":
                        cols[definition_col_idx] = f" {definition} "
                
                lines[i] = "|".join(cols)
                return lines
        
        # Project not found - could add a new row, but for now just skip
        # (would need to know all column values to add properly)
        return lines

    def _archive_source(self, source_path: Path, result: ApplyResult):
        """Archive source file to Sources directory."""
        from .envelope import ContentType
        
        try:
            relative = source_path.relative_to(self.vault_root)
        except ValueError:
            relative = None

        # Already archived; no-op but record for reporting
        if relative and "Sources" in relative.parts:
            result.files_archived.append(str(relative))
            return

        # Determine archive location
        year = datetime.now().strftime("%Y")
        
        # Detect content type from path
        if "Email" in source_path.parts:
            archive_dir = self.vault_root / "Sources" / "Email" / year
        elif "Transcripts" in source_path.parts:
            archive_dir = self.vault_root / "Sources" / "Transcripts" / year
        else:
            archive_dir = self.vault_root / "Sources" / "Documents" / year
        
        archive_dir.mkdir(parents=True, exist_ok=True)
        archive_path = archive_dir / source_path.name
        
        # Move to archive
        shutil.move(str(source_path), str(archive_path))
        result.files_archived.append(str(archive_path.relative_to(self.vault_root)))
    
    def _backup(self, path: Path):
        """Backup a file before modification."""
        if path in self._backed_up:
            return
        
        self.backup_dir.mkdir(parents=True, exist_ok=True)
        backup_path = self.backup_dir / path.name
        shutil.copy2(path, backup_path)
        self._backed_up[path] = backup_path
    
    def _atomic_write(self, path: Path, content: str):
        """Write file atomically (write temp, then rename)."""
        temp_path = path.with_suffix(path.suffix + ".tmp")
        temp_path.write_text(content)
        temp_path.rename(path)
    
    def _rollback(self):
        """Rollback all changes on failure."""
        # Restore backups
        for original, backup in self._backed_up.items():
            if backup.exists():
                shutil.copy2(backup, original)
        
        # Delete created files
        for created in self._created:
            if created.exists():
                created.unlink()
        
        # Cleanup backup directory
        if self.backup_dir.exists():
            shutil.rmtree(self.backup_dir)
