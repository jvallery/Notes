---
type: projects
title: Cloud
last_contact: unknown
created: '2026-01-03'
tags:
- type/projects
- generated
---

# Cloud

## Recent Context

- unknown: [[2025-10 - Yogev Vankin]] - A completed task to summarize Oracle Cloud POC learnings and the current AWS/GCP/Azure cluster statu... (via Yogev Vankin)
- unknown: [[2025-10 - SaaS]] - Drafted the cloud SaaS operating model requirements for VAST Cloud, covering DevOps/LifeSite rotatio...
- unknown: [[Available Capacity Calculations]] - Internal note arguing against using a single fixed overhead percentage (e.g., 35%) for cloud deploym...
- unknown: [[2025-10 - Cloud Marketplace MVP]] - Checklist of completed Product, Marketing, and Performance Team deliverables for a Cloud Marketplace...
- unknown: [[Pricing]] - Internal note to the Pricing v-team outlining principles and a recommended direction for VAST Cloud ... (via Pricing)
- 2025-11-14: [[2025-11-14 - Internal sync to align on Walmart’s big data initiative, clarify requirements, a]] - Internal team sync to align on Walmart’s big data initiative, focusing on clarifying disaster recove... (via Walmart)
- 2025-11-03: [[2025-11-03 - Team reviewed how cloud clusters must map to Salesforce assets (AccountSitePSN]] - Group meeting reviewing how VAST cloud clusters must map to Salesforce assets (Account/Site/Cluster ...
- 2025-10-30: [[2025-10-30 - Intro 1-1 between Jason and Dre. Dre outlined SE enablement cadence and an S3Ob]] - Intro 1:1 between Jason Vallery and Deandre (Dre) Jackson focused on aligning cloud enablement messa... (via Deandre Jackson)
- 2025-10-30: [[2025-10-30 - The group aligned on the cloud support operating model (Customer Success, Suppor]]
- 2025-10-28: [[2025-10-28 - Cloud BU leadership aligned on a dual-track strategy (1) ship GCP MVP via marke]]
- 2025-10-22: [[2025-10-22 - Rosanne outlined Dhammak’s rapid data center and GPU cloud buildout and interest]] - Weekly 1:1 where Rosanne described Dhammak/Dimac’s rapid data center and GPU cloud buildout and desi... (via Rosanne Kincaid–Smith)
- 2025-10-20: [[2025-10-20 - Discussed cloud architectures for VAST on AWSGCPAzure, the need for object-sto]] - Weekly 1:1 with Yogev Vankin focused on VAST multi-cloud architecture across AWS/GCP/Azure, centerin... (via Yogev Vankin)
- 2025-10-06: [[2025-10-06 - Jason updated Jai that he has a complex, high-variance offer from VAST and an ex]] - Weekly 1:1 between Jai Menon and Jason Vallery focused on Jason’s competing job offers (VAST vs Crus... (via Jai Menon)
- 2025-09-15: [[2025-09-15 - Silk briefed Jason on its cloud storage architecture optimized for databases and]] - Weekly 1:1 where Silk briefed Jason on its software-defined cloud storage architecture optimized for... (via Silk)

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

Silk cloud storage architecture for database workloads, AI-driven access patterns to systems of record, Performance characteristics: throughput, latency, TPS, Real-time vs near-real-time copies for AI access, Competitive positioning vs Azure NetApp Files (ANF) and Azure native storage, RDMA front-end support on Azure L-series and CPU overhead reduction, Executive introduction planning (Jay Menon via Ong), Walmart big data initiative alignment, Disaster recovery (DR) requirements clarification, Architecture/whiteboarding session gating criteria, Hybrid cloud roadmap strategy, Native Google Cloud Storage (GCS) integration requirements, Proposal options: minimum config vs phase-one (D-box/capacity differences), Customer timeline and decision process, Scaling limitations of VM-based cloud deployments

## Related

<!-- Wikilinks to related entities -->
