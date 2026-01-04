---
type: customer
title: VAST Azure integration outline
date: '2025-12-18'
account: Microsoft
participants: []
source: transcript
tags:
- type/customer
- account/microsoft
- generated
---

# VAST Azure integration outline

**Date**: 2025-12-18
**Account**: [[Microsoft]]
**Attendees**: 

## Summary

Discussion focused on drafting a joint document describing how VAST Data integrates with Microsoft Azure, covering business rationale, target workloads, and required engineering on both sides. Key integration themes included GPU-adjacent VAST storage synchronized with a central Azure Blob data lake, MVP compatibility with AzCopy via a minimal Blob API surface, and longer-term options for tiering/offload and deeper first-party Azure service integration (e.g., private endpoints/control-plane wiring).
## Action Items
- [ ] Analyze AzCopy (open source) to enumerate the specific Azure Blob REST APIs/signatures it depends on, to define the minimum viable Blob API surface VAST must emulate for AzCopy compatibility. @TBD ⏫ #task

## Key Information
- The intended deliverable is a single document (with carve-out sections) answering the what/why/how of VAST Data integration with Microsoft Azure, including business strategy, partnership areas, workloads, differentiation, and engineering/design constraints.
- Current VAST-on-cloud runs on VMs across cloud providers; it is suitable for endpoints/caching but is not cost-effective for storing large volumes due to VM/ephemeral storage constraints.
- A key target scenario is a centralized Azure data lake (Blob) with disaggregated GPU compute across many regions/neo-clouds; GPU-adjacent storage needs staging of training data and checkpoints synchronized back to the central data estate.
- OpenAI historically used AzCopy (built on Put Blob from URL) and reportedly moved to rclone; Microsoft internal tools (e.g., Azure Storage Mover) also build on AzCopy primitives.
- Proposed VAST approach: expose a Blob Storage API on top of VAST primarily for compatibility/data movement (not to replace VAST-native integrations like Spark/Databricks drivers or Kafka endpoint).
- MVP Blob API focus: support core operations used by AzCopy (e.g., put blob, put block, get blob, list blobs/containers, metadata). Longer-tail features (append/page blob, ADLS Gen2/HNS/DFS endpoint) are non-MVP but should be documented with rationale.
- Tiering/offload is a gap: VAST currently lacks tiering; in an Azure-centric model, tiering from VAST flash to Blob (HDD-backed) is a key concept due to flash supply constraints and TCO considerations.
- Two tiering permutations were discussed: (A) store VAST-native/erasure-coded/encrypted extents in Blob (best efficiency but not directly readable via Blob APIs), or (B) keep objects in native Blob format and have VAST index/sync namespace via change feed/eventing (better ecosystem compatibility but adds sync/auth complexity).
- Azure first-party services often connect to Blob via control-plane resource provider selection and private endpoints/NSP; third-party endpoints (like VAST-on-VM) may require public routable endpoints, creating security/adoption blockers without Microsoft engineering.
- Microsoft 'Project Tuscany' was mentioned as a reverse-proxy concept (initially for S3) where Blob can proxy to remote object stores; analogous patterns could enable Azure services to access data stored in VAST via Blob endpoints.

---

*Source: [[Inbox/_archive/2025-12-18/Azure integration recording.md|Azure integration recording]]*

## Related

- [[OpenAI]]
- [[CoreWeave]]
- [[Databricks]]
- [[Samsung]]
- [[SK]]
- [[Micron]]
- [[VAST on Azure Integration]]
