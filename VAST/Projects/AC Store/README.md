---
type: projects
title: AC Store
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

# AC Store

## Overview

Internal proposal (Krishnan’s team) as part of caching strategy options for MAI.

## Status

| Field | Value |
|-------|-------|
| **Status** | active |
| **Owner** | Krishnan |

## Current Blockers

- ❌ Need maturity/performance validation vs MAI timelines
- ❌ Need clarity on integration with AKS + Spark and scale to ~100k nodes
- ❌ Unclear fit/performance at MAI scale

## Next Steps

- [ ] Re-engage with Krishnan team for latest proposal and performance data
- [ ] Compare against other options and document pros/cons

## Collaborators

| Person | Role | Company |
|--------|------|---------|
| [[Krishnan]] |  |  |
| [[Yumin]] |  |  |
| [[Jason Vallery]] | Product management (cloud); partnerships with hyperscale cloud providers | VAST Data |

## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed
SORT due ASC
```


## Key Decisions

- ✅ Jason will lead the OpenAI cache evaluation and comparison against internal/external options.
- ✅ Design preference is a single, pluggable cache for training and inference (including KB caching), framework-agnostic; prioritize training first.
- ✅ Near-term performance direction centers on Bifrost (including a direct read path) plus a distributed cache; DeltaZero positioned as follow-on.
- ✅ Primary focus is training cache requirements; inference KB caching follows after.
- ✅ Aim for a unified, pluggable cache design that supports multiple frameworks.
- ✅ Jason to prioritize OpenAI cache evaluation while tracking other options (BlobFuse/Blockfuse, AC Store, Alluxio/DAX).

## Key Facts

- MAI targets 400k GPUs for training and 40k GPUs for inference within 2 years.
- Cache must scale to ~100k nodes and run on AKS + Spark.
- OpenAI cache IP may be usable by Microsoft, but legal/IP clearance and repo access must be confirmed (Pete and Sila involved).
- Options under evaluation include OpenAI cache IP, Alluxio/DAX, BlobFuse, and AC Store (Krishnan’s team).
- Bifrost adds a direct read path bypassing FE/table layers to capacity nodes; DeltaZero is a potential follow-on.
- Lukasz is building parts of Bifrost, including the direct read path.
- Compute for AI moved to Brendan’s org; AKS compute for MAI is led by a CVP referred to as 'Kiki'; Yumin is interfacing.
- Possible MAI requirement: multi-region logical cache pooling (to confirm).
- There is a morale/engagement risk related to Jason’s 'meets expectations' snapshot outcome; may require escalation discussions.
- MAI target scale in ~2 years: ~400k GPUs for training and ~40k GPUs for inferencing.

## Topics / Themes

MAI unified caching strategy (training-first, later inference/KB caching), OpenAI cache IP/code access and legal clearance, Scalability requirements (100k nodes; 400k/40k GPU targets), AKS + Spark integration constraints, Comparison of caching options (BlobFuse, Alluxio/DAX, AC Store, OpenAI cache), Blob performance roadmap: Bifrost direct read path and DeltaZero follow-on, Snapshot feedback and potential escalation path (Ong, Manish, Wamshi), Multi-region cache pooling possibility, Post-sabbatical alignment and role focus shift to technical evaluations, MAI AI caching requirements and scale targets, OpenAI cache feasibility and IP/legal access, Alternative caching options: Blockfuse/BlobFuse, AC Store, Alluxio/DAX, Unified vs separate caches for training and inference/KB caching, AKS/Kubernetes and Spark integration constraints, Bifrost architecture and direct read path

## Related People

- [[Krishnan]]
- [[Yumin]]
- [[Jason Vallery]]

## Related Customers

- [[Microsoft]]

## Recent Context

- 2025-09-03: [[2025-09-03 - Jai outlined a near-term technical focus evaluate OpenAI’s caching code as a ca]] - Weekly 1:1 where Jai Menon aligned with Jason Vallery on a near-term technical focus: evaluate OpenA... (via Jai Menon)
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