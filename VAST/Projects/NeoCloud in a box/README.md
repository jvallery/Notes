---
type: projects
title: NeoCloud in a box
created: '2026-01-03'
last_updated: ''
status: active
auto_created: true
tags:
- type/projects
- needs-review
- status/active
last_contact: '2025-12-19'
---

# NeoCloud in a box

## Overview

Packaging VAST portfolio as a blueprint for NeoClouds to offer AI cloud services beyond GPU-as-a-service, including storage, event streaming, analytics/warehouse, telemetry, and potentially serverless functions.

## Status

| Field | Value |
|-------|-------|
| **Status** | active |
| **Owner** | Morty |

## Current Blockers

- ❌ NeoCloud market still forming; strategies not mature
- ❌ Need VAST to help shape market and provide clear productized stories
- ❌ Unclear internal execution cadence (QBRs/templates not consistently run)

## Next Steps

- [ ] Jason to push Morty on executing agreed plan and help if needed
- [ ] Gather signals/roadmaps from NeoClouds (e.g., Lambda launching full VAST portfolio) and incorporate into messaging
- [ ] Define narrow initial scenarios to win first 10 customers

## Collaborators

| Person | Role | Company |
|--------|------|---------|
| [[Jeff Denworth]] |  |  |
| [[Morty]] |  |  |
| [[Jason Vallery]] | Product management (cloud); partnerships with hyperscale cloud providers | VAST Data |

## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed
SORT due ASC
```


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

Azure Blob API vs Tuscany trade-offs, OpenAI storage architecture and internal competition (Rockset/FoundationDB/RocksDB), AZCopy as Blob API MVP target, ABFS driver and Spark/Databricks integration considerations, Tiering/offload to Azure Blob and flash vs HDD supply dynamics, Namespace/metadata synchronization with existing cloud object data (change feed, eventual consistency), Azure Key Vault / customer-managed keys gap, Azure networking constraints (Private Link, first-party vs partner access), Foundry and Fabric integration opportunities, NeoCloud market shaping and packaging VAST portfolio, SCO session planning and messaging

## Related People

- [[Jeff Denworth]]
- [[Morty]]
- [[Jason Vallery]]

## Related Customers

- [[Lambda]]
- [[N-Scale]]
- [[CoreWeave]]

## Recent Context

- 2025-12-19: [[2025-12-19]] - Discussion between Jeff Denworth and Jason Vallery on VAST’s Microsoft/Azure strategy: what level of... (via Jeff Denworth)

## Artifacts

```dataview
TABLE file.mtime as "Modified"
FROM ""
WHERE type != "readme" AND type != "projects"
SORT file.mtime DESC
```

---
*Last updated: *