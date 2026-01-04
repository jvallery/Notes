---
type: customer
title: CoreWeave
created: '2026-01-03'
last_contact: '2025-12-19'
status: active
auto_created: true
tags:
- type/customer
- needs-review
- status/active
---

# CoreWeave

## Account Overview

_Brief description of this customer, their business, and relationship..._

## Account Status

| Field | Value |
|-------|-------|
| **Status** | Prospect |
| **Industry** | _Unknown_ |

## Key Contacts

- [[Gordon Brown]]

## Active Projects

_What projects/initiatives are active with this customer?_

```dataview
LIST
FROM "VAST/Projects" OR "Personal/Projects"
WHERE contains(file.outlinks, this.file.link)
```


## Current Blockers

- ❌ Exceptional case; may not generalize
- ❌ Strict SLA/SLO requirements with potential legal penalties
- ❌ Operational coverage strain (weekends/off-shift knowledge transfer gaps)

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

- Move faster than others; exemplar NeoCloud; expand services beyond GPUs over time
- Define/validate SLA/SLO commitments and legal penalties; ensure staffing/on-call model meets requirements
- Potentially treat as partner-like engagement model informing VAST-as-a-Service operations

## Key Decisions

- ✅ Do not prioritize building 'append blob' support speculatively for OpenAI; only consider if/when OpenAI asks or if pipelines will take years to move and VAST wants that data.
- ✅ Define Blob API MVP for Microsoft AI as AZCopy compatibility rather than full Blob API breadth.

## Key Facts

- OpenAI is reportedly replatforming away from Azure Blob API for some scenarios and building its own data movement solution (e.g., rclone).
- Microsoft’s deal with OpenAI reportedly grants Microsoft ownership/exclusive rights to code written by OpenAI until AGI is declared; Microsoft can reuse/reship that IP.
- AZCopy is open source and is a key data movement tool for Azure Blob; MAI uses it as a data movement engine.
- Bing uses an internal storage platform called Cosmos (not Cosmos DB) with its own API surface; attempts to migrate Bing to Blob reportedly failed.
- Azure premium blob is described as small (likely petabytes, not exabytes); Azure disks business is not the near-term winnable market for VAST.
- Flash supply constraints may persist due to vendor capacity shifting toward higher-margin HBM/DRAM; price of flash recently doubled (per discussion).
- Two distinct integration patterns: (1) offload/tiering in VAST-native format (performance/cost optimized but not readable via native cloud APIs), and (2) exposing existing cloud-native data requiring change notifications and eventual consistency (e.g., Azure Change Feed).
- VAST does not support Azure Key Vault integration today (gap for customer-managed keys).
- Private Link / VNet boundary is a recurring constraint for integrating VAST with Azure managed services; first-party services may have deeper access (e.g., network security perimeter).
- Jason is earmarked to present at SCO; Jeff wants him to be 'lord of all things cloud' and cover AI cloud building with VAST.

## Topics / Themes

Azure Blob API vs Tuscany trade-offs, OpenAI storage architecture and internal competition (Rockset/FoundationDB/RocksDB), AZCopy as Blob API MVP target, ABFS driver and Spark/Databricks integration considerations, Tiering/offload to Azure Blob and flash vs HDD supply dynamics, Namespace/metadata synchronization with existing cloud object data (change feed, eventual consistency), Azure Key Vault / customer-managed keys gap, Azure networking constraints (Private Link, first-party vs partner access), Foundry and Fabric integration opportunities, NeoCloud market shaping and packaging VAST portfolio, SCO session planning and messaging, VAST cloud-first vision (VAST-as-a-Service, multi-cloud), Customer Success operating model vs SRE model, CoreWeave and XAI on-prem operations, XAI workload patterns (training data, checkpointing, inferencing)

## Recent Context

- 2025-12-19: [[2025-12-19]] - Discussion between Jeff Denworth and Jason Vallery on VAST’s Microsoft/Azure strategy: what level of... (via Jeff Denworth)
- 2025-10-29: [[2025-10-29 - Jason introduced his cloud-first vision for VAST (VAST-as-a-Service, multi-cloud]] - 1:1 between Jason Vallery and Rick Haselton covering Jason’s cloud-first VAST-as-a-Service vision an... (via Rick Haselton)

## Collaborators

| Person | Role | Company |
|--------|------|---------|
| [[Rick Haselton]] | Tech lead (Customer Success; managed-services/SRE-style pod) | VAST Data |
| [[Gordon Brown]] | CSM for CoreWeave | VAST Data |

## Related People

- [[Rick Haselton]]
- [[Gordon Brown]]
