"""
Structured logging for automation pipeline.

JSON-line logging for observability and debugging.
Logs are written to Workflow/logs/YYYYMMDD_HHMMSS.log

Usage:
    from scripts.utils.logging import setup_logging, log_event, close_logging
    
    log_path = setup_logging(run_id="20260103_180000")
    log_event("extract", "start", {"file": "meeting.md"})
    log_event("extract", "success", {"file": "meeting.md", "latency_ms": 2500})
    close_logging()
"""

from __future__ import annotations

import atexit
import json
from datetime import datetime
from pathlib import Path
from typing import Any, TextIO

from .config import workflow_root


# Global log state
_log_file: TextIO | None = None
_run_id: str | None = None
_log_path: Path | None = None


def setup_logging(run_id: str | None = None, log_dir: Path | None = None) -> Path:
    """
    Initialize logging for this run.
    
    Args:
        run_id: Unique identifier for this run (default: timestamp)
        log_dir: Override log directory (default: Workflow/logs)
    
    Returns:
        Path to the log file
    """
    global _log_file, _run_id, _log_path
    
    # Close any existing log
    close_logging()
    
    # Generate run ID if not provided
    if run_id is None:
        run_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    _run_id = run_id
    
    # Determine log directory
    if log_dir is None:
        log_dir = workflow_root() / "logs"
    
    log_dir.mkdir(parents=True, exist_ok=True)
    
    _log_path = log_dir / f"{run_id}.log"
    _log_file = open(_log_path, "a", encoding="utf-8")
    
    # Register cleanup on exit
    atexit.register(close_logging)
    
    return _log_path


def log_event(
    phase: str,
    status: str,
    data: dict[str, Any] | None = None,
) -> None:
    """
    Log a structured event.
    
    Args:
        phase: Pipeline phase (process, extract, plan, apply)
        status: Event status (start, success, failed, error, complete)
        data: Additional event data
    
    Example:
        log_event("extract", "success", {"file": "meeting.md", "latency_ms": 2500})
    """
    global _log_file, _run_id
    
    event = {
        "timestamp": datetime.now().isoformat(),
        "run_id": _run_id or "unknown",
        "phase": phase,
        "status": status,
    }
    
    if data:
        event.update(data)
    
    line = json.dumps(event, default=str)
    
    if _log_file:
        _log_file.write(line + "\n")
        _log_file.flush()
    else:
        # Fallback to print if not initialized
        print(f"[LOG] {line}")


def close_logging() -> None:
    """Close log file and cleanup."""
    global _log_file, _run_id, _log_path
    
    if _log_file:
        try:
            _log_file.close()
        except Exception:
            pass
        _log_file = None


def get_log_path() -> Path | None:
    """Get current log file path."""
    return _log_path


def get_run_id() -> str | None:
    """Get current run ID."""
    return _run_id
