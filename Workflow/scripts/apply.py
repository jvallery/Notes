#!/usr/bin/env python3
"""
Apply Phase: ChangePlan → File Updates

TRANSACTIONAL EXECUTION - NO AI CALLS
Pure deterministic execution with rollback on failure.

Flow:
1. Require clean git tree (content dirs only)
2. Validate all ChangePlans before touching disk
3. Backup all files to be modified
4. Execute ALL operations from changeplans
5. On failure: restore backups, delete new files
6. On success: archive sources, git commit batch
"""

import shutil
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

import click

sys.path.insert(0, str(Path(__file__).parent.parent))

from models.changeplan import ChangePlan, Operation, OperationType, PatchPrimitive
from scripts.utils import (
    vault_root,
    safe_read_text,
    atomic_write,
    backup_file,
    require_clean,
    is_git_repo,
    stage_content_dirs,
    commit,
    get_archive_path,
    safe_relative_path,
    render_note,
    validate_changeplan,
    validate_before_write,
)
from scripts.utils.patch_primitives import (
    upsert_frontmatter,
    append_under_heading,
    prepend_under_heading,
    ensure_wikilinks,
)
from scripts.utils.fs import sanitize_path


# validate_changeplan is imported from scripts.utils.validation


@dataclass
class TransactionalApply:
    """Executes ChangePlans with rollback on failure."""
    
    vault_root: Path
    run_id: str
    backup_dir: Path = field(init=False)
    created_files: list[Path] = field(default_factory=list)
    backed_up: dict[Path, Path] = field(default_factory=dict)
    modified_files: list[Path] = field(default_factory=list)
    moved_sources: list[tuple[Path, Path]] = field(default_factory=list)
    
    def __post_init__(self):
        self.backup_dir = self.vault_root / ".workflow_backups" / self.run_id
    
    def execute_batch(
        self,
        changeplans: list[ChangePlan],
        source_files: list[Path],
        allow_dirty: bool = False,
        allow_overwrite: bool = False,
    ) -> str:
        """
        Execute ALL changeplans atomically.
        
        Returns commit hash on success.
        Raises on failure (after rollback).
        """
        # 1. Require clean git tree
        require_clean(self.vault_root, allow_dirty=allow_dirty)
        
        # 2. Validate ALL changeplans before touching disk
        all_issues = []
        for plan in changeplans:
            issues = validate_changeplan(plan)
            if issues:
                all_issues.extend([f"{plan.source_file}: {issue}" for issue in issues])
        
        if all_issues:
            raise ValueError("Invalid changeplans:\n" + "\n".join(all_issues))
        
        try:
            # 3. Backup ALL files that will be modified
            for plan in changeplans:
                for op in plan.operations:
                    target = self.vault_root / op.path
                    if target.exists() and op.op in [OperationType.PATCH, OperationType.LINK]:
                        self._backup(target)
            
            # 4. Execute ALL operations
            for plan in changeplans:
                for op in plan.operations:
                    self._apply_operation(op, allow_overwrite=allow_overwrite)
            
            # 5. Archive ALL sources
            for source_file in source_files:
                if source_file.exists():
                    self._archive_source(source_file)
            
            # 6. Stage all changes and commit (if in git repo)
            commit_hash = ""
            if is_git_repo(self.vault_root):
                # Stage all content directories with -A to capture creates, modifies, deletes, renames
                stage_content_dirs(self.vault_root)
                
                # Build commit message
                summary = self._build_commit_message(changeplans)
                commit_hash = commit(self.vault_root, summary)
            
            # 7. Cleanup backups on success
            shutil.rmtree(self.backup_dir, ignore_errors=True)
            
            return commit_hash
            
        except Exception:
            self._rollback()
            raise
    
    def _backup(self, file_path: Path) -> None:
        """Create backup of file before modification."""
        if file_path not in self.backed_up:
            backup_path = backup_file(file_path, self.backup_dir, self.vault_root)
            self.backed_up[file_path] = backup_path
    
    def _apply_operation(self, op: Operation, allow_overwrite: bool = False) -> None:
        """Apply a single operation."""
        # Sanitize and resolve path safely
        sanitized_path = sanitize_path(op.path)
        rel = safe_relative_path(self.vault_root, sanitized_path)
        target = self.vault_root / rel
        
        if op.op == OperationType.CREATE:
            # Fail if exists unless override
            if target.exists() and not allow_overwrite:
                raise FileExistsError(f"Target exists for CREATE: {target}")
            
            # Render template with context
            context_dict = op.context.model_dump() if hasattr(op.context, 'model_dump') else op.context
            content = render_note(op.template, context_dict)
            
            # Validate before writing (standards compliance)
            note_type = context_dict.get("type") if isinstance(context_dict, dict) else getattr(op.context, "type", None)
            # Infer note_type from template name if not in context
            if not note_type:
                note_type = op.template.replace(".md.j2", "") if op.template else "unknown"
            
            issues = validate_before_write(target, content, note_type)
            if issues:
                raise ValueError(
                    f"Standards validation failed for {target.name}:\n"
                    + "\n".join(f"  - {i}" for i in issues)
                )
            
            # Ensure parent exists and write
            target.parent.mkdir(parents=True, exist_ok=True)
            atomic_write(target, content)
            self.created_files.append(target)
        
        elif op.op == OperationType.PATCH:
            if not target.exists():
                raise FileNotFoundError(f"Target not found for PATCH: {target}")
            
            content = safe_read_text(target)
            for patch in op.patches:
                content = self._apply_patch(content, patch)
            atomic_write(target, content)
            self.modified_files.append(target)
        
        elif op.op == OperationType.LINK:
            if not target.exists():
                raise FileNotFoundError(f"Target not found for LINK: {target}")
            
            content = safe_read_text(target)
            content = ensure_wikilinks(content, op.links)
            atomic_write(target, content)
            self.modified_files.append(target)
        
        elif op.op == OperationType.UPDATE_ENTITY:
            if not target.exists():
                raise FileNotFoundError(f"Target not found for UPDATE_ENTITY: {target}")
            
            content = safe_read_text(target)
            content = self._apply_entity_update(content, op.entity_update)
            atomic_write(target, content)
            self.modified_files.append(target)
    
    def _apply_entity_update(self, content: str, update) -> str:
        """Apply entity update by converting to patch primitives."""
        # Determine date field based on entity type
        date_field = "last_updated" if update.entity_type == "project" else "last_contact"
        
        # Update frontmatter with date
        from models.changeplan import FrontmatterPatch
        date_patches = [FrontmatterPatch(key=date_field, value=update.source_date)]
        content = upsert_frontmatter(content, date_patches)
        
        # Add context line if provided
        if update.context_line:
            content = prepend_under_heading(
                content,
                "## Recent Context",
                update.context_line
            )
        
        # Add new facts if provided
        if update.new_facts:
            for fact in update.new_facts:
                content = append_under_heading(
                    content,
                    "## Key Facts",
                    f"- {fact}\n"
                )
        
        return content
    
    def _apply_patch(self, content: str, spec) -> str:
        """Apply a single patch primitive."""
        if spec.primitive == PatchPrimitive.UPSERT_FRONTMATTER:
            return upsert_frontmatter(content, spec.frontmatter)
        elif spec.primitive == PatchPrimitive.APPEND_UNDER_HEADING:
            return append_under_heading(
                content,
                spec.heading.heading,
                spec.heading.content
            )
        elif spec.primitive == PatchPrimitive.PREPEND_UNDER_HEADING:
            return prepend_under_heading(
                content,
                spec.heading.heading,
                spec.heading.content
            )
        elif spec.primitive == PatchPrimitive.ENSURE_WIKILINKS:
            return ensure_wikilinks(content, spec.wikilinks)
        return content
    
    def _archive_source(self, source_file: Path) -> None:
        """Move source file to archive."""
        archive_path = get_archive_path(self.vault_root, source_file)
        archive_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(source_file), str(archive_path))
        self.moved_sources.append((archive_path, source_file))
    
    def _build_commit_message(self, changeplans: list[ChangePlan]) -> str:
        """Build git commit message."""
        sources = [Path(p.source_file).name for p in changeplans]
        if len(sources) <= 3:
            files = ", ".join(sources)
        else:
            files = f"{sources[0]}, {sources[1]}, ... (+{len(sources) - 2} more)"
        return f"[auto] Processed: {files}"
    
    def _rollback(self) -> None:
        """Restore backups and delete created files."""
        # Restore backed up files
        for original, backup in self.backed_up.items():
            try:
                shutil.copy2(backup, original)
            except Exception:
                pass  # Best effort
        
        # Delete created files
        for created in self.created_files:
            try:
                created.unlink(missing_ok=True)
            except Exception:
                pass  # Best effort
        
        # Undo archived source moves
        for archive_dst, original_src in self.moved_sources:
            try:
                if archive_dst.exists():
                    original_src.parent.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(archive_dst), str(original_src))
            except Exception:
                pass
        
        # Cleanup backup directory
        shutil.rmtree(self.backup_dir, ignore_errors=True)


def find_pending_changeplans() -> list[Path]:
    """Find changeplan files ready to apply."""
    extraction_dir = vault_root() / "Inbox" / "_extraction"
    
    if not extraction_dir.exists():
        return []
    
    return sorted(extraction_dir.glob("*.changeplan.json"))


def load_changeplan(path: Path) -> ChangePlan:
    """Load ChangePlan from JSON file."""
    content = safe_read_text(path)
    return ChangePlan.model_validate_json(content)


@click.command()
@click.option(
    "--changeplan",
    "changeplan_path",
    type=click.Path(exists=True),
    help="Apply single changeplan file",
)
@click.option("--all", "apply_all", is_flag=True, help="Apply all pending changeplans")
@click.option("--dry-run", is_flag=True, help="Show what would be applied without changes")
@click.option("--allow-dirty", is_flag=True, help="Allow apply with dirty git tree")
@click.option("--allow-overwrite", is_flag=True, help="Allow overwriting existing files")
@click.option("-v", "--verbose", is_flag=True, help="Show detailed output")
def main(
    changeplan_path: str | None,
    apply_all: bool,
    dry_run: bool,
    allow_dirty: bool,
    allow_overwrite: bool,
    verbose: bool,
):
    """Apply ChangePlans to update the vault."""
    
    click.echo(click.style("Apply Phase", fg="blue", bold=True))
    click.echo("=" * 40)
    
    # Find files to process
    if changeplan_path:
        files = [Path(changeplan_path)]
    elif apply_all:
        files = find_pending_changeplans()
    else:
        click.echo("Specify --changeplan or --all")
        return
    
    if not files:
        click.echo(click.style("No changeplans to apply.", fg="yellow"))
        return
    
    click.echo(f"Found {click.style(str(len(files)), bold=True)} changeplan(s)")
    
    # Load all changeplans
    changeplans = []
    source_files = []
    extraction_files = files.copy()
    
    for f in files:
        try:
            plan = load_changeplan(f)
            changeplans.append(plan)
            
            # Resolve source file path
            source_path = vault_root() / plan.source_file
            if source_path.exists():
                source_files.append(source_path)
            
            if verbose:
                click.echo(f"\n{f.name}:")
                for op in plan.operations:
                    click.echo(f"  {op.op.value}: {op.path}")
        except Exception as e:
            click.echo(click.style(f"Failed to load {f.name}: {e}", fg="red"))
            return
    
    if dry_run:
        click.echo("\n" + click.style("Dry run - no changes made", fg="yellow"))
        return
    
    # Execute transactionally
    run_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    executor = TransactionalApply(vault_root(), run_id)
    
    try:
        commit_hash = executor.execute_batch(
            changeplans,
            source_files,
            allow_dirty=allow_dirty,
            allow_overwrite=allow_overwrite,
        )
        
        click.echo("\n" + click.style("✓ Applied successfully", fg="green"))
        click.echo(f"  Created: {len(executor.created_files)} files")
        click.echo(f"  Modified: {len(executor.modified_files)} files")
        click.echo(f"  Archived: {len(executor.moved_sources)} sources")
        if commit_hash:
            click.echo(f"  Commit: {commit_hash[:8]}")
        
        # Cleanup changeplan and extraction files
        for f in extraction_files:
            try:
                f.unlink()
                # Also remove corresponding extraction file
                extraction_file = f.with_name(f.name.replace(".changeplan.json", ".extraction.json"))
                if extraction_file.exists():
                    extraction_file.unlink()
            except Exception:
                pass
        
    except ValueError as e:
        click.echo(click.style(f"\n✗ Validation failed: {e}", fg="red"))
        raise SystemExit(1)
    except Exception as e:
        click.echo(click.style(f"\n✗ Apply failed: {e}", fg="red"))
        click.echo("  Rollback completed - no changes made")
        if verbose:
            import traceback
            traceback.print_exc()
        raise SystemExit(1)


if __name__ == "__main__":
    main()
