---
type: "customer"
title: "Microsoft Apollo aligned on two-track evaluation for VAST AI cloud storage (Azure lab software validation + VAST hardware POC)"
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

# Microsoft Apollo aligned on two-track evaluation for VAST AI cloud storage (Azure lab software validation + VAST hardware POC)

**Date**: 2025-10-31
**Account**: [[]]
**Attendees**: Qingying Zhang, Yanzhao, Jason Wilder, Wendy, Anson (Qi), Paula, Jovane, Lior Genzel, Jason Vallery, Ray, Paul Haddo, Andy Prentice, Alon Horev

## Summary

Microsoft Apollo and VAST aligned on a two-track evaluation: (A) validate VAST software on Azure-native lab hardware and (B) run a VAST loaner-hardware POC in a Microsoft lab and/or Azure Dedicated. Apollo will provide lab hardware SKUs and precise performance KPIs for sizing, while VAST will provide rack/server specs, costs, and ship a minimal resilient POC kit. Discussion included Apollo’s scale targets (30-40 MW initial DC, eventual ~400k GPUs) and key architectural requirements like RoCE/RDMA and 400 GbE uplinks.


## Action Items


- [?] Share detailed VAST rack and server specifications (C-nodes, D-box/D-node, network uplinks) and estimated costs sized for an eventual ~400k GPU Apollo scale target and for an initial 30-40 MW data center site. @Lior Genzel 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Send the latest VAST hardware specifications, including updates referenced as AMD Turing-based changes and DPU details, for the Apollo evaluation. @Ray 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Provide proposed Azure lab hardware SKUs and specifications for the software-only POC (example mentioned: Gen9 storage pod with BlueField-3 DPU). @Yanzhao 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Confirm Microsoft Stargate lab readiness to host the VAST hardware POC, including rack space, approximately 30 kW power availability, air cooling, standard rack size, 400 GbE uplinks, and RoCE/RDMA enablement. @Yanzhao 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Provide VAST POC power specifications, rack size, connector types, and network uplink requirements for the Microsoft Stargate lab deployment. @Ray 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Ship a minimal VAST POC kit (approximately 3 C-nodes and 1 D-box, optionally preconfigured) to the Microsoft Stargate lab for the hardware POC track. @Ray 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Share the evaluation license and installation and operations guide for deploying VAST software on Azure lab hardware for the software-only POC track. @Lior Genzel 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Engage Anand Ramakrishna’s team to scope an Azure Dedicated path for earlier access to hardware for the VAST hardware POC and clarify timeline and logistics. @Qingying Zhang 📅 2025-11-08 #task #proposed #auto

- [?] Coordinate from the VAST side with Anand Ramakrishna’s team to align on Azure Dedicated POC logistics and timing for the Apollo evaluation. @Lior Genzel 📅 2025-11-08 #task #proposed #auto

- [?] Research and confirm precise KPI targets (per-GPU bandwidth, aggregate throughput, and capacity) with NVIDIA inputs and work with John Mao to build a sizing slide for the Apollo evaluation. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Validate that the Microsoft lab network configuration supports RoCE/RDMA and VLAN/SDN requirements for the single-tenant POC environment. @Jason Wilder 📅 2025-11-08 #task #proposed #auto

- [?] Share VAST reference design slides and materials discussed during the Apollo evaluation call. @Lior Genzel 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Arrange Microsoft Ignite introductions and confirm scheduling for a meeting between VAST CEO and Microsoft leadership, including Brendan Burns and a Microsoft VP/PM leader referenced as VPM. @Qingying Zhang 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Clarify DPU programming interface expectations for Apollo, including VAST’s current DOCA and NVMe-oF usage and compatibility considerations with a DASH API requirement. @Alon Horev 📅 2025-11-08 #task #proposed #auto

- [?] Confirm the minimal POC bill of materials and switch requirements if the POC does not use VAST-provided switching, including 400 GbE uplink needs and RoCE/RDMA enablement. @Ray 📅 2025-11-08 #task #proposed #auto

- [?] Confirm whether the VAST hardware POC will run in the Microsoft Stargate lab, Azure Dedicated, or both, and share the expected approval timeline and schedule. @Lior Genzel 📅 2025-11-08 #task #proposed #auto




## Decisions


- Proceed with a two-track evaluation for Microsoft Apollo storage: (A) validate VAST software on Azure-native lab hardware and (B) run a VAST loaner-hardware POC in a Microsoft lab and/or Azure Dedicated.

- Use RoCE/RDMA networking for the POC and require 400 GbE uplinks if VAST-provided switching is not used.

- Baseline the initial VAST POC footprint at approximately 3 C-nodes plus 1 D-box (dual BlueField DPUs), expandable as needed.

- Defer Azure LSv4 VM shapes for performance benchmarking and prioritize VAST-optimized hardware and/or an Azure Dedicated path for representative performance testing.

- Assume an initial single-tenant deployment model for Apollo with SDN readiness for future multi-tenancy.




## Key Information


- Microsoft Apollo is a new AI cloud being built separately from Microsoft Azure, based on Linux and Kubernetes.

- Microsoft Apollo’s initial operating model is single-tenant AI training, with inference workloads running between training windows; software-defined networking (SDN) is planned from day one to enable future multi-tenancy.

- Microsoft Apollo’s maturity scale target discussed was approximately 100k nodes and approximately 400k GPUs, with an initial data center target of 30-40 MW.

- Microsoft Apollo’s target launch timeframe discussed was September to November of the following year (relative to 2025-10-31).

- The evaluation approach is to compare VAST against alternatives such as Lustre and Azure Storage, ideally on the same hardware where possible.

- VAST’s architecture described uses C-nodes for compute, protocol, and erasure coding, and D-nodes for flash with DPUs and no x86 CPUs.

- VAST D-nodes use NVIDIA BlueField-3 DPUs and can expose NVMe-oF targets via NVIDIA DOCA; an alternative implementation path mentioned is SPDK on ARM.

- A minimal resilient VAST POC footprint discussed was approximately 3 C-nodes, 1 D-box (dual BlueField DPUs), and a pair of switches, requiring RoCE/RDMA and 400 GbE uplinks.

- Azure LSv4 VM shapes were considered insufficient for performance benchmarking; LSv5-like shapes were described as coming later, and Azure-qualified flash density may limit perf per watt and perf per PB versus VAST-optimized hardware.

- VAST stated it can ship loaner hardware within days and can preconfigure the POC; racks are standard and air-cooled.

- Anand Ramakrishna’s team was identified as a potential accelerator for an Azure Dedicated path to access hardware for the POC, similar to a prior UK Met Office engagement.

- Jason Vallery joined VAST Data as VP of Product Management for cloud offerings after 13 years at Microsoft, including work as a Group Product Manager for Azure Blob Storage and AI storage.

- Qingying Zhang is a Corporate Vice President in Azure and leads Azure Kubernetes Service (AKS) and cloud-native services, and is currently focused on the Apollo AI cloud project.

- Yanzhao is the Product Manager for the Apollo project at Microsoft.

- Jason Wilder previously ran AKS infrastructure and underlay work and is now working on the Apollo AI cloud project.

- Wendy previously worked on the AKS managed data plane and is now working on the Apollo AI cloud project.

- Jovane is part of Microsoft Corporate Business Development and covers HPC and AI infrastructure business.

- Ray is a VAST Data Field Technical Director focused on large opportunities and designs that must adhere to reference architectures.

- Paul Haddo is a VAST Data Systems Engineering Manager responsible for the pre-sales team in his region.

- Andy Prentice is the VAST Data Field CTO and participated in the Apollo evaluation discussion.



---

*Source: [[2025-10-31 - Teams aligned on a two-track evaluation for Apollo’s AI cloud storage (A) valid]]*