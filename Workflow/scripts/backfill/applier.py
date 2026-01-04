"""
Backfill Applier: Apply README updates transactionally.

This module takes a BackfillPlan and applies all README updates atomically.
Uses the same transactional pattern as the main apply phase:

1. Require clean git tree
2. Backup all files to be modified
3. Apply all patches
4. On failure: rollback all changes
5. On success: git commit
"""

import shutil
import subprocess
from datetime import datetime
from pathlib import Path

from . import (
    BackfillPlan,
    ReadmeUpdate,
    ApplyResult,
    AggregatedPersonDetails,
    AggregatedProjectDetails,
    AggregatedCustomerDetails,
    ExtractedTask,
    Collaborator,
)
from .aggregator import format_recent_context_section
from utils.config import vault_root
from utils.frontmatter import parse_frontmatter, render_frontmatter


# ─────────────────────────────────────────────────────────────────────────────
# Git Operations
# ─────────────────────────────────────────────────────────────────────────────

# Paths to check for git cleanliness (ignore .obsidian/, Workflow/, etc.)
CHECKED_PATHS = ["VAST/", "Personal/"]


def git_is_clean(vault: Path, paths: list[str] | None = None) -> bool:
    """Check if git working directory is clean for specified paths."""
    if paths is None:
        paths = CHECKED_PATHS
    
    try:
        # Check for uncommitted changes in content directories
        result = subprocess.run(
            ["git", "status", "--porcelain", "--"] + paths,
            cwd=vault,
            capture_output=True,
            text=True,
        )
        return result.returncode == 0 and not result.stdout.strip()
    except Exception:
        # If git fails, assume not clean
        return False


def git_commit(vault: Path, message: str, paths: list[str] | None = None) -> str | None:
    """Commit changes and return commit hash."""
    try:
        # Stage specific paths or all
        if paths:
            subprocess.run(["git", "add", "--"] + paths, cwd=vault, check=True)
        else:
            subprocess.run(["git", "add", "-A"], cwd=vault, check=True)
        
        # Commit
        result = subprocess.run(
            ["git", "commit", "-m", message],
            cwd=vault,
            capture_output=True,
            text=True,
        )
        
        if result.returncode == 0:
            # Get commit hash
            hash_result = subprocess.run(
                ["git", "rev-parse", "--short", "HEAD"],
                cwd=vault,
                capture_output=True,
                text=True,
            )
            return hash_result.stdout.strip()
        return None
    except Exception:
        return None


# ─────────────────────────────────────────────────────────────────────────────
# Patch Operations
# ─────────────────────────────────────────────────────────────────────────────


def upsert_frontmatter_field(content: str, key: str, value: str) -> str:
    """Update or insert a frontmatter field."""
    fm, body = parse_frontmatter(content)
    if fm is None:
        fm = {}
    fm[key] = value
    return render_frontmatter(fm) + body


def append_or_replace_section(content: str, heading: str, new_content: str) -> str:
    """
    Append to or replace content under a heading.
    
    If heading exists, replaces its content.
    If heading doesn't exist, adds it before ## Related or at end.
    """
    lines = content.split("\n")
    heading_level = heading.count("#")
    heading_text = heading.strip("# ").strip()
    
    result: list[str] = []
    in_section = False
    section_replaced = False
    i = 0
    
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Check if we're at the target heading
        if stripped.startswith("#" * heading_level + " ") and heading_text in stripped:
            result.append(line)
            result.append("")
            result.append(new_content)
            result.append("")
            in_section = True
            section_replaced = True
            i += 1
            continue
        
        # If in section, skip until next heading of same or higher level
        if in_section:
            if stripped.startswith("#"):
                # Count heading level
                level = len(stripped) - len(stripped.lstrip("#"))
                if level <= heading_level:
                    # End of section
                    in_section = False
                    result.append(line)
            # Skip content in section
            i += 1
            continue
        
        result.append(line)
        i += 1
    
    # If section wasn't found, add it
    if not section_replaced:
        # Try to insert before ## Related
        insert_idx = None
        for idx, line in enumerate(result):
            if line.strip().startswith("## Related"):
                insert_idx = idx
                break
        
        new_section = [heading, "", new_content, ""]
        
        if insert_idx is not None:
            result = result[:insert_idx] + new_section + result[insert_idx:]
        else:
            # Add at end
            if result and result[-1].strip():
                result.append("")
            result.extend(new_section)
    
    return "\n".join(result)


# ─────────────────────────────────────────────────────────────────────────────
# Rich Section Formatters
# ─────────────────────────────────────────────────────────────────────────────


def format_profile_section(profile: AggregatedPersonDetails) -> str:
    """Format person profile as markdown."""
    lines: list[str] = []
    
    if profile.role or profile.company:
        role_line = ""
        if profile.role:
            role_line = profile.role
        if profile.company:
            role_line += f" at {profile.company}" if role_line else profile.company
        if profile.department:
            role_line += f" ({profile.department})"
        if role_line:
            lines.append(f"**Role**: {role_line}")
    
    if profile.location:
        lines.append(f"**Location**: {profile.location}")
    
    if profile.relationship:
        lines.append(f"**Relationship**: {profile.relationship}")
    
    if profile.background:
        lines.append("")
        lines.append("**Background**:")
        for bg in profile.background[:3]:  # Limit to top 3
            lines.append(f"- {bg}")
    
    return "\n".join(lines) if lines else ""


def format_contact_section(profile: AggregatedPersonDetails) -> str:
    """Format contact info as markdown."""
    lines: list[str] = []
    
    if profile.email:
        lines.append(f"- **Email**: {profile.email}")
    if profile.phone:
        lines.append(f"- **Phone**: {profile.phone}")
    if profile.linkedin:
        lines.append(f"- **LinkedIn**: {profile.linkedin}")
    
    return "\n".join(lines) if lines else ""


def format_tasks_section(tasks: list[ExtractedTask]) -> str:
    """Format tasks as Obsidian Tasks plugin format."""
    lines: list[str] = []
    
    for task in tasks[:10]:  # Limit to 10 tasks
        # Build task line: - [ ] text @owner 📅 due
        task_line = f"- [ ] {task.text}"
        
        if task.owner and task.owner.lower() != "myself":
            task_line += f" @{task.owner}"
        
        if task.due:
            task_line += f" 📅 {task.due}"
        
        lines.append(task_line)
    
    return "\n".join(lines) if lines else ""


def format_key_facts_section(facts: list[str]) -> str:
    """Format key facts as bullet list."""
    lines = [f"- {fact}" for fact in facts[:10]]
    return "\n".join(lines) if lines else ""


def format_topics_section(topics: list[str]) -> str:
    """Format topics as inline tags/badges."""
    if not topics:
        return ""
    # Format as a comma-separated list
    return ", ".join(topics[:15])


def format_project_status_section(profile: AggregatedProjectDetails) -> str:
    """Format project status as markdown table."""
    lines: list[str] = []
    lines.append("| Field | Value |")
    lines.append("|-------|-------|")
    lines.append(f"| **Status** | {profile.status or '_Unknown_'} |")
    lines.append(f"| **Owner** | {profile.owner or '_Unknown_'} |")
    
    return "\n".join(lines)


def format_project_overview_section(profile: AggregatedProjectDetails) -> str:
    """Format project overview (description)."""
    return profile.description or "_Brief description of this project..._"


def format_blockers_section(blockers: list[str]) -> str:
    """Format blockers as bullet list."""
    if not blockers:
        return "_No known blockers._"
    lines = [f"- ❌ {b}" for b in blockers[:5]]
    return "\n".join(lines)


def format_next_steps_section(next_steps: list[str]) -> str:
    """Format next steps as task list."""
    if not next_steps:
        return "_No next steps defined._"
    lines = [f"- [ ] {s}" for s in next_steps[:10]]
    return "\n".join(lines)


def format_collaborators_section(collaborators: list[Collaborator]) -> str:
    """Format collaborators as markdown table."""
    if not collaborators:
        return "_Who is working on this?_\n\n| Person | Role | Company |\n|--------|------|---------|"
    
    lines: list[str] = []
    lines.append("| Person | Role | Company |")
    lines.append("|--------|------|---------|")
    for c in collaborators:
        lines.append(f"| [[{c.name}]] | {c.role or ''} | {c.company or ''} |")
    
    return "\n".join(lines)


def format_decisions_section(decisions: list[str]) -> str:
    """Format decisions as bullet list."""
    if not decisions:
        return ""
    lines = [f"- ✅ {d}" for d in decisions[:10]]
    return "\n".join(lines)


def format_linked_entities_section(entities: list[str], entity_type: str) -> str:
    """Format linked entities as wikilinks."""
    if not entities:
        return f"_No linked {entity_type}._"
    lines = [f"- [[{e}]]" for e in entities]
    return "\n".join(lines)


def format_customer_status_section(profile: AggregatedCustomerDetails) -> str:
    """Format customer status as markdown table."""
    lines: list[str] = []
    lines.append("| Field | Value |")
    lines.append("|-------|-------|")
    lines.append(f"| **Status** | {profile.status or '_Unknown_'} |")
    lines.append(f"| **Industry** | {profile.industry or '_Unknown_'} |")
    
    return "\n".join(lines)


def format_contacts_section(contacts: list[str]) -> str:
    """Format key contacts as wikilinks."""
    if not contacts:
        return "_No key contacts identified._"
    lines = [f"- [[{c}]]" for c in contacts]
    return "\n".join(lines)


def format_opportunities_section(opportunities: list[str]) -> str:
    """Format opportunities as bullet list."""
    if not opportunities:
        return "_No active opportunities._"
    lines = [f"- {o}" for o in opportunities[:10]]
    return "\n".join(lines)


def apply_readme_update(vault: Path, update: ReadmeUpdate) -> None:
    """Apply a single README update with rich profile data."""
    readme_path = vault / update.readme_path
    
    if not readme_path.exists():
        raise FileNotFoundError(f"README not found: {update.readme_path}")
    
    content = readme_path.read_text()
    
    # Update last_contact in frontmatter
    if update.last_contact:
        content = upsert_frontmatter_field(content, "last_contact", update.last_contact)
    
    # ─────────────────────────────────────────────────────────────────────────
    # Entity-type-specific sections
    # ─────────────────────────────────────────────────────────────────────────
    
    # For PEOPLE entities - personal profile data
    if update.entity_type == "people" and update.profile:
        # Profile section (role, location, relationship, background)
        profile_content = format_profile_section(update.profile)
        if profile_content:
            content = append_or_replace_section(content, "## Profile", profile_content)
        
        # Contact section (email, phone, linkedin)
        contact_content = format_contact_section(update.profile)
        if contact_content:
            content = append_or_replace_section(content, "## Contact", contact_content)
    
    # For PROJECT entities - project status and collaborators
    if update.entity_type == "projects" and update.project_profile:
        # Overview section
        overview_content = format_project_overview_section(update.project_profile)
        if overview_content:
            content = append_or_replace_section(content, "## Overview", overview_content)
        
        # Status section (table with status, priority, target, owner)
        status_content = format_project_status_section(update.project_profile)
        if status_content:
            content = append_or_replace_section(content, "## Status", status_content)
        
        # Blockers section
        blockers_content = format_blockers_section(update.project_profile.blockers)
        if blockers_content:
            content = append_or_replace_section(content, "## Blockers", blockers_content)
        
        # Next Steps section
        next_steps_content = format_next_steps_section(update.project_profile.next_steps)
        if next_steps_content:
            content = append_or_replace_section(content, "## Next Steps", next_steps_content)
    
    # For CUSTOMER/ACCOUNT entities - relationship and contacts
    if update.entity_type == "accounts" and update.customer_profile:
        # Account Status section
        status_content = format_customer_status_section(update.customer_profile)
        if status_content:
            content = append_or_replace_section(content, "## Account Status", status_content)
        
        # Key Contacts section
        contacts_content = format_contacts_section(update.customer_profile.key_contacts)
        if contacts_content:
            content = append_or_replace_section(content, "## Key Contacts", contacts_content)
        
        # Opportunities section
        opportunities_content = format_opportunities_section(update.customer_profile.opportunities)
        if opportunities_content:
            content = append_or_replace_section(content, "## Opportunities", opportunities_content)
        
        # Blockers section
        blockers_content = format_blockers_section(update.customer_profile.blockers)
        if blockers_content:
            content = append_or_replace_section(content, "## Blockers", blockers_content)
    
    # ─────────────────────────────────────────────────────────────────────────
    # Cross-linked sections (all entity types)
    # ─────────────────────────────────────────────────────────────────────────
    
    # Collaborators section (for projects)
    if update.collaborators:
        collaborators_content = format_collaborators_section(update.collaborators)
        if collaborators_content:
            content = append_or_replace_section(content, "## Collaborators", collaborators_content)
    
    # Linked Projects section
    if update.linked_projects:
        projects_content = format_linked_entities_section(update.linked_projects, "project")
        if projects_content:
            content = append_or_replace_section(content, "## Related Projects", projects_content)
    
    # Linked Customers section
    if update.linked_customers:
        customers_content = format_linked_entities_section(update.linked_customers, "customer")
        if customers_content:
            content = append_or_replace_section(content, "## Related Customers", customers_content)
    
    # Linked People section (for projects/customers)
    if update.linked_people:
        people_content = format_linked_entities_section(update.linked_people, "person")
        if people_content:
            content = append_or_replace_section(content, "## Related People", people_content)
    
    # ─────────────────────────────────────────────────────────────────────────
    # Common sections (all entity types)
    # ─────────────────────────────────────────────────────────────────────────
    
    # Open tasks section
    if update.open_tasks:
        tasks_content = format_tasks_section(update.open_tasks)
        if tasks_content:
            content = append_or_replace_section(content, "## Open Tasks", tasks_content)
    
    # Key Decisions section
    if update.decisions:
        decisions_content = format_decisions_section(update.decisions)
        if decisions_content:
            content = append_or_replace_section(content, "## Key Decisions", decisions_content)
    
    # Key facts section
    if update.key_facts:
        facts_content = format_key_facts_section(update.key_facts)
        if facts_content:
            content = append_or_replace_section(content, "## Key Facts", facts_content)
    
    # Topics section (things we've discussed)
    if update.topics:
        topics_content = format_topics_section(update.topics)
        if topics_content:
            content = append_or_replace_section(content, "## Topics", topics_content)
    
    # Recent Context section (meeting summaries with wikilinks)
    if update.context_entries:
        context_content = format_recent_context_section(update.context_entries)
        content = append_or_replace_section(content, "## Recent Context", context_content)
    
    # Write atomically
    readme_path.write_text(content)


# ─────────────────────────────────────────────────────────────────────────────
# Transactional Applier
# ─────────────────────────────────────────────────────────────────────────────


class TransactionalBackfillApply:
    """
    Apply backfill plan transactionally with rollback support.
    
    Usage:
        applier = TransactionalBackfillApply(vault)
        result = applier.execute(plan, dry_run=False)
    """
    
    def __init__(self, vault: Path | None = None):
        self.vault = vault or vault_root()
        self.run_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.backup_dir = self.vault / ".workflow_backups" / f"backfill_{self.run_id}"
        self.backed_up: dict[Path, Path] = {}
        self.modified_files: list[Path] = []
    
    def _backup(self, file_path: Path) -> None:
        """Create backup of a file."""
        if file_path in self.backed_up:
            return
        
        self.backup_dir.mkdir(parents=True, exist_ok=True)
        
        # Create backup with same relative structure
        relative = file_path.relative_to(self.vault)
        backup_path = self.backup_dir / relative
        backup_path.parent.mkdir(parents=True, exist_ok=True)
        
        shutil.copy2(file_path, backup_path)
        self.backed_up[file_path] = backup_path
    
    def _rollback(self) -> None:
        """Restore all backups."""
        for original, backup in self.backed_up.items():
            if backup.exists():
                shutil.copy2(backup, original)
        
        # Cleanup backup directory
        if self.backup_dir.exists():
            shutil.rmtree(self.backup_dir)
    
    def _cleanup_backups(self) -> None:
        """Remove backups after successful apply."""
        if self.backup_dir.exists():
            shutil.rmtree(self.backup_dir)
    
    def execute(
        self,
        plan: BackfillPlan,
        dry_run: bool = False,
        allow_dirty: bool = False,
    ) -> ApplyResult:
        """
        Execute the backfill plan.
        
        Args:
            plan: BackfillPlan with all README updates
            dry_run: If True, only preview changes without applying
            allow_dirty: If True, skip git clean check
            
        Returns:
            ApplyResult with execution status
        """
        errors: list[str] = []
        updated_count = 0
        skipped_count = 0
        
        # Check git cleanliness
        if not allow_dirty and not dry_run:
            if not git_is_clean(self.vault):
                return ApplyResult(
                    success=False,
                    applied_at=datetime.now(),
                    errors=["Git working directory has uncommitted changes. Use --allow-dirty to override."],
                    dry_run=dry_run,
                )
        
        if dry_run:
            print("\n=== DRY RUN MODE ===\n")
        
        try:
            for update in plan.updates:
                readme_path = self.vault / update.readme_path
                
                if not readme_path.exists():
                    errors.append(f"README not found: {update.readme_path}")
                    skipped_count += 1
                    continue
                
                if not update.context_entries:
                    skipped_count += 1
                    continue
                
                if dry_run:
                    print(f"Would update: {update.readme_path}")
                    print(f"  last_contact: {update.last_contact}")
                    print(f"  entries: {len(update.context_entries)}")
                    updated_count += 1
                    continue
                
                # Backup before modifying
                self._backup(readme_path)
                
                try:
                    apply_readme_update(self.vault, update)
                    self.modified_files.append(readme_path)
                    updated_count += 1
                    print(f"Updated: {update.readme_path} ({len(update.context_entries)} entries)")
                except Exception as e:
                    errors.append(f"Failed to update {update.readme_path}: {e}")
                    raise  # Trigger rollback
            
            # If we got here without exception, commit
            git_hash = None
            if not dry_run and updated_count > 0:
                commit_msg = f"[backfill] Updated {updated_count} READMEs with historical context"
                git_hash = git_commit(
                    self.vault,
                    commit_msg,
                    [str(f.relative_to(self.vault)) for f in self.modified_files],
                )
                if git_hash:
                    print(f"\nCommitted: {git_hash}")
                
                # Cleanup backups on success
                self._cleanup_backups()
            
            return ApplyResult(
                success=len(errors) == 0,
                applied_at=datetime.now(),
                readmes_updated=updated_count,
                readmes_skipped=skipped_count,
                errors=errors,
                git_commit=git_hash,
                dry_run=dry_run,
            )
        
        except Exception as e:
            # Rollback on any failure
            print(f"\n!!! Error: {e}")
            print("Rolling back changes...")
            self._rollback()
            
            return ApplyResult(
                success=False,
                applied_at=datetime.now(),
                readmes_updated=0,
                readmes_skipped=skipped_count,
                errors=errors + [str(e)],
                dry_run=dry_run,
            )


# ─────────────────────────────────────────────────────────────────────────────
# CLI Integration
# ─────────────────────────────────────────────────────────────────────────────


def load_plan(path: Path) -> BackfillPlan:
    """Load BackfillPlan from JSON file."""
    import json
    
    with open(path) as f:
        data = json.load(f)
    
    return BackfillPlan.model_validate(data)


def apply_from_file(
    plan_path: Path,
    dry_run: bool = False,
    allow_dirty: bool = False,
    vault: Path | None = None,
) -> ApplyResult:
    """
    Apply backfill plan from saved file.
    
    Args:
        plan_path: Path to BackfillPlan JSON
        dry_run: Preview only
        allow_dirty: Skip git clean check
        vault: Path to vault root
        
    Returns:
        ApplyResult
    """
    plan = load_plan(plan_path)
    print(f"Loaded plan with {len(plan.updates)} README updates")
    
    applier = TransactionalBackfillApply(vault)
    return applier.execute(plan, dry_run=dry_run, allow_dirty=allow_dirty)
