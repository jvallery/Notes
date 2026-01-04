---
type: people
title: Arun Krishna
created: '2026-01-03'
last_contact: '2025-09-03'
auto_created: true
tags:
- type/people
- needs-review
---

# Arun Krishna

## Contact Information

| Field | Value |
|-------|-------|
| **Role** | Senior Presales System Engineer |
| **Company** | VAST Data |
| **Department** | _Unknown_ |
| **Email** | _Unknown_ |
| **Phone** | _Unknown_ |
| **LinkedIn** | _Unknown_ |
| **Location** | San Jose, California |

## Relationship

_How do you work with this person? What is your dynamic?_

## Background

Hari Krishna has 16 years of experience in the field. Prior to joining VAST Data in November 2023, he worked as a Presales Systems Engineer at Dell Technologies from April 2013 to November 2023. He also held positions as a Solutions Architect at EMC, Storage Solutions Architect at MGM Grand Hotel & Casino Las Vegas, Storage Administrator at A.C. Moore, and Senior Storage Engineer at Key Business Solutions, Inc.


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
WHERE !completed AND contains(text, "Arun Krishna")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@ArunKrishna") AND !completed
SORT due ASC
```

## Key Facts

- MAI target scale in ~2 years: ~400k GPUs for training and ~40k GPUs for inferencing.
- Cache must scale to ~100,000 nodes and integrate with AKS/Kubernetes and Spark.
- OpenAI may provide IP/code usable across Microsoft services, pending legal confirmation via Pete and SILA legal.
- Bifrost includes a direct read path bypassing FE/table layers; Lukasz is implementing parts of this.
- Potential MAI requirement: multi-region pooling for a distributed cache (unconfirmed).
- Compute for AI moved out of Arun Krishna’s org into Brendan’s org (AKS/Kubernetes) for MAI bare-metal AKS environment.

## Topics Discussed

Post-sabbatical alignment and role focus shift to technical evaluations, MAI AI caching requirements and scale targets, OpenAI cache feasibility and IP/legal access, Alternative caching options: Blockfuse/BlobFuse, AC Store, Alluxio/DAX, Unified vs separate caches for training and inference/KB caching, AKS/Kubernetes and Spark integration constraints, Bifrost architecture and direct read path, MAI frictions with Microsoft infrastructure, Performance snapshot discussion and potential escalation path, Agentic coding tools/workflow (Codex/Claude/Copilot)

## Recent Context

- 2025-09-03: [[2025-09-03 - Reconnected post-sabbatical and aligned on Jason’s initial focus evaluate OpenA]] - 1:1 between Jason Vallery and Jai Menon after Jason’s sabbatical to align Jason’s initial focus on e... (via Jai Menon)

## Profile

**Relationship**: Internal senior stakeholder

**Background**:
- Previously owned compute for AI; compute moved out of this org into Brendan’s org.

## Key Decisions

- ✅ Primary focus is training cache requirements; inference KB caching follows after.
- ✅ Aim for a unified, pluggable cache design that supports multiple frameworks.
- ✅ Jason to prioritize OpenAI cache evaluation while tracking other options (BlobFuse/Blockfuse, AC Store, Alluxio/DAX).

## Related Customers

- [[Microsoft]]

## Related Projects

- [[AI caching strategy for MAI]]

## Related




---
*Last updated: *