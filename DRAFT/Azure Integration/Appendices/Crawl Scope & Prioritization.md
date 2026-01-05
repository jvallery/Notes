# Crawl Scope & Prioritization (Ruthless)

**Purpose:** Define the Crawl “wedge” clearly enough that (1) stakeholders align on what we are *not* doing, and (2) engineering can implement the minimum viable surfaces required to pass acceptance gates and unblock pilots.

## Crawl Goal (One Sentence)

Enable customers to hydrate datasets and move checkpoints between Azure Blob Storage and VAST using standard Azure tooling (AzCopy/SDKs) with private connectivity, without refactoring pipelines.

## Default Crawl Wedge (Proposed)

**Core workloads:**

- **W2:** Central Blob lake + GPU‑adjacent VAST satellites (training + checkpoints)
- **W5:** On‑prem VAST tiering to Azure Blob Storage (cold tail + BCDR)

**Adjacent (defer unless forced by a pilot):**

- W1 (burst compute hybrid), W6 (managed service “migration-on-read”), W10 (migration/modernization)

## In Scope (Crawl)

### Blob API façade

- Block Blobs only (no DFS/HNS semantics).
- Enough REST surface to pass **AzCopy Gate A** and targeted SDK validation.
- Multi‑protocol coherence rules (file/dir conflicts, naming constraints).

References: [Blob API Requirements (MVP)](Blob%20API%20Requirements%20%28MVP%29.md), [AzCopy Test Suites & Acceptance](AzCopy%20Test%20Suites%20%26%20Acceptance.md)

### Data movement / hydration primitives

- Server‑side copy from Blob → VAST (range-based) for large objects.
- Deterministic `ETag`/`Last-Modified` and XML list fidelity to satisfy tooling.

### Deployment + networking

- Customer VNet patterns: peering/ExpressRoute + Private Link Service + DNS.
- Repeatable reference architecture(s) for the core workloads.

## Out of Scope (Crawl)

- Page Blobs (Gate B) unless required by a specific pilot.
- ADLS Gen2 / dfs endpoint / HNS semantics.
- Azure Files compatibility.
- “Run” managed service packaging, portal UX, and Azure-native control plane integrations.

## Acceptance Gates (Crawl)

- **Gate A:** AzCopy smoke test suites (Block Blob) pass end-to-end against the VAST Blob façade.
- **SDK sanity:** targeted `azure-storage-blob` flows work for list/read/write for the MVP subset.
- **Reference arch validation:** at least one deployable architecture is validated with documented assumptions + runbook.

## Decisions Needed

- Which customer pilots anchor Crawl (and what they require beyond the default wedge).
- Top 3 Azure services to validate first (for the workload(s) in scope).
- Auth model for Crawl (Entra only vs adding SAS/shared key compatibility for tooling).

## Update Targets (Keep in Sync)

- `VAST/Executive Overview.md` (scope + why now)
- `Microsoft/Executive Overview.md` (scope + why Microsoft wins)
- `VAST/Engineering Delivery Plan.md` (milestones + acceptance gates)
- `Microsoft/Engineering Alignment & Asks.md` (asks + validation plan)
- `Appendices/Azure Native Services Integration Matrix.md` (phase/owner/validation)
