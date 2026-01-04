---
type: people
title: Joe Green
created: '2026-01-03'
last_contact: '2025-10-28'
auto_created: true
tags:
- type/people
- needs-review
- company/microsoft
---

# Joe Green

## Contact Information

| Field | Value |
|-------|-------|
| **Role** | Software Engineer |
| **Company** | Microsoft |
| **Department** | _Unknown_ |
| **Email** | _Unknown_ |
| **Phone** | _Unknown_ |
| **LinkedIn** | _Unknown_ |
| **Location** | San Francisco Bay Area, United States |

## Relationship

_How do you work with this person? What is your dynamic?_

## Background

Previously worked as a Software Development Engineer II at Amazon Web Services (AWS) and as an Enterprise Engineer at Meta.


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
WHERE !completed AND contains(text, "Joe Green")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@JoeGreen") AND !completed
SORT due ASC
```

## Key Facts

- Azure LSV4 is a poor fit for VAST (too many cores, weak networking, low NVMe density) leading to poor cost/perf and sticker shock.
- LSV5 is committed by Egal’s team but roughly a year+ out; networking plans may still be insufficient for UK Met Office economics.
- VAST density advantage cited: ~10x fewer racks (≈240 racks Blob vs ≈20 racks VAST for 1 EB) and ~1/5 power in MAI Falcon-like scenarios.
- MAI (ex-Inflection) has existing VAST affinity; champions include Kushal and Vipin Sachdeva.
- Azure NetApp Files is cited as prior art for a partner-hardware-in-Azure model (OEM/ODM path) that could work for VAST.
- Neo cloud deployments need GPU-adjacent storage for network disconnect resilience; a target ratio of local storage per ~8k GPUs is desired.
- Foundry/OpenAI long-term memory needs a high-TPS key-value store; VAST has an option ('Undivided Attention') vs current RocksDB/FoundationDB usage.
- Marketplace control plane from Yancey’s team was acquired by VAST; rollout sequencing discussed as Google first, Azure to follow.
- GPU supply constraints limit 3P deals; demand remains high.
- Azure LSV4 is the only current option and has poor economics (too many cores, weak networking, low drive density).

## Topics Discussed

MAI as marquee win to drive Azure hardware alignment, UK Met Office opportunity and LSV5 networking economics, Azure LSV4/LSV5 VM shape limitations for VAST, Comparative economics deck (VAST vs Blob; on-prem vs Azure), Azure Marketplace offer progress and limitations, Neo clouds and GPU-adjacent storage for network disconnect resilience, OpenAI/Foundry long-term memory and key-value store needs, Supercomputing and Ignite coordination (booth/panel/keynote slide), 3P GPU capacity constraints and seller enablement, MAI as lighthouse customer to force Azure hardware shape, UK Met Office constraints (price, networking) and Supercomputing meetings, Azure LSV4 vs LSV5 economics and networking limitations, Azure Marketplace listing and control plane integration, Internal stakeholder alignment (Nidhi, Igal, Azure Storage conflict), Neo clouds and GPU-adjacent storage for network-disconnect resilience

## Recent Context

- 2025-10-28: [[2025-10-28 - Jason and Koncha aligned on using MAI and UK Met Office as marquee wins to push]] - Weekly 1:1 between Jason Vallery and Kanchan Mehrotra ("Koncha") aligning on using MAI and UK Met Of... (via Kanchan Mehrotra)
- 2025-10-28: [[2025-10-28 - Jason and Kanchan aligned to pursue MAI and UK Met Office as flagship wins to un]] - Weekly 1:1 between Jason Vallery (VAST) and Kanchan Mehrotra (Microsoft) aligning on a dual-track pl... (via Kanchan Mehrotra)

## Profile

**Role**: Microsoft
**Relationship**: Microsoft collaborator for events/storytelling

**Background**:
- From Koncha's team; previously on Evan's team and owned H-series as PM; organizing Supercomputing activities with Andrew.
- From Kanchan’s team; organizing Supercomputing activities with Andrew; previously on Evan’s team and owned H-series PM role.

## Key Decisions

- ✅ Focus first on MAI and UK Met Office to create executive pull for a VAST-suitable Azure hardware shape.
- ✅ Pursue a dual track: ship marketplace offers while driving a leadership-backed hardware path.
- ✅ Defer broad sales pushes until a credible Azure product/SKU path exists.
- ✅ Near-term focus on MAI and UK Met Office over broad sales motion.
- ✅ Pursue a dual-track: marketplace listing plus flagship customer escalations.
- ✅ Use Nidhi to re-energize internal advocacy once the story and offer are ready.

## Related Customers

- [[Microsoft]]

## Related Projects

- [[Cloud]]

## Related




---
*Last updated: *