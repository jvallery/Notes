---
type: customer
title: Zoom
created: '2026-01-03'
last_contact: '2025-10-27'
status: active
auto_created: true
tags:
- type/customer
- needs-review
- status/active
---

# Zoom

## Account Overview

_Brief description of this customer, their business, and relationship..._

## Account Status

| Field | Value |
|-------|-------|
| **Status** | Prospect |
| **Industry** | Information Technology Software & Services |

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

- Zoom on OCI mentioned as a strong opportunity; cloud-only deal dynamics discussed

## Key Decisions

- ✅ Use capacity-only pricing for cloud private offers until 2025-02-01.
- ✅ Do not disable or rate-limit vCPUs in cloud instances.
- ✅ Target Feb 1 for broader pricing rollout aiming to align on-prem and cloud models.
- ✅ Proceed with marketplace private offers (AWS, Azure, GCP, OCI) before public offers.

## Key Facts

- Instance core density varies widely across hyperscalers, skewing any core-based pricing unless normalized.
- Cloud infra COGS for NVMe VMs is high (~$0.15–$0.30/GB/mo), so early cloud use cases are mostly burst.
- Three-phase cloud GTM: private offers now; public PAYGO in ~6 months; full multi-tenant SaaS likely FY28.
- Network limits (e.g., 100 Gbps east-west) can cap performance; extra cores may not translate to throughput.
- Marketplace entitlement/schema changes (notably Google) can take ~3 weeks, creating launch timing risk.
- Hybrid ELAs and marketplace burn-down are important for large customers (example discussed: Two Sigma).
- Initial market list price reference discussed: cloud capacity list around ~$0.07/GB/mo; on-prem list rework targets ~$13/TB plus core component.

## Topics / Themes

Cloud pricing model: capacity-only vs normalized cores-per-PB, Cross-cloud parity and customer perception of price discrepancies, Discount policy for cloud private offers vs on-prem discounting behavior, Marketplace private offers vs public PAYGO offers vs full SaaS timeline, Avoiding technical core disabling; commercial normalization only, TCO modeling inputs: reserved pricing, egress, infra COGS, Performance tiers / throughput-per-PB framing, Hybrid ELAs, marketplace burn-down, and entitlement tracking (Polaris/Uplink), Competitive landscape pricing models (capacity-based competitors)

## Recent Context

- 2025-10-27: [[2025-10-27 - The team debated how to align cloud pricing with the new on‑prem model. Two opti]] - Group meeting transcript debating how to align VAST cloud pricing with the new on-prem core+capacity... (via Pricing)

## Collaborators

| Person | Role | Company |
|--------|------|---------|
| [[Lior Genzel]] | Meeting participant; cloud/pricing stakeholder | VAST Data |

## Related People

- [[Lior Genzel]]
