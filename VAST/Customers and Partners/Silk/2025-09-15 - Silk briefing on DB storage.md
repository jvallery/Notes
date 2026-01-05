---
type: customer
title: Silk briefing on DB storage
date: '2025-09-15'
account: Silk
participants:
- Jason
- Chris
- Tom
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-09-15 - Silk briefed Jason on its software-defined
  cloud storage for high-performance re.md
tags:
- type/customer
- account/silk
- generated
---

# Silk briefing on DB storage

**Date**: 2025-09-15
**Account**: [[Silk]]
**Attendees**: Jason, Chris, Tom

## Summary

Silk briefed Jason on its software-defined cloud storage optimized for high-performance relational databases across Azure/GCP/AWS, emphasizing rising AI/agentic load on systems of record. They discussed performance characteristics, architectural options (accelerate production vs near-real-time instant copies), and a key request for RDMA support on Azure L-series to reduce CPU overhead. Next steps include an introduction to Silk CEO Jay Menon via Ong and follow-up on RDMA timeline with Gal’s team.
## Action Items
- [ ] Coordinate introduction to Jay Menon as suggested by Ong @TBD 📅 2025-10-26 ⏫ #task #proposed
- [ ] Advise what topics Jay Menon cares about to tailor the session @Myself 📅 2025-10-26 ⏫ #task #proposed
- [ ] Follow up with Gal’s team on RDMA support timeline for L-series/Duo Boost @Silk engineering team 📅 2025-10-26 ⏫ #task #proposed
- [ ] Share customer opportunities that exceed native Azure storage performance with Silk @Myself 📅 2025-10-26 ⏫ #task #proposed
- [ ] Schedule meeting with Jay Menon after intro @Chris 📅 2025-10-26 ⏫ #task #proposed
- [ ] Prepare concise real-world use cases highlighting real-time vs near-real-time DB access needs @Tom 📅 2025-10-26 🔽 #task #proposed

## Decisions
- Proceed with connecting to Jay Menon through Ong.

## Key Information
- Silk is software-defined cloud storage optimized for structured/relational DB workloads across Azure, GCP, and AWS.
- A single Silk data pod supports roughly 1–500 databases up to ~1 PB, with n+x resilience and optional read cache (cNodes) placed close to DB VMs (e.g., via proximity placement groups).
- Reported performance includes sub-millisecond latency, tens of GB/s throughput, and ~40 GB/s per host observed with Azure Boost VMs; current stated limit is ~2–3M transactions/sec with typical IO size around 64 KB.
- Durability options include PV2 volumes with additional erasure coding or a UCL series using ephemeral media; data is always compressed with optional deduplication.
- Silk often competes with Azure NetApp Files (ANF) and claims better cost/performance than ANF Ultra for certain workloads.
- AI/agentic access is increasing and making load on production systems of record less predictable; two patterns discussed were accelerating production DBs vs creating near-real-time instant copies with tens-of-seconds lag.
- Key feature request is RDMA on Azure L-series front end to reduce CPU overhead; no clear Azure timeline; Silk is working with Gal’s team.

---

*Source: [[Inbox/_archive/2025-09-15/2025-09-15 - Silk briefed Jason on its software-defined cloud storage for high-performance re.md|2025-09-15 - Silk briefed Jason on its software-defined cloud storage for high-performance re]]*

## Related

- [[Microsoft]]
- [[Amazon]]
- [[Google]]
- [[Oracle]]
- [[Jai Menon]]