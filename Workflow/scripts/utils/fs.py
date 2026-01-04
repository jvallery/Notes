"""Atomic file system operations."""

from pathlib import Path
import tempfile
import os
import re
import shutil


def sanitize_filename(name: str) -> str:
    """
    Sanitize a filename by replacing/removing invalid filesystem characters.
    
    This is called deterministically in Python, NOT by the LLM.
    
    Rules:
    - `:` → `-` (common in titles like "Google: Update")
    - `/` → `-` (path separator)
    - `\\` → `-` (Windows path separator)
    - `|`, `<`, `>`, `"`, `?`, `*` → removed
    - Multiple consecutive `-` or spaces → single
    - Trim leading/trailing whitespace and dashes
    
    Args:
        name: The filename to sanitize (without extension)
        
    Returns:
        Sanitized filename safe for all filesystems
    """
    # Replace common problematic characters with dash
    result = name.replace(":", "-").replace("/", "-").replace("\\", "-")
    
    # Remove other invalid characters
    result = re.sub(r'[|<>"?*]', '', result)
    
    # Collapse multiple spaces only (not dashes - they're meaningful in dates like 2025-12-15)
    result = re.sub(r' {2,}', ' ', result)
    
    # Collapse multiple dashes, but not when surrounded by digits (preserve date formats)
    result = re.sub(r'(?<!\d)-{2,}(?!\d)', '-', result)
    
    # Trim
    result = result.strip(' -')
    
    return result


def sanitize_path(path: str) -> str:
    """
    Sanitize a vault-relative path, handling both directory and filename.
    
    Applies sanitize_filename to the final component only (the filename),
    preserving the directory structure.
    
    Args:
        path: Vault-relative path like "VAST/People/Name/2026-01-03 - Title.md"
        
    Returns:
        Path with sanitized filename
    """
    p = Path(path)
    if p.suffix:
        # Has extension - sanitize stem only
        sanitized_name = sanitize_filename(p.stem) + p.suffix
        return str(p.parent / sanitized_name)
    else:
        # No extension - sanitize the whole name
        return str(p.parent / sanitize_filename(p.name))


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
