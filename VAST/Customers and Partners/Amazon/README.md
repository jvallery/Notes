---
type: customer
title: Amazon
created: '2026-01-03'
last_contact: '2025-10-27'
status: active
auto_created: true
tags:
- type/customer
- needs-review
- status/active
---

# Amazon

## Account Overview

_Brief description of this customer, their business, and relationship..._

## Account Status

| Field | Value |
|-------|-------|
| **Status** | Prospect |
| **Industry** | _Unknown_ |

## Key Contacts

- [[Pete Emig]]

## Active Projects

_What projects/initiatives are active with this customer?_

```dataview
LIST
FROM "VAST/Projects" OR "Personal/Projects"
WHERE contains(file.outlinks, this.file.link)
```


## Current Blockers

_No known blockers._

## Next Steps

_What are the immediate next actions for this account?_


## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed
SORT due ASC
```


## Opportunities

- Historical: offered Jason a PM role on S3; used as competitive offer to secure Microsoft match
- Historical: offered Jason a PM role on S3; Microsoft matched via Juergen.

## Key Decisions

- ✅ Proceed with a competitive-offer approach to evaluate a Microsoft retention path.
- ✅ Keep communication open this week and reassess after Jason’s offer arrives.
- ✅ Shared view that Apollo likely requires a clean-sheet storage approach to be competitive.
- ✅ Use Jason’s best external offer as a reference point for potential Microsoft counter and role discussion.
- ✅ Jai to inform Manish that Jason is targeting management roles and needs clear ownership/scope.
- ✅ Pursue a BizDev-led path (Joe Vane/Harish) to secure executive sponsorship (John Tinter) and engage Ronnie Booker’s org, rather than focusing on Nidhi/Manish.
- ✅ Treat the Azure Marketplace VM-based VAST offer as a checkbox while pushing a hardware/OEM storage-dense path for real density wins.

## Key Facts

- Jason has been at Microsoft for 13 years.
- Jason previously received a large Microsoft stock grant after presenting an Amazon offer to Juergen; the 4-year vest completes soon.
- Jason has four external opportunities (two likely, two ruled out), including verbal commitments and an expected strong written offer after a CEO call.
- Jason’s decision timeline target was end of the week; he planned to share his best offer and explicit stay requirements.
- Jason prefers a management/leadership role with clear scope/ownership and latitude to execute; he is not interested in moving to another hyperscaler.
- Apollo storage: concern that datacenter buildouts require near-term storage now, while a clean-sheet stack could take 2–3 years; build vs buy/partner remains open.
- Jason has 13 years at Microsoft.
- Jason previously received an Amazon offer that Juergen matched with a large stock grant; that vesting cycle completes in a few months.
- Jason is pursuing management roles (not IC) and wants clear scope/ownership, collaborators, resourcing, executive backing, and industry-level compensation to stay.
- Jason has four external opportunities; two are likely and include verbal commitments; he expects a strong written offer after speaking with a CEO.

## Topics / Themes

Retention risk and compensation/rewards, External job offers and decision timeline, Role scope/ownership and management vs IC path, Organizational politics and execution speed, Apollo storage strategy (clean-sheet vs existing Azure Storage/Bifrost), Build vs buy/partner for near-term storage, Jason retention risk and external job offers, Compensation/rewards dissatisfaction, Need for management role and clear ownership/scope, Microsoft organizational politics and territorialism, Apollo storage strategy (clean-sheet vs Bifrost-only), Timeline mismatch: near-term datacenter buildouts vs 2–3 year storage stack readiness, Build vs buy vs partner considerations for Apollo storage, Industry instability/layoffs, Azure GTM path for VAST storage (BizDev-led engagement)

## Recent Context

- 2025-10-27: [[2025-10-27 - Jason and Kurt aligned on a go-to-market path to bring VAST’s high-density, lowe]] - Weekly 1:1 where Jason Vallery and Kurt Niebuhr aligned on a Microsoft Azure go-to-market path for V... (via Kurt Niebuhr)
- 2025-09-30: [[2025-09-30 - Jason shared that after meeting with Manish and reviewing rewards, he began expl]] - Weekly 1:1 between Jai Menon and Jason Vallery focused on Jason’s retention risk after disappointing... (via Jai Menon)
- 2025-09-30: [[2025-09-30 - Jason shared that after meeting with Ong and seeing rewards, he began exploring]] - Weekly 1:1 between Jai Menon and Jason Vallery focused on Jason’s intent to pursue external manageme... (via Jai Menon)

## Collaborators

| Person | Role | Company |
|--------|------|---------|
| [[Pete Emig]] |  |  |
| [[Jason Vallery]] | Product management (cloud); partnerships with hyperscale cloud providers | VAST Data |

## Related People

- [[Pete Emig]]
- [[Jason Vallery]]
