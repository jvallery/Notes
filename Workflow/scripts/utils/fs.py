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


def backup_file(source: Path, backup_dir: Path) -> Path:
    """Copy file to backup directory, preserving relative structure."""
    # Preserve the filename in backup dir
    backup_path = backup_dir / source.name
    backup_path.parent.mkdir(parents=True, exist_ok=True)

    shutil.copy2(source, backup_path)
    return backup_path
