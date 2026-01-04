---
type: people
title: Align on OpenAI cache evaluation
date: '2025-09-03'
person: Jai Menon
participants:
- Jai Menon
- Jason Vallery
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-09-03 - Reconnected post-sabbatical and
  aligned on Jason’s initial focus evaluate OpenA.md
tags:
- type/customer
- account/jai-menon
- generated
---

# Align on OpenAI cache evaluation

**Date**: 2025-09-03
**Account**: [[Jai Menon]]
**Attendees**: Jai Menon, Jason Vallery

## Summary

Jai and Jason reconnected post-sabbatical and aligned Jason’s initial focus on evaluating OpenAI’s AI caching approach for MAI at extreme scale, including fit for AKS/Kubernetes and Spark and ability to scale to ~100k nodes. They discussed alternative caching options (BlobFuse/Blockfuse, AC Store, Alluxio/DAX) and the Blob/Bifrost direction, plus the need to confirm OpenAI IP/code access via Pete and SILA legal before code review.
## Action Items
- [ ] Evaluate OpenAI caching code for feasibility (unified vs separate caches), performance/scale (~100k nodes), and AKS/Spark fit; produce a recommendation. @Jason Vallery 📅 2025-10-26 🔺 #task
- [ ] Confirm OpenAI IP rights and request code access with Pete and SILA legal; ensure Jason has access. @Jason Vallery 📅 2025-10-26 🔺 #task
- [ ] Discuss the performance snapshot outcome with Ong and decide whether to escalate to Manish. @Jason Vallery 📅 2025-09-05 🔺 #task
- [ ] Meet MAI to confirm requirements (GPU counts, multi-region need, cluster status, training framework plans). @Jason Vallery 📅 2025-09-05 🔺 #task
- [ ] Review latest Blockfuse/BlobFuse progress and Nagendra’s document; sync with the team. @Jason Vallery 📅 2025-10-26 ⏫ #task
- [ ] Compare caching options (BlobFuse/Blockfuse, AC Store, Alluxio/DAX) against MAI scale and AKS/Spark integration; capture pros/cons. @Jason Vallery 📅 2025-10-26 ⏫ #task
- [ ] Sync with Lukasz to understand Bifrost direct read path and applicability to MAI workloads. @Jason Vallery 📅 2025-10-26 ⏫ #task
- [ ] Send Jason the OpenAI IP agreement details referenced in prior discussions. @Jai Menon 📅 2025-10-26 ⏫ #task
- [ ] Send MAI 'frictions with Microsoft infra' document to Jason. @Jai Menon 📅 2025-10-26 ⏫ #task
- [ ] Send Apollo document to Jason. @Jai Menon 📅 2025-10-26 ⏫ #task
- [ ] Connect Jason with Lukasz regarding Bifrost direct read path. @Jai Menon 📅 2025-10-26 ⏫ #task
- [ ] Draft an AI caching requirements/options document (training-first; inference KB later; unified cache goal). @Jai Menon 📅 2025-10-26 ⏫ #task

## Decisions
- Primary focus is training cache requirements; inference KB caching follows after.
- Aim for a unified, pluggable cache design that supports multiple frameworks.
- Jason will prioritize OpenAI cache evaluation while tracking other options (BlobFuse/Blockfuse, AC Store, Alluxio/DAX).

## Key Information
- MAI target scale discussed: ~400k GPUs for training and ~40k GPUs for inferencing in ~2 years.
- Cache must scale to ~100,000 nodes and integrate with AKS/Kubernetes and Spark.
- OpenAI may provide IP/code usable across Microsoft services, pending legal confirmation via Pete and SILA legal.
- Bifrost includes a direct read path bypassing FE/table layers for reads; Lukasz is implementing parts of this.
- Potential MAI constraint raised: multi-region pooling for a distributed cache (needs confirmation).

---

*Source: [[Inbox/_archive/2025-09-03/2025-09-03 - Reconnected post-sabbatical and aligned on Jason’s initial focus evaluate OpenA.md|2025-09-03 - Reconnected post-sabbatical and aligned on Jason’s initial focus evaluate OpenA]]*

## Related

- [[Jason Vallery]]
- [[SILA legal]]
- [[Maneesh Sah]]
- [[Brendan Burns]]
- [[Qi Ke]]
- [[Arun Krishna]]
- [[Cloud control plane]]
- [[DeltaZero]]
- [[Microsoft]]
- [[OpenAI]]
- [[CoreWeave]]
