# Terminology & Conventions

This appendix standardizes key terms used across the VAST + Azure integration doc set.

## Core Concepts

- **Azure Blob Storage (“Blob”):** The governed system of record and durable capacity tier.
- **VAST (performance tier):** GPU‑adjacent, high‑performance tier that can cache/hydrate data near compute and synchronize value back to Blob.
- **Blob API façade (on VAST):** A high‑fidelity subset of the Azure Blob REST API implemented on VAST to enable Azure tooling/SDK compatibility (not full Blob emulation). See: [Blob API Requirements (MVP)](Blob%20API%20Requirements%20%28MVP%29.md)
- **Governance tier vs performance tier:** “Blob as truth” (governance, durability, ecosystem) vs “VAST as hot working set” (latency/throughput near GPUs).

## Deployment Terms

- **Hero Region / Hero Regions:** A centralized Azure region that anchors the governed data lake and Azure ecosystem access.
- **Edge / satellite / neo‑cloud:** Locations where GPU capacity lands (satellite Azure regions, specialized GPU clouds, colo, on‑prem AI factories).

## Networking Terms

- **Customer VNet:** Customer-owned virtual network where workloads run and where VAST endpoints are reachable privately via peering/ExpressRoute and Private Link.
- **Managed VNet:** Service-managed networking boundary (e.g., some Synapse/Fabric/serverless offerings) that often requires managed private endpoints and approval workflows.
- **Private Link Service (PLS):** Azure construct to expose partner services privately to customer VNets.
- **Private Endpoint:** Customer-side NIC that maps to a PLS or Azure PaaS service over private IP.

## Common Abbreviations

- **1P:** Microsoft first‑party service.
- **BCDR:** Business continuity / disaster recovery.
- **RWX:** ReadWriteMany (shared read/write persistent storage).

## VAST Module Naming (Preferred)

Use VAST’s module names when referring to specific product capabilities:

- **DataStore:** file/object protocol access layer (e.g., NFS/SMB/S3; plus Blob API façade where applicable).
- **DataSpace:** global namespace / hybrid data orchestration.
- **DataBase:** analytics/query acceleration (e.g., predicate pushdown).
- **DataEngine:** pipeline/eventing/automation capabilities.
- **InsightEngine:** metadata/vector/index capabilities (where applicable).
- **SyncEngine:** data movement/synchronization between tiers.
- **Event Broker:** Kafka-compatible streaming interface (where applicable).

## Pattern Names

- **“Tuscany” / migration‑on‑read:** A proxy/federation pattern where Azure services can interact with VAST data “as if” it were native Blob, typically by presenting compatible endpoints and mapping semantics. (This term should be clarified/validated before external sharing.)

## Document Conventions

- **Phases:** Crawl → Walk → Run
- **Variants:** Variant A/B/C/D (see [Workloads & Reference Topologies](Workloads%20%26%20Reference%20Topologies.md))
- **Workloads:** W1–W10 (see [Workloads & Reference Topologies](Workloads%20%26%20Reference%20Topologies.md))
