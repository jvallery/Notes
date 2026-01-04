---
type: people
title: Kanchan Mehrotra
created: '2026-01-03'
last_contact: '2025-10-01'
auto_created: true
tags:
- type/people
- needs-review
---

# Kanchan Mehrotra

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
FROM "VAST/People/Kanchan Mehrotra"
WHERE !completed
SORT due ASC
```

## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@KanchanMehrotra") AND !completed
SORT due ASC
```

## Key Facts

## Recent Context

- 2025-10-01: [[2025-10-01 - Follow-up on storage plays]]

- 2025-10-28: Aligned on MAI + UK Met Office as marquee wins to create exec pull for a VAST-suitable Azure hardware shape; dual-track marketplace offer + leadership-backed hardware path.

- 2025-10-28: [[2025-10-28 - Align on MAI and UKMO]] (via Microsoft)

- 2025-10-28: [[2025-10-28 - UK Met Gen2 pilot planning]] (via Microsoft)

- 2025-10-30: [[2025-10-30 - MAI testing path and deck]] (via Lior Genzel)

- 2025-11-06: [[2025-11-06 - VAST adoption in Microsoft programs]] (via Microsoft)

- 2025-11-06: [[2025-11-06 - VAST momentum and Azure Apollo]] (via Microsoft)