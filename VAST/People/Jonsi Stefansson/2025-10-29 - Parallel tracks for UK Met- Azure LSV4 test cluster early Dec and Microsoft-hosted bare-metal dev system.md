---
type: people
title: 'Parallel tracks for UK Met: Azure LSV4 test cluster (early Dec) and Microsoft-hosted bare-metal dev system'
date: '2025-10-29'
participants:
- Jason Vallery
- Jonsi Stephenson
- Leo
- Mike
- James
- Nico
- Eirikur Hrafnsson
- Trevor
- Tiff
- Anand
- Roni
- Ed Kim
- Sara
- Claire
- John
- Eiki
source: transcript
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-29 - Teams aligned to run two tracks in parallel an Azure LSV4 test cluster for UK M.md
tags:
- type/people
- generated
person: Jonsi Stefansson
---

# Parallel tracks for UK Met: Azure LSV4 test cluster (early Dec) and Microsoft-hosted bare-metal dev system

**Date**: 2025-10-29
**Attendees**: Jason Vallery, Jonsi Stephenson, James, Leo, Mike, Nico, Eirikur Hrafnsson, Trevor, Tiff, Anand, Roni, Ed Kim, Sara, Claire, John

## Summary

The group aligned to run two parallel tracks: deliver an 8-node VAST test system on Azure LSV4 in the UK Met Office tenant in early December 2025, and in parallel pursue a Microsoft-hosted bare-metal VAST dev system via Anand’s organization. Discussion covered LSV4 VM availability (LS96 vs LS192), RDMA enablement timelines, region constraints, procurement constraints for internal Microsoft (non-Marketplace software), and deeper engineering engagement on Polaris/Lifter for full Azure Native API exposure and automation.

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

- Pursue two parallel paths for UK Met validation: (1) an Azure LSV4-based VAST test cluster in UK Met’s Azure tenant and (2) a Microsoft-hosted bare-metal VAST dev system via Anand’s organization.

- Target early December 2025 for UK Met to begin testing VAST on Azure LSV4.

- Proceed with LS96 where LS192 is not available, and support both SKUs where possible to avoid region-based blocking.

- Treat Slingshot integration as a separate track and prioritize Azure Ethernet integration to Azure Compute for the main path.

- Engage UK Met as a design partner for Polaris and Lifter with emphasis on full API exposure and automation.

- Maintain a single weekly sync until testing begins, then split into separate engineering and business tracks.

- Pursue two parallel tracks: (1) an Azure LSV4-based VAST test cluster for UK Met and (2) a Microsoft-hosted bare-metal VAST dev system via Anand’s organization.

- Target early December 2025 for UK Met to begin testing VAST on Azure LSV4 in the UK Met tenant.

- Proceed with LS96 where LS192 is not available, and support both SKUs where possible to avoid region availability blocking testing.

- Treat Slingshot integration as a separate track and prioritize Azure Ethernet integration for the main Azure path.

- Engage UK Met as a design partner for Polaris and Lifter with emphasis on full API exposure, automation, and Azure Native API and UI parity.

- Pursue two tracks in parallel: (1) an Azure LSV4-based VAST test cluster for UK Met Office and (2) a Microsoft-hosted bare-metal VAST dev system via Anand’s organization.

- Target early December 2025 for UK Met Office to begin testing VAST in their Azure tenant using an 8-node LSV4-based test system.

- Engage UK Met Office as a design partner for Polaris/Lifter with emphasis on full API exposure and automation.

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

- Eiki (full name not provided) is the VP of Engineering for cloud engineering at VAST Data and is described as a co-founder at Green Cloud with Jonsi Stephenson.

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

- Jonsi Stephenson is the GM of Cloud for VAST Data and previously served as Global CTO and GM of cloud storage at NetApp, where he helped build Azure NetApp Files (ANF).

- Eiki is the VP of Engineering for Cloud Engineering at VAST Data and is described as a co-founder at Green Cloud.

- Azure LSV4 full VM availability slipped by approximately two weeks, moving UK Met Office test readiness to early December 2025.

- UK Met Office Gen1 environment uses HPE Cray with GPFS and Slingshot; Gen2 must be hosted in the UK with dedicated facilities and network.

- UK Met Office has a symmetric I/O requirement of 1 TB/s read and 1 TB/s write simultaneously on large file systems.

- UK Met Office small-files tier target is approximately 1 PB at approximately 25 GB/s bidirectional, with additional metadata performance validation (MDTest).

- Azure LSV5 AMP is expected to be tested in Q1 2026 with production in Q2 2026, and Azure compute is considering a higher-density SKU targeting up to 800 Gbps and approximately 300 TB NVMe.

- Azure is planning RDMA enablement for VM-to-VM traffic; applicability to LSV4 and LSV5 was under review, including VNet and MTU constraints.

- The primary integration target is Azure Ethernet to Azure Compute; Slingshot integration is treated as a separate effort.

- VAST Polaris and Lifter path targets an Azure Native Resource Provider (RP) plus an Azure Marketplace offer with full API exposure and automation parity with Azure UI.

- Ed Kim is the procurement contact for OEM hardware; HPE was described as the likely path of least resistance, with alternatives under review.

- East US 2 was discussed as a potential test region due to H-series capacity, but the final region for benchmarking and the December test cluster was still TBD.

- Leo reached out to Anand to pursue a Microsoft-hosted VAST hardware deployment in Anand’s data center as a plan B that could become plan A for production success, with UK Met Office as first priority by timeline.
