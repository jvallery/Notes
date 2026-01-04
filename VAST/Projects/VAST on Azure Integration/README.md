---
type: projects
title: VAST on Azure Integration
last_contact: unknown
created: '2026-01-03'
tags:
- type/projects
- generated
---

# VAST on Azure Integration

## Recent Context

- unknown: [[Untitled]] - Forwardable write-up/email draft instructing an internal Performance team to populate Google’s “VAST... (via Google)
- unknown: [[2025-10 - Microsoft Tasks]] - Checklist of completed Microsoft-related action items for VAST’s Azure offerings, including networki... (via Microsoft)
- unknown: [[MAI Notes]] - Note references a Microsoft project called "New Azure" under Qi and Brenden, intended to create a ne... (via Microsoft)
- unknown: [[2025-10 - Kishore Inampudi]] - Follow-up task to coordinate with Kishore Enamapuri on Azure Extended Zones after A2N approval, alig... (via Kishore Inampudi)
- unknown: [[Outline]] - Outline section defining deployment variants and a workload catalog for “VAST on Azure Integration,”...
- unknown: [[Azure + VAST Integration Opportunities and Approach v2]] - Draft strategy/architecture roadmap for integrating VAST with Microsoft Azure, positioning VAST as a...
- unknown: [[Azure + VAST Integration Opportunities and Approach v1]] - Strategy and phased roadmap for integrating VAST with Microsoft Azure so customers can stage AI/HPC ...
- 2025-12-18: [[2025-12-18 1303 - New Recording]] - Brainstorming and outlining a joint document describing how VAST Data will integrate with Microsoft ...
- 2025-11-12: [[2025-11-12 - Announcements]] - Internal note summarizing SemiAnalysis and Microsoft disclosures about Microsoft’s renewed push for ... (via Microsoft)
- 2025-11-05: [[2025-11-05 - Walmart Analytics]] - Note captures Walmart’s hybrid analytics storage/replication requirements for moving a hot working s... (via Walmart)
- 2025-10-28: [[2025-10-28 - Jason and Erez aligned on delivering Azure Blob API support in VAST to enable Az]] - Weekly 1:1 between Jason Vallery and Erez Zilber aligning on delivering Azure Blob API support in VA... (via Erez Zilber)
- 2025-10-22: [[2025-10-22 - Jason shared candid guidance on Microsoft’s approach to GPU capacity preference]] - Weekly 1:1 between Jason Vallery (VAST) and Rosanne Kincaid–Smith (Dhammak Group) discussing Microso... (via Rosanne Kincaid–Smith)
- 2025-09-30: [[2025-09-30 - Jason shared that after meeting with Manish and reviewing rewards, he began expl]] - Weekly 1:1 between Jai Menon and Jason Vallery focused on Jason’s retention risk after reviewing rew... (via Jai Menon)
- 2025-09-15: [[2025-09-15 - Silk briefed Jason on its cloud storage architecture optimized for databases and]] - Weekly 1:1 where Silk briefed Jason on its software-defined cloud storage architecture optimized for... (via Silk)
- 2025-09-15: [[2025-09-15 - Silk briefed Jason on its software-defined cloud storage for high-performance re]] - Silk briefed Jason (with Chris and Tom) on Silk’s software-defined cloud storage optimized for high-... (via Silk)

## Key Facts

- Google will compare vendors primarily on IOPS per GiB and price per GiB; throughput is secondary.
- IOPS results must be reported only where mean latency is under 2 ms (apples-to-apples constraint).
- Benchmarks must have encryption enabled: IPsec for file+block, TLS for S3; encryption at rest must also be enabled with an additional tenant-granularity (or finer) layer.
- Dedupe and compression must be disabled for performance tests and random data used to avoid inflated results.
- Object tests must use a working set at least 20% of usable capacity to avoid cache-only measurements.
- Google standardizes on TiB/GiB units (not TB/GB).
- BLOCK protocol is NVMe over TCP; FILE is NFSv4; OBJECT is S3.
- Object workloads: Standard class uses 50/50 GET/PUT; Archive class uses 10/90 GET/PUT; both specify new object PUTs and uniform random GET access.
- Performance Profile tab requires fio-based mean and P95 latency vs IOPS curves for specified 8KiB and 64KiB random workloads; template appears to contain typos that should be called out as assumptions.
- VAST does not support SEDs due to HA/dual-controller key management complexity; FIPS is met via dual software-layer encryption.

## Topics

Google GDC Storage RFP spreadsheet deliverable requirements, Normalized performance and price/performance reporting (IOPS/GiB, price/GiB), Benchmarking assumptions (80/20 random, 4KiB IOPS, mean latency <2ms), Encryption requirements (in transit IPsec/TLS; at rest with tenant-level granularity), Disabling dedupe/compression and using random data for performance tests, S3 object workload definitions and working set constraints, fio latency-vs-IOPS curve generation for NVMe/TCP workloads, Handling template typos and documenting assumptions, Self-Encrypting Drives (SED) non-support and how to document it, Microsoft AI capacity expansion (self-build, leases, neocloud), Azure Foundry and token/API monetization strategy, OpenAI–Microsoft partnership terms (exclusivity, IP rights, ROFR, AGI provisions, Azure spend commitment), Accelerator roadmap and dependency risk (Nvidia, MAIA, OpenAI ASIC, AMD), Neocloud overflow strategy and cross-cloud mobility, VAST positioning and sales plays for Microsoft and OpenAI

## Related

<!-- Wikilinks to related entities -->
