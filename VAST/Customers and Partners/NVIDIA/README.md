---
type: customer
title: NVIDIA
created: '2026-01-03'
last_contact: '2025-12-19'
status: active
auto_created: true
tags:
- type/customer
- needs-review
- industry/semiconductors-/-ai-infrastructure
- status/active
---

# NVIDIA

## Account Overview

_Brief description of this customer, their business, and relationship..._

## Account Status

| Field | Value |
|-------|-------|
| **Status** | Partner |
| **Industry** | Semiconductors / AI infrastructure |

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

- ❌ Flash supply constraints impacting GPU cluster deployment

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

- Broaden perception of VAST beyond object store; align on evolving inference/storage needs
- Feature intake example: NVIDIA-driven request for S3 RDMA targeted for a next major release.

## Key Decisions

- ✅ Do not prioritize building 'append blob' support speculatively for OpenAI; only consider if/when OpenAI asks or if pipelines will take years to move and VAST wants that data.
- ✅ Define Blob API MVP for Microsoft AI as AZCopy compatibility rather than full Blob API breadth.

## Key Facts

- Eyal Traitel joined VAST in Dec 2024; Noa Cohen is a long-tenured VAST employee focusing on major releases while Eyal focuses on minor releases.
- Feature intake channels include leadership/architects, and SE requests filed in Salesforce tied to opportunities and triaged by Tomer Hagay’s team with bi-weekly reviews.
- Release managers run day-to-day execution for major and minor releases; Shelly Martin (Ops) and Liraz Ben Or (R&D) drive phase-gate documentation/process.
- vForce (Roy Sterman) and Dafna’s team manage service packs and hotfixes, including back/forward-porting and ensuring fixes go upstream to minors/majors.
- Minor releases are treated like full releases with regression and performance testing; weekly content/testing reviews.
- Planning is highly dynamic due to frequent urgent customer/field requests (example: Tesla), causing scope churn and parallel streams.
- 5.6 phase gates are underway with target GA in July next year.
- Historical cadence is roughly 2–3 major releases per year.
- Major multi-tenancy blocker: authentication providers limited to 8 and configured at host cluster rather than tenant-scoped; scaling and tenantizing is a large effort.
- Control plane (Polaris/Iceland) is more cloud-native; cluster layer is not yet operating in an agile/SaaS mode.

## Topics / Themes

Release planning and execution (major/minor releases), Hotfixes and service packs (backport/forward-port, upgrade alignment), Feature intake and triage process (Salesforce tied to opportunities), Phase-gate process and documentation, QA/regression/performance testing for minor releases, SaaS and multi-tenant readiness, Multi-tenancy gaps (auth providers limit, tenant-scoped auth), Control plane vs cluster responsibilities (Polaris/Iceland vs cluster), Impact of urgent customer requests on scope and resourcing, 5.6 timeline and GA target, Azure Blob API vs Tuscany trade-offs, OpenAI storage architecture and internal competition (Rockset/FoundationDB/RocksDB), AZCopy as Blob API MVP target, ABFS driver and Spark/Databricks integration considerations, Tiering/offload to Azure Blob and flash vs HDD supply dynamics

## Recent Context

- 2025-12-19: [[2025-12-19]] - Discussion between Jeff Denworth and Jason Vallery on VAST’s Microsoft/Azure strategy: what level of... (via Jeff Denworth)
- 2025-10-29: [[2025-10-29 - Jason and Eyal aligned on how VAST plans and executes majorminor releases, hotf]] - Jason Vallery and Eyal Traitel aligned on VAST’s release planning/execution (major/minor releases, h... (via Eyal Traitel)

## Related People

_Internal team members working on this account..._


---
*Last updated: *