---
type: customer
title: Intel
created: '2026-01-03'
last_contact: '2025-10-31'
status: active
auto_created: true
tags:
- type/customer
- needs-review
---

# Intel

## Account Overview

_Brief description of this customer, their business, and relationship..._

## Account Status

| Field | Value |
|-------|-------|
| **Status** | _Unknown_ |
| **Industry** | _Unknown_ |

## Key Contacts

_No key contacts identified._

## Active Projects

_What projects/initiatives are active with this customer?_

```dataview
LIST
FROM "VAST/Projects" OR "Personal/Projects"
WHERE contains(file.outlinks, this.file.link)
```


## Current Blockers

_No known blockers._

## Next Steps

_What are the immediate next actions for this account?_


## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed
SORT due ASC
```


## Opportunities

_No active opportunities._

## Key Decisions

- ✅ P0 priority: enable capacity scaling independent of performance via object/S3 offload for cloud viability.
- ✅ Cloud team should spearhead GDC/neo-cloud single-tenant GPU-adjacent storage opportunities, coordinating required integrations.

## Key Facts

- Jason Vallery recently took on cloud product responsibility reporting to Jeff Denworth; vision is a planet-scale multi-tenant/SaaS platform across hyperscalers and neo-clouds.
- Karl Vietmeier is a hands-on Linux/distributed-systems specialist with strong automation skills (bash/PowerShell/Terraform/Ansible; some Python) and uses AI tools heavily for productivity.
- A GDC RFP surfaced via Cisco; success requires integration with Google control plane (APIs, monitoring, billing).
- Edge/extended-zone footprints are large (~60–80 racks) and can fail if parent-region connectivity is lost.
- Without object/S3 offload (capacity/perf decoupling), VAST lacks a viable cloud cost/perf model.

## Topics / Themes

VAST cloud strategy and multi-tenant SaaS vision, Google Distributed Cloud (GDC) RFP via Cisco, Control-plane integrations (API/monitoring/billing), Single-tenant GPU-adjacent storage patterns for neo-clouds, Global namespace portability and avoiding data gravity, Upstream integrations (Spark, Trino, Vertex AI, Bigtable), Object/S3 offload and capacity/performance decoupling, Org planning and potential reporting line for Karl

## Recent Context

- 2025-10-31: [[2025-10-31 - Introductory 1-1 aligning on VAST’s cloud strategy. Jason outlined a vision for]] - Introductory 1:1 between Jason Vallery and Karl Vietmeier aligning on VAST’s cloud strategy, includi... (via Karl Vietmeier)

## Related People

_Internal team members working on this account..._


---
*Last updated: *