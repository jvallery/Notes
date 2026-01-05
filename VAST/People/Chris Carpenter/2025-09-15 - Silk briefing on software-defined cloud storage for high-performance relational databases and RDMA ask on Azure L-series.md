---
type: "customer"
title: "Silk briefing on software-defined cloud storage for high-performance relational databases and RDMA ask on Azure L-series"
date: "2025-09-15"
account: ""
participants: ["Jason Vallery", "Chris Carpenter", "Tom (last name unknown)", "Ong (last name unknown, not present)", "Jay Menon (not present)", "J\u00fcrgen (last name unknown, not present)", "Gal (last name unknown, not present)"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-09-15 - Silk briefed Jason on its software-defined cloud storage for high-performance re.md"
tags:
  - "type/customer"
  - "account/"
  - "generated"

---

# Silk briefing on software-defined cloud storage for high-performance relational databases and RDMA ask on Azure L-series

**Date**: 2025-09-15
**Account**: [[]]
**Attendees**: Jason Vallery, Chris Carpenter, Tom (last name unknown), Ong (last name unknown, not present), Jay Menon (not present), Jürgen (last name unknown, not present), Gal (last name unknown, not present)

## Summary

Silk briefed Jason Vallery on its software-defined cloud storage optimized for high-performance relational database workloads across Azure, GCP, and AWS, with emphasis on rising AI-driven load on systems of record. The team discussed Silk architecture (data pod, cache, durability options), observed performance limits, and a feature request for RDMA support on Azure L-series to reduce CPU overhead. Next step is to pursue an introduction to Silk CEO Jay Menon via Ong and keep Silk in mind for customers exceeding Azure native storage performance.


## Action Items


- [?] Coordinate an introduction between Silk and Jay Menon via Ong. @TBD 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Provide guidance on what topics Jay Menon cares about most so the Silk introduction meeting can be tailored. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Follow up with Gal’s team on the Azure timeline and feasibility for RDMA support on Azure L-series (and any related Boost/Duo Boost configuration) for Silk front-end connectivity. @TBD 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Share customer opportunities where Azure native storage performance is insufficient and Silk could be a fit for high-performance relational database workloads. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Schedule a meeting with Jay Menon after the introduction is made. @Chris Carpenter 📅 2025-10-26 #task #proposed #auto

- [?] Prepare concise real-world use cases contrasting real-time production database acceleration versus near-real-time instant copies (tens-of-seconds lag) for AI-driven access patterns. @Tom (last name unknown) 📅 2025-10-26 🔽 #task #proposed #auto




## Decisions


- Proceed with connecting Silk to Jay Menon via Ong for an introductory discussion.




## Key Information


- Silk provides software-defined cloud storage optimized for structured relational database workloads across Azure, Google Cloud Platform, and Amazon Web Services.

- Silk is typically used for systems-of-record database workloads rather than very large HPC-style deployments, and scales to about 1 PB in a single configuration in a single zone.

- Silk architecture supports roughly 1 to 500 databases per 'data pod' and uses an n+x resilience model (for example n+1, n+2, n+3) with a performance layer that includes read cache 'cNodes' that can be placed close to database VMs (for example in a proximity placement group) to minimize latency.

- Silk persists data either to Azure PV2 volumes protected with Silk erasure coding or to a 'UCL series' durable layer using ephemeral media; Silk always compresses data and optionally deduplicates it.

- Silk reported sub-millisecond latency and tens of GB/s throughput for database workloads, including a demonstration of just under 40 GB/s throughput from a single host using Boost VMs; Silk stated the limiting factor is often the database VM physical throughput.

- Silk often competes with Azure NetApp Files (ANF) and claims it can significantly outperform ANF Ultra configurations with better cost efficiency for certain database workloads.

- Silk is seeing unpredictable increases in load on production relational databases due to AI workloads (including RAG and agentic workloads) that need access to the system-of-record rather than a secondary copy in a lakehouse.

- Silk described two customer patterns for AI-driven database access: (1) make the production database as fast as possible, or (2) create near-real-time instant copies with tens-of-seconds lag to protect production.

- Silk requested RDMA support on Azure L-series front-end connectivity to reduce CPU overhead; Silk indicated they are working with 'Gal’s team' and there was no clear Azure timeline shared in the meeting notes.

- Silk referenced customer domains including trading, retail, distribution, and healthcare, with performance spikes such as market open driving peak load.

- Ong told Silk he wanted to introduce them to Jay Menon, and Silk had not previously heard of or spoken with Jay Menon before that call.



---

*Source: [[2025-09-15 - Silk briefed Jason on its software-defined cloud storage for high-performance re]]*