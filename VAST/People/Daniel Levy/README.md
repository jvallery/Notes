---
type: people
title: Daniel Levy
created: '2026-01-03'
last_contact: '2025-12-19'
auto_created: true
tags:
- type/people
- needs-review
- company/ssi-(safe-superintelligence-inc.)
---

# Daniel Levy

## Contact Information

| Field | Value |
|-------|-------|
| **Role** | Co-founder / President (infra/compute) |
| **Company** | SSI (Safe Superintelligence Inc.) |
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
WHERE !completed AND contains(text, "Daniel Levy")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@DanielLevy") AND !completed
SORT due ASC
```

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

## Topics Discussed

Azure Blob API vs Tuscany trade-offs, OpenAI storage architecture and internal competition (Rockset/FoundationDB/RocksDB), AZCopy as Blob API MVP target, ABFS driver and Spark/Databricks integration considerations, Tiering/offload to Azure Blob and flash vs HDD supply dynamics, Namespace/metadata synchronization with existing cloud object data (change feed, eventual consistency), Azure Key Vault / customer-managed keys gap, Azure networking constraints (Private Link, first-party vs partner access), Foundry and Fabric integration opportunities, NeoCloud market shaping and packaging VAST portfolio, SCO session planning and messaging, Warm intro mapping via LinkedIn mutuals, Investor vectors for introductions, NVIDIA relationship strategy (events vs 1:1 intros), Outreach messaging strategy (pipeline components vs platform narrative)

## Recent Context

- 2025-12-19: [[2025-12-19]] - Discussion between Jeff Denworth and Jason Vallery on VAST’s Microsoft/Azure strategy: what level of... (via Jeff Denworth)
- 2025-11-07: [[2025-11-07 - Working session to brute-force warm paths into priority model builders using Lin]] - Working session for the Model Builder Turbine project to map warm introduction paths into priority m... (via Model Builder Turbine)

## Profile

**Role**: Co-founder / President (infra/compute) at SSI (Safe Superintelligence Inc.)
**Relationship**: Target contact (prospect)

**Background**:
- Primary SSI target contact; previously at OpenAI; noted that OpenAI paths are not viable due to conflict.

## Key Decisions

- ✅ Do not prioritize building 'append blob' support speculatively for OpenAI; only consider if/when OpenAI asks or if pipelines will take years to move and VAST wants that data.
- ✅ Define Blob API MVP for Microsoft AI as AZCopy compatibility rather than full Blob API breadth.
- ✅ Reframe outreach to focus on concrete pipeline components (Kafka for RL, real-time vector DB) rather than platform narratives.
- ✅ Use an NVIDIA-customer event (via AI Circle) as the primary NVIDIA intro mechanism; direct 1:1 intros from NVIDIA reps are unlikely.
- ✅ Broaden persona targeting to include data/pipeline owners, not just CTO-level contacts.
- ✅ Defer direct Google/Microsoft-introduced paths where conflicts exist to reduce hyperscaler conflict risk.

## Related Projects

- [[Model Builder Turbine]]

## Related




---
*Last updated: *