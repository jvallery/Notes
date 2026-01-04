---
type: customer
title: OpenAI
last_contact: '2025-10-01'
created: '2026-01-03'
tags:
- type/customer
- generated
---

# OpenAI

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

## Open Tasks

- [ ] Discuss with OpenAI the idea of providing a sync engine/data movement capability (in response to OpenAI moving away from Blob’s replication engine).

## Recent Context

- 2025-10-01: OpenAI storage requirements tasks (S3 vs Blob API parity; global KV store requirements; SF in-person meeting planning)

- 2025-10-28: Aligned on Azure Blob API support requirements (Entra ID managed identities, offline JWT validation 72–96h, RBAC/ABAC mapping, Append Blob, PutBlobFromURL) and planned POC + Tel Aviv working sessions. [[2025-10-28 - Align on Azure Blob API]]

- 2025-10-22: Discussed OpenAI storage tiering (Blob=cold, VAST=warm near GPUs) and POC status/requirements; POC currently on hold. ([[2025-10-22 - OpenAI storage strategy and VAST]])

- 2025-10-22: [[2025-10-22 - VAST warm storage POC sync]]
## Key Facts

## Topics

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

## Related

<!-- Wikilinks to related entities -->
