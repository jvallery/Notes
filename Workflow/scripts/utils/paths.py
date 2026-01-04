"""Path utilities for vault operations."""

from pathlib import Path
from datetime import date


def get_archive_path(vault_root: Path, original_file: Path, archive_date: date | None = None) -> Path:
    """Get archive destination for a source file."""
    if archive_date is None:
        archive_date = date.today()
    return vault_root / "Inbox" / "_archive" / archive_date.isoformat() / original_file.name


def get_extraction_path(vault_root: Path, source_file: Path) -> Path:
    """Get extraction JSON path for a source file."""
    return vault_root / "Inbox" / "_extraction" / f"{source_file.stem}.extraction.json"


def get_changeplan_path(vault_root: Path, source_file: Path) -> Path:
    """Get changeplan JSON path for a source file."""
    return vault_root / "Inbox" / "_extraction" / f"{source_file.stem}.changeplan.json"


def safe_relative_path(vault_root: Path, path: Path | str) -> Path:
    """Convert to vault-relative path, preventing directory traversal."""
    if isinstance(path, str):
        path = Path(path)

    # If already relative, resolve against vault root
    if not path.is_absolute():
        path = vault_root / path

    # Resolve to catch any .. traversal
    resolved = path.resolve()
    vault_resolved = vault_root.resolve()

    # Ensure path is within vault
    try:
        resolved.relative_to(vault_resolved)
    except ValueError:
        raise ValueError(f"Path {path} is outside vault root {vault_root}")

    return resolved.relative_to(vault_resolved)


def ensure_parent_exists(path: Path) -> None:
    """Create parent directories if they don't exist."""
    path.parent.mkdir(parents=True, exist_ok=True)
