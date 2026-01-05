---
type: "customer"
title: "Microsoft and VAST align parallel tracks: UK Met Azure LSV4 test cluster and Microsoft-hosted bare-metal dev system"
date: "2025-10-29"
account: ""
participants: ["Jason Vallery", "Jonsi Stephenson", "Leo", "Mike", "James", "Nico", "Eirikur Hrafnsson", "Trevor", "Tiff"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-29 - Teams aligned to run two tracks in parallel an Azure LSV4 test cluster for UK M.md"
tags:
  - "type/customer"
  - "account/"
  - "generated"

---

# Microsoft and VAST align parallel tracks: UK Met Azure LSV4 test cluster and Microsoft-hosted bare-metal dev system

**Date**: 2025-10-29
**Account**: [[]]
**Attendees**: Jason Vallery, Jonsi Stephenson, Leo, Mike, James, Nico, Eirikur Hrafnsson, Trevor, Tiff

## Summary

VAST and Microsoft aligned to run two tracks in parallel: an Azure LSV4-based VAST test cluster for UK Met in early December 2025 and a potential Microsoft-hosted bare-metal VAST dev system via Anand’s organization. The group discussed VM SKU availability (LS96 vs LS192), RDMA enablement timelines, region constraints, and procurement blockers including internal Microsoft inability to buy VAST software via Azure Marketplace.


## Action Items


- [?] Review and approve the shared VAST configuration and drive internal approval plus expedited shipping, installation, deployment, and QA readiness for the Microsoft-hosted bare-metal VAST system path. @Leo 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Connect Nico with Ronnie Booker to align Azure VM type, target region, and VM availability to meet early December 2025 readiness for the UK Met LSV4 test cluster. @Leo 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Coordinate Azure VM choice (LS96 vs LS192) and select a target Azure region for the December 2025 UK Met test cluster, accounting for regional capacity constraints. @Nico 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Deliver an 8-node LSV4-based VAST test system in UK Met’s Azure tenant by early December 2025, with flexibility to use LS96 if LS192 is unavailable. @Leo 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Prepare Azure demos for Supercomputing and Ignite during the week of 2025-11-17. @Leo 📅 2025-11-17 ⏫ #task #proposed #auto

- [?] Confirm mid-November 2025 commitment on the EGAL and Azure Compute platform timeline and capacity by pinging Sara (Microsoft contact, last name not provided). @Tiff 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Follow up with Microsoft PM to confirm RDMA timelines and scope, including VM-to-VM, GPU-to-VAST, east-west vs north-south traffic, and VNet and MTU limits. @Nico 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Set up a separate engineering workshop for Polaris, Lifter, and data-plane integration to ensure full API exposure and automation parity for Azure Native management. @James 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Build and share a bill of materials (BOM) for the Microsoft-hosted bare-metal VAST dev system option. @James 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Discuss with Anand’s organization the data center location, ownership model, and procurement approach for the bare-metal dev system, and provide an answer by Supercomputing week (2025-11-17). @Mike 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Open the terms, commercials, and KPI discussion for the UK Met effort and involve John (last name not provided). @Claire 📅 2025-11-08 #task #proposed #auto

- [?] Provide ranked OEM preferences for secure supply (for example HPE and alternatives) to support procurement planning for the bare-metal dev system. @TBD 📅 2025-11-08 #task #proposed #auto

- [?] Engage Ed Kim to align the procurement path and approved OEM list for the bare-metal dev system hardware acquisition. @James 📅 2025-11-08 #task #proposed #auto

- [?] Draft a GPFS replacement or swap design for the Gen1 Slingshot path, including risks, performance expectations, and approval needs, coordinating with Trevor. @Trevor 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Share Azure Compute status on NVMe persistence and dedicated hosts feasibility for L-series and LSV5 to support UK Met design decisions. @Leo 📅 2025-11-08 #task #proposed #auto

- [?] Define a non-Marketplace procurement route for internal Microsoft to obtain VAST software subscriptions. @James 📅 2025-11-08 ⏫ #task #proposed #auto




## Decisions


- Pursue two parallel paths for UK Met validation: (1) an Azure LSV4-based VAST test cluster in UK Met’s Azure tenant and (2) a Microsoft-hosted bare-metal VAST dev system via Anand’s organization.

- Target early December 2025 for UK Met to begin testing VAST on Azure LSV4.

- Proceed with LS96 where LS192 is not available, and support both SKUs where possible to avoid region-based blocking.

- Treat Slingshot integration as a separate track and prioritize Azure Ethernet integration to Azure Compute for the main path.

- Engage UK Met as a design partner for Polaris and Lifter with emphasis on full API exposure and automation.

- Maintain a single weekly sync until testing begins, then split into separate engineering and business tracks.




## Key Information


- Jonsi Stephenson is the GM of Cloud at VAST Data and previously served as Global CTO and GM of cloud storage at NetApp, where he helped build Azure NetApp Files (ANF).

- Eirikur Hrafnsson is the VP of Engineering for cloud engineering at VAST Data and is described as a co-founder at Green Cloud.

- Azure LSV4 full VM availability slipped by approximately two weeks, moving UK Met test readiness to early December 2025.

- LS96 provides approximately 40 Gbps networking, while LS192 targets approximately 200 Gbps, but LS192 availability varies by Azure region.

- UK Met Gen1 environment uses HPE Cray with GPFS and Slingshot; Gen2 must be hosted in the UK with dedicated facilities and network constraints.

- UK Met performance requirement includes symmetric I/O of 1 TB/s read and 1 TB/s write simultaneously on large file systems.

- UK Met small-files tier target is approximately 1 PB at approximately 25 GB/s bidirectional throughput with additional metadata performance validation (MDTest).

- Azure is planning RDMA enablement for VM-to-VM traffic; applicability to LSV4 and LSV5 was discussed as under review, including VNet and MTU constraints.

- The primary integration target is Azure Ethernet to Azure Compute; Slingshot integration is treated as a separate exercise.

- VAST Polaris and Lifter path targets an Azure Native Resource Provider (RP) plus an Azure Marketplace offer with full API exposure and automation parity.

- Internal Microsoft teams cannot procure software via Azure Marketplace, requiring a non-Marketplace procurement route for VAST software subscriptions.

- Ed Kim is the procurement contact for OEM hardware; HPE was discussed as the likely path of least resistance, with alternatives under review.

- Testing region for benchmarking may be East US 2 due to H-series capacity, but final region selection was not decided.



---

*Source: [[2025-10-29 - Teams aligned to run two tracks in parallel an Azure LSV4 test cluster for UK M]]*