---
type: people
title: Qiu Ke
created: '2026-01-03'
last_contact: '2025-09-03'
auto_created: true
tags:
- type/people
- needs-review
- company/microsoft
---

# Qiu Ke

## Contact Information

| Field | Value |
|-------|-------|
| **Role** | CVP |
| **Company** | Microsoft |
| **Department** | _Unknown_ |
| **Email** | _Unknown_ |
| **Phone** | _Unknown_ |
| **LinkedIn** | _Unknown_ |
| **Location** | _Unknown_ |

## Relationship

_How do you work with this person? What is your dynamic?_

## Background

_Career history, expertise, interests, personal details shared..._


## Projects

_What projects are you collaborating on with this person?_

```dataview
LIST
FROM "VAST/Projects" OR "Personal/Projects"
WHERE contains(file.outlinks, this.file.link)
```


## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed AND contains(text, "Qiu Ke")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@QiuKe") AND !completed
SORT due ASC
```

## Key Facts

- MAI scale targets in ~2 years: ~400k GPUs for training (~100k nodes) and ~40k GPUs for inference.
- Primary environment for MAI is AKS/Kubernetes with Spark.
- Caching options under consideration include C-Store proposals (Krishnan’s team), Alluxio/DAX (supports inference/KB caching), OpenAI cache code (pending IP confirmation), and BlockFuse/BlobFuse approaches.
- OpenAI cache access appears permitted for Microsoft services but requires confirmation via Pete and SILA legal.
- Bifrost includes a direct read path from compute to capacity nodes, bypassing FE/table for reads; Lukasz is implementing this component.
- Compute for MAI moved under Brendan’s org (AKS); CVP Qiu Ke involved; Yumin coordinating.
- Possible MAI requirement: multi-region pooling for a distributed cache (unconfirmed).

## Topics Discussed

MAI caching strategy and unified cache goal, OpenAI cache code access and IP/licensing, Scaling requirements to ~100k nodes and AKS/Spark fit, Comparison of caching options (C-Store, Alluxio/DAX, BlobFuse/BlockFuse), Bifrost architecture and direct read path, MAI org changes (compute under AKS leadership), Performance snapshot feedback and follow-up conversations

## Recent Context

- 2025-09-03: [[2025-09-03 - Jai welcomed Jason back and aligned on a forward-looking scope evaluate OpenAI’]] - Weekly 1:1 between Jai Menon and Jason Vallery aligning Jason’s initial scope after returning: evalu... (via Jai Menon)

## Profile

**Role**: CVP at Microsoft (AKS/Kubernetes (compute support for MAI))
**Relationship**: Internal stakeholder (compute leadership)

**Background**:
- CVP in Brendan’s org; involved in MAI compute/AKS support.

## Key Decisions

- ✅ Evaluate OpenAI cache as a first concrete step toward MAI caching strategy.
- ✅ Pursue a single pluggable cache design across training and inference, prioritizing training first.
- ✅ Target deployment environment is AKS + Spark and must scale to ~100k nodes.

## Related Customers

- [[Microsoft]]

## Related




---
*Last updated: *