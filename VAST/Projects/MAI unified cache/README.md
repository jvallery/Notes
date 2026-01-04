---
type: projects
title: MAI unified cache
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

# MAI unified cache

## Overview

Define and deliver a single, pluggable caching solution for MAI that prioritizes training workloads first and later supports inference/KB caching; must scale to ~100k nodes and run on AKS + Spark, potentially with multi-region logical pooling.

## Status

| Field | Value |
|-------|-------|
| **Status** | active |
| **Owner** | Jai Menon |

## Current Blockers

- ❌ Fragmentation risk if multiple caches are pursued in parallel
- ❌ Unclear multi-region pooling requirement and expectations (latency/consistency)
- ❌ Alternative solutions’ maturity/performance may not meet MAI timelines

## Next Steps

- [ ] Refine requirements using MAI pain points and Apollo documents
- [ ] Validate scale targets and platform constraints (AKS + Spark)
- [ ] Decide preferred approach after OpenAI cache evaluation and comparisons

## Collaborators

| Person | Role | Company |
|--------|------|---------|
| [[Jai Menon]] |  |  |
| [[Nagendra]] |  |  |
| [[Lukasz]] |  |  |
| [[Sila]] | Lawyer / legal contact (implied) |  |
| [[Pete]] |  |  |
| [[Krishnan]] |  |  |
| [[Manish]] |  |  |
| [[Ong]] |  |  |
| [[Wamshi]] |  |  |
| [[Brendan]] |  |  |
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

## Topics / Themes

MAI unified caching strategy (training-first, later inference/KB caching), OpenAI cache IP/code access and legal clearance, Scalability requirements (100k nodes; 400k/40k GPU targets), AKS + Spark integration constraints, Comparison of caching options (BlobFuse, Alluxio/DAX, AC Store, OpenAI cache), Blob performance roadmap: Bifrost direct read path and DeltaZero follow-on, Snapshot feedback and potential escalation path (Ong, Manish, Wamshi), Multi-region cache pooling possibility

## Related People

- [[Jai Menon]]
- [[Nagendra]]
- [[Lukasz]]
- [[Sila]]
- [[Pete]]
- [[Krishnan]]
- [[Manish]]
- [[Ong]]
- [[Wamshi]]
- [[Brendan]]
- [[Yumin]]
- [[Jason Vallery]]

## Related Customers

- [[Microsoft]]

## Recent Context

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