---
type: people
title: "Jack Kabat"
created: "2026-01-03"
last_contact: "2025-09-18"
auto_created: true
tags:
  - type/people
  - needs-review
---

# Jack Kabat

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
FROM "VAST/People/Jack Kabat"
WHERE !completed
SORT due ASC
```

## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@JackKabat") AND !completed
SORT due ASC
```

## Key Facts

## Recent Context

