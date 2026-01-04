---
type: customer
title: Tesla
created: '2026-01-03'
last_contact: '2025-10-29'
status: active
auto_created: true
tags:
- type/customer
- needs-review
- industry/automotive-/-technology
- status/active
---

# Tesla

## Account Status

| Field | Value |
|-------|-------|
| **Status** | Active |
| **Industry** | Automotive / Technology |

## Key Contacts

_No key contacts identified._

## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed
SORT due ASC
```

## Recent Context

- 2025-10-29: [[2025-10-29 - Jason and Eyal aligned on how VAST plans and executes majorminor releases, hotf]] - Jason Vallery and Eyal Traitel aligned on VAST’s release planning/execution (major/minor releases, h... (via Eyal Traitel)

## Key Facts

- Eyal Traitel joined VAST in Dec 2024; Noa Cohen is a long-tenured VAST employee focusing on major releases while Eyal focuses on minor releases.
- Feature intake channels include leadership/architects, and SE requests filed in Salesforce tied to opportunities and triaged by Tomer Hagay’s team with bi-weekly reviews.
- Release managers run day-to-day execution for major and minor releases; Shelly Martin (Ops) and Liraz Ben Or (R&D) drive phase-gate documentation/process.
- vForce (Roy Sterman) and Dafna’s team manage service packs and hotfixes, including back/forward-porting and ensuring fixes go upstream to minors/majors.
- Minor releases are treated like full releases with regression and performance testing; weekly content/testing reviews.
- Planning is highly dynamic due to frequent urgent customer/field requests (example: Tesla), causing scope churn and parallel streams.
- 5.6 phase gates are underway with target GA in July next year.
- Historical cadence is roughly 2–3 major releases per year.
- Major multi-tenancy blocker: authentication providers limited to 8 and configured at host cluster rather than tenant-scoped; scaling and tenantizing is a large effort.
- Control plane (Polaris/Iceland) is more cloud-native; cluster layer is not yet operating in an agile/SaaS mode.

## Opportunities

- Ongoing relationship; urgent incremental requests after trials drive additional development and QA work, impacting release scope.
