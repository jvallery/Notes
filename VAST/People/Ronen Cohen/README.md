---
type: people
title: Ronen Cohen
created: '2026-01-03'
last_contact: unknown
auto_created: true
tags:
- type/people
- needs-review
- company/vast-data
---

# Ronen Cohen

## Contact Information

| Field | Value |
|-------|-------|
| **Role** |  |
| **Company** | VAST Data |
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
WHERE !completed AND contains(text, "Ronen Cohen")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@RonenCohen") AND !completed
SORT due ASC
```

## Key Facts

- Internal Slack contacts for Shachar Feinblit: Omri (support), Ronnie Lazar and Maxim Dunaivicher (cloud), Liron (UX), Yaniv Sharon (QA cloud), Ronen Cohen and Dotan Arnin (solution).

## Topics Discussed

Internal points of contact, Support, Cloud, UX, QA cloud, Solution

## Recent Context

- unknown: [[_Open Topics]] - Open topics note for Shachar Feinblit, listing key internal Slack contacts by functional area (suppo... (via Shachar Feinblit)

## Profile

**Role**: VAST Data (Solution)
**Relationship**: Internal collaborator

**Background**:
- Listed as a Solution contact in Slack.

## Related




---
*Last updated: *