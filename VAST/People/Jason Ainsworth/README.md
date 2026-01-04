---
type: people
title: Jason Ainsworth
created: '2026-01-03'
last_contact: '2025-11-07'
auto_created: true
tags:
- type/people
- needs-review
---

# Jason Ainsworth

## Contact Information

| Field | Value |
|-------|-------|
| **Role** | Chief Accounting Officer |
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
WHERE !completed AND contains(text, "Jason Ainsworth")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@JasonAinsworth") AND !completed
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
- John runs alliances/partnerships and is the go-to for AMD/NVIDIA and conventional channel partnerships (non-cloud).
- Sagi leads pipelines/serverless; packaging and cloud GTM for pipelines is under-thought.

## Topics Discussed

GCP Marketplace MVP launch scope (private offers, fixed capacity, no BYOL), Tackle.io integration with Salesforce for private offers, Polaris entitlements, metering, call-home, and Uplink registration automation, Overage policy and GCP marketplace limitations; PAYGO overage workaround, EULA language requirements for overage billing, Finance processes: billing, payout cadence, reconciliation, reporting controls, rev rec, Future pricing model: VAST units of measurement for compute/capacity, Hybrid on-prem/cloud conversion and revenue recognition complexity, Multi-cloud pooling feasibility and hyperscaler positioning concerns, Need for cloud customer success coverage and internal usage alerting, Org map and key leaders/roles, Cross-cloud platform strategy and homogenization across providers, Cloud GTM plays and integrations (Foundry/Bedrock/Vertex), Cataloging in-flight deals by product requirements, Control-plane partnerships and 'cloud-in-a-box' for Tier-2 clouds

## Recent Context

- 2025-11-07: [[2025-11-07 - We reviewed the org landscape and aligned on my near-term focus. Jeff outlined k]] - 1:1 with Jeff Denworth to review the org landscape, clarify key stakeholders, and align on the autho... (via Jeff Denworth)
- 2025-11-07: [[2025-11-07 - We reviewed the org landscape and immediate priorities. Jeff highlighted key pla]] - 1:1 discussion with Jeff Denworth reviewing VAST org landscape, immediate priorities, and a pragmati... (via Jeff Denworth)
- 2025-11-07: [[2025-11-07 - Working session to brute-force warm paths into priority model builders using Lin]] - Working session for the Model Builder Turbine project to map warm introduction paths into priority m... (via Model Builder Turbine)
- 2025-10-28: [[2025-10-28 - Team aligned on MVP launch on GCP via private offers with fixed capacity pricing]] - Internal group meeting to finalize the MVP launch plan for VAST on Google Cloud Marketplace using pr... (via Google)
- 2025-10-28: [[2025-10-28 - Introductory 1-1 covering backgrounds, finance org context, and cloud solutions]] - Introductory 1:1 between Jason Vallery and Timo Pervane focused on finance org context, Cloud Soluti... (via Timo Pervane)
- 2025-10-24: [[2025-10-24 - Jason and Tomer discussed accelerating VAST’s engineering maturity and cloud str]] - Weekly 1:1 between Jason Vallery and Tomer Hagay focused on improving VAST engineering maturity and ... (via Tomer Hagay)

## Profile

**Role**: Meeting organizer at VAST Data (Finance/Accounting)
**Location**: Boston
**Relationship**: Internal collaborator

**Background**:
- Not in note content; appears only in known-entities list and is not referenced in this note's narrative.
- Listed in known entities; not substantively discussed in this note.
- Listed as meeting organizer in known people manifest; not otherwise detailed in note.

## Key Decisions

- ✅ Transact exclusively through cloud marketplaces for MVP (no BYOL).
- ✅ Use Tackle.io to generate and manage private offers integrated with Salesforce.
- ✅ MVP pricing based on fixed capacity at $0.07/GB.
- ✅ Polaris will manage entitlement, call-home registration, and usage reporting.
- ✅ Carl will move to ProServe under Rob rather than supporting customer-facing PM work.
- ✅ Set a monthly touchpoint with Brandon to align on cloud platform priorities.
- ✅ Customer requirement docs and FRDs will be authored and maintained in Confluence.
- ✅ Prioritize building a first-class cross-cloud platform and GTM versus ad hoc deal chasing.
- ✅ Carl will move to ProServe under Rob due to customer-facing risk.
- ✅ Morty will transition to the author’s team while maintaining Neo cloud feature ownership/commitments.

## Related Customers

- [[Google]]

## Related Projects

- [[Pricing]]
- [[Model Builder Turbine]]

## Related




---
*Last updated: *