---
type: customer
title: Avanade
created: '2026-01-03'
last_contact: '2025-10-28'
status: active
auto_created: true
tags:
- type/customer
- needs-review
- status/active
---

# Avanade

## Account Overview

_Brief description of this customer, their business, and relationship..._

## Account Status

| Field | Value |
|-------|-------|
| **Status** | Partner |
| **Industry** | Professional services, Technology services |

## Key Contacts

- [[Jason Vallery]]

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

_No active opportunities._

## Key Decisions

_Important decisions made with this customer..._


## Key Facts

- Timo leads Corporate Finance (FP&A, planning, IR, corp dev) and joined VAST ~11 months ago under CFO Amy Shapiro.
- VAST is ~1100 people and Amy is the first CFO; finance bandwidth/coverage is constrained.
- Boston hub has ~40–45 employees including Marian Budnick (CMO), Jason Ainsworth (CAO), and Joe Stevens (data).
- Investor valuation lens for the next ~3 years is a growth-adjusted ARR multiple.
- Current pricing is primarily $/TB with $/compute added mid-Q2; discount discipline is poor with wide price dispersion.
- Unit-based pricing ('VAST units') is viewed as a way to normalize pricing across cohorts and across storage/compute and on-prem/cloud, while easing migration to a new model.
- Key risks include customer backlash/contraction from inconsistent pricing and deal-level discount leakage when cloud SKUs are undiscountable.

## Topics / Themes

Corporate finance scope and constraints, Hiring a Cloud Solutions finance business partner, Investor valuation metrics (growth-adjusted ARR multiple), Pricing model evolution (unit-based pricing), Discount discipline and controls, Cloud Solutions strategy beyond marketplace VM limits, Exabyte-scale customer targeting to unlock hyperscaler hardware, Common data namespace across on-prem, multi-cloud, and neo-clouds, Founder-driven decision dynamics and change management

## Recent Context

- 2025-10-28: [[2025-10-28 - Introductory 1-1 covering backgrounds, finance org context, and cloud solutions]] - Introductory 1:1 between Jason Vallery and Timo Pervane focused on finance org context, Cloud Soluti... (via Timo Pervane)

## Collaborators

| Person | Role | Company |
|--------|------|---------|
| [[Jason Vallery]] | Cloud partnerships / Cloud Solutions leader (new in role) | VAST Data |

## Related People

- [[Jason Vallery]]
