---
type: people
title: Pete Eming
created: '2026-01-03'
last_contact: '2025-12-19'
auto_created: true
tags:
- type/people
- needs-review
---

# Pete Eming

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
WHERE !completed AND contains(text, "Pete Eming")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@PeteEming") AND !completed
SORT due ASC
```

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

## Topics Discussed

MAI caching strategy and unified cache goal, OpenAI cache code access and IP/licensing, Scaling requirements to ~100k nodes and AKS/Spark fit, Comparison of caching options (C-Store, Alluxio/DAX, BlobFuse/BlockFuse), Bifrost architecture and direct read path, MAI org changes (compute under AKS leadership), Performance snapshot feedback and follow-up conversations, MAI unified caching strategy (training-first, later inference/KB caching), OpenAI cache IP/code access and legal clearance, Scalability requirements (100k nodes; 400k/40k GPU targets), AKS + Spark integration constraints, Comparison of caching options (BlobFuse, Alluxio/DAX, AC Store, OpenAI cache), Blob performance roadmap: Bifrost direct read path and DeltaZero follow-on, Snapshot feedback and potential escalation path (Ong, Manish, Wamshi), Multi-region cache pooling possibility

## Recent Context

- 2025-12-19: [[2025-12-19]] - Discussion between Jeff Denworth and Jason Vallery on VAST’s Microsoft/Azure strategy: what level of... (via Jeff Denworth)
- 2025-10-27: [[2025-10-27 - Jason and Kurt aligned on a go-to-market path to bring VAST’s high-density, lowe]] - Weekly 1:1 where Jason Vallery and Kurt Niebuhr aligned on a Microsoft Azure go-to-market path for V... (via Kurt Niebuhr)
- 2025-09-03: [[2025-09-03 - Jai welcomed Jason back and aligned on a forward-looking scope evaluate OpenAI’]] - Weekly 1:1 between Jai Menon and Jason Vallery aligning Jason’s initial scope after returning: evalu... (via Jai Menon)
- 2025-09-03: [[2025-09-03 - Jai outlined a near-term technical focus evaluate OpenAI’s caching code as a ca]] - Weekly 1:1 where Jai Menon aligned with Jason Vallery on a near-term technical focus: evaluate OpenA... (via Jai Menon)
- 2025-09-03: [[2025-09-03 - Jai outlined a high-priority evaluation for an AI caching strategy to support MA]] - Weekly 1:1 where Jai Menon aligned with Jason Vallery on a high-priority evaluation of AI caching st... (via Jai Menon)
- 2025-09-03: [[2025-09-03 - Reconnected post-sabbatical and aligned on Jason’s initial focus evaluate OpenA]] - 1:1 between Jason Vallery and Jai Menon after Jason’s sabbatical to align Jason’s initial focus on e... (via Jai Menon)

## Profile

**Relationship**: External contact / former colleague

**Background**:
- Reports to Vamshi; previously worked at Amazon; took over ownership of relationship between Azure Storage and OpenAI/Microsoft AI after Jason left; shared that OpenAI is replatforming away from Blob API and building their own data movement solution (e.g., rclone).

## Key Decisions

- ✅ Evaluate OpenAI cache as a first concrete step toward MAI caching strategy.
- ✅ Pursue a single pluggable cache design across training and inference, prioritizing training first.
- ✅ Target deployment environment is AKS + Spark and must scale to ~100k nodes.
- ✅ Jason will lead the OpenAI cache evaluation and comparison against internal/external options.
- ✅ Design preference is a single, pluggable cache for training and inference (including KB caching), framework-agnostic; prioritize training first.
- ✅ Near-term performance direction centers on Bifrost (including a direct read path) plus a distributed cache; DeltaZero positioned as follow-on.
- ✅ Near-term priority is a unified caching approach, with training requirements prioritized first and inference (KB cache) following.
- ✅ Proceed to evaluate OpenAI cache alongside ongoing reviews of Alluxio/DAX, C-Store proposals, and Blockfuse/BlobFuse.
- ✅ Continue Blob performance direction via Bifrost; consider DeltaZero as a subsequent step.
- ✅ Primary focus is training cache requirements; inference KB caching follows after.

## Related Customers

- [[Microsoft]]
- [[OpenAI]]

## Related Projects

- [[VAST on Azure Integration]]

## Related




---
*Last updated: *