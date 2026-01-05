---
type: people
title: Vishnu Charan TJ
created: '2026-01-03'
last_contact: '2025-09-16'
auto_created: true
tags:
- type/people
- needs-review
---

# Vishnu Charan TJ

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
FROM "VAST/People/Vishnu Charan TJ"
WHERE !completed
SORT due ASC
```

## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@VishnuCharanTJ") AND !completed
SORT due ASC
```

## Key Facts

## Recent Context

- 2025-09-16: Discussed distributed cache private preview planning (AKS Linux mount vs CSI), scale testing (100–200 nodes), and MAI re-engagement after metrics are ready.

- 2025-09-15: Discussed Blobfuse distributed caching preview scope/gaps, benchmarking needs, and NVIDIA Dynamo KVCache offload exploration.