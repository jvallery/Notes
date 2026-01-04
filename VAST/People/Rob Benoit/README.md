---
type: people
title: Rob Benoit
created: '2026-01-03'
last_contact: '2025-10-01'
auto_created: true
tags:
- type/people
- needs-review
---

# Rob Benoit

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
FROM "VAST/People/Rob Benoit"
WHERE !completed
SORT due ASC
```

## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@RobBenoit") AND !completed
SORT due ASC
```

## Key Facts

## Recent Context

- 2025-10-01: Tech Summit content coordination

- 2025-10-31: Discussed VAST-in-cloud strategy (object storage + bare metal), DataSpaces/global namespace differentiation, and SE enablement gaps; agreed to follow up at Tech Summit. ([[2025-10-31 - VAST cloud strategy and enablement]])