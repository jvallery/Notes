#!/usr/bin/env python3
"""
Migration Executor: Phase 3 of migrate.py

Applies migration plan operations transactionally with rollback support.
Reuses TransactionalApply pattern from main pipeline.

Usage:
    python scripts/migration/executor.py -p migration-plan.json --dry-run
    python scripts/migration/executor.py -p migration-plan.json
"""

import shutil
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

import click

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from scripts.migration.models import MigrationPlan, MigrationOperation, MigrationOpType
from scripts.utils import (
    vault_root as get_vault_root,
    safe_read_text,
    atomic_write,
    backup_file,
    require_clean,
    is_git_repo,
    add_files,
    commit,
)
from scripts.utils.patch_primitives import upsert_frontmatter
from scripts.utils.templates import render_note


@dataclass
class MigrationExecutor:
    """Executes migration operations with transactional rollback."""
    
    vault_root: Path
    run_id: str
    backup_dir: Path = field(init=False)
    created_files: list[Path] = field(default_factory=list)
    modified_files: list[Path] = field(default_factory=list)
    backed_up: dict[Path, Path] = field(default_factory=dict)
    
    def __post_init__(self):
        self.backup_dir = self.vault_root / ".workflow_backups" / f"migration-{self.run_id}"
    
    def execute(
        self,
        plan: MigrationPlan,
        allow_dirty: bool = False,
        dry_run: bool = False,
    ) -> str:
        """
        Execute migration plan.
        
        Returns commit hash on success.
        Raises on failure (after rollback).
        """
        if dry_run:
            return self._dry_run(plan)
        
        # 1. Require clean git tree
        require_clean(self.vault_root, allow_dirty=allow_dirty)
        
        try:
            # 2. Backup files that will be modified
            for op in plan.operations:
                target = self.vault_root / op.path
                if target.exists() and op.op != MigrationOpType.CREATE_README:
                    self._backup(target)
            
            # 3. Execute all operations
            for op in plan.operations:
                self._apply_operation(op)
            
            # 4. Git commit
            commit_hash = ""
            if is_git_repo(self.vault_root):
                all_files = self.created_files + self.modified_files
                add_files(self.vault_root, all_files)
                
                summary = f"[migration] {plan.scope}: {len(plan.operations)} operations"
                commit_hash = commit(self.vault_root, summary)
            
            # 5. Cleanup backups on success
            shutil.rmtree(self.backup_dir, ignore_errors=True)
            
            return commit_hash
            
        except Exception:
            self._rollback()
            raise
    
    def _dry_run(self, plan: MigrationPlan) -> str:
        """Show what would be done without making changes."""
        click.echo("\n" + click.style("DRY RUN - No changes will be made", fg="yellow", bold=True))
        click.echo("-" * 40)
        
        for i, op in enumerate(plan.operations, 1):
            target = self.vault_root / op.path
            exists = target.exists()
            
            if op.op == MigrationOpType.CREATE_README:
                status = "SKIP (exists)" if exists else "CREATE"
                color = "yellow" if exists else "green"
                click.echo(f"{i}. [{click.style(status, fg=color)}] {op.path}")
                
            elif op.op in (MigrationOpType.FIX_FRONTMATTER, MigrationOpType.FIX_TYPE, MigrationOpType.ADD_MISSING_KEY):
                if not exists:
                    click.echo(f"{i}. [{click.style('SKIP (missing)', fg='red')}] {op.path}")
                else:
                    patches = op.patches or []
                    patch_desc = ", ".join(f"{p.get('key')}={p.get('value')}" for p in patches)
                    click.echo(f"{i}. [{click.style('PATCH', fg='cyan')}] {op.path}: {patch_desc}")
                    
            elif op.op == MigrationOpType.RENAME_FILE:
                click.echo(f"{i}. [{click.style('RENAME', fg='magenta')}] {op.path} -> {op.new_path}")
        
        click.echo("-" * 40)
        click.echo(f"Total operations: {len(plan.operations)}")
        return ""
    
    def _backup(self, file_path: Path) -> None:
        """Create backup of file before modification."""
        if file_path not in self.backed_up:
            backup_path = backup_file(file_path, self.backup_dir)
            self.backed_up[file_path] = backup_path
    
    def _apply_operation(self, op: MigrationOperation) -> None:
        """Apply a single migration operation."""
        target = self.vault_root / op.path
        
        if op.op == MigrationOpType.CREATE_README:
            if target.exists():
                # Skip if README already exists
                return
            
            # Render template
            content = render_note(op.template, op.context or {})
            
            # Ensure parent exists and write
            target.parent.mkdir(parents=True, exist_ok=True)
            atomic_write(target, content)
            self.created_files.append(target)
            
        elif op.op in (MigrationOpType.FIX_FRONTMATTER, MigrationOpType.FIX_TYPE, MigrationOpType.ADD_MISSING_KEY):
            if not target.exists():
                # Skip if file doesn't exist
                return
            
            content = safe_read_text(target)
            
            # Apply frontmatter patches
            patches = op.patches or []
            content = upsert_frontmatter(content, patches)
            
            atomic_write(target, content)
            self.modified_files.append(target)
            
        elif op.op == MigrationOpType.RENAME_FILE:
            if not target.exists() or not op.new_path:
                return
            
            new_target = self.vault_root / op.new_path
            new_target.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(target), str(new_target))
            self.modified_files.append(new_target)
    
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
        
        # Cleanup backup directory
        shutil.rmtree(self.backup_dir, ignore_errors=True)


@click.command()
@click.option("-p", "--plan", "plan_path", required=True, help="Migration plan JSON")
@click.option("--dry-run", is_flag=True, help="Show changes without applying")
@click.option("--allow-dirty", is_flag=True, help="Allow dirty git working tree")
@click.option("-v", "--verbose", is_flag=True, help="Show detailed output")
def main(plan_path: str, dry_run: bool, allow_dirty: bool, verbose: bool):
    """Execute migration plan."""
    
    click.echo(click.style("Migration Executor", fg="blue", bold=True))
    click.echo("=" * 40)
    
    # Load plan
    plan_file = Path(plan_path)
    if not plan_file.exists():
        click.echo(click.style(f"Plan not found: {plan_path}", fg="red"))
        raise SystemExit(1)
    
    plan = MigrationPlan.model_validate_json(plan_file.read_text())
    
    click.echo(f"Scope: {plan.scope}")
    click.echo(f"Operations: {len(plan.operations)}")
    
    # Execute
    vault = get_vault_root()
    run_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    executor = MigrationExecutor(vault, run_id)
    
    try:
        commit_hash = executor.execute(plan, allow_dirty=allow_dirty, dry_run=dry_run)
        
        if not dry_run:
            click.echo("\n" + click.style("✓ Migration completed", fg="green"))
            click.echo(f"  Created: {len(executor.created_files)} files")
            click.echo(f"  Modified: {len(executor.modified_files)} files")
            if commit_hash:
                click.echo(f"  Commit: {commit_hash[:8]}")
        
    except RuntimeError as e:
        click.echo(click.style(f"\n✗ Migration failed: {e}", fg="red"))
        click.echo("  Rollback completed - no changes made")
        raise SystemExit(1)
    except Exception as e:
        click.echo(click.style(f"\n✗ Error: {e}", fg="red"))
        click.echo("  Rollback completed - no changes made")
        if verbose:
            import traceback
            traceback.print_exc()
        raise SystemExit(1)


if __name__ == "__main__":
    main()
