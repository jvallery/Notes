---
type: "customer"
title: "MAI exabyte storage options"
date: "2025-10-30"
account: "Microsoft"
participants: ["Jason Vallery", "Paul", "Ray"]
source: "transcript"
source_ref: "Inbox/_archive/2025-10-30/2025-10-30 - Team aligned on presenting two exabyte-scale storage options for MAI (1) an NVI.md"
tags:
  - "type/customer"
  - "account/microsoft"
  - "generated"
---

# MAI exabyte storage options

**Date**: 2025-10-30
**Account**: [[Microsoft]]
**Attendees**: Jason Vallery, Paul, Ray

## Summary

Team aligned on presenting Microsoft MAI two exabyte-scale storage options: an NVIDIA NCP-aligned high-performance pod (~41,472 GPUs) as the baseline building block, and a high-density Maverick 5400 capacity-optimized exabyte alternative with performance trade-offs. The deck will emphasize AKS-led standalone control plane fit for neo-cloud/leased sites, local storage for checkpointing during WAN outages, Kubernetes integration (CSI/COSI), file+object support, and single-pane monitoring/logging; pricing will be avoided. Materials (rack layouts and side-by-side metrics) are to be produced for a MAI call the next day, with a separate Azure Blob comparison prepared for follow-on discussions.
## Action Items
- [ ] Draft NCP-aligned design slides and rack diagrams for a 41,472-GPU pod (≈450 C / 180 D, ≈215 PB usable) and extrapolate to 1 EB. @Paul 📅 2025-10-30 ⏫ #task
- [ ] Compile performance, capacity, and power metrics for the NCP pod and produce a side-by-side metrics table. @Ray 📅 2025-10-30 ⏫ #task
- [ ] Design capacity-optimized Maverick 5400 exabyte option and rack layout; include C:D ratio variants (e.g., 420:210 and 105:210). @Paul 📅 2025-10-30 ⏫ #task
- [ ] Model read/write performance and power for the Maverick option at chosen C:D ratios and validate backend media limits. @Ray 📅 2025-10-30 🔺 #task
- [ ] Add bullets on Kubernetes (CSI/COSI), file+object support, single-pane monitoring/logging, and offline auth/DNS resiliency to the deck. @Paul 📅 2025-10-30 🔺 #task
- [ ] Create a one-slide/Excel view adding Azure Blob comparison columns for the 1 EB reference. @Jason Vallery 📅 2025-10-31 🔺 #task
- [ ] Join MAI call to present the architecture and answer technical questions. @Paul 📅 2025-10-31 🔺 #task
- [ ] Join MAI call to present performance/power modeling and NCP alignment. @Ray 📅 2025-10-31 🔺 #task
- [ ] Confirm MAI checkpointing method and sustained write throughput targets during 1:1. @Jason Vallery 📅 2025-10-31 ⏫ #task
- [ ] Validate distribution of 160k GPUs across sites/pods and max non-blocking cluster size with MAI. @Jason Vallery 📅 2025-10-31 ⏫ #task
- [ ] Clarify MAI data movement standard (azcopy vs PutBlobFromURL pipelines vs Sync Engine) and implications for design. @Jason Vallery 📅 2025-11-05 ⏫ #task
- [ ] Confirm NVIDIA acceptance/certification posture for Maverick-based capacity-optimized design. @Ray 📅 2025-11-05 ⏫ #task

## Decisions
- Use NVIDIA NCP reference architecture as the lead option for MAI (~41,472 GPU pod, ~215 PB usable).
- Include a capacity-optimized Maverick 5400 exabyte option as an alternative focused on density and power.
- Reference 1 EB as the comparison baseline across options.
- Defer direct Azure Blob comparison in the next-day call; prepare it for follow-on stakeholder discussions.
- Do not emphasize Azure Lifter/RPaaS APIs; prioritize thin, standalone control-plane compatibility.
- Keep proposal messaging consistent with NScale and avoid pricing; focus on architecture and benefits.

## Key Information
- Target environment is ~160k GPUs likely split across ~3 sites; propose sizing per ~40k GPU training clusters.
- NVIDIA NCP pod baseline: ~41,472 GPUs with ~450 C-nodes and ~180 D-nodes; ~215 PB usable per pod.
- Baseline performance per pod: ~11 TB/s read and ~4–5 TB/s write.
- Maverick 5400 density: ~5.4 PB per 2U; exabyte-class build is ~210 Mavericks usable after erasure coding.
- Maverick rack density estimate: ~30 racks for ~1 EB; 1350-series would require ~4–5x more racks.
- Azure Blob reference throughput: ~2.5 Tbps per 100 PB; ~25 Tbps per 1 EB aggregate.
- AKS is driving a thin, standalone control plane for leased/neo-cloud sites to reduce dependency on an Azure region.
- Extended Zones introduce WAN dependency; local storage is needed for checkpointing and pre-staging to avoid GPU idling.
- Data movement today: OpenAI uses PutBlobFromURL pipelines; MAI uses azcopy with scripting; VaST Sync Engine is optional/needs fit.
- Interfaces expected: Kubernetes CSI/COSI; file and object likely required (MAI prefers file, moving to object).
- Single-pane monitoring/logging in VaST is valuable because Azure Log Analytics/Kusto are typically unavailable in these sites.

---

*Source: [[Inbox/_archive/2025-10-30/2025-10-30 - Team aligned on presenting two exabyte-scale storage options for MAI (1) an NVI.md|2025-10-30 - Team aligned on presenting two exabyte-scale storage options for MAI (1) an NVI]]*

## Related

- [[Jason Vallery]]
- [[Jeff Denworth]]
- [[Kishore Inampudi]]
- [[Sam Altman]]
- [[Cloud control plane]]
- [[CoreWeave]]
- [[OpenAI]]
- [[Databricks]]
