---
type: people
title: Silk briefing on software-defined cloud storage for high-performance database workloads on Azure
date: '2025-09-15'
participants:
- Jason Vallery
- Chris Carpenter
- Tom (Silk, last name unknown)
- Jürgen (last name unknown)
- Ong (last name unknown)
- Remote (Silk, name unknown)
source: transcript
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-09-15 - Silk briefed Jason on their software-defined cloud storage for databases, emphas.md
tags:
- type/people
- generated
person: Chris Carpenter
---

# Silk briefing on software-defined cloud storage for high-performance database workloads on Azure

**Date**: 2025-09-15
**Attendees**: Jason Vallery, Chris Carpenter, Tom (Silk, last name unknown), Remote (Silk, name unknown)

## Summary

Silk briefed Jason Vallery, with Chris Carpenter present, on Silk's software-defined cloud storage optimized for structured database workloads, highlighting sub-millisecond latency and tens of GB/s throughput at up to ~1 PB per pod. The discussion focused on AI-driven, unpredictable spikes hitting systems of record, patterns to either accelerate production databases or create near-real-time clones, and a request for RDMA support on Azure L-series to reduce CPU overhead.

## Action Items

- [?] Confirm whether Azure L-series supports RDMA for Silk's front-end access path, identify the feasibility and any available timeline guidance, and report back to Silk. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Schedule and prepare a follow-up meeting with Jay Menon (Microsoft Apollo storage side) and Silk, including a clear agenda and desired outcomes for all parties. @Chris Carpenter 📅 2025-10-26 #task #proposed #auto

- [?] Flag customer opportunities where native Azure storage performance is insufficient for high-performance transactional database workloads and consider Silk as an option. @Myself 📅 2025-10-26 🔽 #task #proposed #auto

- [?] Compile concrete customer use cases that require real-time access to transactional systems versus near-real-time clones (tens of seconds behind) to inform the discussion with Jay Menon. @TBD 📅 2025-10-26 #task #proposed #auto

- [?] Confirm feasibility and any available timeline for enabling RDMA support on Azure L-series for Silk front-end access, coordinating with Gal Piglin's team (Microsoft contact referenced in notes as 'Gal Piglin’s team'). @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Schedule and prepare a follow-up meeting with Jay Menon, including a clear agenda that is valuable for both Microsoft and Silk (focus areas: RDMA on L-series, database performance patterns, and AI-driven access spikes). @Chris Carpenter 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Identify and flag customer opportunities where native Azure storage cannot meet required database performance, and consider Silk as an option for those workloads. @Myself 📅 2025-10-26 🔽 #task #proposed #auto

## Decisions

- Proceed with setting up an introduction and follow-up meeting involving Jay Menon (Microsoft Apollo storage side) to discuss Silk's database acceleration approach and Azure platform needs.

- Evaluate customer-by-customer whether the right pattern is accelerating the production database directly versus creating near-real-time database clones that are tens of seconds behind for AI/agentic access.

- Proceed with setting up an introduction and follow-up meeting with Jay Menon (Microsoft Apollo storage team) to discuss Silk and relevant Azure storage/RDMA topics.

- Evaluate customer-by-customer whether the right pattern is accelerating the production database directly or creating near-real-time cloned copies that lag by tens of seconds.

## Key Information

- Silk is a software-defined cloud storage product primarily used to accelerate structured database workloads and is not designed for file-level sharing as a primary use case.

- Silk typically scales to about 1 PB of capacity in a single configuration (single zone) and supports roughly 1 to 500 databases per 'data pod'.

- Silk targets very low latency and high throughput for database IO, described as sub-millisecond latency and tens of GB/s throughput, with a cited example of just under ~40 GB/s from a single host using Azure Boost VMs.

- Silk architecture includes a performance layer with a read cache, deployed in an N+X resiliency model (for example N+1, N+2, N+3), and can be placed close to database VMs using Azure Proximity Placement Groups (PPG) to minimize latency.

- Silk persists data to Azure PV2 volumes protected with Silk's own erasure coding, and data is always compressed with optional deduplication.

- Silk reports increasing customer load driven by AI workloads (RAG and agentic access) that need to query or access the system-of-record relational database rather than a secondary copy in a lakehouse.

- Silk often competes with Azure NetApp Files (ANF) for database acceleration use cases and positions itself as able to outperform ANF in some configurations.

- Silk requested RDMA support on Azure L-series for Silk's front-end access path to reduce CPU overhead and improve performance.

- Ong (last name unknown) told Silk he wanted to introduce them to Jay Menon at Microsoft, and Silk had not previously interacted with Jay Menon before that suggestion.

---

- Silk is a software-defined cloud storage product primarily used for structured database workloads and single system-of-record deployments, not for file-level sharing.

- Silk scales to approximately 1 PB capacity in a single configuration (single zone) and supports roughly 1 to 500 databases per data pod.

- Silk architecture includes a performance layer with read cache and N+X resiliency (for example N+1, N+2, N+3) and can place performance nodes close to database VMs using Azure Proximity Placement Groups (PPG) to minimize latency.

- Silk persists data either to VM ephemeral media or to Azure PV2 volumes, adding its own erasure coding; data is always compressed and can be optionally deduplicated.

- Silk reports that AI workloads (RAG and agentic access patterns) are increasing unpredictable load on customers' relational systems of record, and customers increasingly want models/agents to access the relational source of truth rather than only a secondary copy in a lakehouse.

- Silk often competes with Azure NetApp Files (ANF) for these database performance use cases and claims it can significantly outperform ANF in some ultra configurations for the targeted workloads.

- Silk requested RDMA access on Azure L-series for Silk's front end to reduce CPU overhead and improve performance.

- Chris Carpenter attended the Silk briefing with Jason Vallery and helped present/share Silk materials during the call due to screen sharing issues.
