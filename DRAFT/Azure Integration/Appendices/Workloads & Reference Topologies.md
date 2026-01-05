# Workloads & Reference Topologies

**Scope:** Deployment variants + workload patterns used throughout the VAST + Azure integration collateral.

**Related references:**
- VAST engineering delivery plan: [Engineering Delivery Plan](../VAST/Engineering%20Delivery%20Plan.md)
- Microsoft engineering alignment & asks: [Engineering Alignment & Asks](../Microsoft/Engineering%20Alignment%20%26%20Asks.md)
- Azure service integration matrix: [Azure Native Services Integration Matrix](Azure%20Native%20Services%20Integration%20Matrix.md)
- Terminology & conventions: [Terminology & Conventions](Terminology%20%26%20Conventions.md)

This appendix turns strategy into deployable architectural patterns. It maps scenarios to concrete deployment variants and integration mechanics.

## Deployment Variants (VAST on/with Azure)

- **Variant A (ODM / edge):** VAST hardware adjacent to GPUs/CPUs in customer datacenters, colocation facilities, or neo‑clouds; best for maximum density and performance.
- **Variant B (Azure IaaS):** VAST software on storage‑optimized Azure VMs (Lasv4/Lasv5) with local NVMe; best for elasticity and cloud‑native VNet integration.
- **Variant C (Azure bare metal):** Future/roadmap: VAST on Azure‑provided bare metal for high‑density managed service scenarios.
- **Variant D (Hybrid):** Unified namespace spanning a mix of on‑prem ODM clusters and Azure VM clusters.

## Workloads

### W1: On‑Prem VAST + Burst Compute on Azure

- **Scenario:** A customer holds massive datasets on premises (gravity/compliance) but needs ephemeral Azure CPU/GPU capacity to hit deadlines without migrating petabytes or refactoring POSIX applications.
- **Topology & flow:** On‑prem VAST ODM is the data origin; a temporary Variant B cluster in Azure acts as a caching satellite; connected via ExpressRoute.
- **VAST + Azure integration:** Breaks data gravity by presenting a unified namespace to cloud compute; the Azure satellite caches only the hot working set to mask WAN latency and avoid egress shock.

### W2: Central Blob Lake + GPU‑Adjacent VAST Satellites

- **Scenario:** A model builder keeps the system of record in a central Azure “Hero Region” for governance and capacity, but trains in a neo‑cloud or colo due to power/silicon constraints. WAN latency and checkpoint uploads stall GPUs.
- **Topology & flow:** Azure Blob Storage (central region) for durability; Variant A (ODM) deployed inside the neo‑cloud/colo adjacent to the GPU fabric. Training data hydrates from Azure Blob Storage → VAST; checkpoints flow VAST → Azure Blob Storage.
- **VAST + Azure integration:** Using the Blob API façade, teams can use standard AzCopy, VAST SyncEngine, or other Blob‑native transfer patterns to hydrate VAST from the central lake without pipeline refactors. Training writes checkpoints locally at NVMe speed (often via GPUDirect Storage over NFS), then VAST asynchronously syncs checkpoints back to Azure Blob Storage for durability and lineage.

### W3: Streaming Data Pipelines (Kafka & Event Broker)

- **Scenario:** High‑velocity ingest from IoT fleets/telemetry/logs needs real‑time persistence plus historical analysis; traditional Kafka retention is expensive at scale.
- **Topology & flow:** Variant A (edge) or Variant B (Azure). Producers write to VAST; consumers (Spark/Azure Stream Analytics) read from VAST.
- **VAST + Azure integration:** Using the VAST Event Broker, producers write to VAST using Kafka protocols; VAST persists streams on flash (tiered to Azure Blob Storage) for “infinite retention.” Downstream Azure services can query historical data directly via S3/Parquet patterns without rehydration steps.

### W4: Spark & Databricks Analytics (VAST DataBase)

- **Scenario:** Azure Databricks/Spark teams hit I/O bottlenecks during shuffle phases and high‑concurrency queries against standard object stores.
- **Topology & flow:** Variant B (Azure). Databricks clusters in the same VNet interact with VAST.
- **VAST + Azure integration:** VAST DataBase can push down predicates (filters/projections) to the storage layer so only relevant results traverse the network, enabling stateless/lean compute that scales independently of storage performance.

### W5: Hybrid Cloud Tiering (On-Prem Flash to Azure Blob Storage)

- **Scenario:** Flash performance is needed for recent/hot data, but cloud economics are needed for the cold tail (PACS, media archives, backups).
- **Topology & flow:** Variant A (on‑prem) tiers to Azure Blob Storage (Cool/Cold).
- **VAST + Azure integration:** Remote sites ingest at flash speed on small VAST footprints and tier to a central Azure Blob Storage lake for low‑cost durability. In a disaster, a new VAST instance can spin up in Azure (or a secondary site) and resume operations by reading metadata from Azure Blob Storage and hydrating only on demand.

### W6: Ecosystem Access (Azure PaaS Integration)

- **Scenario:** Data on VAST must trigger Azure Functions/Event Grid, or be accessible to Azure 1P services (e.g., AI Foundry) without heavy data movement.
- **Topology & flow:** Variant B (Azure) connected to Azure PaaS via “Tuscany” patterns, VNet injection, and/or Private Link.
- **VAST + Azure integration:**
  - **Tuscany (migration‑on‑read proxy pattern):** enable on‑read federation where Azure services interact with VAST data “as if” it were native Blob.
  - **Eventing:** integrate with Azure Event Grid so “file landed” can trigger Azure Functions for tokenization, embedding, or indexing.
  - **Fabric:** expose VAST data to Microsoft Fabric via S3‑compatible shortcuts for query‑in‑place.

### W7: Cloud Native Applications (AKS & Microservices)

- **Scenario:** AKS workloads need high‑throughput Read‑Write‑Many (RWX) persistent storage; standard cloud file services often throttle.
- **Topology & flow:** Variant B (Azure) linked to AKS clusters in the customer VNet.
- **VAST + Azure integration:** VAST provides shared file performance to AKS via the CSI driver (and/or direct NFS), enabling many microservices to share a single high‑performance persistence layer.

### W8: Cross‑Region Training & Global WAN

- **Scenario:** Multinational teams collaborate on shared datasets across US/EU/APAC without public-internet variability.
- **Topology & flow:** Variant B (multi‑region) connected via Azure Virtual WAN and VAST DataSpace.
- **VAST + Azure integration:** Combine VAST global namespace with Azure’s backbone to replicate deterministically; VAST similarity‑based global dedup ensures only unique bytes traverse the wire.

### W9: Regulated AI & Enclaves (Sovereign & Hybrid)

- **Scenario:** Financial services/defense customers need sovereign controls: cloud agility without the provider accessing data or keys.
- **Topology & flow:** Variant B (isolated VNet) or Variant D (hybrid) with Customer‑Managed Keys (CMK).
- **VAST + Azure integration:** Deploy inside locked‑down VNets with strict private connectivity and customer‑held keys. The goal is a “logical air‑gap” posture that supports residency and audit requirements (ITAR/GDPR) while retaining cloud provisioning speed.

### W10: Migration & Modernization

- **Scenario:** Exiting legacy on‑prem NAS (NetApp/Isilon) is blocked because applications rely on protocol behaviors cloud‑native storage doesn’t fully emulate.
- **Topology & flow:** Source (legacy) → Target (Variant B).
- **VAST + Azure integration:** VAST provides protocol parity (NFSv3/v4, SMB, S3) to enable “zero‑refactor” lift‑and‑shift. Customers can modernize incrementally by leveraging VAST multi‑protocol access.

## Workload Alignment Matrix

|---|---|---|---|
|Workload|Recommended VAST Variant|Integration Pattern|Key Value Driver|
|W1: Burst Compute|Variant D (Hybrid)|Global Namespace (Cache)|Elasticity without Egress Shock|
|W2: GPU Adjacent|Variant A|Blob API; Tiering (cache)|Performance and efficiency|
|W3: Streaming|Variant A/B|VAST Event Broker|Infinite Retention & Real-time Query|
|W4: Spark/Databricks|Variant B|VAST DataBase (Pushdown)|Zero-Shuffle Analytics|
|W5: Hybrid Tiering|Variant A|Transparent/Opaque Tiering|Edge Ingest & BCDR|
|W6: Ecosystem (PaaS)|Variant B|Tuscany / Event Grid|Seamless "Migration-on-Read"|
|W7: Cloud Native (AKS)|Variant B|CSI Driver / NFS|True RWX Performance|
|W8: Global Namespace|Variant B (Multi)|Azure Virtual WAN|Dedupe-Optimized Global Backbone|
|W9: Regulated AI|Variant A/B|Private Link / Enclave|Sovereign Data Control|
|W10: Migration|Variant B|Multiprotocol (NFS/SMB)|Risk-Free Cloud Entry|

## Open Items

Tracked in: [TODO](../TODO.md)
