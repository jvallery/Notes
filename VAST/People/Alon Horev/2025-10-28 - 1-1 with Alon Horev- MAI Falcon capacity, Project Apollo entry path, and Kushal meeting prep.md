---
type: "people"
title: "1:1 with Alon Horev: MAI Falcon capacity, Project Apollo entry path, and Kushal meeting prep"
date: "2025-10-28"
person: ""
participants: ["Jason Vallery", "Alon Horev"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-28 - Discussed Microsoft AI (MAI) landscape, Falcon capacity rollout, and Azure dynam.md"
tags:
  - "type/people"
  - "person/"
  - "generated"

---

# 1:1 with Alon Horev: MAI Falcon capacity, Project Apollo entry path, and Kushal meeting prep

**Date**: 2025-10-28
**With**: Jason Vallery, Alon Horev

## Summary

Jason Vallery and Alon Horev aligned on Microsoft AI Infrastructure (MAI) context ahead of Jason’s Friday meeting with Kushal, including Falcon capacity rollout constraints and Azure internal dynamics. They agreed to prioritize Project Apollo (AKS-led slim control plane for single-tenant GPU sites) as the near-term entry path for VAST, while treating Blob compatibility as exploratory and focusing near-term on performance wins that keep GPUs utilized.


## Action Items


- [?] Meet Kushal (Microsoft MAI) to discuss a potential VAST deployment outside Microsoft Azure data centers and clarify target site, scale, timeline, and hardware profile. @Myself 📅 2025-10-31 ⏫ #task #proposed #auto

- [?] Send notes from the Kushal meeting to Alon Horev to inform follow-up with Vipin and next steps on MAI and Project Apollo. @Myself 📅 2025-10-31 ⏫ #task #proposed #auto

- [?] Follow up with Vipin after receiving Jason Vallery’s notes to align on MAI path and probe AKS and Project Apollo angles (including whether Vipin spoke with Anson and Keek in AKS). @Alon Horev #task #proposed #auto

- [?] Stay closely aligned with Lior Genzel and Tiffany (last name not provided) to advance VAST storage integration positioning for Project Apollo. @Myself #task #proposed #auto

- [?] Map Microsoft Azure stakeholders across AKS/Project Apollo, Azure Storage, Azure Compute, and Azure Hardware, including their incentives and priorities for third-party storage adoption. @Myself #task #proposed #auto

- [?] Engage Azure Hardware leadership (Ronnie Booker’s team) to explore qualifying a VAST-friendly storage-optimized SKU and understand the multi-year first-party qualification path. @Myself 🔽 #task #proposed #auto

- [?] Explore liquid-cooled storage SKU options with ODM partners to support data center cooling fungibility and late-binding storage vs GPU rack decisions for MAI and Apollo-like sites. @Myself 🔽 #task #proposed #auto

- [?] Evaluate Blob API compatibility and a multi-protocol head (Blob plus S3), and test interest with Microsoft Azure contacts while accounting for Azure control plane integration hurdles. @Myself 🔽 #task #proposed #auto

- [?] Confirm whether the reported Microsoft contract with Nscale is intended for MAI and assess implications for a potential VAST deployment. @Myself 🔽 #task #proposed #auto




## Decisions


- Alon Horev will wait until after Jason Vallery’s Friday meeting with Kushal before following up with Vipin about MAI and Project Apollo alignment.

- VAST will prioritize Project Apollo (AKS-led slim control plane for single-tenant GPU sites) as the first entry path into Microsoft MAI and adjacent deployments, rather than relying on Azure Marketplace VM offers (LSv4/LSv5).

- VAST will use MAI success as a wedge to influence broader Azure storage strategy and to start the longer hardware qualification path for first-party Azure SKUs.

- Blob API compatibility will be treated as exploratory; near-term emphasis will remain on performance outcomes that keep GPUs utilized.




## Key Information


- Kushal (former Inflection, now part of Microsoft AI Infrastructure under Mustafa) reconnected with Jason Vallery and scheduled a Friday meeting to discuss using VAST outside Microsoft Azure data centers.

- Microsoft AI Infrastructure (MAI) Falcon capacity plan includes three sites, Phoenix, Dallas, and Richmond, each sized for roughly 40,000 GPUs, connected by Microsoft 'AI WAN' high-bandwidth fiber links.

- The initial MAI Falcon storage tranche was described as approximately 3 EB of Azure Blob storage.

- MAI has struggled to effectively utilize Falcon GPU capacity due to control plane fragility and GPU-related issues.

- OpenAI GPT-4.5 training was described as a multi-island run lasting about nine months and peaking around 100,000 NVIDIA H100 GPUs, with disappointing results that shifted thinking away from ever-larger clusters.

- MAI is exploring online reinforcement learning continuous learning workflows with trainers in Phoenix and generators elsewhere, targeting a tight feedback loop of roughly 60 seconds.

- Vipin presented VAST internally at Microsoft and valued VAST capabilities including global namespace, quotas, capacity estimation, and QoS, and acknowledged Azure Blob cannot match VAST performance.

- Microsoft reportedly closed a large contract with Nscale, but the end customer was not disclosed in the notes.

- Project Apollo is described as an AKS-led effort to create a slim control plane for single-tenant GPU sites that lease power and space, avoiding full Azure region overhead.

- Azure Storage does not currently have a deployable solution for Apollo-like sites, and AKS is exploring a thin VAST control plane and topology for those deployments.

- Azure Marketplace VM offers such as LSv4 and LSv5 were assessed as not price-performance competitive for VAST at scale.

- Azure Compute leadership incentives favor keeping workloads on Azure first-party services, creating potential internal resistance to third-party storage adoption.

- A likely path to first-party Azure SKUs for VAST would run through Azure Hardware leadership (referenced as Ronnie Borker) and is expected to be a multi-year effort.

- Liquid-cooled storage SKUs were discussed as a way to improve data center cooling fungibility and enable late-binding decisions between storage and GPU rack deployments.

- Blob API compatibility was characterized as Microsoft-specific legacy, while S3 compatibility remains broadly attractive; a multi-protocol head (Blob plus S3) could broaden appeal but faces Azure control plane integration hurdles.



---

*Source: [[2025-10-28 - Discussed Microsoft AI (MAI) landscape, Falcon capacity rollout, and Azure dynam]]*