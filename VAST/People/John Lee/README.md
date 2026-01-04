---
type: people
title: John Lee
created: '2026-01-03'
last_contact: '2025-11-06'
auto_created: true
tags:
- type/people
- needs-review
- company/microsoft
---

# John Lee

## Contact Information

| Field | Value |
|-------|-------|
| **Role** |  |
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
WHERE !completed AND contains(text, "John Lee")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@JohnLee") AND !completed
SORT due ASC
```

## Key Facts

- VAST signed a ~$1.2B software licensing deal with CoreWeave.
- Apollo leadership requested (1) a VAST POC on VAST hardware shipped to an Azure data center and (2) a POC to run VAST bare metal on Azure Storage hardware.
- Azure Storage hardware spec options include Fungible DPU or NVIDIA BlueField 3; Fungible maturity is a risk with no production storage tenants using it yet.
- MAI is Apollo’s first customer; long-term Apollo vision is multi-tenant, third-party configurable offering.
- MAI Dallas capacity: initial tranche in December and larger tranche in April; April storage plan is still fluid and Kushal is interested in VAST.
- To support MAI Dallas on classic Azure (not Apollo), VAST would need to run bare metal on Azure Storage hardware and interoperate with Overlake/SDN.
- UK Met Office is exploring a POC with VAST hardware in an Azure Canary region.
- NVIDIA DGX Cloud storage requires aggressive per-GPU throughput; VAST and Weka are qualified; Azure Storage currently does not meet these specs.
- DGX Cloud on Azure uses AMLFS for H100/A100; no GB-series storage benchmarking observed by Kanchan.
- Deploying VAST on Lsv4/Lsv5 compute SKUs is power/capex prohibitive at exabyte scale; co-engineered bare metal on Azure Storage hardware is needed.

## Topics Discussed

Project Apollo overview and requests to VAST, VAST POC rack shipment to Azure data center, Running VAST bare metal on Azure Storage hardware, Fungible DPU vs NVIDIA BlueField 3 risk/selection, MAI Dallas capacity (Dec/Apr) and storage plan-of-record uncertainty, Classic Azure interoperability needs (Overlake/SDN), UK Met Office POC in Azure Canary region, NVIDIA DGX Cloud storage performance requirements and leverage vs Azure Storage, Azure internal politics and stakeholder alignment (Manish resistance), Co-engineering a VAST-optimized Azure Storage SKU with Michael Myrah, Exec meeting planning with Nidhi and Renan (around Ignite), Azure Dedicated (Anand) as parallel bare-metal path, Licensing strategy: all-you-can-eat enterprise license, MAI and Project Apollo alignment and timelines, VAST bare metal on Azure storage hardware vs VM-based deployment

## Recent Context

- 2025-11-06: [[2025-11-06 - Jason shared VAST’s momentum (CoreWeave $1.2B deal) and updates on Microsoft’s A]] - Weekly 1:1 between Jason Vallery and Kanchan Mehrotra covering Microsoft Project Apollo and MAI Dall... (via Kanchan Mehrotra)
- 2025-11-06: [[2025-11-06 - Discussion centered on accelerating VAST adoption within Microsoft programs (MAI]] - 1:1 strategy sync focused on accelerating VAST adoption inside Microsoft via MAI and Project Apollo,... (via Kanchan Mehrotra)
- 2025-10-27: [[2025-10-27 - Jason and Kurt aligned on a go-to-market path to bring VAST’s high-density, lowe]] - Weekly 1:1 where Jason Vallery and Kurt Niebuhr aligned on a Microsoft Azure go-to-market path for V... (via Kurt Niebuhr)

## Profile

**Role**: Microsoft
**Relationship**: Partner stakeholder at Microsoft

**Background**:
- Team doing significant work for MAI customer success/technical efforts; Kanchan notes her team is being pulled in to help with technical delivery pieces.
- His team is doing significant work for MAI customer success; Kanchan’s team pulled in for technical delivery support.

## Key Decisions

- ✅ Jason will not contact Michael Myrah directly to avoid premature escalation; Kanchan will open that thread when appropriate.
- ✅ Primary path is through Azure Storage hardware (Michael Myrah) for a single unified story; Azure Dedicated (Anand) is a parallel option if needed.
- ✅ Prioritize a storage-hardware path (Azure Storage Hardware / Michael Myrah’s team) over VM-based approaches for VAST performance and scale.
- ✅ Use MAI-driven demand (via Kushal) to advance the Dallas April window for a VAST bare-metal option.
- ✅ Position NVIDIA DGX reference storage compliance as strategic justification in executive conversations.
- ✅ Avoid opening a direct thread with Michael Myrah until Nidhi’s support is secured.
- ✅ Pursue a BizDev-led path (Joe Vane/Harish) to secure executive sponsorship (John Tinter) and engage Ronnie Booker’s org, rather than focusing on Nidhi/Manish.
- ✅ Treat the Azure Marketplace VM-based VAST offer as a checkbox while pushing a hardware/OEM storage-dense path for real density wins.

## Related Customers

- [[Microsoft]]

## Related Projects

- [[Cloud]]

## Related




---
*Last updated: *