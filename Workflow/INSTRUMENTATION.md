# Instrumentation & Logging Framework

> **Version**: 1.0.0  
> **Last Updated**: 2026-01-04

This document describes the centralized logging and AI instrumentation framework used across all Notes Vault automation scripts.

## Overview

All automation scripts share a common infrastructure for:

1. **AI Client Management** — Single instrumented OpenAI client with request/response logging
2. **Unified Logging** — Consistent log formatting, context tracking, and file output
3. **Cost Tracking** — Token usage and cost estimation per model/caller
4. **Audit Trail** — Complete record of all AI interactions for debugging
5. **Pipeline Metrics** — Phase timings + prompt cache stats recorded per ingest run

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     YOUR SCRIPT                                  │
│   from utils import get_openai_client, get_logger, setup_logging│
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│               Workflow/scripts/utils/                            │
├─────────────────────────────┬───────────────────────────────────┤
│     ai_client.py            │           logging.py              │
│  ─────────────────          │        ─────────────────          │
│  • InstrumentedClient       │  • ContextLogger                  │
│  • Request/Response logging │  • Colored console output         │
│  • Token tracking           │  • JSON file output               │
│  • Cost estimation          │  • Context managers               │
└─────────────────────────────┴───────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Workflow/logs/                                │
├─────────────────────────────────────────────────────────────────┤
│  YYYY-MM-DD_HHMMSS_run.log    # Standard run logs               │
│  ai/                                                             │
│   └── YYYY-MM-DD/                                                │
│       ├── requests.jsonl       # All AI requests (append-only)  │
│       ├── responses.jsonl      # All AI responses (append-only) │
│       └── summary.json         # Daily aggregated stats         │
│   └── latest.json → (symlink to most recent summary)            │
└─────────────────────────────────────────────────────────────────┘
```

## Quick Start

### Basic Usage

```python
#!/usr/bin/env python3
"""Example script using the instrumentation framework."""

from utils import get_openai_client, get_logger, setup_logging

# Setup logging first (optional but recommended for CLI scripts)
log_file = setup_logging(verbose=True)

# Get a logger with context support
logger = get_logger("my_script")
logger.info("Starting processing")

# Get instrumented OpenAI client
client = get_openai_client("my_script")

# All API calls are now automatically logged!
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Hello!"}]
)

logger.info(f"Got response: {response.choices[0].message.content}")
```

### With Context Tracking

```python
from utils import get_logger

logger = get_logger("extract")

# Context is added to all log messages in this scope
with logger.context(phase="extract", file="email_001.md"):
    logger.info("Processing started")    # Shows: INFO [extract] (email_001.md) Processing started
    logger.debug("Parsing metadata")     # Shows: DEBUG [extract] (email_001.md) Parsing metadata
```

## AI Client (`utils.ai_client`)

### Getting the Client

```python
from utils import get_openai_client

# With caller identification (recommended)
client = get_openai_client("draft_responses.extract_email")

# Without caller (will show as "unknown" in logs)
client = get_openai_client()
```

### What Gets Logged

Every API call logs:

**Request (`requests.jsonl`):**
```json
{
  "id": "2026-01-04_a1b2c3d4",
  "timestamp": "2026-01-04T15:30:00.123456",
  "operation": "chat.completions.create",
  "model": "gpt-4o",
  "messages": [{"role": "user", "content": "..."}],
  "temperature": 0.7,
  "caller": "draft_responses.extract_email",
  "context": {"email": "meeting_notes.md"}
}
```

**Response (`responses.jsonl`):**
```json
{
  "request_id": "2026-01-04_a1b2c3d4",
  "timestamp": "2026-01-04T15:30:02.456789",
  "success": true,
  "model": "gpt-4o-2024-05-13",
  "content": "...",
  "usage": {
    "prompt_tokens": 150,
    "completion_tokens": 89,
    "total_tokens": 239
  },
  "finish_reason": "stop",
  "latency_ms": 2333
}
```

### Daily Summary

`Workflow/logs/ai/YYYY-MM-DD/summary.json`:
```json
{
  "date": "2026-01-04",
  "total_requests": 52,
  "successful_requests": 51,
  "failed_requests": 1,
  "total_prompt_tokens": 45230,
  "total_completion_tokens": 12450,
  "total_tokens": 57680,
  "total_latency_ms": 125000,
  "by_model": {
    "gpt-4o": {"requests": 45, "tokens": 50000, "latency_ms": 100000, "errors": 0},
    "gpt-4o-mini": {"requests": 7, "tokens": 7680, "latency_ms": 25000, "errors": 1}
  },
  "by_operation": {
    "chat.completions.create": 52
  },
  "by_caller": {
    "draft_responses": 22,
    "ingest_emails": 20,
    "entity_discovery": 10
  },
  "estimated_cost_usd": 0.85,
  "pipeline_runs": [
    {
      "timestamp": "2026-01-05T00:15:00.123Z",
      "total": 3,
      "success": 3,
      "failed": 0,
      "skipped": 0,
      "run_ms": 1820,
      "phase_ms_avg": {
        "adapter_ms": 8,
        "context_ms": 10,
        "extract_ms": 520,
        "patch_ms": 40,
        "apply_ms": 650,
        "outputs_ms": 90
      },
      "cache": {
        "calls": 3,
        "hits": 2,
        "hit_rate": 66.7,
        "cached_tokens": 900,
        "prompt_tokens": 1500,
        "total_tokens": 1800
      }
    }
  ]
}
```

### Viewing Stats

```python
from utils import get_ai_stats

stats = get_ai_stats()
print(f"Requests today: {stats['total_requests']}")
print(f"Tokens used: {stats['total_tokens']}")
print(f"Estimated cost: ${stats['estimated_cost_usd']:.2f}")
```

### Unified Pipeline Metrics

- Show per-run timings + cache stats inline: `python scripts/ingest.py --all --show-cache-stats`
- Aggregated metrics live in `Workflow/logs/ai/YYYY-MM-DD/summary.json` under `pipeline_runs` (hit rate, cached tokens, average phase timings).

## Logging (`utils.logging`)

### Setup

```python
from utils import setup_logging, get_logger

# For CLI scripts - call at entry point
log_file = setup_logging(
    verbose=True,       # DEBUG level on console (default: INFO)
    log_file=None,      # Auto-generate filename (default)
    json_output=False,  # Use text format (default)
)
```

### Logger with Context

```python
from utils import get_logger

logger = get_logger("my_module")

# Simple logging
logger.info("Processing started")
logger.debug("Debug details")
logger.warning("Something unexpected")
logger.error("Something failed", exc_info=True)

# With context manager
with logger.context(phase="extract", file="email.md"):
    logger.info("Now shows phase and file in output")
```

### Global Context

```python
from utils import set_context, clear_context

# Set context that applies to ALL loggers
set_context(phase="extract")

# Later
clear_context()
```

### Summary Tables

```python
from utils import log_summary

log_summary({
    "Files processed": 52,
    "Drafts created": 22,
    "Patches applied": 516,
    "Errors": 1,
}, title="Pipeline Results")
```

Output:
```
==================================================
 Pipeline Results
==================================================
  Files processed : 52
  Drafts created  : 22
  Patches applied : 516
  Errors          : 1
==================================================
```

## Log File Locations

| Path | Contents |
|------|----------|
| `Workflow/logs/*.log` | Run logs (human-readable) |
| `Workflow/logs/ai/YYYY-MM-DD/requests.jsonl` | All AI requests |
| `Workflow/logs/ai/YYYY-MM-DD/responses.jsonl` | All AI responses |
| `Workflow/logs/ai/YYYY-MM-DD/summary.json` | Daily aggregated stats |
| `Workflow/logs/ai/latest.json` | Symlink to most recent summary |

## Scripts Updated

The following scripts now use the centralized framework:

| Script | Caller ID |
|--------|-----------|
| `draft_responses.py` | `draft_responses` |
| `ingest_emails.py` | `ingest_emails` |
| `process_emails.py` | `process_emails` |
| `entity_discovery.py` | `entity_discovery` |
| `extract.py` | `extract` |

## Debugging Tips

### View Recent Requests

```bash
# See last 10 requests
tail -10 Workflow/logs/ai/$(date +%Y-%m-%d)/requests.jsonl | jq

# Filter by caller
grep '"caller": "draft_responses"' Workflow/logs/ai/*/requests.jsonl | tail -5
```

### View Failed Requests

```bash
# Find failed responses
grep '"success": false' Workflow/logs/ai/*/responses.jsonl | jq
```

### Cost Analysis

```bash
# View today's costs
cat Workflow/logs/ai/$(date +%Y-%m-%d)/summary.json | jq '.estimated_cost_usd'

# View by model
cat Workflow/logs/ai/$(date +%Y-%m-%d)/summary.json | jq '.by_model'
```

### Correlate Request/Response

```bash
# Find a specific request
REQUEST_ID="2026-01-04_a1b2c3d4"
grep "$REQUEST_ID" Workflow/logs/ai/*/requests.jsonl | jq
grep "$REQUEST_ID" Workflow/logs/ai/*/responses.jsonl | jq
```

## Best Practices

1. **Always pass a caller ID** — Makes debugging much easier
   ```python
   client = get_openai_client("my_script.my_function")
   ```

2. **Use context managers** — Groups related log entries
   ```python
   with logger.context(file=filename):
       # All logs here show the filename
   ```

3. **Setup logging early** — Call `setup_logging()` at script entry
   ```python
   if __name__ == "__main__":
       setup_logging(verbose=args.verbose)
   ```

4. **Check stats after runs** — Monitor costs and errors
   ```python
   stats = get_ai_stats()
   if stats['failed_requests'] > 0:
       logger.warning(f"Had {stats['failed_requests']} failed API calls")
   ```

## Migration Guide

To update an existing script to use the framework:

### Before

```python
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[...]
)
```

### After

```python
from utils import get_openai_client

client = get_openai_client("my_script")

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[...]
)
# Now automatically logged!
```

That's it — the API is identical, just the client creation changes.
