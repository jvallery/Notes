---
type: people
title: Yogev Vankin
created: '2026-01-03'
last_contact: '2025-10-01'
auto_created: true
tags:
- type/people
- needs-review
---

# Yogev Vankin

## Profile

**Role**: _Unknown_
**Company**: _Unknown_
**Location**: _Unknown_
**Relationship**: _How do you work with this person?_

**Background**:
_Career history, expertise, interests..._
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
FROM "VAST/People/Yogev Vankin"
WHERE !completed
SORT due ASC
```

## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@YogevVankin") AND !completed
SORT due ASC
```

## Key Facts

## Recent Context

- 2025-10-01: [[2025-10-01 - Oracle Cloud POC learnings]]

- 2025-11-03: [[2025-11-03 - 5.5 plan timeline review]] (via Roy)