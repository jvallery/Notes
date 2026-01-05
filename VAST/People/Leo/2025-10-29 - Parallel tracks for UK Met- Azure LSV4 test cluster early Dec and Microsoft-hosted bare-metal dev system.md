---
type: "customer"
title: "Parallel tracks for UK Met: Azure LSV4 test cluster (early Dec) and Microsoft-hosted bare-metal dev system"
date: "2025-10-29"
account: ""
participants: ["Leo", "Mike", "James", "Nico", "Jason Vallery", "Jonsi Stephenson", "Eiki", "Trevor", "Tiff"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-29 - Teams aligned to run two tracks in parallel an Azure LSV4 test cluster for UK M.md"
tags:
  - "type/customer"
  - "account/"
  - "generated"

---

# Parallel tracks for UK Met: Azure LSV4 test cluster (early Dec) and Microsoft-hosted bare-metal dev system

**Date**: 2025-10-29
**Account**: [[]]
**Attendees**: Leo, Mike, James, Nico, Jason Vallery, Jonsi Stephenson, Eiki, Trevor, Tiff

## Summary

The group aligned to run two parallel tracks: deliver an 8-node VAST test system on Azure LSV4 in the UK Met Office tenant in early December 2025, and in parallel pursue a Microsoft-hosted bare-metal VAST dev system via Anand’s organization. Discussion covered LSV4 VM availability (LS96 vs LS192), RDMA enablement timelines, region constraints, procurement constraints for internal Microsoft (non-Marketplace software), and deeper engineering engagement on Polaris/Lifter for full Azure Native API exposure and automation.


## Action Items


- [?] Review and approve the shared VAST configuration and drive internal approval plus expedited shipping, installation, deployment, and QA readiness for the Microsoft-hosted bare-metal VAST system path. @Leo 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Connect Nico with Roni to align VM type, region, and availability to ensure December 2025 readiness for the UK Met Office Azure LSV4 test cluster. @Leo 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Coordinate VM choice (LS96 vs LS192) and target Azure region for the December 2025 UK Met Office test cluster, including confirming LS192 regional availability versus H-series capacity constraints. @Nico 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Deliver an 8-node LSV4-based VAST test system in the UK Met Office Azure tenant by early December 2025. @Leo 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Prepare Azure demos for Supercomputing and Microsoft Ignite during the week of 2025-11-17. @Leo 📅 2025-11-17 ⏫ #task #proposed #auto

- [?] Ping Sara to confirm mid-November 2025 commitment on the EGAL/compute platform timeline and capacity for L-series/LSV4 readiness. @Tiff 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Follow up with Microsoft PM to confirm RDMA timelines and scope, including VM-to-VM, GPU-to-VAST, east-west versus north-south, and VNet/MTU limits. @Nico 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Set up a separate engineering track or workshop for Polaris/Lifter and data-plane integration with VAST, Azure, and UK Met Office teams. @James 📅 2025-11-08 #task #proposed #auto

- [?] Build and share a bill of materials (BOM) for the Microsoft-hosted bare-metal VAST dev system. @James 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Discuss with Anand’s organization the data center location, ownership model, and purchase decision for the bare-metal dev system, aiming for an answer by Supercomputing week of 2025-11-17. @Mike 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Open the T&Cs, commercials, and KPIs discussion for the UK Met Office engagement and involve John. @Claire 📅 2025-11-08 #task #proposed #auto

- [?] Provide ranked OEM preferences for secure supply (for example HPE and alternatives) for the bare-metal VAST system procurement path. @TBD 📅 2025-11-08 #task #proposed #auto

- [?] Engage Ed Kim to align the procurement path and confirm the approved OEM list for the bare-metal VAST system. @James 📅 2025-11-08 #task #proposed #auto

- [?] Draft a GPFS swap design for the Gen1 Slingshot path, including risks, performance expectations, and approval needs, coordinating with Trevor. @Trevor 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Share Microsoft compute status on NVMe persistence and dedicated hosts feasibility for L-series and LSV5 for UK Met Office requirements. @Leo 📅 2025-11-08 #task #proposed #auto

- [?] Define the non-Marketplace software procurement route for internal Microsoft subscriptions to VAST software. @James 📅 2025-11-08 ⏫ #task #proposed #auto




## Decisions


- Pursue two tracks in parallel: (1) an Azure LSV4-based VAST test cluster for UK Met Office and (2) a Microsoft-hosted bare-metal VAST dev system via Anand’s organization.

- Target early December 2025 for UK Met Office to begin testing VAST in their Azure tenant using an 8-node LSV4-based test system.

- Proceed with LS96 where LS192 is not available, and support both SKUs where possible to avoid region availability blocking testing.

- Treat Slingshot integration as a separate track and prioritize Azure Ethernet integration for the main Azure path.

- Engage UK Met Office as a design partner for Polaris/Lifter with emphasis on full API exposure and automation.

- Maintain a single weekly sync until testing begins, then split into separate engineering and business tracks.




## Key Information


- Jonsi Stephenson is the GM of Cloud for VAST Data and previously served as Global CTO and GM of cloud storage at NetApp, where he helped build Azure NetApp Files (ANF).

- Eiki is the VP of Engineering for Cloud Engineering at VAST Data and is described as a co-founder at Green Cloud.

- Azure LSV4 full VM availability slipped by approximately two weeks, moving UK Met Office test readiness to early December 2025.

- LS96 provides approximately 40 Gbps networking, while LS192 targets approximately 200 Gbps, but LS192 availability varies by Azure region.

- UK Met Office Gen1 environment uses HPE Cray with GPFS and Slingshot; Gen2 must be hosted in the UK with dedicated facilities and network.

- UK Met Office has a symmetric I/O requirement of 1 TB/s read and 1 TB/s write simultaneously on large file systems.

- UK Met Office small-files tier target is approximately 1 PB at approximately 25 GB/s bidirectional, with additional metadata performance validation (MDTest).

- Azure LSV5 AMP is expected to be tested in Q1 2026 with production in Q2 2026, and Azure compute is considering a higher-density SKU targeting up to 800 Gbps and approximately 300 TB NVMe.

- Azure is planning RDMA enablement for VM-to-VM traffic; applicability to LSV4 and LSV5 was under review, including VNet and MTU constraints.

- The primary integration target is Azure Ethernet to Azure Compute; Slingshot integration is treated as a separate effort.

- VAST Polaris and Lifter path targets an Azure Native Resource Provider (RP) plus an Azure Marketplace offer with full API exposure and automation parity with Azure UI.

- Internal Microsoft teams cannot procure software via Azure Marketplace, requiring an alternate non-Marketplace procurement route for VAST software subscriptions.

- Ed Kim is the procurement contact for OEM hardware; HPE was described as the likely path of least resistance, with alternatives under review.

- East US 2 was discussed as a potential test region due to H-series capacity, but the final region for benchmarking and the December test cluster was still TBD.

- Leo reached out to Anand to pursue a Microsoft-hosted VAST hardware deployment in Anand’s data center as a plan B that could become plan A for production success, with UK Met Office as first priority by timeline.



---

*Source: [[2025-10-29 - Teams aligned to run two tracks in parallel an Azure LSV4 test cluster for UK M]]*