---
type: people
title: Olivia Kim
created: '2026-01-03'
last_contact: '2025-11-07'
auto_created: true
tags:
- type/people
- needs-review
- company/google
---

# Olivia Kim

## Contact Information

| Field | Value |
|-------|-------|
| **Role** |  |
| **Company** | Google |
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
WHERE !completed AND contains(text, "Olivia Kim")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@OliviaKim") AND !completed
SORT due ASC
```

## Key Facts

- John owns alliances/partnerships for conventional channels (incl. AMD/NVIDIA) and control-plane partner ecosystem for Tier-2 cloud-in-a-box.
- Morty owns Neo cloud feature requirements; moving to Jason’s team but must keep Neo focus.
- Customer Success under Rob is effectively reactive support, not proactive CS.
- SE org is critical to Jason’s success; Hari called out as a top SE.
- China posture agreed: software-only sales outpost; avoid CAPEX/headcount build-out.
- Need a crisp, quantified Azure Storage gaps narrative ('dagger' slide) and a repeatable measurement rubric across clouds.
- Win/loss analysis should be routine and tied to Sales Ops; cloud is a platform, product gaps apply across deployment environments.
- Confluence is the engineering-respected source of truth for FRDs/requirements; coordinate taxonomy with Alon (A.L.) and Tomer.

## Topics Discussed

Org chart and key leaders across marketing, alliances, SE, sales, finance, Multi-cloud strategy mandate (Azure/AWS/GCP/Oracle) and complement vs compete framing, Cloud packaging and serverless/pipelines gaps, Neo cloud requirements ownership and team transition, Customer Success vs support operating model, SE engagement strategy and Tech Summit embedding, China go-to-market posture (software-only), Azure Storage limitations and messaging for Microsoft, Google RFP triage and no-bid criteria for block/latency-heavy asks, Confluence as FRD system of record and documentation taxonomy, Win/loss cadence and product MBR rhythm

## Recent Context

- 2025-11-07: [[2025-11-07 - Reviewed org landscape and key players; aligned that Jason will deeply understan]] - Weekly 1:1 between Jason Vallery and Jeff Denworth reviewing VAST’s org landscape and key players, a... (via Jeff Denworth)

## Profile

**Role**: Google
**Relationship**: Partner contact (Google)

**Background**:
- Mentioned as 'from Google'; associated with Lior’s org context.

## Key Decisions

- ✅ Carl to move to ProServe under Rob.
- ✅ FRDs and detailed customer requirements will be authored/maintained in Confluence.
- ✅ Jason will own multi-cloud strategy end-to-end and catalog in-flight opportunities from a product requirements lens.
- ✅ Establish a monthly touchpoint between Jason and Brandon.

## Related Customers

- [[Google]]

## Related Projects

- [[Google RFP]]

## Related




---
*Last updated: *