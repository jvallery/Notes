---
type: people
title: Cliff Henson
created: '2026-01-03'
last_contact: '2025-10-30'
auto_created: true
tags:
- type/people
- needs-review
- company/microsoft
---

# Cliff Henson

## Contact Information

| Field | Value |
|-------|-------|
| **Role** | Corporate Vice President, Cloud Supply Chain |
| **Company** | Microsoft |
| **Department** | _Unknown_ |
| **Email** | _Unknown_ |
| **Phone** | _Unknown_ |
| **LinkedIn** | [https://www.linkedin.com/in/cliff-henson-8b906025](https://www.linkedin.com/in/cliff-henson-8b906025) |
| **Location** | Austin, Texas Metropolitan Area, United States |

## Relationship

_How do you work with this person? What is your dynamic?_

## Background

Cliff Henson has over 24 years of experience in supply chain management. Prior to joining Microsoft in February 2020, he held various leadership roles at Hewlett Packard Enterprise, including Senior Vice President of Global Supply Chain. He holds a BSME from Texas Tech University and an MBA from the University of St. Thomas (TX).


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
WHERE !completed AND contains(text, "Cliff Henson")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@CliffHenson") AND !completed
SORT due ASC
```

## Key Facts

- MAI contact requested to start testing immediately and prefers functional access now.
- Current support requires pre-certified hardware; VM support expected in December and only for small VMs.
- LSV4 is poor; future VM specs may be strong but are ~1 year out and uncertain versus competitors.
- Non-public Azure Blob HDD/Flash data should not be shared externally (e.g., with third parties).
- Microsoft org incentives are fragmented across storage/compute/networking; politics are sensitive.
- Azure hardware engagement likely requires sponsorship to reach CVP Ronnie Borker.
- Marketplace presence is viewed as important for credibility with some stakeholders.
- OpenAI is described as the top strategic win; reported right of first refusal lifted enabling multi-cloud data plane.
- Jason travel is heavy until mid-December; meeting Jeff in San Francisco next week for guidance.

## Topics Discussed

MAI meeting preparation and testing plan, Hardware vs VM support timeline, External sharing constraints for Azure Blob data, Deck improvements: observability and CSI driver, Microsoft internal politics and stakeholder management, Engaging Azure hardware leadership via sponsorship, Two-track cloud strategy: marketplace SaaS + first-party hardware wins, CSP prioritization: Azure primary, OCI secondary, AWS deprioritized, GCP program review and GKE-native integration approach, Resourcing/team structure and potential addition of Karl

## Recent Context

- 2025-10-30: [[2025-10-30 - Reviewed MAI meeting prep and testing path (prefer hardware; VMs supported in De]] - Weekly 1:1 with Lior Genzel focused on preparing for an upcoming MAI call, defining the near-term te... (via Lior Genzel)

## Profile

**Role**: Runs CSCP (Azure capacity supply chain / logistics partner org) at Microsoft (CSCP)
**Relationship**: Microsoft infrastructure leader (context)

**Background**:
- One of three CVPs (with Ronnie Borker and Paul Clark) responsible for building/delivering Azure infrastructure capacity.

## Key Decisions

- ✅ Do not include non-public Azure BLOB performance data in externally shared decks.
- ✅ Emphasize observability (single pane of glass) and CSI driver in the MAI deck.
- ✅ Pursue parallel strategy: marketplace SaaS maturity and first-party hardware-optimized wins.
- ✅ Near-term focus: Azure first-party opportunities (MAI, UK Met); OCI as secondary; AWS deprioritized for SC.

## Related Customers

- [[Microsoft]]

## Related Projects

- [[Cloud]]

## Related




---
*Last updated: *