---
type: person
name: Alon Horev
email: ''
company: ''
title: ''
last_contact: '2025-10-28'
created: '2026-01-05'
tags:
- type/person
- needs-review
---

# Alon Horev

## Key Facts

- Alon Horev will pursue a 1:1 with Muninder Singh Sambi to discuss AI approach, VM shapes, RDMA, and hardware tradeoffs for Google Distributed Cloud air-gapped deployments.

- Alon Horev was identified as a key internal stakeholder for aligning on the SyncEngine replication pattern and lessons learned to apply to Walmart.

- Alon Horev was identified as an internal stakeholder for aligning on the SyncEngine replication pattern and lessons learned from the Wave project for Walmart.

- Alon Horev suggested working with InScale and modifying their existing design to have a consistent proposal ready for Microsoft MAI.

- Jason Vallery stated he has already met and is actively chatting with Alon Horev.

- Alon Horev told Erez Zilber that Jason Vallery has understanding of OpenAI's intended use of VAST as an Azure Blob-compatible storage server.

- Jason Vallery considered establishing a weekly or monthly 1:1 cadence with Alon Horev for coordination on cloud-related work.

- Alon Horev was identified as a coordination point for making Confluence the canonical home for FRDs and customer requirements.

- Alon Horev has prior touchpoints with SSI (Safe Superintelligence Inc.) and can provide a quick read on SSI contacts including Daniel Levy.
## Recent Context

- 2025-11-14: Mentioned in: Google Distributed Cloud RFP debrief and federal coordination (air-gapped focus)

- 2025-11-06: Mentioned in: Walmart hybrid lakehouse architecture prep, SyncEngine + DataSpaces approach and Q4 two-cluster pilot

- 2025-10-31: Microsoft Apollo aligned on two-track evaluation for VAST AI cloud storage (Azure lab software validation + VAST loaner hardware POC)

- 2025-10-30: Mentioned in: MAI storage proposal: two VAST designs (NVIDIA NCP-aligned 40k GPU pod + Maverick 5400 density option) and deck deliverables

- 2025-10-28: Mentioned in: 1:1 with Shachar Feinblit, weekly cadence and Tel Aviv visit planning (Nov 23-26, 2025)

- 2026-01-05: Weekly 1:1 with Lior Genzel, MAI stakeholder mapping and Davos exec meeting setup

- 2025-10-28: Mentioned in: 1:1 with Erez Zilber, Azure Blob API support for OpenAI and Azure Marketplace

- 2025-10-28: Jason Vallery and Alon Horev aligned on Microsoft AI Infrastructure (MAI) context ahead of Jason's F...

- 2026-01-05: Mentioned in: 1:1 with Jeff Denworth - travel planning, scope ownership, and cloud team alignment

- 2025-11-07: Mentioned in: Org map, priorities, and cloud strategy alignment (1:1 with Jeff Denworth)

- 2025-11-07: Mentioned in: Warm intros and outreach planning for priority model builders (LinkedIn, investors, NVIDIA, NeoClouds)
## Tasks

```tasks
path includes Alon Horev
not done
```

## Topics

- Microsoft AI Infrastructure (MAI) org context, including Kushal's role and relationship to Mustafa

- Falcon rollout plan: Phoenix, Dallas, Richmond, AI WAN interconnect, and storage sizing assumptions

- MAI operational blockers: control plane fragility and GPU issues limiting Falcon utilization

- Implications of OpenAI GPT-4.5 training experience on cluster scaling philosophy

- Project Apollo architecture: AKS-led slim control plane for single-tenant GPU sites and VAST integration opportunity

## Key Decisions

- Alon Horev will wait until after Jason Vallery's Friday meeting with Kushal before following up with Vipin to avoid misalignment and to incorporate the latest MAI direction.

- VAST Data will prioritize Project Apollo (AKS-led slim control plane for single-tenant GPU sites) as the primary entry path into Microsoft MAI and Azure-adjacent deployments, rather than relying on Azure Marketplace VM offers (LSv4/LSv5).

- VAST Data will use success in Microsoft AI Infrastructure (MAI) as a wedge to influence broader Azure storage strategy and to justify a longer-term Azure hardware qualification path.

- Blob API compatibility will be treated as exploratory; near-term focus remains on performance outcomes that keep GPUs utilized in MAI environments.