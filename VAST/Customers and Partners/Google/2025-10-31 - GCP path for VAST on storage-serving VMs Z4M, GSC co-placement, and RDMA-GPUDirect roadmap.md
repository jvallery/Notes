---
type: customer
title: GCP path for VAST on storage-serving VMs (Z4M), GSC co-placement, and RDMA/GPUDirect roadmap
date: '2025-10-31'
account: Google
participants:
- Jason Vallery
- Billy Kettler
- John Downey
- Lior Genzel
- Unknown Google Cloud participant
source: transcript
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-31 - GCP outlined the path to run VAST on storage-serving VMs (Z4M) with higher stora.md
tags:
- type/customer
- generated
---

# GCP path for VAST on storage-serving VMs (Z4M), GSC co-placement, and RDMA/GPUDirect roadmap

**Date**: 2025-10-31
**Account**: [[Google]]
**Attendees**: Jason Vallery, Billy Kettler, John Downey, Lior Genzel

## Summary

Google Cloud outlined the evolution from Z3 to Z4M storage-serving VMs to run VAST with higher storage and network density, plus upcoming co-placement/provisioning via the Google Supercomputer (GSC) interface. The group aligned on local SSD as the initial tier for latency, with future evaluation of HyperDisk and object-tier metadata offload, and discussed RDMA and GPUDirect Storage enablement for A5X GPUs (TPU RDMA later) and the economics of internal and cross-region data movement.

## Action Items

- [?] Draft and share a written list of networking questions and formal requests for Google Cloud (including Cloud WAN and internal load balancing or egress-like cost drivers) ahead of Supercomputing meetings. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Review the Google Cloud WAN material shared by Google Cloud and assess applicability to VAST multi-region and neo-hyperscaler data movement patterns. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Analyze performance and design implications of offloading VAST metadata to an object tier on Google Cloud, including latency sensitivity and required object tier characteristics. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Schedule Supercomputing in-person meetings between VAST and Google Cloud and attempt to include Google Cloud stakeholders Ilyas (cluster program) and Dean (CTO/expert). @John Downey 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Confirm RDMA and GPUDirect Storage enablement details and cost implications for Z4M storage-serving VMs and A5X GPU instances, and share the plan internally at VAST. @Billy Kettler 📅 2025-11-08 #task #proposed #auto

- [?] Engage Google Cloud networking and pricing stakeholders to explore commercial constructs that reduce internal networking and egress-like costs for partner storage-serving solutions at multi-TB/s throughput. @John Downey 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Draft and share a written set of networking questions and formal requests for Google Cloud (including Cloud WAN, ILB cost drivers, and multi-region data movement architecture) ahead of Supercomputing. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Explore commercial constructs with Google Cloud to mitigate inter-region and egress-like internal networking costs for VAST and joint customers running storage-serving partner solutions. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Schedule Supercomputing meetings and attempt to include Google Cloud stakeholders Ilyas (cluster program) and Dean (CTO/expert) for in-person alignment on Z4M, GSC integration, and RDMA roadmap. @John Downey 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Confirm RDMA and GPUDirect Storage enablement details and cost implications for Z4M and A5X GPU environments, and share the plan internally at VAST Data. @Billy Kettler 📅 2025-11-08 #task #proposed #auto

- [?] Scope how VAST could be offered as a selectable storage option within the Google Supercomputer (GSC) provisioning flow, including auto-deploy and co-placement behavior. @Billy Kettler 📅 2025-11-08 #task #proposed #auto

- [?] Analyze performance and design implications of offloading VAST metadata to object storage on Google Cloud, including required object-tier latency and throughput characteristics. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Engage Google Cloud networking and pricing teams to reduce ILB and internal egress-like costs for storage-serving partner solutions at high throughput. @John Downey 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Evaluate feasibility and timeline for a higher-performance object storage tier on Google Cloud suitable for VAST metadata offload (for example, an S3 One Zone-like or Premium Blob-like tier). @TBD 📅 2025-11-08 #task #proposed #auto

- [?] Define the path and expected timeline for RDMA enablement on Google TPUs and implications for VAST deployments that target TPU-based training or inference. @Billy Kettler 📅 2025-11-08 🔽 #task #proposed #auto

## Decisions

- Start VAST on GCP using local SSD-backed storage-serving VM shapes (Z4M path) for initial deployments due to latency advantages, and evaluate HyperDisk and object-tier approaches later for capacity and metadata offload.

- Coordinate in-person working sessions at Supercomputing and include additional Google Cloud stakeholders (Ilyas and Dean) to accelerate alignment on GSC integration, networking, and RDMA enablement.

- Use local SSD-backed storage-serving VMs (Z4M) as the initial approach for running VAST on Google Cloud due to latency requirements, and evaluate HyperDisk and object-tier options later.

- Coordinate in-person working sessions at Supercomputing and include key Google Cloud stakeholders (Ilyas and Dean) to accelerate alignment on GSC integration, networking, and RDMA enablement.

## Key Information

- Google Cloud launched Z3 as its first storage-optimized VM shape, optimized for compute workloads leveraging local storage, and it is a step toward storage-serving use cases due to higher storage and network density per VM.

- Google Cloud is developing Z4M as the next VM shape targeted at storage-serving workloads, increasing storage density and network density and aiming to match storage bandwidth to network bandwidth for storage-serving VMs.

- Google Cloud expects Z3 and Z4M to be overprovisioned on vCPU and memory for storage-serving use cases, and plans pricing optimization to make the cost model work despite overprovisioning.

- Google Cloud and VAST have been collaborating for 6-12 months to define the first-generation storage-serving VM requirements for VAST on GCP, following 18+ months of architecture discussions.

- The group discussed using local SSD initially for VAST on GCP due to lower latency compared to HyperDisk and object storage, with later evaluation of HyperDisk and object tiers for other parts of the system.

- Google Cloud is developing a Google Supercomputer (GSC) provisioning interface to co-provision and co-place storage VMs and accelerator or compute VMs for AI/ML and HPC workloads, rather than provisioning independently without placement awareness.

- Billy Kettler has been at Google since approximately mid-November 2020 (nearing five years as of 2025-10-31) and previously worked at Scality, Nexenta, and Dell, with a background in storage, backup, and disaster recovery across engineering and partner-facing roles.

- Jason Vallery worked at Microsoft for 13 years focused on Azure and joined VAST Data approximately two weeks before 2025-10-31; he has strong cloud and storage experience but is ramping on GCP specifics like Marketplace and VM instance types.

---

- Jason Vallery joined VAST Data after 13 years at Microsoft focused on Azure and cloud storage product management, and has less hands-on experience operating on Google Cloud Platform.

- An unknown Google Cloud participant has been at Google for nearly five years (as of 2025-10-31) and previously worked at Scality, Nexenta, and Dell in storage, backup, and disaster recovery roles.

- Google Cloud launched Z3 as its first storage-optimized VM, optimized for compute workloads leveraging local storage, and it is a step toward storage-serving use cases due to higher storage and network density per VM.

- Google Cloud is developing Z4M as the next storage-serving VM with increased storage density and network density, with a goal to better match storage bandwidth to network bandwidth for storage-serving workloads.

- Z3 and Z4M are overprovisioned on vCPU and memory for storage-serving use cases, and Google Cloud intends to optimize pricing to make these shapes cost-effective for storage-serving deployments even before right-sizing CPU and memory.

- Google Cloud is developing a Google Supercomputer (GSC) interface to provision storage VMs and accelerator/compute VMs with awareness of each other to improve co-placement and performance for AI/ML and HPC workloads.

- The group discussed that local SSD is the initial storage tier choice for VAST on GCP due to lower latency compared to HyperDisk and object storage.

- HyperDisk decouples capacity and performance but has higher latency than local SSD, making it a candidate for later tiers rather than the initial VAST on GCP deployment.

- Anywhere Cache can reduce intra-zone egress and operational cost but does not reduce object-store latency, so it helps economics more than performance for metadata-heavy paths.

- The group discussed offloading some VAST metadata to an object tier to improve economics, contingent on availability of a higher-performance, lower-latency object storage tier.

- Google Cloud supports erasure coding across availability domains and is targeting larger availability domain counts than the current baseline discussed (8).

- The group discussed planned RDMA enablement for Z4M and A5X GPU environments, including GPUDirect Storage support, with TPU RDMA expected later than GPU RDMA.

- Internal networking constructs such as internal load balancing (ILB) can create egress-like costs at very high throughput, which can materially impact the economics of partner storage solutions at multi-TB/s scale.

- VAST Data is preparing a Google Cloud Marketplace launch and is considering integration points with Google Vertex AI and TPU ecosystems.

- Customers commonly keep exabyte-scale data lakes in object storage and want mixed POSIX and S3 access patterns, which drives the need for hybrid object and file semantics in cloud deployments.

- Cross-region, cross-cloud, and neo-hyperscaler data movement economics (including egress) are a major constraint for VAST and joint customers at scale.
