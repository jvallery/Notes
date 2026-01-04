---
type: people
title: Akanksha Mehrotra
created: '2026-01-03'
last_contact: '2025-09-16'
auto_created: true
tags:
- type/people
- needs-review
---

# Akanksha Mehrotra

## Contact Information

| Field | Value |
|-------|-------|
| **Role** |  |
| **Company** |  |
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
WHERE !completed AND contains(text, "Akanksha Mehrotra")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@AkankshaMehrotra") AND !completed
SORT due ASC
```

## Key Facts

- Distributed cache for checkpointing (write/read) implementation is complete; node up/down scenarios are under test.
- MVP scope is checkpointing only: no model/dataset loading, no prefetch, and no cross-node model refill on node loss.
- Two checkpoint modes exist: cache-only and cache with lazy writeback to storage.
- AKS integration will use Linux mounts initially due to CSI/containers team concerns about internal node communications and Kubernetes integration.
- Scale testing planned at 100–200 nodes with intent to extrapolate to 10k–100k nodes; need to quantify TPS per node and throughput reduction to Blob.
- Figure AI is the initial preview candidate and uses VMSS (not AKS) for training; AKS work is primarily motivated by MAI.
- MAI is not adopting BlobFuse currently; re-engagement depends on a data-driven narrative (throughput reduction, scalability, reliability).
- CoreAI requested SSD-only KV cache offload without cloud tier; feasibility is unclear.
- AWS patterns referenced: PyTorch S3 storage writer, prefix layout/naming to reduce partition hot-spotting/503s, and S3 Express as a cache reference.

## Topics Discussed

Distributed cache for checkpointing status and MVP scope, Scale and resilience testing (100–200 nodes) and extrapolation to 10k–100k nodes, Network throughput reduction measurement to Blob and TPS per node to metadata/blob, AKS integration approach: Linux mount vs CSI PV and containers team concerns, Private preview planning and customer cohort (Figure AI first; MAI deferred), CoreAI SSD-only KV cache offload request, Long-term strategy: open-source/Python tool contributions vs kernel-mode driver vs user-mode library, AWS reference implementations (PyTorch S3 storage writer, prefix entropy, S3 Express)

## Recent Context

- 2025-09-16: [[2025-09-16 - Team reviewed status of distributed cache for checkpointing implementation comp]] - Weekly 1:1 focused on the distributed cache for checkpointing: implementation is complete, with scal... (via Vishnu Charan TJ)

## Profile

**Relationship**: Internal collaborator

**Background**:
- Running scale tests and capturing performance metrics (including throughput reduction) for distributed cache checkpointing.

## Key Decisions

- ✅ Proceed toward a private preview by end of September with Figure AI; defer MAI until metrics and scale narrative are ready.
- ✅ Use Linux mount for AKS integration initially; CSI route remains under evaluation.
- ✅ Focus preview on checkpointing use cases; exclude model/dataset loading and prefetch for MVP.
- ✅ Include measurement of network throughput reduction and TPS to metadata/blob as part of scale testing.

## Related Projects

- [[Cloud]]

## Related




---
*Last updated: *