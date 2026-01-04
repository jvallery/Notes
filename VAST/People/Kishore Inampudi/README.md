---
type: people
title: Kishore Inampudi
created: '2026-01-03'
last_contact: '2025-10-01'
auto_created: true
tags:
- type/people
- needs-review
---

# Kishore Inampudi

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
FROM "VAST/People/Kishore Inampudi"
WHERE !completed
SORT due ASC
```

## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@KishoreInampudi") AND !completed
SORT due ASC
```

## Key Facts

## Recent Context

- 2025-10-01: Azure Extended Zones coordination; align on storage needs after A2N approval. ([[2025-10-01 - Azure Extended Zones coordination]])

- 2025-10-30: [[2025-10-30 - MAI exabyte storage options]] (via Microsoft)

- 2025-10-28: [[2025-10-28 - Align on MAI and UK Met]] (via Kanchan Mehrotra)