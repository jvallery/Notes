#!/usr/bin/env python3
"""
Unified Logging Framework for Notes Vault Automation.

This module provides:
1. Consistent logging configuration across all scripts
2. Structured logging with JSON output option
3. Log rotation and archival
4. Console + file output with different verbosity levels
5. Context tracking (which phase, which file, etc.)

Usage:
    from utils.logging import get_logger, setup_logging
    
    # Simple usage
    logger = get_logger("my_script")
    logger.info("Processing started")
    
    # With setup for CLI scripts
    setup_logging(verbose=True, log_file="my_run.log")
    logger = get_logger("my_script")
    
    # With context
    with logger.context(phase="extract", file="email.md"):
        logger.info("Extracting content")

Log Files:
    - Workflow/logs/YYYY-MM-DD_HHMMSS_run.log  # Run logs
    - Workflow/logs/ai/YYYY-MM-DD/             # AI request/response logs
    - Workflow/logs/archive/                    # Rotated old logs
"""

import json
import logging
import os
import sys
import threading
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, Any


# Thread-local context storage
_context = threading.local()


class ContextFilter(logging.Filter):
    """Add context fields to log records."""
    
    def filter(self, record):
        # Add context from thread-local storage
        ctx = getattr(_context, 'data', {})
        for key, value in ctx.items():
            setattr(record, key, value)
        
        # Ensure defaults exist
        if not hasattr(record, 'phase'):
            record.phase = ''
        if not hasattr(record, 'file'):
            record.file = ''
        if not hasattr(record, 'entity'):
            record.entity = ''
            
        return True


class ColoredFormatter(logging.Formatter):
    """Colored console output for better readability."""
    
    COLORS = {
        'DEBUG': '\033[36m',     # Cyan
        'INFO': '\033[32m',      # Green
        'WARNING': '\033[33m',   # Yellow
        'ERROR': '\033[31m',     # Red
        'CRITICAL': '\033[35m',  # Magenta
    }
    RESET = '\033[0m'
    
    def format(self, record):
        # Add color to level name
        levelname = record.levelname
        if levelname in self.COLORS:
            record.levelname = f"{self.COLORS[levelname]}{levelname:8}{self.RESET}"
        else:
            record.levelname = f"{levelname:8}"
        
        # Format context if present
        ctx_parts = []
        if getattr(record, 'phase', ''):
            ctx_parts.append(f"[{record.phase}]")
        if getattr(record, 'file', ''):
            ctx_parts.append(f"({record.file})")
        
        record.context_str = ' '.join(ctx_parts)
        if record.context_str:
            record.context_str = f" {record.context_str}"
        
        return super().format(record)


class JSONFormatter(logging.Formatter):
    """JSON formatter for structured logging."""
    
    def format(self, record):
        log_data = {
            'timestamp': datetime.fromtimestamp(record.created).isoformat(),
            'level': record.levelname,
            'logger': record.name,
            'message': record.getMessage(),
        }
        
        # Add context fields
        for field in ['phase', 'file', 'entity']:
            if hasattr(record, field) and getattr(record, field):
                log_data[field] = getattr(record, field)
        
        # Add exception info if present
        if record.exc_info:
            log_data['exception'] = self.formatException(record.exc_info)
        
        return json.dumps(log_data)


class ContextLogger(logging.LoggerAdapter):
    """Logger adapter that supports context managers for adding context."""
    
    def __init__(self, logger, extra=None):
        super().__init__(logger, extra or {})
    
    @contextmanager
    def context(self, **kwargs):
        """
        Context manager to add fields to all log messages in this scope.
        
        Example:
            with logger.context(phase="extract", file="email.md"):
                logger.info("Processing")  # Will include phase and file
        """
        # Save current context
        old_context = getattr(_context, 'data', {}).copy()
        
        # Update context
        if not hasattr(_context, 'data'):
            _context.data = {}
        _context.data.update(kwargs)
        
        try:
            yield
        finally:
            # Restore old context
            _context.data = old_context
    
    def process(self, msg, kwargs):
        # Add any context from the adapter
        extra = kwargs.get('extra', {})
        extra.update(self.extra)
        kwargs['extra'] = extra
        return msg, kwargs


# Module-level logger cache
_loggers: Dict[str, ContextLogger] = {}
_configured = False
_log_file: Optional[Path] = None


def setup_logging(
    verbose: bool = False,
    log_file: Optional[str] = None,
    json_output: bool = False,
    log_dir: Optional[Path] = None,
) -> Path:
    """
    Configure the logging system for a run.
    
    Args:
        verbose: If True, show DEBUG level on console
        log_file: Optional log file name. If None, auto-generates.
        json_output: If True, use JSON format for file output
        log_dir: Optional log directory. Defaults to Workflow/logs/
    
    Returns:
        Path to the log file
    """
    global _configured, _log_file
    
    # Determine log directory
    if log_dir is None:
        workflow_dir = Path(__file__).parent.parent.parent
        log_dir = workflow_dir / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate log file name if not provided
    if log_file is None:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
        log_file = f"{timestamp}_run.log"
    
    _log_file = log_dir / log_file
    
    # Configure root logger
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    
    # Remove existing handlers
    root.handlers.clear()
    
    # Add context filter
    context_filter = ContextFilter()
    
    # Console handler
    console = logging.StreamHandler(sys.stdout)
    console.setLevel(logging.DEBUG if verbose else logging.INFO)
    console.addFilter(context_filter)
    
    console_format = "%(levelname)s%(context_str)s %(message)s"
    console.setFormatter(ColoredFormatter(console_format))
    root.addHandler(console)
    
    # File handler
    file_handler = logging.FileHandler(_log_file)
    file_handler.setLevel(logging.DEBUG)
    file_handler.addFilter(context_filter)
    
    if json_output:
        file_handler.setFormatter(JSONFormatter())
    else:
        file_format = "%(asctime)s %(levelname)-8s [%(name)s]%(context_str)s %(message)s"
        file_handler.setFormatter(logging.Formatter(file_format, datefmt="%Y-%m-%d %H:%M:%S"))
    
    root.addHandler(file_handler)
    
    _configured = True
    
    # Log the start
    logger = get_logger("logging")
    logger.info(f"Log file: {_log_file}")
    
    return _log_file


def get_logger(name: str) -> ContextLogger:
    """
    Get a logger instance with context support.
    
    Args:
        name: Logger name (typically module or script name)
    
    Returns:
        ContextLogger instance
    
    Example:
        logger = get_logger("extract")
        logger.info("Starting extraction")
        
        with logger.context(phase="extract", file="email.md"):
            logger.debug("Processing file")
    """
    if name not in _loggers:
        logger = logging.getLogger(name)
        _loggers[name] = ContextLogger(logger)
    
    return _loggers[name]


def get_log_file() -> Optional[Path]:
    """Get the current log file path."""
    return _log_file


def set_context(**kwargs):
    """
    Set global context for all loggers.
    
    Example:
        set_context(phase="extract")
        logger.info("Message")  # Will include phase
    """
    if not hasattr(_context, 'data'):
        _context.data = {}
    _context.data.update(kwargs)


def clear_context():
    """Clear all global context."""
    _context.data = {}


def log_summary(stats: Dict[str, Any], title: str = "Summary"):
    """
    Log a formatted summary table.
    
    Args:
        stats: Dictionary of stat name -> value
        title: Title for the summary
    """
    logger = get_logger("summary")
    
    logger.info(f"{'='*50}")
    logger.info(f" {title}")
    logger.info(f"{'='*50}")
    
    max_key_len = max(len(str(k)) for k in stats.keys()) if stats else 10
    
    for key, value in stats.items():
        logger.info(f"  {key:<{max_key_len}} : {value}")
    
    logger.info(f"{'='*50}")
