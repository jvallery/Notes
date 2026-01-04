---
type: people
title: Pete Emig
created: '2026-01-03'
last_contact: '2025-09-30'
auto_created: true
tags:
- type/people
- needs-review
---

# Pete Emig

## Contact Information

| Field | Value |
|-------|-------|
| **Role** |  |
| **Company** |  |
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
WHERE !completed AND contains(text, "Pete Emig")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@PeteEmig") AND !completed
SORT due ASC
```

## Key Facts

- Jason has been at Microsoft for 13 years.
- Jason previously received a large Microsoft stock grant after presenting an Amazon offer to Juergen; the 4-year vest completes soon.
- Jason has four external opportunities (two likely, two ruled out), including verbal commitments and an expected strong written offer after a CEO call.
- Jason’s decision timeline target was end of the week; he planned to share his best offer and explicit stay requirements.
- Jason prefers a management/leadership role with clear scope/ownership and latitude to execute; he is not interested in moving to another hyperscaler.
- Apollo storage: concern that datacenter buildouts require near-term storage now, while a clean-sheet stack could take 2–3 years; build vs buy/partner remains open.

## Topics Discussed

Retention risk and compensation/rewards, External job offers and decision timeline, Role scope/ownership and management vs IC path, Organizational politics and execution speed, Apollo storage strategy (clean-sheet vs existing Azure Storage/Bifrost), Build vs buy/partner for near-term storage

## Recent Context

- 2025-09-30: [[2025-09-30 - Jason shared that after meeting with Manish and reviewing rewards, he began expl]] - Weekly 1:1 between Jai Menon and Jason Vallery focused on Jason’s retention risk after disappointing... (via Jai Menon)

## Profile

**Relationship**: Industry contact / former candidate-hire connection

**Background**:
- Met Jason during Jason’s Amazon interview process; later became friends and Jason eventually hired him (direction reversed).

## Key Decisions

- ✅ Proceed with a competitive-offer approach to evaluate a Microsoft retention path.
- ✅ Keep communication open this week and reassess after Jason’s offer arrives.
- ✅ Shared view that Apollo likely requires a clean-sheet storage approach to be competitive.

## Related Customers

- [[Amazon]]

## Related




---
*Last updated: *