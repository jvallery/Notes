---
type: projects
title: DeltaZero
created: '2026-01-03'
last_updated: ''
status: active
auto_created: true
tags:
- type/projects
- needs-review
- status/active
last_contact: '2025-09-03'
---

# DeltaZero

## Overview

Positioned as a follow-on to Bifrost for further Blob performance enhancements; positioning still in progress.

## Status

| Field | Value |
|-------|-------|
| **Status** | active |
| **Owner** | Jai Menon |

## Current Blockers

- ❌ Positioning/definition work in progress
- ❌ Positioning and scope still a work in progress.
- ❌ Positioning and scope not finalized
- ❌ Positioning/scope not finalized
- ❌ Dependent on Bifrost progress and outcomes

## Next Steps

- [ ] Continue positioning DeltaZero as follow-on after Bifrost; clarify scope/timeline.
- [ ] Continue positioning work after Bifrost and distributed cache direction solidifies
- [ ] Refine positioning and sequencing after Bifrost progress
- [ ] Continue positioning and planning relative to Bifrost and MAI needs

## Collaborators

| Person | Role | Company |
|--------|------|---------|
| [[Jai Menon]] |  |  |
| [[Jason Vallery]] | Product management (cloud); partnerships with hyperscale cloud providers | VAST Data |

## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed
SORT due ASC
```


## Key Decisions

- ✅ Evaluate OpenAI cache as a first concrete step toward MAI caching strategy.
- ✅ Pursue a single pluggable cache design across training and inference, prioritizing training first.
- ✅ Target deployment environment is AKS + Spark and must scale to ~100k nodes.
- ✅ Jason will start with evaluating the OpenAI cache as the first concrete task.
- ✅ Retroactive performance snapshot discussion to be handled with Ong first, with possible follow-up to Wamshi and Manish.
- ✅ Primary cache focus is MAI training/checkpoint/find-data workloads first; inference KB cache supported later.
- ✅ Aim for a single, framework-pluggable cache rather than separate caches per use case.
- ✅ Near-term storage performance focus remains Bifrost; DeltaZero positioned as follow-on.
- ✅ Jason will lead the OpenAI cache evaluation and comparison against internal/external options.
- ✅ Design preference is a single, pluggable cache for training and inference (including KB caching), framework-agnostic; prioritize training first.

## Key Facts

- MAI scale targets in ~2 years: ~400k GPUs for training (~100k nodes) and ~40k GPUs for inference.
- Primary environment for MAI is AKS/Kubernetes with Spark.
- Caching options under consideration include C-Store proposals (Krishnan’s team), Alluxio/DAX (supports inference/KB caching), OpenAI cache code (pending IP confirmation), and BlockFuse/BlobFuse approaches.
- OpenAI cache access appears permitted for Microsoft services but requires confirmation via Pete and SILA legal.
- Bifrost includes a direct read path from compute to capacity nodes, bypassing FE/table for reads; Lukasz is implementing this component.
- Compute for MAI moved under Brendan’s org (AKS); CVP Qiu Ke involved; Yumin coordinating.
- Possible MAI requirement: multi-region pooling for a distributed cache (unconfirmed).
- MAI target scale in ~2 years: ~400,000 GPUs for training (~100,000 nodes) and ~40,000 GPUs for inferencing.
- Primary environment for MAI: AKS/Kubernetes and Spark.
- Caching options considered: OpenAI cache, Blobfuse/Blockfuse, AC Store/C-Store, Alexio/DAX.

## Topics / Themes

MAI caching strategy and unified cache goal, OpenAI cache code access and IP/licensing, Scaling requirements to ~100k nodes and AKS/Spark fit, Comparison of caching options (C-Store, Alluxio/DAX, BlobFuse/BlockFuse), Bifrost architecture and direct read path, MAI org changes (compute under AKS leadership), Performance snapshot feedback and follow-up conversations, MAI AI caching strategy and requirements, OpenAI cache IP/access and code evaluation, Scalability to 100k nodes and AKS/Spark integration, Bifrost performance improvements and direct read path, Potential multi-region cache pooling requirement, Performance snapshot and recognition discussion (Ong/Wamshi/Manish), MAI unified caching strategy (training-first, later inference/KB caching), OpenAI cache IP/code access and legal clearance

## Related People

- [[Jai Menon]]
- [[Jason Vallery]]

## Related Customers

- [[Microsoft]]

## Recent Context

- 2025-09-03: [[2025-09-03 - Jai welcomed Jason back and aligned on a forward-looking scope evaluate OpenAI’]] - Weekly 1:1 between Jai Menon and Jason Vallery aligning Jason’s initial scope after returning: evalu... (via Jai Menon)
- 2025-09-03: [[2025-09-03 - Jai outlined a high-priority need to define an AI caching strategy for MAI at ma]] - Weekly 1:1 with Jai Menon focused on defining an AI caching strategy for Microsoft AI (MAI) at massi... (via Jai Menon)
- 2025-09-03: [[2025-09-03 - Jai outlined a near-term technical focus evaluate OpenAI’s caching code as a ca]] - Weekly 1:1 where Jai Menon aligned with Jason Vallery on a near-term technical focus: evaluate OpenA... (via Jai Menon)
- 2025-09-03: [[2025-09-03 - Jai outlined a high-priority evaluation for an AI caching strategy to support MA]] - Weekly 1:1 where Jai Menon aligned with Jason Vallery on a high-priority evaluation of AI caching st... (via Jai Menon)
- 2025-09-03: [[2025-09-03 - Reconnected post-sabbatical and aligned on Jason’s initial focus evaluate OpenA]] - 1:1 between Jason Vallery and Jai Menon after Jason’s sabbatical to align Jason’s initial focus on e... (via Jai Menon)

## Artifacts

```dataview
TABLE file.mtime as "Modified"
FROM ""
WHERE type != "readme" AND type != "projects"
SORT file.mtime DESC
```

---
*Last updated: *