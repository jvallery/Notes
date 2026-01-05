---
type: "customer"
title: "Microsoft Apollo aligned on two-track evaluation for VAST AI cloud storage (Azure lab software validation + VAST loaner hardware POC)"
date: "2025-10-31"
account: ""
participants: ["Qingying Zhang", "Yanzhao", "Jason Wilder", "Wendy", "Anson (Qi)", "Paula", "Jovane", "Lior Genzel", "Jason Vallery", "Ray", "Paul Haddo", "Andy Prentice", "Alon Horev"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-31 - Teams aligned on a two-track evaluation for Apollo’s AI cloud storage (A) valid.md"
tags:
  - "type/customer"
  - "account/"
  - "generated"

---

# Microsoft Apollo aligned on two-track evaluation for VAST AI cloud storage (Azure lab software validation + VAST loaner hardware POC)

**Date**: 2025-10-31
**Account**: [[]]
**Attendees**: Qingying Zhang, Yanzhao, Jason Wilder, Wendy, Anson (Qi), Paula, Jovane, Lior Genzel, Jason Vallery, Ray, Paul Haddo, Andy Prentice, Alon Horev

## Summary

Microsoft Apollo and VAST Data aligned on a two-track evaluation: (A) validate VAST software on Azure-native lab hardware, and (B) run a VAST loaner-hardware POC in Microsoft’s Stargate lab and/or via an Azure dedicated path. VAST will provide rack/server specs, BOM and power/network requirements, ship a minimal resilient POC kit, and share install/ops guidance. Microsoft Apollo will provide lab hardware SKUs/specs and finalize performance KPIs needed for sizing, with a target Apollo launch window of Sep–Nov 2026 and initial datacenter sizing of 30–40 MW scaling toward ~400k GPUs.


## Action Items


- [?] Share VAST Data rack and server specifications (C-nodes, D-box/D-node, network uplinks) and estimated costs sized for an eventual ~400k GPU Apollo scale target and for an initial 30–40 MW datacenter site. @Lior Genzel 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Send the latest VAST Data hardware specifications including AMD Turin-based updates and DPU details for the Apollo evaluation. @Ray 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Provide proposed Azure lab hardware SKUs and specifications (example mentioned: Gen9 storage pod with BlueField-3 DPU) to be used for the software-only VAST-on-Azure-hardware POC. @Yanzhao 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Confirm Microsoft Stargate lab can host the VAST loaner-hardware POC, including rack space, approximately 30 kW power availability, air cooling, standard rack size, 400 GbE uplinks, and RoCE/RDMA enablement. @Yanzhao 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Provide POC power specifications, rack size, connector types, and network uplink requirements for the VAST loaner-hardware kit intended for Microsoft Stargate lab and/or Azure dedicated. @Ray 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Ship a minimal VAST loaner-hardware POC kit (approximately 3 C-nodes and 1 D-box, optionally preconfigured) to Microsoft’s Stargate lab for Apollo evaluation. @Ray 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Share the evaluation license and installation and operations guide for deploying VAST software on Microsoft Azure lab hardware for the software-only POC track. @Lior Genzel 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Engage Anand Ramakrishna to scope an Azure dedicated path for earlier access to a VAST hardware POC and clarify timeline and logistics. @Qingying Zhang 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Coordinate from the VAST side with Anand Ramakrishna’s team to align on Azure dedicated POC logistics and timing for the Apollo evaluation. @Lior Genzel 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Research and confirm precise AI storage KPI targets (per-GPU bandwidth, aggregate throughput, capacity) with NVIDIA inputs and work with John Mao to build a sizing slide for the Apollo evaluation. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Validate that the Microsoft lab network configuration supports RoCE/RDMA (SP3/SP4) and VLAN/SDN requirements for the single-tenant Apollo POC. @Jason Wilder 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Share VAST reference design slides and materials discussed during the call with the Microsoft Apollo team. @Lior Genzel 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Arrange Microsoft Ignite introductions and confirm scheduling for a meeting between VAST CEO and Microsoft leadership, including coordinating with Brendan Burns’ attendance. @Qingying Zhang 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Clarify DPU programming interface expectations for production, including VAST’s current DOCA and NVMe-oF usage and compatibility considerations with DASH API requirements from Microsoft Apollo. @Alon Horev 📅 2025-11-08 #task #proposed #auto

- [?] Confirm the minimal POC bill of materials and any switch requirements if the POC does not use VAST-provided switching. @Ray 📅 2025-11-08 #task #proposed #auto

- [?] Confirm whether the VAST hardware POC will run in Microsoft Stargate lab, Azure dedicated, or both, and share the expected approval timeline and execution plan. @Lior Genzel 📅 2025-11-08 #task #proposed #auto




## Decisions


- Microsoft Apollo and VAST Data will proceed with a two-track evaluation: (A) validate VAST software on Azure-native lab hardware, and (B) run a VAST loaner-hardware POC in Microsoft’s Stargate lab and/or via an Azure dedicated path.

- Microsoft Apollo’s initial deployment model will be single-tenant, with SDN planned from day one to support future multi-tenancy.

- The POC will use RoCE/RDMA networking, and 400 GbE uplinks are required if VAST-provided switching is not used.

- The baseline POC footprint will start at approximately 3 VAST C-nodes plus 1 VAST D-box (dual BlueFields), expandable as needed.

- Azure LSv4 VM shapes will be deferred for performance testing; the evaluation will instead prioritize VAST-optimized hardware and/or an Azure dedicated hardware path for representative benchmarking.




## Key Information


- Microsoft Apollo is a new AI cloud being built separately from Microsoft Azure, based on Linux and Kubernetes.

- Microsoft Apollo’s initial operational model is single-tenant AI training, with inference workloads running between training windows, and SDN planned from day one to enable future multi-tenancy.

- Microsoft Apollo’s maturity scale target discussed was approximately 100k nodes, equating to roughly 400k GPUs, with an initial datacenter target of 30–40 MW.

- Microsoft Apollo’s target launch timeframe discussed was Sep–Nov 2026 (next year relative to 2025-10-31).

- The evaluation approach is to compare VAST Data against alternatives such as Lustre and Azure Storage, using the same hardware where possible to isolate software differences.

- VAST Data architecture described uses C-nodes for compute, protocol and erasure coding, and D-nodes (D-box) for flash with DPUs and no x86 CPUs.

- VAST Data D-nodes use NVIDIA BlueField-3 DPUs and can expose NVMe-oF targets via NVIDIA DOCA, with an alternative option to use SPDK on ARM.

- A minimal resilient VAST Data POC footprint discussed was approximately 3 C-nodes, 1 D-box (dual BlueFields), plus a pair of switches, requiring RoCE/RDMA and 400 GbE uplinks if VAST switching is not used.

- Azure LSv4 VM shapes were called out as insufficient for performance benchmarking; LSv5-like shapes were described as coming later, and Azure-qualified flash density may limit perf per watt and perf per PB compared to VAST-optimized hardware.

- VAST Data indicated it can ship standard air-cooled loaner hardware within days and can preconfigure the POC kit before shipment.

- Anand Ramakrishna’s team was identified as a potential accelerator for an Azure dedicated path to access hardware POC capacity, similar to a prior UK Met Office engagement.

- Jason Vallery stated he joined VAST Data a couple weeks prior to 2025-10-31 as VP of Product Management for cloud offerings and previously spent 13 years at Microsoft as a Group Product Manager for Azure Blob/object storage with focus on AI storage.

- Qingying Zhang stated she is a Corporate Vice President in Azure, previously leading Azure Kubernetes Service and cloud-native services, and is now focused on the Apollo AI cloud project.

- Yanzhao stated he is the Apollo Product Manager working with Qingying Zhang.

- Jason Wilder stated he previously ran AKS infrastructure and underlay work and is now working on the Apollo project in similar areas.

- Jovane stated he is part of Microsoft Corporate Business Development covering HPC and AI infrastructure business.



---

*Source: [[2025-10-31 - Teams aligned on a two-track evaluation for Apollo’s AI cloud storage (A) valid]]*