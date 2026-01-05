# VAST + Azure Integration — Engineering Delivery Plan

**Audience:** VAST engineering, product, and solution architecture teams responsible for delivery.

**Intent:** Turn the vision (“Blob governance core + VAST performance edge”) into a scoped, testable, phased engineering plan.

## Outcomes (What “Done” Means)

- Customers can **move data and checkpoints** between Azure Blob Storage and VAST using **standard Azure tooling** (AzCopy/SDKs) without refactoring.
- VAST can **tier cold data** to Azure Blob Storage to preserve flash for the working set.
- VAST deployments on Azure and edge environments are **repeatable, secure, and observable** with clear runbooks.

## Scope (Crawl / Walk / Run)

### Crawl (Compatibility + Offload)

- Blob API façade (subset) targeted at:
  - Data movers (AzCopy-like patterns)
  - AI libraries that depend on Blob semantics (e.g., high-concurrency block upload + ranged reads)
- Server‑side copy primitives to support lake→edge hydration.
- Tiering/offload to Azure Blob Storage for cold artifacts.
- 1–2 reference architectures that can be deployed repeatedly.

**Acceptance gates (Crawl):**

- AzCopy copy/sync/remove scenarios succeed against VAST Blob endpoint.
- High‑concurrency clients (e.g., boostedblob) are stable (no server bottlenecks).
- Basic Azure Storage SDK flows work for list/read/write (targeted subset).

### Walk (Production Hardening + Scenario Expansion)

- Private connectivity patterns:
  - Private Link Service (partner exposure) + Private Endpoints
  - DNS architecture (private zones, split‑horizon, managed VNet constraints)
  - Throughput tuning playbooks (timeouts, keep‑alive, SNAT/conntrack constraints)
- API coverage expansion based on observed production needs.
- Initial federation patterns for metadata/index/value propagation into Azure workflows.

### Run (Managed Azure-Native Offering)

- Managed lifecycle (provisioning/upgrades/patching/scaling) with SLOs.
- Entra ID integration + CMK (Key Vault) + audit logging.
- Azure Monitor / Log Analytics integration.
- Marketplace / billing integration and packaging constraints.

## Engineering Workstreams

### 1) Blob API Façade (Core)

Primary spec: [Blob API Requirements (MVP)](../Appendices/Blob%20API%20Requirements%20%28MVP%29.md)

Deliverables:

- MVP REST surface (Block Blobs only), plus strict XML error and list response fidelity.
- Deterministic ETag/Last‑Modified semantics sufficient for sync tools.
- Copy-from-URL primitives (including range-based block copy).

### 2) Identity / AuthN / AuthZ

MVP alignment targets:

- Entra ID OAuth token validation (JWT signature + claim mapping).
- Managed Identity access patterns (audience/claims validation).
- Compatibility modes where necessary (SAS, Shared Key) to match existing tooling.

### 3) Tiering / Lifecycle / Data Formats

Deliverables:

- Policies for hot/warm/cold behavior and pinning.
- Blob as low‑cost durable tier with clear data format choices:
  - Opaque (max reduction) vs transparent (ecosystem access)
- Rehydration semantics and operational visibility (what is local vs remote).

### 4) Namespace / Metadata Federation (“Federation Plane”)

Deliverables:

- Defined patterns (Blob master ingest vs VAST master tiering) and conflict rules.
- Change detection/reconciliation approach (events vs change feed vs scans).
- Consistency guarantees that are explicit and testable.

### 5) Networking / Connectivity

Deliverables:

- Reference architectures for:
  - Customer VNet (“easy mode”)
  - Managed VNet services (“wall”) bridging patterns
- Private Link Service exposure model and approval workflow expectations.

### 6) Observability / Ops

Deliverables:

- Metrics and logs for: API health, sync lag, tiering behavior, error codes, throughput.
- Runbooks for common failure modes (auth issues, DNS issues, throttling, copy failures).

## Workload Enablement

Canonical workload catalog: [Workloads & Reference Topologies](../Appendices/Workloads%20%26%20Reference%20Topologies.md)

Engineering plan should map each workload to:

- Required integration pattern (Blob API / S3 / NFS/SMB / Kafka)
- Required networking model (VNet peering / ExpressRoute / PLS / managed private endpoints)
- Known blockers and “walk/run” requirements

## Open Items (Tracked in TODO)

Project tracker: [TODO](../TODO.md)

This includes:

- Placeholder sections that still need to be written (identity, encryption, etc.)
- Backlog outlines for architecture, networking, security, federation, and managed service requirements
- Cross‑references needed between workloads and Azure services
