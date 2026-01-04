---
type: people
title: Shelly Martin
created: '2026-01-03'
last_contact: '2025-10-29'
auto_created: true
tags:
- type/people
- needs-review
- company/vast-data
---

# Shelly Martin

## Contact Information

| Field | Value |
|-------|-------|
| **Role** | Ops (phase-gate process/operations for releases) |
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
WHERE !completed AND contains(text, "Shelly Martin")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@ShellyMartin") AND !completed
SORT due ASC
```

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

## Topics Discussed

Release planning and execution (major/minor releases), Hotfixes and service packs (backport/forward-port, upgrade alignment), Feature intake and triage process (Salesforce tied to opportunities), Phase-gate process and documentation, QA/regression/performance testing for minor releases, SaaS and multi-tenant readiness, Multi-tenancy gaps (auth providers limit, tenant-scoped auth), Control plane vs cluster responsibilities (Polaris/Iceland vs cluster), Impact of urgent customer requests on scope and resourcing, 5.6 timeline and GA target, Release intake and prioritization (leadership, architects, SE/Salesforce), Major vs minor releases and phase-gate process, Service packs and hotfix process (vForce, upstreaming fixes), Regression/performance testing practices for minors, SaaS agility vs storage reliability constraints

## Recent Context

- 2025-10-29: [[2025-10-29 - Jason and Eyal aligned on how VAST plans and executes majorminor releases, hotf]] - Jason Vallery and Eyal Traitel aligned on VAST’s release planning/execution (major/minor releases, h... (via Eyal Traitel)
- 2025-10-29: [[2025-10-29 - Jason and Eyal discussed VAST’s release intake, planning, and execution model, i]] - 1:1 between Jason Vallery and Eyal Traitel covering VAST’s release intake, planning, and execution m... (via Eyal Traitel)

## Profile

**Role**: Ops (phase-gate process/operations for releases) at VAST Data (Operations)
**Relationship**: Internal collaborator

**Background**:
- Ops lead helping drive and document the release phase-gate process and commitments for releases.
- Leads (with Liraz) the operational process to organize and document release commitments and phase gates.

## Related




---
*Last updated: *