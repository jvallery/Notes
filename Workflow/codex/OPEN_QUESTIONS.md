# Open Questions

- Should backfill enrichment (web search) be enabled by default? If so, add caching and clear opt-in.
- Where should canonical prompts/templates live long-term: `Workflow/*` or `Inbox/_bins/*`? Align `config.yaml` accordingly.
- For profile selection, do we prefer a tiny classifier prompt vs. rules only? Target latency/quality?
- Standards checker: finalized tag depth rules (only one slash or nested allowed)?
- Commit strategy: single commit per batch vs per source? Current Apply batches all changes.
