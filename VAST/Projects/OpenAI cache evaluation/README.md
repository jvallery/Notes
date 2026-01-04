---
type: projects
title: OpenAI cache evaluation
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

# OpenAI cache evaluation

## Overview

Evaluate OpenAI’s caching code/IP as a candidate for MAI’s unified cache: confirm legal/IP and repo access, review architecture and readiness, assess scalability to ~100k nodes, and fit with AKS+Spark; compare against BlobFuse, Alluxio/DAX, and AC Store.

## Status

| Field | Value |
|-------|-------|
| **Status** | active |
| **Owner** | Jason Vallery |

## Current Blockers

- ❌ Uncertain legal/IP clearance and repository access to OpenAI cache code
- ❌ Unknown maturity/production readiness of OpenAI cache implementation
- ❌ Unproven scalability to ~100k nodes and potential multi-region pooling requirement
- ❌ Integration fit with AKS + Spark and MAI workflows not validated

## Next Steps

- [ ] Confirm IP/legal clearance and obtain repository access for OpenAI cache code (coordinate with Pete and Sila)
- [ ] Review OpenAI cache code and document architecture and capabilities (training vs inference/KB caching)
- [ ] Assess scalability to ~100k nodes and integration with AKS + Spark; identify gaps vs MAI requirements
- [ ] Collect comparison data from BlobFuse, Alluxio/DAX, and AC Store teams
- [ ] Confirm whether MAI requires multi-region logical cache pooling

## Collaborators

| Person | Role | Company |
|--------|------|---------|
| [[Jai Menon]] |  |  |
| [[Sila]] | Lawyer / legal contact (implied) |  |
| [[Pete]] |  |  |
| [[Wamshi]] |  |  |
| [[Ong]] |  |  |
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
- ✅ Near-term priority is a unified caching approach, with training requirements prioritized first and inference (KB cache) following.
- ✅ Proceed to evaluate OpenAI cache alongside ongoing reviews of Alluxio/DAX, C-Store proposals, and Blockfuse/BlobFuse.
- ✅ Continue Blob performance direction via Bifrost; consider DeltaZero as a subsequent step.

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
- MAI scale targets: ~400k GPUs for training and ~40k GPUs for inference in ~2 years.

## Topics / Themes

MAI unified caching strategy (training-first, later inference/KB caching), OpenAI cache IP/code access and legal clearance, Scalability requirements (100k nodes; 400k/40k GPU targets), AKS + Spark integration constraints, Comparison of caching options (BlobFuse, Alluxio/DAX, AC Store, OpenAI cache), Blob performance roadmap: Bifrost direct read path and DeltaZero follow-on, Snapshot feedback and potential escalation path (Ong, Manish, Wamshi), Multi-region cache pooling possibility, AI caching strategy for MAI (training and inference), OpenAI cache IP/code access and feasibility, Alluxio/DAX as unified cache option, C-Store proposal evaluation, Blockfuse/BlobFuse maturity and performance, MAI requirements: scale, AKS + Spark, possible multi-region pooling, Blob performance roadmap: Bifrost direct-read path and DeltaZero follow-on

## Related People

- [[Jai Menon]]
- [[Sila]]
- [[Pete]]
- [[Wamshi]]
- [[Ong]]
- [[Jason Vallery]]

## Related Customers

- [[Microsoft]]
- [[OpenAI]]

## Recent Context

- 2025-09-03: [[2025-09-03 - Jai outlined a near-term technical focus evaluate OpenAI’s caching code as a ca]] - Weekly 1:1 where Jai Menon aligned with Jason Vallery on a near-term technical focus: evaluate OpenA... (via Jai Menon)
- 2025-09-03: [[2025-09-03 - Jai outlined a high-priority evaluation for an AI caching strategy to support MA]] - Weekly 1:1 where Jai Menon aligned with Jason Vallery on a high-priority evaluation of AI caching st... (via Jai Menon)

## Artifacts

```dataview
TABLE file.mtime as "Modified"
FROM ""
WHERE type != "readme" AND type != "projects"
SORT file.mtime DESC
```

---
*Last updated: *