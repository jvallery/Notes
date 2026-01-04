---
type: people
title: Juergen Willis
created: '2026-01-03'
last_contact: '2025-10-31'
auto_created: true
tags:
- type/people
- needs-review
- company/microsoft
---

# Juergen Willis

## Contact Information

| Field | Value |
|-------|-------|
| **Role** | CVP of Azure Storage (retired) |
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
WHERE !completed AND contains(text, "Juergen Willis")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@JuergenWillis") AND !completed
SORT due ASC
```

## Key Facts

- Jason has been at Microsoft for 13 years.
- Jason previously received a large Microsoft stock grant after presenting an Amazon offer to Juergen; the 4-year vest completes soon.
- Jason has four external opportunities (two likely, two ruled out), including verbal commitments and an expected strong written offer after a CEO call.
- Jason’s decision timeline target was end of the week; he planned to share his best offer and explicit stay requirements.
- Jason prefers a management/leadership role with clear scope/ownership and latitude to execute; he is not interested in moving to another hyperscaler.
- Apollo storage: concern that datacenter buildouts require near-term storage now, while a clean-sheet stack could take 2–3 years; build vs buy/partner remains open.
- Jason Vallery moved from Microsoft Azure Storage to VAST Data to drive hyperscaler penetration and cloud product management.
- Kushal Datta is on Microsoft's Apollo team.
- Dallas HDD capacity is expected to land in January; a larger capacity build is expected in April; Richmond was replaced by a larger capacity site.
- Target per-site scale discussed: ~1 exabyte usable (potentially ~7 exabytes for a 350MW site) and ~120,000 GPUs.

## Topics Discussed

Retention risk and compensation/rewards, External job offers and decision timeline, Role scope/ownership and management vs IC path, Organizational politics and execution speed, Apollo storage strategy (clean-sheet vs existing Azure Storage/Bifrost), Build vs buy/partner for near-term storage, Deploying VAST for Apollo training workloads on Azure, Azure Gen9 XIO bare metal vs Azure Storage software stack benchmarking, VAST ODM hardware options (performance-optimized vs capacity-optimized), Power and rack density constraints at exabyte scale, Read/write throughput requirements for large GPU clusters, NIC/DPU choices and qualification (Fungible vs NVIDIA BlueField), Blob API requirement vs NFS/S3 and impact on data loaders, Azure internal stakeholder alignment and politics, Dallas/Phoenix/Richmond site capacity timelines

## Recent Context

- 2025-10-31: [[2025-10-31 - Jason (now at VAST) and Kushal discussed deploying VAST for Apollo’s training wo]] - 1:1 between Jason Vallery (VAST Data) and Kushal Datta (Microsoft Apollo) to evaluate deploying VAST... (via Kushal Datta)
- 2025-09-30: [[2025-09-30 - Jason shared that after meeting with Manish and reviewing rewards, he began expl]] - Weekly 1:1 between Jai Menon and Jason Vallery focused on Jason’s retention risk after disappointing... (via Jai Menon)
- 2025-09-29: [[2025-09-29 - Jason shared disappointment with his rewards and anxiety about scope and support]] - Weekly 1:1 between Maneesh Sah and Jason Vallery focused on Jason’s dissatisfaction with rewards, re... (via Maneesh Sah)

## Profile

**Role**: CVP of Azure Storage (retired) at Microsoft (Azure Storage)
**Relationship**: Referenced former sponsor

**Background**:
- Jason's former champion/sponsor in Azure Storage; left ~18 months prior, contributing to Jason lacking a champion in the org.

## Key Decisions

- ✅ Proceed with a competitive-offer approach to evaluate a Microsoft retention path.
- ✅ Keep communication open this week and reassess after Jason’s offer arrives.
- ✅ Shared view that Apollo likely requires a clean-sheet storage approach to be competitive.

## Related Customers

- [[Microsoft]]

## Related Projects

- [[Cloud]]

## Related




---
*Last updated: *