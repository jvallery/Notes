---
type: projects
title: AI caching strategy for MAI
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

# AI caching strategy for MAI

## Overview

Define and execute a unified, pluggable caching strategy for MAI at extreme scale, prioritizing training cache requirements first and adding inference/KB caching later; evaluate OpenAI cache/IP and alternatives (BlobFuse/Blockfuse, AC Store, Alluxio/DAX).

## Status

| Field | Value |
|-------|-------|
| **Status** | active |
| **Owner** | Jai Menon |

## Current Blockers

- ❌ Unclear IP/legal access to OpenAI cache code and which components are available
- ❌ Uncertainty whether OpenAI cache is unified across training and inference/KB or separate
- ❌ Potential multi-region pooling requirement for distributed cache (unconfirmed)
- ❌ Risk that solutions may not scale to ~100,000 nodes or meet MAI performance targets
- ❌ Integration complexity with AKS/Kubernetes and Spark at MAI scale

## Next Steps

- [ ] Confirm OpenAI IP rights and obtain code access
- [ ] Evaluate OpenAI caching architecture and feasibility for MAI (scale, performance, AKS/Spark fit)
- [ ] Meet MAI stakeholders to confirm requirements and cluster status
- [ ] Compare alternative cache options and document pros/cons
- [ ] Draft requirements/options document (training-first; inference KB later)

## Collaborators

| Person | Role | Company |
|--------|------|---------|
| [[Jai Menon]] |  |  |
| [[Pete]] |  |  |
| [[Manish]] |  |  |
| [[Ong]] |  |  |
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

- ✅ Primary focus is training cache requirements; inference KB caching follows after.
- ✅ Aim for a unified, pluggable cache design that supports multiple frameworks.
- ✅ Jason to prioritize OpenAI cache evaluation while tracking other options (BlobFuse/Blockfuse, AC Store, Alluxio/DAX).

## Key Facts

- MAI target scale in ~2 years: ~400k GPUs for training and ~40k GPUs for inferencing.
- Cache must scale to ~100,000 nodes and integrate with AKS/Kubernetes and Spark.
- OpenAI may provide IP/code usable across Microsoft services, pending legal confirmation via Pete and SILA legal.
- Bifrost includes a direct read path bypassing FE/table layers; Lukasz is implementing parts of this.
- Potential MAI requirement: multi-region pooling for a distributed cache (unconfirmed).
- Compute for AI moved out of Arun Krishna’s org into Brendan’s org (AKS/Kubernetes) for MAI bare-metal AKS environment.

## Topics / Themes

Post-sabbatical alignment and role focus shift to technical evaluations, MAI AI caching requirements and scale targets, OpenAI cache feasibility and IP/legal access, Alternative caching options: Blockfuse/BlobFuse, AC Store, Alluxio/DAX, Unified vs separate caches for training and inference/KB caching, AKS/Kubernetes and Spark integration constraints, Bifrost architecture and direct read path, MAI frictions with Microsoft infrastructure, Performance snapshot discussion and potential escalation path, Agentic coding tools/workflow (Codex/Claude/Copilot)

## Related People

- [[Jai Menon]]
- [[Pete]]
- [[Manish]]
- [[Ong]]
- [[Yumin]]
- [[Jason Vallery]]

## Related Customers

- [[Microsoft]]
- [[OpenAI]]

## Recent Context

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