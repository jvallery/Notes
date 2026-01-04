---
type: people
title: Kurt Niebuhr
created: '2026-01-03'
last_contact: '2025-10-01'
auto_created: true
tags:
- type/people
- needs-review
---

# Kurt Niebuhr

## Contact Information

| Field          | Value     |
| -------------- | --------- |
| **Role**       | _Unknown_ |
| **Company**    | _Unknown_ |
| **Department** | _Unknown_ |
| **Email**      | _Unknown_ |
| **Phone**      | _Unknown_ |
| **LinkedIn**   | _Unknown_ |
| **Location**   | _Unknown_ |

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
FROM "VAST/People/Kurt Niebuhr"
WHERE !completed
SORT due ASC
```

## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@KurtNiebuhr") AND !completed
SORT due ASC
```

## Key Facts

## Recent Context

- 2025-10-01: Neo-cloud partnership pipeline updates; Supercomputing touchpoints/intros planning.

- 2025-10-27: [[2025-10-27 - VAST into Azure GTM]] (via Microsoft)