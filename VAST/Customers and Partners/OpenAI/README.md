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

- unknown: [[2025-10 - OpenAI Tasks]] - Task list for coordinating with OpenAI on storage API requirements, global KV store needs, and arran...
- unknown: [[Oct 22nd, 2025]] - Updated stakeholder map and technical positioning for using VAST as “warm storage” near GPU fleets t... (via Sam Hopewell)
- 2025-12-19: [[2025-12-19]] - Conversation between Jason Vallery and Jeff Denworth about how to approach Microsoft/OpenAI storage ... (via Jeff Denworth)
- 2025-12-18: [[2025-12-18 1303 - New Recording]] - Brainstorming and outlining a joint document describing how VAST Data will integrate with Microsoft ... (via VAST on Azure Integration)
- 2025-11-12: [[2025-11-12 - Announcements]] - Internal note summarizing SemiAnalysis and Microsoft disclosures about Microsoft’s renewed push for ... (via Microsoft)
- 2025-10-30: [[2025-10-30 - Intro 1-1 between Jason and Dre. Dre outlined SE enablement cadence and an S3Ob]] - Intro 1:1 between Jason Vallery and Deandre (Dre) Jackson focused on aligning cloud enablement messa... (via Deandre Jackson)
- 2025-10-28: [[2025-10-28 - Jason and Erez aligned on delivering Azure Blob API support in VAST to enable Az]] - Weekly 1:1 between Jason Vallery and Erez Zilber aligning on delivering Azure Blob API support in VA... (via Erez Zilber)
- 2025-10-22: [[2025-10-22 - Rosanne outlined Dhammak’s rapid data center and GPU cloud buildout and interest]] - Weekly 1:1 where Rosanne described Dhammak/Dimac’s rapid data center and GPU cloud buildout and desi... (via Rosanne Kincaid–Smith)
- 2025-10-22: [[2025-10-22 - Jason shared candid guidance on Microsoft’s approach to GPU capacity preference]] - Weekly 1:1 between Jason Vallery (VAST) and Rosanne Kincaid–Smith (Dhammak Group) discussing Microso... (via Rosanne Kincaid–Smith)
- 2025-10-20: [[2025-10-20 - Discussed cloud architectures for VAST on AWSGCPAzure, the need for object-sto]] - Weekly 1:1 with Yogev Vankin focused on VAST multi-cloud architecture across AWS/GCP/Azure, centerin... (via Yogev Vankin)
- 2025-10-06: [[2025-10-06 - Jason updated Jai that he has a complex, high-variance offer from VAST and an ex]] - Weekly 1:1 between Jai Menon and Jason Vallery focused on Jason’s competing job offers (VAST vs Crus... (via Jai Menon)
- 2025-10-06: [[2025-10-06 - Jason has a complex VAST offer with risky, sales-linked compensation and a more]] - Weekly 1:1 between Jai Menon and Jason Vallery focused on Jason’s pending job decision between a ris... (via Jai Menon)
- 2025-10-06: [[2025-10-06 - Jason briefed Jai on offers from VAST and Crusoe, noting VAST’s complex, risky c]] - Weekly 1:1 where Jason and Jai discussed Jason’s competing offers from VAST and Crusoe versus stayin... (via Jai Menon)
- 2025-10-06: [[2025-10-06 - Jason shared he has a complex, risky offer from VAST and a more stable option fr]] - 1:1 between Jai Menon and Jason Vallery about Jason’s external offers (VAST vs Crusoe) and why stayi... (via Jai Menon)
- 2025-09-29: [[2025-09-29 - Jason shared disappointment with his rewards and anxiety about scope and support]] - Weekly 1:1 between Maneesh Sah and Jason Vallery focused on Jason’s disappointment with his rewards,... (via Maneesh Sah)

## Key Facts

- Microsoft’s 'Big Pause' is over; Microsoft is scrambling for near-term AI capacity across self-build, leases, and neocloud.
- Microsoft’s monetization thesis is Tokens/API > IaaS; Azure Foundry is framed as a 'token factory.'
- Accelerator dependencies: Nvidia remains the workhorse; MAIA lags; Microsoft may use OpenAI’s ASIC.
- Oct 28 agreement details (as disclosed/linked): Azure API exclusivity for OpenAI continues; Microsoft IP rights extended to 2032; research IP access ends by AGI panel decision or 2030; OpenAI to purchase $250B+ of Azure services; no right-of-first-refusal for Microsoft; both parties can independently pursue AGI.
- The agreement both locks in Azure demand (via OpenAI’s Azure spend) and loosens exclusivity constraints operationally (no ROFR).
- Training vs post-training/inference mix is shifting; post-training compute (RL/SFT/mid-training) is ramping and is latency-insensitive, enabling placement in remote data centers.
- Microsoft’s compute fleet is described as 'fungible.'
- Economic life of GPUs is expected to extend beyond 2–3 years, implying long-lived clusters with continual data growth needs (checkpoints, logs, evals, datasets).
- Enterprise token monetization is early but expected to grow with Foundry, supporting sustained distributed storage growth.
- OpenAI evaluation includes whether S3 API is sufficient for GPU-adjacent storage versus needing Blob API parity.

## Topics

Microsoft AI capacity expansion (self-build, leases, neocloud), Azure Foundry and token/API monetization strategy, OpenAI–Microsoft partnership terms (exclusivity, IP rights, ROFR, AGI provisions, Azure spend commitment), Accelerator roadmap and dependency risk (Nvidia, MAIA, OpenAI ASIC, AMD), Neocloud overflow strategy and cross-cloud mobility, VAST positioning and sales plays for Microsoft and OpenAI, Training storage needs (checkpoint/restore, ingestion, replication), Post-training and inference data plane (caches, RAG corpora, telemetry, retention tiers), Distributed/remote data center placement for latency-insensitive workloads, Long-lived GPU clusters driving ongoing data growth, S3 API vs Blob API parity for GPU-adjacent storage, Global KV store requirements (TPS per PB, <=64 KB IO), Feasibility assessment on VAST, In-person meeting planning (San Francisco Nov 4–6), SE enablement cadence and weekly call structure

## Open Tasks

- [ ] Discuss with OpenAI the idea of providing a sync engine/data movement capability (in response to OpenAI moving away from Blob’s replication engine).

## Related

<!-- Wikilinks to related entities -->
