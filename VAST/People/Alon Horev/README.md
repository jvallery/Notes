---
type: people
email: alon@vastdata.com
company: VAST Data
title: Alon Horev
last_contact: '2025-12-01'
created: '2026-01-05'
tags:
- type/people
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

- Lior Genzel messaged Alon Horev to strategize options for where to run Anson (Qi)'s VAST PoC at 1,000 to 2,000 GPU scale.

- Alon Horev stated that Violet should be the primary person to work with on encryption and related RFP matters for Google Distributed Cloud.

- Alon Horev is leading AI Model Builder sessions for VAST Forward (as of 2025-12-23 program update).

- Lior Genzel reported that Kushal requested a meeting with Alon Horev the following week to discuss MAI solution design.

- Alon Horev stated that Violet should be the primary VAST Data contact for questions about encryption key granularity and related encryption matters for the Google Distributed Cloud RFP.

- Alon Horev is leading AI Model Builder sessions for VAST Forward.
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

- 2025-12-21: Mentioned in: Jeff Denworth escalation on MAI supply chain risk and need for immediate deployment plan

- 2025-12-01: RFE 0482 (NVIDIA DGX Cloud): unified visibility across NCPs, dual-uplink and tenant-scoped visibility

- 2025-12-15: Mentioned in: Google Distributed Cloud RFP follow-up: encryption at rest, SEDs, and key granularity across S3 and NFS

- 2025-12-23: Mentioned in: VAST Forward: Selected as VAST breakout session spokesperson, required prep schedule

- 2025-12-21: Mentioned in: Jeff Denworth escalation: MAI supply chain risk and need for immediate deployment plan

- 2025-12-01: RFE 0482 (NVIDIA DGX Cloud): unified visibility across NCP VAST clusters via dual-uplink and tenant-scoped views

- 2025-12-15: Mentioned in: Google Distributed Cloud RFP follow-up: encryption key granularity, SED/FIPS, and SSE-C support

- 2025-12-23: Mentioned in: VAST Forward: Selected VAST spokespeople for breakout sessions and required prep schedule
## Open Tasks
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