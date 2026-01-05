---
type: "customer"
title: "GCP path for VAST on storage-serving VMs (Z4M), GSC co-placement, and RDMA/GPUDirect roadmap"
date: "2025-10-31"
account: ""
participants: ["Jason Vallery", "Billy Kettler", "John Downey", "Lior Genzel"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-31 - GCP outlined the path to run VAST on storage-serving VMs (Z4M) with higher stora.md"
tags:
  - "type/customer"
  - "account/"
  - "generated"

---

# GCP path for VAST on storage-serving VMs (Z4M), GSC co-placement, and RDMA/GPUDirect roadmap

**Date**: 2025-10-31
**Account**: [[]]
**Attendees**: Jason Vallery, Billy Kettler, John Downey, Lior Genzel

## Summary

Google Cloud outlined how VAST can run on upcoming storage-serving VM shapes (Z4M) with higher storage and network density, plus future co-placement via the Google Supercomputer (GSC) provisioning interface. The group aligned on starting with local SSD for latency, exploring HyperDisk and object-tier metadata offload later, and validating RDMA and GPUDirect Storage enablement for A5X GPUs (TPU RDMA later).


## Action Items


- [?] Draft and share a written list of networking questions and formal requests for Google Cloud (including Cloud WAN and internal load balancing or egress-like cost drivers) ahead of Supercomputing meetings. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Review the Google Cloud WAN material shared by Google Cloud and assess applicability to VAST multi-region and neo-hyperscaler data movement patterns. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Analyze performance and design implications of offloading VAST metadata to an object tier on Google Cloud, including latency sensitivity and required object tier characteristics. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Schedule Supercomputing in-person meetings between VAST and Google Cloud and attempt to include Google Cloud stakeholders Ilyas (cluster program) and Dean (CTO/expert). @John Downey 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Confirm RDMA and GPUDirect Storage enablement details and cost implications for Z4M storage-serving VMs and A5X GPU instances, and share the plan internally at VAST. @Billy Kettler 📅 2025-11-08 #task #proposed #auto

- [?] Engage Google Cloud networking and pricing stakeholders to explore commercial constructs that reduce internal networking and egress-like costs for partner storage-serving solutions at multi-TB/s throughput. @John Downey 📅 2025-11-08 ⏫ #task #proposed #auto




## Decisions


- Start VAST on GCP using local SSD-backed storage-serving VM shapes (Z4M path) for initial deployments due to latency advantages, and evaluate HyperDisk and object-tier approaches later for capacity and metadata offload.

- Coordinate in-person working sessions at Supercomputing and include additional Google Cloud stakeholders (Ilyas and Dean) to accelerate alignment on GSC integration, networking, and RDMA enablement.




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

*Source: [[2025-10-31 - GCP outlined the path to run VAST on storage-serving VMs (Z4M) with higher stora]]*