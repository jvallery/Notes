---
type: people
title: Mike Kiernan
created: '2026-01-03'
last_contact: '2025-11-06'
auto_created: true
tags:
- type/people
- needs-review
- company/microsoft
---

# Mike Kiernan

## Profile

**Role**: Microsoft
**Relationship**: Partner stakeholder at Microsoft

**Background**:
- Involved in UK Met Office POC discussions; plan mentioned to deploy VAST hardware into an Azure Canary region for independent POC.
- Contact driving UK Met Office POC interest in an Azure Canary region (separate from Apollo).
- UK Met Office stakeholder; expected at Supercomputing; has a key storage person (Nico) on his team.

## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed AND contains(text, "Mike Kiernan")
SORT due ASC
```

## Recent Context

- 2025-11-06: [[2025-11-06 - Jason shared VAST’s momentum (CoreWeave $1.2B deal) and updates on Microsoft’s A]] - Weekly 1:1 between Jason Vallery and Kanchan Mehrotra covering Microsoft Project Apollo and MAI Dall... (via Kanchan Mehrotra)
- 2025-11-06: [[2025-11-06 - Discussion centered on accelerating VAST adoption within Microsoft programs (MAI]] - 1:1 strategy sync focused on accelerating VAST adoption inside Microsoft via MAI and Project Apollo,... (via Kanchan Mehrotra)
- 2025-10-28: [[2025-10-28 - Jason and Koncha aligned on using MAI and UK Met Office as marquee wins to push]] - Weekly 1:1 between Jason Vallery and Kanchan Mehrotra ("Koncha") aligning on using MAI and UK Met Of... (via Kanchan Mehrotra)
- 2025-10-28: [[2025-10-28 - Jason and Kanchan aligned to pursue MAI and UK Met Office as flagship wins to un]] - Weekly 1:1 between Jason Vallery (VAST) and Kanchan Mehrotra (Microsoft) aligning on a dual-track pl... (via Kanchan Mehrotra)

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

## Background

_Career history, expertise, interests, personal details shared..._

## Key Decisions

- ✅ Jason will not contact Michael Myrah directly to avoid premature escalation; Kanchan will open that thread when appropriate.
- ✅ Primary path is through Azure Storage hardware (Michael Myrah) for a single unified story; Azure Dedicated (Anand) is a parallel option if needed.
- ✅ Prioritize a storage-hardware path (Azure Storage Hardware / Michael Myrah’s team) over VM-based approaches for VAST performance and scale.
- ✅ Use MAI-driven demand (via Kushal) to advance the Dallas April window for a VAST bare-metal option.
- ✅ Position NVIDIA DGX reference storage compliance as strategic justification in executive conversations.
- ✅ Avoid opening a direct thread with Michael Myrah until Nidhi’s support is secured.
- ✅ Focus first on MAI and UK Met Office to create executive pull for a VAST-suitable Azure hardware shape.
- ✅ Pursue a dual track: ship marketplace offers while driving a leadership-backed hardware path.
- ✅ Defer broad sales pushes until a credible Azure product/SKU path exists.
- ✅ Near-term focus on MAI and UK Met Office over broad sales motion.

## Related Customers

- [[Microsoft]]

## Related Projects

- [[VAST on Azure Integration]]
- [[Cloud]]

## Related

---
*Last updated: *
