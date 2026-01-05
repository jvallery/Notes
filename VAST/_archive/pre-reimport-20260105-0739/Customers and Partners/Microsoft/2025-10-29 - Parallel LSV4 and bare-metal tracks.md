---
type: customer
title: Parallel LSV4 and bare-metal tracks
date: '2025-10-29'
account: Microsoft
participants:
- Leo
- Mike
- James
- Nico
- Jason Vallery
- Jonsi Stephenson
- Eiki
- Trevor
- Tiff
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-10-29 - Teams aligned to run two tracks
  in parallel an Azure LSV4 test cluster for UK M.md
tags:
- type/customer
- account/microsoft
- generated
---

# Parallel LSV4 and bare-metal tracks

**Date**: 2025-10-29
**Account**: [[Microsoft]]
**Attendees**: Leo, Mike, James, Nico, Jason Vallery, Jonsi Stephenson, Eiki, Trevor, Tiff

## Summary

Teams aligned to run two tracks in parallel: an 8-node Azure LSV4 VAST test cluster in the UK Met tenant targeted for early December, and a potential bare-metal dev system hosted in a Microsoft data center (Anand’s org). Key blockers discussed were LSV4 VM availability by region (LS96 vs LS192), RDMA scope/timelines, and internal Microsoft procurement constraints (Marketplace not usable for internal subscriptions). Engineering engagement will deepen on Polaris/Lifter to ensure full API exposure and automation parity (portal/CLI/SDK).
## Action Items
- [?] Review and approve the shared VAST configuration; drive internal approval and expedite shipping/installation and QA readiness. @Leo 📅 2025-11-08 🔺 #task #proposed
- [?] Connect Nico with Roni to align VM type, region, and availability for December readiness. @Leo 📅 2025-11-08 ⏫ #task #proposed
- [?] Coordinate VM choice (LS96 vs LS192) and target region for the December test cluster. @Nico 📅 2025-11-08 🔺 #task #proposed
- [?] Deliver an 8-node LSV4-based VAST test system in the UK Met tenant (early December target). @Leo 📅 2025-11-08 ⏫ #task #proposed
- [?] Prepare Azure demo for Supercomputing/Ignite (week of 2025-11-17). @Leo 📅 2025-11-17 🔺 #task #proposed
- [?] Ping Sara to confirm mid-November commitment on the EGAL/compute platform timeline and capacity. @Tiff 📅 2025-11-08 🔺 #task #proposed
- [?] Follow up with PM on RDMA timelines and scope (VM-to-VM, GPU-to-VAST, east-west vs north-south, VNet/MTU limits). @Nico 📅 2025-11-08 🔺 #task #proposed
- [?] Set up a separate engineering track/workshop for Polaris/Lifter and data-plane integration (VAST, Azure, UK Met). @James 📅 2025-11-08 ⏫ #task #proposed
- [?] Build and share a BOM for the bare-metal dev system. @James 📅 2025-11-08 🔺 #task #proposed
- [?] Discuss with Anand DC location, ownership, and purchase of the bare-metal dev system; aim for an answer by Supercomputing. @Mike 📅 2025-11-08 🔺 #task #proposed
- [?] Open the T&Cs/commercials/KPIs discussion and involve John. @Claire 📅 2025-11-08 ⏫ #task #proposed
- [?] Provide OEM preferences (ranked) for secure supply (e.g., HPE and alternatives). @TBD 📅 2025-11-08 ⏫ #task #proposed
- [?] Engage Ed Kim to align procurement path and approved OEM list. @James 📅 2025-11-08 ⏫ #task #proposed
- [?] Draft GPFS swap design for Gen1 Slingshot path (risks, performance, approval needs) with Trevor. @Trevor 📅 2025-11-08 🔽 #task #proposed
- [?] Share compute status on NVMe persistence/dedicated hosts feasibility for L-series/LSV5. @Leo 📅 2025-11-08 ⏫ #task #proposed
- [?] Define a non-Marketplace software procurement route for internal Microsoft subscriptions. @James 📅 2025-11-08 🔺 #task #proposed
- [?] Confirm LSV5 AMP and proposed 800G/300TB SKU timeline and suitability for UK Met (mid-November answer). @Tiff 📅 2025-11-08 🔺 #task #proposed
- [?] Verify RDMA announcement at Ignite and applicability to LSV4/LSV5; validate private review timing. @Nico 📅 2025-11-08 🔺 #task #proposed

## Decisions
- Pursue Azure LSV4 and bare-metal (Anand DC) paths in parallel.
- Target early December for UK Met to begin testing VAST on Azure LSV4.
- Proceed on LS96 where LS192 is not available; support both SKUs where possible.
- Treat Slingshot integration as a separate track; prioritize Azure Ethernet integration.
- Engage UK Met as a design partner on Polaris/Lifter with emphasis on full API exposure.
- Keep one weekly sync until testing begins, then split into engineering and business tracks.

## Key Information
- Azure LSV4 full VM availability slipped by ~2 weeks; UK Met test readiness moved to early December.
- LS96 provides ~40 Gbps networking; LS192 targets ~200 Gbps but availability varies by region.
- UK Met Gen1 uses HPE Cray/GPFS; Gen2 must be UK-hosted with dedicated facilities and network.
- Symmetric I/O requirement: 1 TB/s read and 1 TB/s write simultaneously on large file systems.
- Small-files tier target: ~1 PB at ~25 GB/s bidirectional plus metadata performance (MDTest).
- LSV5 AMP expected Q1 testing / Q2 production; compute team considering higher-density SKU (up to 800 Gbps, ~300 TB NVMe).
- Azure RDMA enablement (VM-to-VM) is being planned; applicability to LSV4/LSV5 under review.
- Main integration target is Azure Ethernet to Azure Compute; Slingshot integration considered separately.
- VAST Polaris/Lifter path targets Azure Native Resource Provider + Marketplace offer with full API exposure.
- Internal Microsoft cannot procure software via Marketplace; alternate procurement route required.
- Procurement contact for OEM hardware: Ed Kim; HPE considered path of least resistance; alternatives under review.
- Testing region may be East US 2 due to H-series capacity; final region TBD.

---

*Source: [[Inbox/_archive/2025-10-29/2025-10-29 - Teams aligned to run two tracks in parallel an Azure LSV4 test cluster for UK M.md|2025-10-29 - Teams aligned to run two tracks in parallel an Azure LSV4 test cluster for UK M]]*

## Related

- [[HPE]]
- [[NetApp]]
- [[Dell]]
- [[Cloud control plane]]
- [[Neo]]
- [[Alluxio]]
- [[Jason Vallery]]
- [[Jonsi Stephenson]]
- [[John Downey]]
- [[Jan Niemus]]