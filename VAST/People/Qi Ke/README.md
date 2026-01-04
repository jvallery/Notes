---
type: people
title: Qi Ke
created: '2026-01-03'
last_contact: '2025-11-06'
auto_created: true
tags:
- type/people
- needs-review
- company/microsoft
---

# Qi Ke

## Contact Information

| Field | Value |
|-------|-------|
| **Role** | CVP |
| **Company** | Microsoft |
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
WHERE !completed AND contains(text, "Qi Ke")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@QiKe") AND !completed
SORT due ASC
```

## Key Facts

- MAI scale targets: ~400k GPUs for training and ~40k GPUs for inference in ~2 years.
- Target data-plane scale for caching: ~100k nodes; environment focus: AKS + Spark.
- Potential requirement: multi-region, cross-WAN cache pooling (to confirm with MAI).
- Bifrost includes a direct read path bypassing FE/table for reads by caching location info and reading directly from capacity nodes.
- DeltaZero is positioned as a follow-on to Bifrost (positioning still in progress).
- Compute for MAI moved into Brendan’s AKS org; Qi ("Kiki") Ke (CVP) leads compute side; Yumin interfaces from storage side.
- Performance snapshot outcome appears to be 'Meets Expectations'; Jason is disappointed and plans to discuss with Ong and potentially Manish.
- VAST signed an approximately $1.2B software-only licensing deal with CoreWeave (press same day).
- Apollo requested two POCs: urgent VAST-on-VAST hardware (rack shipped) and VAST bare metal on Azure storage hardware.
- Azure storage hardware spec variants include Fungible DPU and NVIDIA BlueField-3; Fungible production rollout in Azure storage is not broadly delivered.


- MAI scale targets in ~2 years: ~400k GPUs for training (~100k nodes) and ~40k GPUs for inference.
- Primary environment for MAI is AKS/Kubernetes with Spark.
- Caching options under consideration include C-Store proposals (Krishnan’s team), Alluxio/DAX (supports inference/KB caching), OpenAI cache code (pending IP confirmation), and BlockFuse/BlobFuse approaches.
- OpenAI cache access appears permitted for Microsoft services but requires confirmation via Pete and SILA legal.
- Bifrost includes a direct read path from compute to capacity nodes, bypassing FE/table for reads; Lukasz is implementing this component.
- Compute for MAI moved under Brendan’s org (AKS); CVP Qiu Ke involved; Yumin coordinating.
- Possible MAI requirement: multi-region pooling for a distributed cache (unconfirmed).
## Topics Discussed

AI caching strategy for MAI (training and inference), OpenAI cache IP/code access and feasibility, Alluxio/DAX as unified cache option, C-Store proposal evaluation, Blockfuse/BlobFuse maturity and performance, MAI requirements: scale, AKS + Spark, possible multi-region pooling, Blob performance roadmap: Bifrost direct-read path and DeltaZero follow-on, Performance snapshot discussion and escalation path, Establishing ongoing 1:1 cadence, MAI and Project Apollo alignment and timelines, VAST bare metal on Azure storage hardware vs VM-based deployment, Fungible DPU readiness risk vs BlueField-3 alternative, Dallas capacity planning (Dec/Apr) and classic Azure feasibility, Networking/SDN (Overlake) constraints for bare metal in classic Azure, NVIDIA DGX Cloud reference architecture and storage throughput requirements


MAI caching strategy and unified cache goal, OpenAI cache code access and IP/licensing, Scaling requirements to ~100k nodes and AKS/Spark fit, Comparison of caching options (C-Store, Alluxio/DAX, BlobFuse/BlockFuse), Bifrost architecture and direct read path, MAI org changes (compute under AKS leadership), Performance snapshot feedback and follow-up conversations
## Recent Context

- 2025-11-06: [[2025-11-06 - Discussion centered on accelerating VAST adoption within Microsoft programs (MAI]] - 1:1 strategy sync focused on accelerating VAST adoption inside Microsoft via MAI and Project Apollo,... (via Kanchan Mehrotra)
- 2025-10-31: [[2025-10-31 - Jason (now at VAST) and Kushal discussed deploying VAST for Apollo’s training wo]] - 1:1 between Jason Vallery (VAST Data) and Kushal Datta (Microsoft Apollo) to evaluate deploying VAST... (via Kushal Datta)
- 2025-09-03: [[2025-09-03 - Jai outlined a high-priority evaluation for an AI caching strategy to support MA]] - Weekly 1:1 where Jai Menon aligned with Jason Vallery on a high-priority evaluation of AI caching st... (via Jai Menon)


- 2025-09-03: [[2025-09-03 - Jai welcomed Jason back and aligned on a forward-looking scope evaluate OpenAI’]] - Weekly 1:1 between Jai Menon and Jason Vallery aligning Jason’s initial scope after returning: evalu... (via Jai Menon)
## Profile

**Role**: CVP at Microsoft (AKS org (Brendan's org))
**Relationship**: Internal stakeholder (compute lead)

**Background**:
- Leading the compute side for MAI support within Brendan's AKS org; referred to as "Qi/"Kiki" Ke".

## Key Decisions

- ✅ Near-term priority is a unified caching approach, with training requirements prioritized first and inference (KB cache) following.
- ✅ Proceed to evaluate OpenAI cache alongside ongoing reviews of Alluxio/DAX, C-Store proposals, and Blockfuse/BlobFuse.
- ✅ Continue Blob performance direction via Bifrost; consider DeltaZero as a subsequent step.
- ✅ Prioritize a storage-hardware path (Azure Storage Hardware / Michael Myrah’s team) over VM-based approaches for VAST performance and scale.
- ✅ Use MAI-driven demand (via Kushal) to advance the Dallas April window for a VAST bare-metal option.
- ✅ Position NVIDIA DGX reference storage compliance as strategic justification in executive conversations.
- ✅ Avoid opening a direct thread with Michael Myrah until Nidhi’s support is secured.

## Related Customers

- [[Microsoft]]

## Related Projects

- [[AI caching strategy for MAI scale]]

## Related




---
*Last updated: *