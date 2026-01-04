---
type: people
title: Greg Brockman
created: '2026-01-03'
last_contact: unknown
auto_created: true
tags:
- type/people
- needs-review
- company/openai
---

# Greg Brockman

## Profile

**Role**: OpenAI
**Relationship**: Customer executive stakeholder (indirect)

**Background**:
- Referenced as an executive in the reporting chain above Uday (not fully identified in note).
- Uday reports to him at OpenAI.

## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed AND contains(text, "Greg Brockman")
SORT due ASC
```

## Recent Context

- 2025-10-27: [[2025-10-27 - Jason and Kurt aligned on a go-to-market path to bring VAST’s high-density, lowe]] - Weekly 1:1 where Jason Vallery and Kurt Niebuhr aligned on a Microsoft Azure go-to-market path for V... (via Kurt Niebuhr)
- unknown: [[Oct 22nd, 2025]] - Stakeholder mapping and technical positioning for an OpenAI research primary storage proof-of-concep... (via Sam Hopewell)

## Key Facts

- Kurt is global pre-sales lead for AI Infra under Zia; his team scores constrained GPU allocations and must approve any allocation of constrained SKUs.
- Kurt’s proposal: GA Azure Extended Zones as network-only plus AKS NodeJoin (ACAS FlexNode) to connect neo/sovereign cloud training sites to Azure for global inference.
- VAST vs Azure Blob per 1 EB: ~1/10 racks, ~1/5 megawatts, >=5x performance, but ~2x capex.
- Azure Marketplace VAST offer on L-series VMs is not density/cost competitive for real workloads; positioned as a checkbox.
- Apollo ownership boundaries: Chi owns bare-metal control plane; Sky/Overlake owns security; Ronnie Booker’s org owns chassis/layout/storage placement decisions.
- Azure MAI/Falcon issues include lack of topology-aware scheduling; rack-level placement not expected until ~Feb; IB/telemetry improving.
- OpenAI infra leadership changed: Uday (ex-xAI) now runs infra at OpenAI and reports to Greg Brockman; may reduce Microsoft alignment; power is a major Azure constraint.
- Kurt expected A2N approval for Extended Zones/NodeJoin in ~3 weeks; target partners include sovereign/neo-clouds such as sakura.net in Japan.
- OpenAI tiering vocabulary: Azure Blob = cold; VAST = warm (near GPUs, efficient/high-throughput for staging large working sets); on-GPU/local = hot/ultra.
- POC goal: make more clusters research-worthy despite poor/transient WAN by staging checkpoints/training sets locally and serving some reads from VAST when GPU caching isn’t required.

## Background

Co-founder and President of OpenAI; former CTO at Stripe; led projects like OpenAI Gym and OpenAI Five.

## Key Decisions

- ✅ Pursue a BizDev-led path (Joe Vane/Harish) to secure executive sponsorship (John Tinter) and engage Ronnie Booker’s org, rather than focusing on Nidhi/Manish.
- ✅ Treat the Azure Marketplace VM-based VAST offer as a checkbox while pushing a hardware/OEM storage-dense path for real density wins.
- ✅ Near-term approach should focus on per-cluster islands plus object API rather than pushing a third-party global namespace into OpenAI’s stack.

## Related Customers

- [[OpenAI]]

## Related

---
*Last updated: *
