---
type: projects
title: BlobFuse
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

# BlobFuse

## Overview

BlobFuse-based approaches considered for MAI caching/data access; must scale to ~100k nodes and integrate with AKS/Spark.

## Status

| Field | Value |
|-------|-------|
| **Status** | active |
| **Owner** | _Unknown_ |

## Current Blockers

- ❌ Unclear ability to scale to ~100k nodes
- ❌ Potential limitations if only suitable for training vs unified cache goal
- ❌ Unclear integration fit with AKS + Spark at MAI scale

## Next Steps

- [ ] Jason to review current BlobFuse/BlockFuse progress and performance numbers
- [ ] Re-engage with Nagendra team for latest proposal and performance data
- [ ] Collect scaling plans for side-by-side comparison

## Collaborators

| Person | Role | Company |
|--------|------|---------|
| [[Jai Menon]] |  |  |
| [[Nagendra]] |  |  |
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
- ✅ Jason will lead the OpenAI cache evaluation and comparison against internal/external options.
- ✅ Design preference is a single, pluggable cache for training and inference (including KB caching), framework-agnostic; prioritize training first.
- ✅ Near-term performance direction centers on Bifrost (including a direct read path) plus a distributed cache; DeltaZero positioned as follow-on.

## Key Facts

- MAI scale targets in ~2 years: ~400k GPUs for training (~100k nodes) and ~40k GPUs for inference.
- Primary environment for MAI is AKS/Kubernetes with Spark.
- Caching options under consideration include C-Store proposals (Krishnan’s team), Alluxio/DAX (supports inference/KB caching), OpenAI cache code (pending IP confirmation), and BlockFuse/BlobFuse approaches.
- OpenAI cache access appears permitted for Microsoft services but requires confirmation via Pete and SILA legal.
- Bifrost includes a direct read path from compute to capacity nodes, bypassing FE/table for reads; Lukasz is implementing this component.
- Compute for MAI moved under Brendan’s org (AKS); CVP Qiu Ke involved; Yumin coordinating.
- Possible MAI requirement: multi-region pooling for a distributed cache (unconfirmed).
- MAI targets 400k GPUs for training and 40k GPUs for inference within 2 years.
- Cache must scale to ~100k nodes and run on AKS + Spark.
- OpenAI cache IP may be usable by Microsoft, but legal/IP clearance and repo access must be confirmed (Pete and Sila involved).

## Topics / Themes

MAI caching strategy and unified cache goal, OpenAI cache code access and IP/licensing, Scaling requirements to ~100k nodes and AKS/Spark fit, Comparison of caching options (C-Store, Alluxio/DAX, BlobFuse/BlockFuse), Bifrost architecture and direct read path, MAI org changes (compute under AKS leadership), Performance snapshot feedback and follow-up conversations, MAI unified caching strategy (training-first, later inference/KB caching), OpenAI cache IP/code access and legal clearance, Scalability requirements (100k nodes; 400k/40k GPU targets), AKS + Spark integration constraints, Comparison of caching options (BlobFuse, Alluxio/DAX, AC Store, OpenAI cache), Blob performance roadmap: Bifrost direct read path and DeltaZero follow-on, Snapshot feedback and potential escalation path (Ong, Manish, Wamshi), Multi-region cache pooling possibility

## Related People

- [[Jai Menon]]
- [[Nagendra]]
- [[Jason Vallery]]

## Related Customers

- [[Microsoft]]

## Recent Context

- 2025-09-03: [[2025-09-03 - Jai welcomed Jason back and aligned on a forward-looking scope evaluate OpenAI’]] - Weekly 1:1 between Jai Menon and Jason Vallery aligning Jason’s initial scope after returning: evalu... (via Jai Menon)
- 2025-09-03: [[2025-09-03 - Jai outlined a near-term technical focus evaluate OpenAI’s caching code as a ca]] - Weekly 1:1 where Jai Menon aligned with Jason Vallery on a near-term technical focus: evaluate OpenA... (via Jai Menon)

## Artifacts

```dataview
TABLE file.mtime as "Modified"
FROM ""
WHERE type != "readme" AND type != "projects"
SORT file.mtime DESC
```

---
*Last updated: *