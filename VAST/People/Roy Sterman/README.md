---
type: people
title: Roy Sterman
created: '2026-01-03'
last_contact: '2025-11-07'
auto_created: true
tags:
- type/people
- needs-review
- company/vast-data
---

# Roy Sterman

## Profile

**Role**: vForce lead (front-line R&D for CS/customers) at VAST Data (vForce)
**Relationship**: Internal collaborator

**Background**:
- Leads vForce; front R&D arm in front of CS and customers; drives urgent fixes/hotfix needs and backport requests; collaborates with service pack/hotfix management team.
- Drives urgent fixes and requests for hotfixes/service packs; initiates backports from future releases for customers; coordinates with Dafna’s team.

## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed AND contains(text, "Roy Sterman")
SORT due ASC
```

## Recent Context

- 2025-11-07: [[2025-11-07 - Reviewed org landscape and key players; aligned that Jason will deeply understan]] - Weekly 1:1 between Jason Vallery and Jeff Denworth reviewing VAST’s org landscape and key players, a... (via Jeff Denworth)
- 2025-10-29: [[2025-10-29 - Jason and Eyal aligned on how VAST plans and executes majorminor releases, hotf]] - Jason Vallery and Eyal Traitel aligned on VAST’s release planning/execution (major/minor releases, h... (via Eyal Traitel)
- 2025-10-29: [[2025-10-29 - Jason and Eyal discussed VAST’s release intake, planning, and execution model, i]] - 1:1 between Jason Vallery and Eyal Traitel covering VAST’s release intake, planning, and execution m... (via Eyal Traitel)

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

## Background

_Career history, expertise, interests, personal details shared..._

## Key Decisions

- ✅ Carl to move to ProServe under Rob.
- ✅ FRDs and detailed customer requirements will be authored/maintained in Confluence.
- ✅ Jason will own multi-cloud strategy end-to-end and catalog in-flight opportunities from a product requirements lens.
- ✅ Establish a monthly touchpoint between Jason and Brandon.

## Related

---
*Last updated: *
