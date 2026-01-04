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

## Status

| Field | Value |
|-------|-------|
| **Status** | active |
| **Owner** | Jai Menon |

## Overview

Define a unified, pluggable caching approach to meet MAI training-first requirements and later inference/KB caching, at extreme scale (target ~100k nodes) in an AKS + Spark environment; compare multiple options and align with Blob performance improvements.

## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed
SORT due ASC
```

## Recent Context

- 2025-09-03: [[2025-09-03 - Jai outlined a high-priority evaluation for an AI caching strategy to support MA]] - Weekly 1:1 where Jai Menon aligned with Jason Vallery on a high-priority evaluation of AI caching st... (via Jai Menon)

## Key Facts

- MAI scale targets: ~400k GPUs for training and ~40k GPUs for inference in ~2 years.
- Target data-plane scale for caching: ~100k nodes; environment focus: AKS + Spark.
- Potential requirement: multi-region, cross-WAN cache pooling (to confirm with MAI).
- Bifrost includes a direct read path bypassing FE/table for reads by caching location info and reading directly from capacity nodes.
- DeltaZero is positioned as a follow-on to Bifrost (positioning still in progress).
- Compute for MAI moved into Brendan’s AKS org; Qi ("Kiki") Ke (CVP) leads compute side; Yumin interfaces from storage side.
- Performance snapshot outcome appears to be 'Meets Expectations'; Jason is disappointed and plans to discuss with Ong and potentially Manish.
