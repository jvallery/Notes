---
type: people
title: Rajat Monga
created: '2026-01-03'
last_contact: '2025-09-15'
auto_created: true
tags:
- type/people
- needs-review
---

# Rajat Monga

## Profile

**Role**: Leads inferencing stuff (Inferencing)
**Location**: Silicon Valley
**Relationship**: Internal stakeholder (potential offsite participant)

**Background**:
- Potential offsite speaker; inferencing leader interested in KV caching and how inferencing fits into OpenAI inferencing framework.

## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed AND contains(text, "Rajat Monga")
SORT due ASC
```

## Recent Context

- 2025-09-15: [[2025-09-15 - Jason and Jai discussed options and strategy for distributed caching (BlobFuse v]] - Weekly 1:1 between Jason Vallery and Jai Menon focused on choosing a distributed cache strategy (Blo... (via Jai Menon)

## Key Facts

- Team offsite planned in Silicon Valley on 2025-10-15 for ~1.5 days; casual sessions plus social/dinner; release around noon on day 2.
- Goal is a distributed cache strategy covering fan-out writes, fan-out reads, fan-in reads, and separately KV cache.
- MAI currently writes checkpoints to local NVMe and asynchronously copies to Blob; simplicity valued and checkpoints tolerate partial loss.
- BlobFuse PP currently targets fan-out writes with limited/no read caching; some scale testing done via 100-node CycleCloud simulation.
- Inferencing team has been interested in BlobFuse but lacked a usable build for ~2 months.
- Manifold reportedly outperforms OpenAI TensorCache in shared benchmarks and uses consistent hashing (no central metadata store).
- OpenAI TensorCache reportedly moved away from a metadata store toward hashing; churn expected as GPT-6 focuses on memory/long context.
- Key technical concerns: consistent hashing scalability/rebalancing, whether to build a high-TPS metadata/index store, Go+FUSE performance vs C++/kernel client, and Alluxio IP/Java considerations.
- North Star tradeoff: productize best-of open source vs deeply integrate with platform/hardware offloads (kernel-mode, GPUs, DPU/FunOS).

## Background

_Career history, expertise, interests, personal details shared..._

## Key Decisions

- ✅ Jason should book travel to attend the Oct 15 Silicon Valley team offsite.

## Related Projects

- [[Cloud]]

## Related

---
*Last updated: *
