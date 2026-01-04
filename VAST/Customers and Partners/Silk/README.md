---
type: customer
title: Silk
last_contact: '2025-09-15'
created: '2026-01-03'
tags:
- type/customer
- generated
---

# Silk

## Recent Context

- 2025-09-15: [[2025-09-15 - Silk briefed Jason on its cloud storage architecture optimized for databases and]] - Weekly 1:1 where Silk briefed Jason on its software-defined cloud storage architecture optimized for...
- 2025-09-15: [[2025-09-15 - Silk briefed Jason on its software-defined cloud storage for high-performance re]] - Silk briefed Jason (with Chris and Tom) on Silk’s software-defined cloud storage optimized for high-...
- 2025-09-15: [[2025-09-15 - Silk briefed Jason on their software-defined cloud storage for databases, emphas]] - Silk briefed Jason (and team) on Silk’s software-defined cloud storage optimized for database worklo...

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
