---
type: people
title: Jai Menon
last_contact: '2025-10-06'
created: '2026-01-03'
tags:
- type/people
- generated
---

# Jai Menon

## Recent Context

- 2025-10-06: [[2025-10-06 - Jason updated Jai that he has a complex, high-variance offer from VAST and an ex]] - Weekly 1:1 between Jai Menon and Jason Vallery focused on Jason’s competing job offers (VAST vs Crus...
- 2025-10-06: [[2025-10-06 - Jason has a complex VAST offer with risky, sales-linked compensation and a more]] - Weekly 1:1 between Jai Menon and Jason Vallery focused on Jason’s pending job decision between a ris...
- 2025-10-06: [[2025-10-06 - Jason briefed Jai on offers from VAST and Crusoe, noting VAST’s complex, risky c]] - Weekly 1:1 where Jason and Jai discussed Jason’s competing offers from VAST and Crusoe versus stayin...
- 2025-10-06: [[2025-10-06 - Jason shared he has a complex, risky offer from VAST and a more stable option fr]] - 1:1 between Jai Menon and Jason Vallery about Jason’s external offers (VAST vs Crusoe) and why stayi...
- 2025-09-30: [[2025-09-30 - Jason shared that after meeting with Manish and reviewing rewards, he began expl]] - Weekly 1:1 between Jai Menon and Jason Vallery focused on Jason’s retention risk after reviewing rew...
- 2025-09-30: [[2025-09-30 - Jason shared he has multiple external management opportunities and plans to deci]] - Weekly 1:1 between Jai Menon and Jason Vallery focused on Jason’s potential departure from Microsoft...
- 2025-09-30: [[2025-09-30 - Jason shared that after meeting with Ong and seeing rewards, he began exploring]] - Weekly 1:1 between Jai Menon and Jason Vallery focused on Jason’s exploration of external opportunit...
- 2025-09-22: [[2025-09-22 - Jason and Jai discussed Apollo’s target workloads and deployment model (scale pe]] - Weekly 1:1 between Jason Vallery and Jai Menon focused on Apollo’s target workloads, per-site GPU cl...
- 2025-09-15: [[2025-09-15 - Silk briefed Jason on its cloud storage architecture optimized for databases and]] - Weekly 1:1 where Silk briefed Jason on its software-defined cloud storage architecture optimized for... (via Silk)
- 2025-09-15: [[2025-09-15 - Silk briefed Jason on its software-defined cloud storage for high-performance re]] - Silk briefed Jason (with Chris and Tom) on Silk’s software-defined cloud storage optimized for high-... (via Silk)
- 2025-09-15: [[2025-09-15 - Silk briefed Jason on their software-defined cloud storage for databases, emphas]] - Silk briefed Jason (and team) on Silk’s software-defined cloud storage optimized for database worklo... (via Silk)
- 2025-09-15: [[2025-09-15 - Discussed distributed cache strategy, MAI needs, and BlobFuse readiness. Aligned]]
- 2025-09-15: [[2025-09-15 - Jason and Jai aligned on next steps for a distributed cache strategy and short-t]]
- 2025-09-15: [[2025-09-15 - Jason and Jai discussed options and strategy for distributed caching (BlobFuse v]]
- 2025-09-03: [[2025-09-03 - Jai welcomed Jason back and aligned on a forward-looking scope evaluate OpenAI’]]

## Profile

**Role**: Manager / 1:1 counterpart (exact title not stated) at Microsoft (Storage (implied via "storage leadership team" context))
**Relationship**: Jason Vallery's 1:1 manager/leader and internal sponsor

**Background**:
- Meets weekly with Jason to build trust, remove blockers, align priorities, and coach; involved in discussions about Jason’s scope/comp options at Microsoft.
- Meets weekly with Jason; discussed internal constraints around compensation and unclear Apollo scope; offered to be available for clarification/references.
- Advising on Jason’s career decision; discussed feasibility of Microsoft counteroffer and Apollo scope; prefers not to push for a small counteroffer that could be perceived as insulting.

## Key Facts

- Silk is software-defined cloud storage focused on database and single source of truth workloads.
- Typical scale cited: up to ~1 PB per data pod; tens of GB/s throughput with sub-ms latency.
- Performance layer cited: ~2–3M TPS with 64k transactions; can serve millions of transactions/sec.
- Architecture: deployed near database VMs; uses read cache; compresses and can dedupe; durable layer on Azure PV2 with added erasure coding or on VMs with ephemeral media.
- Silk often competes with Azure NetApp Files and may outperform ANF Ultra at lower cost for certain DB workloads.
- Boost VMs can deliver ~40 GB/s from a single host in Silk tests.
- AI workloads are increasing and making access to production relational databases (SQL/Oracle/Postgres) more unpredictable.
- Two AI/DB patterns discussed: maximize production DB performance vs create near-real-time copies (tens of seconds) for AI access.
- Silk is seeking RDMA on the front end of Azure L-series to reduce CPU overhead; they are working with Gal Piglin’s team.
- Ong may introduce Silk to Jay Menon.

## Topics

Silk cloud storage architecture for database workloads, AI-driven access patterns to systems of record, Performance characteristics: throughput, latency, TPS, Real-time vs near-real-time copies for AI access, Competitive positioning vs Azure NetApp Files (ANF) and Azure native storage, RDMA front-end support on Azure L-series and CPU overhead reduction, Executive introduction planning (Jay Menon via Ong), Silk architecture for high-performance relational databases, AI-driven increases in load on systems of record, Performance limits and throughput/latency characteristics, Production acceleration vs near-real-time instant DB copies, RDMA support request on Azure L-series and CPU overhead reduction, Competitive landscape (Azure NetApp Files, Vaast, Weka), Customer opportunity identification when Azure native storage cannot meet performance, Silk software-defined cloud storage for databases

## Related

<!-- Wikilinks to related entities -->
