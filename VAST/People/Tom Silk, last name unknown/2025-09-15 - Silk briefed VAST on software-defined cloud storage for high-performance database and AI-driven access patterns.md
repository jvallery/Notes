---
type: "customer"
title: "Silk briefed VAST on software-defined cloud storage for high-performance database and AI-driven access patterns"
date: "2025-09-15"
account: ""
participants: ["Jason Vallery", "Tom (Silk, last name unknown)", "Chris (Silk, last name unknown)", "Remote (Silk, name unknown)", "J\u00fcrgen (last name unknown, mentioned only)", "Ong (last name unknown, mentioned only)", "Jay Menon", "Gal Piglin"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-09-15 - Silk briefed Jason on its cloud storage architecture optimized for databases and.md"
tags:
  - "type/customer"
  - "account/"
  - "generated"

---

# Silk briefed VAST on software-defined cloud storage for high-performance database and AI-driven access patterns

**Date**: 2025-09-15
**Account**: [[]]
**Attendees**: Jason Vallery, Tom (Silk, last name unknown), Chris (Silk, last name unknown), Remote (Silk, name unknown), Jürgen (last name unknown, mentioned only), Ong (last name unknown, mentioned only), Jay Menon, Gal Piglin

## Summary

Silk briefed Jason Vallery on its software-defined cloud storage architecture optimized for relational databases and single source-of-truth workloads, including performance characteristics and deployment patterns near database VMs. The team discussed increasing AI-driven access to production databases, Silk's competitive positioning versus Azure NetApp Files, and Silk's request for RDMA support on the Azure L-series front end to reduce CPU overhead. Next steps include an intro path to Jay Menon via Ong and follow-up with Gal Piglin’s team on RDMA feasibility.


## Action Items


- [?] Coordinate with Ong (last name unknown) to schedule an introduction meeting between Silk and Jai Menon (Microsoft Apollo storage side). @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Check feasibility and status of RDMA front-end support for Azure L-series for Silk’s database storage use case with Gal Piglin’s team. @Myself 📅 2025-10-27 ⏫ #task #proposed #auto

- [?] Send Silk architecture and real-time vs near-real-time AI access use-case slides (including the discussed slide) to Jason Vallery. @Chris (Silk, last name unknown) 📅 2025-10-26 #task #proposed #auto

- [?] Confirm with Silk whether target AI use cases require real-time access to transactional systems of record or can use near-real-time copies (for example, tens-of-seconds lag). @Tom (Silk, last name unknown) 📅 2025-10-26 #task #proposed #auto

- [?] Clarify what topics Jai Menon cares about so the Silk executive meeting can be tailored to Microsoft Apollo storage priorities. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Track Silk as an option for customer opportunities where Azure native storage offerings (for example, Azure NetApp Files) cannot meet required database performance. @Myself 📅 2025-10-26 🔽 #task #proposed #auto






## Key Information


- Silk is a software-defined cloud storage product primarily used for relational database workloads and single source-of-truth systems, not typically for very large HPC-style hundreds-of-petabytes deployments.

- Silk typically scales to about 1 PB in a single configuration in a single cloud zone and targets tens of GB/s throughput with sub-millisecond latency for database workloads.

- Silk architecture supports roughly 1 to 500 databases per 'data pod' and uses a performance layer with read cache deployed in an N+X resiliency model (N+1, N+2, N+3 depending on customer requirements).

- Silk positions its performance nodes (cache nodes) close to database VMs, including in Azure Proximity Placement Groups (PPG), to minimize latency and maximize throughput.

- Silk persists data either to protected Azure PV2 volumes using Silk-managed erasure coding or to VMs using ephemeral media, and it always compresses data with optional deduplication.

- Silk reported internal testing showing just under ~40 GB/s throughput from a single host using 'Boost VMs', aiming to improve performance for database environments constrained by single-VM throughput.

- Silk often competes with Azure NetApp Files (ANF) and claims it can significantly outperform ANF Ultra configurations with more cost-efficient solutions for certain database workloads.

- Silk stated it does not provide file-level sharing directly, and it is sometimes deployed under a file-sharing layer running on VMs (for example, Windows file sharing).

- Silk is seeing unpredictable increases in load on production relational systems because AI workloads (for example RAG and agentic workloads) increasingly access systems of record rather than secondary copies in a lakehouse.

- Silk requested RDMA support on the Azure L-series front end to reduce CPU overhead and indicated they are already working with Gal Piglin’s team on this topic.

- Ong told Silk he wanted to introduce them to Jay Menon, and Silk had not previously heard of or spoken with Jay Menon before that conversation.



---

*Source: [[2025-09-15 - Silk briefed Jason on its cloud storage architecture optimized for databases and]]*