---
type: people
title: Soraya Alami
created: '2026-01-03'
last_contact: '2025-11-07'
auto_created: true
tags:
- type/people
- needs-review
- company/vast-data
---

# Soraya Alami

## Contact Information

| Field | Value |
|-------|-------|
| **Role** |  |
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
WHERE !completed AND contains(text, "Soraya Alami")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@SorayaAlami") AND !completed
SORT due ASC
```

## Key Facts

- EY is the near-term priority as a design partner, starting on Azure, with executive alignment planned around Microsoft Ignite.
- VAST has no GA cloud marketplace offer yet; near-term cloud fit is burst-to-cloud and repatriation.
- Work underway on optimized VM shapes and potential bare metal/storage-core integrations to improve cloud economics.
- Accenture is building an opinionated AI/HPC stack that currently includes VAST.
- Deloitte AI Factory lessons: advisory alone is insufficient; need co-developed, productized solutions.
- Referral incentive program is contemplated at ~3% of ACV (licenses only) and is moving through legal.
- Competitive overlap expected with Microsoft AI Foundry; VAST to emphasize data/workflow portability across clouds and on-prem.
- Multiple SIs (TCS, Wipro, Tech Mahindra, Infosys) are reorganizing around AI; sales/build misalignment exists.

## Topics Discussed

SI go-to-market strategy focused on workflow automation, EY Azure-first design partnership and executive alignment at Microsoft Ignite, Cloud roadmap: marketplace GA timing, burst/repatriation scenarios, Optimized VM shapes and potential bare metal/storage-core integrations, Competitive positioning vs Microsoft AI Foundry, Accenture opinionated AI/HPC stack inclusion, Deloitte AI Factory learnings and productized delivery, Partner referral incentive program (~3% ACV), Kyndryl engagement via workshop and incentive-led motion, SI organizational changes around AI (TCS, Wipro, Tech Mahindra, Infosys)

## Recent Context

- 2025-11-07: [[2025-11-07 - The team aligned on a go-to-market strategy with global SIs focused on enterpris]] - GSI Team aligned on a go-to-market strategy with global SIs centered on enterprise workflow automati... (via GSI Team)

## Profile

**Role**: VAST Data (GSI Team)
**Relationship**: Internal collaborator (GSI Team)

**Background**:
- Driving SI coordination and partner engagement planning (EY, Accenture/Avanade, Kyndryl) and internal prep for executive meetings.

## Key Decisions

- ✅ Prioritize EY design partnership on Azure to unlock co-development and a portability-led narrative (reversible).
- ✅ Concentrate SI engagement on workflow automation practices to drive repeatable end-to-end solutions (reversible).
- ✅ Treat Kyndryl as an incentive-driven partner rather than a strategic co-development focus; revisit post-workshop.
- ✅ Advance referral incentive program (~3% ACV, licenses only) to enable pay-for-play partners while protecting margin.

## Related Customers

- [[Microsoft]]

## Related Projects

- [[GSI Team]]

## Related




---
*Last updated: *