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

## Profile

**Role**: Microsoft
**Relationship**: Microsoft collaborator for events/storytelling

**Background**:
- From Koncha's team; previously on Evan's team and owned H-series as PM; organizing Supercomputing activities with Andrew.
- From Kanchan’s team; organizing Supercomputing activities with Andrew; previously on Evan’s team and owned H-series PM role.

## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed AND contains(text, "Joe Green")
SORT due ASC
```

## Recent Context

- 2025-10-28: [[2025-10-28 - Jason and Koncha aligned on using MAI and UK Met Office as marquee wins to push]] - Weekly 1:1 between Jason Vallery and Kanchan Mehrotra ("Koncha") aligning on using MAI and UK Met Of... (via Kanchan Mehrotra)
- 2025-10-28: [[2025-10-28 - Jason and Kanchan aligned to pursue MAI and UK Met Office as flagship wins to un]] - Weekly 1:1 between Jason Vallery (VAST) and Kanchan Mehrotra (Microsoft) aligning on a dual-track pl... (via Kanchan Mehrotra)

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

## Background

Previously worked as a Software Development Engineer II at Amazon Web Services (AWS) and as an Enterprise Engineer at Meta.

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
