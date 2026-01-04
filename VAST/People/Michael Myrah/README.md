---
type: people
title: Michael Myrah
created: '2026-01-03'
last_contact: '2025-11-06'
auto_created: true
tags:
- type/people
- needs-review
- company/microsoft
---

# Michael Myrah

## Profile

**Role**: Partner PM (Azure Storage Hardware) at Microsoft (Azure Storage Hardware (under Long’s team))
**Relationship**: Partner stakeholder at Microsoft (target collaborator)

**Background**:
- Owns Azure Storage hardware stack; potential partner to co-engineer a VAST-optimized Azure storage SKU; Jason knows him well but wants Kanchan/Nidhi-led intro to avoid premature escalation.
- Proposed key partner to co-design a VAST-optimized Azure storage SKU enabling VAST bare metal on Azure storage hardware.

## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed AND contains(text, "Michael Myrah")
SORT due ASC
```

## Recent Context

- 2025-11-06: [[2025-11-06 - Jason shared VAST’s momentum (CoreWeave $1.2B deal) and updates on Microsoft’s A]] - Weekly 1:1 between Jason Vallery and Kanchan Mehrotra covering Microsoft Project Apollo and MAI Dall... (via Kanchan Mehrotra)
- 2025-11-06: [[2025-11-06 - Discussion centered on accelerating VAST adoption within Microsoft programs (MAI]] - 1:1 strategy sync focused on accelerating VAST adoption inside Microsoft via MAI and Project Apollo,... (via Kanchan Mehrotra)
- 2025-10-30: [[2025-10-30 - Reviewed MAI meeting prep and testing path (prefer hardware; VMs supported in De]] - Weekly 1:1 with Lior Genzel focused on preparing for an upcoming MAI call, defining the near-term te... (via Lior Genzel)

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


- MAI contact requested to start testing immediately and prefers functional access now.
- Current support requires pre-certified hardware; VM support expected in December and only for small VMs.
- LSV4 is poor; future VM specs may be strong but are ~1 year out and uncertain versus competitors.
- Non-public Azure Blob HDD/Flash data should not be shared externally (e.g., with third parties).
- Microsoft org incentives are fragmented across storage/compute/networking; politics are sensitive.
- Azure hardware engagement likely requires sponsorship to reach CVP Ronnie Borker.
- Marketplace presence is viewed as important for credibility with some stakeholders.
- OpenAI is described as the top strategic win; reported right of first refusal lifted enabling multi-cloud data plane.
- Jason travel is heavy until mid-December; meeting Jeff in San Francisco next week for guidance.

## Background

Michael Myrah has been with Microsoft since at least 2012, holding various positions including Senior PM Manager for Microsoft Azure, Principal PM Manager for Azure Storage Engineering, and currently serves as the General Manager for Azure Storage Platform Systems and Advanced Technology.

## Key Decisions

- ✅ Jason will not contact Michael Myrah directly to avoid premature escalation; Kanchan will open that thread when appropriate.
- ✅ Primary path is through Azure Storage hardware (Michael Myrah) for a single unified story; Azure Dedicated (Anand) is a parallel option if needed.
- ✅ Prioritize a storage-hardware path (Azure Storage Hardware / Michael Myrah’s team) over VM-based approaches for VAST performance and scale.
- ✅ Use MAI-driven demand (via Kushal) to advance the Dallas April window for a VAST bare-metal option.
- ✅ Position NVIDIA DGX reference storage compliance as strategic justification in executive conversations.
- ✅ Avoid opening a direct thread with Michael Myrah until Nidhi’s support is secured.

## Related Customers

- [[Microsoft]]

## Related Projects

- [[Cloud]]

## Related

---
*Last updated: *
