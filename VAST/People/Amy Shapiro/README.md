---
type: people
title: Amy Shapiro
created: '2026-01-03'
last_contact: '2025-10-28'
auto_created: true
tags:
- type/people
- needs-review
- company/vast-data
---

# Amy Shapiro

## Contact Information

| Field | Value |
|-------|-------|
| **Role** | CFO |
| **Company** | VAST Data |
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
WHERE !completed AND contains(text, "Amy Shapiro")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@AmyShapiro") AND !completed
SORT due ASC
```

## Key Facts

- Timo leads Corporate Finance (FP&A, planning, IR, corp dev) and joined VAST ~11 months ago under CFO Amy Shapiro.
- VAST is ~1100 people and Amy is the first CFO; finance bandwidth/coverage is constrained.
- Boston hub has ~40–45 employees including Marian Budnick (CMO), Jason Ainsworth (CAO), and Joe Stevens (data).
- Investor valuation lens for the next ~3 years is a growth-adjusted ARR multiple.
- Current pricing is primarily $/TB with $/compute added mid-Q2; discount discipline is poor with wide price dispersion.
- Unit-based pricing ('VAST units') is viewed as a way to normalize pricing across cohorts and across storage/compute and on-prem/cloud, while easing migration to a new model.
- Key risks include customer backlash/contraction from inconsistent pricing and deal-level discount leakage when cloud SKUs are undiscountable.

## Topics Discussed

Corporate finance scope and constraints, Hiring a Cloud Solutions finance business partner, Investor valuation metrics (growth-adjusted ARR multiple), Pricing model evolution (unit-based pricing), Discount discipline and controls, Cloud Solutions strategy beyond marketplace VM limits, Exabyte-scale customer targeting to unlock hyperscaler hardware, Common data namespace across on-prem, multi-cloud, and neo-clouds, Founder-driven decision dynamics and change management

## Recent Context

- 2025-10-28: [[2025-10-28 - Introductory 1-1 covering backgrounds, finance org context, and cloud solutions]] - Introductory 1:1 between Jason Vallery and Timo Pervane focused on finance org context, Cloud Soluti... (via Timo Pervane)

## Profile

**Role**: CFO at VAST Data (Finance)
**Relationship**: Executive leadership; finance org leader

**Background**:
- First CFO at VAST; previously CFO at Shopify; long-standing professional relationship with Timo.

## Related Customers

- [[Shopify]]

## Related Projects

- [[Pricing]]
- [[Cloud]]

## Related




---
*Last updated: *