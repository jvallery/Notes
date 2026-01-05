---
type: "people"
title: "1:1 with Kushal Datta: VAST deployment options for Microsoft Apollo training storage on Azure Gen9 XIO vs ODM"
date: "2025-10-31"
person: ""
participants: ["Jason Vallery", "Kushal Datta"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-31 - Jason (now at VAST) and Kushal discussed deploying VAST for Apollo’s training wo.md"
tags:
  - "type/people"
  - "person/"
  - "generated"

---

# 1:1 with Kushal Datta: VAST deployment options for Microsoft Apollo training storage on Azure Gen9 XIO vs ODM

**Date**: 2025-10-31
**With**: Jason Vallery, Kushal Datta

## Summary

Jason Vallery and Kushal Datta discussed how to meet Microsoft Apollo training workload storage requirements on Azure, comparing Azure compute-based storage SKUs, running VAST bare metal on Azure Gen9 Blob/XIO hardware, and deploying VAST-qualified ODM hardware. Kushal shared exabyte-scale requirements with extreme read bandwidth needs and tight power and rack constraints, and they aligned on an apples-to-apples test of Azure Storage stack vs VAST bare metal on Gen9 XIO.


## Action Items


- [?] Draft and circulate a crisp requirements document for Microsoft Apollo storage (throughput, capacity, power budget, rack tile constraints) to drive storage selection and SKU design. @Kushal Datta 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Start an internal Microsoft thread to assess feasibility and timing to swap Dallas Blob storage from HDD to Premium SSD and to validate whether VAST can run bare metal on the target Azure storage hardware. @Kushal Datta 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Provide detailed per-GPU read and write throughput targets and final capacity targets (per site and aggregate) for the ~120,000 GPU per site Apollo design point. @Kushal Datta 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Prepare a proposal and bill of materials for VAST-qualified ODM hardware options (performance-optimized vs capacity-optimized) once Apollo requirements are received. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Support and advocate for an apples-to-apples test on Azure Gen9 XIO hardware comparing Azure Storage stack versus VAST running bare metal. @Kushal Datta 📅 2025-11-08 #task #proposed #auto

- [?] Stand up VAST running bare metal on Azure Gen9 XIO hardware for the A/B test when the test window is scheduled and hardware access is confirmed. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Determine the DPU and NIC path and qualification plan (Fungible NIC vs NVIDIA BlueField) aligned with Azure networking requirements for running VAST on Azure storage hardware. @TBD 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Confirm whether an Azure Blob-compatible API on VAST is required alongside NFS and S3 for Apollo data loaders and workflows. @Kushal Datta 📅 2025-11-08 #task #proposed #auto

- [?] Scope and plan engineering work to support an Azure Blob-compatible API on VAST if Apollo requires it for existing data loaders. @TBD 📅 2025-11-08 #task #proposed #auto

- [?] Clarify which Azure storage offerings and hardware configurations will be available in the January 2026 and April 2026 timeframes for the target Apollo sites (Dallas and the replacement for Richmond). @Kushal Datta 📅 2025-11-08 #task #proposed #auto

- [?] Schedule a follow-up meeting after Apollo requirements are finalized to review deployment approach and test plan. @Kushal Datta 📅 2025-11-08 🔽 #task #proposed #auto




## Decisions


- No formal decision was made, but Jason Vallery and Kushal Datta aligned to pursue an apples-to-apples evaluation on Azure Gen9 XIO hardware comparing Azure Storage stack versus VAST running bare metal.




## Key Information


- Jason Vallery moved from Microsoft Azure Storage to VAST Data to lead cloud product management focused on hyperscaler penetration and marketplace offerings across AWS, Azure, and GCP.

- Kushal Datta is a member of Microsoft's Apollo team.

- Kushal Datta reported that the Falcon 1 capacity was delivered and is being used, and that model training has started on that capacity.

- Kushal Datta described Apollo target scale per site as approximately 120,000 GPUs and approximately 1 exabyte usable capacity, with potential discussion of much larger sites (up to ~350 MW) implying multi-exabyte capacity.

- Kushal Datta stated Apollo checkpointing could be approximately 100 PB/day, with peak write throughput needs around 1-2 TB/s and read throughput needs around 24 TB/s.

- Kushal Datta stated Dallas storage capacity (HDD-based) is expected to land in January 2026, and a larger capacity site is expected around April 2026; Richmond was removed and replaced by a larger capacity site.

- Jason Vallery stated Azure compute-based storage-dense SKUs (for example LSP and future LSP5) are not viable for exabyte-scale storage due to poor compute-to-storage ratio, rack count, and power inefficiency.

- Jason Vallery stated VAST can deploy on VAST-qualified ODM hardware using a C-node (compute/network) and D-node (flash) architecture with tunable ratios to optimize for performance or capacity.

- Jason Vallery stated VAST supports NFS, GPU Direct Storage (GDS), and S3 API, and VAST could add an Azure Blob-compatible API if required by existing data loaders.

- The planned evaluation approach discussed was an apples-to-apples test on Azure Gen9 XIO hardware comparing the Azure Storage software stack versus VAST running bare metal on the same hardware.

- Jason Vallery referenced that Juergen Willis was his prior champion and sponsor in Azure Storage and that leadership changes reduced his ability to drive initiatives inside Azure Storage.

- Jason Vallery stated Glenn Lockwood previously worked with him at OpenAI, moved to VAST Data in July 2025, and that influenced Jason's move to VAST Data.



---

*Source: [[2025-10-31 - Jason (now at VAST) and Kushal discussed deploying VAST for Apollo’s training wo]]*