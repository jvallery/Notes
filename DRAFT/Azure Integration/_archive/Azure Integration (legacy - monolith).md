# Executive Summary

The gravitational center of the AI ecosystem is tearing in two directions.

  

On one side, Data Gravity pulls everything toward the Azure "Hero Region." Enterprises and foundation model builders alike demand a single, durable source of truth for their multi-exabyte data estates. They require the rigorous governance, low-cost durability, and rich ecosystem integration (Microsoft Fabric, Synapse, Purview, AI Foundry) that only a centralized Azure Blob Data Lake can provide. This is the Governance Tier.

  

On the other side, Compute Gravity is fracturing outward. The sheer power density required for frontier model training and massive-scale inference cannot be served by a single region’s capacity. GPUs are landing wherever power, cooling, and silicon supply allow. This includes satellite Azure regions, neo-clouds, colo facilities, and on-premises AI factories. These data hungry compute clusters cannot tolerate the latency, egress costs, or throughput bottlenecks of fetching every byte over a WAN from a central lake. They demand a performance tier that is physically adjacent to the silicon.

  

The VAST + Azure integration resolves this tension by treating them not as competing storage silos, but as a unified data fabric.

  

In this architecture:

  

- Azure Blob Storage remains the immutable system of record and the capacity substrate. It anchors the namespace, enforces governance, and feeds the broad ecosystem of Azure native analytics services.
    

  

- VAST Data Platform serves as the decentralized, GPU-adjacent performance tier. It acts as a high-performance cache and global namespace that hydrates data from the central lake to the edge, saturates GPUs with local NVMe speed, and captures checkpoints instantly before syncing them back to the core.
    

  

The success of this partnership relies on transparent interoperability. By implementing an Azure Blob API facade on VAST, we allow customers to use standard Azure data movers (like AzCopy) to stage data to the edge without refactoring their toolchains. By integrating namespace federation, we ensure that data landed in the central lake becomes visible to the edge GPUs automatically, and value created at the edge flows back to the governance core. We stop asking customers to choose between the governance of the cloud and the performance of the edge.

## Productization Roadmap: Crawl, Walk, Run

To execute quickly without over-scoping, we propose a phased plan that evolves from compatibility → production hardening → a fully managed Azure-native SaaS offering. This approach ensures immediate customer value while building towards the ultimate product destination.

## Crawl: Unblock Adoption and Offload Capacity

Goal: Remove the primary adoption barrier by enabling data movement and offloading capacity using standard Azure tools.

  

Crawl delivers:

  

- A Blob API compatibility façade on VAST (a deliberate subset focused on data movers and client interoperability).
    
- The ability to offload/tier cold and durable artifacts to Azure Blob so VAST flash is reserved for the hot working set.
    
- A small number of reference architectures that can go live immediately (W2: Central Blob lake + GPU-adjacent VAST satellite; W5: On-prem VAST offload to Blob).
    

  

Outcome: Customers adopt VAST as a performance tier without refactoring pipelines, and Azure remains the governed center of gravity.

## Walk: Production Hardening and Scenario Expansion

Goal: Make deployments repeatable, secure, and enterprise-ready, expanding interoperability based on real-world adoption.

  

Walk delivers:

  

- Private connectivity and network patterns (Private Link Service, DNS, managed-VNet constraints playbooks, network throughput tuning).
    
- Expanded Blob API coverage driven by observed production scenarios rather than attempting full Blob emulation.
    
- Initial namespace/metadata/index integration patterns so edge-created value becomes discoverable and usable across Azure workflows (e.g., preliminary integration for W6 and W9).
    

  

Outcome: Fewer operational "hybrid taxes," more secure and repeatable deployments, and broader Azure service interoperability.

## Run: Azure-native SaaS Offering (Managed Performance Tier for Blob)

Goal: The productized destination: a fully managed service that customers consume like an Azure-native offering.

  

Run includes:

  

- Managed lifecycle: Provisioning, upgrades, scaling, patching, and support are handled as a service with clear SLOs.
    
- Azure-native control plane experience: Deploy and govern via Azure constructs (identity, policy, logging/monitoring, private networking), with consumption and procurement aligned to Azure buying motions.
    
- A unified fabric experience where data is accelerated near compute while governance, durability, and ecosystem access remain anchored in Azure Blob.
    

  

Outcome: Customers stop "building hybrid" and start consuming a managed, Azure-native performance tier that follows GPUs wherever they land.

  

# Crawl / Walk / Run Roadmap at a GlanceRun (SaaS) Requirements

|Phase|What we're proving|What we ship|What changes for customers|
|---|---|---|---|
|Crawl|Data plane works|Blob API façade (data-movement subset), server-side copy primitives, VAST↔Blob offload/tiering, 1–2 reference architectures|No refactors; use AzCopy/SDKs; keep Blob as system of record; reserve VAST flash for hot set|
|Walk|Ops + security are repeatable|Private connectivity patterns, managed-VNet playbooks, observability hooks, API expansion based on demand, initial metadata/index patterns|Lower hybrid tax; repeatable enterprise deployments; fewer manual sync workflows|
|Run|It's a product|Azure-native SaaS: managed lifecycle, buying/billing alignment, integrated governance/identity/networking/monitoring, "service-grade" experience|Customers consume a managed performance tier; no cluster ops; faster procurement, upgrades, and scale|

To ensure the "Run" phase is a legitimate product destination, the solution must meet these concrete, managed service requirements:

  

- Azure-native provisioning model: Resource lifecycle, private networking, and identity integration managed via Azure portal/APIs.
    
- Billing/procurement alignment: Consumption-based billing via Azure Marketplace/Private Offer.
    
- Managed operations: Automated upgrades, patching, scaling, and proactive incident response against defined SLOs.
    
- Security posture: Deep Entra ID integration, Customer-Managed Keys (CMK) via Key Vault, and comprehensive audit logs.
    
- Observability: Built-in integration with Azure Monitor / Log Analytics for a single-pane operational view.
    

  
  

## The "What": Solution Overview

We are delivering a unified data platform integration that connects Azure’s ecosystem centric data estate with VAST’s performance-centric compute fabric. 

TODO: Need to expand out all integration work including identity, encryption. Merge what/why narrative into sub-sections based on the proposed work.  

### The Blob API:

A lightweight, high-fidelity, Azure Blob REST endpoint on the VAST cluster. This is not a full Blob replacement, but a compatibility façade designed specifically for data movement and client interoperability. By supporting critical server-side copy primitives (PutBlobFromURL, PutBlockFromURL) and high-concurrency block operations, we ensure that standard enterprise tools like AzCopy work out of the box. Equally important, this compatibility enables the use of AI-centric client libraries favored by foundation model builders such as boostedblob (used by OpenAI). This ensures that both general-purpose IT workflows and specialized, high-throughput AI training pipelines can stage data to VAST and return checkpoints to Azure without refactoring code or installing custom drivers.

### Intelligent Tiering & Namespace Federation:

The solution establishes a federated global namespace where VAST acts as the high-performance caching and staging tier, while Azure Blob Storage serves as the low-cost, durable capacity tier.

- Hot Working Set: Resides on VAST flash, adjacent to GPUs for sub-millisecond and high throughput training and inference access.
    
- Cold Data: Is transparently tiered to Azure Blob using VAST native opaque formats (for maximum data reduction) or transparent open standard formats (for ecosystem accessibility), enabling infinite scale without the flash price premium.
    

### Hardware Independence

The integration provides a consistent software experience across three distinct hardware substrates, allowing customers to place performance exactly where their compute lives:

  

- Edge/Satellite/Neo-Cloud: VAST on ODM hardware for maximum density adjacent to distributed GPU clusters.
    
- Central Azure Region: VAST on Azure L-series VMs (Lasv4, Lasv5) for elastic, cloud-native deployments within the Azure vNet.
    
- Future/Managed: Roadmap support for VAST on Azure provided bare metal storage infrastructure for high-performance managed service scenarios.
    

  
  

## The "Why": Strategic Value & Timing

  

The urgency for this integration is driven by four converging market forces that make the status quo (siloed storage or pure cloud-native storage) untenable for frontier AI.

  

#### The Distributed GPU Reality

We are entering an era where power availability, not just silicon availability, dictates where training happens. Exabyte-scale data lakes are anchored in major Azure "Hero Regions" (e.g., East US), but GW-scale compute clusters are being forced into satellite regions, neo-clouds, and retrofitted industrial sites. In these power-starved environments, density is currency. Deploying inefficient HDD-based storage or standard Azure Blob infrastructure at the edge incurs a prohibitive opportunity cost: every megawatt or rack unit burned on low-performance storage is compute capacity stolen from the training cluster. VAST’s architecture maximizes the GPU-to-Storage density ratio, ensuring that scarce power and space are dedicated to the highest-value GPU assets, while the bulk data lake remains centralized. You cannot move the lake to the edge, and you cannot starve the edge waiting for the lake; VAST + Azure decouples storage capacity from compute locality without sacrificing the power envelope.

  

#### Supply Chain & Media Volatility

The flash memory market is entering a cycle of constrained supply and rising prices. An "all-flash everything" strategy for exabyte-scale data is economically dangerous. By integrating deeply with Azure Blob, we allow customers to lean on HDD based object storage for the massive tail of their dataset, reserving high-premium VAST flash strictly for the GPU-adjacent working set. This provides a hedge against component volatility.

#### Ecosystem Gravity (AI Foundry, Fabric & OneLake)

Data has gravity, but ecosystems have stronger gravity. Microsoft Fabric, Synapse, and AI Foundry require data to be accessible via Azure-native protocols and control planes. If VAST remains a "dark silo" outside this ecosystem, it loses relevance. By building transparent tiering and connectivity shortcuts that the Azure ecosystem can consume, we ensure VAST data remains a first-class citizen.

  

#### Tooling Inertia 

Azure-native data engineering teams have spent considerable effort standardizing on Azure Blob Storage and REST API based data pipelines. They will not adopt a high-performance storage tier if it requires rewriting their data movement and ingestion logic to use proprietary clients or POSIX-only shims. We propose building a Blob API facade to remove the single biggest friction point in hybrid AI adoption by frontier model builders (E.g., OpenAI and MicrosoftAI).

  

## Value Proposition

  

This partnership and integration resolve the "Gravity vs. Performance" tension by playing to the distinct strengths of each platform.

  

### Why Microsoft Wins

- Governance Gravity: Azure reinforces its position as the central nervous system for enterprise data. Even decentralized edge workloads remain tethered to Azure’s governance model (Entra ID, Purview).
    
- Ecosystem Capture: High-performance AI workloads are pulled into the Azure orbit. Data staged on VAST for training inevitably flows back to Azure Blob for lifecycle management and integration with Azure AI Foundry, Databricks, Fabric, and Synapse.
    
- Unblocking Adoption: By solving the high-performance storage gap, Microsoft removes a key barrier for demanding HPC/AI customers who might otherwise look to specialized niche clouds or bare-metal competitors.
    

  

### Why VAST Wins

- Enterprise Scale: Partnering with Azure instantly scales VAST’s reach to the Global 2000, positioning it as a critical component of the modern cloud-native AI stack rather than just a storage appliance.
    
- Commercial Velocity: Leveraging Azure as the capacity tier simplifies the sales motion. Customers don't need to over-provision expensive flash for cold data; VAST can sell a leaner, high-velocity performance layer that "bursts" capacity to the cloud.
    
- Validation: Deep integration validates VAST’s architecture as a standard for enterprise AI, bridging the gap between on-prem performance and cloud scalability.
    

  

# Target Scenarios and Workloads

This section turns strategy into deployable architectural patterns. It maps business scenarios to concrete hardware and integration mechanics.

  

## VAST on Azure Deployment Scenarios

- Variant A (ODM / Edge): VAST hardware deployed adjacent to GPUs/CPUs in customer datacenters, colocation facilities, or "neo-clouds." Best for maximum density and performance.
    
- Variant B (Azure IaaS): VAST software running on storage-optimized Azure VMs (Lasv4/Laosv4) with local NVMe. Best for elasticity and cloud-native integration.
    
- Variant C (Azure Bare Metal): Future/Roadmap. VAST on Azure-provided bare metal infrastructure for high-density managed service scenarios.
    
- Variant D (Hybrid): A unified namespace spanning a mix of on-prem ODM clusters and Azure VM clusters.
    

  

## VAST + Azure Workloads

  

TODO: Cross reference between “workloads” and “Azure services” mapping. Tie both sections back to what work needs to be done to fully enable. Rethink structure on how to tell the PaaS + IaaS story better together 

### W1: On-Prem VAST + Burst Compute on Azure

- Scenario
    

A customer holds massive datasets on premises (often due to gravity or compliance) but needs ephemeral Azure CPU/GPU capacity to meet critical processing deadlines. They cannot afford to permanently migrate petabytes or refactor POSIX applications.

  

- Topology & Flow
    

On-prem VAST ODM acts as the data origin, a temporary Variant B cluster in Azure acts as a caching satellite. Connected via ExpressRoute.

  

- VAST + Azure Integration
    

This architecture breaks data gravity. Customers gain infinite compute elasticity without the egress tax and time penalty of moving cold data. The VAST Global Namespace presents a unified view to cloud compute. The satellite in Azure intelligently caches only the "hot" working set, ensuring high-performance local access for Azure GPU/CPUs while masking WAN latency.

  
  

### W2: Central Blob Lake + GPU-Adjacent VAST Satellites

- Scenario
    

A model builder maintains its "System of Record" in a central Azure "Hero Region" (e.g., East US) for governance, compliance, and massive capacity. However, due to power or silicon constraints, their high-performance training clusters (e.g., thousands of GB200s) are deployed in a "Neo-Cloud" (e.g., Nebius, CoreWeave) or a dedicated colo facility. The latency of fetching training shards over the WAN kills GPU utilization, and the bandwidth required to push multi-terabyte checkpoints back to Azure stalls training loops.

  

- Topology & Flow
    

Azure Blob Storage (Central Region) for durability. Variant A (ODM) deployed inside the Neo-Cloud datacenter, directly adjacent to the GPU fabrics. Training data is hydrated from Azure Blob to VAST; Checkpoints flow VAST to Azure Blob.

  

- VAST + Azure Integration
    

Using the Blob API Façade, data engineering teams can use standard AzCopy, VAST SyncEngine, or Azure Storage Mover jobs to "hydrate" the VAST cluster from the central lake. To the movers, the VAST cluster appears simply as another Azure region, allowing pipelines to remain unchanged while moving data into the high-performance local tier.  
  

The training cluster writes checkpoints to the local VAST ODM system at full NVMe speeds (often via GPUDirect Storage over NFS), ensuring the GPUs return to training immediately. VAST then asynchronously syncs these checkpoints back to the central Azure Blob store for long-term durability and model lineage, effectively decoupling the "save" time from the "upload" time.

### W3: Streaming Data Pipelines (Kafka & Event Broker)

- Scenario
    

High velocity ingest from IoT fleets, telemetry, or logs requires real-time persistence and historical analysis. Traditional Kafka architectures struggle with retention limits and storage costs at scale.

  

- Topology & Flow
    

Variant A (Edge) or Variant B (Azure). Producers write to VAST; Consumers (Spark/Azure Stream Analytics) read from VAST.

  

- VAST + Azure Integration
    

Leveraging the VAST Event Broker, producers write directly to VAST using Kafka protocols. VAST persists the stream indefinitely on flash (tiered to Blob), eliminating expensive ephemeral broker storage. Downstream Azure services (Stream Analytics, Data Explorer) can query this historical data directly via S3/Parquet protocols, bypassing rehydration steps.

### W4: Spark & Databricks Analytics (VAST Database)

- Scenario
    

Data Engineering teams using Azure Databricks or Spark face I/O bottlenecks during shuffle phases and high-concurrency queries against standard object stores.

  

- Topology & Flow
    

Variant B (Azure). Databricks clusters in the same VNet interact with VAST.

  

- VAST + Azure Integration
    

The VAST Database pushes query predicates (filters, projections) down to the storage layer. Instead of pulling massive tables over the network, VAST filters data in situ, sending only relevant results. This allows Databricks clusters to run stateless and lean, scaling compute independently of storage performance.

  

### W5: Hybrid Cloud Tiering (On-Prem Flash to Azure Blob)

- Scenario
    

Customers love flash performance but need cloud economics for cold data. This is critical for PACS (Medical Imaging), Media Archives, and Backup Targets where recent data is hot but historical data is vast.

  

- Topology & Flow
    

 Variant A (On-Prem) tiers to Azure Blob (Cool/Cold).

  

- VAST + Azure Integration
    

Remote sites (factories, sequencers) ingest data at line-rate flash speeds on small VAST footprints, immediately tiering to the central Azure Blob lake. Azure Blob acts as the low cost, immutable, air-gapped "gold copy." In a disaster, a new VAST instance can spin up in Azure (or secondary site) and instantly resume operations by reading metadata from Blob, hydrating data only on demand.

  

### W6: Ecosystem Access (PaaS Integration)

- Scenario
    

Data on VAST needs to trigger workflows in Azure Functions, feed Event Grid topics, or be accessible to other Azure 1P services like AI Foundry without heavy data movement. See complete set of integrations in the “Azure Native Services Integration” section.

  

- Topology & Flow
    

Variant B (Azure) connected to Azure PaaS via Tuscany, VNet Injection, or Private Link.

  

- VAST + Azure Integrations
    

- "Tuscany": Leveraging on-read patterns to enable seamless federation where Azure PaaS services interact with VAST data as if it were native Blob.
    
- Integration with Azure Event Grid turns storage into a trigger. A file upload to VAST can instantly fire an Azure Function to tokenize data or update a vector index.
    
- VAST data is exposed to Microsoft Fabric via S3-compatible shortcuts, allowing the ecosystem to query high-performance data in place.
    

  
  

### W7: Cloud Native Applications (AKS & Microservices)

- Scenario
    

Complex containerized applications on AKS require high-throughput, Read-Write-Many (RWX) persistent storage that standard cloud file services often throttle.

  

- Topology & Flow
    

Variant B (Azure) linked to AKS Clusters.

  

- VAST + Azure Integration
    

Unlike Azure Files or BlobFuse, VAST provides "SAN-grade" shared file performance to AKS via the CSI Driver. It allows diverse microservices (databases, queues, web servers) to share a single, high-performance persistence layer.

  

### W8: Cross-Region Training & Global WAN

- Scenario
    

Multinational research teams need to collaborate on shared datasets across US, Europe, and Asia regions without the latency or unreliability of the public internet.

- Topology & Flow
    

Variant B (Multi-Region) connected via Azure Virtual WAN and VAST DataSpaces.

  

- VAST + Azure Integration
    

Coupling VAST's Global Namespace with Azure’s Global WAN creates a deterministic, private backbone for replication. VAST’s similarity-based global deduplication ensures only unique bytes traverse the wire, while Azure’s backbone provides stability unmatched by the public internet.

### W9: Regulated AI & Enclaves (Sovereign & Hybrid)

- Scenario 
    

FSI or Defense customers require "Sovereign Cloud" security using cloud agility but ensuring the provider (Microsoft) cannot access sensitive data or keys.

  

- Topology & Flow
    

Variant B (Isolated VNet), Variant D (Hybrid) with Customer-Managed Keys (CMK).

  

- VAST + Azure Integration
    

VAST enables a logical airgap. By deploying inside a locked-down VNet with strict Private Link controls and customer-held encryption keys, the data remains opaque to the underlying infrastructure. This architecture satisfies strict residency and audit requirements (ITAR, GDPR) while retaining cloud provisioning speed.

  

### W10: Migration & Modernization

- Scenario
    

Exiting legacy on-prem NAS (NetApp/Isilon) to Azure is blocked because applications rely on specific protocol behaviors cloud-native storage doesn't fully emulate.

  

- Topology & Flow
    

Source (Legacy) to Target (Variant B).

  

- VAST + Azure Integration
    

VAST provides absolute protocol parity (NFSv3/v4, SMB, S3) with enterprise appliances. This enables a "zero-refactor" lift-and-shift. Once in Azure, customers can incrementally modernize applications to cloud-native patterns (like object storage) using VAST’s multi-protocol access to bridge the gap.

  

## Workload Alignment Matrix

TODO: Add in the equiv PaaS service to the matrix for each workload. Update linking to documentation. 

  

|   |   |   |   |
|---|---|---|---|
|Workload|Recommended VAST Variant|Integration Pattern|Key Value Driver|
|W1: Burst Compute|Variant D (Hybrid)|Global Namespace (Cache)|Elasticity without Egress Shock|
|W2: GPU Adjacent|Variant A|BlobAPI; Tiering (Cache)|Performance and efficiency|
|W3: Streaming|Variant A/B|VAST Event Broker|Infinite Retention & Real-time Query|
|W4: Spark/Databricks|Variant B|VAST Database (Pushdown)|Zero-Shuffle Analytics|
|W5: Hybrid Tiering|Variant A|Transparent/Opaque Tiering|Edge Ingest & BCDR|
|W6: Ecosystem (PaaS)|Variant B|Tuscany / Event Grid|Seamless "Migration-on-Read"|
|W7: Cloud Native (AKS)|Variant B|CSI Driver / NFS|True RWX Performance|
|W8: Global Namespace|Variant B (Multi)|Azure Virtual WAN|Dedupe-Optimized Global Backbone|
|W9: Regulated AI|Variant A/B|Private Link / Enclave|Sovereign Data Control|
|W10: Migration|Variant B|Multiprotocol (NFS/SMB)|Risk-Free Cloud Entry|

  
  

# Azure Native Services Integration

|   |   |   |   |   |
|---|---|---|---|---|
|Azure Service|Primary scenarios and integration value|Network Connectivity||Blockers / gaps|
|Azure AI Foundry|- RAG grounding + retrieval over large private corpora; “knowledge base” for agents<br>    <br>- App-tier calls VAST: InsightEngine/DataBase (vector + metadata) over S3/HTTP; DataStore for source docs<br>    <br>- Zero-copy RAG (query data where it lives); lower duplication vs copying into separate vector stores|Azure AI Foundry itself doesn’t mount storage; your orchestration app runs on AKS/App Service/VMs in Customer VNet and reaches VAST via VNet peering/Private Link Service (PLS)|🟡|Not a direct storage integration requires reference architecture + app pattern; optional need for VAST-managed auth alignment (VAST)|
|Azure AI Foundry (Hub/Project control plane)|- Secure Foundry hub/project networking (private access) while datasets live on VAST<br>    <br>- Compute-plane mounts: DataStore (NFS) or S3; AI OS features (DataEngine pipelines) for agentic workflows<br>    <br>- High-performance dataset access for training/agent pipelines without rewriting storage layer|Foundry supports private endpoints for hubs/projects; compute used by projects must reach VAST via Customer VNet injection/peering or PLS|🟡|Control-plane defaults to Azure Storage account selection for “first party” experiences; VAST can be used via compute-plane mounts but not always as a first-class “project default datastore” (Microsoft control-plane + VAST docs/UX)  <br>  <br>https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/configure-private-link?view=foundry-classic|
|Azure Machine Learning (AML)|- Training on massive datasets; staging to GPU-adjacent VAST; hybrid data access<br>    <br>- Direct mount path: DataStore (NFS) and/or S3 endpoint; DataSpace for hybrid/global namespace<br>    <br>- GPU saturation + faster epochs/checkpoints vs blobfuse/object-store metadata throttling|AML compute clusters can be VNet-injected; mount VAST over private IP (peering/ExpressRoute/PLS). AML “Datastores” are Azure-storage-centric for managed UX|🟢|AML managed “Datastore” UX assumes Azure Storage accounts; for best perf, bypass datastore and mount directly (Solution architecture + customer ops)<br><br>  <br><br>https://learn.microsoft.com/en-us/azure/machine-learning/concept-data?view=azureml-api-2|
|Azure AI Search|- Index + retrieval over documents living on VAST; hybrid indexing where “gold source” stays on VAST<br>    <br>- S3 (preferred) for custom ingestion pipelines; Blob API façade (roadmap/MVP) if trying to use Blob indexer semantics<br>    <br>- Keep source data on VAST; reduce copies; accelerate refresh cycles|AI Search outbound to private resources often uses shared private link patterns; VAST reachable via PLS + approval workflow OR ingest via pipeline that runs in Customer VNet|🟡|Blob Indexers assume Azure Blob semantics; to integrate “natively” needs either (a) VAST Blob API compatibility or (b) custom indexer pipeline (VAST + customer). Private connectivity model must be validated per tenant (Customer + VAST)<br><br>  <br><br>https://docs.azure.cn/en-us/search/search-indexer-howto-access-private|
|Microsoft Fabric / OneLake (Shortcuts)|- Virtualize VAST datasets into Fabric lakehouses/notebooks without ETL<br>    <br>- S3-compatible shortcut to VAST S3 endpoint; optionally DataEngine pipelines feeding curated parquet/delta<br>    <br>- “Virtual lakehouse” over VAST: query-in-place; avoid copy-to-OneLake tax; leverage Fabric compute on top of VAST data|Managed VNet: OneLake shortcuts to external S3-compatible endpoints typically require public reachability OR On-Prem Data Gateway for private network paths|🟡|S3-compatible shortcut uses key/secret-style credentials; private connectivity usually requires gateway; Fabric managed private endpoints do NOT support FQDN endpoints/PLS (Microsoft platform constraint + VAST guidance)<br><br>  <br><br>https://learn.microsoft.com/en-us/fabric/onelake/create-s3-compatible-shortcut|
|Microsoft Fabric (On-Premises / private shortcut bridging)|- Access VAST in private VNets or on-prem via gateway<br>    <br>- S3-compatible shortcut via On-Prem Data Gateway to VAST S3 VIP  <br>      <br>    <br>- Unlock private datasets (no public endpoint); faster adoption in regulated environments|Gateway machine must have network path to VAST endpoint; Fabric uses gateway as bridge|🟡|Gateway is a bottleneck & operational burden; HA/scale patterns required (Customer + Microsoft docs; VAST sizing guidance)<br><br>  <br><br>https://learn.microsoft.com/en-us/fabric/onelake/create-on-premises-shortcut|
|Azure Databricks Classic (VNet injected)|- ETL + ML engineering; spark workloads over high-performance data plane<br>    <br>- VAST DataBase (spark connector) and/or DataStore via NFS/S3<br>    <br>- High throughput + predicate pushdown; reduce shuffle; one shared dataset for spark + non-spark code|VNet-injected classic compute reaches VAST over peering/ExpressRoute; no managed VNet wall here|🟢|Requires deploying/validating VAST spark connector and tuning; otherwise, straightforward (VAST)|
|Azure Databricks Serverless (SQL/Model Serving)|- Serverless SQL/serving accessing VAST datasets securely<br>    <br>- S3 endpoint (and/or future Blob API)<br>    <br>- Stay relevant as Databricks shifts to serverless; keep storage layer consistent across classic + serverless|Serverless compute plane uses Network Connectivity Configurations (NCC) + Private Link to reach customer resources via Azure load balancer / private connectivity|🟡|Validate whether serverless Private Link can target partner PLS endpoints in your environment; expect extra networking approval/ops (Customer + Databricks + VAST)<br><br>  <br><br>https://learn.microsoft.com/en-us/azure/databricks/security/network/serverless-network-security/serverless-private-link|
|Azure Synapse Analytics (Workspace + Spark)|- External tables / spark reads from VAST; staging datasets for SQL/Spark<br>    <br>- VAST S3 (external table / spark) and/or NFS for spark pools (where feasible)<br>    <br>- Access high-performance datasets without copying to ADLS; accelerate load + query for big scans|Managed VNet + Synapse Managed Private Endpoints to reach Azure resources and Azure-hosted partner services; requires PE approval workflow|🟡|Managed Private Endpoint approval must be operationalized; Synapse UX often assumes ADLS in browse experiences (Customer ops + VAST PLS approval workflow)  <br>  <br>https://learn.microsoft.com/en-us/azure/synapse-analytics/security/synapse-workspace-managed-private-endpoints|
|Azure Kubernetes Service (AKS)|- Inference farms; feature/model serving; RWX shared storage for thousands of pods<br>    <br>- CSI driver (NFS) and/or direct NFS mounts; AI OS for pipelines (DataEngine)<br>    <br>- “True RWX performance” + consistent semantics; avoid Azure Files throttling for metadata-heavy workloads|Customer VNet: nodes connect to VAST via peering/ExpressRoute/PLS; private DNS required for clean endpointing|🟢|Validate CSI auth story: Azure Workload Identity / federated tokens vs static secrets; define best practice (VAST + customer platform team)  <br>  <br>https://kubernetes.io/docs/concepts/storage/persistent-volumes/|
|Azure Batch|- Burst rendering, genomics, Monte Carlo; thousands of cores need shared dataset<br>    <br>- NFS/SMB mounts to VAST DataStore; DataSpace for hybrid datasets<br>    <br>- Prevent I/O starvation at job start; faster checkpoints & job completion|Customer VNet pools mount VAST on boot; peering/ExpressRoute/PLS|🟢|Mount automation & image hardening are customer tasks; otherwise, straightforward (Customer)|
|Azure Data Factory (ADF)|- Orchestrate copy/transform pipelines to/from VAST and Azure storage<br>    <br>- S3 connector to VAST<br>    <br>- ADF remains orchestration hub while VAST is performance tier; reduce custom scripts|Managed VNet + managed private endpoints for Azure PaaS; for private access to VAST, typically use Self‑Hosted Integration Runtime (SHIR) in customer network|🟡|Managed VNet has limited ability to reach arbitrary endpoints; SHIR introduces VM ops tax; “first-class” VAST would require deeper integration (Customer + Microsoft + VAST)  <br>  <br>https://learn.microsoft.com/en-us/azure/data-factory/managed-virtual-network-private-endpoint|
|Azure Storage Mover|- Migrate SMB/NFS file shares into Azure storage (Blob/Files)<br>    <br>- Typically uses VAST as SOURCE (NFS/SMB) when migrating into Azure first-party storage<br>    <br>- High-speed lift-out of legacy NAS data where VAST is source of truth|Agent-based; runs where data is; targets are Azure storage services|🟡|Storage Mover targets are Azure first-party storage; it won’t target VAST as a destination (Microsoft product constraint). Use VAST SyncEngine/AzCopy/Rclone for VAST-target migrations (Customer + VAST). Storage Mover built on AzCopy so Microsoft could enable the scenario once VAST has BlobAPI.  <br>  <br>https://learn.microsoft.com/en-us/azure/storage-mover/endpoint-manage|
|Azure Data Box|- Offline ingest / bulk import at PiB scale for Azure storage<br>    <br>- Use as staging into Blob/ADLS; then hydrate to VAST (AzCopy/Put-from-URL/SyncEngine)<br>    <br>- De-risk initial bulk seeding; then VAST accelerates hot set|Physical appliance workflow into Azure storage; subsequent private transfer to VAST|🟡|Not a direct Data Box to VAST target; requires post-seed pipeline (Customer + VAST)|
|Azure Event Grid|- Event-driven pipelines: “file landed” triggers downstream processing<br>    <br>- DataEngine emits events to Event Grid custom topic; or VAST publishes webhook-  <br>      <br>    <br>- Storage becomes a trigger; near-real-time pipelines without polling<br>    <br>- VAST EventBroker as target/consumer|Public or Private Endpoint for Event Grid resources; for private delivery patterns, design carefully around Event Grid limitations|🟡|VAST must implement Event Grid event schema + delivery guarantees; choose push vs alternative private delivery patterns (VAST + customer)  <br>  <br>https://learn.microsoft.com/en-us/azure/event-grid/configure-private-endpoints|
|Azure Functions|- Serverless transforms on arrival; glue code for sync + indexing<br>    <br>- DataEngine triggers Functions via HTTPS; Functions then call VAST S3/Blob API/NFS paths indirectly<br>    <br>- Fast “reaction loops” (tokenize, embed, catalog) without managing servers|Functions can integrate with VNets; private endpoints supported for inbound; outbound to VAST via VNet integration + routing|🟡|Native Blob-trigger bindings are tied to Azure Storage accounts; use webhook/event patterns instead. VNet integration constraints vary by plan (Customer + Microsoft + VAST)  <br>  <br>https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-vnet|
|Azure Logic Apps / Power Automate|- Workflow automation around data arrival + approvals<br>    <br>- DataEngine → Event Grid/HTTP to Logic Apps; Logic Apps invokes downstream systems<br>    <br>- Business-process automation integrated with data pipelines|Typically managed; can use private endpoints for some resources; otherwise through connectors|🟡|Connector behaviors and private network support vary widely; define supported “blessed” patterns (Customer + Microsoft)|
|Microsoft Purview|- Data catalog + classification over datasets that live on VAST<br>    <br>- Prefer S3 scanning patterns (validate VAST S3 compat); optionally ingest metadata via custom connector<br>    <br>- Keep VAST as a governed tier (avoid “compliance dark data”)|Managed service: often needs private network bridging (SHIR/gateway) depending on source|🟡|Purview S3 scanning is designed for AWS S3; must validate against VAST S3 semantics + auth model (VAST QA + customer)  <br>  <br>https://learn.microsoft.com/en-us/purview/register-scan-amazon-s3|
|Azure Monitor / Log Analytics|- Central observability for VAST + Azure compute; correlate storage + GPU metrics<br>    <br>- Uplink/collectors export logs/metrics; send to Log Analytics via REST ingestion APIs<br>    <br>- Single-pane ops; faster MTTR; chargeback reporting|Public or private ingestion depending on design; typically, HTTPS to workspace endpoints|🟢|Choose which ingestion API + schema governance; minor engineering integration (Customer + VAST)  <br>  <br>https://learn.microsoft.com/en-us/rest/api/loganalytics/create-request|
|Azure Lighthouse|- Fleet management for many VAST deployments across tenants<br>    <br>- Control-plane integration for managed app offers; operational delegation (not data path)<br>    <br>- MSP-scale operations; centralized governance + delegated access|Azure control plane delegation; no data plane requirement|🟡|Requires packaging decisions (Managed App/Marketplace) and Lighthouse definitions (VAST product + GTM)|
|Azure Private Link / Private Link Service (PLS)|- Secure private access to VAST endpoints from customer VNets + some managed VNets<br>    <br>- Expose VAST NFS/S3/Blob API behind Azure Standard Load Balancer + PLS<br>    <br>- Security parity with Azure-native storage; no public endpoints|Customer creates Private Endpoints; managed services may require “managed private endpoints” + approval; DNS must be correct|🟡|PLS connection approval workflow must be operationalized; some managed services don’t support FQDN/PLS (Fabric limitation) (Customer + VAST + Microsoft platform limits)  <br>  <br>https://learn.microsoft.com/en-us/azure/private-link/|

  
  

  
  

# Appendices  
  
Appendix A: Blob API Requirements

This section defines the strict subset of the Azure Blob REST API that VAST must implement to support Azure-native data movement tools and AI client libraries without client-side refactoring.  
  

The full Azure Blob REST API is documented here: [https://learn.microsoft.com/en-us/rest/api/storageservices/blob-service-rest-api](https://learn.microsoft.com/en-us/rest/api/storageservices/blob-service-rest-api)

  
  

### Goals, Non-Goals, and Success Criteria

Primary Goal: 

Enable standard Azure data movers (azcopy, Azure Storage Mover, VAST SyncEngine) and AI-centric libraries (boostedblob, azure-storage-blob Python SDK) to interact with VAST as if it were a standard Azure Storage endpoint.

  

Non-Goal:

Full emulation of Azure Blob Storage capabilities (e.g., Page Blobs, Append Blobs, Table/Queue services, ADLS Gen2/HNS) is explicitly out of scope.

  

Success Criteria:

- azcopy copy https://blob.core.windows.net/... https://vast-cluster/... succeeds 
    
- Standard Python training scripts using BlobServiceClient function correctly for list/read/write operations.
    
- Server-side copy operations (PutBlockFromURL) saturate available WAN links
    

  

Scope: Block Blobs Only (MVP)

AI workloads (training data, checkpoints, models) rely almost exclusively on Block Blobs.

- Included: Block Blobs (up to 4.75 TiB support via block list).
    
- Excluded: Page Blobs (VM disks), Append Blobs (legacy logs).
    
- Endpoint Type: The MVP emulates the Blob Service endpoint (blob.core.windows.net), not the Data Lake Storage Gen2 (DFS) endpoint (dfs.core.windows.net).
    

- Implication: No support for atomic directory renames or ACLs in the MVP API. Directories are emulated via "/" delimiters, mapping to VAST directories on the backend.
    

  
  

### MVP REST Surface Area

- Upload: Put Blob, Put Block, Put Block List
    

- Must respect x-ms-blob-type: BlockBlob.
    
- Must accept Base64-encoded Block IDs.
    
- Must support out-of-order block arrival. Commit path. Reassembles the blob from uncommitted blocks. Must support Latest, Committed, and Uncommitted block lists. This operation finalizes the ETag and Last-Modified timestamps.
    

- Download: Get Blob (Range), Head Blob
    

- Range Support is Mandatory: AI loaders (PyTorch) and resume-capable tools rely heavily on byte-range requests (Range: bytes=start-end).
    
- Must return status 206 Partial Content for ranges, not 200 OK.
    
- Get Blob Properties / Head Blob (REST verb: HEAD):
    

- Used by clients to check existence, size (Content-Length), and freshness (ETag) before downloading.
    

- List: List Blobs (prefix/delimiter/pagination)
    

- XML Fidelity: The response body must match the Azure enumeration XML schema exactly. SDKs parsers are brittle.
    
- Virtual Directories: Must support delimiter=/ to emulate folder browsing.
    
- Pagination: Must support maxresults and return a valid NextMarker for continuation.
    

- Delete: Delete Blob
    

- Must return 202 Accepted on success.
    
- Must return 404 Not Found (with XML error body) if blob is missing.
    

- Copy: PutBlobFromURL/PutBlockFromUrl (and fallbacks)
    

- This is the engine for "Central Lake -> Edge" hydration.
    
- VAST acts as the client, fetching data from the source URL provided in the header.
    
- Critical for Large Objects: AzCopy splits large files into blocks. VAST must fetch specific byte ranges (x-ms-source-range) from the source URL and stage them as blocks.
    
- This enables parallelized server-side copying of multi-GB checkpoints.
    

- Metadata/Properties
    

- User Metadata: Support x-ms-meta-* headers on PUT/HEAD.
    
- System Properties: Persist Content-Type, Content-Encoding, Content-MD5, and Cache-Control.
    

- Container Ops (Minimum Needed for Tools/SDKs)
    

- Create Container (PUT)
    
- Delete Container (DELETE)
    
- Get Container Properties (HEAD) – required by azcopy validation checks.
    
- List Containers (GET) – required for root-level browsing.
    

  

- Semantics Contract
    

- Headers
    

- ETag: Must emit standard strong ETags (quoted strings). VAST internal versions must map deterministically to ETags.
    
- Last-Modified: RFC 1123 format. Critical for sync logic ("copy only if newer").
    
- Content-MD5: If provided by the client on upload, VAST must validate the hash and reject on mismatch (400 Bad Request).
    

- Conditional Requests
    

- Optimistic Concurrency: Support If-Match (update only if ETag matches) and If-None-Match (don't overwrite if exists).
    
- Range + Resume: Support If-Range to ensure data hasn't changed while resuming a download.
    
- Error Model: XML Errors
    

  

- Error Handling
    

- Azure SDKs do not rely solely on HTTP Status Codes; they parse the XML error body to determine retry logic.
    
- Requirement: On 4xx/5xx errors, VAST must return Content-Type: application/xml with the standard Azure error schema. 
    
- Critical Codes: BlobNotFound, ContainerNotFound, ContainerAlreadyExists, LeaseIdMissing (if locking is touched).
    

  

- Throttling Model
    

- Behavior: On overload, return 503 Service Unavailable.
    
- Retry-After: Include the Retry-After header to inform smart SDKs to back off.
    
- Avoid 429: While Azure uses 429, AzCopy handles 503s more gracefully for "server busy" states in third-party implementations.
    

  

- Authentication & Authorization
    

- Entra ID / OAuth Token Validation (MVP Requirement)
    

- Mechanism: VAST validates the JWT signature using Microsoft's OIDC discovery keys.
    
- Identity Mapping: Map the Token's oid (Object ID) or appid (Service Principal ID) to a VAST User/Group for permission checking.
    

- Managed Identity Patterns
    

- Support access from Azure resources using System-Assigned or User-Assigned Managed Identities. This is functionally identical to (OAuth) but requires testing the specific token audience claims used by MSI.
    

- SAS Tokens (Compatibility Mode)
    

- Support Service SAS (at the container/blob level).
    
- Validation: VAST must recompute the signature based on the parameters (sp, st, se, sv) and the shared account key to allow/deny the request.
    

- Shared Key (Compatibility Mode)
    

- Legacy support for tools configured with "Connection Strings."
    
- Validation: Implementation of the "CanonicalizedResource" and "CanonicalizedHeaders" signing algorithm defined in Azure docs. Note: This is complex to get right but required for legacy compatibility.
    

- Authorization Mapping
    

- MVP: Simple mapping. Azure Container = VAST Bucket. Container Access Policy = Bucket Policy.
    
- Roadmap: Fine-grained ACL mapping (POSIX ACLs <-> Azure RBAC) is deferred.
    

- Performance Targets
    

- Concurrency: Support 1,000+ concurrent PutBlock requests per VIP to saturate high-bandwidth links.
    
- Keep-Alive: Aggressive connection reuse (HTTP/1.1 Keep-Alive) to avoid SSL handshake overhead on small operations.
    
- Large Objects: Validated support for 4TB+ objects (via Block List).
    

- Compatibility Harness (Gates)
    

- AzCopy Gate
    

- Test: Full suite of azcopy copy (upload/download), sync (differential), and remove.
    
- Pass Criteria: Zero errors, checksum validation passes, no manual flags required (other than endpoint override).
    

- High-Concurrency Clients Gate
    

- Test: boostedblob (used by OpenAI).
    
- Why: These libraries aggressively optimize concurrency and pipelining. If VAST's HTTP server implementation has locking bottlenecks, these tools will expose them immediately.
    

- Azure Storage SDK Gate (Python)
    

- Test: Standard azure-storage-blob library tests:
    

ContainerClient.list_blobs()

BlobClient.upload_blob(max_concurrency=N)

BlobClient.download_blob()

  

- Forward Compatibility & API Drift Strategy
    

- Versioning: The API will advertise a specific Azure Storage API version (e.g., 2021-08-06).
    
- Drift Policy: Unknown parameters or headers will be ignored rather than causing 400 errors, ensuring newer clients degrade gracefully.
    

  
  
  

# Appendix: Backlog of sections

  

## Strategic Context & Business Case

- ### Economics of GPU Starvation: Why “Good Enough” Storage Fails
    
- ### Supply Chain & Media Constraints: Flash Volatility, HDD as Capacity Tier, Procurement Lead Times
    
- ### Success Metrics & Measurement Framework
    

  

## Platform Overviews & Capability Alignment

- ### VAST Platform Overview
    

- #### Modules: DataStore, DataSpace, DataBase, DataEngine, InsightEngine, SyncEngine, AI OS, Uplink
    
- #### Protocol Surfaces: NFS/SMB/S3/Blob API/Kafka (as applicable)
    
- #### Data Reduction (DRR) Model and Capacity Math
    
- #### Resiliency & Failure Model (Fail‑in‑place, Erasure/Parity, Snapshots)
    

- ### Azure Platform Overview
    

- #### Storage: Blob/ADLS Gen2, Tiers, Private Link, Change Feed, Object Replication
    
- #### Compute: GPU VM Families, Lasv4/Lasv5, AKS, Batch, HPC
    
- #### Analytics: Fabric/OneLake, Synapse, Databricks (Classic + Serverless)
    
- #### Integration: Event Grid, Functions, Data Factory
    

- ### Key Architectural Constraints
    

- #### Control Plane Binding vs. Data Plane Endpoint Binding
    
- #### Managed VNet Constraints vs. Customer VNet Capabilities
    
- #### “Picker‑based” Services vs. URL/Endpoint‑based Services
    

  

## Deployment Variants & Reference Topologies

- ### Variant Catalog (Multi‑Hardware Reality)
    

- #### Variant A: VAST ODM Hardware Adjacent to GPUs (On‑Prem/Colo/Edge)
    
- #### Variant B: VAST on Azure IaaS (Lasv4/Lasv5) in Centralized Regions
    
- #### Variant C: VAST on Azure Storage‑Provided Bare Metal (Opportunity / Roadmap)
    
- #### Variant D: Hybrid Mesh (ODM + Azure Satellites + Blob Capacity Tier)
    

- ### Selection Framework (Customer/Region/Requirements to Variant mapping)
    
- ### Performance Profiles (Capacity, Bandwidth, IOPS, Latency)
    
- ### DRR & Efficiency Profiles (Effective Capacity, Power, Rack Density)
    
- ### Regional Constraints (Quotas, SKU Availability, Capacity Reservations)
    
- ### Supply Chain & Procurement Implications (Lead Times, Substitution Options)
    
- ### Reliability, Failure Domains & HA Options
    
- ### DR/BC Reference Designs (RPO/RTO Targets, Replication Patterns)
    

  

## Integration Architecture Overview

- ### Layered Integration Model
    

- #### Data Plane
    
- #### Namespace/Metadata Plane
    
- #### Control Plane
    
- #### Operations Plane
    
- #### Commercial/Billing Plane
    

- ### Network Models
    

- #### Customer VNet (“Easy Mode”)
    
- #### Microsoft Managed VNet (“Wall”)
    
- Public Endpoint
    

- ### Core Integration Patterns Library
    

- #### Direct Mount (NFS/SMB)
    
- #### Direct Object (S3)
    
- #### Blob API Endpoint (Compatibility Façade)
    
- #### Virtualization (Fabric Shortcuts / External Locations)
    
- #### Bridging (On‑Prem Gateway / Self‑Hosted IR / Jump‑Box Patterns)
    
- #### Private Link Service (Partner PaaS‑like Exposure)
    
- #### Cross‑Region Replication over Azure Backbone (Peering/vWAN)
    

  

## Namespace & Metadata Federation (Federation Plane)

- ### Problem Statement: The “Split‑Brain Namespace”
    

- ### Patterns
    

- #### Pattern A: VAST Master (Tiering Flow)
    
- #### Pattern B: Blob Master (Ingest Flow)
    
- #### Pattern C: Proxy / Migration‑on‑Read (Tuscany‑like Future)
    

- ### Change Detection & Reconciliation
    

- #### Event Grid (Low Latency Trigger)
    
- #### Change Feed (Authoritative Log)
    
- #### Reconciliation Scans (Safety Net)
    

- ### Metadata Model & Mapping
    

- #### Namespace Mapping (Containers/Prefixes ↔ Directories)
    
- #### Metadata Mapping (mtime, etag, content-type, custom metadata)
    
- #### Security Mapping (Identity, ACL semantics, drift control)
    

- ### Stub/Hydration Design
    

- #### Metadata‑Only Stubs
    
- #### Read‑Through Fetch & Cache Policies
    
- #### Rehydration/Pinning Policies
    

- ### Consistency & Concurrency
    

- #### Eventual Consistency Guarantees & SLAs
    
- #### Conflict Resolution (Last‑Writer‑Wins, Read‑Only Zones, etc.)
    
- #### Leases/Locks (Future)
    

- ### Scale Architecture
    

- #### Sharding, Checkpointing, Lag Tracking
    
- #### Backpressure and Rate Limiting
    

- ### Observability & Operations (Sync Health, Lag, Reconciliation Metrics)
    

  

## Tiering, Lifecycle & Data Formats

- ### Tiering Modes: Opaque vs Transparent vs Hybrid
    
- ### Policy Framework (Hot/Warm/Cold, Retention, Compliance, Residency)
    
- ### Cost & Transfer Considerations (Egress, Cross‑Region, Cache Amplification)
    
- ### Portability & Exit Strategy
    

  

## Networking & Connectivity

- ### Connectivity Design Principles (Private‑First, Deterministic Routing)
    
- ### Private Endpoints & Private Link Fundamentals
    
- ### Private Link Service (PLS) for VAST Endpoints
    
- ### PLS Alias & Connection Approval Workflow (Who Approves, How Automated)
    
- ### DNS Architecture (Private Zones, Split‑Horizon, Managed VNet DNS)
    
- ### Customer VNet Connectivity (Peering, Routing, NSGs, ExpressRoute)
    
- ### Managed VNet Connectivity Patterns (Fabric/Synapse/Serverless)
    
- ### Throughput & Scale Limits (Azure SLB, SNAT, Conntrack, Timeouts, Keep‑Alive)
    
- ### Cross‑Region Backbone Patterns (Global Peering, vWAN, Replication Paths)
    

  

## Identity, Security, Compliance & Governance

- ### Threat Model & Security Posture
    
- ### Identity Integration
    
- ### Key Management (Key Vault, Rotation, Customer‑Managed Keys)
    
- ### Perimeter Controls (NSP, Firewalls, Egress Policies, Exfiltration Control)
    
- ### Shared Responsibility Model (VAST vs Microsoft vs Customer)
    

  
