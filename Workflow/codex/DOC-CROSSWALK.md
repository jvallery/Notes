# Doc vs Code Crosswalk

This highlights direct contradictions between documentation and implementation.

## OpenAI API Usage

- Docs:
  - `DESIGN.md`, `REQUIREMENTS.md`, `README.md` specify `client.responses.parse(..., store=False)`.
- Code:
  - `scripts/utils/openai_client.py` uses `client.beta.chat.completions.parse(...)` without `store=False`.
  - `scripts/backfill/extractor.py` uses `client.chat.completions.create(...)` and manual JSON parsing.
  - `scripts/cleanup/readme_auditor.py` uses `client.chat.completions.create(...)` without `store=False`.

## Model Policy

- Docs:
  - `REQUIREMENTS.md` and `README.md` reference `gpt-4o` / `gpt-4o-mini`.
  - `BACKFILL-DESIGN.md` specifies `gpt-4o-mini` for backfill extraction.
- Config:
  - `Workflow/config.yaml` uses `gpt-5.2-2025-12-11` for classify/extract/plan/backfill.

## Privacy Enforcement

- Docs:
  - Multiple docs insist `store=False` on all API calls.
- Code:
  - `openai_client.parse_structured()` checks `config.get("api").store`, but config uses `models.privacy.store`.
  - No `store=False` in `openai_client` calls.

## Standards vs Templates (Root Docs)

- Docs:
  - `STANDARDS.md` defines `type: person-root/project-root/account-root` for README.
- Templates:
  - `Workflow/templates/readme-person.md.j2` uses `type: people` and `title`.
  - `Workflow/templates/readme-customer.md.j2` uses `type: customer` and `title`.
  - `Workflow/templates/readme-project.md.j2` uses `type: projects` and `title`.

## Schema vs Models

- Docs/Schemas:
  - `Workflow/schemas/changeplan.schema.json` expects patch `{ primitive, heading, content }`.
- Code:
  - Pydantic `PatchSpec` expects `heading: {heading, content}`.

## Paths & Resources

- Docs/Config:
  - `config.yaml` references `Inbox/_bins/_prompts` + `_templates`.
- Code:
  - `scripts/utils/templates.py` defaults to `Workflow/prompts` and `Workflow/templates`.
- Vault:
  - `Inbox/_bins` does not exist.

## Classification

- Docs:
  - README describes “Classify (AI) -> Select Profile”.
- Code:
  - `scripts/classify.py` is heuristics only (no AI).

