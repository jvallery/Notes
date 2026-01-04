---
type: people
title: John Mill
created: '2026-01-03'
last_contact: '2025-10-31'
auto_created: true
tags:
- type/people
- needs-review
---

# John Mill

## Contact Information

| Field | Value |
|-------|-------|
| **Role** |  |
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
WHERE !completed AND contains(text, "John Mill")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@JohnMill") AND !completed
SORT due ASC
```

## Key Facts

- Jason Vallery moved from Microsoft Azure Storage to VAST Data to drive hyperscaler penetration and cloud product management.
- Kushal Datta is on Microsoft's Apollo team.
- Dallas HDD capacity is expected to land in January; a larger capacity build is expected in April; Richmond was replaced by a larger capacity site.
- Target per-site scale discussed: ~1 exabyte usable (potentially ~7 exabytes for a 350MW site) and ~120,000 GPUs.
- Checkpoint writes are ~100 PB/day; peak write throughput need ~1–2 TB/s; required read throughput ~24 TB/s.
- Azure compute-based storage SKUs (e.g., LSP) are considered inefficient for exabyte storage due to compute:storage ratio and power/rack inefficiency.
- Planned evaluation: apples-to-apples test on Azure Gen9 XIO hardware comparing Azure Storage stack vs VAST bare metal.
- VAST can ship VAST-qualified ODM hardware in ~30 days after order once requirements are set (subject to facility/organizational approval).
- VAST supports NFS, GPU Direct Storage, S3 API; Blob API is being considered/possible if required.
- Azure Gen9 XIO uses CX5 NICs (~40Gbps) which may be a throughput bottleneck; BlueField-3 supported and BlueField-4 in progress; Fungible NIC could be qualified if required.

## Topics Discussed

Deploying VAST for Apollo training workloads on Azure, Azure Gen9 XIO bare metal vs Azure Storage software stack benchmarking, VAST ODM hardware options (performance-optimized vs capacity-optimized), Power and rack density constraints at exabyte scale, Read/write throughput requirements for large GPU clusters, NIC/DPU choices and qualification (Fungible vs NVIDIA BlueField), Blob API requirement vs NFS/S3 and impact on data loaders, Azure internal stakeholder alignment and politics, Dallas/Phoenix/Richmond site capacity timelines

## Recent Context

- 2025-10-31: [[2025-10-31 - Jason (now at VAST) and Kushal discussed deploying VAST for Apollo’s training wo]] - 1:1 between Jason Vallery (VAST Data) and Kushal Datta (Microsoft Apollo) to evaluate deploying VAST... (via Kushal Datta)

## Profile

**Relationship**: Referenced contact

**Background**:
- Mentioned as someone Kushal runs into at conferences; Jason asks Kushal to say hi to him.

## Related Projects

- [[Cloud]]

## Related




---
*Last updated: *