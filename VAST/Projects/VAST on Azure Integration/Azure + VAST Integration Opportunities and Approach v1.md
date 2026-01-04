VAST + Microsoft Azure Integration

Do not build “VAST-as-Blob” as a product goal. Build VAST as the GPU-adjacent performance tier + global namespace, while Azure Blob remains the system-of-record capacity tier and ecosystem “gravity well.” The integration succeeds if customers can:

1. Stage training data to GPU-adjacent VAST fast and safely (from central Azure data lakes),
2. Push checkpoints + artifacts back to the central estate, and
3. Continue using Azure-native services and tooling without refactoring—_where it matters_.

The “What” in one sentence

A set of integration patterns that connect Azure Blob–centric data estates to distributed GPU-adjacent VAST clusters using:

- a minimum Blob REST API façade on VAST for _Azure-native data movement tooling_, and
- optional tiering + namespace synchronization to reduce TCO and avoid data silos.

The “Why” in one sentence

AI/HPC is becoming a distributed compute problem (GPUs anywhere power exists) while data remains a centralized governance/economics problem (multi-exabyte lakes). VAST + Azure is a practical way to reconcile the two.

The “How” (phased)

Phase 1 (MVP):

- Implement a VAST “Blob API façade” whose first contract is: AzCopy workflows work without code changes (configuration allowed).
- Focus on service-to-service copy primitives (Put Blob From URL / Put Block From URL + Put Block List) and the minimum list/get operations that AzCopy depends on. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/common/storage-reference-azcopy-map-commands-to-rest-operations "Map of AzCopy v10 commands to Azure Blob Storage ..."))

Phase 2:

- Add tiering/offload from VAST to Blob, starting with an opaque VAST-native layout (best economics), plus an optional transparent export mode for specific ecosystem needs.

Phase 3:

- Pursue deeper Azure-native integration for first-party services that can’t point at arbitrary endpoints (control-plane/resource provider bindings), likely via Azure-side proxy patterns (e.g., “Blob as a reverse proxy to external object stores”) and/or formal joint engineering.

Key points uncovered (current)

- AzCopy’s “server-side copy” primitives rely on Blob REST operations like Put Blob From URL and sometimes Put Block From URL + Put Block List. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/common/storage-reference-azcopy-map-commands-to-rest-operations "Map of AzCopy v10 commands to Azure Blob Storage ..."))
- Azure Blob Change Feed provides an ordered, durable transaction log of blob changes—useful for namespace sync. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-change-feed "Change feed support in Azure Blob Storage"))
- Microsoft Fabric supports “S3-compatible shortcuts” (not only AWS S3). This is a major “easy win” integration point for VAST’s S3 endpoint—no Blob emulation required for Fabric access patterns. ([Microsoft Learn](https://learn.microsoft.com/en-us/fabric/onelake/create-s3-compatible-shortcut "Create an Amazon S3 compatible shortcut - Microsoft Fabric"))
- The VAST + Microsoft partnership is positioned as bringing “VAST AI OS” to Azure for hybrid/multi-cloud AI workflows. ([VAST Data](https://www.vastdata.com/press-releases/vast-data-partners-with-microsoft-to-power-the-next-wave-of-agentic-ai "VAST Data Partners with Microsoft to Power the Next Wave ..."))

Research needed to complete this section

- Quantify the top 3 customer pipelines (OpenAI-style, MAI-style, enterprise AI factory) with real data volumes, object size distributions, concurrency, and checkpoint patterns.
- Validate whether AzCopy CLI can be configured to target a non-Microsoft endpoint (or whether we require Microsoft-hosted DNS/TLS integration).
- Identify top 10 Azure services to prioritize for “touchless” integration and which are blocked by control plane constraints.

---

Framing: scope, assumptions, non-goals

Scope

This document covers:

- Business strategy (“Why”)
- Workload alignment (“What we solve”)
- Feature alignment and integration inventory
- Architecture options and MVP/roadmap
- Engineering responsibilities (VAST vs Microsoft vs joint)

Assumptions (explicit)

- Azure Blob is the default persistence substrate for a large fraction of Azure services and customer data lakes.
- Modern AI factories are multi-region + multi-cloud + on-prem GPU fleets with centralized governance/data lakes.
- VAST’s current cloud deployment model (VM-based) is strong for endpoint + caching + GPU-adjacent, but economics for multi-exabyte “cold” data push toward tiering/offload (Blob HDD economics).
- Some critical Azure services integrate storage via resource-provider control plane (select a storage account) rather than “enter an endpoint URL,” meaning deep ecosystem integration may require Microsoft work.

Non-goals (opinionated)

- Not building full Blob feature parity (Append Blobs, Page Blobs, full ADLS Gen2/HNS/DFS endpoint parity) in MVP.
- Not turning VAST into a “Blob storage account replacement.”
- Not expecting Azure first-party services to consume VAST endpoints _directly_ without a deliberate Microsoft integration strategy.

Key points uncovered (current)

- AzCopy depends on a bounded set of Blob operations for common copy/sync workflows (documented mapping exists). ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/common/storage-reference-azcopy-map-commands-to-rest-operations "Map of AzCopy v10 commands to Azure Blob Storage ..."))
- Fabric shortcut support includes S3-compatible endpoint URLs (good for VAST S3). ([Microsoft Learn](https://learn.microsoft.com/en-us/fabric/onelake/create-s3-compatible-shortcut "Create an Amazon S3 compatible shortcut - Microsoft Fabric"))

Research needed

- A “hard list” of Blob features to explicitly defer (and the customer/workload rationale for each deferral).
- A crisp definition of “AzCopy works unmodified” (what flags/configuration changes are allowed?).

---

Partnership thesis and positioning

The strategic positioning

Azure is the:

- ecosystem control plane,
- security/governance anchor,
- and the cost-effective capacity substrate.

VAST is the:

- GPU-adjacent performance tier,
- global namespace / data spaces fabric,
- and the high-performance multi-protocol gateway for AI pipelines.

The partnership wins when it enables:  
“Centralize governance and durability in Azure; decentralize performance to wherever GPUs exist.”

Why now

- Distributed GPU reality: GPUs are landing where power is, not where the central lake is.
- Tooling inertia: Azure-native movement and orchestration often standardize on AzCopy-like primitives, and customers resist refactors.
- Ecosystem adjacency: Fabric and OneLake are increasingly the “data UX,” and the fact that Fabric supports S3-compatible shortcuts gives VAST a low-friction analytics touchpoint immediately. ([Microsoft Learn](https://learn.microsoft.com/en-us/fabric/onelake/create-s3-compatible-shortcut "Create an Amazon S3 compatible shortcut - Microsoft Fabric"))
- Partnership momentum: VAST + Microsoft publicly position VAST AI OS as running on Azure to support hybrid/multi-cloud “agentic AI” workflows. ([VAST Data](https://www.vastdata.com/press-releases/vast-data-partners-with-microsoft-to-power-the-next-wave-of-agentic-ai "VAST Data Partners with Microsoft to Power the Next Wave ..."))

Success metrics (what we should commit to)

MVP success metrics (Phase 1):

- Time-to-stage N TB of training data to a GPU-adjacent site (P50/P95).
- Checkpoint round-trip time (GPU → VAST → central lake) with target cadence.
- No-refactor: AzCopy-based workflows succeed (with documented configuration).
- Security posture: private networking supported for enterprise deployments (Private Link patterns).

Product success metrics (Phase 2+):

- Working set economics: policy-driven offload to Blob reduces flash footprint.
- Operational simplicity: unified observability, predictable failure modes, clear support boundaries.
- Ecosystem integration depth: number of Azure services that can access data without bespoke glue.

Key points uncovered (current)

- Public partnership messaging already frames VAST on Azure as enabling unified hybrid workflows. ([VAST Data](https://www.vastdata.com/press-releases/vast-data-partners-with-microsoft-to-power-the-next-wave-of-agentic-ai "VAST Data Partners with Microsoft to Power the Next Wave ..."))
- Fabric provides an immediate integration path via S3-compatible shortcuts. ([Microsoft Learn](https://learn.microsoft.com/en-us/fabric/onelake/create-s3-compatible-shortcut "Create an Amazon S3 compatible shortcut - Microsoft Fabric"))

Research needed

- Quantify Microsoft’s internal and top customer priority workloads (which services matter most).
- Validate supply-chain claims (flash constraints) only if we want to use them as a primary pillar; otherwise frame as a risk factor, not the main argument.

---

Workload catalog and end-to-end flows

Pattern: Every workload gets: problem statement, topology, data flow, integration touchpoints, MVP definition, and what we defer.

Workload A: On-prem VAST + burst compute on Azure (current strength)

Problem: compute bursts to Azure; dataset remains on-prem; customers need consistent namespace and performance.  
Topology: on-prem VAST cluster ↔ VAST-on-Azure endpoints (cache + protocol termination) ↔ Azure compute.  
Primary protocols: NFS and S3.

MVP stance: already viable; document as “Phase 0” baseline and reference architecture.

Key integration points: data spaces/global namespace between clusters; WAN optimization; security and identity.

Research needed: baseline cost/perf envelope and when the VM-based model breaks (capacity economics).

---

Workload B: Central Azure data lake + GPU-adjacent VAST clusters (the focus)

Problem: centralized exabyte-scale data lake in hero Azure region; GPUs distributed across satellite regions / neo-clouds / on-prem. Need fast staging and checkpoint synchronization.  
Primary requirement: _Data movement + orchestration_ that doesn’t require refactoring.

Canonical flow (training):

- Data ingested and curated into central Blob lake
- Training shards staged to GPU-adjacent VAST
- Training happens on GPU cluster
- Checkpoints + artifacts returned to central lake

flowchart LR

  subgraph Hero[Hero Azure Region]

    Blob[(Azure Blob / Central Lake)]

    ETL[Ingest + Transform Pipeline]

  end

  subgraph Edge[GPU Sites: Satellite Azure Regions / Neo-cloud / On-prem]

    VAST[(VAST GPU-Adjacent Cluster)]

    GPUs[GPU Training / Inference]

  end

  ETL --> Blob

  Blob <--> |stage shards + return checkpoints| VAST

  VAST <--> GPUs

MVP stance: this is the “why Blob API façade exists.” Not to replace Blob, but to make movement frictionless.

Key integration points:

- Azure-native mover primitives (AzCopy-like) → VAST Blob façade
- Optionally, VAST S3/NFS for compute adjacency
- Security: private networking, scoped access, audit logs

Research needed: confirm customer patterns (tooling: AzCopy wrappers vs rclone; object sizes; concurrency; checkpoint structure).

---

Workload C: Tiering/offload from VAST to Azure Blob (economics and supply)

Problem: VAST is high-performance flash; customers need a low-cost capacity tier, especially for cold data, retention, or “dataset history.”  
Topologies: GPU-adjacent VAST at sites + optional central VAST + Blob as capacity substrate.

Key decision fork: opaque vs transparent tiering (covered later).

Research needed: quantify what percentage of data is “working set” vs “cold set” in target AI factories.

---

Workload D: “Azure ecosystem access” (Azure services still think they’re using Blob)

Problem: many Azure services bind to storage via control plane and expect storage accounts, private endpoints, and NSP policies.  
Implication: direct endpoint substitution with a 3P VM endpoint often fails.

MVP stance (opinionated):

- Don’t promise broad “Azure service compatibility” via Blob emulation in Phase 1.
- Instead:

1. enable Fabric access through S3-compatible shortcuts (fast win), and
2. pursue Azure-side proxy/control-plane integration as a joint roadmap item.

Research needed: service-by-service matrix (what requires RP integration vs supports endpoint URL).

---

Key points uncovered (current)

- Fabric supports S3-compatible shortcuts, which should allow VAST S3 endpoints to present data to Fabric without Blob emulation. ([Microsoft Learn](https://learn.microsoft.com/en-us/fabric/onelake/create-s3-compatible-shortcut "Create an Amazon S3 compatible shortcut - Microsoft Fabric"))
- Azure Blob Change Feed provides ordered logs that can underpin namespace sync. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-change-feed "Change feed support in Azure Blob Storage"))

---

Integration surface area inventory

This is the exhaustive “coverage map” you asked for—organized so we don’t miss categories.

Integration layers

|Layer|Integration Point|Examples|Notes|
|---|---|---|---|
|Data plane|Protocol endpoints|NFS/SMB/S3 today; Blob API façade proposed|Blob façade is compatibility-driven, not “new product surface for everyone”|
|Data movement|Movers + server-side copy|AzCopy, Storage Mover-like primitives|AzCopy uses Put Blob From URL / Put Block From URL patterns ([Microsoft Learn](https://learn.microsoft.com/en-us/rest/api/storageservices/put-blob-from-url "Put Blob From URL (REST API) - Azure Storage"))|
|Metadata/namespace|Change log + indexing|Change Feed, Event Grid, periodic reconciliation|Change Feed is ordered/durable log ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-change-feed "Change feed support in Azure Blob Storage"))|
|Identity/auth|AuthN/Z|Entra ID, SAS/shared key, service principals|Blob façade must pick a limited auth set|
|Networking|Private connectivity|Private Link / Private Link Service|Private Link supports partner services via private endpoint ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview "What is Azure Private Link?"))|
|Security perimeter|Exfiltration prevention|Azure NSP (PaaS), private endpoints|NSP is about logical boundaries for PaaS resources ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security-perimeter "Network Security Perimeter for Azure Storage"))|
|Control plane|Resource provider integration|“Pick a storage account” UX|Often Microsoft work required|
|Ops|Observability & lifecycle|Telemetry, upgrade, support|VAST Uplink exists as SaaS mgmt layer (confirm integration with Azure Monitor) ([Vast Support Portal](https://support.vastdata.com/s/document-item?nocache=https%3A%2F%2Fsupport.vastdata.com%2Fs%2Fdocument-item%3FbundleId%3Duplink-user-guide%26_LANG%3Denus "About VAST Uplink"))|

Key points uncovered (current)

- Private Link covers access to PaaS and “Azure hosted customer-owned/partner services” using private endpoints. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview "What is Azure Private Link?"))
- Private Link Service includes destination-side NAT and can use TCP Proxy Protocol v2 for source IP metadata propagation patterns. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/private-link/private-link-service-overview "What is Azure Private Link service?"))
- Change Feed is a viable primitive for ordered namespace sync. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-change-feed "Change feed support in Azure Blob Storage"))

Research needed

- Confirm “private-only” requirements for Microsoft internal adoption (policy baseline).
- Determine if VAST should ship a reference Private Link Service + private DNS deployment pattern as default.

---

Architecture options and a decision framework

Options (the real ones)

1. Blob façade on VAST (MVP) — enable Azure movers and server-side copy semantics into/out of VAST.
2. Opaque tiering to Blob — VAST stores reduced/encrypted extents in Blob (Blob as capacity substrate).
3. Transparent objects + VAST indexing — Blob remains canonical; VAST mirrors metadata and caches/stages.
4. Azure-side reverse proxy (“Blob proxies to external”) — Azure services talk to Blob; Blob fetches data from VAST/S3 endpoints (requires Microsoft work).

Decision matrix (opinionated)

|Criterion|(1) Blob façade|(2) Opaque tiering|(3) Transparent indexing|(4) Azure reverse proxy|
|---|---|---|---|---|
|Fastest path to customer value|High|Medium|Medium|Low|
|No-refactor tooling compatibility|High|Medium|High|High|
|Azure ecosystem compatibility (first-party services)|Medium|Low|High|High|
|Performance for GPU-adjacent|High|High|High (for cache)|Medium–High|
|Best TCO for cold data|Medium|High|Medium|Medium|
|Complexity/engineering risk|Medium|Medium|High|High (MSFT)|
|Customer portability (data usable without VAST)|Medium|Low|High|High|
|Vendor stickiness|Medium|High|Medium|Low–Medium|

Key points uncovered (current)

- The existence and importance of Put Blob From URL and Put Block From URL for server-side copy is documented and central to AzCopy. ([Microsoft Learn](https://learn.microsoft.com/en-us/rest/api/storageservices/put-blob-from-url "Put Blob From URL (REST API) - Azure Storage"))
- Fabric S3-compatible shortcuts reduce the need for Blob emulation in analytics scenarios. ([Microsoft Learn](https://learn.microsoft.com/en-us/fabric/onelake/create-s3-compatible-shortcut "Create an Amazon S3 compatible shortcut - Microsoft Fabric"))

Research needed

- Define what “Azure reverse proxy” could realistically support (semantics, performance, auth).
- Confirm which workloads truly require transparent Blob-native objects vs are fine with opaque VAST-managed extents.

---

Recommended path

Recommendation (the strong stance)

Build Option (1) first, pair it with a narrowly-scoped Option (2), and pursue Option (4) as the long-term Azure ecosystem unlock. Option (3) is powerful but should be treated as “only if we must,” because it is the hardest to make correct (consistency, security drift, namespace sync).

Phase 1 (MVP): Blob façade for movers + staging

- Goal: accelerate data movement into/out of GPU-adjacent VAST, using Azure-native copy patterns.
- Deliverable: “AzCopy Compatibility Contract” + automated test harness.

Phase 2: Opaque tiering to Blob + optional export

- Default: opaque (VAST-optimized extents) to maximize data reduction and economics.
- Optional: “export mode” for specific datasets that must remain usable directly in Blob.

Phase 3: Joint Azure integration (“Blob proxies to VAST”)

- Objective: make first-party Azure services access VAST-backed data without needing endpoint reconfiguration.

What we explicitly do _not_ do early

- Do not chase full Blob API parity.
- Do not promise universal Azure service compatibility with a VM-hosted endpoint.

---

MVP spec: “AzCopy Compatibility Contract” for a VAST Blob API façade

Treat AzCopy as the spec: we implement the minimum Blob REST surface that AzCopy uses for copy/sync patterns—and we match semantics and error models closely enough that it “just works.”

Why this exists (and why S3 isn’t enough)

AzCopy’s S3 support is AWS URL-pattern specific and historically rejects other S3 providers/endpoints, which undermines “just point AzCopy at a VAST S3 endpoint.” ([GitHub](https://github.com/Azure/azure-storage-azcopy/issues/1587 "AzCopy does not support S3 providers besides AWS #1587"))  
Therefore, Blob compatibility is the pragmatic path for Azure-native movers.

MVP Blob operations (initial list)

This list is grounded by Microsoft’s published “AzCopy commands ↔ REST operations” mapping and Blob REST docs. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/common/storage-reference-azcopy-map-commands-to-rest-operations "Map of AzCopy v10 commands to Azure Blob Storage ..."))

Required for enumeration and diff

- List Blobs (container listing)
- Get Blob Properties (HEAD / properties)
- Get Blob (including range reads)

Required for upload

- Put Blob (single shot for small blobs) ([Microsoft Learn](https://learn.microsoft.com/en-us/rest/api/storageservices/put-blob "Put Blob (REST API) - Azure Storage"))
- Put Block (stage blocks) ([Microsoft Learn](https://learn.microsoft.com/en-us/rest/api/storageservices/put-block "Put Block (REST API) - Azure Storage"))
- Put Block List (commit block blob)

Required for service-to-service copy (critical)

- Put Blob From URL (copy entire source blob into destination) ([Microsoft Learn](https://learn.microsoft.com/en-us/rest/api/storageservices/put-blob-from-url "Put Blob From URL (REST API) - Azure Storage"))
- Put Block From URL + Put Block List (partial updates / large objects) ([Microsoft Learn](https://learn.microsoft.com/en-us/rest/api/storageservices/put-block-from-url "Put Block From URL (REST API) - Azure Storage"))

Put Blob From URL copies the entire blob and isn’t for partial updates; for partial updates you use Put Block From URL + Put Block List. ([Microsoft Learn](https://learn.microsoft.com/en-us/rest/api/storageservices/put-blob-from-url "Put Blob From URL (REST API) - Azure Storage"))

Required for delete/sync correctness

- Delete Blob
- (Optional in MVP) Create Container / Delete Container if workflow demands

Authentication modes (MVP choice)

Opinionated MVP auth set:

- SAS-like signed URL tokens (closest to tooling patterns)
- Shared Key style signing (for service principals / controlled environments)

Defer (Phase 2/3):

- Full Entra ID OAuth flows for the façade unless required by top customers.

Research needed: what auth AzCopy workflows _actually_ use in target environments (SAS vs OAuth vs shared key).

Semantics we must match (or clearly document gaps)

|Semantic|Why AzCopy cares|MVP stance|
|---|---|---|
|ETag / If-Match / If-None-Match|correctness + sync|Implement or document as “best effort”|
|Last-Modified|diffing|Implement|
|Range reads|resume/download|Implement|
|Retryable error codes|throughput + resilience|Match common Azure patterns|
|Multipart/blocks|large objects|Implement Put Block + Put Block List|
|Copy source auth|server-side copy|Support source URLs with signed access|

Compatibility test harness

Definition of done:

- A CI suite that runs a matrix of AzCopy operations against VAST Blob façade:

- local → VAST
- VAST → local
- Blob → VAST (service-to-service copy patterns)
- VAST → Blob
- sync/diff correctness tests

- Include chaos tests: transient failures, partial block uploads, retry behavior.

Proposed minimal OpenAPI sketch (illustrative)

openapi: 3.0.0

info:

  title: VAST Blob API Facade (MVP)

  version: 0.1

paths:

  /{container}:

    get:

      summary: List Blobs

      parameters:

        - in: query

          name: comp

          schema: { type: string, enum: [list] }

      responses:

        "200": { description: OK }

  /{container}/{blob}:

    head:

      summary: Get Blob Properties

      responses:

        "200": { description: OK }

    get:

      summary: Get Blob (supports Range)

      parameters:

        - in: header

          name: Range

          schema: { type: string }

      responses:

        "200": { description: OK }

    put:

      summary: Put Blob (small upload) OR Put Blob From URL (when x-ms-copy-source present)

      responses:

        "201": { description: Created }

  /{container}/{blob}?comp=block:

    put:

      summary: Put Block / Put Block From URL

      responses:

        "201": { description: Created }

  /{container}/{blob}?comp=blocklist:

    put:

      summary: Put Block List

      responses:

        "201": { description: Created }

This is a shape sketch, not a final contract. The precise URI formats, headers, versions, and auth need to be derived from AzCopy dependency analysis.

Research needed (critical)

- Derive the exact REST calls, headers, and expected behaviors from AzCopy (code + runtime traces).
- Validate whether AzCopy CLI can target the façade endpoint without code changes (DNS/TLS/endpoint inference constraints).
- Decide whether the façade must support Put Blob From URL and/or Put Block From URL for the primary workflows (likely yes). ([Microsoft Learn](https://learn.microsoft.com/en-us/rest/api/storageservices/put-blob-from-url "Put Blob From URL (REST API) - Azure Storage"))

---

Tiering/offload designs: opaque vs transparent vs hybrid

Option 2: Opaque tiering (VAST-native extents in Blob)

Concept: VAST writes reduced/encrypted/erasure-coded extents into Blob. Blob is cheap capacity; VAST remains the only reader/writer.

flowchart LR

  App[Client / GPU Workload] --> VAST[VAST Endpoints]

  VAST -->|tier cold extents| Blob[(Azure Blob)]

  Blob -->|hydrate on read| VAST

Pros (why this is default):

- Best TCO (data reduction remains effective)
- Cleaner correctness model (single writer semantics via VAST)
- Stronger “stickiness” (strategically valuable for VAST)

Cons:

- Azure-native services cannot directly consume the data in Blob.

Option 3: Transparent objects (Blob-native) + VAST indexing/caching

Concept: Blob remains the canonical store. VAST mirrors/indexes namespace and caches/stages data adjacent to GPUs.

flowchart LR

  Blob[(Azure Blob - Canonical)]

  CF[Change Feed / Events] --> VASTMeta[VAST Metadata Mirror]

  Blob --> VASTCache[VAST Cache/Stage]

  VASTMeta --> VASTCache

  GPUs --> VASTCache

Pros:

- Azure ecosystem compatibility
- Customer portability (data remains usable without VAST)

Cons (why it’s hard):

- Namespace sync correctness, race conditions, partial uploads
- Dual auth models (policy drift)
- Potentially high operational complexity

Hybrid recommendation

Default opaque tiering for:

- GPU-adjacent staging areas
- checkpoint repositories
- cold retention behind VAST

Transparent mode only for:

- datasets explicitly required by Azure services to read directly from Blob
- interop scenarios where customer insists on portability

Key points uncovered (current)

- Blob Change Feed can support ordered synchronization in transparent designs. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-change-feed "Change feed support in Azure Blob Storage"))
- Fabric can access VAST data via S3-compatible shortcuts, potentially reducing transparent-tiering pressure for analytics. ([Microsoft Learn](https://learn.microsoft.com/en-us/fabric/onelake/create-s3-compatible-shortcut "Create an Amazon S3 compatible shortcut - Microsoft Fabric"))

Research needed

- Performance benchmarks: hydration penalties; cache hit/miss behavior; checkpoint write patterns.
- Correctness model for transparent mode: conflict policies, delete/versioning behavior, and lifecycle policies.

---

Namespace + metadata synchronization

Building blocks

1. Azure Blob Change Feed: ordered, durable, immutable log of blob and metadata changes. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-change-feed "Change feed support in Azure Blob Storage"))
2. Event Grid: event-driven triggers for blob events (useful but not a full ordered log). ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-event-overview "Reacting to Blob storage events - Azure"))
3. Reconciliation scanner: periodic scan to heal missed events.

Opinionated approach

- If we do transparent mode: use Change Feed as the authoritative change stream + periodic reconciliation.
- Avoid relying solely on events for correctness.

Research needed

- Retention and cost characteristics of Change Feed for very high change rates.
- How to handle multi-region replication scenarios and whether Change Feed semantics meet needs.

---

Security and networking

Non-negotiable: private-only access must be possible

Enterprises will not accept “public endpoint + IP allowlist” for core data plane in many cases.

Recommended pattern: Azure Private Link Service for VAST endpoints

Azure Private Link can provide private endpoint access to partner services. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview "What is Azure Private Link?"))  
Private Link Service performs destination-side NAT to avoid IP conflicts. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/private-link/private-link-service-overview "What is Azure Private Link service?"))  
It can be combined with TCP Proxy Protocol v2 to propagate original client IP information patterns. ([TECHCOMMUNITY.MICROSOFT.COM](https://techcommunity.microsoft.com/t5/fasttrack-for-azure/tcp-proxy-protocol-v2-with-azure-private-link-service-deep-dive/ba-p/3574968 "TCP Proxy Protocol v2 with Azure Private Link Service"))

Design sketch:

- VAST endpoints behind an Azure Standard Load Balancer
- Private Link Service attached
- Consumers create private endpoints in their VNets
- Private DNS zones for name resolution

Network Security Perimeter (NSP) implications

NSP creates logical isolation boundaries for PaaS resources (like Storage, Key Vault) and helps prevent unwanted data exfiltration from storage resources. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security-perimeter "Network Security Perimeter for Azure Storage"))  
Implication: VAST (IaaS/VM-based) won’t “be” an NSP resource, but it must interoperate with NSP-secured dependencies (Key Vault, etc.).

Research needed

- Validate best-practice reference architecture for Private Link Service scaling limits and operational patterns.
- Determine if we need proxy protocol support in VAST endpoints for audit/logging requirements.

---

Azure service touchpoints matrix

This is intentionally a first-pass list. We’ll expand to 50+ services in an appendix.

|Azure service|Typical storage binding model|VAST integration path|Feasibility in Phase 1|
|---|---|---|---|
|Microsoft Fabric / OneLake|Shortcut-based virtualization|Use VAST S3 via S3-compatible shortcut ([Microsoft Learn](https://learn.microsoft.com/en-us/fabric/onelake/create-s3-compatible-shortcut "Create an Amazon S3 compatible shortcut - Microsoft Fabric"))|High|
|Azure AI Foundry / ML|Often workspace-linked storage accounts|Likely needs Azure-side integration or mount NFS/S3 at compute layer|Medium|
|Data movement (AzCopy)|Direct REST to Blob endpoints|VAST Blob façade (AzCopy contract) ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/common/storage-reference-azcopy-map-commands-to-rest-operations "Map of AzCopy v10 commands to Azure Blob Storage ..."))|High (pending endpoint/TLS feasibility)|
|AKS|CSI / NFS / S3 clients|Use NFS/S3 endpoints, optional Private Link|High|
|Event-driven workflows|Blob events, Event Grid|If façade supports events, maybe; otherwise use change feed + integration glue|Medium|
|Data Factory / Pipelines|Connector model, often storage-account centric|Likely requires Microsoft connector work or proxy approach|Low–Medium|

Research needed

- Build the real matrix for the top 25 services and classify:

- “Endpoint-configurable” vs “storage-account-only”
- “private networking required” vs “public acceptable”
- “data plane only” vs “control plane required”

---

Engineering plan: who builds what

VAST workstreams (Phase 1–2)

1. Blob API façade (AzCopy contract)
2. Compatibility harness + CI regression suite
3. Data movement performance + resilience (retries, resumability)
4. Tiering engine (opaque first) + hydration policies
5. Optional transparent export mode (later)
6. Private Link Service reference deployment templates

Microsoft workstreams (Phase 3+)

1. Evaluate “Blob reverse proxy to external object stores” feasibility and roadmap
2. Control plane integration paths for first-party services that cannot target custom endpoints
3. Joint security posture review and guidance

Joint workstreams

- Reference architectures (hero region + satellites + neo-cloud)
- Pilot customers + workload validation
- Support model / escalation boundaries

---

Roadmap and milestones

gantt

  title VAST + Azure Integration Roadmap (Draft)

  dateFormat  YYYY-MM-DD

  section Phase 0 (Baseline)

  Document existing burst-to-Azure patterns         :done, p0, 2025-12-01, 30d

  section Phase 1 (MVP)

  AzCopy Compatibility Contract (spec + tests)      :active, p1a, 2025-12-18, 45d

  Implement Blob façade MVP                         :p1b, 2026-02-01, 90d

  Private Link reference architecture               :p1c, 2026-02-01, 60d

  section Phase 2 (Economics)

  Opaque tiering to Blob + hydration policies       :p2a, 2026-05-01, 120d

  Optional export mode                              :p2b, 2026-07-15, 90d

  section Phase 3 (Deep Azure Integration)

  Azure-side proxy/control-plane integration        :p3, 2026-09-01, 180d

Dates are placeholders; we will replace with actual planning once MVP scope is locked.

---

Risks, constraints, and mitigations

|Risk|Why it matters|Mitigation|
|---|---|---|
|AzCopy endpoint/TLS constraints|Blob façade may be correct but unreachable by existing tooling|Validate early; document allowed config; consider joint Microsoft enablement|
|Overbuilding Blob parity|Infinite scope|Strict MVP contract; defer long tail|
|Transparent mode correctness|Consistency + security drift|Opaque-by-default; transparent only for validated cases|
|Security posture mismatch|Public endpoints may be unacceptable|Private Link Service reference pattern ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview "What is Azure Private Link?"))|
|Ecosystem integration blocked by control plane|Services require storage accounts|Phase 3 proxy/RP integration strategy|

---

Research backlog

This is the “follow-ups we must defend” list—turned into a backlog we can execute.

1) Workload validation (highest priority)

- Confirm actual data movement tools used (AzCopy wrappers vs rclone) and why.
- Quantify dataset staging and checkpoint patterns (size, frequency, atomicity).

2) AzCopy dependency analysis (turn it into the spec)

- Enumerate exact Blob REST calls and required headers/versions.
- Confirm required semantics: ETags, conditional headers, error codes.
- Validate feasibility of pointing AzCopy at non-Azure endpoints; identify required config or MSFT support.

3) Tiering decision record

- Benchmark opaque tiering reduction ratios and hydration costs.
- Identify top scenarios requiring transparent objects.
- Define security and portability positions.

4) Azure services integration matrix

- Build the top 25 service matrix; prioritize top 10 by value.
- Identify which need Azure engineering (control plane / proxy).

5) Networking + security posture

- Validate Private Link Service scale limits, logging requirements, and proxy protocol needs. ([TECHCOMMUNITY.MICROSOFT.COM](https://techcommunity.microsoft.com/t5/fasttrack-for-azure/tcp-proxy-protocol-v2-with-azure-private-link-service-deep-dive/ba-p/3574968 "TCP Proxy Protocol v2 with Azure Private Link Service"))
- Define minimum acceptable posture for Microsoft internal usage (NSP implications, Key Vault, etc.). ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security-perimeter "Network Security Perimeter for Azure Storage"))

---

Appendix: glossary

- GPU-adjacent storage: storage deployed close to GPUs to reduce stall time and improve throughput.
- Hero region: large Azure region with massive compute/storage capacity for central data estates.
- Satellite region: smaller Azure region used for GPU placement close to power/capacity availability.
- Opaque tiering: data is stored in Blob in VAST-managed internal format; Blob isn’t directly usable without VAST.
- Transparent tiering: data stored as standard objects in Blob; VAST indexes/caches/stages and keeps namespace consistent.
- Change Feed: ordered transaction log of blob changes in a storage account. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-change-feed "Change feed support in Azure Blob Storage"))
- Private Link / Private Link Service: private endpoint connectivity to PaaS and partner services. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview "What is Azure Private Link?"))

---

Suggested next iteration (no questions—just a plan)

1. We “lock” the outline above as v0.1.
2. We pick three workloads to fully spec first:

- Central Blob → GPU-adjacent VAST staging
- Checkpoints → central Blob return
- Tiering/offload

4. We immediately produce two standalone appendices:

- Appendix C: AzCopy Compatibility Contract (full REST+semantics list)
- Appendix D: Opaque vs Transparent Decision Record (with benchmark plan)

If you paste any additional notes (or your own preferred structure), I’ll revise this draft into v0.2 and start fleshing out the API contract and the Azure services matrix in much more detail.

VAST + Microsoft Azure Integration

What / Why / How — Working Draft v0.2 (2025-12-18)

Changelog vs v0.1 (key refactors)

- Added: Multi-variant deployment model (GPU-adjacent ODM, Azure IaaS on L‑series v4 VMs, and “Azure bare metal / Azure-provided hardware” variants).
- Corrected/updated Azure SKU assumptions: treat L‑series v4 (Laosv4 / Lasv4 / Lsv4) as the current “center-of-gravity” for Azure IaaS deployments; Lasv5 is now treated as _future/unknown_ pending confirmation. ([TECHCOMMUNITY.MICROSOFT.COM](https://techcommunity.microsoft.com/blog/azurecompute/announcing-the-general-availability-of-azure-laosv4-lasv4-and-lsv4-storage-optim/4422481 "Announcing the general availability of Azure Laosv4, Lasv4, and Lsv4 storage optimized VMs | Microsoft Community Hub"))
- Expanded integration section into a Pattern Library + Service Matrix (scales to 100+ services without becoming unreadable).
- Strengthened “data movement primitives” section with concrete Azure REST/API anchors (AzCopy ↔ Put Blob/Block From URL; Change Feed for namespace deltas). ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/common/storage-reference-azcopy-map-commands-to-rest-operations "Map of AzCopy commands to REST operations (Azure Blob Storage) | Microsoft Learn"))
- Updated security posture to explicitly include Azure Private Link for partner/customer-owned services as a first-class option for VAST endpoints deployed in Azure. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/private-link/ "Private Link Documentation - Quickstarts, How to guides, and API references | Microsoft Learn"))
- Folded in your Azure First-Party Services → VAST Capabilities matrix as a prioritized “top slice” + an appendix strategy for full coverage.

---

Table of contents

1. Executive summary
2. Framing: purpose, scope, assumptions, definitions
3. The integration thesis (Why this exists)
4. Deployment variants and reference architectures (the new core)
5. Workload catalog and end-to-end flows
6. Integration pattern library (How we integrate)
7. Azure first‑party services integration matrix (prioritized)
8. Roadmap and MVP definition
9. Engineering plan: who builds what
10. Risks, constraints, and decision log
11. Appendices (API contracts, full matrices, deep dives)

---

1. Executive summary

What we are building

A multi-variant VAST + Azure integration that lets customers run GPU-adjacent high-performance storage close to disaggregated GPU fleets while retaining Azure Blob-centric “central lake” economics and ecosystem reach.

This is not a single product—it is a family of deployment variants with a consistent “northbound” integration contract (data movement, namespace, security, and service touchpoints).

Why now

- AI training/inference is increasingly disaggregated (GPUs land where power, availability, and supply allow), while data gravity remains centralized (hero regions / central lakes).
- GPU idle time is the new tax: storage and data movement bottlenecks burn GPU dollars.
- Azure and VAST have publicly positioned VAST AI OS “available soon” to Azure customers, built on Azure infrastructure (including Laos VM series + Azure Boost) and aligned to Azure tools/billing/governance. ([VAST Data](https://www.vastdata.com/press-releases/vast-data-partners-with-microsoft-to-power-the-next-wave-of-agentic-ai "VAST Data Partners with Microsoft to Power the Next Wave of Agentic AI - VAST Data"))

The most opinionated stance in this doc (on purpose)

1. MVP must be “data movement compatibility” first: implement a Blob API subset sufficient for AzCopy compatibility (treat AzCopy as the spec), because Azure’s internal + external movers orbit those primitives. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/common/storage-reference-azcopy-map-commands-to-rest-operations "Map of AzCopy commands to REST operations (Azure Blob Storage) | Microsoft Learn"))
2. Do not attempt full Blob/ADLS parity. It’s a trap. We instead build:

- a minimal Blob façade for movement + tooling reuse, and
- preserve VAST-native integrations for analytics/streaming where they already win.

4. Tiering/offload to Blob is mandatory for long-term economics and supply constraints _if_ VAST is positioned as a performance tier at scale. (We will defend this with data; today it’s a directional thesis.)
5. The hardest problem is control-plane + private connectivity parity with Azure Storage. Most Azure services “pick a storage account” rather than “enter an endpoint URL.” Solving this cleanly likely requires either:

- an Azure-side proxy model (e.g., “Blob as reverse proxy”), and/or
- a deeper Azure-native / managed-service variant of VAST.

Research needed (to complete/defend the exec summary)

- Confirm the exact scope/shape of “VAST AI OS on Azure” offering: packaging, deployment model, whether it includes Private Link, RP integration, billing path, and which VM families are in-scope. ([VAST Data](https://www.vastdata.com/press-releases/vast-data-partners-with-microsoft-to-power-the-next-wave-of-agentic-ai "VAST Data Partners with Microsoft to Power the Next Wave of Agentic AI - VAST Data"))
- Validate real customer toolchains: AzCopy vs wrappers vs rclone; checkpoint formats; concurrency; topology counts.
- Quantify TCO and GPU-utilization benefits with real workload profiles.

---

2. Framing: purpose, scope, assumptions, definitions

Purpose

Create the foundational What / Why / How document for a VAST + Azure integration, spanning:

- business justification,
- workload alignment,
- feature alignment,
- integration points (data plane + control plane),
- architecture variants and phased delivery.

Scope

In-scope

- Multi-variant deployment options (ODM, Azure IaaS, Azure bare metal / Azure-provided hardware).
- Data movement + synchronization patterns (Blob API subset, Change Feed, async replication).
- Tiering/offload design options (opaque vs transparent vs hybrid).
- Service integration matrix (prioritized, defensible).
- Security + networking posture including Private Link options.

Out-of-scope (for MVP)

- Full Azure Blob parity (Append/Page blobs, full feature tail).
- Full ADLS Gen2 / hierarchical namespace parity.
- End-to-end “every Azure service must integrate day 1.”

Definitions (working)

- Hero region: primary Azure region hosting the central lake + large CPU/GPU capacity.
- Satellite region: smaller Azure region used for GPU capacity/availability.
- GPU-adjacent storage: storage close to GPUs to stage training shards + checkpoints at high bandwidth/low latency.
- Opaque tiering: data stored in Blob in VAST-optimized layouts (not directly usable via Blob without VAST).
- Transparent tiering: data stored as native Blob objects; VAST indexes/caches/accelerates access.

Research needed

- Agree internally on canonical glossary + naming: “DataSpace/DataSpaces”, “InsightEngine/DataEngine/SyncEngine”, etc.
- Define “Azure-native” in measurable terms: which Azure control-plane constructs are required (Resource Provider, Private Endpoint types, policy integration, etc.). ([VAST Data](https://www.vastdata.com/technology/microsoft-azure "VAST and Microsoft Partner to Power Agentic AI on Azure - VAST Data"))

---

3. The integration thesis

The core thesis

Azure Blob is the ecosystem storage substrate; VAST is the performance + global namespace substrate for AI/HPC. The integration is about making these behave like a single data fabric across:

- central Blob-backed lakes,
- distributed GPU-adjacent VAST clusters (Azure, neo-cloud, on-prem),
- and the Azure first-party services that expect Blob semantics.

Key points uncovered

- Azure and VAST have publicly stated that Azure customers will gain access to VAST AI OS, running on Azure infrastructure and operated with Azure tools/billing/governance, with VAST benefiting from Azure infrastructure like the Laos VM series and Azure Boost. ([VAST Data](https://www.vastdata.com/press-releases/vast-data-partners-with-microsoft-to-power-the-next-wave-of-agentic-ai "VAST Data Partners with Microsoft to Power the Next Wave of Agentic AI - VAST Data"))
- Azure’s data movement ecosystem heavily relies on “copy from URL” primitives. AzCopy documentation and mapping tables explicitly call out Put Blob From URL / Put Block From URL / Put Block List as core operations depending on scenario and object size. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-s3 "Copy data from Amazon S3 to Azure Storage by using AzCopy | Microsoft Learn"))
- Blob Change Feed is a concrete primitive for ordered-ish “what changed” logs that can drive namespace sync in transparent models. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-change-feed "Change feed in Blob Storage - Azure Storage | Microsoft Learn"))
- Azure Private Link can be used for Azure hosted customer-owned/partner services over private endpoints, implying VAST endpoints deployed in Azure can participate in a private connectivity posture—though _service-by-service feasibility_ still varies. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/private-link/ "Private Link Documentation - Quickstarts, How to guides, and API references | Microsoft Learn"))

Research needed

- Determine which Azure first-party services can consume partner Private Link services vs only native Storage private endpoints.
- Decide the “default” data location truth: is Blob always source of truth with VAST as cache/perf tier, or can VAST be source of truth with Blob as capacity tier? This choice drives almost everything.

---

4. Deployment variants and reference architectures

Refactor note: This section is now a first-class pillar because integration choices depend heavily on _where/how_ VAST runs.

4.1 Variant overview table (hardware & operational variants)

|Variant|Where it runs|What it’s made of|Why it exists|Primary constraints / watch-outs|
|---|---|---|---|---|
|V1 — GPU-adjacent VAST on ODM hardware|Adjacent to GPU fleets (neo-cloud, on-prem, colo, satellite sites)|VAST ODM appliances (flash), high-bandwidth fabric|Max performance, stable ops, no cloud-VM jitter; “AI factory” pattern|Connectivity back to Azure lake (ExpressRoute/Internet), egress costs, async consistency|
|V2 — VAST on Azure IaaS (L-series v4)|Azure regions (hero or satellite)|VAST deployed on Laosv4 / Lasv4 / Lsv4 local NVMe–optimized VMs|Fast “cloud-native” GPU-adjacent tier using Azure primitives; scale-out storage layers|Local NVMe is local/ephemeral; quotas and regional availability; noisy neighbor; lifecycle/deallocation semantics ([TECHCOMMUNITY.MICROSOFT.COM](https://techcommunity.microsoft.com/blog/azurecompute/announcing-the-general-availability-of-azure-laosv4-lasv4-and-lsv4-storage-optim/4422481 "Announcing the general availability of Azure Laosv4, Lasv4, and Lsv4 storage optimized VMs \| Microsoft Community Hub"))|
|V3 — VAST on Azure BareMetal Infrastructure|Azure regions that support BMI|Dedicated bare metal instances in your VNet, root access, no internet|Determinism + isolation; avoid virtualization overhead; potentially better for sustained storage services|BMI is specialized & SKU/region constrained; operational model differs; may require Microsoft-led provisioning/consultation ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/baremetal-infrastructure/concepts-baremetal-infrastructure-overview "What is BareMetal Infrastructure on Azure? - Azure Baremetal Infrastructure \| Microsoft Learn"))|
|V4 — VAST on “Azure Storage-provided hardware” (partner/managed-service direction)|Azure regions, ideally as Storage-adjacent service|Azure-managed/partner-managed hardware footprint + deep Azure control-plane integration|Unlock first-party service compatibility & private connectivity parity; “looks like Azure Storage”|Requires deep Microsoft partnership work (resource provider, networking policy hooks, service onboarding, support model)|

Key points uncovered

- Azure has GA’d L‑series v4 (Laosv4 / Lasv4 / Lsv4) with up to 23TB local NVMe and major performance improvements vs v3, powered by Azure Boost, including high local IOPS at large sizes. ([TECHCOMMUNITY.MICROSOFT.COM](https://techcommunity.microsoft.com/blog/azurecompute/announcing-the-general-availability-of-azure-laosv4-lasv4-and-lsv4-storage-optim/4422481 "Announcing the general availability of Azure Laosv4, Lasv4, and Lsv4 storage optimized VMs | Microsoft Community Hub"))
- Microsoft Learn describes BareMetal Infrastructure as dedicated instances in your VNet with no internet connectivity and root control; includes high-performance storage options and emphasizes low-latency connectivity to Azure VMs. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/baremetal-infrastructure/concepts-baremetal-infrastructure-overview "What is BareMetal Infrastructure on Azure? - Azure Baremetal Infrastructure | Microsoft Learn"))
- VAST’s press release explicitly references running on Azure infrastructure and benefiting from the Laos VM series using Azure Boost. ([VAST Data](https://www.vastdata.com/press-releases/vast-data-partners-with-microsoft-to-power-the-next-wave-of-agentic-ai "VAST Data Partners with Microsoft to Power the Next Wave of Agentic AI - VAST Data"))

Research needed

- Confirm Lasv5 reality: as of current public Azure L-series v4 announcements, v4 is the latest; we should treat v5 as “future” until Microsoft publishes it. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/virtual-machines/migration/sizes/d-ds-dv2-dsv2-ls-series-migration-guide "General Purpose Sizes Migration Guide - Azure Virtual Machines | Microsoft Learn"))
- For V4: clarify what “Azure Storage-provided hardware” means operationally:

- Is this BMI-based, or closer to “ANF/Managed Lustre” style partner-managed service?
- What Azure control-plane hooks are available/required?

---

4.2 Reference architecture A — “Central Blob lake + distributed GPU-adjacent VAST”

flowchart LR

  subgraph Hero[Hero Azure Region]

    Blob[(Azure Blob / ADLS Gen2)]

    ETL[Ingest + Transform\n(Spark/Databricks/Fabric/etc.)]

  end

  subgraph Edge[GPU Sites: Satellite Regions / Neo-cloud / On-Prem]

    VAST[VAST GPU-adjacent tier\n(V1 ODM or V2 IaaS)]

    GPUs[GPU Clusters\n(Train/Infer)]

  end

  ETL --> Blob

  Blob <--> |AzCopy-compatible movement\nPut Blob/Block From URL| VAST

  VAST <--> GPUs

  GPUs --> |Checkpoints| VAST

  VAST --> |Async sync| Blob

Key points uncovered

- Azure’s server-side copy primitives are explicitly documented (Put Blob From URL / Put Block From URL), and AzCopy uses them in multiple scenarios. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/common/storage-reference-azcopy-map-commands-to-rest-operations "Map of AzCopy commands to REST operations (Azure Blob Storage) | Microsoft Learn"))

Research needed

- What is the preferred directionality per workload (central→edge staging vs bidirectional)?
- What are the throughput + concurrency targets for the mover plane?
- What consistency is required for checkpoint “commit” semantics?

---

4.3 Reference architecture B — “Azure-first-party service access (control plane reality)”

This is the key nuance: many Azure services integrate with Blob via the Azure Storage Resource Provider, not via arbitrary endpoints. This is why V4 (deep Azure integration) matters.

Key points uncovered

- Azure Private Link supports private endpoints for Azure PaaS and customer-owned/partner services, which helps data-plane connectivity—but does not by itself solve control-plane “pick a storage account” coupling. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/private-link/ "Private Link Documentation - Quickstarts, How to guides, and API references | Microsoft Learn"))

Research needed

- For each target service (Fabric, AI Foundry, AML, etc.), confirm:

- Does it accept external endpoints (S3/HTTP/NFS), or only storage accounts?
- Does it run in customer VNet (so it can mount NFS), or in managed VNet with restricted egress?
- Can it reach partner private endpoints?

---

5. Workload catalog and end-to-end flows

Each workload uses the same template: Problem → Topology → Flow → Integration patterns → MVP → Future → KPIs.

5.1 Workload W1 — On‑prem VAST + burst compute on Azure (existing strength)

Problem: data lives on-prem; compute bursts to Azure.  
Topology: On-prem VAST ↔ VAST-in-Azure endpoint ↔ Azure compute.  
Integration patterns: P1 (NFS), P2 (S3), P7 (DataSpace/global namespace).  
MVP: solidify reference architecture + security posture + performance envelope.

Key points uncovered

- VAST’s public materials emphasize hybrid/multi-cloud workflows and unified global namespace (DataSpace). ([VAST Data](https://www.vastdata.com/press-releases/vast-data-partners-with-microsoft-to-power-the-next-wave-of-agentic-ai "VAST Data Partners with Microsoft to Power the Next Wave of Agentic AI - VAST Data"))

Research needed

- Where are the breaking points today (cost, capacity limits, operational friction)?
- Can we standardize a “burst kit”: templates, network, DNS, auth, monitoring?

---

5.2 Workload W2 — Central Azure Blob lake + GPU-adjacent VAST (the “inverse” story)

Problem: central data lake sits in Blob; GPUs distributed. Need fast staging + checkpoint sync.  
Topology: Blob in hero region ↔ VAST near GPUs (V1 or V2) ↔ GPUs.  
Integration patterns: P3 (Blob façade), P4 (tiering), P5 (namespace sync).  
MVP: AzCopy-compatible Blob subset on VAST (read/write + server-side copy primitives).

Key points uncovered

- AzCopy’s REST operation map is explicit about which Blob operations are used for upload/download/copy/sync, including Put Blob From URL and Put Block From URL depending on scenario/size. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/common/storage-reference-azcopy-map-commands-to-rest-operations "Map of AzCopy commands to REST operations (Azure Blob Storage) | Microsoft Learn"))

Research needed

- Define the “AzCopy Compatibility Contract” for VAST (exact operations/headers/error behaviors).
- Confirm if customers rely on ADLS endpoint behaviors (DFS) vs Blob endpoint; AzCopy’s own mapping calls out different operations when targeting the Data Lake endpoint. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/common/storage-reference-azcopy-map-commands-to-rest-operations "Map of AzCopy commands to REST operations (Azure Blob Storage) | Microsoft Learn"))

---

5.3 Workload W3 — Tiering/offload from VAST to Blob (economics + capacity)

Problem: VAST flash is premium; Blob HDD-backed tiers provide scale economics.  
Two design branches:

- Opaque tiering: VAST writes VAST-native extents/chunks into Blob (encrypted/compressed/deduped).
- Transparent tiering: VAST keeps objects as native Blob objects; VAST indexes/caches/accelerates.

Key points uncovered

- Blob Change Feed exists as a first-party mechanism to track changes and can be enabled at the storage account level. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-change-feed "Change feed in Blob Storage - Azure Storage | Microsoft Learn"))

Research needed

- Decide if MVP includes tiering, or if tiering is Phase 2.
- For transparent tiering, define how VAST consumes Change Feed and reconciles misses (scan/rebuild).
- For opaque tiering, define recoverability: what happens if VAST control-plane is lost?

---

5.4 Workload W4 — “Azure ecosystem still thinks it’s Blob”

Problem: Azure services and enterprise orgs prefer Blob-native control plane integration and portability.  
Candidate approaches:

- Azure-side reverse proxy (Blob fronts remote VAST/S3).
- Deep Azure-native VAST service (V4).

Key points uncovered

- Private Link can secure access to partner services, which supports a private data plane; but control-plane integration remains a distinct lift. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/private-link/ "Private Link Documentation - Quickstarts, How to guides, and API references | Microsoft Learn"))

Research needed

- Validate feasibility of “Blob reverse proxy” mechanisms (incl. constraints, semantics, perf).
- Identify minimum Azure platform work required for top 5 services.

---

5.5 Workload W5 — RAG / in-place vector + event-driven “agentic” pipelines

Problem: customers want RAG grounding and agentic workflows without duplicative data pipelines.  
Integration: VAST InsightEngine/AgentEngine/DataEngine as “in-place” services; Azure OpenAI / AI Foundry as model endpoints and orchestration layers.

Key points uncovered

- VAST’s press release and tech page position InsightEngine/AgentEngine and “agentic AI” capabilities as part of the Azure offering. ([VAST Data](https://www.vastdata.com/press-releases/vast-data-partners-with-microsoft-to-power-the-next-wave-of-agentic-ai "VAST Data Partners with Microsoft to Power the Next Wave of Agentic AI - VAST Data"))

Research needed

- Define what is product capability vs solution pattern:

- What is natively delivered by VAST vs what is a reference architecture built with Azure Functions/Event Grid/etc.

- Define the “event contract” (what events, schemas, delivery guarantees).

---

6. Integration pattern library

This is how we keep “all possible integration points” tractable.

P1 — File semantics for compute: NFS/SMB

Use when: training code expects POSIX paths, shared file access, many small files, RWX for clusters.  
Applies to: AML compute (VNet-injected), AKS nodes, HPC VMs, Azure Batch.

Research needed

- Validate per-service ability to mount NFS/SMB (managed VNets vs customer VNets).

---

P2 — Object semantics: S3

Use when: tools are S3-native (common in AI ecosystem); or Fabric shortcut path.  
Applies to: Fabric (S3 shortcut), Databricks (S3A), many OSS tools.

Research needed

- Confirm Fabric’s S3 shortcut networking requirements (private endpoints, DNS, egress).

---

P3 — Blob façade on VAST (AzCopy compatibility MVP)

Use when: you must reuse Azure tooling and data movement engines without refactor.  
Hard requirement: implement the subset of Blob REST operations AzCopy depends on.

Anchors (publicly documented)

- AzCopy uses server-side URL copy primitives: e.g., “Put Block From URL” for S3→Blob in docs. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-s3 "Copy data from Amazon S3 to Azure Storage by using AzCopy | Microsoft Learn"))
- Put Blob From URL semantics and auth modes are formally documented (SAS, Entra, Shared Key, etc.). ([Microsoft Learn](https://learn.microsoft.com/en-us/rest/api/storageservices/put-blob-from-url "Put Blob From URL (REST API) - Azure Storage | Microsoft Learn"))

P3.1 AzCopy Compatibility Contract (draft skeleton)

This becomes Appendix A (owned by engineering).

Minimum operations (first-pass from AzCopy REST map): ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/common/storage-reference-azcopy-map-commands-to-rest-operations "Map of AzCopy commands to REST operations (Azure Blob Storage) | Microsoft Learn"))

- List Blobs
- Get Blob
- Get Blob Properties
- Put Blob (size-dependent path)
- Put Block, Put Block List
- Put Blob From URL and/or Put Block From URL (copy scenarios)
- Create Container, Delete Container, Delete Blob
- Optional (phase-gated): Set Blob Metadata, Set Blob Tier, tags

Open questions

- Auth: SAS vs Entra vs Shared Key; which are required for MVP? ([Microsoft Learn](https://learn.microsoft.com/en-us/rest/api/storageservices/put-blob-from-url "Put Blob From URL (REST API) - Azure Storage | Microsoft Learn"))
- Do we support “Blob endpoint” only, or also “DFS endpoint” behaviors (ADLS Gen2)? AzCopy’s own table separates them. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/common/storage-reference-azcopy-map-commands-to-rest-operations "Map of AzCopy commands to REST operations (Azure Blob Storage) | Microsoft Learn"))

---

P4 — Tiering/offload to Blob

Two sub-patterns

- P4a Opaque (VAST-native extents in Blob)
- P4b Transparent (native Blob objects; VAST indexes/caches)

Research needed

- Decide default per workload; define what customers gain/lose (portability vs reduction vs ecosystem reach).

---

P5 — Namespace & metadata synchronization (Change Feed + reconciliation)

Base primitive: Blob Change Feed can be enabled and configured for retention. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-change-feed "Change feed in Blob Storage - Azure Storage | Microsoft Learn"))  
Use when: VAST needs to mirror Blob namespace or detect changes for cache invalidation.

Research needed

- Define ordering/consistency expectations from Change Feed for our scenarios.
- Define reconciliation strategy: full scan, prefix scan, Bloom filter, etc.

---

P6 — Azure-side reverse proxy (Blob → external object store)

Use when: Azure services must remain Blob-native in control-plane, but data lives elsewhere.  
Research needed

- Confirm feasibility, semantics, and performance constraints; identify what Microsoft must build.

---

P7 — Eventing integration (VAST ↔ Event Grid / Functions / Foundry)

Use when: storage events drive AI/ETL workflows.

Research needed

- Define canonical event schema and delivery semantics (at-least-once vs exactly-once).
- Confirm per-service ingestion: Event Grid topics vs Service Bus vs Functions triggers.

---

P8 — Networking & security posture (Private Link, isolation)

Key primitive: Azure Private Link supports customer-owned/partner services over Private Endpoints. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/private-link/ "Private Link Documentation - Quickstarts, How to guides, and API references | Microsoft Learn"))  
Use when: enterprise adoption requires private-only access (no public endpoints).

Research needed

- Private Link scaling limits (connections/SNAT, port exhaustion) for high fan-out clients.
- Service-by-service: which Azure managed services can reach partner private endpoints.

---

7. Azure first‑party services integration matrix (prioritized)

Your provided matrix is excellent as a candidate inventory. Here we refactor it into a prioritized, actionable matrix that calls out “works now vs needs work vs needs Microsoft”.

7.1 Legend

- Works now: achievable with today’s data-plane + networking patterns (NFS/S3/Private Link).
- VAST work: requires VAST engineering (Blob façade, tiering, eventing, connectors).
- Microsoft work: requires Azure control-plane / first-party service changes (or Azure-side proxy).

7.2 Top slice matrix (high impact for the AI factory thesis)

|Azure Service|Primary scenario|VAST modules|Integration patterns|Feasibility|Research needed|
|---|---|---|---|---|---|
|Azure Machine Learning|Training on large datasets|DataStore/DataSpace|P1 (NFS), P2 (S3), P8|Works now (when compute is in customer VNet)|Validate AML networking modes + mount patterns|
|Microsoft Fabric|Query without moving data|DataStore/DataBase|P2 (S3 shortcut), P8|Mostly works (pattern-dependent)|Confirm private networking + caching behaviors|
|Azure Databricks|ETL / Spark pipelines|DataBase/DataStore|P2 (S3A) + VAST native connectors|Works with VAST work|Validate pushdown semantics + auth|
|AKS|Inference farms / microservices|DataStore|P1 (NFS/SMB), CSI + P8|Works now|Confirm CSI maturity + perf/scale|
|Azure Blob Storage|Central lake + tiering|DataSpace/SyncEngine|P3, P4, P5|Core|Define opaque vs transparent tiering plan|
|Azure Event Grid|Storage-driven workflows|DataEngine/Platform Services|P7|VAST work|Event schema, delivery guarantees|
|Azure Functions|Serverless reactions|DataEngine|P7|VAST work|Trigger model (push vs poll), auth|
|Azure OpenAI Service|RAG grounding|InsightEngine|Solution-level integration|Pattern-based|Define reference architecture & eval metrics|
|Azure AI Foundry|Agentic workflows|InsightEngine/AgentEngine|P7 + solution pattern|Pattern-based|Identify what is first-party vs custom|
|Azure Storage Mover / movers|Data movement at scale|SyncEngine|P3|Depends|Confirm which movers can target non-Azure endpoints|

7.3 Full matrix strategy (so it doesn’t explode)

- Appendix B: Full “Azure services candidate list” (your inventory) tagged with:

- Category (AI/ML, Analytics, Compute, Integration, Hybrid, Security, DevOps)
- Storage binding model (endpoint URL vs storage account selection)
- Network model (customer VNet vs managed VNet)
- Integration patterns (P1–P8)
- Feasibility class (Works / VAST work / Microsoft work)

Research needed

- Validate service names and scope: some items in the candidate list appear duplicated or potentially non-canonical; we should ground the final appendix in the official Azure product catalog.

---

8. Roadmap and MVP definition

Phase 0 — Baseline (today)

- VAST deployed in cloud/on-prem with NFS/S3 endpoints and DataSpace-style global namespace.
- Establish reference architectures for burst-to-cloud and GPU-adjacent staging.

Phase 1 — MVP (the non-negotiable)

Deliver: P3 Blob façade for AzCopy compatibility

- Implement the AzCopy-dependent Blob REST subset. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/common/storage-reference-azcopy-map-commands-to-rest-operations "Map of AzCopy commands to REST operations (Azure Blob Storage) | Microsoft Learn"))
- Provide a compatibility harness: AzCopy CLI becomes the regression suite.

Deliver: Private connectivity baseline

- Standardize Private Link Service pattern for VAST endpoints deployed in Azure. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/private-link/ "Private Link Documentation - Quickstarts, How to guides, and API references | Microsoft Learn"))

Phase 2 — Economics & scale

- Tiering/offload to Blob (P4) + namespace sync (P5). ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-change-feed "Change feed in Blob Storage - Azure Storage | Microsoft Learn"))
- Introduce policy-driven movement (hotset vs coldset) and measurable TCO metrics.

Phase 3 — “Azure ecosystem parity”

- Azure-side reverse proxy or deep Azure-native managed service variant (V4).
- Control-plane integration for “pick a storage account” experiences.

Research needed

- Confirm which of these are already implied by the “Azure-native deployment” messaging and what is still aspirational. ([VAST Data](https://www.vastdata.com/technology/microsoft-azure "VAST and Microsoft Partner to Power Agentic AI on Azure - VAST Data"))

---

9. Engineering plan: who builds what

VAST workstreams

1. Blob façade (P3): implement subset + compatibility harness. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/common/storage-reference-azcopy-map-commands-to-rest-operations "Map of AzCopy commands to REST operations (Azure Blob Storage) | Microsoft Learn"))
2. Mover performance: concurrency, retries, resumability, checksums, throttling.
3. Tiering engine (P4): opaque first vs transparent first (decision).
4. Namespace sync (P5): Change Feed consumer + reconciliation. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-change-feed "Change feed in Blob Storage - Azure Storage | Microsoft Learn"))
5. Eventing (P7): publish to Event Grid / invoke Functions; define schema.
6. Networking (P8): Private Link Service templates + DNS patterns. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/private-link/ "Private Link Documentation - Quickstarts, How to guides, and API references | Microsoft Learn"))

Microsoft workstreams (if we want ecosystem parity)

1. Control-plane support for VAST-like storage accounts or proxy endpoints.
2. Tuscany-like reverse proxy extension (if that’s the chosen path).
3. Service onboarding: Fabric/Foundry/others to support partner endpoints where possible.

Joint workstreams

- Reference architectures (hero + satellite + neo-cloud).
- Security review/threat model (public vs private endpoints, data exfiltration).
- 2–3 lighthouse customer validations.

---

10. Risks, constraints, and decision log

Major decision 1: Tiering model

- Opaque = stickier + better reduction, worse ecosystem portability.
- Transparent = ecosystem-friendly, more complexity + less reduction.

Research needed

- Pick per workload; support both if justified.

Major decision 2: “Control plane truth”

- If Azure ecosystem must integrate without changes, we need V4 and/or Azure proxy.
- If we accept “VAST endpoints only,” integration footprint narrows but is faster.

Major decision 3: Deployment variant selection logic

We need a defensible rule set:

- When do we recommend ODM GPU-adjacent vs Azure IaaS vs Azure bare metal?

Research needed

- SKU/region availability for L‑series v4 vs customer target regions. ([TECHCOMMUNITY.MICROSOFT.COM](https://techcommunity.microsoft.com/blog/azurecompute/announcing-the-general-availability-of-azure-laosv4-lasv4-and-lsv4-storage-optim/4422481 "Announcing the general availability of Azure Laosv4, Lasv4, and Lsv4 storage optimized VMs | Microsoft Community Hub"))
- Feasibility of BMI for storage-heavy deployments and how it intersects with the “Azure Storage-provided hardware” vision. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/baremetal-infrastructure/concepts-baremetal-infrastructure-overview "What is BareMetal Infrastructure on Azure? - Azure Baremetal Infrastructure | Microsoft Learn"))

---

11. Appendices (to be built next)

- Appendix A — AzCopy Compatibility Contract

- Derived from AzCopy REST mapping and validated via CI harness. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/common/storage-reference-azcopy-map-commands-to-rest-operations "Map of AzCopy commands to REST operations (Azure Blob Storage) | Microsoft Learn"))

- Appendix B — Azure Services Integration Matrix (Full)

- Your candidate inventory, normalized + validated against Azure product catalog.

- Appendix C — API spec: Blob façade MVP

- Request/response headers, auth modes, error codes, idempotency, ETag semantics. ([Microsoft Learn](https://learn.microsoft.com/en-us/rest/api/storageservices/put-blob-from-url "Put Blob From URL (REST API) - Azure Storage | Microsoft Learn"))

- Appendix D — Tiering design deep dive

- Opaque vs transparent vs hybrid; recovery semantics; operational model.

- Appendix E — Networking & Security reference designs

- Private Link templates, DNS, identity mapping, Key Vault hooks.

---

Updated research backlog (delta from your new inputs)

R1 — Deployment variants validation (new)

- Confirm L‑series v4 is the correct baseline for Azure IaaS deployments; document Laosv4 vs Lasv4 selection criteria. ([TECHCOMMUNITY.MICROSOFT.COM](https://techcommunity.microsoft.com/blog/azurecompute/announcing-the-general-availability-of-azure-laosv4-lasv4-and-lsv4-storage-optim/4422481 "Announcing the general availability of Azure Laosv4, Lasv4, and Lsv4 storage optimized VMs | Microsoft Community Hub"))
- Validate what “Azure Storage-provided hardware” concretely means:

- BMI? Partner-managed PaaS? Something else? ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/baremetal-infrastructure/concepts-baremetal-infrastructure-overview "What is BareMetal Infrastructure on Azure? - Azure Baremetal Infrastructure | Microsoft Learn"))

- Confirm “Lasv5” status; treat as future until public docs exist. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/virtual-machines/migration/sizes/d-ds-dv2-dsv2-ls-series-migration-guide "General Purpose Sizes Migration Guide - Azure Virtual Machines | Microsoft Learn"))

R2 — Service-by-service feasibility (refactor your matrix into facts)

- For top ~15 services (Fabric, Foundry, AML, Databricks, AKS, Event Grid, Functions, Storage Mover, etc.), record:

- Storage binding model (endpoint URL vs storage account selection)
- Network model (customer VNet vs managed VNet)
- Allowed private endpoint types (native storage vs partner private link) ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/private-link/ "Private Link Documentation - Quickstarts, How to guides, and API references | Microsoft Learn"))

R3 — Data movement contract (must-do)

- Implement “AzCopy Contract” from official operation mapping; create a test matrix by command and scenario. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/common/storage-reference-azcopy-map-commands-to-rest-operations "Map of AzCopy commands to REST operations (Azure Blob Storage) | Microsoft Learn"))
- Decide whether we must support Put Blob From URL, Put Block From URL, or both (likely both). ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/common/storage-reference-azcopy-map-commands-to-rest-operations "Map of AzCopy commands to REST operations (Azure Blob Storage) | Microsoft Learn"))

R4 — Namespace sync primitives

- Prototype using Blob Change Feed to drive namespace/index updates; define reconciliation strategy. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-change-feed "Change feed in Blob Storage - Azure Storage | Microsoft Learn"))

---

If you want the next iteration to be maximally productive, I’ll take Appendix A (AzCopy Compatibility Contract) and Appendix B (Prioritized Azure Services Matrix) and draft them in the same style (opinionated, with “what we know” vs “what we must validate”).

Appendix C — VAST Blob API Compatibility Contract (MVP)

Purpose (opinionated): The Blob API MVP is not a “Blob clone.” It is a compatibility façade on top of VAST that makes _existing Azure-centric data movers_ work without refactor, specifically for AI data staging + checkpoint movement between a _central Azure Blob lake_ and _GPU-adjacent VAST_ (or between VAST sites).  
The MVP should be judged by “does it run the real tools (AzCopy + high‑concurrency direct REST clients) with zero code change?” — not by broad API surface.

This appendix is written as an implementation-ready contract that we can drop into the main document under Integration Points → Data Plane → Blob API on VAST.

---

C.1 Where this API runs (variant-agnostic)

The Blob API endpoint must behave identically across the VAST deployment variants we’re considering:

- GPU-adjacent: VAST ODM hardware sitting adjacent to GPU pods / training clusters.
- Central Azure regions: VAST on Lasv4/Lasv5 VM SKUs (subject to regional availability/quota).
- Potential future: VAST on Azure Storage-provided bare metal (where applicable).

Key design constraint: regardless of hardware, the Blob API endpoint must present a _stable_ contract to client tooling (auth, paths, headers, ETags, XML shapes, retry semantics).

---

C.2 MVP goals and non-goals

Goals (MVP)

1. Enable “no-refactor” data movement workflows using Azure-native conventions and tools:

- Block blob uploads/downloads (high concurrency, resumable).
- Server-side copy primitives to hydrate GPU-adjacent VAST from a central Blob lake.

3. Pass an explicit compatibility test plan (see C.8).
4. Remain small and defensible (clear rationale for what’s deferred).

Non-goals (explicitly out of MVP)

- ADLS Gen2 / DFS endpoint (hierarchical namespace semantics, rename primitives, ACLs).
- Append blobs / page blobs (not relevant to AI dataset + checkpoint movement).
- Snapshots / versioning / soft delete / legal hold / immutability.
- Full account management & control-plane (ARM resource provider integration).
- Full parity of all blob features (tags, tiering, lease orchestration, etc.) unless required by the compatibility harness.

---

C.3 Why Block Blob only (and why “From URL” is mandatory)

For AI pipelines, the dominant object pattern is:

- Large objects (dataset shards, checkpoints) and
- High concurrency transfers (many workers, range reads, parallel multipart uploads).

Azure’s REST surface for this is Block Blobs + Put Block + Put Block List and (for efficient cross-account/cross-endpoint movement) Put Blob From URL / Put Block From URL.

Crucially:

- Put Blob From URL is a _whole-object_ create/overwrite primitive (no partial updates) and has a source-size limit of 5,000 MiB. ([Microsoft Learn](https://learn.microsoft.com/en-us/rest/api/storageservices/put-blob-from-url "Put Blob From URL (REST API) - Azure Storage | Microsoft Learn"))
- Therefore, Put Block From URL must be implemented to support “server-side hydration” of large objects by copying _ranges_ from a source into blocks, then committing via Put Block List. ([Microsoft Learn](https://learn.microsoft.com/en-us/rest/api/storageservices/put-block-from-url "Put Block From URL (REST API) - Azure Storage | Microsoft Learn"))

---

C.4 The MVP API surface

This is the minimum set of Blob Service operations we should implement first, derived from:

- AzCopy’s published mapping of commands → REST operations ([Azure Docs](https://docs.azure.cn/en-us/storage/common/storage-reference-azcopy-map-commands-to-rest-operations "Map of AzCopy commands to REST operations (Azure Blob Storage) | Azure Docs"))
- plus the core Block Blob REST operations required for high-concurrency clients.

C.4.1 “Must have” operations (MVP)

|Area|REST Operation|Method / Path|Why it’s in MVP|
|---|---|---|---|
|Namespace|Create Container|PUT /{container}?restype=container|Enables “mkdir” style workflows + bootstrapping destinations (AzCopy supports make). ([Azure Docs](https://docs.azure.cn/en-us/storage/common/storage-reference-azcopy-map-commands-to-rest-operations "Map of AzCopy commands to REST operations (Azure Blob Storage) \| Azure Docs"))|
||Delete Container|DELETE /{container}?restype=container|Cleanup/teardown; keeps parity with AzCopy surface. ([Azure Docs](https://docs.azure.cn/en-us/storage/common/storage-reference-azcopy-map-commands-to-rest-operations "Map of AzCopy commands to REST operations (Azure Blob Storage) \| Azure Docs"))|
||List Blobs|GET /{container}?restype=container&comp=list|Required for scan/sync operations and “directory” listing semantics via prefix/delimiter. ([Azure Docs](https://docs.azure.cn/en-us/storage/common/storage-reference-azcopy-map-commands-to-rest-operations "Map of AzCopy commands to REST operations (Azure Blob Storage) \| Azure Docs"))|
|Reads|Get Blob Properties|HEAD /{container}/{blob}|Existence checks, size/mtime/etag, resume logic. ([Azure Docs](https://docs.azure.cn/en-us/storage/common/storage-reference-azcopy-map-commands-to-rest-operations "Map of AzCopy commands to REST operations (Azure Blob Storage) \| Azure Docs"))|
||Get Blob (Range)|GET /{container}/{blob}|High-throughput download + resumable/range reads. ([Azure Docs](https://docs.azure.cn/en-us/storage/common/storage-reference-azcopy-map-commands-to-rest-operations "Map of AzCopy commands to REST operations (Azure Blob Storage) \| Azure Docs"))|
|Writes|Put Blob (single-shot)|PUT /{container}/{blob}|Small/medium objects and simple overwrite cases. ([Azure Docs](https://docs.azure.cn/en-us/storage/common/storage-reference-azcopy-map-commands-to-rest-operations "Map of AzCopy commands to REST operations (Azure Blob Storage) \| Azure Docs"))|
||Put Block|PUT /{container}/{blob}?comp=block&blockid=...|Parallel/multipart uploads. Must accept URL-encoded Base64 block IDs. ([Azure Docs](https://docs.azure.cn/en-us/storage/common/storage-reference-azcopy-map-commands-to-rest-operations "Map of AzCopy commands to REST operations (Azure Blob Storage) \| Azure Docs"))|
||Put Block List|PUT /{container}/{blob}?comp=blocklist|Atomic commit of blocks (the “finish upload” point). ([Azure Docs](https://docs.azure.cn/en-us/storage/common/storage-reference-azcopy-map-commands-to-rest-operations "Map of AzCopy commands to REST operations (Azure Blob Storage) \| Azure Docs"))|
|Deletes|Delete Blob|DELETE /{container}/{blob}|Sync/delete use cases. ([Azure Docs](https://docs.azure.cn/en-us/storage/common/storage-reference-azcopy-map-commands-to-rest-operations "Map of AzCopy commands to REST operations (Azure Blob Storage) \| Azure Docs"))|
|Metadata|Set Blob Metadata|PUT /{container}/{blob}?comp=metadata|Preserve metadata across moves; used by many workflows. ([Azure Docs](https://docs.azure.cn/en-us/storage/common/storage-reference-azcopy-map-commands-to-rest-operations "Map of AzCopy commands to REST operations (Azure Blob Storage) \| Azure Docs"))|
||Set Blob Properties|PUT /{container}/{blob}?comp=properties|Preserve content-type/encoding/disposition etc. ([Microsoft Learn](https://learn.microsoft.com/en-us/rest/api/storageservices/get-blob "Get Blob (REST API) - Azure Storage \| Microsoft Learn"))|
|Server-side copy|Put Blob From URL|PUT /{container}/{blob} + x-ms-copy-source|Efficient object hydration without routing through clients; required, but limited to 5,000 MiB source objects. ([Azure Docs](https://docs.azure.cn/en-us/storage/common/storage-reference-azcopy-map-commands-to-rest-operations "Map of AzCopy commands to REST operations (Azure Blob Storage) \| Azure Docs"))|
||Put Block From URL|PUT /{container}/{blob}?comp=block&blockid=... + x-ms-copy-source|Required to copy large objects by range into blocks; supports x-ms-source-range. ([Azure Docs](https://docs.azure.cn/en-us/storage/common/storage-reference-azcopy-map-commands-to-rest-operations "Map of AzCopy commands to REST operations (Azure Blob Storage) \| Azure Docs"))|

C.4.2 “Nice to have (still small)” operations (recommend for early follow-on)

|REST Operation|Why|
|---|---|
|Get Block List (GET ...?comp=blocklist)|Helps debugging + resume behaviors for multipart transfers; likely shows up in tooling edge-cases. (Validate via tool harness.)|
|Get Container Properties (HEAD /{container}?restype=container)|Many clients check container existence/metadata; low effort to add.|

C.4.3 Explicitly deferred

From AzCopy’s own mapping, these are the first things to defer unless a target customer proves they need them:

- Set Blob Tier (access tier semantics) ([Azure Docs](https://docs.azure.cn/en-us/storage/common/storage-reference-azcopy-map-commands-to-rest-operations "Map of AzCopy commands to REST operations (Azure Blob Storage) | Azure Docs"))
- Set/Get Blob Tags ([Azure Docs](https://docs.azure.cn/en-us/storage/common/storage-reference-azcopy-map-commands-to-rest-operations "Map of AzCopy commands to REST operations (Azure Blob Storage) | Azure Docs"))
- Any DFS/HNS operations (ADLS Gen2), append/page blob operations.

---

C.5 Behavioral contract and “gotchas” we must emulate

C.5.1 Versioning headers (x-ms-version) must be accepted

Authorized requests require x-ms-version and a valid Date / x-ms-date style header. ([Microsoft Learn](https://learn.microsoft.com/en-us/rest/api/storageservices/put-blob-from-url "Put Blob From URL (REST API) - Azure Storage | Microsoft Learn"))  
MVP recommendation: accept a broad range of x-ms-version values and behave as a “latest-compatible” service for the MVP surface.

C.5.2 Block upload rules we must honor (or clients will break)

From the REST spec for Put Block:

- A block blob can have up to 50,000 blocks.
- With version 2019-12-12 and later, max block size is 4,000 MiB. ([Microsoft Learn](https://learn.microsoft.com/en-us/rest/api/storageservices/put-block "Put Block (REST API) - Azure Storage | Microsoft Learn"))
- For a given blob, block IDs must have the same length and must be Base64 then URL-encoded. ([Microsoft Learn](https://learn.microsoft.com/en-us/rest/api/storageservices/put-block "Put Block (REST API) - Azure Storage | Microsoft Learn"))

Implication for VAST: we need a staging store for uncommitted blocks (keyed by blob+blockid), tolerant of out-of-order arrival, and an atomic commit at Put Block List.

C.5.3 Range reads are first-class

High-concurrency clients commonly use range reads (e.g., resumable download, parallel reading of large objects).  
MVP must: support Range: bytes=start-end on GET Blob and return correct 206 Partial Content semantics.

C.5.4 “From URL” primitives have strict HTTP requirements

Both Put Blob From URL and Put Block From URL require:

- Content-Length: 0 (non-zero fails). ([Microsoft Learn](https://learn.microsoft.com/en-us/rest/api/storageservices/put-blob-from-url "Put Blob From URL (REST API) - Azure Storage | Microsoft Learn"))
- x-ms-copy-source specifying a URL; if the source is not public, it must be authorized via SAS in the URL or via x-ms-copy-source-authorization. ([Microsoft Learn](https://learn.microsoft.com/en-us/rest/api/storageservices/put-blob-from-url "Put Blob From URL (REST API) - Azure Storage | Microsoft Learn"))
- Put Blob From URL only supports BlockBlob (x-ms-blob-type: BlockBlob). ([Microsoft Learn](https://learn.microsoft.com/en-us/rest/api/storageservices/put-blob-from-url "Put Blob From URL (REST API) - Azure Storage | Microsoft Learn"))
- Put Blob From URL has the 5,000 MiB source limit. ([Microsoft Learn](https://learn.microsoft.com/en-us/rest/api/storageservices/put-blob-from-url "Put Blob From URL (REST API) - Azure Storage | Microsoft Learn"))
- Put Block From URL can specify x-ms-source-range to copy specific byte ranges. ([Microsoft Learn](https://learn.microsoft.com/en-us/rest/api/storageservices/put-block-from-url "Put Block From URL (REST API) - Azure Storage | Microsoft Learn"))

Implication: the “hydration” story for large objects must be Put Block From URL + Put Block List, not Put Blob From URL.

---

C.6 Authentication strategy (MVP vs next)

Azure’s REST APIs support multiple authorization models, and Microsoft recommends Microsoft Entra ID where possible. ([Microsoft Learn](https://learn.microsoft.com/en-us/rest/api/storageservices/put-block-from-url "Put Block From URL (REST API) - Azure Storage | Microsoft Learn"))

MVP auth stance (pragmatic + compatible):

1. SAS tokens (service SAS + user delegation SAS) as the “default” production mechanism

- SAS provides time-bound delegated access; Blob supports multiple SAS types. ([Microsoft Learn](https://learn.microsoft.com/en-us/rest/api/storageservices/put-block-from-url "Put Block From URL (REST API) - Azure Storage | Microsoft Learn"))

3. Shared Key (account key) for early testing / constrained environments

- Shared Key is a documented REST scheme (Authorization header, x-ms-date, x-ms-version). ([Microsoft Learn](https://learn.microsoft.com/en-us/rest/api/storageservices/put-blob-from-url "Put Blob From URL (REST API) - Azure Storage | Microsoft Learn"))

Post-MVP (strategic):

- Microsoft Entra ID (OAuth bearer tokens) for Zero Trust / managed identity flows (resource: https://storage.azure.com/). ([Microsoft Learn](https://learn.microsoft.com/en-us/rest/api/storageservices/authorize-with-azure-active-directory "Authorize with Microsoft Entra ID (REST API) - Azure Storage | Microsoft Learn"))

Important integration note: Put Blob From URL / Put Block From URL include x-ms-copy-source-authorization (bearer scheme) for authorized sources in newer versions. ([Microsoft Learn](https://learn.microsoft.com/en-us/rest/api/storageservices/put-blob-from-url "Put Blob From URL (REST API) - Azure Storage | Microsoft Learn"))  
If we want “server-side hydration” from protected sources without embedding SAS in URLs, Entra becomes high-value.

---

C.7 Endpoint shape and namespace mapping (MVP design decision)

We need a consistent mapping between Azure blob concepts and VAST constructs:

|Azure Concept|MVP Mapping on VAST (recommended)|
|---|---|
|Storage account|VAST tenant / logical namespace boundary|
|Container|VAST bucket / top-level directory boundary|
|Blob|VAST object/file (block blob semantics)|

Critical research item: confirm the most compatible URL style for AzCopy + popular REST clients:

- Virtual-host style: https://{account}.{domain}/{container}/{blob}
- Path style (emulator style): https://{domain}/{account}/{container}/{blob} (common in emulators; docs show emulator uses account in path). ([Microsoft Learn](https://learn.microsoft.com/en-us/rest/api/storageservices/put-blob-from-url "Put Blob From URL (REST API) - Azure Storage | Microsoft Learn"))

We should choose one canonical style for MVP and optionally support the other via routing.

---

C.8 Compatibility harness and “definition of done”

C.8.1 AzCopy command coverage (MVP)

Using AzCopy’s published mapping of commands to REST operations as the baseline: ([Azure Docs](https://docs.azure.cn/en-us/storage/common/storage-reference-azcopy-map-commands-to-rest-operations "Map of AzCopy commands to REST operations (Azure Blob Storage) | Azure Docs"))

MVP should successfully execute:

- azcopy copy

- local ↔ VAST
- Azure Blob ↔ VAST (server-side hydration path)

- azcopy sync (basic)
- azcopy make (container create)
- azcopy remove (basic delete)

Not required in MVP:

- tag/tier manipulation (set-properties variants that map to Set Tier / Set Tags). ([Azure Docs](https://docs.azure.cn/en-us/storage/common/storage-reference-azcopy-map-commands-to-rest-operations "Map of AzCopy commands to REST operations (Azure Blob Storage) | Azure Docs"))

C.8.2 REST-client coverage (high concurrency)

The MVP should also be validated against at least one direct REST client (async/high concurrency) that does not use the official SDK (to catch subtle protocol deviations early). The exact client can be chosen based on customer reality; what matters is that it stresses:

- large multipart uploads
- range reads
- recursive listings with prefix/delimiter
- metadata preservation
- retry/backoff

---

C.9 Key points we’ve uncovered (what belongs in the main “What/Why/How” narrative)

- The MVP is small but non-trivial: it’s basically “Block Blob + server-side copy primitives + faithful headers/XML.”
- Put Blob From URL alone is insufficient (5,000 MiB source limit; no partial updates). ([Microsoft Learn](https://learn.microsoft.com/en-us/rest/api/storageservices/put-blob-from-url "Put Blob From URL (REST API) - Azure Storage | Microsoft Learn"))
- Put Block From URL is required to make server-side hydration work for large objects, with optional x-ms-source-range. ([Microsoft Learn](https://learn.microsoft.com/en-us/rest/api/storageservices/put-block-from-url "Put Block From URL (REST API) - Azure Storage | Microsoft Learn"))
- Block upload semantics impose hard constraints (50k blocks, 4,000 MiB blocks in newer versions, same-length block IDs). ([Microsoft Learn](https://learn.microsoft.com/en-us/rest/api/storageservices/put-block "Put Block (REST API) - Azure Storage | Microsoft Learn"))
- Auth must start with SAS + Shared Key for practical compatibility, while Entra ID is the strategic follow-on for managed identity and Zero Trust. ([Microsoft Learn](https://learn.microsoft.com/en-us/rest/api/storageservices/put-block-from-url "Put Block From URL (REST API) - Azure Storage | Microsoft Learn"))

---

C.10 Research needed to complete/defend this section

These are the “prove it” items we should assign and track:

1. AzCopy wire-level validation

- Confirm any additional preflight calls not covered by the published mapping table (e.g., service/account info endpoints) by running AzCopy against an Azure REST logger and/or reading code paths.

3. Client endpoint targeting

- Validate how AzCopy and the chosen REST client accept custom endpoint base URLs (path-style vs virtual-host style), including TLS + DNS expectations.

5. Version matrix

- Identify the minimum set of x-ms-version values we must accept to avoid brittle failures.

7. Error-body fidelity

- Determine which clients require Azure-style XML error bodies (and which specific error codes) for correct retry/behavior.

9. Concurrency and throttling posture

- Establish targets: parallel PutBlock count, range-read fanout, keep-alive behavior, and expected throttling semantics (when to 503 vs 409 vs 429).

11. Server-side copy topology

- Confirm network reachability assumptions for Put * From URL:

- Can the VAST endpoint reach the central Blob lake privately?
- Do we need to support x-ms-copy-source-authorization early for private sources? ([Microsoft Learn](https://learn.microsoft.com/en-us/rest/api/storageservices/put-blob-from-url "Put Blob From URL (REST API) - Azure Storage | Microsoft Learn"))

---

If you want the next iteration to be maximally useful, I can take this appendix and refactor it into:

- a 1-page executive “Blob API MVP” summary (for alignment), and
- an engineering spec version (request/response examples, acceptance suite, and a “deviation log” template).

# VAST + Microsoft Azure Integration

## End-to-end **What / Why / How** (Highly Opinionated First Draft v0.3)

**Intent:** This document is the backbone for a VAST + Azure integration strategy. It is deliberately modular—each section can be carved out into its own standalone memo/spec.

---

## Document metadata

·       **Primary audiences**

o   **Exec / BD / Partnering:** business rationale, differentiation, deal shape

o   **Product:** workload/feature alignment, roadmap options, MVP definitions

o   **Engineering (VAST + Microsoft):** concrete integration points, constraints, dependencies

o   **Field / SA / CS:** reference architectures, “how to sell/position,” what works vs. what requires Microsoft work

·       **Non-goals**

o   We are **not** building a full Azure Storage clone (no full ADLS Gen2 parity, no full page/append blob surface) in the MVP.

o   We are **not** assuming Azure-first-party control-plane integration exists unless explicitly scoped as a Microsoft engineering dependency.

---

## 0. Executive summary

### 0.1 What we’re building

A **multi-variant VAST deployment + integration model** that can span:

1.        **GPU-adjacent VAST (edge/satellite/neo-cloud/on-prem)** on **VAST ODM hardware** (highest performance adjacency).

2.        **Central-region VAST in Azure** deployed on **storage-optimized Azure VM SKUs** (baseline: **Lasv4/Lsv4**; keep **Lasv5** as a placeholder for next-gen) for GPU-adjacent storage _inside_ Azure regions.

3.        A forward-looking option: **VAST on Azure bare metal / “Azure-native” partner integration** where VAST could run on Microsoft-provided hardware with deeper platform integration (conceptually similar to Azure BareMetal Infrastructure + “Azure Native” ISV patterns).

### 0.2 Why this matters

The dominant emerging pattern for frontier-scale AI/HPC is:

·       **Central data estate** (often Blob-based lakes) in **hero Azure regions**

·       **Distributed GPUs** (satellite Azure regions + neo-clouds + on-prem) where power exists

·       A requirement for **fast data staging + checkpoint sync** between the two

### 0.3 How we get to value fast

**Opinionated sequencing:**

1.        **MVP (Phase 1): Blob API endpoint on VAST** to unlock **no-refactor** data movement using **AzCopy-style** and **high-concurrency REST clients** (the “data mover ecosystem”).

2.        **Phase 2: Tiering/offload + namespace sync** between VAST and Blob (choose opaque vs transparent; possibly both).

3.        **Phase 3: Deeper Azure ecosystem integration** (control-plane, managed networking parity, proxy patterns, stronger semantics).

### 0.4 Key decisions we must make early

·       **Tiering model:** **Opaque VAST-native layout in Blob** vs **Transparent Blob-native objects indexed/served by VAST** (or both).

·       **Networking posture:** where we can use **Customer VNet** vs where we hit the **Managed VNet Wall** (Fabric/Synapse/ADF patterns).

·       **Blob API MVP contract:** the smallest surface that reliably supports real tooling (AzCopy + strict REST clients), with correct auth/ETag/error/XML behaviors.

### 0.5 Research needed to complete the executive story

·       Validate the **top 3 customer pipelines** (actual tools, object sizes, concurrency, checkpoint semantics)

·       Confirm feasibility + performance of **Put Blob From URL / Put Block From URL** equivalents on VAST for server-side copy paths

·       Confirm which **Azure services** can connect to a **Private Link Service** endpoint vs only to **Azure resource IDs** (managed private endpoints constraints)

---

## 1. Problem statement and scope framing

### Key points uncovered

·       Azure has a deep ecosystem that **assumes Blob** (and often assumes it via **control-plane resource selection**, not “enter an endpoint URL”).

·       VAST’s differentiation is strongest when it is the **GPU-adjacent performance tier** and/or the **global namespace** across distributed sites.

·       We need an integration story that works when VAST is:

o   **ODM hardware adjacent to GPUs** (non-Azure sites included)

o   **Azure VMs in central/hero regions**

o   **(future)** Azure bare metal / Azure-native integration pattern

### Research needed

·       Concrete list of Azure “picker-based” storage bindings vs URL-based bindings for our top workloads

·       Clarify which customer scenarios require **Azure-first-party private networking posture** vs tolerate public endpoints

---

## 2. Deployment variants and reference architectures

### 2.1 Variant A — GPU-adjacent VAST on ODM hardware (satellite / neo-cloud / on-prem)

**Where it wins**

·       Highest GPU adjacency performance

·       Best control over hardware topology

**Where it’s hard**

·       Must integrate back to Azure lakes over WAN (cost/egress/latency)

·       Azure-first-party services in managed networks won’t directly reach it without bridges

### 2.2 Variant B — VAST in Azure central regions on storage-optimized VMs (Lasv4 baseline)

**Why Lasv4/Lsv4-class matters**

·       Storage-optimized VMs with **local NVMe** are the most natural substrate for “GPU-adjacent storage in Azure.”

**Notes**

·       We treat **Lasv5** as “next-gen candidate” but anchor current planning on **Lasv4/Lsv4** because that’s what Azure documents publicly as the current generation in this class.

### 2.3 Variant C — VAST on Azure bare metal / Azure-native partner pattern (under consideration)

Two plausible routes:

·       **Azure BareMetal Infrastructure** class deployments (dedicated physical servers within Azure connectivity model).

·       “**Azure Native ISV**” style managed offering (example pattern: Azure Native Pure Storage Cloud).

### Research needed

·       Define what “Azure Storage provided hardware” concretely maps to commercially/technically (BMI? dedicated host? native ISV service?)

·       Determine the minimum platform primitives we’d need from Microsoft for this to be viable (operational model, lifecycle, security, networking)

---

## 3. Workload alignment

### 3.1 Workload 1 — Burst compute in Azure against on-prem VAST (existing pattern)

**Key points**

·       VAST in cloud can act as a **cloud endpoint/cache** into an on-prem VAST estate (global namespace/data spaces story).

·       Best for: burst compute, short-lived staging, remote access patterns.

**Research needed**

·       Quantify where VM-based VAST is “good enough” vs where it breaks economically for capacity-heavy scenarios.

---

### 3.2 Workload 2 — Central Azure lake + distributed GPUs + GPU-adjacent VAST staging (primary target)

**Key points**

·       Central lake in Blob, GPUs distributed across regions/providers.

·       Need two pipelines:

o   **Stage training data → GPU-adjacent VAST**

o   **Sync checkpoints → central Azure lake**

**Why this drives Blob API MVP**

·       The fastest path to adoption is: **do not make customers rewrite their data movers**.

·       The MVP should support both:

o   **server-side copy primitives** (AzCopy-style)

o   **high-concurrency REST clients** (async Python-style, rclone-like, etc.)

**Research needed**

·       Real object size distributions (few huge vs millions of small)

·       Checkpoint semantics (atomic commit patterns, lease-like needs)

---

### 3.3 Workload 3 — Tiering/offload from VAST flash tier to Azure Blob capacity tier

**Key points**

·       VAST flash is the performance tier; Blob (HDD-based economics) is the capacity tier.

·       Two models:

1.        **Opaque VAST-native layout in Blob** (best reduction/stickiness; not directly readable by Blob consumers)

2.        **Transparent Blob-native objects** (ecosystem-friendly; more sync complexity; weaker reduction)

**Research needed**

·       Decide which model is MVP for which customer segment (or support both with a clear decision rubric)

·       Validate cost + performance implications

---

## 4. Integration points inventory

### Key points uncovered

Integration happens across four layers:

1.        **Data plane:** NFS/SMB/S3/**Blob API (new)**

2.        **Metadata/namespace:** change feed/eventing, listing semantics, consistency

3.        **Networking/security:** private endpoints, managed VNets, Private Link Service

4.        **Control plane:** “picker-based” Azure services vs endpoint-based services

### Research needed

·       Per-service feasibility matrix (top 15 services first)

·       Which services can connect to **Private Link Service** endpoints vs only to Azure-native PaaS private endpoints

---

# 5. Azure service integration patterns (UPDATED for network realities)

## 5.1 The four network patterns we must design around

### Pattern A — **Customer VNet data-plane integration (the “easy path”)**

·       Service compute runs **in your VNet** (or is VNet-injected).

·       VAST connects via:

o   VNet peering / routing

o   or **Private Link Service** if we need to avoid peering and provide private endpoints at scale.

**Important gotcha:** Private Link Service traffic is SNAT’d by default; if we need original client IP for auditing, consider **Proxy Protocol v2** patterns.

---

### Pattern B — **Managed VNet + managed private endpoints (the “Azure-native wall”)**

·       Service runs in a Microsoft-managed network and uses managed private endpoints.

·       Typically requires **Azure Resource IDs** (not arbitrary FQDNs).

·       Example constraint: Fabric managed private endpoints can’t be created using FQDN and don’t support Private Link Service targets in the normal way. ([Microsoft Learn](https://learn.microsoft.com/en-us/fabric/security/security-managed-private-endpoints-create "Create and use managed private endpoints in Microsoft Fabric - Microsoft Fabric | Microsoft Learn"))

---

### Pattern C — **Gateway / Self-hosted runtime bridge**

·       When Pattern B blocks us, we bridge via:

o   **Fabric On-premises Data Gateway shortcuts** for network-restricted sources ([Microsoft Learn](https://learn.microsoft.com/en-us/fabric/onelake/create-on-premises-shortcut "Create shortcuts to on-premises data - Microsoft Fabric | Microsoft Learn"))

o   **ADF Self-hosted Integration Runtime** style deployments (VM in your network/VNet) ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/data-factory/concepts-integration-runtime "Integration runtime - Azure Data Factory & Azure Synapse | Microsoft Learn"))

---

### Pattern D — **Control-plane binding vs data-plane binding**

·       If a service requires “pick a Storage Account” in the portal, it will not “see” a VAST endpoint unless Microsoft adds control-plane support.

·       If a service accepts a URL/endpoint, VAST can integrate much more directly.

---

## 5.2 The Azure Service Integration Matrix (top services, with validated references)

**Legend**

·       **Binding model**

o   **Control-plane (Resource ID / Picker)**: service expects Azure resource types

o   **Data-plane (Endpoint URL / Credentials)**: service can target arbitrary endpoints

·       **Network model**

o   **Customer VNet / VNet-injected**

o   **Managed VNet (service-managed)**

|**Azure Service**|**Storage binding model**|**Network model**|**Private connectivity model**|**VAST integration strategy**|**Notes / constraints**|**Primary references**|
|---|---|---|---|---|---|---|
|Microsoft Fabric|OneLake **Shortcuts** (incl. “Amazon S3 compatible” shortcut)|Managed (service-managed)|Fabric uses **managed private endpoints** for supported Azure resources; for **network-restricted** sources use **on-premises data gateway** shortcuts|Use **S3-compatible shortcut** to VAST S3 endpoint; if VAST endpoint isn’t publicly reachable, use **on-premises data gateway** shortcut|Fabric MPE limitations (no FQDN / no PLS target); shortcuts + MPE support is evolving|([Microsoft Learn](https://learn.microsoft.com/en-us/fabric/onelake/create-s3-compatible-shortcut "Create an Amazon S3 compatible shortcut - Microsoft Fabric \| Microsoft Learn"))|
|Azure AI Foundry|Foundry hub/projects support managed network + private endpoints to dependent resources (storage/kv/acr/etc.)|Hybrid (service-managed control plane + workload networking options)|Private link for Foundry hubs; supports managed network isolation|For training/inference compute running in customer network: mount/access VAST via NFS/S3; treat Foundry’s default storage as “control-plane required,” VAST as “data-plane high-perf tier”|Foundry private link is for hub/project resources; VAST as “storage account” isn’t a native option without Microsoft work|([Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/hub-configure-private-link?view=foundry-classic "How to configure a private link for a Microsoft Foundry hub - Microsoft Foundry \| Microsoft Learn"))|
|Azure Databricks|External locations/mounts via URLs + credentials (S3/ADLS/etc.)|Customer VNet (VNet injection available)|Private connectivity options via workspace networking features; data sources often reached via private endpoints|Use VAST **Spark connector** and/or access VAST via NFS/S3 from cluster nodes in same VNet/peered VNet|Distinguish Classic compute vs Serverless networking; pick the topology that keeps data paths private|([Microsoft Learn](https://learn.microsoft.com/en-us/azure/databricks/security/network/classic/vnet-inject "Deploy Azure Databricks in your Azure virtual network ..."))|
|Azure Machine Learning|Datastores typically Azure Storage; compute can be network isolated|Customer VNet options + managed network features|Private Link for AML workspace/resources; network isolation controls|For high-perf training: bypass datastore abstraction where needed; mount VAST NFS/S3 on compute nodes in customer VNet|AML “storage account picker” doesn’t map to VAST; integration is via compute data plane|([Microsoft Learn](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-network-security-overview?view=azureml-api-2 "Secure workspace resources using virtual networks (VNets)"))|
|Azure Synapse Analytics|Linked services / external tables typically bind to Azure storage resources|Often Managed VNet (Synapse workspace managed VNet option)|**Managed private endpoints** from Synapse workspace to Azure PaaS|If direct query to VAST is blocked, ingest from VAST via S3/NFS into ADLS/Blob, then analyze|Managed endpoints optimize Azure resource targets; third-party endpoints need workarounds|([Microsoft Learn](https://learn.microsoft.com/en-us/azure/synapse-analytics/security/synapse-workspace-managed-private-endpoints "Managed private endpoints - Azure Synapse Analytics \| Microsoft Learn"))|
|AKS|Kubernetes PV/PVC; storage reachable via VNet routing|Customer VNet|Private cluster option; nodes in VNet; service-to-storage often via private endpoints|**Gold path:** VAST CSI driver / NFS PVs; connect via VNet peering or Private Link Service|Primary integration target for inference + data services|([Microsoft Learn](https://learn.microsoft.com/en-us/azure/aks/private-clusters "Create a private Azure Kubernetes Service (AKS) cluster"))|
|Azure Functions|Blob triggers/bindings are Azure Storage-account bound|Customer VNet integration (Premium/isolated)|Private endpoints for inbound; VNet integration for outbound|Prefer **webhook/event** pattern: VAST publishes to Event Grid or calls Functions over HTTP; avoid “Blob trigger” dependence|Blob triggers assume Azure Storage account types|([Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-vnet "Use private endpoints to integrate Azure Functions with a virtual network \| Microsoft Learn"))|
|Azure Batch|Pool supports mounting file systems|Customer VNet (pool can be placed in VNet)|Private networking via VNet configuration|Burst rendering/HPC: mount VAST NFS/SMB in pool configuration|Works well when Batch nodes are in same/peered VNet|([Microsoft Learn](https://learn.microsoft.com/en-us/azure/batch/virtual-file-mount "Mount a virtual file system on a Batch pool - Azure"))|
|Azure App Service|Built-in storage mounts focus on Azure Storage; VNet integration exists|Customer VNet integration (outbound) + Private Endpoint (inbound)|Private endpoints supported for inbound access|Don’t treat App Service as primary for mounted VAST; prefer AKS/Container Apps; App Service can call VAST via S3/HTTPS if needed|App Service “mount storage” is Azure Storage oriented (not arbitrary NFS)|([Microsoft Learn](https://learn.microsoft.com/en-us/azure/app-service/configure-connect-to-azure-storage "Mount Azure Storage as a local share in App Service"))|
|Azure Data Factory|Linked services + Integration Runtime|Managed VNet option exists for ADF; also self-hosted IR|Private Link support; managed VNet + managed private endpoints for Azure resources|**Self-hosted IR** VM inside VAST VNet to orchestrate data movement to/from VAST|Managed networking is optimized for Azure PaaS targets; third-party endpoints typically require IR bridging|([Microsoft Learn](https://learn.microsoft.com/en-us/azure/data-factory/managed-virtual-network-private-endpoint "Managed virtual network and managed private endpoints - Azure Data Factory \| Microsoft Learn"))|
|Azure Storage Mover|Endpoint-based migration tool (source/target types constrained)|Agent-based model|Agent runs where source is|Use where VAST can present a supported “source” interface; otherwise prefer AzCopy/Rclone/VAST Sync tooling|Storage Mover targets are Azure Storage services; VAST as target is unlikely without Microsoft changes||
|Azure Event Grid|Custom topics/domains + webhook delivery|Service-managed|Private endpoints supported for topics/domains|VAST publishes events to Event Grid custom topic; Azure services subscribe|Event Grid is a clean “event bus” for VAST → Azure actions|([Microsoft Learn](https://learn.microsoft.com/en-us/azure/event-grid/configure-private-endpoints "Configure private endpoints for Azure Event Grid custom ..."))|

### Research needed (to harden this section)

·       Validate Fabric’s evolving support for shortcuts + networking (what’s GA vs preview for private connectivity to non-Azure endpoints)

·       For each “Managed VNet” service: confirm whether it can target **Private Link Service** endpoints or only native Azure PaaS IDs

---

# 6. Blob API on VAST — **MVP specification** (new section)

## 6.1 Why Blob API compatibility is a first-class MVP

Blob API compatibility is not “because we want to be Blob.” It is because:

·       **Azure data movement ecosystems** and many “glue” workflows depend on Blob REST semantics.

·       Customers will adopt fastest when **they don’t refactor** movers/scripts.

·       This MVP is the best short-term lever to unlock:

o   Central Blob lake → GPU-adjacent VAST staging

o   GPU-adjacent VAST checkpoints → central Blob lake

## 6.2 MVP scope principles (hard boundaries)

**In MVP we do:**

·       **Block blobs only**

·       Required REST operations for:

o   listing + enumeration

o   upload/download (single-shot + block commit)

o   server-side copy primitives (from URL) as a first-class capability

**In MVP we do not:**

·       Page blobs, append blobs

·       Full ADLS Gen2 DFS endpoint / hierarchical namespace parity

·       Snapshots, immutability policies, object replication, etc.

## 6.3 The MVP “Compatibility Contract” — required operations

**Implementation stance:** treat **tooling compatibility** as the spec; validate against real tools and unit tests.

|**Priority**|**Operation**|**REST API (method + query)**|**MVP requirements**|**Spec reference**|
|---|---|---|---|---|
|Critical|List blobs|`GET` container `?comp=list`|Prefix + delimiter support, pagination/continuation; XML response fidelity||
|Critical|Put Blob|`PUT` blob|Small object upload path, overwrite semantics||
|Critical|Put Block|`PUT` blob `?comp=block&blockid=`|High concurrency, out-of-order blocks allowed, base64 block IDs||
|Critical|Put Block List|`PUT` blob `?comp=blocklist`|Atomic commit semantics, return ETag/Last-Modified; MD5 support||
|Critical|Get Blob|`GET` blob|Must support `Range` reads (resume + partial fetch)||
|Critical|Get Blob Properties|`HEAD` blob|Content-Length, Last-Modified, ETag, metadata headers||
|High|Delete Blob|`DELETE` blob|Idempotent deletes; recursive tooling uses this heavily||
|High|Set Blob Metadata|`PUT` blob `?comp=metadata`|Preserve custom metadata; must round-trip||
|High|Get Blob Metadata|`GET` / `HEAD` blob (metadata headers)|Ensure metadata visibility via HEAD/GET semantics||
|High|Put Blob From URL|`PUT` blob (copy from URL headers)|Server-side copy from HTTPS source; avoid client egress||
|High|Put Block From URL|`PUT` blob `?comp=block&blockid=` + source header|Enables server-side block staging for large copies||

### Notes (why these matter)

·       **Put Blob From URL / Put Block From URL** are central to efficient “server-side” data movement patterns on Azure.

·       **List Blobs XML fidelity** is not optional: many clients parse it strictly; deviating XML structure causes failures.

·       **Range reads** are essential for resumability and checkpoint workflows.

## 6.4 Authentication & authorization (MVP vs target)

### MVP auth (Phase 1)

1.        **SAS** (service/container/blob SAS)

o   Most portable, supports delegated access patterns.

2.        **Shared Key**

o   Needed for many existing compatibility paths and simple connection strings.

### Post-MVP (Phase 2/3)

3.        **Microsoft Entra ID / OAuth**

o   Required for “enterprise zero trust” and managed identity patterns.

## 6.5 Required protocol behaviors (the “gotchas” that break real tools)

### Required behaviors

·       **ETag + Last-Modified** correctness across PUT/GET/HEAD flows

·       **Standard Blob error response bodies** (XML `<Error><Code>…</Code>`) for 4xx/5xx so clients can classify errors

·       **MD5 / integrity** support as expected by some tools (Content-MD5 handling)

·       **Concurrency scaling**: design front-end to survive hundreds/thousands of parallel block PUTs without connection churn

## 6.6 Namespace mapping (how VAST models “storage accounts” and “containers”)

Opinionated mapping proposal:

·       **Azure Storage Account** ⇄ **VAST tenant / namespace boundary**

·       **Container** ⇄ **VAST bucket / top-level export**

·       **Blob name** ⇄ **Object key** (flat namespace with delimiter-based pseudo-folders)

### Research needed

·       Confirm exact canonicalization rules for Shared Key signing we must implement (to avoid auth mismatch)

·       Identify which account-level APIs clients call by default (and whether we can stub them safely)

## 6.7 Acceptance tests (definition of “works”)

Preview readiness means:

·       AzCopy can:

o   list / copy / sync from Blob → VAST and VAST → Blob using server-side primitives where applicable

·       A strict REST client can:

o   list recursively

o   upload large objects via block uploads

o   resume downloads via range reads

o   delete recursively

### Research needed

·       Extract the **exact** AzCopy REST dependency list from source and lock it as the compatibility contract (CI gate).

---

# 7. Networking for VAST endpoints in Azure (how we expose Blob/S3/NFS safely)

## 7.1 Recommended private connectivity baseline

·       For VAST deployed in Azure VNets, expose endpoints privately via:

o   **VNet peering** for same-tenant integration

o   **Private Link Service** when we need scalable private consumption without peering

## 7.2 Managed VNet reality check

·       Fabric managed private endpoints do not support targeting arbitrary FQDNs / Private Link Services as a managed endpoint today (documented constraints). ([Microsoft Learn](https://learn.microsoft.com/en-us/fabric/security/security-managed-private-endpoints-create "Create and use managed private endpoints in Microsoft Fabric - Microsoft Fabric | Microsoft Learn"))

·       Therefore: to reach VAST from Fabric/Synapse-like managed network services, we generally need:

o   **gateway/IR bridges**, or

o   Microsoft-first-party proxy integration work

---

# 8. Roadmap (phased)

## Phase 0 — current-state foundations

·       VAST in cloud as endpoints/caching, global namespace back to on-prem

## Phase 1 — MVP: Blob API on VAST (tooling compatibility)

·       Implement the MVP contract in §6

·       Build regression harness with:

o   tool-based integration tests

o   REST conformance tests for XML/errors/auth signatures

## Phase 2 — Tiering + sync

·       Deliver at least one tiering model (opaque or transparent)

·       Add change-feed/event-driven sync where applicable

## Phase 3 — Deeper Azure ecosystem integration

·       Control-plane integration for picker-based services

·       Proxy patterns where Microsoft must participate

·       Stronger semantics where workloads require it (leases/consistency subsets)

---

# 9. Research & defense backlog (next iteration targets)

## 9.1 Blob API MVP hardening

·       Enumerate AzCopy REST calls + headers + expected status/error bodies

·       Validate server-side copy viability (Put Blob From URL / Put Block From URL) under high concurrency

·       Decide MVP auth order: SAS-first vs SharedKey-first (and what enterprise constraints require)

## 9.2 Managed VNet wall

·       For each managed-network service (Fabric/Synapse/ADF):

o   confirm what third-party connectivity patterns are truly supported today

o   define the “bridge default” (gateway vs IR vs proxy)

## 9.3 Deployment variant selection

·       Build a decision rubric: ODM vs Lasv4 vs bare metal/native

·       Confirm regional availability + quota implications for storage-optimized VM families

---

## Appendix A — Suggested diagrams (to be added as we iterate)

### A1. End-to-end data flow (central lake ↔ GPU-adjacent VAST)

```
flowchart LR
```

```
  subgraph Central["Hero Azure Region (Central Data Estate)"]
```

```
    Blob["Azure Blob / ADLS Gen2 (Central Lake)"]
```

```
    ETL["ETL / Preprocess (Spark/Databricks/etc.)"]
```

```
  end
```

```
  subgraph Edge["Distributed GPU Sites (Satellite/Neo-cloud/On-prem)"]
```

```
    VAST["VAST GPU-adjacent (ODM or Azure VMs)"]
```

```
    GPUs["GPU Cluster (Train/Infer)"]
```

```
  end
```

```
  ETL --> Blob
```

```
  Blob -- "Stage via BlobAPI movers" --> VAST
```

```
  VAST --> GPUs
```

```
  GPUs -- "Checkpoints" --> VAST
```

```
  VAST -- "Sync back via BlobAPI movers" --> Blob
```

### A2. Connectivity pattern decision

```
flowchart TD
```

```
  Q1["Is the consuming service in Customer VNet?"] -->|Yes| P1["Use VNet peering or Private Link Service to VAST"]
```

```
  Q1 -->|No / Managed VNet| Q2["Can the service target arbitrary endpoints?"]
```

```
  Q2 -->|Yes| P2["Use URL-based endpoint (S3/Blob) + security controls"]
```

```
  Q2 -->|No| P3["Use Gateway/Integration Runtime bridge OR require Microsoft engineering"]
```

---

If you want the next iteration, I suggest we do **one pass focused only on**:

1.        The **Blob API MVP contract** (derive from AzCopy source + lock exact headers/status codes), and

2.        The **Managed VNet wall** (Fabric/Synapse/ADF) — identify the top 3 viable connectivity patterns we can defend for each.

## Appendix X: Namespace & Metadata Federation Between Azure Blob and VAST DataSpaces

This appendix is the **opinionated** design for how we keep a **single, usable namespace** across:

·       **Azure Blob Storage** (deep, cheap “lake”)

·       **VAST clusters** (fast, GPU-adjacent “performance tier”), deployed as:

o   VAST **ODM hardware** next to GPUs (customer datacenter / neo-cloud / edge)

o   VAST **on Azure** (Lasv4 / Lasv5 SKUs in “hero” regions)

o   VAST **bare metal** on Azure-provided hardware (where available)

The core goal is to move from **copying** (slow + duplicative) to **federation** (metadata synchronized; bytes moved only when needed).

---

### 1) What we are solving

#### The “split-brain namespace” problem

In a hybrid lake + performance-tier design, two “masters” can exist:

·       **Azure Blob** is the **deep master** for many Azure-native pipelines (ADF, Fabric ingest, etc.).

·       **VAST** is the **fast master** for GPU training/inference, checkpointing, and low-latency RAG pipelines.

If changes happen on both sides without coordination:

·       Deletes may not propagate (compliance/security risk).

·       Overwrites may not be visible (stale reads).

·       Listings diverge (users don’t trust the namespace).

#### Key design principle (opinionated)

**Pick an authority per prefix.**  
Do not attempt bidirectional “both sides write anything” in an MVP.

Concretely, we define folder prefixes as:

·       **Blob-authoritative (read-mostly via VAST)**: datasets landed into Blob should show up in VAST quickly.

·       **VAST-authoritative (write + replicate/tier to Blob)**: checkpoints / curated outputs written on VAST get exported to Blob.

Bidirectional writes are a **Phase 3+** problem (leases/conflicts/security).

---

### 2) Azure primitives we can (and should) leverage

|**Azure primitive**|**What it gives us**|**What it does** _**not**_ **give us**|**Why it matters**|
|---|---|---|---|
|**Event Grid Storage events**|Push notifications for blob events (low latency). Includes a `**sequencer**` field to order events for the _same blob name_ (helps idempotency).|Not a durable log; delivery is **at-least-once** (duplicates possible) and can fail delivery unless dead-lettering is configured.|Great as a **real-time trigger**, not as the authoritative record. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/event-grid/event-schema-blob-storage "Azure Blob Storage as Event Grid source - Azure Event Grid \| Microsoft Learn"))|
|**Blob Change Feed**|Durable, replayable transaction log of blob and metadata changes, stored as **Avro** records. Includes event types like create/delete and **properties updates** (which Event Grid does not fully cover).|**Not supported** for storage accounts with **hierarchical namespace enabled** (ADLS Gen2/HNS). Has a “few minutes” publishing delay.|This is the **source of truth** for correctness… when you can use it. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-change-feed "Change feed in Blob Storage - Azure Storage \| Microsoft Learn"))|
|**Storage Inventory**|Periodic authoritative listing of objects + properties (CSV/Parquet), useful for reconciliation and drift correction; can emit an Event Grid completion event.|Not real-time (daily/weekly).|This is your **safety net** and rebuild mechanism. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/blob-inventory "Azure Storage blob inventory \| Microsoft Learn"))|
|**Object Replication**|Azure-managed async replication of **block blobs** between two Azure storage accounts. Replicates blob properties/metadata, requires versioning and change feed on the source.|Only Azure-to-Azure (not external); **not supported for HNS**; doesn’t replicate index tags; destination has write restrictions.|Useful to stage datasets closer to a region (or to create an “AI distribution account”), but not a direct “Blob → VAST” replicator. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/object-replication-overview "Object replication overview - Azure Storage \| Microsoft Learn"))|
|**Blob Leases**|A per-blob lock mechanism to coordinate exclusive write access.|Not a full distributed lock service; doesn’t solve multi-object atomic commits.|Relevant for Phase 3+ (bidirectional writes). ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/event-grid/event-schema-blob-storage "Azure Blob Storage as Event Grid source - Azure Event Grid \| Microsoft Learn"))|

---

### 3) The VAST side: how we should model Blob in DataSpaces

**We need a first-class concept:** _External-Origin Global Folder_A folder in VAST DataSpaces whose “origin” is **not** a VAST cluster, but an **external object namespace** (Azure Blob).

We can reuse the mental model of **Origin vs Satellite** used in global namespace/caching designs (origin holds full set; satellite caches locally). A third-party description of VAST’s origin/satellite global folder behavior (and caching satellites) aligns with this model. ([Blocks and Files](https://blocksandfiles.com/2025/02/12/a-vast-effort-data-estate-vectorization-and-data-storage-for-the-ai-era/ "A VAST effort: Data estate vectorization and storage for the ..."))

#### Recommended semantics for MVP

·       External-origin folders are **read-only from VAST** (enforced).

·       Writes occur either:

o   directly to Blob (Blob-authoritative prefixes), or

o   to a separate VAST-authoritative prefix that later exports to Blob.

This is a deliberate constraint to avoid split-brain without inventing a distributed transaction/lock system.

---

### 4) Three patterns we must support

#### Pattern A: VAST is master (tier/export to Blob)

**Use when:** training outputs, checkpoints, curated data, “hot working set” on VAST with cold storage in Blob.

·       Write to VAST.

·       VAST exports/tier-to-Blob by policy.

This pattern is primarily a **data movement/export** problem. Namespace consistency is already strict within VAST clusters; the question is how we publish objects into Blob (opaque vs native object) and how we expose “stubs” in VAST once tiered.

**Key design choice:**

·       **Opaque format in Blob** maximizes VAST data reduction but makes Blob unreadable without VAST.

·       **Native object format in Blob** enables Azure ecosystem reads (Fabric, Synapse, etc.), but may reduce VAST-side reductions.

_(This decision belongs in the tiering appendix; called out here because it impacts how namespace federation works for “Azure reads.”)_

---

#### Pattern B: Blob is master (VAST is cache/index)

**Use when:** central Blob lake feeds GPU-adjacent VAST clusters.

This is the **core namespace/metadata federation** problem.

We need:

·       VAST to **see** what exists in Blob (metadata sync)

·       VAST to **serve** it efficiently (hydrate/cache on demand)

---

#### Pattern C: Migration-on-read proxy (future)

This is the “Tuscany-like” idea: Blob remains the front door and pulls from VAST when missing.

There’s no public Azure “Tuscany” spec we can cite. But **Cloudflare Sippy** is a good public analog: it fetches from an upstream source on cache miss and migrates objects lazily. ([Cloudflare Docs](https://developers.cloudflare.com/r2/data-migration/sippy/ "Sippy · Cloudflare R2 docs"))

We should treat this as a **Microsoft-dependent future option**, not the MVP.

---

### 5) The recommended MVP architecture for Blob → VAST namespace sync

#### Design goals

1.        **Low-latency visibility**: new blobs show up quickly in VAST listings.

2.        **No missed deletes**: eventual correctness is non-negotiable.

3.        **Idempotent and replayable**: duplicates/out-of-order are expected.

4.        **Scales to billions of objects** without “LIST the world” loops.

5.        Works across **multi-variant VAST deployments** (ODM, Lasv4/5, bare metal) with the same control logic.

---

## 5.1 Reference architecture

```
flowchart LR
```

```
  subgraph Azure["Azure Subscription"]
```

```
    EG["Event Grid\n(Storage events)"] --> Q["Durable Queue\n(Event Hubs / Service Bus)"]
```

```
    CF["Blob Change Feed\n(Avro log)\n(non-HNS only)"] --> CFR["Change Feed Reader"]
```

```
    INV["Storage Inventory\n(daily/weekly)"] --> RECON["Reconciler"]
```

```
  end
```

```
  Q --> P["Namespace Processor\n(idempotent)"]
```

```
  CFR --> P
```

```
  RECON --> P
```

```
  P --> VIDX["VAST Namespace Index\n(stubs + attributes)"]
```

```
  VIDX --> DS["VAST DataSpaces\n(Global namespace)"]
```

```
  DS --> CLIENTS["GPU clusters / AKS / ML\n(NFS/S3/BlobAPI clients)"]
```

```
  CLIENTS --> READ["Read Request"]
```

```
  READ --> CACHE["Hydrate/Cache Manager"]
```

```
  CACHE --> BLOB["Azure Blob (data)"]
```

```
  CACHE --> LOCAL["VAST local flash/NVMe\n(ODM / Lasv4/5 / bare metal)"]
```

### Why this exact shape is opinionated

·       **Event Grid** drives _speed_; **Change Feed** drives _correctness_ when possible; **Inventory** drives _recovery and drift repair_. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/event-grid/event-schema-blob-storage "Azure Blob Storage as Event Grid source - Azure Event Grid | Microsoft Learn"))

·       We do **not** directly update VAST from Event Grid webhooks without a durable queue in between (backpressure + retries).

---

## 5.2 Event sources and what we trust them for

### Event Grid (fast trigger)

Use Event Grid storage events for:

·       Create / delete (and rename events where available for HNS accounts)

·       Triggering prefetch/hydration jobs (optional)

But assume:

·       **Duplicates** can happen (at-least-once).

·       Delivery can fail; you need retries and dead-lettering for robustness. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/event-grid/event-schema-blob-storage "Azure Blob Storage as Event Grid source - Azure Event Grid | Microsoft Learn"))

·       It does not cover all update semantics that Change Feed can emit (e.g., “properties updated” events are change-feed-exclusive). ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-change-feed "Change feed in Blob Storage - Azure Storage | Microsoft Learn"))

### Change Feed (durable truth, but not everywhere)

Use Change Feed for:

·       Deterministic replay and “no missed events”

·       Property updates (e.g., overwritten objects, metadata/properties changes)

Critical limitation:

·       **Not supported for hierarchical namespace (HNS) accounts**. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-change-feed "Change feed in Blob Storage - Azure Storage | Microsoft Learn"))

### Storage Inventory (reconciliation)

Use Inventory for:

·       Periodic reconciliation of VAST index vs Blob truth

·       Disaster recovery: rebuilding the index after outage/data loss

·       Supporting HNS accounts as the “eventual truth snapshot” mechanism ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/blob-inventory "Azure Storage blob inventory | Microsoft Learn"))

---

## 5.3 The metadata model we store in VAST

For each Blob object, VAST stores a **stub record** (metadata-only entry) representing the object in the global namespace.

**Stub fields (MVP):**

·       `container`

·       `blob_name`

·       `size`

·       `last_modified`

·       `etag`

·       `content_type`

·       `content_md5` (if provided)

·       `remote_url` or `(account, container, blob)` pointer

·       `state`: `REMOTE_ONLY | CACHED | HYDRATING | TOMBSTONED`

·       `last_seen_sequence`: for idempotency (Event Grid `sequencer` or Change Feed equivalent)

We do _not_ require full user metadata/tags in MVP (costly HEAD calls), but we must design the schema to add them.

---

## 5.4 Idempotency and ordering

### What we use

·       **Event Grid** `**sequencer**`: order events for a single blob name. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/event-grid/event-schema-blob-storage "Azure Blob Storage as Event Grid source - Azure Event Grid | Microsoft Learn"))

·       **ETag**: validate whether an update is newer.

·       **Inventory snapshot**: reconciliation anchor.

### Algorithm (MVP)

For any event about `(container, blob_name)`:

1.        Look up last processed `sequencer` (or equivalent) for that key.

2.        If event is older/equal, drop it (duplicate/out-of-order).

3.        Otherwise:

o   If created/updated: upsert stub with new etag/size/last_modified.

o   If deleted: mark stub TOMBSTONED and optionally purge cached bytes.

---

## 5.5 Read path behavior: “hydrate on demand” vs “proxy stream”

We support two read modes; **default depends on deployment**.

### Mode 1: Hydrate + cache (recommended for GPU-adjacent)

·       First read triggers hydration from Blob into VAST local NVMe/flash.

·       Subsequent reads are served locally.

·       Best for GPU utilization and repeated epoch reads.

### Mode 2: Proxy stream (fallback)

·       VAST streams bytes directly from Blob without persisting a local copy.

·       Useful for low-touch access or when local cache is constrained.

**Opinionated default**

·       ODM GPU-adjacent: **hydrate+cache by default**.

·       Azure Lasv4/Lasv5 centralized “hub”: **policy-driven** (cache hot prefixes; proxy cold).

·       Bare metal Azure storage hardware: treat like ODM (cache aggressive).

_(We will need perf benchmarks to tune thresholds.)_

---

### 6) Handling HNS (ADLS Gen2) accounts

This is the hard reality:

·       Change Feed is not supported for HNS-enabled accounts. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-change-feed "Change feed in Blob Storage - Azure Storage | Microsoft Learn"))

·       Object Replication also depends on Change Feed and is not supported for HNS. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/object-replication-overview "Object replication overview - Azure Storage | Microsoft Learn"))

**Opinionated recommendation**If near-real-time federation is required, customers should create a **non-HNS “AI distribution” storage account** as the federation source for training datasets (even if the “analytics lake” remains HNS). Then:

·       replicate into that account using whatever pipeline they already use, and

·       run Change Feed + Event Grid against that non-HNS account for strong correctness.

If customers insist on federating directly from HNS accounts:

·       Event Grid becomes the “fast trigger”

·       Storage Inventory becomes the “eventual truth”

·       Expect more reconciliation work and longer correctness windows

---

### 7) Tradeoff matrix

|**Approach**|**Latency**|**Completeness**|**Works with HNS?**|**Operational cost**|**My take**|
|---|---|---|---|---|---|
|**Event Grid only**|seconds|medium (miss/dup risk; no full update coverage)|yes|low|Great trigger, **bad truth** ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/event-grid/event-schema-blob-storage "Azure Blob Storage as Event Grid source - Azure Event Grid \| Microsoft Learn"))|
|**Change Feed only**|minutes|high|**no**|medium (polling + checkpointing)|Best truth where supported ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-change-feed "Change feed in Blob Storage - Azure Storage \| Microsoft Learn"))|
|**Event Grid + Change Feed (recommended)**|seconds-to-minutes|high|no|medium-high|Best balance for non-HNS ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/event-grid/event-schema-blob-storage "Azure Blob Storage as Event Grid source - Azure Event Grid \| Microsoft Learn"))|
|**Event Grid + Inventory (HNS fallback)**|seconds-to-hours|medium-high|yes|high|Works, but reconciliation-heavy ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/blob-inventory "Azure Storage blob inventory \| Microsoft Learn"))|
|**Full periodic scan (LIST everything)**|hours-days|high|yes|very high|Do only for tiny accounts|

---

### 8) Failure modes and how we harden

1.        **Event Grid delivery failures**

o   Mitigation: dead-lettering + durable queue + replay. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/event-grid/event-schema-blob-storage "Azure Blob Storage as Event Grid source - Azure Event Grid | Microsoft Learn"))

2.        **Change Feed lag**

o   Mitigation: treat as correctness loop; Event Grid gives perceived freshness while Change Feed catches up. Change Feed publishing can lag “a few minutes.” ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-change-feed "Change feed in Blob Storage - Azure Storage | Microsoft Learn"))

3.        **Reconciliation drift**

o   Mitigation: Storage Inventory periodic diff to ensure we never miss deletes. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/blob-inventory "Azure Storage blob inventory | Microsoft Learn"))

4.        **Overwrite races**

o   Mitigation: last-writer-wins using `sequencer` + etag checks; rehydrate if etag changed. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/event-grid/event-schema-blob-storage "Azure Blob Storage as Event Grid source - Azure Event Grid | Microsoft Learn"))

---

### 9) Roadmap (pragmatic, defensible)

#### Phase 1: MVP (Namespace visibility + on-demand hydration)

·       Event Grid subscription → queue → VAST Namespace Processor

·       Change Feed Reader for non-HNS accounts

·       Stub index + listing + on-demand hydration

·       Storage Inventory reconciliation (at least weekly; daily for critical datasets)

#### Phase 2: Performance + operational maturity

·       Prefetch policies (manifest-driven or prefix hotness)

·       Backpressure + QoS for hydration storms

·       Better rename semantics for HNS accounts (where applicable via events)

·       “Authority by prefix” enforcement tooling

#### Phase 3: Bidirectional / deeper semantics

·       Optional per-object locking/coordination (leases, conditional requests) ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/event-grid/event-schema-blob-storage "Azure Blob Storage as Event Grid source - Azure Event Grid | Microsoft Learn"))

·       Conflict detection and resolution policy (likely “Blob wins” or “VAST wins” per prefix)

·       Consider proxy-based migration-on-read where Microsoft provides the control plane (Sippy-like / Tuscany-like direction) ([Cloudflare Docs](https://developers.cloudflare.com/r2/data-migration/sippy/ "Sippy · Cloudflare R2 docs"))

---

### 10) Research needed to finalize this appendix

These are the “prove it or don’t ship it” items:

1.        **Throughput and scaling**

o   Max sustained Event Grid event rate in target regions and our queue sizing strategy.

o   Change Feed shard/segment processing parallelism behavior under high write rates. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-change-feed "Change feed in Blob Storage - Azure Storage | Microsoft Learn"))

2.        **Event coverage gaps**

o   Precisely which operations in Blob generate which Event Grid events vs Change Feed events, especially around overwrite and metadata updates. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/event-grid/event-schema-blob-storage "Azure Blob Storage as Event Grid source - Azure Event Grid | Microsoft Learn"))

3.        **HNS customer reality**

o   How many target “hero lakes” are HNS-enabled, and whether an “AI distribution account” is acceptable.

4.        **VAST-specific implementation gaps**

o   Formal VAST spec for an “external-origin folder” behavior and supported consistency semantics across DataSpaces (we need official VAST references beyond third-party descriptions). ([Blocks and Files](https://blocksandfiles.com/2025/02/12/a-vast-effort-data-estate-vectorization-and-data-storage-for-the-ai-era/ "A VAST effort: Data estate vectorization and storage for the ..."))

---

If you want, next iteration I’ll write the **API contract** for the internal “Namespace Processor” component (webhook/queue payloads, idempotency keys, status endpoints, and metrics) and align it directly to the **Blob API MVP** section (so BlobAPI + Namespace Federation read like a single coherent product plan).

## Appendix: Deployment Models, Hardware Substrates, and DRR-Driven Economics

This appendix codifies the **multi-variant deployment thesis** for VAST + Azure: the _same_ VAST logical platform can sit on **very different hardware foundations** depending on (a) where GPUs live, (b) which Azure region(s) matter, (c) network/security constraints, and (d) flash supply + power-density realities.

It is intentionally opinionated: **standardize the software contract; vary the substrate**.

---

### A.1 Deployment model taxonomy

We will treat “VAST on Azure” as **three distinct deployment substrates**, not one:

|**Substrate**|**What it is**|**Where it lives**|**What it optimizes for**|**What it sacrifices / constrains**|
|---|---|---|---|---|
|**1) VAST on ODM hardware (GPU-adjacent)**|VAST running on VAST-qualified ODM racks (CNodes + DBoxes) adjacent to GPU fleets|Customer DC, colo, “neo-cloud”, or dedicated footprint near GPU clusters|**Deterministic performance**, best rack efficiency, full hardware control, lowest latency to GPUs|Capex + lead times, physical ops, facility constraints (power/cooling), regionality is where you can deploy|
|**2) VAST on Azure VMs (Central region / elastic)**|VAST deployed as IaaS on **storage-optimized VM families** with local NVMe (e.g., **Lasv4/Laosv4**)|Azure “hero” regions (and some satellite regions where quotas exist)|**Speed of provisioning**, Azure-native networking/governance, elastic scaling, co-location with Azure compute/services|**VM quota + SKU availability**, ephemeral local disks, virtualization overhead vs bare metal, throughput ceilings per VM family ([Microsoft Tech Community](https://techcommunity.microsoft.com/blog/azurecompute/announcing-the-general-availability-of-azure-laosv4-lasv4-and-lsv4-storage-optim/4422481 "Announcing the general availability of Azure Laosv4 ..."))|
|**3) VAST on Azure Storage-provided bare metal (co-engineered / future)**|VAST running directly on Azure-managed storage-class hardware (no hypervisor tax)|Azure-controlled infra, potentially exposed as a partner/managed offer|**Best-of-both**: cloud operational model with bare-metal performance density|Requires Microsoft partnership + productization (support boundaries, control plane wiring, security reviews); **not publicly specified** today (treat as roadmap)|

**Non-negotiable principle:** all three substrates must present **the same client-facing contract** (NFS/SMB/S3, and the proposed Blob REST endpoint), and the same **global namespace semantics** (DataSpaces) — otherwise customers can’t move workloads without refactoring.

---

### A.2 Why “multi-variant” is the only sane strategy in 2026+

#### 1) GPU locality is non-negotiable

AI training/inference pipelines are routinely **storage-limited** (random read + metadata-heavy patterns). If storage isn’t “GPU-adjacent,” you burn GPU dollars on I/O wait. The “correct” substrate is the one that can be placed **closest to the GPUs you actually have** (not the GPUs you wish you had).

#### 2) Supply chain volatility is now an architectural input

NAND pricing and availability are **not stable** in this cycle. Trend reporting indicates major price spikes and constrained supply extending into 2026, with some industry commentary suggesting tightness could persist longer. ([Tom's Hardware](https://www.tomshardware.com/tech-industry/nand-wafer-shortage-pushes-november-contract-prices-up "NAND wafer shortages push November contract prices up by over 60% - market tightens as hyperscalers purchase capacity for AI data centers"))**Implication:** We need an architecture that can:

·       deploy on **whatever flash is actually obtainable** (ODM flexibility), and/or

·       use **Azure capacity** when procurement lead times are the blocker, and/or

·       lean harder on **HDD-backed Azure Blob** as the “deep tier” when flash is scarce/overpriced.

#### 3) DRR (Data Reduction Ratio) determines whether flash is feasible

VAST’s architecture emphasizes global data reduction (dedupe/compression/similarity). VAST publicly describes “Similarity” as delivering a weighted-average data reduction across its fleet. ([VAST Data](https://www.vastdata.com/blog/similarity-reduction-report-from-the-field "Similarity Reduction: Report From the Field"))  
**Implication:** the feasibility of “all-flash at scale” depends heavily on what the dataset _actually is_ (see DRR section).

---

### A.3 Substrate details and “what you should run where”

#### A.3.1 Substrate 1 — VAST on ODM hardware (GPU-adjacent, performance-first)

**Use when**

·       You have GPU fleets in a customer-controlled facility (enterprise DC / colo / neo-cloud) and need **lowest latency** + predictable throughput.

·       You want maximum **hardware control** (drive types, network, DPU options, upgrade cadence).

·       You’re building a **repeatable AI factory** where the storage footprint is stable and amortized.

**Why it exists**

·       It’s the _most deterministic_ way to eliminate GPU starvation.

·       It’s the “escape valve” when Azure region capacity/quotas for storage-optimized SKUs are constrained.

**Operational posture**

·       Customer-managed physical ops; VAST-managed software/telemetry.

·       Pair with **Azure connectivity** (ExpressRoute / VPN) for hybrid control plane + data exchange.

**DRR impact (very high leverage)**

·       ODM deployments win disproportionately when DRR is strong (text, logs, structured tables, duplicates across corpora).

**Research needed to finalize this section**

·       Confirm ODM reference designs for “GPU-adjacent” (network topology, recommended fabric, DPU usage).

·       Validate a representative DRR distribution for frontier AI datasets (not marketing averages).

---

#### A.3.2 Substrate 2 — VAST on Azure VMs (Lasv4/Laosv4 today; Lasv5 TBD)

**What we can say confidently today (public)**

·       **Lasv4 / Laosv4** are Azure “storage optimized” VM families with **local NVMe** intended for high-throughput, low-latency workloads. ([Microsoft Tech Community](https://techcommunity.microsoft.com/blog/azurecompute/announcing-the-general-availability-of-azure-laosv4-lasv4-and-lsv4-storage-optim/4422481 "Announcing the general availability of Azure Laosv4 ..."))

·       They’re positioned specifically for heavy local storage + fast compute, which is exactly the building block you need for a VAST DASE-style deployment in Azure.

**Use when**

·       You need a **centralized Azure region** footprint to connect into Azure-native services and governance.

·       You want rapid provisioning and scaling (spin up more nodes when training bursts occur).

·       You’re building “central Blob lake ↔ GPU-adjacent VAST staging” patterns and want the staging tier in Azure.

**Core constraint you must design around**

·       **Local NVMe is not the same as durable managed storage**. A VM lifecycle event can destroy local disks.  
Your VAST deployment must assume and tolerate node loss through redundancy/erasure coding and operational automation (replace nodes, rebalance). VAST resilience work explicitly discusses designing for larger failure domains such as racks and correlated failures — the same mental model applies to cloud failure domains. ([VAST Data](https://www.vastdata.com/blog/bringing-rack-level-resilience-to-vast-part-one "Bringing Rack-Level Resilience to VAST - Part One"))

**My opinionated stance on VM-based VAST**

·       VM substrate is your **elastic performance tier** and “integration beachhead” into Azure.

·       Do **not** attempt to make the VM substrate your cheapest deep archive. Let Blob do that.

**Where Lasv5 comes in**

·       You called out Lasv5 as a likely candidate. We could not validate public Lasv5 details in the available research window, so treat it as **“candidate next-gen SKU family”** until confirmed.**Action:** add a “VM SKU confirmation” checklist to the doc before final publish.

**Research needed to finalize**

·       Confirm Lasv4/Laosv4 regional availability + quota strategy for target “hero regions.”

·       Confirm exact behavior on VM deallocation/maintenance and how that maps to VAST rebuild times and customer SLAs.

---

#### A.3.3 Substrate 3 — VAST on Azure Storage-provided bare metal (strategic bet)

**What this is**

·       A co-engineered model where VAST runs on Azure-provided storage-class hardware without the typical hypervisor/VM constraints.

**Why it matters**

·       It’s the only path that plausibly combines:

o   **cloud operational model** (Azure-managed footprint) and

o   **near-ODM performance density** (bare metal, direct device control).

**Where it fits**

·       “Central region, very large footprint” scenarios where VM-based ceilings become expensive/complex.

·       Workloads that want a “storage service” feel but require the VAST stack and semantics.

**Hard truth**

·       This is not an engineering-only decision; it’s a **product + partnership** decision with Microsoft:

o   support boundaries

o   security model

o   private networking primitives

o   control plane integration (resource provider wiring)

o   marketplace/commercial packaging

**Research needed**

·       Define the minimum Azure-side primitives required (deployment, lifecycle, telemetry hooks).

·       Define how Private Link and “picker-based” first-party services would treat this deployment (does it get a first-class Azure Resource ID?).

---

### A.4 DRR as a first-class design input

#### A.4.1 What DRR is (and what it is not)

·       **DRR = effective capacity multiplier** from dedupe + compression + similarity.

·       DRR is **workload-dependent**, not vendor-dependent.

VAST describes its “Similarity” approach as delivering a weighted-average data reduction across its global fleet. ([VAST Data](https://www.vastdata.com/blog/similarity-reduction-report-from-the-field "Similarity Reduction: Report From the Field"))  
Treat that as **directional**; you still need to measure your corpus.

#### A.4.2 DRR expectations by dataset type (rule-of-thumb)

This table is intentionally pragmatic; it tells solution architects what to expect _before_ running a pilot:

|**Data type**|**DRR expectation**|**Why**|**Design implication**|
|---|---|---|---|
|Source code, text corpora, logs|High|High redundancy + compressibility|ODM becomes extremely cost-effective; VM clusters can be smaller|
|Parquet/ORC tables|Medium|Columnar compression exists but duplication still common|DRR helps; also consider VAST DataBase/query pushdown|
|Model checkpoints (large binary blobs)|Low–Medium|Often already compressed; repetition varies|Plan for high sustained bandwidth more than DRR|
|JPEG/PNG images|Low|Pre-compressed|DRR not a savior; capacity tiering to Blob matters|
|Video (H.264/H.265)|Very low|Highly compressed|Treat DRR as near-1:1; build storage economics around tiering|
|Encrypted-at-source objects|Very low|Encryption destroys dedupe/compress|Avoid double-encryption that kills DRR unless required|

**Opinionated policy:**For each target workload, publish a **DRR assumption range** and force the pilot to measure it. If measured DRR is below the assumed floor, the design must pivot harder toward Blob tiering and/or capacity planning changes.

#### A.4.3 DRR and tiering format choice

If you tier data from VAST to Blob:

·       **Opaque/VAST-native layout** preserves VAST reduction benefits but makes Blob objects less directly usable by Azure services.

·       **Transparent/native objects** improve ecosystem interoperability but can reduce overall DRR benefits and increase Blob costs.

(We already treat this as a top-level decision record elsewhere; this appendix just ties it to deployment model economics.)

---

### A.5 Workload-to-substrate mapping

This is the table we should keep coming back to in reviews; it forces alignment between architecture and real workloads.

|**Workload**|**Primary substrate**|**Secondary substrate**|**Why**|
|---|---|---|---|
|**Frontier training (GPU-adjacent)**|**ODM adjacent to GPUs**|Azure VM cluster in same region as GPU fleet|Latency + predictable throughput dominate|
|**Centralized “hero region” staging + governance**|**Azure VMs (Lasv4/Laosv4)**|Bare metal (future)|Fast Azure integration, elastic scaling, “cloud feel”|
|**Hybrid burst (on-prem training ↔ Azure overflow)**|ODM on-prem + Azure VM endpoint|—|DataSpaces + caching patterns; keep working set near compute|
|**RAG / vector + retrieval layer**|ODM or Azure VM depending on where inference runs|—|Retrieval is latency-sensitive; choose substrate near inference tier|
|**Fabric-first analytics on cold/archival**|Azure Blob (system of record)|VAST as accelerator for hot slices|Fabric’s managed network model favors Blob; use VAST selectively|
|**Mass migration / onboarding**|Azure VMs (as movers)|ODM if migration source is on-prem high speed|VM movers are easy to spin up; ODM movers if WAN isn’t the bottleneck|

---

### A.6 Supply chain strategy embedded in deployment choices

Given the current NAND volatility signals (price spikes, constrained supply), the deployment strategy should explicitly support **supply substitution**: ([Tom's Hardware](https://www.tomshardware.com/tech-industry/nand-wafer-shortage-pushes-november-contract-prices-up "NAND wafer shortages push November contract prices up by over 60% - market tightens as hyperscalers purchase capacity for AI data centers"))

1.        **Flash where it matters** (GPU-adjacent working set, hot metadata, checkpoints)

2.        **HDD economics where it doesn’t** (Blob as deep capacity tier)

3.        **Multiple procurement paths** (ODM sourcing + Azure capacity + potential bare metal partnership)

**Opinionated recommendation:**Treat **Azure Blob** as the default “deep tier” for exabyte-scale lakes during this supply cycle, and use VAST flash substrates primarily as **performance tiers**.

---

### A.7 Operational notes that must be in the main doc (but belong here as “appendix truth”)

·       **Cloud failure domains are correlated.** Design for “rack-like” correlated failures (maintenance events, host groups) the same way you design for racks on-prem. VAST has explicitly discussed rack-level resilience techniques to tolerate larger failure domains efficiently. ([VAST Data](https://www.vastdata.com/blog/bringing-rack-level-resilience-to-vast-part-one "Bringing Rack-Level Resilience to VAST - Part One"))

·       **VM local NVMe is a different durability contract** than managed disks; the deployment must assume node turnover as normal (automated replace + rebalance).

·       **Quota/availability is part of the deployment spec.** For VM substrates, “Can I get 200 Lasv4 nodes in East US 2 next month?” is not an implementation detail; it’s a gating requirement.

---

### A.8 Research backlog to complete this appendix (make it “defensible”)

1.        **Confirm Lasv5 reality** (if it exists publicly): SKUs, local NVMe size, bandwidth, regional rollout.

2.        **Publish a DRR measurement methodology** (standard dataset sampling, encryption caveats, confidence intervals).

3.        **Quantify performance per substrate** with the same benchmark harness (AI shard read, metadata ops/s, checkpoint write throughput).

4.        **Supply chain evidence pack** (replace secondary sources with primary/industry analyst references if possible; keep Tom’s Hardware as supporting color, not the pillar). ([Tom's Hardware](https://www.tomshardware.com/tech-industry/nand-wafer-shortage-pushes-november-contract-prices-up "NAND wafer shortages push November contract prices up by over 60% - market tightens as hyperscalers purchase capacity for AI data centers"))

5.        **Bare metal feasibility memo**: required Microsoft primitives, packaging, and the control-plane path to make it “first-party-like.”

---

### Appendix add-on: “Deployment selection” flowchart (doc-ready)

```
flowchart TD
```

```
  A[Start: Define workload] --> B{Are GPUs local to customer facility?}
```

```
  B -->|Yes| C[Choose ODM GPU-adjacent VAST]
```

```
  B -->|No| D{Are GPUs in Azure + need Azure-native integration?}
```

```
  D -->|Yes| E[Choose VAST on Azure VMs (Lasv4/Laosv4)]
```

```
  D -->|No| F[Choose ODM in nearest colo/neo-cloud]
```

```
  E --> G{Do you need service-like, bare-metal density?}
```

```
  G -->|Yes (future)| H[Evaluate Azure Storage bare metal co-engineered option]
```

```
  G -->|No| I[Use Blob as deep tier + VAST as performance tier]
```

```
  C --> I
```

```
  F --> I
```

If you want, I can also generate a **second table** that maps each deployment substrate to **networking patterns** (VNet injection vs managed VNet vs Private Link) and explicitly calls out which Azure first-party services are viable per substrate.

Below is a **v0.4 delta plan** that directly closes the holes you called out, plus copy‑paste‑ready sections/appendices you can drop into the doc.

I’m going to be explicit where Azure’s “managed network” reality or product constraints force a particular design choice, and I’ll attach **reference URLs** (citations) wherever we’re asserting something concrete about Azure networking/features.

---

# 1) New Sections to Add (Doc Structure Changes)

### Add to main body (recommended placement)

1.        **Section X — Commercial Integration & Marketplace Strategy (MACC / transactability)**

2.        **Section Y — Identity & Zero Trust Readiness (Entra ID / Managed Identity as MVP)**

3.        **Section Z — Tiering Modes vs Ecosystem Access (Opaque vs Transparent vs Hybrid)**

4.        **Section AA — Managed VNet Connectivity Playbook (PLS Alias + Approval Workflow)**  
(This is the “how it actually works” for Fabric/Synapse/Serverless Databricks etc.)

5.        **Section AB — Compatibility & Conformance Harness (Tools + SDKs)**(Explicitly adds `azure-storage-blob` Python SDK as a _go/no-go_ gate.)

### Add to appendices (recommended)

·       **Appendix C — Blob API MVP + Compatibility Harness (AzCopy + boostedblob + Azure SDK)**

·       **Appendix D — Namespace & Metadata Federation Design (Change Feed/Event Grid/Stub model)**

·       **Appendix E — Deployment Variants & Supply Chain Constraints (ODM vs Lasv4/Lasv5 vs Azure Bare Metal)**

·       **Appendix F — Private Link Service (PLS) Operational Runbook (Approval + DNS + multi-tenant)**

---

# 2) Section X — Commercial Integration & Marketplace Strategy (Copy/Paste)

## Commercial Integration & Marketplace Strategy

### Why this section exists

Azure-native adoption fails if procurement cannot transact in an Azure-aligned way (e.g., **draw down Azure commitment** and purchase through familiar channels). This document therefore defines **how the customer buys VAST** across the deployment variants (ODM, VM-based, and potential Azure bare metal).

### Commercial goals

·       **Transactable** (ideally through Azure Marketplace) so customers can align spend with Azure procurement and consumption motions.

·       Clear separation of what is billed as **Azure infrastructure** (VMs, network, disks) vs **VAST software/services**.

·       A consistent “SKU story” across deployment variants.

### Variant-based commercial patterns

#### Variant A — VAST on Azure VMs (Lasv4 / Lasv5)

**Recommended commercial packaging:**

·       **Azure Marketplace Managed Application** (or Solution Template) that deploys the VAST cluster into the customer subscription/VNet.

·       Customer pays:

1.        **Azure infrastructure costs** directly (VMs, networking, etc.), and

2.        **VAST software subscription** (metered or BYOL) via Marketplace terms.

**Why this is the “default”:**

·       Matches how customers procure most ISV infra stacks on Azure.

·       Aligns to repeatable deployment patterns (IaC, standard networking, standard monitoring).

#### Variant B — VAST ODM hardware adjacent to GPUs (on‑prem / colo / edge)

**Recommended commercial packaging:**

·       **Direct quote** for hardware + software subscription, with optional Azure‑aligned contracting (private offers / reseller motions) depending on customer procurement.

**Reality check:**This model is often chosen due to **supply chain**, rack density, power/space efficiency, or customer sovereignty constraints. It is not inherently “Azure consumption,” even if it integrates with Azure services.

#### Variant C — VAST on Azure “storage-provided” bare metal (opportunity)

**Recommended commercial packaging:**

·       Treat as **co-sell / special program** until productized.

·       Document it explicitly as **“under consideration”** with preconditions: region availability, hardware program availability, and Microsoft/VAST joint support boundary.

### Procurement risks to surface (explicitly)

·       If customers require “Azure-native commit burn” for software costs, Marketplace transactability becomes a gating item.

·       If regulated customers require Entra ID (token-based) auth on Day 1, then Marketplace-ready identity and governance become adoption multipliers (see next section).

---

# 3) Section Y — Identity & Zero Trust Readiness (Copy/Paste)

## Identity & Zero Trust Readiness

### Why identity cannot be “Phase 2”

Many Azure-first AI environments are moving to **secretless access** (Managed Identity / workload identities) specifically to avoid long-lived storage keys and difficult-to-govern SAS patterns. Azure’s own guidance frames managed identities as avoiding credential management by providing an automatically managed identity for Azure resources. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview "Managed identities for Azure resources - Managed identities for Azure resources | Microsoft Learn"))

### MVP identity requirement (explicit)

**Blob API MVP must support token-based auth (Entra ID / OAuth Bearer) as a first-class path**, not a post-MVP enhancement.

### Supported auth modes (recommended MVP stance)

1.        **Entra ID (OAuth Bearer tokens) — MUST for MVP**

o   Enables secretless access patterns required by many enterprise deployments.

o   Aligns with Managed Identity usage (system-assigned/user-assigned) where workloads obtain tokens from Entra without distributing secrets. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview "Managed identities for Azure resources - Managed identities for Azure resources | Microsoft Learn"))

2.        **SAS + Shared Key — Supported, but treated as “compatibility mode”**

o   Still required for some integration surfaces and legacy tooling.

o   Must be clearly documented as a **security tradeoff** and potentially disallowed by customer policy in regulated environments.

### Practical implication for Fabric (callout)

Fabric’s **S3-compatible shortcut** path is currently constrained to **key/secret-style authentication**, and explicitly does not support Entra OAuth for that connection type. ([Microsoft Learn](https://learn.microsoft.com/en-us/fabric/onelake/create-s3-compatible-shortcut "Create an Amazon S3 compatible shortcut - Microsoft Fabric | Microsoft Learn"))  
So: even if VAST Blob API supports Entra, **Fabric S3 shortcuts still drive a secret-based requirement** for that specific integration path.

### Authorization model options (opinionated)

·       **Option A (fastest): coarse RBAC mapping** (Reader/Writer/Admin per container/prefix).

o   Good for MVP; lowest friction.

·       **Option B (Azure RBAC semantic parity):** map Entra roles/claims to fine-grained permissions.

o   Highest compatibility; more work.

·       **Recommendation:** Start with **Option A** with a clear roadmap to Option B. The critical MVP test is “token works, no secrets required,” then progressively enhance authorization parity.

### AKS-specific identity callout (CSI driver)

If AKS workloads are expected to be secretless, validate whether the VAST CSI driver supports a workload-identity pattern (federated tokens) versus static secrets in Kubernetes Secrets.  
**If not supported, document as a security risk and adoption limiter** for security-sensitive Kubernetes environments.

---

# 4) Section Z — Tiering Modes vs Ecosystem Access (Copy/Paste)

## Tiering Modes vs Ecosystem Access

### Why this matters

Our document currently recommends “opaque tiering” for economics, but this has a critical architectural side-effect: **opaque tiering forces reads back through VAST**, which can conflict with Azure-native analytics patterns where services read _directly_ from Blob.

### Define the three modes (use these names consistently)

1.        **Opaque Tiering (VAST-native object layout in Blob)**

o   **Pros:** best DRR, best economics, best VAST-managed performance.

o   **Cons:** data in Blob is not directly consumable by services expecting open formats.

o   **Implication:** analytics consumers must access through **VAST S3/NFS** (or VAST must rehydrate).

2.        **Transparent Tiering (open-format objects in Blob)**

o   **Pros:** services like Fabric can read directly from Blob if formats are open (Parquet/Delta, etc.).

o   **Cons:** reduced DRR / less freedom for VAST-native layout; may trade some cost efficiency.

3.        **Hybrid Tiering (recommended)**

o   Apply **opaque tiering for GPU-adjacent “working set”** and performance-critical data.

o   Apply **transparent tiering for “analytics lake” datasets** where Fabric/Synapse are expected to read directly.

### Fabric-specific callout (non-negotiable constraint)

·       Fabric’s S3 shortcut integration expects to read data via the configured S3-compatible endpoint and has specific requirements around how that endpoint behaves. ([Microsoft Learn](https://learn.microsoft.com/en-us/fabric/onelake/create-s3-compatible-shortcut "Create an Amazon S3 compatible shortcut - Microsoft Fabric | Microsoft Learn"))

·       If data is tiered to Blob opaquely, **Fabric cannot magically interpret VAST-native chunks**. This should be stated explicitly as a tradeoff.

---

# 5) Section AA — Managed VNet Connectivity Playbook (PLS Alias + Approval) (Copy/Paste)

## Managed VNet Connectivity Playbook

### The key reality: managed services need Private Link patterns that include approvals

For services operating inside Microsoft-managed networks, connectivity often requires **Private Link** to supported resources or a **Private Link Service (PLS)** hosted by the customer/partner, with an explicit approval workflow.

### Private Link Service (PLS) role

Azure Private Link Service enables you to publish a partner/customer service behind a private endpoint so consumers can connect privately. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/private-link/private-link-service-overview "What is Azure Private Link service? | Microsoft Learn"))

### Fabric: what’s actually supported

Fabric supports creating **managed private endpoints** in the workspace and includes explicit steps for approving private endpoint connections, including PLS scenarios and allowing admins to configure which subscription IDs can be auto-approved. ([Microsoft Learn](https://learn.microsoft.com/en-us/fabric/security/workspace-outbound-access-protection-allow-list-endpoint "Create an allow list using managed private endpoints - Microsoft Fabric | Microsoft Learn"))

### Fabric + on-prem / behind firewall shortcut pattern

Fabric supports creating shortcuts to **on-premises data sources** using an **on-premises data gateway**, including S3-compatible storage that is hosted on-prem or behind a firewall. ([Microsoft Learn](https://learn.microsoft.com/en-us/fabric/onelake/create-on-premises-shortcut "Create shortcuts to on-premises data - Microsoft Fabric | Microsoft Learn"))

### Engineering requirement: PLS connection approval workflow

**We must document and operationalize:**

·       Who owns the PLS (customer vs VAST-managed)?

·       Who approves inbound private endpoint connection requests?

·       How approvals are automated (or at least made repeatable), especially in multi-tenant scenarios.

This is not “nice-to-have.” It is the difference between a 2-hour deployment and a 2-week deployment.

### Recommended runbook excerpt (include in Appendix F)

1.        Deploy VAST endpoint behind a PLS. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/private-link/private-link-service-overview "What is Azure Private Link service? | Microsoft Learn"))

2.        Consumer creates private endpoint (Fabric managed private endpoint / Databricks NCC / etc.). ([Microsoft Learn](https://learn.microsoft.com/en-us/fabric/security/workspace-outbound-access-protection-allow-list-endpoint "Create an allow list using managed private endpoints - Microsoft Fabric | Microsoft Learn"))

3.        Connection lands in **Pending** state.

4.        Approver validates request metadata and approves. ([Microsoft Learn](https://learn.microsoft.com/en-us/fabric/security/workspace-outbound-access-protection-allow-list-endpoint "Create an allow list using managed private endpoints - Microsoft Fabric | Microsoft Learn"))

5.        Private DNS configuration validated (service name resolves to private IP).

6.        Health check from managed service confirms connectivity.

---

# 6) Section AB — Compatibility & Conformance Harness (Copy/Paste)

## Compatibility & Conformance Harness

### Why `azcopy` passing is not enough

We must validate compatibility against both:

·       **Tooling clients** (`azcopy`, boostedblob / rclone-like high concurrency), and

·       **SDK clients** (especially Azure Python SDK), because AI engineers often embed storage access in training and ETL code.

### MVP Go/No-Go: three conformance gates

1.        **AzCopy Gate:** `azcopy copy/sync` with server-side copy paths and large blob uploads.

2.        **High-Concurrency Gate:** boostedblob-style parallel PUT block / range GET patterns at high concurrency.

3.        **Azure SDK Gate (Python):** `azure-storage-blob` end-to-end upload/download/list/error semantics.

### What gets tested (minimum)

·       Block blob upload via Put Block / Put Block List

·       Range reads

·       List Blobs XML parsing + pagination + delimiter behavior

·       Error body correctness (XML error codes)

·       Auth variants: Entra token path + SAS/key fallback paths

### Why this belongs in the doc

Because “it worked for `azcopy`” does not equal “it works for AI developer code.”

---

# 7) Updates to the Azure Service Matrix (Targeted Fixes)

Below are the **specific changes** I recommend making to the existing “Top Azure Services” matrix, based on the constraints you asked to verify.

## 7.1 Microsoft Fabric row (refined)

Add **two sub-rows** under Fabric:

### Fabric — S3-compatible Shortcuts

·       **Key reality:** S3-compatible shortcut has explicit endpoint/auth constraints; it relies on key/secret style auth and has endpoint formatting requirements. ([Microsoft Learn](https://learn.microsoft.com/en-us/fabric/onelake/create-s3-compatible-shortcut "Create an Amazon S3 compatible shortcut - Microsoft Fabric | Microsoft Learn"))

·       **Private network reality:** if the endpoint is on-prem/behind firewall, Fabric supports using an on-premises data gateway to create the shortcut. ([Microsoft Learn](https://learn.microsoft.com/en-us/fabric/onelake/create-on-premises-shortcut "Create shortcuts to on-premises data - Microsoft Fabric | Microsoft Learn"))

### Fabric — Managed Private Endpoints (general)

·       Fabric supports managed private endpoints and a workflow to approve private endpoint connections, including PLS patterns. ([Microsoft Learn](https://learn.microsoft.com/en-us/fabric/security/workspace-outbound-access-protection-allow-list-endpoint "Create an allow list using managed private endpoints - Microsoft Fabric | Microsoft Learn"))

## 7.2 Azure Databricks row split: Classic vs Serverless

### Databricks Classic Compute

·       Keep as “customer VNet injected” integration (easy path).

### Databricks Serverless (SQL, Model Serving, etc.)

·       Add a new row:

o   **Network:** serverless compute plane, requiring explicit network connectivity configuration patterns. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/databricks/security/network/ "Networking - Azure Databricks | Microsoft Learn"))

o   **Requirement:** support Private Link–style private endpoints via the Databricks network connectivity configuration model. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/databricks/security/network/serverless-network-security/ "Serverless compute plane networking - Azure Databricks | Microsoft Learn"))

This directly addresses the “Databricks is pushing serverless” risk.

## 7.3 PLS Alias / Approval workflow column

Add a column called: **“Connection Approval Required?”**

·       Fabric managed private endpoints explicitly require approval flows (and can support auto-approval rules by subscription ID). ([Microsoft Learn](https://learn.microsoft.com/en-us/fabric/security/workspace-outbound-access-protection-allow-list-endpoint "Create an allow list using managed private endpoints - Microsoft Fabric | Microsoft Learn"))

·       Databricks serverless private endpoint flows are part of the NCC design and must be handled operationally. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/databricks/security/network/serverless-network-security/ "Serverless compute plane networking - Azure Databricks | Microsoft Learn"))

---

# 8) Two Opportunities Worth Adding as New Scenarios

## Opportunity — Cross-Region Global Namespace using Azure backbone

Add a scenario section (even short) describing:

·       Training in West US 3, data lake in East US 2

·       VAST instances in each region, synced via DataSpace replication

·       Connectivity via Azure backbone networking constructs (vWAN / global peering patterns)

·       Value: replication deduped over the wire, avoids blunt “GRS everywhere” patterns

## Opportunity — Azure Lighthouse for fleet management

Add an operational appendix:

·       Managing many VAST clusters across tenants/subscriptions

·       Use Azure Lighthouse delegated resource management concepts to centralize operations. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/private-link/create-private-link-service-portal "Quickstart - Create a Private Link service - Azure portal"))

---

# 9) What I’d Mark as “Needs Validation” (Explicitly, in the doc)

These are important enough to mention now, but we should mark them as validation items so we don’t over-claim:

1.        **VAST CSI driver + AKS Workload Identity support**

o   If not supported, call out a secret-management risk for K8s.

2.        **VAST “ANF as backend cache” feasibility**

o   If VAST can treat external NFS exports as a namespace backend/cached mount, this is a migration-free acceleration story. If not, propose SyncEngine-based ingestion as fallback.

---

## If you want the cleanest integration narrative for v1.0

I’d implement the doc changes in this order (highest risk first):

1.        **Identity/Entra as MVP** (or explicitly “blocker for regulated customers”)

2.        **Commercial transactability** (how customers buy it)

3.        **Databricks Serverless + NCC row**

4.        **Tiering conflict (Opaque vs Fabric direct access)**

5.        **PLS approval runbook + operationalization**

6.        **SDK conformance harness**

If you paste these sections in, your v1.0 will read like something an Azure platform architect and procurement lead can both sign off on—because it addresses the “painful Managed VNet reality” and the “how do we buy it” reality head-on.