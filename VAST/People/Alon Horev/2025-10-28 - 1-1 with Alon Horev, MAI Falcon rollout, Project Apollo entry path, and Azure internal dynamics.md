---
type: people
title: 1:1 with Alon Horev, MAI Falcon rollout, Project Apollo entry path, and Azure internal dynamics
date: '2025-10-28'
person: Alon Horev
participants:
- Jason Vallery
- Alon Horev
source: transcript
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-28 - Discussed Microsoft AI (MAI) landscape, Falcon capacity rollout, and Azure dynam.md
tags:
- type/people
- generated
---

# 1:1 with Alon Horev, MAI Falcon rollout, Project Apollo entry path, and Azure internal dynamics

**Date**: 2025-10-28
**With**: Jason Vallery, Alon Horev

## Summary

Jason Vallery and Alon Horev aligned on Microsoft AI Infrastructure (MAI) context ahead of Jason's Friday meeting with Kushal, focusing on MAI Falcon capacity rollout, MAI control plane fragility, and VAST's best entry path. They agreed to prioritize Project Apollo (AKS-led slim control plane for single-tenant GPU sites) over Azure Marketplace SKUs, use MAI success as a wedge for broader Azure adoption, and treat Blob compatibility as exploratory while emphasizing near-term GPU-utilization performance wins.

## Action Items

- [?] Meet with Kushal (Microsoft AI Infrastructure) on Friday, 2025-10-31, to discuss potential VAST Data deployment options for MAI outside Azure data centers and clarify target site, scale, timelines, and hardware profile. @Myself 📅 2025-10-31 ⏫ #task #proposed #auto

- [?] Send detailed notes to Alon Horev after the 2025-10-31 Kushal meeting, including MAI deployment scope, decision owners, and next-step recommendations for engaging Vipin and AKS/Apollo stakeholders. @Myself 📅 2025-10-31 ⏫ #task #proposed #auto

- [?] Follow up with Vipin after receiving Jason Vallery's notes from the 2025-10-31 Kushal meeting to align on MAI path and probe AKS and Project Apollo integration angles for VAST Data. @Alon Horev 📅 2025-11-03 #task #proposed #auto

- [?] Maintain close collaboration with Lior Genzel and Tiffany (last name not provided) to position VAST Data for Project Apollo storage integration, including identifying required control plane and topology work. @Myself 📅 2025-11-15 #task #proposed #auto

- [?] Map Azure stakeholders across AKS/Project Apollo, Azure Storage, Azure Compute, and Azure Hardware, including their incentives and decision rights for adopting third-party storage in Apollo-like sites. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Engage Azure Hardware (Ronnie Booker's team) to understand requirements and process for qualifying a VAST-friendly storage-optimized SKU, acknowledging this is likely a multi-year path. @Myself 📅 2025-11-22 🔽 #task #proposed #auto

- [?] Explore liquid-cooled storage SKU options with ODM partners to support data center cooling fungibility and late-binding storage vs GPU rack decisions for MAI and Apollo-like deployments. @Myself 📅 2025-12-06 🔽 #task #proposed #auto

- [?] Evaluate strategic value and feasibility of Blob API compatibility and a multi-protocol head (Blob plus S3), including testing interest with Microsoft Azure contacts and identifying control plane integration hurdles. @Myself 📅 2025-12-06 🔽 #task #proposed #auto

- [?] Confirm whether the reported Microsoft contract with Nscale is intended for MAI and assess any implications or opportunities for a VAST Data deployment. @Myself 📅 2025-11-15 🔽 #task #proposed #auto

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

- Alon Horev will wait until after Jason Vallery's Friday meeting with Kushal before following up with Vipin to avoid misalignment and to incorporate the latest MAI direction.

- VAST Data will prioritize Project Apollo (AKS-led slim control plane for single-tenant GPU sites) as the primary entry path into Microsoft MAI and Azure-adjacent deployments, rather than relying on Azure Marketplace VM offers (LSv4/LSv5).

- VAST Data will use success in Microsoft AI Infrastructure (MAI) as a wedge to influence broader Azure storage strategy and to justify a longer-term Azure hardware qualification path.

- Blob API compatibility will be treated as exploratory; near-term focus remains on performance outcomes that keep GPUs utilized in MAI environments.

- Alon Horev will wait until after Jason Vallery’s Friday meeting with Kushal before following up with Vipin about MAI and Project Apollo alignment.

- VAST will prioritize Project Apollo (AKS-led slim control plane for single-tenant GPU sites) as the first entry path into Microsoft MAI and adjacent deployments, rather than relying on Azure Marketplace VM offers (LSv4/LSv5).

- VAST will use MAI success as a wedge to influence broader Azure storage strategy and to start the longer hardware qualification path for first-party Azure SKUs.

- Blob API compatibility will be treated as exploratory; near-term emphasis will remain on performance outcomes that keep GPUs utilized.

## Key Information

- Kushal (former Inflection, now in Microsoft AI Infrastructure under Mustafa) reconnected with Jason Vallery and scheduled a Friday meeting to discuss using VAST Data outside Azure data centers.

- Microsoft AI Infrastructure (MAI) Falcon capacity plan includes Phoenix, Dallas, and Richmond, Virginia, each designed for about 40,000 GPUs, connected by Microsoft's AI WAN (petabits of point-to-point fiber).

- Initial MAI Falcon storage tranche was described as approximately 3 EB of Azure Blob storage.

- MAI has struggled to effectively use Falcon capacity due to control plane fragility and GPU issues.

- OpenAI GPT-4.5 training was described as a multi-island run lasting about nine months, peaking around 100,000 H100 GPUs, with disappointing outcomes that shifted philosophy away from ever-bigger clusters.

- MAI has explored online reinforcement learning continuous learning with trainers in Phoenix and generators elsewhere, targeting a tight loop of about 60 seconds.

- Vipin presented VAST Data internally at Microsoft and valued VAST's global namespace, quotas, capacity estimation, and QoS, and acknowledged Azure Blob cannot match VAST performance.

- Microsoft reportedly closed a large contract with Nscale, but the end customer was not disclosed.

- Project Apollo is described as an AKS-led effort to deliver a slim control plane for single-tenant GPU sites that lease power and space, avoiding full Azure region overhead.

- Azure Storage does not currently have a deployable solution for Apollo-like sites, and AKS has explored a thin VAST control plane and topology as an option.

- Azure Marketplace VM offers such as LSv4 and LSv5 were viewed as not price-performance competitive for VAST Data at scale.

- Azure Compute leadership incentives favor keeping workloads on Azure first-party services, creating potential internal resistance to third-party storage adoption.

- A first-party Azure hardware qualification path for VAST-friendly SKUs likely runs through Azure Hardware leadership associated with Ronnie Booker and is expected to be a multi-year effort.

- Liquid-cooled storage SKUs were discussed as a way to improve data center cooling fungibility and enable late-binding decisions between storage and GPU rack deployments.

- Blob API was characterized as Microsoft-specific legacy; S3 compatibility remains broadly attractive, and a multi-protocol head (Blob plus S3) could broaden appeal but faces control plane integration hurdles.

---

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

- A likely path to first-party Azure SKUs for VAST would run through Azure Hardware leadership (referenced as Ronnie Borker) and is expected to be a multi-year effort.

- Blob API compatibility was characterized as Microsoft-specific legacy, while S3 compatibility remains broadly attractive; a multi-protocol head (Blob plus S3) could broaden appeal but faces Azure control plane integration hurdles.
