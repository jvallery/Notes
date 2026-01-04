---
type: projects
title: AI Pipelines Collateral
last_contact: '2025-12-19'
created: '2026-01-03'
tags:
- type/projects
- generated
---

# AI Pipelines Collateral

## Recent Context

- 2025-11-06: [[Sources/Transcripts/2025/2025-11-06 - Aaron walked through updated slides for next week’s SE conference covering two p.md|Aaron walked through updated slides for next week’s SE conference covering two p]] — **Date:** 2025-11-06 · **Project:** AI Pipelines Collateral · **Folder:** Projects/AI Pipelines Coll...

- 2025-12-19: [[2025-12-19]] - Discussion between Jeff Denworth and Jason Vallery on VAST’s Microsoft/Azure strategy: what level of... (via Jeff Denworth)
- 2025-11-13: [[2025-11-13 - GDC RFP meeting]] - Notes from a Google Distributed Cloud (GDC) RFP-related discussion covering storage TCO (HDD vs QLC)... (via Google)
- 2025-11-07: [[2025-11-07 - We reviewed the org landscape and aligned on my near-term focus. Jeff outlined k]] - 1:1 with Jeff Denworth to review the org landscape, clarify key stakeholders, and align on the autho... (via Jeff Denworth)
- 2025-11-07: [[2025-11-07 - Reviewed org landscape and key players; aligned that Jason will deeply understan]] - Weekly 1:1 between Jason Vallery and Jeff Denworth reviewing VAST’s org landscape and key players, a... (via Jeff Denworth)
- 2025-11-06: [[2025-11-06 - Aaron walked through updated slides for next week’s SE conference covering two p]] - Review of updated AI pipeline slides for an upcoming VAST SE Tech Summit, covering model training (c...
- 2025-10-29: [[2025-10-29 - Team aligned on positioning and mechanics for VAST on Cloud. Emphasis on using g]] - Group office hours aligned the team on positioning and operating mechanics for VAST on Cloud, emphas... (via VAST on Cloud Office Hours)
- 2025-10-28: [[2025-10-28 - Cloud BU leadership aligned on a dual-track strategy (1) ship GCP MVP via marke]] - Cloud BU leadership aligned on a dual-track cloud strategy: ship a near-term GCP marketplace MVP wit... (via Cloud)
- 2025-10-27: [[2025-10-27 - Jason and Kurt aligned on a go-to-market path to bring VAST’s high-density, lowe]] - Weekly 1:1 where Jason Vallery and Kurt Niebuhr aligned on a Microsoft Azure go-to-market path for V... (via Kurt Niebuhr)

## Key Facts

- GDC RFP discussion topics included HDD vs QLC TCO, SED, hardware partners, availability zones, SyncEngine, and potential GCS API considerations.
- Operational/security focus areas: multi-tenancy, QoS/quotas, tags and policy-based management, network security, air-gapped security certifications, remote patching, and troubleshooting/patching processes.
- Dell was referenced for hardware recommendation shapes.
- OpenAI is reportedly replatforming away from Azure Blob API for some scenarios and building its own data movement solution (e.g., rclone).
- Microsoft’s deal with OpenAI reportedly grants Microsoft ownership/exclusive rights to code written by OpenAI until AGI is declared; Microsoft can reuse/reship that IP.
- AZCopy is open source and is a key data movement tool for Azure Blob; MAI uses it as a data movement engine.
- Bing uses an internal storage platform called Cosmos (not Cosmos DB) with its own API surface; attempts to migrate Bing to Blob reportedly failed.
- Azure premium blob is described as small (likely petabytes, not exabytes); Azure disks business is not the near-term winnable market for VAST.
- Flash supply constraints may persist due to vendor capacity shifting toward higher-margin HBM/DRAM; price of flash recently doubled (per discussion).
- Two distinct integration patterns: (1) offload/tiering in VAST-native format (performance/cost optimized but not readable via native cloud APIs), and (2) exposing existing cloud-native data requiring change notifications and eventual consistency (e.g., Azure Change Feed).

## Topics

HDD vs QLC TCO, SED (self-encrypting drives), Hardware partners and sizing (Dell shapes), Availability zones (AZs), SyncEngine, GCS API considerations, Federal connection for mutual customer (SE and operations), Separation of duties / two-person rule, Multi-tenancy, QoS/quotas, Tags and policy-based management, Network security, Air-gapped security details and certifications, Remote patching, Operations: manage, troubleshoot, patch

## Overview

Follow-up AI pipelines whiteboarding to capture trade-offs and related guidance/collateral.

## Status

| Field | Value |
|-------|-------|
| **Status** | active |
| **Owner** | Jason Vallery |

## Blockers

- ❌ Need follow-up whiteboarding session to clarify trade-offs
- ❌ Unclear cloud packaging and how to sell/consume pipelines/serverless in cloud contexts
- ❌ Risk of confusing storage-centric SE audience if Data Engine/function triggers are emphasized
- ❌ Ambiguity in Kafka placement (ingestion head vs core storage lane) could mislead field teams
- ❌ Need to ensure KV cache depiction matches engineering reality (NFS today; GPU-direct-to-object future)

## Next Steps

- [ ] Schedule and conduct AI pipelines whiteboarding follow-up
- [ ] Document trade-offs and outcomes from the whiteboarding session
- [ ] Connect with Shachar Feinblit to align pipelines/serverless roadmap with cloud GTM packaging
- [ ] Consult SE leadership on whether/how to include Data Engine and function triggers
- [ ] Ensure diagrams show Kafka as event-stream ingestion head and RL feedback path
- [ ] Ensure RAG diagram shows embeddings as precomputed and clarifies chatbot-to-inference linkage and sequencing
- [ ] Validate KV cache representation with engineering (Glenn)
- [ ] Share and incorporate Ray workflow diagrams into slide refinements
- [ ] Finalize positioning assets, battle cards, and talk tracks for VAST on Cloud
- [ ] Deliver SE training deck before SE and ensure collateral is ready for Supercomputing demos

## Key Decisions

- ✅ Do not prioritize building 'append blob' support speculatively for OpenAI; only consider if/when OpenAI asks or if pipelines will take years to move and VAST wants that data.
- ✅ Define Blob API MVP for Microsoft AI as AZCopy compatibility rather than full Blob API breadth.
- ✅ Carl will move to ProServe under Rob rather than supporting customer-facing PM work.
- ✅ Set a monthly touchpoint with Brandon to align on cloud platform priorities.
- ✅ Customer requirement docs and FRDs will be authored and maintained in Confluence.
- ✅ Prioritize building a first-class cross-cloud platform and GTM versus ad hoc deal chasing.
- ✅ Carl to move to ProServe under Rob.
- ✅ FRDs and detailed customer requirements will be authored/maintained in Confluence.
- ✅ Jason will own multi-cloud strategy end-to-end and catalog in-flight opportunities from a product requirements lens.
- ✅ Establish a monthly touchpoint between Jason and Brandon.

## Collaborators

| Person | Role | Company |
|--------|------|---------|
| [[Sagi]] |  | VAST Data |
| [[Tiffany Stonehill]] | Cloud field lead for AWS and Azure (exact title not stated) | VAST Data |
| [[Glenn Lockwood]] |  |  |
| [[Lior Genzel]] |  |  |
| [[Shachar Feinblit]] |  |  |
| [[Jason Vallery]] | Product management (cloud); partnerships with hyperscale cloud providers | VAST Data |

## Related People

- [[Sagi]]
- [[Tiffany Stonehill]]
- [[Glenn Lockwood]]
- [[Lior Genzel]]
- [[Shachar Feinblit]]
- [[Jason Vallery]]

## Related Customers

- [[Microsoft]]
- [[OpenAI]]
- [[Google]]

## Related

<!-- Wikilinks to related entities -->
