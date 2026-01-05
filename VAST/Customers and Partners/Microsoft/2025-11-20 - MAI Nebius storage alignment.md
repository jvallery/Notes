---
type: customer
title: MAI Nebius storage alignment
date: '2025-11-20'
account: Microsoft
participants:
- Lior Genzel
- Bilal
- Jason Vallery
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-11-20 - Microsoft (Bilal) and VAST (Jason,
  Lior) aligned on storage options for MAI’s la.md
tags:
- type/customer
- account/microsoft
- generated
---

# MAI Nebius storage alignment

**Date**: 2025-11-20
**Account**: [[Microsoft]]
**Attendees**: Lior Genzel, Bilal, Jason Vallery

## Summary

Microsoft (Bilal) and VAST (Jason, Lior) aligned on storage options for MAI’s large-scale Nebius deployment (~100K–120K GPUs). MAI prefers file-based storage (NFS/RDMA, GPU Direct Storage) due to tooling friction and protocol/performance gaps with Azure Blob; VAST outlined its software-defined file/object platform and sizing approach based on per-GPU throughput and capacity requirements. They discussed a potential integration path that could avoid Sirius overlay networking costs if VAST can attach to the physical GPU front-end network, and agreed to proceed with a requirements-first workshop and potential early-December site survey participation.
## Action Items
- [?] Debrief MAI on the VAST option and validate file-based requirements including per-GPU throughput targets, read/write mix, capacity needs, and whether MAI posture is pivot vs supplement to Blob. @Bilal 📅 2025-11-20 🔺 #task #proposed
- [?] Share VAST sizing examples, performance/capacity design options, and management/API documentation with Microsoft (including Suresh). @Myself ⏫ #task #proposed
- [?] Schedule a three-way technical workshop (Microsoft, MAI, VAST) to capture requirements and draft the site design. @Suresh ⏫ #task #proposed
- [?] Confirm Nebius front-end/back-end network topology and whether storage can attach to the physical GPU network without Sirius overlay; document required security/compliance controls. @Suresh ⏫ #task #proposed
- [?] Provide detailed Gen10.3 plan-of-record specs (rack counts, CX7 NICs, power per rack, usable PB per rack, total Tbps) and Sirius overlay limits to VAST. @Bilal ⏫ #task #proposed
- [?] Validate VAST supply chain and lead times for the 2026 ramp (flash, compute/data node quantities) and propose tranche sizing aligned to MAI dates. @Myself #task #proposed
- [?] Coordinate VAST participation in the early-December Nebius site survey and align agenda time. @Bilal #task #proposed
- [?] Decide deployment model (Azure storage hardware vs qualified VAST ODM hardware) with pros/cons, cost, and performance implications. @Suresh #task #proposed
- [?] Draft rack adjacency/row allocation plan for VAST given constraints across 14 data halls. @Suresh #task #proposed
- [?] Align on deduplication planning assumptions to set effective capacity targets for MAI datasets. @Lior Genzel Genzel 🔽 #task #proposed
- [?] Send meeting notes and VAST design tables to MAI stakeholders. @Myself #task #proposed
- [?] Confirm the exact site survey date, location, and attendees; circulate logistics. @Bilal ⏫ #task #proposed
- [?] Book an in-person workshop (Redmond or site) with Microsoft, MAI, and VAST engineering. @Suresh ⏫ #task #proposed

## Decisions
- Suresh will serve as DRI while Bilal is out in early December.
- Proceed with a requirements-first approach, followed by site design and a site survey.

## Key Information
- MAI strongly prefers file-based access; Azure Blob has forced tooling refactors and is seen as problematic for protocol/performance needs.
- VAST supports NFS over RDMA, GPU Direct Storage, and S3 over RDMA; can tune compute (C) vs data (D) node ratios to meet throughput/capacity targets.
- Microsoft plan-of-record discussed: ~1.6 exabytes all-flash across ~400 Gen10.3 racks (~15 kW/rack) delivering ~192 Tbps total; CX7 NICs referenced.
- VAST deduplication can increase effective capacity (example cited: ~1.7x observed at an MAI cluster).
- VAST can integrate with Azure Active Directory and provides its own management plane/portal and APIs.
- VAST is not yet an Azure hardware provider; Marketplace on Lsv4 is not viable at this scale.
- Potential cost savings if VAST can attach to the physical GPU front-end network and bypass Sirius overlay, pending security/compliance approval.
- An internal bake-off comparing VAST and Lustre on future Azure hardware was mentioned as underway.
- Bilal expected to be out of office roughly 2025-12-03 to 2025-12-16; early-December site survey discussed.

---

*Source: [[Inbox/_archive/2025-11-20/2025-11-20 - Microsoft (Bilal) and VAST (Jason, Lior) aligned on storage options for MAI’s la.md|2025-11-20 - Microsoft (Bilal) and VAST (Jason, Lior) aligned on storage options for MAI’s la]]*

## Related

- [[Lior Genzel]]
- [[Jason Vallery]]
- [[CoreWeave]]
- [[NetApp]]
- [[NVIDIA]]
- [[Amazon]]
- [[Google]]
- [[Oracle]]
- [[Toshiba]]
- [[Databricks]]
- [[Micron]]
- [[Shopify]]
- [[Tesla]]
- [[Samsung]]
- [[HPE]]
- [[Cisco]]
- [[Snowflake]]
- [[Seagate]]