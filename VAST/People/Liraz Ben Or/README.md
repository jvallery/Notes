---
type: people
title: Liraz Ben Or
last_contact: unknown
created: '2026-01-03'
tags:
- type/people
- generated
---

# Liraz Ben Or

## Recent Context

- unknown: [[2025-10 - Liraz Ben Or]] - Checklist note about syncing with Liraz Ben Or and establishing release gate meeting cadence. Both l...
- unknown: [[2025-10 - Noa Cohen]] - Note tracks a completed action to introduce Jason Vallery and coordinate a sync with program manager... (via Noa Cohen)
- 2025-10-29: [[2025-10-29 - Liraz walked Jason through VAST’s non-traditional release management 4 phase ga]]
- 2025-10-29: [[2025-10-29 - Intro 1-1 where Liraz walked Jason through VAST’s non-traditional release manage]]
- 2025-09-18: [[2025-09-18 - Jason outlined his new architect remit to assess VAST and CoreWeave strategies,]] - Weekly 1:1 between Jack Kabat and Jason Vallery focused on Jason’s new architect remit to deep dive ... (via Jack Kabat)

## Profile

**Role**: Program manager
**Relationship**: Program manager I synced with

**Background**:
- Program manager involved in coordinating with the note author; connected to release gate meetings and cadence.

## Key Facts

- Jason returned from a 3-month sabbatical and moved into a new architect role created by Manish.
- Jason’s initial remit: assess VAST and CoreWeave capabilities, NVIDIA DGX alignment, and gaps in Azure’s storage stack; Project Apollo likely relevant.
- CoreWeave positions VAST as preferred storage but also built its own object storage to avoid full vertical coupling.
- NVIDIA is pushing DGX architecture and hardware-level optimizations integrating with VAST; NVIDIA relies on partners for storage.
- OpenAI pattern: local NVMe on GPU hosts with lazy movement to/from blob for cheap/deep storage; Fairwater cited as an example.
- OpenAI has proprietary global/regional synchronization IP layered above Azure data movement; Azure lacks this as a native storage primitive.
- VAST offers a global namespace (DataSpaces) with cross-region locking and strong consistency; optimized for high-performance flash rather than HDD-based cheap-and-deep.
- Azure’s 70+ regions and convergence of training and inference require layered storage design and distributed consistency.
- Microsoft risks being commoditized by NVIDIA’s roadmap due to storage maturity gaps and historically slow execution.
- Project Apollo introduces uncertainty (innovation path vs duplicative effort).

## Topics

VAST vs CoreWeave storage strategies, NVIDIA DGX architecture direction and partner ecosystem, Azure storage stack gaps for AI training/inference workloads, Global namespace and strong consistency across regions (VAST DataSpaces-like capability), OpenAI storage architecture (local NVMe + blob) and proprietary sync layer, Layered storage approach balancing performance and cost at Azure scale, Project Apollo alignment/overlap risk, Execution speed and commoditization risk from NVIDIA roadmap, UK Met Office Gen 2 (brief mention, no detail), Program manager sync, Release gate meetings, Release cadence, Introductions, Sync with program managers

## Related

<!-- Wikilinks to related entities -->
