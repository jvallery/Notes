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
- **Associated Microsoft 1P services (typical):**
  - **Azure Virtual Machines (VMSS, GPU SKUs):** burst compute plane; jobs mount/access VAST via NFS/SMB/S3.
  - **Azure ExpressRoute (or VPN Gateway):** private hybrid connectivity between on‑prem and Azure VNets for predictable throughput/latency.
  - **Azure Private Link / Private Link Service:** optional private exposure for storage endpoints across VNets/tenants.
  - **Azure Batch / Azure CycleCloud (optional):** schedulers for burst/HPC job execution.
- **Typical Azure 1P deployment pattern (baseline):**
  - On‑prem VAST is the authoritative dataset (NFS/SMB/S3) with ExpressRoute into an Azure landing zone VNet.
  - Burst compute runs on VMSS (optionally under Batch/CycleCloud); jobs mount VAST directly over private IP and follow strict egress controls.
  - If direct reads are too WAN-sensitive, a VAST Variant B “cache satellite” runs in Azure and is warmed via replication/sync from on‑prem.
  - Observability lands in Azure Monitor/Log Analytics; identity uses Entra ID (and, where applicable, workload identities/service principals).
- **Typical open‑source deployment pattern (baseline):**
  - Burst compute runs on self-managed **Slurm** or **Kubernetes** on Azure VMs; jobs mount VAST via NFS/SMB or use S3 clients.
  - Orchestration uses **Argo Workflows** or **Airflow**; data movers include **rsync/rclone/s5cmd**.
  - Observability uses **Prometheus + Grafana** and centralized logging (e.g., **OpenSearch**).
- **Where VAST fits (in both patterns):**
  - VAST stays the high-performance origin on‑prem while enabling Azure compute to access data without pre-copying petabytes.
  - VAST Variant B provides an Azure-local cache tier when WAN variability or high fan-out makes direct reads inefficient.
  - Multi‑protocol access reduces refactor pressure and lets teams adopt object workflows incrementally.

### W2: Central Blob Lake + GPU‑Adjacent VAST Satellites

- **Scenario:** A model builder keeps the system of record in a central Azure “Hero Region” for governance and capacity, but trains in a neo‑cloud or colo due to power/silicon constraints. WAN latency and checkpoint uploads stall GPUs.
- **Topology & flow:** Azure Blob Storage (central region) for durability; Variant A (ODM) deployed inside the neo‑cloud/colo adjacent to the GPU fabric. Training data hydrates from Azure Blob Storage → VAST; checkpoints flow VAST → Azure Blob Storage.
- **VAST + Azure integration:** Using the Blob API façade, teams can use standard AzCopy, VAST SyncEngine, or other Blob‑native transfer patterns to hydrate VAST from the central lake without pipeline refactors. Training writes checkpoints locally at NVMe speed (often via GPUDirect Storage over NFS), then VAST asynchronously syncs checkpoints back to Azure Blob Storage for durability and lineage.
- **Associated Microsoft 1P services (typical):**
  - **Azure Blob Storage:** governed system of record and durable checkpoint sink.
  - **Microsoft Entra ID:** identity plane for SDK/tooling auth patterns (service principals, managed identities).
  - **Azure Private Link (Blob private endpoints):** private access to hero-region Blob from Azure VNets and controlled hybrid routes.
  - **Azure Event Grid / Blob Change Feed (optional):** change detection/eventing for downstream workflows.
  - **Azure Monitor / Log Analytics:** telemetry for transfer throughput, errors, and sync lag.
- **Typical Azure 1P deployment pattern (baseline):**
  - Blob in the hero region is the authoritative lake (governance, durability, ecosystem); private endpoints are enabled for enterprise deployments.
  - Orchestration and governance live in Azure control planes (e.g., AML for experiment/pipeline tracking) even when compute is external.
  - Data movement uses AzCopy/SDKs over private routes where possible; eventing uses Event Grid/change feed to trigger downstream processing and cataloging.
- **Typical open‑source deployment pattern (baseline):**
  - Training runs on self-managed **Kubernetes** or **Slurm** in colo/neo‑cloud; workflows use **Argo**, **Ray**, or **Kubeflow**.
  - Data movement uses **rclone/s5cmd/azcopy**; dataset versioning uses **DVC** or **lakeFS**; artifact tracking uses **MLflow**.
  - Metadata/catalog (if needed) uses **DataHub/OpenMetadata**.
- **Where VAST fits (in both patterns):**
  - VAST is the GPU‑adjacent performance tier (hot dataset + fast checkpoint writes) while Blob remains the system of record.
  - The Blob API façade minimizes refactors by letting standard Azure tooling target the VAST endpoint during training.
  - Multi‑protocol access (NFS for training paths, Blob/S3 for tool ecosystems) reduces “two worlds” friction.

### W3: Streaming Data Pipelines (Kafka & Event Broker)

- **Scenario:** High‑velocity ingest from IoT fleets/telemetry/logs needs real‑time persistence plus historical analysis; traditional Kafka retention is expensive at scale.
- **Topology & flow:** Variant A (edge) or Variant B (Azure). Producers write to VAST; consumers (Spark/Azure Stream Analytics) read from VAST.
- **VAST + Azure integration:** Using the VAST Event Broker, producers write to VAST using Kafka protocols; VAST persists streams on flash (tiered to Azure Blob Storage) for “infinite retention.” Downstream Azure services can query historical data directly via S3/Parquet patterns without rehydration steps.
- **Associated Microsoft 1P services (typical):**
  - **Azure IoT Hub / Azure Event Hubs:** common 1P ingest front doors; can bridge into VAST for retention/analytics.
  - **Azure Functions / Azure Logic Apps:** glue for fan-out, transforms, enrichment, and workflow triggers.
  - **Azure Data Explorer (Kusto) / Azure Synapse / Microsoft Fabric:** analytics destinations; VAST can be the lake substrate via S3/Parquet patterns.
  - **Azure Event Grid (optional):** event-driven triggers for “new data available” patterns.
- **Typical Azure 1P deployment pattern (baseline):**
  - Ingest lands in IoT Hub/Event Hubs; streaming transforms run in Stream Analytics/Functions; raw and curated data lands in Blob/ADLS.
  - “Fast query” is handled by Data Explorer; “lake analytics” is handled by Synapse/Fabric over curated parquet/delta.
  - Governance and monitoring use Azure-native logging/metrics and RBAC.
- **Typical open‑source deployment pattern (baseline):**
  - Ingestion uses **Kafka** (often on Kubernetes); stream processing uses **Flink**, **Spark Structured Streaming**, or **Kafka Streams**.
  - Long-term storage uses open table formats (**Iceberg/Delta**) over S3-compatible endpoints; search uses **OpenSearch**; metrics use **Prometheus/Grafana**.
  - Orchestration uses **Airflow** or **Argo**.
- **Where VAST fits (in both patterns):**
  - VAST can be the high-throughput durable landing zone (Kafka via Event Broker) with tiering to Blob for long-term retention.
  - VAST S3 endpoints and file protocols provide a performant lake surface for downstream analytics (1P or OSS compute).
  - VAST reduces Kafka retention cost and keeps historical replay/query viable without constant rehydration.

### W4: Spark & Databricks Analytics (VAST DataBase)

- **Scenario:** Azure Databricks/Spark teams hit I/O bottlenecks during shuffle phases and high‑concurrency queries against standard object stores.
- **Topology & flow:** Variant B (Azure). Databricks clusters in the same VNet interact with VAST.
- **VAST + Azure integration:** VAST DataBase can push down predicates (filters/projections) to the storage layer so only relevant results traverse the network, enabling stateless/lean compute that scales independently of storage performance.
- **Associated Microsoft 1P services (typical):**
  - **Azure Synapse Analytics (Spark + SQL):** 1P analytics plane; private networking patterns must be validated to reach VAST endpoints.
  - **Microsoft Fabric (Spark / lakehouse):** 1P lakehouse plane; shortcut/private connectivity constraints must be validated.
  - **Microsoft Entra ID:** identity plane for job execution and data access.
  - **Azure Private Link / VNet injection:** connectivity patterns for managed compute to reach private storage endpoints.
- **Typical Azure 1P deployment pattern (baseline):**
  - Lakehouse analytics runs in Synapse/Fabric with Blob/ADLS as the default storage substrate; curated data is stored as Parquet/Delta.
  - Private access relies on managed private endpoints and strict DNS/routing; orchestration uses platform-native pipelines where available.
  - Governance and lineage flow through Azure-native catalogs/logs.
- **Typical open‑source deployment pattern (baseline):**
  - Compute is **Spark on Kubernetes** (or standalone) with query engines like **Trino/Presto**; orchestration via **Airflow/Dagster**.
  - Table formats use **Iceberg/Delta/Hudi**; catalogs use **Hive Metastore/Nessie**; BI uses **Superset**.
  - Lineage and metadata (if needed) use **DataHub/OpenMetadata**.
- **Where VAST fits (in both patterns):**
  - VAST supplies high-throughput storage for shuffle-heavy and high-concurrency workloads via S3 and/or NFS.
  - DataBase pushdown reduces network amplification by moving filters/projections closer to storage (valuable for wide scans).
  - In 1P patterns, VAST becomes a performance tier backing lakehouse compute (subject to networking constraints); in OSS patterns, VAST can be the primary S3-compatible lake.

### W5: Hybrid Cloud Tiering (On-Prem Flash to Azure Blob Storage)

- **Scenario:** Flash performance is needed for recent/hot data, but cloud economics are needed for the cold tail (PACS, media archives, backups).
- **Topology & flow:** Variant A (on‑prem) tiers to Azure Blob Storage (Cool/Cold).
- **VAST + Azure integration:** Remote sites ingest at flash speed on small VAST footprints and tier to a central Azure Blob Storage lake for low‑cost durability. In a disaster, a new VAST instance can spin up in Azure (or a secondary site) and resume operations by reading metadata from Azure Blob Storage and hydrating only on demand.
- **Associated Microsoft 1P services (typical):**
  - **Azure Blob Storage (Cool/Cold/Archive):** economical durability tier and BCDR anchor.
  - **Azure ExpressRoute (or VPN Gateway):** private hybrid connectivity for predictable tiering.
  - **Azure Key Vault (optional):** CMK/HSM patterns for regulated deployments (Walk/Run alignment).
  - **Azure Data Box (optional):** bulk seeding into Blob for large cold estates.
- **Typical Azure 1P deployment pattern (baseline):**
  - Cold tier is Blob with lifecycle policies; bulk seed uses Data Box; steady-state tiering runs over ExpressRoute with documented operational windows and error budgets.
  - Restore/DR assumes “rehydrate from Blob” plus a tested runbook; audit and key management anchor on Key Vault for regulated environments.
- **Typical open‑source deployment pattern (baseline):**
  - Tiering uses **rclone/restic/borg/rsync** plus scheduled jobs; retention and verification rely on policy scripts and checksums.
  - Inventory/catalog (if needed) uses **Postgres + custom services**; monitoring uses **Prometheus/Grafana**.
- **Where VAST fits (in both patterns):**
  - VAST is the hot ingest/performance tier while Blob supplies durable, economical cold storage.
  - VAST tiering/sync can replace brittle scripts and make “hydrate on demand” recovery repeatable.
  - Blob API compatibility improves interoperability with enterprise tooling for tiering and restore workflows.

### W6: Ecosystem Access (Azure PaaS Integration)

- **Scenario:** Data on VAST must trigger Azure Functions/Event Grid, or be accessible to Azure 1P services (e.g., AI Foundry) without heavy data movement.
- **Topology & flow:** Variant B (Azure) connected to Azure PaaS via “Tuscany” patterns, VNet injection, and/or Private Link.
- **VAST + Azure integration:**
  - **Tuscany (migration‑on‑read proxy pattern):** enable on‑read federation where Azure services interact with VAST data “as if” it were native Blob.
  - **Eventing:** integrate with Azure Event Grid so “file landed” can trigger Azure Functions for tokenization, embedding, or indexing.
  - **Fabric:** expose VAST data to Microsoft Fabric via S3‑compatible shortcuts for query‑in‑place.
- **Associated Microsoft 1P services (typical):**
  - **Azure AI Foundry:** orchestration apps and agent workflows that need governed, private access to large corpora (often via customer-VNet app tiers reaching VAST).
  - **Microsoft Fabric / OneLake:** shortcut-based query-in-place patterns; private access constraints often require a gateway or approved private endpoint patterns.
  - **Azure Synapse Analytics:** managed private endpoint patterns for analytics jobs to reach VAST privately.
  - **Azure AI Search:** indexing/retrieval; “native” Blob indexers are Azure-storage-centric, so integration often requires either a Blob façade or custom ingestion pipelines.
  - **Microsoft Purview:** governance/crawl/catalog; scanning patterns must be validated against VAST auth and endpoints.
  - **Azure Private Link / managed private endpoints:** the dominant “make it private” path for many managed services; approval workflows and DNS are often the blocker.
- **Typical Azure 1P deployment pattern (baseline):**
  - Data lands in Blob/ADLS and is consumed by managed services using first‑class connectors (Fabric, Synapse, AI Search indexers, Purview scans).
  - Eventing uses Event Grid and Functions; orchestration uses Azure-native pipelines; private access uses managed private endpoints where supported.
  - Identity uses Entra ID and managed identities end-to-end; governance uses Purview plus policy guardrails.
- **Typical open‑source deployment pattern (baseline):**
  - Orchestration uses **Airflow/Dagster**; retrieval/index uses **OpenSearch** plus open vector stores (**Milvus/Qdrant/Weaviate/pgvector**).
  - Catalog/governance uses **DataHub/OpenMetadata/Atlas**; eventing uses **Kafka**; serverless-like compute uses **Knative** or Kubernetes jobs.
  - Data access is S3 + Parquet/Delta/Iceberg, with private connectivity handled at the network layer (VNet, VPN/ER, service mesh).
- **Where VAST fits (in both patterns):**
  - VAST can host the canonical datasets while providing compatible access planes (S3 + Blob façade + NFS/SMB) for whichever ecosystem the customer uses.
  - “Migration-on-read” proxy patterns reduce forced copy‑into‑Blob for services that only speak Blob, while preserving governance strategy.
  - Eventing and indexing can be built either with Azure-native services or OSS stacks, with VAST as the shared storage substrate.

### W7: Cloud Native Applications (AKS & Microservices)

- **Scenario:** AKS workloads need high‑throughput Read‑Write‑Many (RWX) persistent storage; standard cloud file services often throttle.
- **Topology & flow:** Variant B (Azure) linked to AKS clusters in the customer VNet.
- **VAST + Azure integration:** VAST provides shared file performance to AKS via the CSI driver (and/or direct NFS), enabling many microservices to share a single high‑performance persistence layer.
- **Associated Microsoft 1P services (typical):**
  - **Azure Kubernetes Service (AKS):** primary compute/orchestration plane; storage integration via CSI + NFS/SMB patterns.
  - **Azure Private Link / Private Link Service:** private storage endpoint exposure and repeatable “platform” patterns across environments.
  - **Azure Monitor / Container Insights:** observability for pods plus storage KPIs (latency, throughput, saturation).
- **Typical Azure 1P deployment pattern (baseline):**
  - AKS uses Azure-native RWX options (Azure Files Premium or Azure NetApp Files) for shared volumes; ingress/egress uses Azure load balancing and managed identities.
  - Networking is private-first (private AKS, private endpoints) with platform monitoring in Azure Monitor.
  - Stateful workloads are scoped carefully to match the performance envelope of the managed storage choice.
- **Typical open‑source deployment pattern (baseline):**
  - Kubernetes uses **Rook/Ceph**, **Longhorn**, or **OpenEBS** for persistence; ingress is **NGINX**; service mesh via **Istio/Linkerd**.
  - Observability via **Prometheus/Grafana** and tracing via **OpenTelemetry**.
  - Storage and state are run by the platform team with explicit SLOs and runbooks.
- **Where VAST fits (in both patterns):**
  - VAST provides a high-performance RWX backend for AKS (CSI/NFS/SMB) when Azure-native file services become the bottleneck.
  - A single storage substrate can serve both containerized apps and adjacent analytics/AI workloads (reducing copy pipelines).
  - Private Link Service exposure enables repeatable, enterprise-grade “platform storage” patterns.

### W8: Cross‑Region Training & Global WAN

- **Scenario:** Multinational teams collaborate on shared datasets across US/EU/APAC without public-internet variability.
- **Topology & flow:** Variant B (multi‑region) connected via Azure Virtual WAN and VAST DataSpace.
- **VAST + Azure integration:** Combine VAST global namespace with Azure’s backbone to replicate deterministically; VAST similarity‑based global dedup ensures only unique bytes traverse the wire.
- **Associated Microsoft 1P services (typical):**
  - **Azure Virtual WAN:** managed hub-and-spoke/global routing for multi-region and multi-site connectivity.
  - **Azure ExpressRoute:** deterministic private connectivity into Azure hubs (from on‑prem/colo/partner locations).
  - **Azure Private DNS / DNS Private Resolver (optional):** cross-region name resolution for private endpoints/PLS.
  - **Azure Monitor / Log Analytics:** latency/throughput baselines and replication health telemetry.
- **Typical Azure 1P deployment pattern (baseline):**
  - Data is centralized in Blob with replication (ZRS/GRS as required) and accessed from multiple regions; compute is placed near data when possible.
  - Global private networking uses Virtual WAN + ExpressRoute; private DNS provides consistent resolution for private endpoints.
  - Cross-region performance is managed by partitioning datasets and minimizing cross-region read/write amplification.
- **Typical open‑source deployment pattern (baseline):**
  - Multi-site connectivity is built with **WireGuard/OpenVPN** overlays or BGP-based WAN; DNS uses **CoreDNS/Bind** patterns.
  - Object replication uses **MinIO** multi-site or application-level replication; file replication uses **rsync**-style tooling.
  - Monitoring and SLOs are enforced via Prometheus/Grafana and custom health checks.
- **Where VAST fits (in both patterns):**
  - VAST provides a global namespace with efficient replication (dedup-aware) so users access data “locally” while maintaining coherence.
  - Azure backbone connectivity (vWAN/ExpressRoute) becomes the predictable transport for replication paths.
  - VAST reduces the need to duplicate full datasets by moving only unique bytes and caching hot working sets.

### W9: Regulated AI & Enclaves (Sovereign & Hybrid)

- **Scenario:** Financial services/defense customers need sovereign controls: cloud agility without the provider accessing data or keys.
- **Topology & flow:** Variant B (isolated VNet) or Variant D (hybrid) with Customer‑Managed Keys (CMK).
- **VAST + Azure integration:** Deploy inside locked‑down VNets with strict private connectivity and customer‑held keys. The goal is a “logical air‑gap” posture that supports residency and audit requirements (ITAR/GDPR) while retaining cloud provisioning speed.
- **Associated Microsoft 1P services (typical):**
  - **Azure Key Vault (Managed HSM/CMK):** customer-held key patterns for encryption and compliance; a Run requirement that influences Crawl/Walk choices.
  - **Microsoft Entra ID:** identity plane with conditional access and least-privilege service principals.
  - **Azure Private Link / Private Endpoints:** private-only access model; reduces exfiltration risk and supports “no public endpoint” policies.
  - **Azure Policy + Defender for Cloud (optional):** posture management, guardrails, and compliance evidence.
- **Typical Azure 1P deployment pattern (baseline):**
  - Workloads run in isolated VNets with private-only connectivity; storage and control planes are accessed via private endpoints and audited centrally.
  - Encryption uses Key Vault/Managed HSM (CMK), and governance uses Azure Policy/Defender for continuous compliance evidence.
  - Where required, compute uses Confidential VMs and restricted egress patterns; operations use strict RBAC and logging.
- **Typical open‑source deployment pattern (baseline):**
  - Identity and secrets use **HashiCorp Vault** and **OPA/Gatekeeper** for policy; network segmentation uses service mesh controls and firewalling.
  - Observability uses **OpenTelemetry** and self-hosted logging stacks; compliance evidence is assembled via automated controls + audits.
  - Data plane services are deployed in private enclaves with explicit “no internet” assumptions.
- **Where VAST fits (in both patterns):**
  - VAST provides high-performance storage inside the enclave while supporting strict private networking and auditable access.
  - CMK and identity integration choices should be made early because they constrain how the Blob façade and replication are implemented.
  - A consistent storage substrate across on‑prem and Azure enclaves reduces migration risk for regulated customers.

### W10: Migration & Modernization

- **Scenario:** Exiting legacy on‑prem NAS (NetApp/Isilon) is blocked because applications rely on protocol behaviors cloud‑native storage doesn’t fully emulate.
- **Topology & flow:** Source (legacy) → Target (Variant B).
- **VAST + Azure integration:** VAST provides protocol parity (NFSv3/v4, SMB, S3) to enable “zero‑refactor” lift‑and‑shift. Customers can modernize incrementally by leveraging VAST multi‑protocol access.
- **Associated Microsoft 1P services (typical):**
  - **Azure Migrate:** discovery/assessment tooling and a migration program wrapper.
  - **Azure Storage Mover / Azure Data Box:** large-scale transfer tooling (constraints: Storage Mover targets Azure-native endpoints today; Data Box seeds into Azure storage).
  - **Azure Virtual Machines / AKS:** target compute planes that benefit from protocol parity without refactoring.
  - **Azure Private Link + ExpressRoute:** private connectivity foundations for repeatable enterprise migrations.
- **Typical Azure 1P deployment pattern (baseline):**
  - Assess and plan with Azure Migrate; seed data with Data Box where needed; ongoing transfer uses AzCopy/ADF into Azure-native storage targets.
  - Modernize apps into Azure VMs/AKS; storage defaults to Azure Files/ANF/Blob depending on protocol needs, with private endpoints and governance guardrails.
  - Migration waves are managed through repeatable landing zones and standardized networking patterns.
- **Typical open‑source deployment pattern (baseline):**
  - Bulk copy and sync uses **rsync/robocopy/rclone** and checksum validation; orchestration via scripts or **Ansible/Terraform**.
  - “Lift and shift” targets are Kubernetes or VMs with open-source ingress/service mesh; CI/CD uses standard GitOps patterns.
  - Data validation and cutover are implemented with application-level smoke tests and inventory comparisons.
- **Where VAST fits (in both patterns):**
  - VAST is a migration target that preserves protocol behaviors (NFS/SMB/S3) so applications can move without refactoring.
  - Once workloads run in Azure, VAST can remain the performance tier while Blob becomes the durable capacity tier as customers modernize incrementally.
  - VAST reduces the number of “one-way” migrations by enabling hybrid coexistence during long modernization programs.

## Workload Alignment Matrix

|Workload|Recommended VAST Variant|Integration Pattern|Primary Microsoft 1P services|Key Value Driver|
|---|---|---|---|---|
|W1: Burst Compute|Variant D (Hybrid)|Global namespace cache|VMs/VMSS, ExpressRoute, Private Link|Elasticity without egress shock|
|W2: GPU Adjacent|Variant A|Blob API façade + tiering/sync|Blob Storage, Entra ID, Private Link, Event Grid|GPU saturation + governed durability|
|W3: Streaming|Variant A/B|Kafka (Event Broker) + tiering|IoT Hub/Event Hubs, Functions, Synapse/Fabric, Data Explorer|Retention + real-time/historical query|
|W4: Spark analytics|Variant B|DataBase (pushdown) + S3/NFS|Fabric, Synapse, Entra ID, Private Link|High concurrency analytics performance|
|W5: Hybrid tiering|Variant A|Tiering/offload to Blob|Blob Storage, ExpressRoute, Key Vault, Data Box|Edge ingest + BCDR economics|
|W6: Ecosystem (PaaS)|Variant B|Migration-on-read + eventing|AI Foundry, Fabric, Synapse, AI Search, Purview|Azure-native ecosystem access|
|W7: Cloud native|Variant B|CSI + NFS/SMB|AKS, Private Link, Azure Monitor|True RWX performance for apps|
|W8: Global WAN|Variant B (Multi)|DataSpace + WAN replication|Virtual WAN, ExpressRoute, Private DNS, Azure Monitor|Deterministic global collaboration|
|W9: Regulated AI|Variant A/B|Private enclaves + CMK|Key Vault (CMK/HSM), Entra ID, Private Link, Policy|Sovereign control + compliance posture|
|W10: Migration|Variant B|Multiprotocol parity|Azure Migrate, Storage Mover/Data Box, Private Link, VMs/AKS|Zero-refactor modernization path|

## Open Items

Tracked in: [TODO](../TODO.md)
