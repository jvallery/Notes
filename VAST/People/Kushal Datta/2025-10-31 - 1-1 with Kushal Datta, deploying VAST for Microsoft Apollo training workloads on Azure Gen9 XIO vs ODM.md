---
type: "people"
title: "1:1 with Kushal Datta, deploying VAST for Microsoft Apollo training workloads on Azure (Gen9 XIO vs ODM)"
date: "2025-10-31"
person: ""
participants: ["Jason Vallery", "Kushal Datta", "Glenn Lockwood", "Juergen Willis", "Jay Menon", "Girish", "Maneesh Sah", "Pradeep"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-31 - Jason (now at VAST) and Kushal discussed deploying VAST for Apollo’s training wo.md"
tags:
  - "type/people"
  - "person/"
  - "generated"

---

# 1:1 with Kushal Datta, deploying VAST for Microsoft Apollo training workloads on Azure (Gen9 XIO vs ODM)

**Date**: 2025-10-31
**With**: Jason Vallery, Kushal Datta, Glenn Lockwood, Juergen Willis, Jay Menon, Girish, Maneesh Sah, Pradeep

## Summary

Jason Vallery and Kushal Datta discussed options to deploy VAST Data for Microsoft Apollo training workloads on Azure, focusing on exabyte-scale storage with extreme read bandwidth and tight power and rack constraints. They aligned on pursuing an apples-to-apples evaluation on Azure Gen9 XIO hardware comparing the Azure Storage stack versus VAST running bare metal, while Kushal drafts crisp requirements and VAST prepares an ODM-based BOM option.


## Action Items


- [?] Draft and circulate a crisp requirements document for Microsoft Apollo storage selection including throughput, capacity, power budget, and rack tile constraints. @Kushal Datta 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Start an internal Microsoft thread to assess feasibility of swapping Dallas Blob HDD capacity to Premium SSD and feasibility of running VAST bare metal on Azure storage hardware. @Kushal Datta 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Provide detailed per-GPU read and write throughput targets and final capacity targets (per site and aggregate) for the approximately 120,000 GPU per site plan. @Kushal Datta 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Prepare a proposal and bill of materials for VAST-qualified ODM hardware options (performance-optimized vs capacity-optimized) once Microsoft Apollo requirements are received. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Support and advocate for an apples-to-apples test on Azure Gen9 XIO comparing the Azure Storage stack versus VAST running bare metal on the same hardware. @Kushal Datta 📅 2025-11-08 #task #proposed #auto

- [?] Stand up VAST running bare metal on Azure Gen9 XIO hardware for the A/B test when the evaluation is scheduled. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Determine the DPU and NIC path and qualification plan aligned with Azure networking requirements, including evaluation of Fungible versus NVIDIA BlueField and any overlay or multi-tenancy requirements. @TBD 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Confirm whether an Azure Blob-compatible API on VAST is required alongside NFS and S3 for existing Microsoft Apollo data loaders. @Kushal Datta 📅 2025-11-08 #task #proposed #auto

- [?] Scope and plan implementation of an Azure Blob-compatible API on VAST if Microsoft Apollo requires it for existing data loaders. @TBD 📅 2025-11-08 #task #proposed #auto

- [?] Clarify which Azure storage offerings and hardware configurations will be available in the January 2026 and April 2026 timeframes for the target Apollo sites (Dallas and the replacement for Richmond). @Kushal Datta 📅 2025-11-08 #task #proposed #auto

- [?] Schedule a follow-up meeting after the Microsoft Apollo requirements are finalized to align on evaluation plan and next steps. @Kushal Datta 📅 2025-11-08 🔽 #task #proposed #auto






## Key Information


- Jason Vallery moved from Microsoft Azure Storage to VAST Data and now leads cloud product management focused on hyperscaler penetration and marketplace offerings across AWS, Azure, and GCP.

- Juergen Willis was CVP of Microsoft Azure Storage until roughly 18 months before 2025-10-31 and then retired or was pushed out; his departure removed Jason Vallery's internal champion in Azure Storage.

- Glenn Lockwood previously worked closely with Jason Vallery at OpenAI and moved to VAST Data in July 2025.

- Kushal Datta is a member of Microsoft's Apollo team and is working with the Apollo storage-side team (including Jay Menon).

- Microsoft Apollo training storage requirements discussed include approximately 120,000 GPUs per site, approximately 1-2 TB/s peak write, approximately 24 TB/s read, and approximately 100 PB/day of checkpoint writes, with strict power and rack tile constraints.

- Dallas site storage capacity is expected to land in January 2026, and a larger capacity site is expected around April 2026; the previously planned Richmond site was removed and replaced by a larger capacity site.

- Azure compute-based storage SKUs (example referenced: LSP and future LSP5) are not viable for exabyte-scale storage due to poor compute-to-storage ratio, excessive rack count (example cited: ~1700 racks for ~1 EB usable) and high power draw (example cited: ~8 MW).

- A likely evaluation path is an apples-to-apples test on Azure Gen9 XIO hardware comparing the Azure Storage stack versus VAST running bare metal on the same hardware.

- VAST Data supports NFS, GPU Direct Storage (GDS), and S3 API, and can explore adding an Azure Blob-compatible API if required by existing data loaders.

- VAST Data architecture discussed uses C-nodes (compute and networking) and D-nodes (flash) with tunable ratios to optimize for performance versus capacity.

- Azure Gen9 XIO networking was described as using ConnectX-5 (CX5) NICs at approximately 40 Gbps, which may be a throughput bottleneck for Apollo-scale read bandwidth requirements.

- DPU and NIC options discussed include NVIDIA BlueField (BlueField-3 supported, BlueField-4 in progress) and Fungible, with qualification and overlay or multi-tenancy requirements as potential constraints.



---

*Source: [[2025-10-31 - Jason (now at VAST) and Kushal discussed deploying VAST for Apollo’s training wo]]*