---
type: people
title: Melissa Du
created: '2026-01-03'
last_contact: unknown
auto_created: true
tags:
- type/people
- needs-review
- company/openai
---

# Melissa Du

## Profile

**Role**: Logistics for “neo clouds” / CoreWeave (finance/capacity org) at OpenAI (Finance/capacity)
**Relationship**: Customer stakeholder

**Background**:
- Handles logistics for 'neo clouds'/CoreWeave-related capacity; under Kevin Park.

## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed AND contains(text, "Melissa Du")
SORT due ASC
```

## Recent Context

- unknown: [[Oct 22nd, 2025]] - Stakeholder mapping and technical positioning for an OpenAI research primary storage proof-of-concep... (via Sam Hopewell)

## Key Facts

- OpenAI tiering vocabulary: Azure Blob = cold; VAST = warm (near GPUs, efficient/high-throughput for staging large working sets); on-GPU/local = hot/ultra.
- POC goal: make more clusters research-worthy despite poor/transient WAN by staging checkpoints/training sets locally and serving some reads from VAST when GPU caching isn’t required.
- Status is on-hold due to firefighting/bandwidth and internal decision backlog; a CoreWeave cluster is waiting for go-aheads to 'kick tires'.
- OpenAI is building their own global state on top of a converged layer plus multiple cloud object stores; they question reliability and metadata performance of third-party global namespaces and worry about single blast radius and metadata scalability at multi-EiB.
- Constraint: do not touch software stack on GPU hosts unless net throughput gains are proven; prefer any namespace/client component to run on VAST servers and expose local object endpoints; avoid heavy agents on GPU nodes.
- Internal pressure exists to complete this because it increases GPU fleet fungibility and unlocks capacity for research projects; Sam is short staffed and actively hiring.

## Background

_Career history, expertise, interests, personal details shared..._

## Key Decisions

- ✅ Near-term approach should focus on per-cluster islands plus object API rather than pushing a third-party global namespace into OpenAI’s stack.

## Related Customers

- [[OpenAI]]

## Related

---
*Last updated: *
