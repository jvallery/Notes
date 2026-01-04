---
type: customer
title: Two VAST designs for MAI
date: '2025-10-30'
account: Microsoft
participants:
- Jason Valleri
- Paul
- Ray
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-10-30 - Team aligned on presenting two
  VAST designs for MAI (1) an NVIDIA NCP reference.md
tags:
- type/customer
- account/microsoft
- generated
---

# Two VAST designs for MAI

**Date**: 2025-10-30
**Account**: [[Microsoft]]
**Attendees**: Jason Valleri, Paul, Ray

## Summary

Team aligned to present Microsoft MAI two VAST storage design options: an NVIDIA NCP reference-aligned high-performance pod sized around a ~40k GPU building block, plus a capacity/density-optimized Maverick 5400 option for exabyte-scale. They will deliver side-by-side tables and rack diagrams (capacity, read/write performance, rack count, power) and add Azure Blob comparison columns, emphasizing checkpoint write throughput, Kubernetes CSI/COSI integration, file+object support, monitoring/logging, and resiliency during WAN outages for isolated sites.
## Action Items
- [ ] Model NVIDIA NCP-aligned pod (~41,472 GPUs; Series 1350) with capacity, read/write performance, rack count, total power, and extrapolation toward 1 EB @Paul 📅 2025-10-30 ⏫ #task
- [ ] Validate and model capacity-optimized Maverick 5400 1 EB design (C:D ratios, performance limits, rack count, power) and note any NCP alignment gaps @Ray 📅 2025-10-30 ⏫ #task
- [ ] Produce side-by-side table and rack diagrams for both designs; update existing EnScale/Portugal deck templates @Paul 📅 2025-10-30 🔺 #task
- [ ] Provide consolidated sustained read/write performance estimates (TB/s) and total power figures for both designs @Ray 📅 2025-10-30 🔺 #task
- [ ] Add Kubernetes integration (CSI/COSI), file+object support, monitoring/logging, and offline auth/DNS resiliency notes into the deck @Paul 📅 2025-10-30 ⏫ #task
- [ ] Create Azure Blob comparison columns (racks, performance, power, capacity) and prepare a one-slide view for MAI @Jason Valleri 📅 2025-10-31 🔺 #task
- [ ] Confirm with Kushal the cluster sizes, site count, and checkpointing approach to refine performance targets @Jason Valleri 📅 2025-10-31 ⏫ #task
- [ ] Validate offline identity and RBAC behavior (JWT claims caching, internal DNS/routing) and document limits @Ray 📅 2025-11-05 ⏫ #task
- [ ] Align on MAI data movement strategy (azcopy vs service-to-service vs Sync Engine) and required tooling @Jason Valleri 📅 2025-11-07 🔽 #task

## Decisions
- Lead with NVIDIA NCP reference architecture for credibility and consistency with InScale.
- Include a second, density-first option (Maverick 5400-based) to show the range of possibilities.
- Use a ~40k GPU pod as the standard building block and extrapolate to reach ~1 EB scale.
- Focus the narrative on sustained write throughput for checkpoints and resiliency during WAN outages.
- Emphasize file+object support and Kubernetes CSI/COSI capabilities; keep control plane footprint minimal and avoid emphasizing Lifter/RPaaS.

## Key Information
- Target environment discussed: ~160k GPUs likely split across ~3 sites; single training clusters likely ~40k GPUs.
- Primary goal is local storage for checkpointing and data pre-staging independent of Azure Extended Zones; Azure Blob remains system of record.
- MAI control plane direction described as a thin, standalone AKS-led Kubernetes interface for isolated sites.
- NVIDIA NCP largest modeled pod referenced: ~41,472 GPUs with ~450 C-nodes and ~180 D-nodes (Series 1350), ~215 PB usable per pod.
- Indicative performance for that NCP pod: ~11 TB/s read and ~4–5 TB/s write (subject to attachment limits).
- Blob throughput guidance cited: ~2.5 Tbps per 100 PB (read/write symmetric) for comparison.
- MAI uses azcopy today; OpenAI uses PutBlobFromURL for service-to-service data movement.
- Single-pane monitoring/logging within VAST is positioned as a differentiator due to lack of Kusto/Log Analytics on-site.
- Resilient offline behavior needed: token/claims caching plus internal DNS/routing so GPUs continue during WAN outages.
- Decision stakeholders at Microsoft include AKS, Networking (Extended Zones), and Azure Storage; decision may escalate to Scott Guthrie.

---

*Source: [[Inbox/Transcripts/2025-10-30 - Team aligned on presenting two VAST designs for MAI (1) an NVIDIA NCP reference.md|2025-10-30 - Team aligned on presenting two VAST designs for MAI (1) an NVIDIA NCP reference]]*

## Related

- [[Jeff Denworth]]
- [[Kishore Inampudi]]
- [[Sam Altman]]
- [[Enscale deck]]
- [[Microsoft Azure Engagement Plan]]
- [[OpenAI]]
- [[CoreWeave]]
- [[Databricks]]
- [[NVIDIA]]
