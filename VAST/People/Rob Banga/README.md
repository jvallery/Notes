---
type: people
title: Rob Banga
created: '2026-01-03'
last_contact: '2025-11-07'
auto_created: true
tags:
- type/people
- needs-review
---

# Rob Banga

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
FROM "VAST/People/Rob Banga"
WHERE !completed
SORT due ASC
```

## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@RobBanga") AND !completed
SORT due ASC
```

## Key Facts

## Recent Context

- 2025-10-30: Cloud support operating model alignment across CS/Support/SRE; hyperscaler priority (GCP→Azure→AWS); marketplace phased rollout; readiness target 2026-02-01. [[2025-10-30 - Cloud support operating model alignment]]

- 2025-10-30: [[2025-10-30 - Maturing VAST SaaS support model]] (via VAST)

- 2025-10-30: [[2025-10-30 - Cloud support roles and readiness]] (via Microsoft)

- 2025-10-31: [[2025-10-31 - VAST cloud strategy and enablement]] (via Rob Benoit)

- 2025-11-07: [[2025-11-07 - Org landscape and cloud strategy]] (via Jeff Denworth)