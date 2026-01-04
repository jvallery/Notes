---
type: people
title: John Tinter
created: '2026-01-03'
last_contact: '2025-10-31'
auto_created: true
tags:
- type/people
- needs-review
---

# John Tinter

## Profile

**Role**: Executive sponsor (needed for access to Ronnie org) at Microsoft
**Relationship**: Known person (not discussed)

**Background**:
- Mentioned only in manifest context (intros to Ronnie); not discussed in note content.
- Referenced in note metadata as a path for intros to Ronnie (not otherwise discussed in this note).
- Mentioned as a path for introductions to Ronnie (context referenced in known project manifest).

## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed AND contains(text, "John Tinter")
SORT due ASC
```

## Recent Context

- 2025-10-31: [[2025-10-31 - Jason (now at VAST) and Kushal discussed deploying VAST for Apollo’s training wo]] - 1:1 between Jason Vallery (VAST Data) and Kushal Datta (Microsoft Apollo) to evaluate deploying VAST... (via Kushal Datta)
- 2025-10-31: [[2025-10-31 - Intro discussion covering VAST-in-cloud strategy, field enablement gaps, and SE]] - Weekly 1:1 between Jason Vallery and Rob Benoit to align on VAST’s cloud strategy, marketplace packa... (via Rob Banga)
- 2025-10-29: [[2025-10-29 - Jason introduced his cloud-first vision for VAST (VAST-as-a-Service, multi-cloud]] - 1:1 between Jason Vallery and Rick Haselton covering Jason’s cloud-first VAST-as-a-Service vision an... (via Rick Haselton)
- 2025-10-28: [[2025-10-28 - Jason and Koncha aligned on using MAI and UK Met Office as marquee wins to push]] - Weekly 1:1 between Jason Vallery and Kanchan Mehrotra ("Koncha") aligning on using MAI and UK Met Of... (via Kanchan Mehrotra)
- 2025-10-27: [[2025-10-27 - Jason and Kurt aligned on a go-to-market path to bring VAST’s high-density, lowe]] - Weekly 1:1 where Jason Vallery and Kurt Niebuhr aligned on a Microsoft Azure go-to-market path for V... (via Kurt Niebuhr)

## Key Facts

- Azure LSV4 is a poor fit for VAST (too many cores, weak networking, low NVMe density) leading to poor cost/perf and sticker shock.
- LSV5 is committed by Egal’s team but roughly a year+ out; networking plans may still be insufficient for UK Met Office economics.
- VAST density advantage cited: ~10x fewer racks (≈240 racks Blob vs ≈20 racks VAST for 1 EB) and ~1/5 power in MAI Falcon-like scenarios.
- MAI (ex-Inflection) has existing VAST affinity; champions include Kushal and Vipin Sachdeva.
- Azure NetApp Files is cited as prior art for a partner-hardware-in-Azure model (OEM/ODM path) that could work for VAST.
- Neo cloud deployments need GPU-adjacent storage for network disconnect resilience; a target ratio of local storage per ~8k GPUs is desired.
- Foundry/OpenAI long-term memory needs a high-TPS key-value store; VAST has an option ('Undivided Attention') vs current RocksDB/FoundationDB usage.
- Marketplace control plane from Yancey’s team was acquired by VAST; rollout sequencing discussed as Google first, Azure to follow.
- Kurt is global pre-sales lead for AI Infra under Zia; his team scores constrained GPU allocations and must approve any allocation of constrained SKUs.
- Kurt’s proposal: GA Azure Extended Zones as network-only plus AKS NodeJoin (ACAS FlexNode) to connect neo/sovereign cloud training sites to Azure for global inference.

## Background

_Career history, expertise, interests, personal details shared..._

## Key Decisions

- ✅ Focus first on MAI and UK Met Office to create executive pull for a VAST-suitable Azure hardware shape.
- ✅ Pursue a dual track: ship marketplace offers while driving a leadership-backed hardware path.
- ✅ Defer broad sales pushes until a credible Azure product/SKU path exists.
- ✅ Pursue a BizDev-led path (Joe Vane/Harish) to secure executive sponsorship (John Tinter) and engage Ronnie Booker’s org, rather than focusing on Nidhi/Manish.
- ✅ Treat the Azure Marketplace VM-based VAST offer as a checkbox while pushing a hardware/OEM storage-dense path for real density wins.
- ✅ Meet at Tech Summit for follow-up conversation

## Related Customers

- [[Microsoft]]

## Related Projects

- [[Microsoft BizDev Education & Intros to Ronnie]]
- [[Cloud]]

## Related

---
*Last updated: *
