

## 5. Workload Catalog & Workload‑to‑Variant Mapping

This section turns strategy into deployable architectural patterns. It maps business scenarios to concrete hardware substrates and integration mechanics, providing a playbook for field teams and architects.

### 5.0 Deployment Variant Definitions

To streamline the catalog, we reference these standard deployment models:

- **Variant A (ODM / Edge):** VAST hardware deployed adjacent to GPUs in customer datacenters, colocation facilities, or "neo-clouds." Best for maximum density and performance.
    
- **Variant B (Azure IaaS):** VAST software running on storage-optimized Azure VMs (Lasv4/Laosv4) with local NVMe. Best for elasticity and cloud-native integration.
    
- **Variant C (Azure Bare Metal):** _Future/Roadmap._ VAST on Azure-provided bare metal infrastructure for high-density managed service scenarios.
    
- **Variant D (Hybrid):** A unified namespace spanning on-prem ODM clusters (Origin) and Azure VM clusters (Satellite).
    

---

### 5.1 Workload Definition Template

Every workload is defined by:

- **Scenario:** The business or technical challenge.
    
- **Topology & Flow:** Where data lives and how it moves.
    
- **VAST + Azure Integration:** The specific mechanics and value drivers.
    

---

### 5.2 W1: On‑Prem VAST + Burst Compute on Azure

- **Scenario:** A customer holds massive datasets on-premises (often due to gravity or compliance) but needs ephemeral Azure GPU capacity (e.g., HBv4/ND H100 v5) to meet critical training deadlines. They cannot afford to permanently migrate petabytes or refactor POSIX applications.
    
- **Topology & Flow:** **Variant D (Hybrid)**. On-prem ODM acts as the data origin; a temporary Variant B cluster in Azure acts as a caching satellite. Connected via ExpressRoute.
    
- **VAST + Azure Integration:**
    
    - **Elasticity without Gravity:** This architecture breaks data gravity. Customers gain infinite compute elasticity without the egress tax and time penalty of moving cold data.
        
    - **Namespace Consistency:** The VAST Global Namespace presents a unified view to cloud compute. The satellite intelligently caches only the "hot" working set, ensuring high-performance local access for Azure GPUs while masking WAN latency.
        

### 5.3 W2: Streaming Data Pipelines (Kafka & Event Broker)

- **Scenario:** High-velocity ingest from IoT fleets, telemetry, or cyber logs requires real-time persistence and historical analysis. Traditional Kafka architectures struggle with retention limits and storage costs at scale.
    
- **Topology & Flow:** **Variant A (Edge)** or **Variant B (Azure)**. Producers write to VAST; Consumers (Spark/Azure Stream Analytics) read from VAST.
    
- **VAST + Azure Integration:**
    
    - **Infinite Retention:** Leveraging the **VAST Event Broker**, producers write directly to VAST using Kafka protocols. VAST persists the stream indefinitely on cost-effective flash (tiered to Blob), eliminating the "Kafka Tax" of expensive ephemeral broker storage.
        
    - **Query-in-Place:** Downstream Azure services (Stream Analytics, Data Explorer) can query this historical data directly via S3/Parquet protocols, bypassing rehydration steps.
        

### 5.4 W3: Spark & Databricks Analytics (VAST Database)

- **Scenario:** Data Engineering teams using Azure Databricks or Synapse Spark face I/O bottlenecks during shuffle phases and high-concurrency queries against standard object stores.
    
- **Topology & Flow:** **Variant B (Azure)**. Databricks clusters in the same VNet interact with VAST.
    
- **VAST + Azure Integration:**
    
    - **Zero-Shuffle Analytics:** The **VAST Database** pushes query predicates (filters, projections) down to the storage layer. Instead of pulling massive tables over the network, VAST filters data _in situ_, sending only relevant results.
        
    - **Decoupled Scaling:** This allows Databricks clusters to run stateless and lean, scaling compute independently of storage performance.
        

### 5.5 W4: Hybrid Cloud Tiering (On-Prem Flash $\to$ Azure Blob)

- **Scenario:** Customers love flash performance but need cloud economics for cold data. This is critical for **PACS (Medical Imaging)**, **Media Archives**, and **Backup Targets** where recent data is hot but historical data is vast.
    
- **Topology & Flow:** **Variant A (On-Prem)** tiers to **Azure Blob (Cool/Archive)**.
    
- **VAST + Azure Integration:**
    
    - **Edge Ingestion:** Remote sites (factories, sequencers) ingest data at line-rate flash speeds on small VAST footprints, immediately tiering to the central Azure Blob lake.
        
    - **BCDR & Ransomware Recovery:** Azure Blob acts as the immutable, air-gapped "gold copy." In a disaster, a new VAST instance can spin up in Azure (or secondary site) and instantly resume operations by reading metadata from Blob, hydrating data only on demand.
        

### 5.6 W5: Ecosystem Access (PaaS Integration)

- **Scenario:** AI data on VAST needs to trigger workflows in Azure Functions, feed Event Grid topics, or be accessible to logic apps without heavy ETL movement.
    
- **Topology & Flow:** **Variant B (Azure)** connected to Azure PaaS via VNet Injection or Private Link.
    
- **VAST + Azure Integration:**
    
    - **The "Tuscany" Enabler:** Leveraging migration-on-read patterns (like Cloudflare Sippy/Tuscany), VAST enables seamless federation where Azure PaaS services interact with VAST data as if it were native Blob.
        
    - **Event-Driven Workflow:** Integration with **Azure Event Grid** turns storage into a trigger. A file upload to VAST can instantly fire an Azure Function to tokenize data or update a vector index.
        
    - **Fabric Shortcuts:** VAST data is exposed to **Microsoft Fabric** via S3-compatible shortcuts, allowing the ecosystem to query high-performance data in place.
        

### 5.7 W6: Cloud Native Applications (AKS & Microservices)

- **Scenario:** Complex containerized applications on AKS require high-throughput, Read-Write-Many (RWX) persistent storage that standard cloud file services often throttle.
    
- **Topology & Flow:** **Variant B (Azure)** linked to AKS Clusters.
    
- **VAST + Azure Integration:**
    
    - **True RWX Performance:** Unlike Azure Files or BlobFuse, VAST provides "SAN-grade" shared file performance to AKS via the CSI Driver.
        
    - **Consolidated State:** It allows diverse microservices (databases, queues, web servers) to share a single, high-performance persistence layer that eliminates the "noisy neighbor" problems of multi-tenant cloud storage.
        

### 5.8 W7: Cross‑Region Training & Global WAN

- **Scenario:** Multinational research teams need to collaborate on shared datasets across US, Europe, and Asia regions without the latency or unreliability of the public internet.
    
- **Topology & Flow:** **Variant B (Multi-Region)** connected via **Azure Virtual WAN**.
    
- **VAST + Azure Integration:**
    
    - **Global Data LAN:** Coupling VAST's Global Namespace with **Azure’s Global WAN** creates a deterministic, private backbone for replication.
        
    - **Efficiency:** VAST’s similarity-based global deduplication ensures only unique bytes traverse the wire, while Azure’s backbone provides stability unmatched by the public internet.
        

### 5.9 W8: Regulated AI & Enclaves (Sovereign & Hybrid)

- **Scenario:** FSI or Defense customers require "Sovereign Cloud" security—using cloud agility but ensuring the provider (Microsoft) cannot access sensitive data or keys.
    
- **Topology & Flow:** **Variant B (Isolated VNet)** with Customer-Managed Keys (CMK).
    
- **VAST + Azure Integration:**
    
    - **The Data Enclave:** VAST enables a logical air-gap. By deploying inside a locked-down VNet with strict Private Link controls and customer-held encryption keys, the data remains opaque to the underlying infrastructure.
        
    - **Compliance:** This architecture satisfies strict residency and audit requirements (ITAR, GDPR) while retaining cloud provisioning speed.
        

### 5.10 W9: Migration & Modernization

- **Scenario:** Exiting legacy on-prem NAS (NetApp/Isilon) to Azure is blocked because applications rely on specific protocol behaviors cloud-native storage doesn't fully emulate.
    
- **Topology & Flow:** **Source (Legacy)** $\to$ **Target (Variant B)**.
    
- **VAST + Azure Integration:**
    
    - **Risk-Free Entry:** VAST provides absolute protocol parity (NFSv3/v4, SMB, S3) with enterprise appliances. This enables a "zero-refactor" lift-and-shift.
        
    - **Modernization Bridge:** Once in Azure, customers can incrementally modernize applications to cloud-native patterns (like object storage) using VAST’s multi-protocol access to bridge the gap.
        

### 5.11 Workload Alignment Matrix

| **Workload**               | **Recommended Variant** | **Integration Pattern**    | **Key Value Driver**                 |
| -------------------------- | ----------------------- | -------------------------- | ------------------------------------ |
| **W1: Burst Compute**      | Variant D (Hybrid)      | Global Namespace (Cache)   | Elasticity without Egress Shock      |
| **W2: Streaming**          | Variant A/B             | VAST Event Broker          | Infinite Retention & Real-time Query |
| **W3: Spark/Databricks**   | Variant B               | VAST Database (Pushdown)   | Zero-Shuffle Analytics               |
| **W4: Hybrid Tiering**     | Variant A (On-Prem)     | Transparent/Opaque Tiering | Edge Ingest & BCDR                   |
| **W5: Ecosystem (PaaS)**   | Variant B               | Tuscany / Event Grid       | Seamless "Migration-on-Read"         |
| **W6: Cloud Native (AKS)** | Variant B               | CSI Driver / NFS           | True RWX Performance                 |
| **W7: Global Namespace**   | Variant B (Multi)       | Azure Virtual WAN          | Dedupe-Optimized Global Backbone     |
| **W8: Regulated AI**       | Variant A/B             | Private Link / Enclave     | Sovereign Data Control               |
| **W9: Migration**          | Variant B               | Multiprotocol (NFS/SMB)    | Risk-Free Cloud Entry                |
|                            |                         |                            |                                      |
## 2. Strategic Context & Business Case

### 2.2 Economics of GPU Starvation: Why “Good Enough” Storage Fails

### 2.3 Supply Chain & Media Constraints: Flash Volatility, HDD as Capacity Tier, Procurement Lead Times

### 2.4 Sustainability & Power Density: Efficiency as a First‑Order Constraint

### 2.5 Partnership Value Proposition: Why Microsoft Wins / Why VAST Wins



### 2.8 Success Metrics & Measurement Framework

## 3. Platform Overviews & Capability Alignment

### 3.1 VAST Platform Overview

#### 3.1.1 DASE Architecture

#### 3.1.2 Modules: DataStore, DataSpace, DataBase, DataEngine, InsightEngine, SyncEngine, AI OS, Uplink

#### 3.1.3 Protocol Surfaces: NFS/SMB/S3/Blob API/Kafka (as applicable)

#### 3.1.4 Data Reduction (DRR) Model and Capacity Math

#### 3.1.5 Resiliency & Failure Model (Fail‑in‑place, Erasure/Parity, Snapshots)

### 3.2 Azure Platform Overview

#### 3.2.1 Storage: Blob/ADLS Gen2, Tiers, Private Link, Change Feed, Object Replication

#### 3.2.2 Compute: GPU VM Families, Lasv4/Lasv5, AKS, Batch, HPC

#### 3.2.3 Analytics: Fabric/OneLake, Synapse, Databricks (Classic + Serverless)

#### 3.2.4 Integration: Event Grid, Functions, Data Factory (IR patterns)

#### 3.2.5 Governance/Operations: Purview, Monitor, Lighthouse

### 3.3 Feature Alignment Map: VAST Capabilities ↔ Azure Primitives

### 3.4 Key Architectural Constraints

#### 3.4.1 Control Plane Binding vs. Data Plane Endpoint Binding

#### 3.4.2 Managed VNet Constraints vs. Customer VNet Capabilities

#### 3.4.3 “Picker‑based” Services vs. URL/Endpoint‑based Services

## 4. Deployment Variants & Reference Topologies

### 4.1 Variant Catalog (Multi‑Hardware Reality)

#### 4.1.1 Variant A: VAST ODM Hardware Adjacent to GPUs (On‑Prem/Colo/Edge)

#### 4.1.2 Variant B: VAST on Azure IaaS (Lasv4/Lasv5) in Centralized Regions

#### 4.1.3 Variant C: VAST on Azure Storage‑Provided Bare Metal (Opportunity / Roadmap)

#### 4.1.4 Variant D: Hybrid Mesh (ODM + Azure Satellites + Blob Capacity Tier)

### 4.2 Selection Framework (Customer/Region/Requirements → Variant)

### 4.3 Performance Profiles (Capacity, Bandwidth, IOPS, Latency)

### 4.4 DRR & Efficiency Profiles (Effective Capacity, Power, Rack Density)

### 4.5 Regional Constraints (Quotas, SKU Availability, Capacity Reservations)

### 4.6 Supply Chain & Procurement Implications (Lead Times, Substitution Options)

### 4.7 Reliability, Failure Domains & HA Options

### 4.8 DR/BC Reference Designs (RPO/RTO Targets, Replication Patterns)

## 5
## 6. Integration Architecture Overview

### 6.1 Layered Integration Model

#### 6.1.1 Data Plane

#### 6.1.2 Namespace/Metadata Plane

#### 6.1.3 Control Plane

#### 6.1.4 Operations Plane

#### 6.1.5 Commercial/Billing Plane

### 6.2 Network Models

#### 6.2.1 Customer VNet (“Easy Mode”)

#### 6.2.2 Microsoft Managed VNet (“Wall”)

### 6.3 Core Integration Patterns Library

#### 6.3.1 Direct Mount (NFS/SMB)

#### 6.3.2 Direct Object (S3)

#### 6.3.3 Blob API Endpoint (Compatibility Façade)

#### 6.3.4 Virtualization (Fabric Shortcuts / External Locations)

#### 6.3.5 Bridging (On‑Prem Gateway / Self‑Hosted IR / Jump‑Box Patterns)

#### 6.3.6 Private Link Service (Partner PaaS‑like Exposure)

#### 6.3.7 Cross‑Region Replication over Azure Backbone (Peering/vWAN)

## 7. Azure First‑Party Service Integration Matrix

### 7.1 AI & ML Services

#### 7.1.1 Azure OpenAI Service

#### 7.1.2 Azure AI Foundry (Control Plane vs Compute Plane)

#### 7.1.3 Azure Machine Learning (Datastores vs Direct Mount Paths)

#### 7.1.4 Azure AI Search (Augment vs Replace vs Hybrid)

### 7.2 Analytics

#### 7.2.1 Microsoft Fabric / OneLake (S3 Shortcuts, Gateway, Trusted Access)

#### 7.2.2 Azure Databricks Classic (VNet Injected)

#### 7.2.3 Azure Databricks Serverless (Managed VNet + NCC + Private Link)

#### 7.2.4 Azure Synapse Analytics (Managed Private Endpoints)

### 7.3 Compute & Containers

#### 7.3.1 AKS (CSI, RWX, Identity for Storage Access)

#### 7.3.2 Azure Batch (Mount + Burst)

#### 7.3.3 HPC VMs (NFS/S3, checkpoint patterns)

### 7.4 Data Movement & Eventing

#### 7.4.1 Azure Data Factory (Managed IR vs Self‑Hosted IR)

#### 7.4.2 Azure Storage Mover / Data Box (Constraints & Fit)

#### 7.4.3 Event Grid + Functions (Event‑Driven Pipelines)

### 7.5 Governance & Operations

#### 7.5.1 Microsoft Purview (Catalog/Lineage Touchpoints)

#### 7.5.2 Azure Monitor / Log Analytics (Observability)

#### 7.5.3 Azure Lighthouse (Fleet Management at Scale)

## 8. Blob API Compatibility MVP (Data Plane)

### 8.1 Goals, Non‑Goals, and Success Criteria

### 8.2 Scope: Block Blobs Only (MVP)

### 8.3 MVP REST Surface Area

#### 8.3.1 Upload: Put Blob, Put Block, Put Block List

#### 8.3.2 Download: Get Blob (Range), Head Blob

#### 8.3.3 List: List Blobs (prefix/delimiter/pagination)

#### 8.3.4 Delete: Delete Blob

#### 8.3.5 Copy: Put Blob From URL (and fallbacks if needed)

#### 8.3.6 Metadata/Properties: Get/Set Metadata, Set Properties

#### 8.3.7 Container Ops (Minimum Needed for Tools/SDKs)

### 8.4 Semantics Contract

#### 8.4.1 Headers: ETag, Last‑Modified, Content‑Length, Content‑MD5

#### 8.4.2 Conditional Requests: If‑Match/If‑None‑Match, Range + Resume

#### 8.4.3 Error Model: XML Errors, Retryable Codes, SDK Expectations

#### 8.4.4 Throttling Model: 429/503 Behavior and Backoff Compatibility

### 8.5 Authentication & Authorization

#### 8.5.1 Entra ID / OAuth Token Validation (MVP Requirement)

#### 8.5.2 Managed Identity Patterns (System/User Assigned)

#### 8.5.3 SAS Tokens (Compatibility Mode)

#### 8.5.4 Shared Key (Compatibility Mode)

#### 8.5.5 Authorization Mapping (RBAC/ACL Strategy)

### 8.6 Performance Targets (Concurrency, Keep‑Alive, Large Object Behavior)

### 8.7 Compatibility Harness (Gates)

#### 8.7.1 AzCopy Gate

#### 8.7.2 Azure Storage SDK Gate (Python: `azure-storage-blob`)

#### 8.7.3 Additional SDK Gates (Optional: .NET/Java)

#### 8.7.4 High‑Concurrency Clients Gate (boostedblob/rclone‑class)

### 8.8 Forward Compatibility & API Drift Strategy

### 8.9 MVP → VNext Roadmap (Expanded APIs, ADLS Gen2/DFS Considerations)

## 9. Namespace & Metadata Federation (Federation Plane)

### 9.1 Problem Statement: The “Split‑Brain Namespace”

### 9.2 Patterns

#### 9.2.1 Pattern A: VAST Master (Tiering Flow)

#### 9.2.2 Pattern B: Blob Master (Ingest Flow)

#### 9.2.3 Pattern C: Proxy / Migration‑on‑Read (Tuscany‑like Future)

### 9.3 Change Detection & Reconciliation

#### 9.3.1 Event Grid (Low Latency Trigger)

#### 9.3.2 Change Feed (Authoritative Log)

#### 9.3.3 Reconciliation Scans (Safety Net)

### 9.4 Metadata Model & Mapping

#### 9.4.1 Namespace Mapping (Containers/Prefixes ↔ Directories)

#### 9.4.2 Metadata Mapping (mtime, etag, content-type, custom metadata)

#### 9.4.3 Security Mapping (Identity, ACL semantics, drift control)

### 9.5 Stub/Hydration Design

#### 9.5.1 Metadata‑Only Stubs

#### 9.5.2 Read‑Through Fetch & Cache Policies

#### 9.5.3 Rehydration/Pinning Policies

### 9.6 Consistency & Concurrency

#### 9.6.1 Eventual Consistency Guarantees & SLAs

#### 9.6.2 Conflict Resolution (Last‑Writer‑Wins, Read‑Only Zones, etc.)

#### 9.6.3 Leases/Locks (Future)

### 9.7 Scale Architecture

#### 9.7.1 Sharding, Checkpointing, Lag Tracking

#### 9.7.2 Backpressure and Rate Limiting

### 9.8 Observability & Operations (Sync Health, Lag, Reconciliation Metrics)

### 9.9 Roadmap: Async Sync → Stub Federation → Deeper Collaboration

## 10. Tiering, Lifecycle & Data Formats

### 10.1 Tiering Modes: Opaque vs Transparent vs Hybrid

### 10.2 Ecosystem Interaction Models

#### 10.2.1 Fabric Access Patterns vs Tiering Mode

#### 10.2.2 Synapse/Databricks Access Patterns vs Tiering Mode

### 10.3 Data Format Strategy (Open Formats, Parquet/Delta, “VAST Native”)

### 10.4 Policy Framework (Hot/Warm/Cold, Retention, Compliance, Residency)

### 10.5 Cost & Transfer Considerations (Egress, Cross‑Region, Cache Amplification)

### 10.6 Portability & Exit Strategy

## 11. Networking & Connectivity

### 11.1 Connectivity Design Principles (Private‑First, Deterministic Routing)

### 11.2 Private Endpoints & Private Link Fundamentals

### 11.3 Private Link Service (PLS) for VAST Endpoints

### 11.4 PLS Alias & Connection Approval Workflow (Who Approves, How Automated)

### 11.5 DNS Architecture (Private Zones, Split‑Horizon, Managed VNet DNS)

### 11.6 Customer VNet Connectivity (Peering, Routing, NSGs, ExpressRoute)

### 11.7 Managed VNet Connectivity Patterns (Fabric/Synapse/Serverless)

### 11.8 Throughput & Scale Limits (SNAT, Conntrack, Timeouts, Keep‑Alive)

### 11.9 Cross‑Region Backbone Patterns (Global Peering, vWAN, Replication Paths)

## 12. Identity, Security, Compliance & Governance

### 12.1 Threat Model & Security Posture

### 12.2 Identity Integration

#### 12.2.1 Entra ID / OAuth (Token Validation, Claims, Audience)

#### 12.2.2 Managed Identity (Workflows and Limitations)

#### 12.2.3 AD DS / Kerberos for SMB/NFS (Where Needed)

#### 12.2.4 AKS Workload Identity / Federated Credentials (CSI/Auth Implications)

### 12.3 Key Management (Key Vault, Rotation, Customer‑Managed Keys)

### 12.4 Perimeter Controls (NSP, Firewalls, Egress Policies, Exfiltration Control)

### 12.5 Audit, Forensics & Compliance Reporting

### 12.6 Regulated Workloads Patterns (PHI/PII, Residency, Encryption Boundaries)

### 12.7 Shared Responsibility Model (VAST vs Microsoft vs Customer)

## 13. Operations, Observability & Support

### 13.1 Deployment Automation (IaC, Templates, Golden Paths)

### 13.2 Monitoring & Telemetry (Uplink, Azure Monitor, Dashboards)

### 13.3 Upgrade/Maintenance Strategy (Rolling, Blue/Green, Rollback)

### 13.4 Multi‑Tenancy & QoS (Noisy Neighbor, Rate Limits)

### 13.5 Fleet Management at Scale (Azure Lighthouse Patterns)

### 13.6 DR/BC Operations (Runbooks, Testing Cadence, Failover/Failback)

### 13.7 Support Model (Boundaries, Escalation, SLAs)

## 14. Commercial Integration & GTM

### 14.1 Packaging Models

#### 14.1.1 Marketplace Private Offer (ODM / Private Cloud Attach)

#### 14.1.2 Marketplace Managed App (IaaS + Software Metering)

#### 14.1.3 BYOL + Customer‑Paid Azure Infrastructure

#### 14.1.4 Partner‑Led / Microsoft‑Led Motions

### 14.2 MACC Alignment (How Azure Consumption Is Burned)

### 14.3 Metering & Billing Architecture (Dimensions, Telemetry, Invoicing)

### 14.4 Procurement & Legal (Security Reviews, Data Processing Terms)

### 14.5 Co‑Sell Motion & Field Playbooks

### 14.6 Customer Adoption Journey (Land → Expand → Standardize)

## 15. Validation Plan & Acceptance Criteria

### 15.1 Workload KPIs and Benchmark Suites

### 15.2 Blob API Conformance Gates (Tools + SDKs)

### 15.3 Namespace/Metadata Integrity Tests (Lag, Reconciliation, Drift)

### 15.4 Networking Validation (PLS + Managed VNet End‑to‑End)

### 15.5 Security Validation (Token‑Based Auth, No‑Secrets Modes, Auditability)

### 15.6 Pilot Plan (Reference Customers, Regions, Exit Criteria)

## 16. Risks, Dependencies & Open Questions

### 16.1 Technical Risks (API Drift, Managed VNet Limits, Performance Variance)

### 16.2 Security Risks (Identity Coverage, Secrets Avoidance, Key Rotation)

### 16.3 Commercial Risks (Transactability, Metering, Support Boundaries)

### 16.4 Microsoft Dependencies (Private Connectivity Features, Proxy Futures)

### 16.5 Open Questions (Decision‑Blocking Unknowns)

### 16.6 Research & Experiment Backlog (Prioritized)

## 17. Roadmap & Engineering Plan

### 17.1 Phase Definitions (0–3) and Exit Criteria

### 17.2 Engineering Epics (Blob API, Identity, PLS, Federation, Tiering)

### 17.3 Partner Collaboration Workstreams (Microsoft + VAST)

### 17.4 Timeline Assumptions & Release Cadence

---

## Appendices

### Appendix A. Glossary & Acronyms

### Appendix B. Full Azure Service Integration Matrix (Expanded)

### Appendix C. Blob API MVP Spec + Compatibility Harness (AzCopy + SDK + High‑Concurrency Clients)

### Appendix D. Namespace & Metadata Federation Design (Deep Dive + Tradeoffs)

### Appendix E. Deployment Variants Deep Dive (ODM / Lasv4/Lasv5 / Bare Metal)

### Appendix F. Private Link / PLS Operational Runbook (Alias, Approvals, DNS, Automation)

### Appendix G. Tiering Decision Records (Opaque vs Transparent vs Hybrid)

### Appendix H. Reference Architectures & Sequence Diagrams (by Workload)

### Appendix I. Benchmarking Methodology & Test Results Template

### Appendix J. Commercial Packaging Decision Records (Marketplace, Metering, MACC)

### Appendix K. Security Controls Mapping (Zero Trust, Identity, Audit)

### Appendix L. DR/BC Design Patterns & Runbooks