---
type: people
title: Pete Emig
created: '2026-01-03'
last_contact: '2025-09-30'
auto_created: true
tags:
- type/people
- needs-review
---

# Pete Emig

## Profile

**Relationship**: Industry contact / former candidate-hire connection

**Background**:
- Met Jason during Jason’s Amazon interview process; later became friends and Jason eventually hired him (direction reversed).

## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed AND contains(text, "Pete Emig")
SORT due ASC
```

## Recent Context

- 2025-12-19: [[2025-12-19]] - Discussion between Jeff Denworth and Jason Vallery on VAST’s Microsoft/Azure strategy: what level of... (via Jeff Denworth)
- 2025-10-27: [[2025-10-27 - Jason and Kurt aligned on a go-to-market path to bring VAST’s high-density, lowe]] - Weekly 1:1 where Jason Vallery and Kurt Niebuhr aligned on a Microsoft Azure go-to-market path for V... (via Kurt Niebuhr)
- 2025-09-30: [[2025-09-30 - Jason shared that after meeting with Manish and reviewing rewards, he began expl]] - Weekly 1:1 between Jai Menon and Jason Vallery focused on Jason’s retention risk after disappointing... (via Jai Menon)
- 2025-09-15: [[2025-09-15 - Jason and Jai discussed options and strategy for distributed caching (BlobFuse v]] - Weekly 1:1 between Jason Vallery and Jai Menon focused on choosing a distributed cache strategy (Blo... (via Jai Menon)
- 2025-09-03: [[2025-09-03 - Jai welcomed Jason back and aligned on a forward-looking scope evaluate OpenAI’]] - Weekly 1:1 between Jai Menon and Jason Vallery aligning Jason’s initial scope after returning: evalu... (via Jai Menon)
- 2025-09-03: [[2025-09-03 - Jai outlined a near-term technical focus evaluate OpenAI’s caching code as a ca]] - Weekly 1:1 where Jai Menon aligned with Jason Vallery on a near-term technical focus: evaluate OpenA... (via Jai Menon)
- 2025-09-03: [[2025-09-03 - Jai outlined a high-priority evaluation for an AI caching strategy to support MA]] - Weekly 1:1 where Jai Menon aligned with Jason Vallery on a high-priority evaluation of AI caching st... (via Jai Menon)
- 2025-09-03: [[2025-09-03 - Reconnected post-sabbatical and aligned on Jason’s initial focus evaluate OpenA]] - 1:1 between Jason Vallery and Jai Menon after Jason’s sabbatical to align Jason’s initial focus on e... (via Jai Menon)

## Key Facts

- Jason has been at Microsoft for 13 years.
- Jason previously received a large Microsoft stock grant after presenting an Amazon offer to Juergen; the 4-year vest completes soon.
- Jason has four external opportunities (two likely, two ruled out), including verbal commitments and an expected strong written offer after a CEO call.
- Jason’s decision timeline target was end of the week; he planned to share his best offer and explicit stay requirements.
- Jason prefers a management/leadership role with clear scope/ownership and latitude to execute; he is not interested in moving to another hyperscaler.
- Apollo storage: concern that datacenter buildouts require near-term storage now, while a clean-sheet stack could take 2–3 years; build vs buy/partner remains open.


- MAI scale targets in ~2 years: ~400k GPUs for training (~100k nodes) and ~40k GPUs for inference.
- Primary environment for MAI is AKS/Kubernetes with Spark.
- Caching options under consideration include C-Store proposals (Krishnan’s team), Alluxio/DAX (supports inference/KB caching), OpenAI cache code (pending IP confirmation), and BlockFuse/BlobFuse approaches.
- OpenAI cache access appears permitted for Microsoft services but requires confirmation via Pete and SILA legal.
- Bifrost includes a direct read path from compute to capacity nodes, bypassing FE/table for reads; Lukasz is implementing this component.
- Compute for MAI moved under Brendan’s org (AKS); CVP Qiu Ke involved; Yumin coordinating.
- Possible MAI requirement: multi-region pooling for a distributed cache (unconfirmed).
- MAI targets 400k GPUs for training and 40k GPUs for inference within 2 years.
- Cache must scale to ~100k nodes and run on AKS + Spark.
- OpenAI cache IP may be usable by Microsoft, but legal/IP clearance and repo access must be confirmed (Pete and Sila involved).

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

- ✅ Proceed with a competitive-offer approach to evaluate a Microsoft retention path.
- ✅ Keep communication open this week and reassess after Jason’s offer arrives.
- ✅ Shared view that Apollo likely requires a clean-sheet storage approach to be competitive.

## Related Customers

- [[Amazon]]

## Related

---
*Last updated: *
