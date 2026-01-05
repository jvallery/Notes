# Competitive Landscape & Differentiation (VAST + Azure)

**Purpose:** Provide a crisp “why VAST + Azure” view: what we’re competing with, where we complement Azure-native storage, and what is uniquely differentiated in this joint strategy.

## What We Compete With (Categories)

### Azure-native options (customer defaults)

- **“Just Blob” + client-side caching:** blobfuse/blobfuse2, application caches, bespoke pipeline staging.
- **Azure NetApp Files (ANF):** high-performance managed file service; strong enterprise footprint for POSIX workloads.
- **Azure Managed Lustre (AMLFS):** HPC parallel file system patterns (training/shuffle workloads).

### Storage vendors with “cloud adjacencies”

- **Weka on Azure** (performance tier / file + object patterns)
- **NetApp** (ANF + Cloud Volumes ONTAP patterns)
- **Pure Storage** (hybrid cloud offerings; ecosystem integrations)
- **Dell/Isilon/PowerScale** (hybrid NAS footprints; migration narratives)

### “DIY” architectures

- Move hot data to local NVMe on compute nodes; accept rehydration pain.
- Build proxy layers and custom metadata/index stores; accept operational burden.
- Create bespoke replication + namespace solutions (high risk; long lead times).

## Differentiation Axes (What’s Unique Here)

### 1) Governance tier + performance tier as one fabric

- Blob remains the governed system of record (durability, ecosystem gravity).
- VAST supplies GPU-adjacent performance without creating a “dark silo.”

### 2) Interoperability without refactors

- Blob API façade enables existing Azure tooling (AzCopy/SDKs) and common AI libraries to work end-to-end.
- Multi-protocol coherence (Blob/S3/NFS/SMB) reduces “two namespaces” drift.

### 3) Density + efficiency at scale

- Performance tier reserved for the hot working set; cold tail and durability land in Blob.
- A unified plan for tiering + replication is easier to operate than bespoke copies.

### 4) Deployment flexibility (hybrid reality)

- GPU-adjacent deployments aren’t always in Azure hero regions (colo/neo-cloud/on-prem).
- Variants A/B/D support where compute lands while keeping the governance core centralized.

## Positioning (Working Narrative)

- **We are not trying to be “another Blob.”** Blob is the governance/capacity substrate.
- **We are not only a file service.** Multi-protocol access and federation/tiering are core to the AI data fabric story.
- **We complement Azure-native services** by keeping data and lineage close to Azure workflows while eliminating performance bottlenecks at the edge.

## Research Needed (To Make This Defensible)

- Comparative “what Azure customers do today” for AI/HPC datasets (Blob-only patterns, blobfuse2 performance ceilings, common failure modes).
- ANF and Azure Managed Lustre constraints vs the target Crawl workloads (W2/W5) and multi-protocol needs.
- Weka/NetApp/Pure positioning in Azure: what they claim, what they actually deliver, and where customers get stuck (private networking, namespace, operations).

## Sources (Starting List)

- Azure NetApp Files: https://learn.microsoft.com/en-us/azure/azure-netapp-files/
- Azure Managed Lustre: https://learn.microsoft.com/en-us/azure/azure-managed-lustre/
- blobfuse2: https://learn.microsoft.com/en-us/azure/storage/blobs/blobfuse2-what-is
