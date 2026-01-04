---
type: people
title: Rob Gerard
created: '2026-01-03'
last_contact: '2025-10-31'
auto_created: true
tags:
- type/people
- needs-review
- company/vast-data
---

# Rob Gerard

## Profile

**Role**: CSI/CoSy program/project manager at VAST Data (OCTO team)
**Relationship**: Internal collaborator

**Background**:
- Owns/coordinates CSI driver and CoSy discussions; frequently on customer calls; noted as on paternity leave; should clarify CSI vs CoSy adoption and roadmap.

## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed AND contains(text, "Rob Gerard")
SORT due ASC
```

## Recent Context

- 2025-10-31: [[2025-10-31 - Introductory 1-1 focused on VAST on Cloud strategy and current platform gaps. Jo]] - Introductory 1:1 with Josh Wentzell to align on VAST on Cloud strategy and identify platform gaps, e... (via Josh Wentzell)

## Key Facts

- Josh Wentzell focuses on automation/DevOps, lab tooling, and customer-facing API automation; previously handled many AWS VOC discussions before Carl joined.
- Multi-tenancy gaps include unclear tenant-scoped APIs, insufficient tenant-admin privileges, and limited tenant visibility (e.g., VIP pool selection/filters).
- VOC deployment lacks a guided wizard and preflight checks; failures can occur late in the process.
- Large customers prefer Terraform/Ansible; Terraform coverage gaps force REST fallbacks, creating state-management pain.
- There is no official Ansible module/collection; Josh built a beta but cannot maintain it; the Do team prioritizes Terraform provider maturity.
- CSI adoption is common; CoSy requests have increased in the last 2–3 months; Rob Gerard owns CSI/CoSy.
- Customers often build internal front-ends for buckets/policies/S3 key rotation to enforce approvals and guardrails.
- Loopback OVA can be spun up via AWX/Cosmodrome in OCI; Josh sent the link.

## Background

_Career history, expertise, interests, personal details shared..._

## Related Projects

- [[Cloud]]

## Related

---
*Last updated: *
