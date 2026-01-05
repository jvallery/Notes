---
type: customer
title: Silk briefing on Azure DB storage
date: '2025-09-15'
account: Silk
participants:
- Jason
- Chris
- Tom
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-09-15 - Silk briefed Jason on their software-defined
  cloud storage for databases, emphas.md
tags:
- type/customer
- account/silk
- generated
---

# Silk briefing on Azure DB storage

**Date**: 2025-09-15
**Account**: [[Silk]]
**Attendees**: Jason, Chris, Tom

## Summary

Silk briefed Jason on its software-defined cloud storage optimized for structured database workloads, highlighting sub-millisecond latency, tens of GB/s throughput, and scaling up to ~1 PB per pod. The group discussed AI-driven, unpredictable spikes hitting systems of record and two mitigation patterns: accelerating production databases versus creating near-real-time clones. Next steps included pursuing an intro/follow-up with Jay Menon and checking feasibility/timeline for RDMA support on Azure L-series to reduce CPU overhead.
## Action Items
- [ ] Confirm RDMA support/timeline for L-series front-end access with Azure contacts (Gal Piglin’s team) and report back. @Silk engineering 📅 2025-10-26 🔺 #task #proposed
- [ ] Schedule and prepare a follow-up meeting with Jay Menon; define agenda to ensure value for all parties. @Chris 📅 2025-10-26 ⏫ #task #proposed
- [ ] Flag customer opportunities where native Azure storage cannot meet performance and consider Silk. @Myself 📅 2025-10-26 🔽 #task #proposed
- [ ] Compile concrete customer use cases requiring real-time MCP access vs near-real-time clones for discussion with Jay. @Silk product 📅 2025-10-26 ⏫ #task #proposed

## Decisions
- Proceed with setting up a CEO-level introduction to Jay Menon.
- Evaluate use case fit per customer: accelerate production database performance vs use near-real-time cloned copies.

## Key Information
- Silk targets structured database workloads (block storage), not file-level sharing.
- Silk scales to ~1 PB per data pod and supports roughly 1–500 databases per pod.
- Performance claims discussed: sub-millisecond latency, tens of GB/s throughput; up to ~40 GB/s from a single host with Azure Boost VMs.
- Transactional capability discussed: ~2–3 million TPS with 64K IOs.
- Architecture includes a performance layer with read cache and N+X resiliency; can be placed near DB VMs via Azure Proximity Placement Groups (PPG).
- Durability options include PV2 volumes with additional erasure coding; data is always compressed and optionally deduplicated.
- Silk often competes with Azure NetApp Files (ANF) and claims it can outperform ANF ultra configurations for these database-centric use cases.
- AI/agentic workloads are increasing unpredictable access to systems of record, risking overload of single-VM database architectures.
- Silk requested RDMA access on Azure L-series front end to reduce CPU overhead.

---

*Source: [[Inbox/_archive/2025-09-15/2025-09-15 - Silk briefed Jason on their software-defined cloud storage for databases, emphas.md|2025-09-15 - Silk briefed Jason on their software-defined cloud storage for databases, emphas]]*

## Related

- [[Microsoft]]
- [[Google]]
- [[Amazon]]
- [[Oracle]]
- [[NetApp]]
- [[VAST]]
- [[Jai Menon]]