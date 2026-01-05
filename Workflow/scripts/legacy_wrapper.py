#!/usr/bin/env python3
"""Deprecated script wrapper to funnel callers to scripts/ingest.py."""

import subprocess
import sys
from pathlib import Path


def run_ingest(alias: str) -> int:
    """Print deprecation notice and forward args to ingest.py."""
    ingest_path = Path(__file__).resolve().parent / "ingest.py"
    notice = f"[DEPRECATED] {alias} is replaced by scripts/ingest.py. Forwarding..."
    print(notice)
    cmd = [sys.executable, str(ingest_path), *sys.argv[1:]]
    return subprocess.call(cmd)


if __name__ == "__main__":  # pragma: no cover
    sys.exit(run_ingest("legacy-wrapper"))
