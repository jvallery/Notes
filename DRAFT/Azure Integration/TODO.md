# Azure Integration — TODO

This file tracks the remaining collateral, placeholders, and “still-to-write” sections for the VAST + Azure integration doc set.

## How This File Works

- Each checkbox line is a task (Obsidian Tasks compatible).
- All tasks are currently AI-proposed (`[?]`) and tagged `#proposed #auto` until you accept them.
- Suggested tags:
  - `#p0` / `#p1` / `#p2`: priority (P0 = unblock Crawl pilots; P1 = Walk hardening; P2 = longer-term backlog)
  - `#crawl` / `#walk` / `#run`: roadmap phase
  - `#owner-vast` / `#owner-msft` / `#owner-customer`: primary owner
- Under each task, indented bullets capture: deliverable, acceptance criteria, references, and open questions.

## Doc Set (Audience-Specific)

- [?] Tighten [VAST/Executive Overview](VAST/Executive%20Overview.md) for exec readability (shorter, fewer jargon terms) #task #proposed #auto #p0 #crawl #owner-vast
  - Deliverable: ≤1 page narrative + 1 “governance tier ↔ performance tier” diagram + 3 bullets of key internal decisions/asks.
  - Acceptance: a VAST exec can explain “why/what/roadmap” in <60 seconds; terms match [Terminology & Conventions](Appendices/Terminology%20%26%20Conventions.md).

- [?] Expand [VAST/Engineering Delivery Plan](VAST/Engineering%20Delivery%20Plan.md) into an actionable milestone plan (owners, acceptance criteria, risks) #task #proposed #auto #p0 #crawl #owner-vast
  - Deliverable: add milestone plan (Crawl/Walk/Run), acceptance gates, dependencies, and “what we need from Microsoft” per workstream.
  - Acceptance: engineering can use it to staff/sequence work; explicit links to [Blob API Requirements (MVP)](Appendices/Blob%20API%20Requirements%20%28MVP%29.md), [Workloads](Appendices/Workloads%20%26%20Reference%20Topologies.md), and [Services Matrix](Appendices/Azure%20Native%20Services%20Integration%20Matrix.md).

- [?] Tighten [Microsoft/Executive Overview](Microsoft/Executive%20Overview.md) into a Microsoft-ready brief (clear “why Microsoft wins” + asks) #task #proposed #auto #p0 #crawl #owner-vast
  - Deliverable: ≤1 page brief emphasizing Azure wins, customer outcomes, and a short exec-level ask list (alignment + path to “Run”).
  - Acceptance: Microsoft exec can understand the pitch without VAST context; avoids internal codenames unless explained in [Terminology & Conventions](Appendices/Terminology%20%26%20Conventions.md).

- [?] Expand [Microsoft/Engineering Alignment & Asks](Microsoft/Engineering%20Alignment%20%26%20Asks.md) with concrete asks per service/team and validation plan #task #proposed #auto #p0 #crawl #owner-vast
  - Deliverable: “ask list” by Microsoft org/team + a validation checklist derived from the [Services Matrix](Appendices/Azure%20Native%20Services%20Integration%20Matrix.md).
  - Acceptance: each ask has an owner, desired outcome, and evidence (test/validation) required to close it.

## Consistency & Governance

- [?] Expand and maintain the shared terminology appendix (draft exists) #task #proposed #auto #p0 #crawl #owner-vast
  - Update: [Terminology & Conventions](Appendices/Terminology%20%26%20Conventions.md)
  - Acceptance: no conflicting use of “Blob/Blob Storage”, “AI Foundry/Foundry”, module names, or phase/variant/workload labels across docs.

- [?] Decide whether “Tuscany” is an internal codename vs external term; standardize on “migration‑on‑read proxy” for Microsoft-facing collateral if needed #task #proposed #auto #p0 #crawl #owner-vast
  - Deliverable: update terminology + replace language in Microsoft-facing docs as needed.
  - Acceptance: external-facing docs do not require insider vocabulary; “Tuscany” (if retained) is explicitly defined.

- [?] Add an explicit “assumptions + non-goals” section to each audience doc to prevent scope creep #task #proposed #auto #p0 #crawl #owner-vast
  - Deliverable: add sections to `VAST/Executive Overview`, `VAST/Engineering Delivery Plan`, `Microsoft/Executive Overview`, `Microsoft/Engineering Alignment & Asks`.
  - Acceptance: each doc clearly states MVP non-goals (e.g., no DFS/HNS semantics, no full Blob emulation, no managed service in Crawl).

## Extracted Placeholders (from legacy monolith)

- [?] Expand integration work detail (identity, encryption, security) and restructure “What/Why” as workstream subsections #task #proposed #auto #p1 #walk #owner-vast
  - Deliverable: a workstream-oriented write-up (identity/security/networking/ops/commercial) referenced from the engineering plan and Microsoft alignment doc.
  - Acceptance: each workstream has scope (Crawl vs Walk vs Run), dependencies, and validation gates.

- [?] Cross-reference workloads ↔ Azure services; tie both to required enablement work; improve PaaS + IaaS narrative cohesion #task #proposed #auto #p0 #crawl #owner-vast
  - Deliverable: add explicit mapping between [Workloads](Appendices/Workloads%20%26%20Reference%20Topologies.md) (W1–W10) and the [Services Matrix](Appendices/Azure%20Native%20Services%20Integration%20Matrix.md).
  - Acceptance: each workload lists “related Azure services” and each service lists “workloads enabled/blocked.”

- [?] Add equivalent Azure PaaS service mapping into the workload matrix and update doc links #task #proposed #auto #p0 #crawl #owner-vast
  - Deliverable: extend the Workload Alignment Matrix with a “Primary Azure services” column (and keep links current).
  - Acceptance: matrix quickly answers “which Azure teams/services are involved per workload.”

## Collateral to Develop (Implied by the Current Content)

- [?] Create 1–2 reference architectures with diagrams + deployment steps for “Crawl” (W2, W5) #task #proposed #auto #p0 #crawl #owner-vast
  - Deliverable: two deployment-ready docs (architecture diagram + steps + assumptions): W2 “central Blob + GPU-adjacent VAST satellite” and W5 “on‑prem tiering to Blob Storage.”
  - Acceptance: includes networking prerequisites (Private Link/ExpressRoute), data movement method (AzCopy/server-side copy), and a simple “day-1 / day-2 ops” checklist.

- [?] Define “AzCopy gate” + “SDK gate” execution plan (test cases, environment, pass/fail) #task #proposed #auto #p0 #crawl #owner-vast
  - Deliverable: a test matrix and step-by-step procedures for validating the Blob API façade with AzCopy and `azure-storage-blob`.
  - Acceptance: covers endpoint patterns (virtual-host + path-style), block uploads (`PutBlock`/`PutBlockList`/`GetBlockList`), range reads, XML list fidelity, `PutBlockFromURL` (range-based), `ETag`/`Last-Modified` semantics, conditional headers, and metadata translation (`x-ms-meta-*`).
  - References:
    - AzCopy command reference (includes `--trusted-microsoft-suffixes`): https://learn.microsoft.com/en-us/azure/storage/common/storage-ref-azcopy
    - AzCopy getting started: https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10
    - `BlobServiceClient(account_url=...)` constructor: https://learn.microsoft.com/en-us/python/api/azure-storage-blob/azure.storage.blob.blobserviceclient?view=azure-python

- [?] Specify the Blob API façade “account + endpoint model” (DNS, certs, account naming, container↔bucket mapping, key lifecycle for SAS/shared-key modes) #task #proposed #auto #p0 #crawl #owner-vast
  - Deliverable: a concrete endpoint model (virtual-host + path-style support, hostname/TLS cert strategy, how `{account}`/containers/blobs map to VAST constructs, and what auth modes are supported in Crawl).
  - References:
    - AzCopy trusted suffixes (for AAD tokens to non-`core.windows.net` domains): https://learn.microsoft.com/en-us/azure/storage/common/storage-ref-azcopy
    - Shared key auth: https://learn.microsoft.com/en-us/rest/api/storageservices/authorize-with-shared-key
    - Put Block From URL: https://learn.microsoft.com/en-us/rest/api/storageservices/put-block-from-url
  - Open questions: do we require `*.core.windows.net`-style domains vs custom domains; how do we get a partner `{blob_suffix}` treated as “trusted” (avoid `--trusted-microsoft-suffixes` in production); what is the token audience/scope for Entra auth in partner endpoints; when is `x-ms-copy-source-authorization` required for `PutBlockFromURL`.

- [?] Define multi-protocol namespace constraints for the Blob façade (naming, file/dir conflicts, case collisions) #task #proposed #auto #p0 #crawl #owner-vast
  - Deliverable: documented rules + chosen Azure-compatible error codes for rejected names/conflicts; align with [Terminology & Conventions](Appendices/Terminology%20%26%20Conventions.md) and [Blob API Requirements (MVP)](Appendices/Blob%20API%20Requirements%20%28MVP%29.md).
  - Acceptance: Azure tooling/SDKs behave predictably (or have documented workarounds); S3/NFS/SMB views remain coherent.
  - References:
    - Naming and referencing containers, blobs, and metadata: https://learn.microsoft.com/en-us/rest/api/storageservices/naming-and-referencing-containers--blobs--and-metadata
    - Common REST API error codes: https://learn.microsoft.com/en-us/rest/api/storageservices/common-rest-api-error-codes

- [?] Define authZ mapping for Blob API façade (Entra principals/claims → VAST users/groups/policies; least-privilege patterns) #task #proposed #auto #p0 #crawl #owner-vast
  - Deliverable: mapping rules, recommended RBAC patterns, and examples for service principals/managed identity.
  - References:
    - Authorize access to blobs using Entra ID: https://learn.microsoft.com/en-us/azure/storage/blobs/authorize-access-azure-active-directory
    - SAS overview: https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview

- [?] Document private connectivity playbooks (PLS + DNS + throughput tuning) for repeatable deployments #task #proposed #auto #p1 #walk #owner-vast
  - Deliverable: a playbook covering PLS exposure, private endpoints, DNS patterns (private zones/split-horizon), and throughput pitfalls (SNAT/conntrack/timeouts).
  - References:
    - Private Link Service overview: https://learn.microsoft.com/en-us/azure/private-link/private-link-service-overview
    - Private endpoint DNS: https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns
    - Storage private endpoints (Blob service model): https://learn.microsoft.com/en-us/azure/storage/common/storage-private-endpoints

- [?] Produce an “ask list” for Microsoft by Azure team (Storage, Private Link, AI Foundry, Fabric, Synapse, Databricks) #task #proposed #auto #p0 #crawl #owner-vast
  - Deliverable: a per-team list of asks with desired outcomes and validation evidence required.
  - Acceptance: aligns with [Microsoft/Engineering Alignment & Asks](Microsoft/Engineering%20Alignment%20%26%20Asks.md) and can be sent as a standalone artifact.

- [?] Extend the Azure services matrix with priority (Crawl/Walk/Run) + owner (VAST/Microsoft/Customer) for each row #task #proposed #auto #p0 #crawl #owner-vast
  - Deliverable: update [Azure Native Services Integration Matrix](Appendices/Azure%20Native%20Services%20Integration%20Matrix.md) to include columns: `Priority`, `Phase`, `Owner`, `Workloads`.
  - Acceptance: matrix becomes a planning tool (not just a snapshot); every row has an owner and an intended validation path.

- [?] Add per-workload “related Azure services” mapping (W1–W10) and link to the services matrix #task #proposed #auto #p0 #crawl #owner-vast
  - Deliverable: update [Workloads & Reference Topologies](Appendices/Workloads%20%26%20Reference%20Topologies.md) so each workload lists the primary services and links to their matrix rows.
  - Acceptance: a reader can traverse Workload → Services → Blockers and understand required enablement work.

- [?] Create a shared “one-slide” architecture diagram (governance tier ↔ performance tier flows) for reuse across executive collateral #task #proposed #auto #p0 #crawl #owner-vast
  - Deliverable: a reusable diagram (Mermaid + exported image) embedded in both exec overviews.
  - Acceptance: the diagram is consistent with terminology and workload W2/W5 narratives.

- [?] Convert the services matrix “blockers” into a validation checklist and capture results per Azure service #task #proposed #auto #p0 #crawl #owner-vast
  - Deliverable: checklist per service (connectivity model + auth assumptions + “hello world” test) and a place to record outcomes.
  - Acceptance: reduces repeated debate; turns “🟡” items into explicit validation work with owners.

## Backlog Sections to Write (from legacy outline)

### Strategic Context & Business Case

- [?] Economics of GPU starvation: why “good enough” storage fails #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: a quantified model (GPU idle cost vs storage/network costs) + 1–2 concrete examples (e.g., checkpoint loops, shard hydration).

- [?] Supply chain & media constraints: flash volatility, HDD capacity tier, procurement lead times #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: narrative + bullets for procurement and BOM volatility; how Blob as capacity tier de-risks flash cycles.

- [?] Success metrics & measurement framework (utilization, throughput, cost, time-to-train, ops burden) #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: a metrics table with definitions, how to measure, and where it shows up (Crawl/Walk/Run).

### Platform Overviews & Capability Alignment

- [?] VAST platform overview (modules + how they map to Azure scenarios) #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: module→use-case mapping (DataStore/DataSpace/DataBase/DataEngine/InsightEngine/SyncEngine/Event Broker) and which workloads each enables.

- [?] Protocol surfaces summary (NFS/SMB/S3/Blob API/Kafka) with “when to use what” #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: “protocol decision guide” for customers and internal SA teams; include tradeoffs (perf/semantics/tooling).

- [?] DRR model and capacity math (what customers actually pay for) #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: a worked example of effective capacity and cost model for hot set vs cold tail.

- [?] Resiliency & failure model (fail‑in‑place, erasure/parity, snapshots) #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: HA/DR design assumptions and what “failure” looks like in tiered/federated deployments.

- [?] Azure platform overview (storage/compute/analytics/integration services relevant to this integration) #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: Azure components that matter, grouped by: storage, networking, compute, analytics, integration/eventing.

- [?] Key architectural constraints (control plane vs data plane, managed VNet walls, picker-based vs endpoint-based services) #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: short “constraints cheat sheet” that maps to blockers in the services matrix.

### Deployment Variants & Reference Topologies

- [?] Variant catalog write-up (A/B/C/D) with selection guidance #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: when-to-use-which guidance with hard constraints (latency, throughput, residency, procurement).

- [?] Selection framework (customer/region/requirements → variant mapping) #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: a decision tree that SAs can use with customers.

- [?] Performance profiles (capacity/bandwidth/IOPS/latency) #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: representative performance envelopes and what factors bottleneck first.

- [?] DRR & efficiency profiles (effective capacity, power, rack density) #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: “density story” for edge GPU sites vs centralized blob lakes.

- [?] Regional constraints (quotas, SKU availability, reservations) #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: checklist of Azure constraints that affect deployments (and mitigations).

- [?] Supply chain & procurement implications (lead times, substitution options) #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: how to plan around lead times for edge deployments and what can substitute.

- [?] Reliability, failure domains, and HA options #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: HA reference patterns aligned to variants A/B/C/D.

- [?] DR/BC reference designs (RPO/RTO targets, replication patterns) #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: DR playbooks for tiered Blob↔VAST deployments.

### Integration Architecture Overview

- [?] Layered integration model (data plane / namespace+metadata / control plane / ops plane / commercial plane) #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: a layered diagram and a “what lives where” mapping.

- [?] Network models (customer VNet vs managed VNet vs public endpoint tradeoffs) #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: a matrix of connectivity options and what breaks in each Azure service.

- [?] Core integration patterns library (direct mount, direct object, Blob API, virtualization, bridging, PLS, cross-region replication) #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: pattern catalog with “when to use” + prerequisites.

### Namespace & Metadata Federation (Federation Plane)

- [?] Problem statement: split-brain namespace and why federation is required #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: a crisp definition of “split-brain” between Blob namespace and VAST namespace, plus why it breaks AI pipelines (grounding, lineage, re-use).
- [?] Federation patterns (VAST master vs Blob master vs proxy/migration-on-read) #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: pattern catalog with diagrams and tradeoffs; explicitly tie each pattern to workloads (e.g., W2 vs W5 vs W6).
- [?] Change detection & reconciliation (Event Grid vs Change Feed vs scans) #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: recommended approach for “fast path” vs “safety net” change detection and how to resolve drift.
  - References:
    - Blob change feed: https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-change-feed
    - Event Grid blob event schema: https://learn.microsoft.com/en-us/azure/event-grid/event-schema-blob-storage
- [?] Metadata mapping model (mtime/etag/content-type/custom metadata) #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: mapping table from Blob properties/headers to VAST metadata, including drift rules and edge cases (rename, overwrite, conditional writes).
  - References:
    - [Blob API Requirements (MVP)](Appendices/Blob%20API%20Requirements%20%28MVP%29.md)
    - [Terminology & Conventions](Appendices/Terminology%20%26%20Conventions.md)
- [?] Security mapping (identity + ACL semantics + drift control) #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: security model for federation (who is authoritative, how to prevent privilege escalation, how to audit).
- [?] Stub/hydration design (metadata-only stubs, cache policies, pinning) #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: hydration semantics and policies (read-through, prefetch, pinning, eviction) aligned to training/inference workloads.
- [?] Consistency/concurrency guarantees + conflict resolution #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: explicit consistency model (eventual vs strong zones), conflict handling, and “last writer wins” rules (or alternatives).
- [?] Scale architecture (sharding, checkpointing, lag tracking, backpressure) #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: scaling strategy and a set of measurable SLOs (sync lag, reconciliation time, backpressure behavior).
- [?] Observability & operations (sync health, lag, reconciliation metrics) #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: dashboards/alerts/runbooks for the federation plane (lag, errors, retries, reconciliation coverage).

### Tiering, Lifecycle & Data Formats

- [?] Tiering modes (opaque vs transparent vs hybrid) #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: decision guide for when to use opaque vs transparent formats and the tradeoffs for ecosystem access (Fabric/Databricks/Synapse).
- [?] Policy framework (hot/warm/cold, retention, compliance, residency) #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: policy model (what knobs exist, who sets them, how enforced) including compliance/residency requirements.
- [?] Cost & transfer considerations (egress, cross-region, cache amplification) #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: cost model + heuristics for cache sizing and transfer behavior; include cross-region replication considerations.
- [?] Portability & exit strategy #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: “how to leave” guidance (data formats, metadata, replication) to reduce buyer risk.

### Networking & Connectivity

- [?] Connectivity design principles (private-first, deterministic routing) #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: a set of design principles and anti-patterns for hybrid Blob↔VAST deployments.
- [?] Private endpoints & Private Link fundamentals (what Azure services expect) #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: “Private Link 101” section focused on partner endpoints and managed services that require managed private endpoints.
- [?] Private Link Service (PLS) model for VAST endpoints (S3/Blob API/NFS) #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: reference architecture for exposing VAST behind Standard Load Balancer + PLS, including DNS and certificate strategy.
- [?] PLS alias & connection approval workflow (who approves, how automated) #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: operational workflow (approval, automation, auditing) for customer private endpoints and managed private endpoints.
- [?] DNS architecture (private zones, split-horizon, managed VNet DNS) #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: DNS playbook for customer VNets and managed VNets (Fabric/Synapse) including split-horizon patterns.
- [?] Customer VNet connectivity (peering/routing/NSGs/ExpressRoute) #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: connectivity checklist and troubleshooting guide for customers (routes, NSGs, firewall, ExpressRoute).
- [?] Managed VNet connectivity patterns (Fabric/Synapse/serverless) #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: “managed VNet wall” patterns and what is (and isn’t) possible per service; link back to the services matrix.
- [?] Throughput & scale limits (SLB, SNAT, conntrack, timeouts, keep-alive) #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: performance tuning + limits guide (client concurrency, connection reuse, Azure load balancer constraints).
- [?] Cross-region backbone patterns (global peering, vWAN, replication paths) #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: reference patterns for cross-region replication (Azure backbone vs public internet) and how dedup affects bandwidth.

### Identity, Security, Compliance & Governance

- [?] Threat model & security posture #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: threat model (assets, adversaries, controls) for partner endpoint + hybrid deployments.
- [?] Identity integration (Entra ID, managed identity patterns, compatibility modes) #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: recommended identity patterns and what we support in each phase (OAuth, MSI, SAS, Shared Key).
- [?] Key management (Key Vault, rotation, customer-managed keys) #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: CMK strategy (Key Vault integration, rotation, tenant separation) aligned to “Run” requirements.
- [?] Perimeter controls (NSP, firewalls, egress policies, exfiltration control) #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: network perimeter patterns and guidance to prevent data exfiltration in regulated deployments.
- [?] Shared responsibility model (VAST vs Microsoft vs customer) #task #proposed #auto #p2 #backlog #owner-vast
  - Deliverable: shared responsibility table by phase (Crawl/Walk/Run) and by integration surface (data plane, identity, networking, monitoring).
