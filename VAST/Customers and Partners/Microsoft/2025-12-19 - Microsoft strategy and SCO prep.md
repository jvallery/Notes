---
type: customer
title: Microsoft strategy and SCO prep
date: '2025-12-19'
account: Microsoft
participants:
- Jason Vallery
- Jeff Denworth
source: transcript
tags:
- type/customer
- account/microsoft
- generated
---

# Microsoft strategy and SCO prep

**Date**: 2025-12-19
**Account**: [[Microsoft]]
**Attendees**: Jason Vallery, Jeff Denworth

## Summary

Jason and Jeff aligned on Microsoft strategy, focusing on what Blob API support is actually needed (primarily Microsoft AI via AZCopy) versus broader Azure integration priorities like tiering/offload to Blob and namespace/metadata synchronization for existing cloud data. They discussed competitive dynamics at OpenAI (internal storage efforts via Rockset/FoundationDB/RocksDB and BoostedBlob) and emphasized that engineering work must be staged to near-term revenue, with Microsoft needing to decide quickly due to flash supply constraints. Jeff also tasked Jason to prepare a Sales Kickoff (SCO) session on building an AI cloud with VAST and to help drive clearer NeoCloud user stories and progress with Morty/NeoCloud partners.
## Action Items
- [ ?] Follow up with Louie (OpenAI data acquisition) and send a relevant VAST blog/link (e.g., event streaming/Kafka-related) to try to re-engage and advance parallel conversations. @Myself #task #proposed
- [ ?] Work with Morty to crystallize NeoCloud-in-a-box user stories and market messaging over the next two months, and help him make progress on the NeoCloud market-shaping plan. @Myself ⏫ #task #proposed
- [ ?] Ask Morty in today's 1:1 for details on Lambda’s plan to launch the full VAST portfolio and how NeoCloud roadmaps evolve beyond GPU-only services. @Myself #task #proposed
- [ ?] Prepare SCO session content for a 45-minute talk on 'building an AI cloud with VAST' (why VAST is used, where it’s going, multi-tenancy best practices, and control plane direction) aimed at NeoCloud audiences. @Myself ⏫ #task #proposed
- [ ?] Develop a near-term roadmap and 'attack vectors' for expanding Microsoft business development (sell-to/sell-with/sell-through), including mapping first-party Azure services and integration opportunities. @Myself ⏫ #task #proposed

## Decisions
- Do not prioritize implementing full Blob API or 'append blob' support speculatively; focus on what Microsoft teams actually require and react to additional needs if/when they arise.
- Define Blob API MVP for Microsoft AI as compatibility with AZCopy scenarios and test cases rather than broad Blob API surface coverage.
- Prioritize a clean, credible tiering/offload-to-Blob story (capacity expansion and supply-chain de-risking) over broader Blob API feature completeness.

## Key Information
- OpenAI is reportedly replatforming away from Azure Blob API for some scenarios, using their own data movement tooling (e.g., rclone) and internal abstractions.
- OpenAI training platform uses an OpenAI-built Python client library (BoostedBlob) that supports S3, Google Cloud Storage, and Azure Blob; Microsoft is considering reshipping BoostedBlob as a preferred Python library.
- Microsoft AI relies on Azure Blob and uses AZCopy as a primary data movement tool; supporting AZCopy is positioned as the practical MVP for Blob API support.
- Azure Blob API surface is large; many features are management-oriented (e.g., versioning, soft delete) and may not be required for VAST’s customer scenarios.
- Bing uses an internal storage platform called Cosmos (not Cosmos DB) with its own API surface; Exchange Online also has its own storage solution.
- Two distinct cloud-integration patterns were discussed: (1) offload/tiering in a VAST-native optimized format, and (2) exposing/synchronizing existing cloud object data into VAST via change notifications (eventual consistency).
- Azure has a 'change feed' mechanism for blob change notifications; integrating for namespace sync implies async/eventual consistency behavior.
- VAST does not currently support Azure Key Vault integration for customer-managed keys; this is a gap for Azure ecosystem readiness.
- Flash supply constraints are a major concern; HDD supply is expected to improve, and vendors may be reallocating capacity toward higher-margin HBM/DRAM, impacting flash availability and pricing.
- Jeff expects Microsoft to need to decide on direction by January due to supply-chain pressure; internal momentum with Microsoft AI was described as positive but deal timing is uncertain.
- SCO will include a session earmarked for Jason; Jeff wants Jason to be the primary spokesperson for 'building an AI cloud with VAST' rather than Morty due to presentation strength.

---

*Source: [[Inbox/_archive/2025-12-19/original.md|original]]*

## Related

- [[Jeff Denworth]]
- [[John Mao]]
- [[Maneesh Sah]]
- [[Eric Wolfie]]
- [[Mordechai Blaunstein]]
- [[Kishore Inampudi]]
- [[Lior Genzel]]
- [[Cloud control plane]]
- [[Cloud-in-a-box Tier-2 Clouds]]
- [[Microsoft Azure Engagement Plan]]
- [[VAST database updates]]
- [[OpenAI]]
- [[Amazon]]
- [[Google]]
- [[Databricks]]
- [[NVIDIA]]
- [[Micron]]
- [[SK]]
- [[Samsung]]
- [[Seagate]]
- [[Western Digital]]
- [[Toshiba]]
- [[CoreWeave]]
- [[Snowflake]]
- [[Lambda]]
- [[Walmart]]
- [[xAI]]