#!/usr/bin/env python3
"""Deprecated wrapper: use scripts/ingest.py instead."""

import sys
from legacy_wrapper import run_ingest


if __name__ == "__main__":
    sys.exit(run_ingest("process_emails.py"))
