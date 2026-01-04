"""Atomic file system operations."""

from pathlib import Path
import tempfile
import os
import shutil


def atomic_write(path: Path, content: str, encoding: str = "utf-8") -> None:
    """
    Write content to file atomically using temp file + rename.

    This prevents partial writes if the process is interrupted.
    """
    path.parent.mkdir(parents=True, exist_ok=True)

    # Write to temp file in same directory (required for atomic rename)
    fd, temp_path = tempfile.mkstemp(dir=path.parent, suffix=".tmp")
    try:
        with os.fdopen(fd, 'w', encoding=encoding) as f:
            f.write(content)
        # Atomic rename
        os.replace(temp_path, path)
    except:
        # Clean up temp file on failure
        try:
            os.unlink(temp_path)
        except OSError:
            pass
        raise


def safe_read_text(path: Path, encoding: str = "utf-8") -> str:
    """Read text file with encoding fallback."""
    try:
        return path.read_text(encoding=encoding)
    except UnicodeDecodeError:
        # Fall back to latin-1 which accepts any byte
        return path.read_text(encoding="latin-1")


def backup_file(source: Path, backup_dir: Path, vault_root: Path = None) -> Path:
    """
    Copy file to backup directory, preserving vault-relative structure.
    
    T3 FIX: Preserves directory structure to prevent collisions when
    multiple files share the same name (e.g., README.md in different folders).
    
    Args:
        source: File to backup
        backup_dir: Root of backup directory
        vault_root: Vault root for relative path calculation (optional)
        
    Returns:
        Path to the backup file
    """
    if vault_root is not None:
        try:
            # Preserve vault-relative path structure
            rel_path = source.resolve().relative_to(vault_root.resolve())
            backup_path = backup_dir / rel_path
        except ValueError:
            # Source not under vault_root, fall back to filename only
            backup_path = backup_dir / source.name
    else:
        # Legacy behavior: filename only (kept for backward compatibility)
        backup_path = backup_dir / source.name
    
    backup_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, backup_path)
    return backup_path
