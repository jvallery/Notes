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

## Contact Information

| Field | Value |
|-------|-------|
| **Role** | CSI/CoSy program/project manager |
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
WHERE !completed AND contains(text, "Rob Gerard")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@RobGerard") AND !completed
SORT due ASC
```

## Key Facts

- Josh Wentzell focuses on automation/DevOps, lab tooling, and customer-facing API automation; previously handled many AWS VOC discussions before Carl joined.
- Multi-tenancy gaps include unclear tenant-scoped APIs, insufficient tenant-admin privileges, and limited tenant visibility (e.g., VIP pool selection/filters).
- VOC deployment lacks a guided wizard and preflight checks; failures can occur late in the process.
- Large customers prefer Terraform/Ansible; Terraform coverage gaps force REST fallbacks, creating state-management pain.
- There is no official Ansible module/collection; Josh built a beta but cannot maintain it; the Do team prioritizes Terraform provider maturity.
- CSI adoption is common; CoSy requests have increased in the last 2–3 months; Rob Gerard owns CSI/CoSy.
- Customers often build internal front-ends for buckets/policies/S3 key rotation to enforce approvals and guardrails.
- Loopback OVA can be spun up via AWX/Cosmodrome in OCI; Josh sent the link.

## Topics Discussed

VAST on Cloud strategy and SaaS multi-tenancy vision, Multi-tenancy API/GUI gaps and tenant-admin permissions, VOC deployment friction and need for preflight/wizard, Terraform provider coverage and state-management issues, Ansible support (beta vs official collection) and resourcing, Customer automation patterns (Terraform/Ansible/REST) and internal portals, CSI vs CoSy adoption and roadmap ownership, Marketplace offers across hyperscalers and price/performance constraints, Multi-cloud data spaces for multi-region durability and data mobility to GPUs, OVA/loopback cluster for hands-on learning

## Recent Context

- 2025-10-31: [[2025-10-31 - Introductory 1-1 focused on VAST on Cloud strategy and current platform gaps. Jo]] - Introductory 1:1 with Josh Wentzell to align on VAST on Cloud strategy and identify platform gaps, e... (via Josh Wentzell)

## Profile

**Role**: CSI/CoSy program/project manager at VAST Data (OCTO team)
**Relationship**: Internal collaborator

**Background**:
- Owns/coordinates CSI driver and CoSy discussions; frequently on customer calls; noted as on paternity leave; should clarify CSI vs CoSy adoption and roadmap.

## Related Projects

- [[Cloud]]

## Related




---
*Last updated: *