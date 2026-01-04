---
type: projects
title: C-Store proposals
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

# C-Store proposals

## Overview

Internal proposals (Krishnan and team) around using a C-Store approach as part of caching strategy; needs evaluation against MAI requirements and other options.

## Status

| Field | Value |
|-------|-------|
| **Status** | active |
| **Owner** | _Unknown_ |

## Current Blockers

- ❌ Unclear maturity and performance characteristics vs requirements

## Next Steps

- [ ] Assess whether C-Store is needed and how it meets MAI requirements
- [ ] Include in comparative recommendation

## Collaborators

| Person | Role | Company |
|--------|------|---------|
| [[Yumin]] |  | Microsoft |

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

- [[Yumin]]

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