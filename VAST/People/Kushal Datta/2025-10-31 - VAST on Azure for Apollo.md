---
type: people
title: VAST on Azure for Apollo
date: '2025-10-31'
person: Kushal Datta
participants:
- Kushal Datta
- Jason Vallery
source: transcript
tags:
- type/people
- person/kushal-datta
- generated
---

# VAST on Azure for Apollo

**Date**: 2025-10-31
**With**: Kushal Datta, Jason Vallery

## Summary

Jason Vallery (now at VAST Data) and Kushal Datta (Microsoft Apollo) discussed options to deploy VAST for Apollo training workloads on Azure infrastructure, comparing Azure compute-based storage, VAST bare metal on Azure Gen9 XIO, and VAST-qualified ODM hardware. They aligned on pursuing an apples-to-apples Gen9 XIO test (Azure Storage stack vs VAST bare metal) and on Kushal producing crisp requirements (throughput/capacity/power/rack) to drive a formal proposal and hardware path decisions.
## Action Items
- [ ] Draft and circulate a crisp requirements document (throughput, capacity, power, rack tiles) to drive storage selection for Apollo. @Kushal Datta 📅 2025-11-08 🔺 #task
- [ ] Start an internal thread to assess swapping Dallas Blob HDD to Premium SSD and feasibility of running VAST bare metal. @Kushal Datta 📅 2025-11-08 🔺 #task
- [ ] Provide detailed read/write throughput per GPU and final capacity targets (per site and aggregate) for ~120k GPUs. @Kushal Datta 📅 2025-11-08 🔺 #task
- [ ] Prepare a proposal/BOM for VAST-qualified ODM hardware (performance-optimized vs capacity-optimized) once requirements are received. @Jason Vallery 📅 2025-11-08 ⏫ #task
- [ ] Support and advocate internally for an apples-to-apples test on Gen9 XIO (Azure Storage stack vs VAST bare metal). @Kushal Datta 📅 2025-11-08 ⏫ #task
- [ ] Stand up VAST bare metal on Gen9 XIO for the A/B test when scheduled. @TBD 📅 2025-11-08 ⏫ #task
- [ ] Determine DPU path and qualification plan (Fungible NIC vs NVIDIA BlueField) aligned with Azure networking requirements. @TBD 📅 2025-11-08 ⏫ #task
- [ ] Confirm whether a Blob API on VAST is required alongside NFS/S3 for existing data loaders. @Kushal Datta 📅 2025-11-08 ⏫ #task
- [ ] Scope and plan Blob API support on VAST if required. @TBD 📅 2025-11-08 ⏫ #task
- [ ] Clarify which Azure storage offerings/SKUs will be available in January and April timeframes for the target sites. @Kushal Datta 📅 2025-11-08 ⏫ #task
- [ ] Schedule a follow-up meeting after requirements are finalized. @Kushal Datta 📅 2025-11-08 🔽 #task

## Key Information
- Jason Vallery moved from Microsoft Azure Storage to VAST Data and is focused on hyperscaler penetration/product management for cloud.
- Kushal Datta is on Microsoft Apollo team and is evaluating storage for large-scale training workloads.
- Dallas HDD capacity is expected to land in January; a larger capacity build is expected in April; Richmond was replaced by a larger capacity site.
- Target scale discussed: ~1 exabyte usable per site (potentially ~7 exabytes for a 350 MW site) and ~120,000 GPUs per site.
- Checkpoint writes discussed: ~100 PB/day; peak write throughput ~1–2 TB/s; required read throughput ~24 TB/s.
- Azure compute-based storage SKUs were described as inefficient for exabyte-scale storage due to compute:storage ratio and power/rack inefficiency.
- VAST can run on Azure Gen9 XIO hardware for an apples-to-apples test; Gen9 XIO uses CX5 ~40 Gbps NICs which may bottleneck throughput.
- VAST offers single namespace and supports NFS, GPU Direct Storage, and S3; VAST is considering/able to add an Azure Blob-compatible API if required.
- VAST ODM hardware can typically be delivered within ~30 days after order, subject to facility/organizational approval for third-party hardware.
- Key risks raised: Azure hardware qualification pace, internal politics, NIC/DPU choice (Fungible vs BlueField), and facility policies restricting third-party hardware.

---

*Source: [[Inbox/_archive/2025-10-31/original.md|original]]*

## Related

- [[Kushal Datta]]
- [[Jason Vallery]]
- [[Jai Menon]]
- [[Qi Ke]]
- [[Maneesh Sah]]
- [[John Mao]]
- [[Microsoft]]
- [[CoreWeave]]
- [[OpenAI]]
- [[NVIDIA]]
- [[HPE]]
- [[Supermicro]]
- [[Micron]]
- [[Solidigm]]
- [[Amazon]]
- [[Google]]
