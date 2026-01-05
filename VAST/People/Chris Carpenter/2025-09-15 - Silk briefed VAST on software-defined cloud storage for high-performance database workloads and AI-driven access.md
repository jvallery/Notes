---
type: people
title: Silk briefed VAST on software-defined cloud storage for high-performance database workloads and AI-driven access
date: '2025-09-15'
participants:
- Jason Vallery
- Chris Carpenter
- TBD (Silk contact, referred to as Tom)
- TBD (Silk contact, referred to as Remote)
- TBD (person mentioned as Jürgen)
source: transcript
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-09-15 - Silk briefed Jason on its cloud storage architecture optimized for databases and.md
tags:
- type/people
- generated
person: Chris Carpenter
---

# Silk briefed VAST on software-defined cloud storage for high-performance database workloads and AI-driven access

**Date**: 2025-09-15
**Attendees**: Jason Vallery, Chris Carpenter, TBD (Silk contact, referred to as Tom), TBD (Silk contact, referred to as Remote), TBD (person mentioned as Jürgen)

## Summary

Silk briefed Jason Vallery on its software-defined cloud storage architecture optimized for relational databases and single source of truth workloads, with increasing AI-driven access patterns. Discussion covered performance characteristics, deployment architecture near database VMs, competitive positioning vs Azure NetApp Files, and a request for RDMA support on Azure L-series to reduce CPU overhead.

## Action Items

- [?] Coordinate with Ong to schedule an introduction meeting between Silk and Jai Menon. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Check status and feasibility of RDMA front-end support for Azure L-series for Silk’s architecture, coordinating with Igal Figlin’s team. @Myself 📅 2025-10-27 ⏫ #task #proposed #auto

- [?] Send Silk architecture and real-time AI access use-case slides (including the referenced slide) to Jason Vallery. @Chris Carpenter 📅 2025-10-26 #task #proposed #auto

- [?] Confirm with Silk whether target AI use cases require real-time access to transactional systems of record or can use near-real-time copies (tens of seconds). @TBD 📅 2025-10-26 #task #proposed #auto

- [?] Clarify what topics Jai Menon cares about so the Silk executive meeting can be tailored appropriately. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Track Silk as a potential option for customer opportunities where Azure native storage offerings cannot meet required database performance. @Myself 📅 2025-10-26 🔽 #task #proposed #auto

## Key Information

- Silk is a software-defined cloud storage product focused primarily on database workloads and single source of truth systems of record, rather than large-scale HPC or hundreds-of-petabytes configurations.

- Silk stated typical scale for a single configuration is up to about 1 PB in a single zone, supporting roughly 1 to 500 databases per data pod.

- Silk claimed it can deliver tens of GB/s throughput at sub-millisecond latency for database workloads when deployed close to the database VMs.

- Silk described a two-layer architecture with a performance layer (including read cache) and a durable persistence layer, with N+X resiliency options (N+1, N+2, N+3).

- Silk said its performance layer can be placed in proximity placement groups (PPG) with database VMs to minimize latency and maximize throughput.

- Silk stated it always compresses data and can optionally deduplicate data.

- Silk stated it can persist data either to Azure Premium SSD v2 (PV2) volumes protected with Silk erasure coding, or to VMs using ephemeral media depending on architecture.

- Silk stated the limiting factor for many deployments is the throughput of the single database VM, and cited internal tests showing just under ~40 GB/s from a single host using Azure Boost VMs.

- Silk stated it does not provide file-level sharing directly, but is often used underneath a file-sharing layer running on VMs (for example Windows file sharing).

- Silk stated it frequently competes with Azure NetApp Files (ANF) and claimed it can significantly outperform ANF Ultra configurations at lower cost for certain database workloads.

- Silk stated customers are seeing unpredictable increases in load on their Silk-backed relational databases due to AI workloads (for example RAG and agentic workloads) accessing systems of record rather than secondary copies in lakehouse environments.

- Silk requested RDMA support on the front end of Azure L-series to reduce CPU overhead for their architecture.

- Silk stated they are already working with Gal Piglin’s team on the RDMA and Azure L-series topic.

- Silk said Ong told them he wanted to introduce them to Jay Menon, and Silk had not previously spoken with Jay Menon.

---

*Source: [[2025-09-15 - Silk briefed Jason on its cloud storage architecture optimized for databases and]]*