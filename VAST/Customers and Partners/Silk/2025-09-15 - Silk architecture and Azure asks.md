---
type: customer
title: Silk architecture and Azure asks
date: '2025-09-15'
account: Silk
participants:
- Jason
- Tom
- Chris
- Ong
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-09-15 - Silk briefed Jason on its cloud
  storage architecture optimized for databases and.md
tags:
- type/customer
- account/silk
- generated
---

# Silk architecture and Azure asks

**Date**: 2025-09-15
**Account**: [[Silk]]
**Attendees**: Jason, Tom, Chris, Ong

## Summary

Silk briefed Jason on its software-defined cloud storage architecture optimized for high-performance database workloads and discussed how AI-driven access is increasing load on systems of record. They compared positioning versus Azure native options (notably Azure NetApp Files) and raised a key request for RDMA support on Azure L-series to reduce CPU overhead, with ongoing engagement with Gal Piglin’s team. Next steps include pursuing an intro to Jai Menon via Ong and sharing concrete customer use cases to tailor an executive discussion.
## Action Items
- [ ] Coordinate with Ong to schedule an introduction meeting with Jai Menon. @Tom 📅 2025-10-26 ⏫ #task #proposed
- [ ] Check RDMA front-end support timeline for Azure L-series with Gal Piglin’s team. @Myself 📅 2025-10-27 ⏫ #task #proposed
- [ ] Send architecture and real-time use-case slides (including the discussed slide) to Jason. @Chris 📅 2025-10-26 ⏫ #task #proposed
- [ ] Keep Silk in mind for customer opportunities requiring more performance than Azure native offerings. @Myself 📅 2025-10-26 🔽 #task #proposed
- [ ] Confirm whether the target AI use cases require real-time access or can use near-real-time copies. @Tom 📅 2025-10-26 ⏫ #task #proposed
- [ ] Clarify what topics Jai Menon cares about to tailor the executive meeting. @Myself 📅 2025-10-26 ⏫ #task #proposed

## Key Information
- Silk is software-defined cloud storage focused on database and system-of-record workloads; typical deployments scale up to ~1 PB per data pod with tens of GB/s throughput and sub-ms latency.
- Silk cited performance of ~2–3M transactions/sec (64k transactions) and noted that single-VM database throughput is often the limiting factor.
- Architecture uses a performance layer with read cache deployed near database VMs (e.g., via proximity placement groups) and a durable layer backed by Azure PV2 (with added erasure coding) or VMs with ephemeral media; data is compressed and can be deduplicated.
- Silk often competes with Azure NetApp Files and claims it can outperform ANF Ultra at lower cost for certain DB workloads.
- Silk reported tests showing Boost VMs delivering ~40 GB/s from a single host.
- AI workloads (RAG/agentic) are increasingly and unpredictably driving access to production relational databases (SQL, Oracle, Postgres), raising risk of overwhelming single-VM constrained systems.
- Silk is seeking RDMA on the front end of Azure L-series to reduce CPU overhead and is already working with Gal Piglin’s team; Ong may facilitate an intro to Jai Menon.

---

*Source: [[Inbox/_archive/2025-09-15/2025-09-15 - Silk briefed Jason on its cloud storage architecture optimized for databases and.md|2025-09-15 - Silk briefed Jason on its cloud storage architecture optimized for databases and]]*

## Related

- [[Microsoft]]
- [[Google]]
- [[Amazon]]
- [[Jai Menon]]