---
type: people
title: Manish Sah
created: '2026-01-03'
last_contact: '2025-12-19'
auto_created: true
tags:
- type/people
- needs-review
---

# Manish Sah

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
WHERE !completed AND contains(text, "Manish Sah")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@ManishSah") AND !completed
SORT due ASC
```

## Key Facts

- MAI Falcon plan includes Phoenix, Dallas, and Richmond sites (~40k GPUs per site) connected by an AI WAN; initial tranche includes ~3 EB of Blob.
- MAI struggles to use Falcon capacity due to control plane fragility and GPU issues.
- OpenAI GPT-4.5 training reportedly took ~9 months across multi-islands and up to ~100k H100s; outcome described as disappointing, shifting away from ever-bigger clusters.
- MAI is exploring online RL continuous learning loops with ~60s feedback cycles (trainers in Phoenix, generators elsewhere).
- Vipin values VAST features (global namespace, quotas, capacity estimation, QoS) and acknowledges Blob cannot match VAST performance.
- Marketplace VM offers (Lsv4/v5) are not price-performance competitive for VAST at scale; hardware qualification is viewed as the long-term path.
- Azure Hardware qualification for first-party SKUs is a multi-year effort; liquid-cooled storage SKUs could help with data center cooling fungibility and late-binding storage vs GPU rack decisions.
- Blob API is largely Microsoft-specific; S3 compatibility is broadly attractive; multi-protocol (Blob + S3) could broaden appeal but faces Azure control plane integration hurdles.
- Jason has a VAST offer with complex, highly variable compensation tied to OpenAI/Azure sales plus equity.
- Crusoe offer deadline is Wednesday; VAST has not set a decision deadline.

## Topics Discussed

Microsoft AI (MAI) org landscape and stakeholders, Falcon capacity rollout and AI WAN, MAI control plane fragility and GPU utilization constraints, Project Apollo (AKS-led slim control plane) and storage integration, Azure internal politics (Compute vs Storage incentives), Azure hardware qualification path and timelines, Liquid-cooled storage SKUs and data center cooling fungibility, Blob API vs S3 compatibility and multi-protocol strategy, Using MAI success as a wedge for broader Azure adoption, Job offers comparison (VAST vs Crusoe vs Microsoft), Compensation structure risk (commission/equity variability), Apollo program scope ambiguity and execution risk, Career trajectory and path to partner at Microsoft, Resignation timeline, Retention risk and compensation/rewards

## Recent Context

- 2025-12-19: [[2025-12-19]] - Discussion between Jeff Denworth and Jason Vallery on VAST’s Microsoft/Azure strategy: what level of... (via Jeff Denworth)
- 2025-11-06: [[2025-11-06 - Jason shared VAST’s momentum (CoreWeave $1.2B deal) and updates on Microsoft’s A]] - Weekly 1:1 between Jason Vallery and Kanchan Mehrotra covering Microsoft Project Apollo and MAI Dall... (via Kanchan Mehrotra)
- 2025-11-06: [[2025-11-06 - Discussion centered on accelerating VAST adoption within Microsoft programs (MAI]] - 1:1 strategy sync focused on accelerating VAST adoption inside Microsoft via MAI and Project Apollo,... (via Kanchan Mehrotra)
- 2025-10-31: [[2025-10-31 - Jason (now at VAST) and Kushal discussed deploying VAST for Apollo’s training wo]] - 1:1 between Jason Vallery (VAST Data) and Kushal Datta (Microsoft Apollo) to evaluate deploying VAST... (via Kushal Datta)
- 2025-10-28: [[2025-10-28 - Discussed Microsoft AI (MAI) landscape, Falcon capacity rollout, and Azure dynam]] - Weekly 1:1 between Jason Vallery and Alon Horev aligning on Microsoft AI (MAI) dynamics, Falcon capa... (via Alon Horev)
- 2025-10-28: [[2025-10-28 - Jason and Kanchan aligned to pursue MAI and UK Met Office as flagship wins to un]] - Weekly 1:1 between Jason Vallery (VAST) and Kanchan Mehrotra (Microsoft) aligning on a dual-track pl... (via Kanchan Mehrotra)
- 2025-10-27: [[2025-10-27 - Jason and Kurt aligned on a go-to-market path to bring VAST’s high-density, lowe]] - Weekly 1:1 where Jason Vallery and Kurt Niebuhr aligned on a Microsoft Azure go-to-market path for V... (via Kurt Niebuhr)
- 2025-10-06: [[2025-10-06 - Jason briefed Jai on offers from VAST and Crusoe, noting VAST’s complex, risky c]] - Weekly 1:1 between Jason Vallery and Jai Menon discussing Jason’s competing offers from VAST and Cru... (via Jai Menon)
- 2025-09-30: [[2025-09-30 - Jason shared that after meeting with Manish and reviewing rewards, he began expl]] - Weekly 1:1 between Jai Menon and Jason Vallery focused on Jason’s retention risk after disappointing... (via Jai Menon)
- 2025-09-15: [[2025-09-15 - Catch-up on Jason’s new role and priorities (distributed caching, KBover-index)]] - Weekly 1:1 between Jason Vallery and Vishnu Charan TJ covering Jason’s new role focus (distributed c... (via Vishnu Charan TJ)
- 2025-09-03: [[2025-09-03 - Jai welcomed Jason back and aligned on a forward-looking scope evaluate OpenAI’]] - Weekly 1:1 between Jai Menon and Jason Vallery aligning Jason’s initial scope after returning: evalu... (via Jai Menon)
- 2025-09-03: [[2025-09-03 - Jai outlined a near-term technical focus evaluate OpenAI’s caching code as a ca]] - Weekly 1:1 where Jai Menon aligned with Jason Vallery on a near-term technical focus: evaluate OpenA... (via Jai Menon)
- 2025-09-03: [[2025-09-03 - Jai outlined a high-priority evaluation for an AI caching strategy to support MA]] - Weekly 1:1 where Jai Menon aligned with Jason Vallery on a high-priority evaluation of AI caching st... (via Jai Menon)
- 2025-09-03: [[2025-09-03 - Reconnected post-sabbatical and aligned on Jason’s initial focus evaluate OpenA]] - 1:1 between Jason Vallery and Jai Menon after Jason’s sabbatical to align Jason’s initial focus on e... (via Jai Menon)

## Profile

**Relationship**: Partner/customer stakeholder (Microsoft)

**Background**:
- Mentioned as a Microsoft leader who could request/use OpenAI-derived IP/code; also referenced in a call with Yancey.

## Key Decisions

- ✅ Wait until Friday’s Kushal meeting before Alon follows up with Vipin.
- ✅ Prioritize Project Apollo as the first entry path over Azure marketplace SKUs.
- ✅ Use MAI success as the wedge to influence broader Azure storage strategy and hardware qualification.
- ✅ Treat Blob compatibility as exploratory; near-term emphasis remains on performance to keep GPUs utilized.
- ✅ Do not pursue a Microsoft counteroffer given compensation constraints and unclear scope.
- ✅ Proceed toward a decision between VAST and Crusoe with intent to resign by Wednesday.
- ✅ Proceed with a competitive-offer approach to evaluate a Microsoft retention path.
- ✅ Keep communication open this week and reassess after Jason’s offer arrives.
- ✅ Shared view that Apollo likely requires a clean-sheet storage approach to be competitive.
- ✅ Evaluate OpenAI cache as a first concrete step toward MAI caching strategy.

## Related Customers

- [[Microsoft]]

## Related Projects

- [[VAST on Azure Integration]]

## Related




---
*Last updated: *