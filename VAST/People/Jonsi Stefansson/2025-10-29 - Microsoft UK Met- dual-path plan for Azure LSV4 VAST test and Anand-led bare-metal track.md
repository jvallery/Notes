---
type: "customer"
title: "Microsoft UK Met: dual-path plan for Azure LSV4 VAST test and Anand-led bare-metal track"
date: "2025-10-29"
account: ""
participants: ["Jason Vallery", "Jonsi Stephenson", "Leo (Unknown)", "Nico (Unknown)", "James (Unknown)", "Mike (Unknown)", "Anand (Unknown)", "Tiff (Unknown)", "Sarah (Unknown)", "Trevor (Unknown)", "Travis (Unknown)", "Trevor (Unknown)", "Ed Kim (Unknown)"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-29 - Team aligned on a dual-path approach 1) deliver an Azure-based VAST test on LSV.md"
tags:
  - "type/customer"
  - "account/"
  - "generated"

---

# Microsoft UK Met: dual-path plan for Azure LSV4 VAST test and Anand-led bare-metal track

**Date**: 2025-10-29
**Account**: [[]]
**Attendees**: Jason Vallery, Jonsi Stephenson, Leo (Unknown), Nico (Unknown), James (Unknown), Mike (Unknown), Anand (Unknown), Tiff (Unknown), Sarah (Unknown), Trevor (Unknown), Travis (Unknown), Trevor (Unknown), Ed Kim (Unknown)

## Summary

The team aligned on a dual-path approach for Microsoft UK Met: deliver an Azure-based VAST test on LSV4 by the first week of December 2025 while also pursuing a bare-metal/dev system in a Microsoft data center via Anand’s organization. Key dependencies include LSV4 VM regional availability (LS96 vs LS192), confirmation of VM-to-VM and GPU-to-VAST RDMA timelines, and defining a non-marketplace procurement path for internal Microsoft subscriptions.


## Action Items


- [?] Review and approve the shared VAST configuration for the Anand-led Microsoft data center bare-metal path, then expedite shipment, installation, and deployment readiness for Leo’s QA team. @Leo (Unknown) 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Introduce Nico to Ronnie Booker (data plane) to align Azure VM type, region, and availability for the December 2025 Azure LSV4 test. @Leo (Unknown) 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Select the starting Azure VM for testing (LS96 vs LS192) based on regional availability and coordinate the specific configuration for the UK Met Office test. @Nico (Unknown) 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Deliver an 8-node Azure LSV4 VAST test system for Microsoft UK Met Office by the first week of December 2025. @TBD 📅 2025-12-05 ⏫ #task #proposed #auto

- [?] Prepare an Azure demo for Supercomputing/Ignite on 2025-11-17 showcasing the Azure LSV4-based VAST test progress. @TBD 📅 2025-11-17 ⏫ #task #proposed #auto

- [?] Contact Sarah (Unknown) to confirm the mid-November 2025 commitment on the EGAL platform update and decision timing. @Tiff (Unknown) 📅 2025-11-15 ⏫ #task #proposed #auto

- [?] Verify RDMA availability and timelines for VM-to-VM and GPU-to-VAST on LSV4/LSV5, including MTU and VNet constraints, with the relevant Microsoft PM. @Nico (Unknown) 📅 2025-11-15 ⏫ #task #proposed #auto

- [?] Schedule an engineering workshop to kick off Lifter/Polaris integration with Nico (Unknown), Trevor (Unknown), and Travis (Unknown). @Jonsi Stephenson 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Create a separate engineering track for OEM and bare-metal automation, including hardware and switch API integration requirements. @James (Unknown) 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Align with Anand (Unknown) on who will purchase and own the bare-metal POC system, targeting an answer around Supercomputing (2025-11-17 to 2025-11-20 timeframe). @Mike (Unknown) 📅 2025-11-20 ⏫ #task #proposed #auto

- [?] Draft a bill of materials and facility requirements (space, power, networking) for the bare-metal dev/POC system in a Microsoft data center. @James (Unknown) 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Coordinate with Ed Kim (Unknown) on OEM sourcing and the transacting route, and align the OEM shortlist for the bare-metal path. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Provide the top 2 to 3 preferred OEMs for the bare-metal path, with HPE as the leading candidate and other options to be determined. @TBD 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Define and confirm a non-marketplace procurement path for VAST software for internal Microsoft subscriptions. @TBD 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Explore Azure compute options to mitigate ephemeral NVMe behavior on L-series for UK Met Office, such as dedicated hosts or a special SKU with persistent NVMe. @TBD 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Draft a GPFS swap-out design using VAST over TCP/IP and Ethernet, including a business case tied to outage penalties for the UK Met Office environment. @Trevor (Unknown) 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Confirm LSV4 LS192 availability in target regions (example mentioned: East US 2) and plan fallback to LS96 if needed. @Nico (Unknown) 📅 2025-11-05 ⏫ #task #proposed #auto

- [?] Confirm EGAL platform specifications (example targets: 800 Gbps and approximately 300 TB NVMe) and timeline, and ensure the platform can be placed in UK Met Office test regions. @TBD 📅 2025-11-15 ⏫ #task #proposed #auto

- [?] Verify whether Ignite announcements include east-west VM-to-VM RDMA for LSV4 and capture preview and GA dates for planning. @Nico (Unknown) 📅 2025-11-18 ⏫ #task #proposed #auto

- [?] Clarify where the bare-metal POC will reside (Microsoft internal environment vs customer environment) and define the access model for UK Met Office stakeholders. @Mike (Unknown) 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Align with the UK Met Office customer stakeholders on symmetric IO requirements and confirm whether requirements can be adjusted based on Azure and networking constraints. @Mike (Unknown) 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Confirm space and power availability for potential POC systems if Microsoft purchases them for the bare-metal path. @Anand (Unknown) 📅 2025-11-08 ⏫ #task #proposed #auto




## Decisions


- Proceed in parallel with (1) an Azure LSV4-based VAST test system for Microsoft UK Met Office by the first week of December 2025 and (2) an Anand-led bare-metal/dev system in a Microsoft data center.

- Use LS96 for initial benchmarking if LS192 is not available in the required Azure regions for the UK Met Office test.

- Treat Slingshot integration as a separate engineering track, with the primary network focus on Azure Ethernet for the initial test and path to production.

- For the bare-metal path, Microsoft prefers sourcing OEM hardware directly, with HPE considered the path of least resistance pending final shortlist.

- Because internal Microsoft subscriptions cannot use Azure Marketplace, pursue a non-marketplace procurement route for VAST software.




## Key Information


- UK Met Office Generation 1 environment uses HPE Cray compute with GPFS/ClusterStore and Slingshot networking in dedicated data centers, while several other workloads (archive, post-processing cluster, VDI) already run on standard Azure services.

- UK Met Office Generation 2 must be UK-based and is expected to use dedicated compute and storage, potentially via Azure L-series (LSv4/LSv5) or bare metal, on a dedicated customer network.

- Azure LSV4 VM options discussed: LS96 provides 40 Gbps networking; LS192 offers higher bandwidth but has limited regional availability.

- VAST committed to deliver an 8-node Azure LSV4-based VAST test system for UK Met Office by the first week of December 2025, with a demo planned around 2025-11-17 for Supercomputing/Ignite.

- VM-to-VM east-west RDMA for LSV4/LSV5 and GPU-to-VAST RDMA are desired for performance, but definitive timelines and constraints (MTU and VNet limitations) require verification with Microsoft PM.

- Slingshot integration is not on the critical path: VAST does not have a kernel-space RDMA path for Slingshot; TCP/IP over Ethernet is viable, and direct connect to Slingshot requires HPE approval.

- Internal Microsoft subscriptions cannot use Azure Marketplace for VAST software procurement, so a non-marketplace procurement mechanism is required.

- Performance targets discussed include up to 1 TB/s symmetric IO and small-file all-flash targets such as 25 GB/s bidirectional on approximately 1 PB.

- Current GPFS issues in the UK Met environment include lockups/outages, and metadata create rate may be tight relative to capacity requirements.

- Jonsi Stephenson is GM of Cloud at VAST Data and previously served as Global CTO and GM of Cloud at NetApp, where he helped build Azure NetApp Files (ANF).



---

*Source: [[2025-10-29 - Team aligned on a dual-path approach 1) deliver an Azure-based VAST test on LSV]]*