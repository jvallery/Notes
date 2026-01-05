---
type: customer
title: UK Met Gen2 pilot planning
date: '2025-10-28'
account: Microsoft
participants:
- Jason Vallery
- Niko Dukic
- Lior Genzel
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-10-28 - Working session on UK Met Gen2
  storagecompute plan. VaST to run a pilot to vali.md
tags:
- type/customer
- account/microsoft
- generated
---

# UK Met Gen2 pilot planning

**Date**: 2025-10-28
**Account**: [[Microsoft]]
**Attendees**: Jason Vallery, Niko Dukic, Lior Genzel

## Summary

Working session on UK Met Office Gen2 ClusterStore replacement and the pilot needed to validate mandatory contract requirements. Two implementation paths are being evaluated: an Azure VM SKU with very high-speed NICs (preferred) versus shipping ODM/bare-metal VAST hardware that would require an SDN intermediary and added complexity. The key dependency is Microsoft providing written confirmation and timeline for a VM SKU meeting ~300 TB/node and 800 Gb NIC requirements (target update by 2025-11-15), with interim testing potentially starting on 100 Gb VMs and a minimal viable test configuration defined with Mike and Anand.
## Action Items
- [?] Confirm availability and exact SKU name for full VMs with high-speed NICs and share readiness date. @Niko 📅 2025-10-28 🔺 #task #proposed
- [?] Share the email thread with Mike and Anand; schedule and run the configuration meeting. @Lior Genzel 📅 2025-10-29 🔺 #task #proposed
- [?] Align with Mike to confirm Anand is waiting on minimal test configuration and greenlight staging. @Niko 📅 2025-10-29 🔺 #task #proposed
- [?] Propose minimal viable test configuration (node count and per-node capacity/compute) for functional and initial scale testing. @Lior Genzel 📅 2025-10-29 🔺 #task #proposed
- [?] Obtain written confirmation and timeline for VMs supporting ~300 TB/node and 800 Gb NICs. @Niko 📅 2025-11-15 🔺 #task #proposed
- [?] Prepare to ship and deploy a small ODM/VAST cluster for testing if required; prioritize rapid turn-up. @Lior Genzel ⏫ #task #proposed
- [?] Provide initial IO workload details (sequential vs random, read/write mix, typical file sizes) once available. @Niko ⏫ #task #proposed
- [?] Decide between Azure VM path vs bare metal + SDN based on SKU outcome and timelines. @Niko 📅 2025-11-15 ⏫ #task #proposed
- [?] Validate whether HBv5 with InfiniBand backend is viable for direct storage connectivity in this deployment. @Niko ⏫ #task #proposed
- [?] If full VM SKU is delayed, confirm starting tests on the 100 Gb VM and plan migration path. @Niko 📅 2025-10-29 ⏫ #task #proposed
- [?] Confirm pilot validation criteria map to contract mandatory requirements. @Myself ⏫ #task #proposed

## Key Information
- Gen2 is a replacement for the current ClusterStore (not an archive project).
- Two compute paths are under consideration: Azure-provided VM SKU with high-speed NICs (preferred) vs ODM/bare metal requiring an SDN intermediary/bridge (adds complexity and an extra hop).
- Requested target node spec is ~300 TB per node with 800 Gb NICs; current proposed LSP5 does not fit.
- Microsoft/Azure team indicated they would propose a new SKU by 2025-11-15; written confirmation and timeline are still pending.
- Interim testing may start on a 100 Gb VM SKU while waiting for the full high-speed VM SKU.
- Workload is expected to be mostly sequential with large files and roughly 50/50 read/write; detailed IO profile is still pending.
- Pilot is intended to validate mandatory contract requirements; nice-to-have items are secondary.
- Alternative topology discussed includes HBv5 with InfiniBand for backend storage connectivity.

---

*Source: [[Inbox/_archive/2025-10-28/2025-10-28 - Working session on UK Met Gen2 storagecompute plan. VaST to run a pilot to vali.md|2025-10-28 - Working session on UK Met Gen2 storagecompute plan. VaST to run a pilot to vali]]*

## Related

- [[Jason Vallery]]
- [[Lior Genzel]]
- [[Mike Requa]]
- [[Amy Hood]]
- [[Kanchan Mehrotra]]
- [[Jai Menon]]
- [[Maneesh Sah]]
- [[Ronen Cohen]]
- [[Jeff Denworth]]
- [[Cloud control plane]]
- [[Google]]
- [[Amazon]]
- [[CoreWeave]]