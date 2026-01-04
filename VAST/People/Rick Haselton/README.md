---
type: people
title: Rick Haselton
created: '2026-01-03'
last_contact: '2025-10-01'
auto_created: true
tags:
- type/people
- needs-review
---

# Rick Haselton

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
FROM "VAST/People/Rick Haselton"
WHERE !completed
SORT due ASC
```

## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@RickHaselton") AND !completed
SORT due ASC
```

## Key Facts

## Recent Context

- 2025-10-01: Customer Success workflow alignment; action item to meet with Customer Success to understand end-to-end account support workflows. ([[2025-10-01 - Customer Success workflow alignment]])

- 2025-10-29: Cloud-first VAST-as-a-Service/CS operating model discussion; CoreWeave/XAI support patterns, SLAs, and multi-cluster namespace limitations.

- 2025-10-29: Discussed CS/SRE operating model for CoreWeave/xAI, incident drivers, RMA workflow, and SLA/SLO expectations.