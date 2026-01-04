---
type: projects
title: Enlightenment API
created: '2026-01-03'
last_updated: ''
status: on-hold
auto_created: true
tags:
- type/projects
- needs-review
- status/on-hold
last_contact: '2025-09-03'
---

# Enlightenment API

## Status

| Field | Value |
|-------|-------|
| **Status** | on-hold |
| **Owner** | _Unknown_ |

## Overview

Prior project related to redirects/enlightenment API; explicitly stated as not the same as current Bifrost direct path work.

## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed
SORT due ASC
```

## Recent Context

- 2025-09-03: [[2025-09-03 - Reconnected post-sabbatical and aligned on Jason’s initial focus evaluate OpenA]] - 1:1 between Jason Vallery and Jai Menon after Jason’s sabbatical to align Jason’s initial focus on e... (via Jai Menon)

## Key Facts

- MAI target scale in ~2 years: ~400k GPUs for training and ~40k GPUs for inferencing.
- Cache must scale to ~100,000 nodes and integrate with AKS/Kubernetes and Spark.
- OpenAI may provide IP/code usable across Microsoft services, pending legal confirmation via Pete and SILA legal.
- Bifrost includes a direct read path bypassing FE/table layers; Lukasz is implementing parts of this.
- Potential MAI requirement: multi-region pooling for a distributed cache (unconfirmed).
- Compute for AI moved out of Arun Krishna’s org into Brendan’s org (AKS/Kubernetes) for MAI bare-metal AKS environment.
