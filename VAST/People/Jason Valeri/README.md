---
type: people
title: Jason Valeri
created: '2026-01-03'
last_contact: '2025-11-07'
auto_created: true
tags:
- type/people
- needs-review
---

# Jason Valeri

## Contact Information

| Field | Value |
|-------|-------|
| **Role** | Finance |
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
WHERE !completed AND contains(text, "Jason Valeri")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@JasonValeri") AND !completed
SORT due ASC
```

## Key Facts

- MVP launch on GCP uses private offers with fixed capacity pricing ($0.07/GB) via GCP Marketplace.
- Tackle.io is the middleware to generate private offers and sync them with Salesforce opportunities.
- Polaris is the source of truth for entitlements and metering; clusters call home to Polaris and enforce entitlements via tokens (no license keys).
- No BYOL for MVP; all transactions go through marketplaces to support hyperscaler partner status and MDF/marketing benefits.
- Considering ~10% overage allowance; goal is to charge overage at list PAYGO, but GCP Marketplace may not support this natively.
- Internal CS/sales alerting for entitlement usage/overage is not yet in place; customer alert exists.
- First GCP transactions targeted for Nov–Dec 2025; plan to replicate approach to AWS/Azure afterward.
- Finance will not have a separate cloud P&L; cloud metrics will be reported within overall P&L; SaaS/consumption metrics and forecasting model must be defined before full SaaS launch.
- Customer Success is currently reactive support rather than proactive CS.
- PM team is small relative to product scope; professionalizing PM is a major initiative for the coming year.

## Topics Discussed

GCP Marketplace MVP launch scope (private offers, fixed capacity, no BYOL), Tackle.io integration with Salesforce for private offers, Polaris entitlements, metering, call-home, and Uplink registration automation, Overage policy and GCP marketplace limitations; PAYGO overage workaround, EULA language requirements for overage billing, Finance processes: billing, payout cadence, reconciliation, reporting controls, rev rec, Future pricing model: VAST units of measurement for compute/capacity, Hybrid on-prem/cloud conversion and revenue recognition complexity, Multi-cloud pooling feasibility and hyperscaler positioning concerns, Need for cloud customer success coverage and internal usage alerting, Org landscape and key players, Cloud strategy beyond S3, Embedding with SEs and customer workflow discovery, Google RFP and TPU angle; fit assessment, Microsoft positioning vs Azure Storage gaps

## Recent Context

- 2025-11-07: [[2025-11-07 - We reviewed the org landscape and immediate priorities. Jeff highlighted key pla]] - 1:1 discussion with Jeff Denworth reviewing VAST org landscape, immediate priorities, and a pragmati... (via Jeff Denworth)
- 2025-10-28: [[2025-10-28 - Team aligned on MVP launch on GCP via private offers with fixed capacity pricing]] - Internal group meeting to finalize the MVP launch plan for VAST on Google Cloud Marketplace using pr... (via Google)

## Profile

**Role**: Finance (Finance)
**Relationship**: Internal finance partner

**Background**:
- Mentioned indirectly as 'T-Mose' / finance strategy discussions; finance wants to run strategy people out of finance.
- Finance lead embedded into Tackle implementation; validating overage-at-PAYGO approach and helping define billing/reconciliation/rev rec processes for marketplace transactions.

## Key Decisions

- ✅ Transact exclusively through cloud marketplaces for MVP (no BYOL).
- ✅ Use Tackle.io to generate and manage private offers integrated with Salesforce.
- ✅ MVP pricing based on fixed capacity at $0.07/GB.
- ✅ Polaris will manage entitlement, call-home registration, and usage reporting.
- ✅ Carl will move to ProServe under Rob due to customer-facing risk.
- ✅ Morty will transition to the author’s team while maintaining Neo cloud feature ownership/commitments.
- ✅ The author owns defining cross-cloud product strategy and prioritization.
- ✅ Customer requirements and FRDs will be authored and maintained in Confluence (coordinated with A.L. and Tomer).

## Related Customers

- [[Google]]

## Related Projects

- [[Cloud]]

## Related




---
*Last updated: *