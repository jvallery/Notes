---
type: customer
title: OpenAI
last_contact: unknown
created: '2026-01-03'
tags:
- type/customer
- generated
---

# OpenAI

## Recent Context

- unknown: [[2025-10 - OpenAI Tasks]] - Task list for coordinating with OpenAI on storage API requirements, global KV store needs, and sched...
- unknown: [[2025-10 - Jeff Denworth]] - Notes capturing planning topics with Jeff Denworth around travel, team reporting structure, cloud ac... (via Jeff Denworth)
- unknown: [[Oct 22nd, 2025]] - Stakeholder mapping and technical positioning for an OpenAI research primary storage proof-of-concep... (via Sam Hopewell)
- unknown: [[Azure + VAST Integration Opportunities and Approach v2]] - Draft strategy and roadmap for integrating VAST with Microsoft Azure, centered on a minimal Blob RES... (via VAST on Azure Integration)
- 2026-01-03: [[2026-01-03 - Prep for Microsoft AI talks]] - Jonsi Stephenson and Jason Vallery aligned messaging and strategy for upcoming Microsoft AI discussi... (via Jonsi Stephenson)
- 2025-12-19: [[2025-12-19]] - Discussion between Jeff Denworth and Jason Vallery on VAST’s Microsoft/Azure strategy: what level of... (via Jeff Denworth)
- 2025-12-18: [[2025-12-18 1303 - New Recording]] - Brainstorming and outlining a joint document describing how VAST will integrate with Microsoft Azure... (via VAST on Azure Integration)
- 2025-11-12: [[2025-11-12 - Announcements]] - Analysis of Microsoft’s recent disclosures and SemiAnalysis commentary on Microsoft’s AI strategy, f... (via Microsoft)
- 2025-11-07: [[2025-11-07 - We reviewed the org landscape and aligned on my near-term focus. Jeff outlined k]] - 1:1 with Jeff Denworth to review the org landscape, clarify key stakeholders, and align on the autho... (via Jeff Denworth)
- 2025-11-07: [[2025-11-07 - Reviewed org landscape and key players; aligned that Jason will deeply understan]] - Weekly 1:1 between Jason Vallery and Jeff Denworth reviewing VAST’s org landscape and key players, a... (via Jeff Denworth)
- 2025-11-07: [[2025-11-07 - We reviewed the org landscape and immediate priorities. Jeff highlighted key pla]] - 1:1 discussion with Jeff Denworth reviewing VAST org landscape, immediate priorities, and a pragmati... (via Jeff Denworth)
- 2025-11-07: [[2025-11-07 - We aligned on hyperscaler strategy across Google and Microsoft. On Google, GDC i]] - 1:1 strategy sync with Jonsi Stephenson aligning VAST’s hyperscaler approach across Google and Micro... (via Jonsi Stephenson)
- 2025-11-07: [[2025-11-07 - Working session to brute-force warm paths into priority model builders using Lin]] - Working session for the Model Builder Turbine project to map warm introduction paths into priority m... (via Model Builder Turbine)
- 2025-11-06: [[2025-11-06 - Jason shared VAST’s momentum (CoreWeave $1.2B deal) and updates on Microsoft’s A]] - Weekly 1:1 between Jason Vallery and Kanchan Mehrotra covering Microsoft Project Apollo and MAI Dall... (via Kanchan Mehrotra)
- 2025-11-06: [[2025-11-06 - Aaron walked through updated slides for next week’s SE conference covering two p]] - Review of updated AI pipeline slides for an upcoming VAST SE Tech Summit, covering model training (c... (via AI Pipelines Collateral)

## Key Facts

- Microsoft’s 'Big Pause' is over; they are scrambling for near-term capacity across self-build, leases, and neocloud.
- Microsoft monetization thesis emphasizes Tokens/API over IaaS; Azure Foundry positioned as a 'token factory'.
- Accelerator dependencies: Nvidia remains primary; MAIA lags; Microsoft may use OpenAI’s ASIC.
- Oct 28 Microsoft–OpenAI agreement: Azure API exclusivity continues; Microsoft IP rights extended to 2032; research IP access ends by AGI panel decision or 2030; OpenAI to purchase $250B+ of Azure services; no right-of-first-refusal for Microsoft; both can independently pursue AGI.
- Training vs post-training/inference mix is shifting; post-training compute is ramping and is latency-insensitive, enabling remote DC placement.
- Economic life of GPUs expected to exceed 2–3 years, implying long-lived clusters with continual data growth needs (checkpoints, logs, evals, datasets).
- OpenAI discussion topics include GPU-adjacent storage API requirements (S3 vs Blob parity) and a potential global KV store workload (TPS per PB, <=64 KB IO).
- Potential in-person meeting window in San Francisco: Nov 4–6.
- MAI Falcon plan includes Phoenix, Dallas, and Richmond sites (~40k GPUs per site) connected by an AI WAN; initial tranche includes ~3 EB of Blob.
- MAI struggles to use Falcon capacity due to control plane fragility and GPU issues.

## Topics

Microsoft near-term AI capacity strategy (self-build, leases, neocloud), Azure Foundry token monetization, Microsoft–OpenAI partnership terms and implications, Accelerator roadmap uncertainty (Nvidia, MAIA, OpenAI ASIC), VAST positioning for training storage (checkpoint/restore, ingestion, replication), VAST positioning for post-training/inference data plane (caches, RAG corpora, telemetry, retention), Neocloud co-sell strategy and portability back to Azure, GPU-adjacent storage API requirements (S3 vs Blob parity), Global KV store requirements (TPS per PB, <=64 KB IO), In-person meeting planning (San Francisco Nov 4–6), Microsoft AI (MAI) org landscape and stakeholders, Falcon capacity rollout and AI WAN, MAI control plane fragility and GPU utilization constraints, Project Apollo (AKS-led slim control plane) and storage integration, Azure internal politics (Compute vs Storage incentives)

## Open Tasks

- [ ] Discuss with OpenAI the idea of providing a sync engine/data movement capability (in response to OpenAI moving away from Blob’s replication engine).

## Account Status

| Field | Value |
|-------|-------|
| **Status** | Active |
| **Industry** | Artificial Intelligence |

## Key Contacts

- [[Greg Brockman]]
- [[Louie]]
- [[Rory]]
- [[Uday]]
- [[Sam Altman]]
- [[Kevin Park]]
- [[Glenn Lockwood]]
- [[Melissa Du]]
- [[Sam Hopewell]]
- [[Rory Carmichael]]

## Opportunities

- Define storage API requirements for GPU-adjacent storage (S3 API sufficiency vs Blob API parity)
- Assess feasibility of a global KV store on VAST (TPS per PB, <=64 KB IO)
- Coordinate in-person meeting in San Francisco (Nov 4–6)
- Define next steps for OpenAI engagement
- Near-GPU 'warm storage' POC using VAST to stage checkpoints/training sets locally and serve some reads directly from VAST to reduce dependence on transient WAN/Azure bandwidth
- Potential longer-term fit if VAST can prove metadata scalability and reliability concerns around global namespace at multi-EiB scale
- Target archetype for frontier-scale distributed training pipelines (central curated datasets, distributed GPU clusters, heavy checkpoint flows) that benefit from Blob-to-VAST staging and checkpoint return patterns
- Positioning VAST+Azure Blob integration to be ready for MAI/OpenAI needs; OpenAI runs massive Databricks/Spark pipelines and has shifted some workloads off Azure due to CPU capacity constraints.
- Engage data acquisition workloads; position VAST Database/event streaming/query-from-ingest rather than building append-blob speculatively
- Potential leverage/pressure on Microsoft via OpenAI interest

## Blockers

- ❌ Unconfirmed OpenAI requirement: S3 API sufficiency vs need for Blob API parity
- ❌ Need detailed global KV store requirements to assess feasibility on VAST
- ❌ Next steps not yet defined
- ❌ POC on hold due to firefighting/bandwidth issues and internal decision backlog
- ❌ Team focused on bringing new research supercomputer capacity online; not a current focus for Sam's team

## Key Decisions

- ✅ Wait until Friday’s Kushal meeting before Alon follows up with Vipin.
- ✅ Prioritize Project Apollo as the first entry path over Azure marketplace SKUs.
- ✅ Use MAI success as the wedge to influence broader Azure storage strategy and hardware qualification.
- ✅ Treat Blob compatibility as exploratory; near-term emphasis remains on performance to keep GPUs utilized.
- ✅ Use Phil Wagstrom as primary multi-tenancy SME contact.
- ✅ Proceed with OVA and SE Lab access for Jason’s learning.
- ✅ Schedule a follow-up focused on OpenAI architecture and needs.
- ✅ Anchor enablement on workload scenarios rather than generic object features.
- ✅ Avoid engaging in price-only competitions (e.g., MinIO) unless the workload merits VAST’s performance/value.
- ✅ Use Entra ID managed identities with JWT-based auth for OpenAI scenarios (no account keys).

## Collaborators

| Person | Role | Company |
|--------|------|---------|
| [[Greg Brockman]] |  | OpenAI |
| [[Glenn Lockwood]] |  | OpenAI |
| [[Melissa Du]] | Logistics for “neo clouds” / CoreWeave (finance/capacity org) | OpenAI |
| [[Jeff Denworth]] |  |  |
| [[SILA legal]] | Legal |  |
| [[Lior Genzel]] |  |  |
| [[Sam Hopewell]] |  |  |
| [[Yogev Vankin]] |  |  |
| [[Rory Carmichael]] | Owns research infrastructure/supercomputers; Sam's boss | OpenAI |
| [[Erez Zilber]] | Protocols architect | VAST Data |
| [[Pete Eming]] |  |  |
| [[Jason Vallery]] | Product management (cloud); partnerships with hyperscale cloud providers | VAST Data |
| [[Sila]] | Lawyer / legal contact (implied) |  |
| [[Asaf Levy]] |  |  |
| [[Sam Altman]] |  | OpenAI |
| [[Kevin Park]] | Finance/capacity leader (manager of Melissa Du) | OpenAI |
| [[Jonsi Stephenson]] | CEO | VAST Data |
| [[Jai Menon]] |  |  |
| [[Louie]] |  | OpenAI |
| [[Uday]] | Runs infrastructure at OpenAI (reports to Greg Brockman) | OpenAI |
| [[Pete]] |  |  |

## Related People

- [[Greg Brockman]]
- [[Glenn Lockwood]]
- [[Melissa Du]]
- [[Jeff Denworth]]
- [[SILA legal]]
- [[Lior Genzel]]
- [[Sam Hopewell]]
- [[Yogev Vankin]]
- [[Rory Carmichael]]
- [[Erez Zilber]]
- [[Pete Eming]]
- [[Jason Vallery]]
- [[Sila]]
- [[Asaf Levy]]
- [[Sam Altman]]
- [[Kevin Park]]
- [[Jonsi Stephenson]]
- [[Jai Menon]]
- [[Louie]]
- [[Uday]]
- [[Pete]]

## Related

<!-- Wikilinks to related entities -->
