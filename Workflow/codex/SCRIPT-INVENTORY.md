# Script Inventory (Workflow/scripts)

## Core Pipeline

- `scripts/extract.py`
  - Finds unprocessed Inbox files.
  - Uses `scripts/classify.py` + `scripts/utils/openai_client.py`.
  - Writes `Inbox/_extraction/*.extraction.json`.

- `scripts/plan.py`
  - Builds planner prompt with limited vault context.
  - Writes `Inbox/_extraction/*.changeplan.json`.

- `scripts/apply.py`
  - Validates ChangePlans, backs up files, applies ops.
  - Archives sources to `Inbox/_archive/YYYY-MM-DD/`.
  - Commits changes (git).

- `scripts/process_inbox.py`
  - Orchestrates Extract -> Plan -> Apply with logging.

## Backfill

- `scripts/backfill/scanner.py`
  - Scans entity folders for notes/README state.

- `scripts/backfill/extractor.py`
  - AI extraction from existing notes (chat API).

- `scripts/backfill/aggregator.py`
  - Aggregates extractions into README updates.

- `scripts/backfill/applier.py`
  - Applies README updates transactionally with backups and git commit.

- `scripts/backfill/entities.py`
  - Manages manifests and optional web enrichment.

## Migration

- `scripts/migration/scanner.py`
  - Scans for STANDARDS compliance issues.

- `scripts/migration/analyzer.py`
  - Builds migration plan (not reviewed in detail).

- `scripts/migration/executor.py`
  - Applies migration plan with backups + commit.

- `scripts/migration/verifier.py`
  - Verifies compliance after migration.

## Cleanup

- `scripts/cleanup/readme_normalizer.py`
  - Normalizes README sections order and ledger entries.

- `scripts/cleanup/readme_auditor.py`
  - Uses OpenAI chat to audit README content.

- `scripts/cleanup/source_normalizer.py`
  - Normalizes source filenames in `Sources/`.

## Validation

- `scripts/validate.py`
  - JSON Schema validation for extraction/changeplan artifacts.

## Config

- `scripts/utils/config.py` (dict-based loader)
- `scripts/config.py` (dot-access loader; appears unused)

