---
type: people
title: SILA legal
created: '2026-01-03'
last_contact: '2025-09-03'
auto_created: true
tags:
- type/people
- needs-review
---

# SILA legal

## Profile

**Role**: Legal
**Relationship**: Internal legal stakeholder

**Background**:
- Legal group involved in confirming OpenAI IP rights and code access for Microsoft services.

## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed AND contains(text, "SILA legal")
SORT due ASC
```

## Recent Context

- 2025-09-03: [[2025-09-03 - Jai welcomed Jason back and aligned on a forward-looking scope evaluate OpenAI’]] - Weekly 1:1 between Jai Menon and Jason Vallery aligning Jason’s initial scope after returning: evalu... (via Jai Menon)
- 2025-09-03: [[2025-09-03 - Jai outlined a near-term technical focus evaluate OpenAI’s caching code as a ca]] - Weekly 1:1 where Jai Menon aligned with Jason Vallery on a near-term technical focus: evaluate OpenA... (via Jai Menon)
- 2025-09-03: [[2025-09-03 - Reconnected post-sabbatical and aligned on Jason’s initial focus evaluate OpenA]] - 1:1 between Jason Vallery and Jai Menon after Jason’s sabbatical to align Jason’s initial focus on e... (via Jai Menon)

## Key Facts

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

## Background

_Career history, expertise, interests, personal details shared..._

## Key Decisions

- ✅ Evaluate OpenAI cache as a first concrete step toward MAI caching strategy.
- ✅ Pursue a single pluggable cache design across training and inference, prioritizing training first.
- ✅ Target deployment environment is AKS + Spark and must scale to ~100k nodes.
- ✅ Jason will lead the OpenAI cache evaluation and comparison against internal/external options.
- ✅ Design preference is a single, pluggable cache for training and inference (including KB caching), framework-agnostic; prioritize training first.
- ✅ Near-term performance direction centers on Bifrost (including a direct read path) plus a distributed cache; DeltaZero positioned as follow-on.
- ✅ Primary focus is training cache requirements; inference KB caching follows after.
- ✅ Aim for a unified, pluggable cache design that supports multiple frameworks.
- ✅ Jason to prioritize OpenAI cache evaluation while tracking other options (BlobFuse/Blockfuse, AC Store, Alluxio/DAX).

## Related Customers

- [[Microsoft]]
- [[OpenAI]]

## Related Projects

- [[AI caching strategy for MAI]]

## Related

---
*Last updated: *
