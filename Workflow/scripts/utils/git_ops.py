#!/usr/bin/env python3
"""
Git operations for Notes Vault automation.

Handles commits, status checks, and recovery operations.
Designed for transactional workflow with smart dirty detection.
"""

from __future__ import annotations

import subprocess
from datetime import datetime
from pathlib import Path
from typing import Optional
from dataclasses import dataclass

from .config import vault_root, load_config


# Paths to CHECK for cleanliness (task list + content directories)
CHECKED_PATHS = ["TASKS.md", "Inbox/", "VAST/", "Personal/"]

# Paths to IGNORE (frequently change from Obsidian/sync)
IGNORED_PATTERNS = [
    ".obsidian/",
    "Workflow/logs/",
    "Workflow/.venv/",
    ".workflow_backups/",
]


@dataclass
class GitStatus:
    """Git repository status."""
    staged: list[str]
    unstaged: list[str]
    untracked: list[str]

    @property
    def is_clean(self) -> bool:
        return not (self.staged or self.unstaged or self.untracked)


def _run_git(repo_path: Path, *args: str) -> tuple[int, str, str]:
    """Run a git command and return (returncode, stdout, stderr)."""
    result = subprocess.run(
        ["git", *args],
        cwd=repo_path,
        capture_output=True,
        text=True
    )
    return result.returncode, result.stdout, result.stderr


def is_git_repo(path: Path = None) -> bool:
    """Check if path is inside a git repository."""
    if path is None:
        path = vault_root()
    code, _, _ = _run_git(path, "rev-parse", "--git-dir")
    return code == 0


def get_status(repo_path: Path = None, paths: list[str] | None = None) -> GitStatus:
    """
    Get git status, optionally filtered to specific paths.

    Returns GitStatus with staged, unstaged, and untracked files.
    """
    if repo_path is None:
        repo_path = vault_root()
    
    cmd = ["status", "--porcelain"]
    if paths:
        cmd.append("--")
        cmd.extend(paths)

    code, stdout, stderr = _run_git(repo_path, *cmd)
    if code != 0:
        raise RuntimeError(f"git status failed: {stderr}")

    staged = []
    unstaged = []
    untracked = []

    for line in stdout.rstrip("\n").split("\n"):
        if not line.strip():
            continue

        # Skip ignored patterns
        file_path = line[3:]  # Status is first 2 chars + space
        if any(pattern in file_path for pattern in IGNORED_PATTERNS):
            continue

        index_status = line[0]
        worktree_status = line[1]

        if index_status == "?":
            untracked.append(file_path)
        else:
            if index_status != " ":
                staged.append(file_path)
            if worktree_status != " ":
                unstaged.append(file_path)

    return GitStatus(staged=staged, unstaged=unstaged, untracked=untracked)


def is_clean(repo_path: Path = None, strict: bool = False) -> bool:
    """
    Check if working directory is clean for automation.

    By default, only checks CHECKED_PATHS.
    If strict=True, checks entire repo.
    """
    if repo_path is None:
        repo_path = vault_root()
    paths = None if strict else CHECKED_PATHS
    status = get_status(repo_path, paths)
    return status.is_clean


def require_clean(repo_path: Path = None, allow_dirty: bool = False) -> None:
    """
    Fail fast if working directory is dirty.

    Raises RuntimeError if dirty (unless allow_dirty=True).
    """
    if allow_dirty:
        return
    
    if repo_path is None:
        repo_path = vault_root()

    if not is_clean(repo_path):
        status = get_status(repo_path, CHECKED_PATHS)
        files = status.staged + status.unstaged + status.untracked
        raise RuntimeError(
            f"Git working directory has uncommitted changes in content directories:\n"
            f"  {', '.join(files[:5])}{'...' if len(files) > 5 else ''}\n"
            f"Commit or stash changes before running automation.\n"
            f"Use --allow-dirty to override (not recommended)."
        )


def add_files(repo_path: Path, files: list[Path]) -> None:
    """Stage files for commit."""
    if not files:
        return

    str_files = [str(f.relative_to(repo_path) if f.is_absolute() else f) for f in files]
    code, _, stderr = _run_git(repo_path, "add", *str_files)
    if code != 0:
        raise RuntimeError(f"git add failed: {stderr}")


def commit(repo_path: Path = None, message: str = None, files: list[str] = None) -> str:
    """
    Create commit and return commit hash.
    
    If files provided, stages them first.
    Returns empty string if nothing to commit.
    """
    if repo_path is None:
        repo_path = vault_root()
    
    # Stage files if provided
    if files:
        for file in files:
            file_path = Path(file)
            if not file_path.is_absolute():
                file_path = repo_path / file
            if file_path.exists():
                _run_git(repo_path, "add", str(file_path))
    
    # Default message
    if not message:
        message = f"[auto] Processed files at {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    
    code, stdout, stderr = _run_git(repo_path, "commit", "-m", message)
    if code != 0:
        if "nothing to commit" in stderr or "nothing to commit" in stdout:
            return ""  # No changes to commit
        raise RuntimeError(f"git commit failed: {stderr}")

    # Get the commit hash
    code, stdout, _ = _run_git(repo_path, "rev-parse", "HEAD")
    return stdout.strip()


def get_current_branch(repo_path: Path = None) -> str:
    """Get current branch name."""
    if repo_path is None:
        repo_path = vault_root()
    code, stdout, stderr = _run_git(repo_path, "branch", "--show-current")
    if code != 0:
        raise RuntimeError(f"git branch failed: {stderr}")
    return stdout.strip()


# Legacy compatibility functions
def is_dirty() -> bool:
    """Check if there are uncommitted changes (legacy)."""
    return not is_clean(strict=True)


def get_changed_files() -> list[str]:
    """Get list of changed files (legacy)."""
    status = get_status()
    return status.staged + status.unstaged + status.untracked


def commit_batch(
    files: list[str], message: Optional[str] = None, prefix: str = "[auto]"
) -> Optional[str]:
    """
    Commit a batch of files (legacy wrapper).

    Returns commit hash on success, None on failure.
    """
    if not message and files:
        file_names = [Path(f).name for f in files[:5]]
        if len(files) > 5:
            file_names.append(f"... and {len(files) - 5} more")
        message = f"{prefix} Processed: {', '.join(file_names)}"
    
    try:
        result = commit(message=message, files=files)
        return result[:8] if result else None
    except RuntimeError:
        return None


def get_last_commit() -> Optional[dict]:
    """Get info about the last commit."""

    if not is_git_repo():
        return None

    result = subprocess.run(
        ["git", "log", "-1", "--format=%H|%s|%ai"],
        cwd=vault_root(),
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        return None

    parts = result.stdout.strip().split("|")
    if len(parts) != 3:
        return None

    return {"hash": parts[0][:8], "message": parts[1], "date": parts[2]}


def revert_last() -> bool:
    """Revert the last commit."""

    if not is_git_repo():
        return False

    result = subprocess.run(
        ["git", "revert", "--no-commit", "HEAD"], cwd=vault_root(), capture_output=True
    )

    return result.returncode == 0


def stash_changes() -> bool:
    """Stash current changes."""

    if not is_git_repo():
        return False

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    result = subprocess.run(
        ["git", "stash", "push", "-m", f"Auto-stash before processing {timestamp}"],
        cwd=vault_root(),
        capture_output=True,
    )

    return result.returncode == 0


def pop_stash() -> bool:
    """Pop the most recent stash."""

    if not is_git_repo():
        return False

    result = subprocess.run(
        ["git", "stash", "pop"], cwd=vault_root(), capture_output=True
    )

    return result.returncode == 0


if __name__ == "__main__":
    # Test git operations
    from rich import print as rprint

    rprint(f"[bold]Git repo:[/bold] {is_git_repo()}")
    rprint(f"[bold]Current branch:[/bold] {get_current_branch()}")
    rprint(f"[bold]Status:[/bold]")
    status = get_status()
    rprint(f"  Staged: {status.staged}")
    rprint(f"  Unstaged: {status.unstaged}")
    rprint(f"  Untracked: {status.untracked}")
    rprint(f"[bold]Clean (content dirs):[/bold] {is_clean()}")
    rprint(f"[bold]Last commit:[/bold] {get_last_commit()}")
