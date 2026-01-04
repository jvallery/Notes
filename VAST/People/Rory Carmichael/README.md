---
type: people
title: Rory Carmichael
created: '2026-01-03'
last_contact: unknown
auto_created: true
tags:
- type/people
- needs-review
- company/openai
---

# Rory Carmichael

## Contact Information

| Field | Value |
|-------|-------|
| **Role** | Owns research infrastructure/supercomputers; Sam's boss |
| **Company** | OpenAI |
| **Department** | _Unknown_ |
| **Email** | _Unknown_ |
| **Phone** | _Unknown_ |
| **LinkedIn** | _Unknown_ |
| **Location** | _Unknown_ |

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
FROM ""
WHERE !completed AND contains(text, "Rory Carmichael")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@RoryCarmichael") AND !completed
SORT due ASC
```

## Key Facts

- OpenAI tiering vocabulary: Azure Blob = cold; VAST = warm (near GPUs, efficient/high-throughput for staging large working sets); on-GPU/local = hot/ultra.
- POC goal: make more clusters research-worthy despite poor/transient WAN by staging checkpoints/training sets locally and serving some reads from VAST when GPU caching isn’t required.
- Status is on-hold due to firefighting/bandwidth and internal decision backlog; a CoreWeave cluster is waiting for go-aheads to 'kick tires'.
- OpenAI is building their own global state on top of a converged layer plus multiple cloud object stores; they question reliability and metadata performance of third-party global namespaces and worry about single blast radius and metadata scalability at multi-EiB.
- Constraint: do not touch software stack on GPU hosts unless net throughput gains are proven; prefer any namespace/client component to run on VAST servers and expose local object endpoints; avoid heavy agents on GPU nodes.
- Internal pressure exists to complete this because it increases GPU fleet fungibility and unlocks capacity for research projects; Sam is short staffed and actively hiring.

## Topics Discussed

OpenAI stakeholder map for research storage/infra, VAST as near-GPU warm storage to mitigate WAN/Azure variability, Storage tiering vocabulary (cold/warm/hot), POC status and operational blockers (bandwidth/firefighting, decision backlog), Global namespace skepticism and metadata scalability at multi-EiB, Architecture constraints: no heavy GPU-host agents; local object endpoints, Win criteria: throughput, list/TPS, WAN resilience, low overhead, fast feature turnaround

## Recent Context

- unknown: [[Oct 22nd, 2025]] - Stakeholder mapping and technical positioning for an OpenAI research primary storage proof-of-concep... (via Sam Hopewell)

## Profile

**Role**: Owns research infrastructure/supercomputers; Sam's boss at OpenAI (Research infrastructure)
**Relationship**: Customer stakeholder (management chain)

**Background**:
- Leads research infra/supercomputers; management chain above Sam.

## Key Decisions

- ✅ Near-term approach should focus on per-cluster islands plus object API rather than pushing a third-party global namespace into OpenAI’s stack.

## Related Customers

- [[OpenAI]]

## Related




---
*Last updated: *