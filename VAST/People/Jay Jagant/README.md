---
type: people
title: Jay Jagant
created: '2026-01-03'
last_contact: '2025-09-29'
auto_created: true
tags:
- type/people
- needs-review
- company/microsoft
---

# Jay Jagant

## Contact Information

| Field | Value |
|-------|-------|
| **Role** |  |
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
WHERE !completed AND contains(text, "Jay Jagant")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@JayJagant") AND !completed
SORT due ASC
```

## Key Facts

- Jason received 100% rewards and felt it did not reflect a high-impact year; he perceived it as potentially retaliatory.
- Jason has 13 years at Microsoft and strong relationships with OpenAI.
- Jason has 2 external job offers and expects ~4 by end of the week; retention risk is high.
- Jason is concerned about insufficient ownership/scope for his IC level and ongoing layoff anxiety; Juergen’s departure reduced his sense of internal support.
- Apollo is funded with a plan to hire ~20 principal+ developers.
- Strategic framing: central storage as system of record; GPU-adjacent storage as cache (read/write cache) for GPU regions.
- OpenAI is squeezing storage pricing; storage cost is becoming more important even in GPU-heavy environments.
- Microsoft lacks a direct storage advocacy channel with NVIDIA; VAST Data is described as having deep NVIDIA alignment and early roadmap access.

## Topics Discussed

Rewards/compensation dissatisfaction and retention risk, Role scope/ownership for senior ICs, Apollo strategy: GPU-adjacent storage, distributed caching, multi-region training, Agentic systems: agentic memory, KVCache, key-value stores, API/ABI direction: POSIX/file APIs vs object storage vs emerging standards, NeoCloud partnerships and competitive dynamics, NVIDIA relationship and roadmap alignment for storage

## Recent Context

- 2025-09-29: [[2025-09-29 - Jason shared disappointment with his rewards and anxiety about scope and support]] - Weekly 1:1 between Maneesh Sah and Jason Vallery focused on Jason’s dissatisfaction with rewards, re... (via Maneesh Sah)

## Profile

**Role**: Microsoft
**Relationship**: Internal collaborator/leader in Apollo area

**Background**:
- Described as non-territorial, smart, and a current high-bandwidth go-to person for Maneesh; expected to create space for Jason in Apollo-related work.

## Related Projects

- [[Apollo]]

## Related




---
*Last updated: *