---
type: "customer"
title: "Dual-path Azure and bare-metal plan"
date: "2025-10-29"
account: "Microsoft"
participants: ["Jonsi Stemmelsson", "Leo", "Nico", "Mike", "Jason Vallery", "James", "Trevor", "Tiff", "John", "Anand", "Eiki", "Jan", "Assaf", "Sarah", "Claire", "Ed Kim", "Roni"]
source: "transcript"
source_ref: "Inbox/_archive/2025-10-29/2025-10-29 - Team aligned on a dual-path approach 1) deliver an Azure-based VAST test on LSV.md"
tags:
  - "type/customer"
  - "account/microsoft"
  - "generated"
---

# Dual-path Azure and bare-metal plan

**Date**: 2025-10-29
**Account**: [[Microsoft]]
**Attendees**: Jonsi Stemmelsson, Leo, Nico, Mike, Jason Vallery, James, Trevor, Tiff, John, Anand, Eiki, Jan, Assaf, Sarah, Claire, Ed Kim, Roni

## Summary

Team aligned on a parallel approach for UK Met: deliver an 8-node Azure LSV4 VAST test system by the first week of December while also pursuing a bare-metal/dev system in a Microsoft data center via Anand’s org. Key blockers include LSV4 full-node (LS192) regional availability, RDMA timelines (VM-to-VM and GPU-to-VAST), and defining procurement paths for OEM hardware and non-marketplace software for internal Microsoft subscriptions.
## Action Items
- [ ] Deliver an 8-node LSV4 VAST test system in Azure for UK Met by the first week of December. @VAST Engineering 📅 2025-12-05 ⏫ #task
- [ ] Prepare Azure demo for Supercomputing/Ignite. @VAST Engineering 📅 2025-11-17 ⏫ #task
- [ ] Verify RDMA availability and timelines (VM-to-VM and GPU-to-VAST), including MTU and VNet constraints, with PM. @Nico 📅 2025-11-15 ⏫ #task
- [ ] Confirm LSV4 LS192 availability in target regions and plan fallback to LS96 as needed. @Nico 📅 2025-11-05 ⏫ #task
- [ ] Verify if Ignite announcements include east-west VM-to-VM RDMA for LSV4 and capture preview/GA dates. @Nico 📅 2025-11-18 #task
- [ ] Discuss with Anand who will purchase/own the bare-metal POC system; target an answer around Supercomputing. @Mike 📅 2025-11-20 ⏫ #task
- [ ] Define a non-marketplace procurement path for VAST software for internal Microsoft subscriptions. @Microsoft Procurement ⏫ #task
- [ ] Coordinate with Ed Kim on OEM sourcing and transacting route; align OEM shortlist. @Jason Vallery #task
- [ ] Schedule engineering workshop on Lifter/Polaris integration with Nico, Trevor, and Travis. @Jonsi Stemmelsson #task
- [ ] Set up a separate engineering track for OEM/bare-metal automation (hardware/switch APIs). @James #task
- [ ] Ping Sarah to confirm mid-November commitment on EGAL platform update. @Tiff 📅 2025-11-15 ⏫ #task

## Decisions
- Proceed with Azure LSV4-based VAST test in early December and a bare-metal/dev system with Anand’s org.
- Accept LS96 for initial benchmarking if LS192 is unavailable in target regions.
- Defer Slingshot specifics from the main development path; handle as a separate track.
- Microsoft to prefer sourcing OEM hardware directly; HPE likely path of least resistance (final shortlist pending).
- Internal Microsoft cannot use Marketplace for software; pursue non-marketplace procurement route.

## Key Information
- UK Met Gen1 uses HPE Cray plus GPFS/ClusterStore in dedicated data centers; several other Azure services already in use.
- Gen2 must be UK-based and likely uses dedicated compute and storage (L-series or bare metal).
- LS96 provides 40 Gbps; LS192 provides higher bandwidth but has limited regional availability.
- VAST Azure test system commitment moved to the first week of December; demo planned around 2025-11-17 (SC/Ignite).
- VM-to-VM RDMA for LSV4/LSV5 is targeted but timelines need verification; GPU-to-VAST RDMA is also desired.
- EGAL/LSV5: AMP VM Q1 test/Q2 prod; potential 800 Gbps and ~300 TB NVMe SKU; mid-November decision expected.
- Marketplace cannot be used for internal Microsoft subscriptions; alternate software procurement is required.
- Slingshot has no kernel-space RDMA path for VAST; TCP/IP/Ethernet is viable; direct connect requires HPE approval.
- Performance targets include up to 1 TB/s symmetric IO and small-file all-flash targets (e.g., 25 GB/s bidirectional on ~1 PB).
- Current GPFS issues include lockups/outages; metadata create rate may be tight versus capacity.

---

*Source: [[Inbox/_archive/2025-10-29/2025-10-29 - Team aligned on a dual-path approach 1) deliver an Azure-based VAST test on LSV.md|2025-10-29 - Team aligned on a dual-path approach 1) deliver an Azure-based VAST test on LSV]]*

## Related

- [[HPE]]
- [[NetApp]]
- [[Dell]]
- [[Lenovo]]
- [[Cloud control plane]]
- [[Seth Haynes]]
- [[Andy Perlsteiner]]
- [[John Heidgerken]]
- [[Robert Brooks]]
- [[Rick Scurfield]]
- [[Michael Myrah]]
- [[Kirstin Bordner]]
- [[John Mao]]
- [[Jan Niemus]]
- [[Frank Ray]]
- [[Jonsi Stephenson]]
- [[Jeremy Winter]]
- [[Jonsi Stemmelsson]]
- [[Jason Vallery]]
