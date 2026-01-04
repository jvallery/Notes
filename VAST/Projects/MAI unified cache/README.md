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

## Status

| Field | Value |
|-------|-------|
| **Status** | active |
| **Owner** | Jai Menon |

## Overview

Define and deliver a single, pluggable caching solution for MAI that prioritizes training workloads first and later supports inference/KB caching; must scale to ~100k nodes and run on AKS + Spark, potentially with multi-region logical pooling.

## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed
SORT due ASC
```

## Recent Context

- 2025-09-03: [[2025-09-03 - Jai outlined a near-term technical focus evaluate OpenAI’s caching code as a ca]] - Weekly 1:1 where Jai Menon aligned with Jason Vallery on a near-term technical focus: evaluate OpenA... (via Jai Menon)

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
