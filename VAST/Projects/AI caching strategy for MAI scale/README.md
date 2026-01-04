---
type: projects
title: AI caching strategy for MAI scale
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

# AI caching strategy for MAI scale

## Overview

Define a unified, pluggable caching approach to meet MAI training-first requirements and later inference/KB caching, at extreme scale (target ~100k nodes) in an AKS + Spark environment; compare multiple options and align with Blob performance improvements.

## Status

| Field | Value |
|-------|-------|
| **Status** | active |
| **Owner** | Jai Menon |

## Current Blockers

- ❌ Uncertainty and timing around IP/legal rights and access to OpenAI cache code
- ❌ Potential need for multi-region, cross-WAN cache pooling (requirements to confirm)
- ❌ Integration complexity with AKS/Spark and varied training/inference frameworks
- ❌ Org/ownership shifts across teams may slow coordination

## Next Steps

- [ ] Clarify MAI requirements (scale, regions, timelines) with Ong
- [ ] Evaluate OpenAI cache feasibility and compare against Alluxio/DAX, C-Store, and Blockfuse/BlobFuse
- [ ] Continue Blob performance direction via Bifrost; consider DeltaZero sequencing

## Collaborators

| Person | Role | Company |
|--------|------|---------|
| [[Jai Menon]] |  |  |
| [[Qi Ke]] | CVP | Microsoft |
| [[Ong]] |  | Microsoft |
| [[Yumin]] |  | Microsoft |
| [[Jason Vallery]] | Product management (cloud); partnerships with hyperscale cloud providers | VAST Data |

## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed
SORT due ASC
```


## Key Decisions

- ✅ Near-term priority is a unified caching approach, with training requirements prioritized first and inference (KB cache) following.
- ✅ Proceed to evaluate OpenAI cache alongside ongoing reviews of Alluxio/DAX, C-Store proposals, and Blockfuse/BlobFuse.
- ✅ Continue Blob performance direction via Bifrost; consider DeltaZero as a subsequent step.

## Key Facts

- MAI scale targets: ~400k GPUs for training and ~40k GPUs for inference in ~2 years.
- Target data-plane scale for caching: ~100k nodes; environment focus: AKS + Spark.
- Potential requirement: multi-region, cross-WAN cache pooling (to confirm with MAI).
- Bifrost includes a direct read path bypassing FE/table for reads by caching location info and reading directly from capacity nodes.
- DeltaZero is positioned as a follow-on to Bifrost (positioning still in progress).
- Compute for MAI moved into Brendan’s AKS org; Qi ("Kiki") Ke (CVP) leads compute side; Yumin interfaces from storage side.
- Performance snapshot outcome appears to be 'Meets Expectations'; Jason is disappointed and plans to discuss with Ong and potentially Manish.

## Topics / Themes

AI caching strategy for MAI (training and inference), OpenAI cache IP/code access and feasibility, Alluxio/DAX as unified cache option, C-Store proposal evaluation, Blockfuse/BlobFuse maturity and performance, MAI requirements: scale, AKS + Spark, possible multi-region pooling, Blob performance roadmap: Bifrost direct-read path and DeltaZero follow-on, Performance snapshot discussion and escalation path, Establishing ongoing 1:1 cadence

## Related People

- [[Jai Menon]]
- [[Qi Ke]]
- [[Ong]]
- [[Yumin]]
- [[Jason Vallery]]

## Related Customers

- [[Microsoft]]

## Recent Context

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