---
type: customer
title: Walmart
last_contact: '2025-11-14'
created: '2026-01-03'
tags:
- type/customer
- generated
---

# Walmart

## Account Status

| Field | Value |
|-------|-------|
| **Status** | Active |
| **Industry** | Retail |

## Key Contacts

- Vandana

- [[Jeff Denworth]]
- [[Mikey]]
## Open Tasks

```tasks
path includes Walmart
not done
```

## Recent Context

- 2025-11-14: Walmart big data DR sync — requirements gating for DR (namespace vs data copy); planned Mingming expectations/vision call; hybrid roadmap + deeper native GCS integration positioning; sizing options and ~1–1.5 month decision timeline.

- 2025-11-06: Internal prep for hybrid lakehouse pilot (GCS->on-prem replication, GCS API compatibility, multi-Tbps replication feasibility). See [[2025-11-06 - Walmart lakehouse pilot prep]]

- 2025-11-05: Discussed hybrid analytics requirements: BigQuery on GCP ingestion/processing, hot working set replication to two Walmart-managed facilities (active/active), strong consistency challenges across ~30+ ms sites, and need for GCS-like API on-prem; POC ready with decision target end of CY26 and roadmap gaps to close by ~Oct 2026.

- 2025-12-23: Jeff Denworth discusses Walmart's internal requirements meeting and the need for a hybrid solution f

- 2025-12-23: Jeff Denworth discusses Walmart's internal requirements meeting and their need for a hybrid solution
## Key Facts

- Walmart needs a hybrid solution for their data team and is starting a big data POC for on-premises workloads.

- Any solution Walmart moves forward with will require integration with GCS.
## Topics

- Walmart
- hybrid solution
- data team
- big data POC
- integration with GCS
## Opportunities

- Namespace/metadata synchronization with pre-existing cloud object data; proxy/always-fast expectations; tiering discussions
- Big data platform deployment with hybrid/DR requirements; two proposals (minimum config vs larger phase-one) with potential scale up to ~500 PB and deal framed up to ~$300M
- Capture and document Walmart requirements/FRDs in Confluence; use as archetype for cloud-invested customers
- Walmart write-up/FRD migration into Confluence; example of complex cloud interplay
- Document Walmart FRDs and future customer requirements in Confluence; use as pattern for cloud-intersection planning
- Google-related Walmart project: sync Google Cloud Storage data into on-prem VAST for analytics; potential longer-term cloud exit/repatriation
- Q4 pilot: deploy two VAST clusters (Region 1/Region 2) for testing
- Long-term repatriation of enterprise analytics lakehouse from GCP to two on-prem sites (target full project in 2027 if approved)
- VAST POC/pilot ready to begin with decision goal by end of CY26; roadmap gap closure needed by ~Oct 2026 ahead of holiday code freeze and Jan 2027 budget cycles
- Hybrid-cloud data lake replication from GCP into two Walmart facilities with preference for GCS-like API on-prem

## Blockers

- ❌ Customer pressure ('boot on your neck') may force prioritizing namespace/existing-data exposure work
- ❌ Eventual consistency/change notification complexity
- ❌ DR requirement ambiguity (full VAST namespace in cloud vs data copy)
- ❌ Unclear capacity/performance/access patterns and acceptance criteria
- ❌ Tight decision timeline (~1–1.5 months) may compress evaluation/testing

## Collaborators

| Person | Role | Company |
|--------|------|---------|
| [[Matt]] |  |  |
| [[Mikey]] |  |  |
| [[Alon Horev]] |  |  |
| [[Josh Wentzell]] | Automation/DevOps; lab tooling; customer-facing API automation | VAST Data |
| Vandana |  | Walmart |
| [[Lior Genzel]] | Cloud ("cloud guy") |  |
| [[Jeff Denworth]] |  |  |
| [[Avi]] | Architecture (DataSpaces/replication/global namespace) |  |
| [[Paul]] | Sales Engineer (SE) for Mikey |  |
| [[Jason Vallery]] | Product management (cloud); partnerships with hyperscale cloud providers | VAST Data |

## Related

<!-- Wikilinks to related entities -->

## Related Projects

- [[big data POC]]
