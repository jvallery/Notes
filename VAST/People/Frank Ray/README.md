---
type: people
title: Frank Ray
created: '2026-01-03'
last_contact: '2025-09-16'
auto_created: true
tags:
- type/people
- needs-review
- company/microsoft
---

# Frank Ray

## Contact Information

| Field | Value |
|-------|-------|
| **Role** | Likely Azure Networking commercial lead (uncertain) |
| **Company** | Microsoft |
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
WHERE !completed AND contains(text, "Frank Ray")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@FrankRay") AND !completed
SORT due ASC
```

## Key Facts

- Jason Vallery has ~13 years at Microsoft Azure Storage and led major AI storage engagements including OpenAI; recently moved into an architect role after a sabbatical.
- VAST signed Microsoft Lifter and is building a SaaS on Azure; cloud GTM team scaling from 1 to 10–15+.
- Potential org fits discussed: Jai Menon’s model builders GTM, Lior Genzel’s hyperscalers/Azure GTM, or CTO Office.
- Cloud GA plan discussed: GCP (October), AWS MVP (December), Azure GA (February), with an additional Azure Lifter milestone around September next year.
- Network egress is a major risk; ExpressRoute Direct Local proposed as a mitigation to enable fixed-price high-bandwidth data movement.
- Microsoft’s regret with ANF/NetApp-style partnerships cited as a strategic constraint (avoid single-source vendor tie-in and margin sharing).

## Topics Discussed

Jason Vallery background and motivations to leave Microsoft, VAST org placement options (Azure GTM vs model builders vs CTO Office), VAST cloud GTM scaling and hiring plan, Azure marketplace, SaaS strategy, and potential 1P/M&A path, Cloud GA milestones across GCP/AWS/Azure, Egress/networking risk and ExpressRoute Direct Local, Microsoft/OpenAI relationship changes and multi-cloud shift

## Recent Context

- 2025-09-16: [[2025-09-16 - Intro call exploring roles for Jason at VAST. Lior outlined three potential home]] - 1:1 intro call between Lior Genzel and Jason Vallery exploring Jason joining VAST, with discussion o... (via Lior Genzel)

## Profile

**Role**: Likely Azure Networking commercial lead (uncertain) at Microsoft (Azure Networking)
**Relationship**: Potential partner contact at Microsoft

**Background**:
- Suggested as a starting point contact for ExpressRoute Direct Local / networking commercial ownership after org changes.

## Key Decisions

- ✅ Proceed with interviews for Jason at VAST.
- ✅ Focus Jason initially on Azure GTM/business side rather than cross-cloud, with option to expand scope later.

## Related Customers

- [[Microsoft]]

## Related Projects

- [[Cloud]]

## Related




---
*Last updated: *