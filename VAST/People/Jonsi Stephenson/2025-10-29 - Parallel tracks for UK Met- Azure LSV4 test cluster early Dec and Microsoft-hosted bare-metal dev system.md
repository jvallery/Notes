---
type: "customer"
title: "Parallel tracks for UK Met: Azure LSV4 test cluster (early Dec) and Microsoft-hosted bare-metal dev system"
date: "2025-10-29"
account: ""
participants: ["Jason Vallery", "Jonsi Stephenson", "James", "Leo", "Mike", "Nico", "Eirikur Hrafnsson", "Trevor", "Tiff", "Anand", "Roni", "Ed Kim", "Sara", "Claire", "John"]
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
**Attendees**: Jason Vallery, Jonsi Stephenson, James, Leo, Mike, Nico, Eirikur Hrafnsson, Trevor, Tiff, Anand, Roni, Ed Kim, Sara, Claire, John

## Summary

The team aligned to run two parallel tracks: an Azure LSV4-based VAST test cluster in the UK Met tenant targeted for early December 2025, and a potential Microsoft-hosted bare-metal VAST dev system via Anand’s organization. Key discussion areas were LSV4 VM availability (LS96 vs LS192), RDMA enablement timelines and constraints, region placement, and procurement constraints including internal Microsoft inability to transact via Azure Marketplace.


## Action Items


- [?] Review and approve the shared VAST configuration and drive expedited shipping, installation, deployment, and QA readiness for the Microsoft-hosted bare-metal VAST dev system path. @Leo 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Connect Nico with Roni to align Azure VM type, region, and availability to meet early December 2025 readiness for the UK Met Azure LSV4 test cluster. @Leo 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Coordinate Azure VM choice (LS96 vs LS192) and select the target Azure region for the early December 2025 UK Met LSV4 test cluster, including confirming LS192 regional availability versus H-series capacity constraints. @Nico 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Deliver an 8-node Azure LSV4-based VAST test system in the UK Met tenant by early December 2025, including readiness validation for benchmarking and customer testing. @Leo 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Prepare Azure demos for Supercomputing and Microsoft Ignite during the week of 2025-11-17, aligned to the UK Met and Azure L-series narrative. @Leo 📅 2025-11-17 ⏫ #task #proposed #auto

- [?] Ping Sara to confirm the mid-November 2025 commitment on the EGAL and Azure compute platform timeline and capacity relevant to LSV4 and LSV5 readiness. @Tiff 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Follow up with the Azure PM team on RDMA timelines and scope, including VM-to-VM, GPU-to-VAST, east-west versus north-south traffic, and VNet/MTU limits for LSV4 and LSV5. @Nico 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Set up a separate engineering workshop for Polaris and Lifter plus data-plane integration, focused on full API exposure, automation, and Azure Native API and UI parity. @James 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Build and share a bill of materials (BOM) for the Microsoft-hosted bare-metal VAST dev system path and circulate for internal approval and procurement planning. @James 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Discuss with Anand the Microsoft data center location, ownership model, and purchase approach for the bare-metal VAST dev system, and provide an answer by Supercomputing week (2025-11-17). @Mike 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Open the terms, commercials, and KPI discussion for the UK Met engagement and involve John in the commercial workstream. @Claire 📅 2025-11-08 #task #proposed #auto

- [?] Provide ranked OEM preferences for secure supply (for example HPE and alternatives) to support procurement planning for the bare-metal VAST dev system. @TBD 📅 2025-11-08 #task #proposed #auto

- [?] Engage Ed Kim to align the procurement path and approved OEM list for the bare-metal VAST dev system hardware acquisition. @James 📅 2025-11-08 #task #proposed #auto

- [?] Draft a GPFS swap design for the Gen1 Slingshot path, including risks, performance expectations, and required approvals, coordinating with Trevor. @Trevor 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Share Azure compute status on NVMe persistence and dedicated hosts feasibility for L-series and LSV5, including implications for UK Met designs. @Leo 📅 2025-11-08 #task #proposed #auto

- [?] Define a non-Marketplace software procurement route for internal Microsoft use of VAST software subscriptions and document the process for the program team. @James 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Confirm MTU settings and any VNet crossing limitations relevant to RDMA scenarios for LSV4 and LSV5 testing and production planning. @Nico 📅 2025-11-08 #task #proposed #auto

- [?] Align on Slingshot integration approach (Ethernet gateways versus direct connect) and identify approvals needed for any Slingshot-related workstream. @Trevor 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Collect and share required switch and hardware API details needed to automate OEM deployments for the bare-metal VAST dev system path. @James 📅 2025-11-08 #task #proposed #auto




## Decisions


- Pursue two parallel tracks: (1) an Azure LSV4-based VAST test cluster for UK Met and (2) a Microsoft-hosted bare-metal VAST dev system via Anand’s organization.

- Target early December 2025 for UK Met to begin testing VAST on Azure LSV4 in the UK Met tenant.

- Proceed with LS96 where LS192 is not available, and support both SKUs where possible to avoid region availability blocking testing.

- Treat Slingshot integration as a separate track and prioritize Azure Ethernet integration for the main Azure path.

- Engage UK Met as a design partner for Polaris and Lifter with emphasis on full API exposure, automation, and Azure Native API and UI parity.

- Maintain a single weekly sync until testing begins, then split into separate engineering and business tracks.




## Key Information


- Jonsi Stephenson is the GM of Cloud at VAST Data and previously served as global CTO and GM of cloud storage at NetApp, where he helped build Azure NetApp Files (ANF).

- Eiki (full name not provided) is the VP of Engineering for cloud engineering at VAST Data and is described as a co-founder at Green Cloud with Jonsi Stephenson.

- Azure LSV4 full VM availability slipped by approximately two weeks, moving UK Met test readiness to early December 2025.

- LS96 provides approximately 40 Gbps networking, while LS192 targets approximately 200 Gbps, but LS192 availability varies by Azure region.

- UK Met Gen1 environment uses HPE Cray with GPFS and Slingshot networking, and Gen2 must be hosted in the UK with dedicated facilities and network reservations.

- UK Met performance requirements include symmetric I/O of 1 TB/s read and 1 TB/s write simultaneously on large file systems.

- UK Met small-files tier target is approximately 1 PB at approximately 25 GB/s bidirectional, with additional metadata performance validated via MDTest.

- Azure LSV5 AMP is expected to be tested in Q1 2026 and targeted for production in Q2 2026, and Azure compute is considering a higher-density SKU up to approximately 800 Gbps with approximately 300 TB NVMe.

- Azure is planning RDMA enablement for VM-to-VM traffic, and applicability to LSV4 and LSV5 is under review including VNet and MTU constraints.

- The primary integration target is Azure Ethernet to Azure Compute, while Slingshot integration is treated as a separate effort.

- The VAST Polaris and Lifter approach targets an Azure Native Resource Provider (RP) plus an Azure Marketplace offer with full API exposure and automation parity.

- Internal Microsoft teams cannot procure software via Azure Marketplace, requiring an alternate non-Marketplace procurement route for VAST software subscriptions.

- Ed Kim is the procurement contact for OEM hardware, and HPE is considered the path of least resistance while alternatives are under review.

- A likely test region discussed was East US 2 due to H-series capacity, but the final region for the December 2025 test cluster was not decided.

- Leo reached out to Anand to pursue a Microsoft-hosted bare-metal VAST hardware path in Anand’s data center as a plan B that could become plan A for production success.



---

*Source: [[2025-10-29 - Teams aligned to run two tracks in parallel an Azure LSV4 test cluster for UK M]]*