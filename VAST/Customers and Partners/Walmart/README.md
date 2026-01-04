---
type: customer
title: Walmart
last_contact: '2025-12-19'
created: '2026-01-03'
tags:
- type/customer
- generated
---

# Walmart

## Recent Context

- 2025-11-14: [[Sources/Transcripts/2025/2025-11-14 - Internal sync to align on Walmart’s big data initiative, clarify requirements, a.md|Internal sync to align on Walmart’s big data initiative, clarify requirements, a]] — **Date:** 2025-11-14 · **Customer:** Walmart · **Folder:** Customers/Walmart

- 2025-11-05: [[Sources/Transcripts/2025/2025-11-05 - Walmart Analytics.md|Walmart Analytics]] — Requirements -

- 2025-11-06: [[Sources/Transcripts/2025/2025-11-06 - Internal prep to shape an architecture whiteboarding session with Walmart’s Lake.md|Internal prep to shape an architecture whiteboarding session with Walmart’s Lake]] — **Date:** 2025-11-06 · **Customer:** Walmart · **Folder:** Customers/Walmart

- 2025-12-19: [[2025-12-19]] - Discussion between Jeff Denworth and Jason Vallery on VAST’s Microsoft/Azure strategy: what level of... (via Jeff Denworth)
- 2025-11-14: [[2025-11-14 - Internal sync to align on Walmart’s big data initiative, clarify requirements, a]] - Internal sync to align on Walmart’s big data initiative, focusing on clarifying disaster recovery re...
- 2025-11-07: [[2025-11-07 - We reviewed the org landscape and aligned on my near-term focus. Jeff outlined k]] - 1:1 with Jeff Denworth to review the org landscape, clarify key stakeholders, and align on the autho... (via Jeff Denworth)
- 2025-11-07: [[2025-11-07 - Reviewed org landscape and key players; aligned that Jason will deeply understan]] - Weekly 1:1 between Jason Vallery and Jeff Denworth reviewing VAST’s org landscape and key players, a... (via Jeff Denworth)
- 2025-11-07: [[2025-11-07 - We reviewed the org landscape and immediate priorities. Jeff highlighted key pla]] - 1:1 discussion with Jeff Denworth reviewing VAST org landscape, immediate priorities, and a pragmati... (via Jeff Denworth)
- 2025-11-07: [[2025-11-07 - We aligned on hyperscaler strategy across Google and Microsoft. On Google, GDC i]] - 1:1 strategy sync with Jonsi Stephenson aligning VAST’s hyperscaler approach across Google and Micro... (via Jonsi Stephenson)
- 2025-11-06: [[2025-11-06 - Internal prep to shape an architecture whiteboarding session with Walmart’s Lake]] - Internal prep for an in-person architecture whiteboarding session with Walmart’s Lakehouse team to d...
- 2025-11-05: [[2025-11-05 - Walmart Analytics]] - Note captures Walmart’s hybrid analytics/storage requirements: replicate a hot working set from BigQ...
- 2025-10-31: [[2025-10-31 - Introductory 1-1 focused on VAST on Cloud strategy and current platform gaps. Jo]] - Introductory 1:1 with Josh Wentzell to align on VAST on Cloud strategy and identify platform gaps, e... (via Josh Wentzell)
- 2025-10-31: [[2025-10-31 - Introductory 1-1 aligning on VAST’s cloud strategy. Jason outlined a vision for]] - Introductory 1:1 between Jason Vallery and Karl Vietmeier aligning on VAST’s cloud strategy, includi... (via Karl Vietmeier)
- 2025-10-30: [[2025-10-30 - The group aligned on the cloud support operating model (Customer Success, Suppor]] - Group meeting to align the cloud support operating model (Customer Success, Support, SRE), hyperscal... (via Cloud)
- 2025-09-29: [[2025-09-29 - Jason shared disappointment with his rewards and anxiety about scope and support]] - Weekly 1:1 between Maneesh Sah and Jason Vallery focused on Jason’s dissatisfaction with rewards, re... (via Maneesh Sah)

## Key Facts

- Walmart DR requirement is ambiguous: full VAST namespace access in cloud vs only a data copy.
- VM-based cloud deployments are not viable at the anticipated Walmart scale.
- Team is driving a hybrid roadmap with a goal of more native Google Cloud Storage integration.
- Jason Vallery plans to meet engineering in Tel Aviv the week after next to shape the roadmap using Walmart as a marquee design partner.
- Walmart is evaluating two proposals: minimum configuration vs larger phase-one (main difference is D-boxes/capacity).
- Walmart decision timeline is ~1–1.5 months.
- Opportunity discussed could reach ~500 PB and is framed as up to a ~$300M deal.
- Walmart uses Azure for dot-com systems and GCP (BigQuery/GCS) for enterprise analytics.
- Walmart wants a consistent lakehouse view across GCP and two on-prem sites; two on-prem DCs run active-active with >30 ms latency.
- Immediate ask: two VAST clusters (Region 1/Region 2) in Q4 for pilot testing.

## Topics

Walmart big data initiative requirements, Disaster recovery approach (full namespace vs data copy), Hybrid cloud roadmap and native Google Cloud Storage integration, Customer engagement sequencing (expectations call before architecture session), Proposal sizing (minimum config vs phase-one; D-box/capacity), Timeline and scheduling constraints (supercomputing conference), Walmart hybrid lakehouse architecture (GCP + two on-prem sites), SyncEngine replication from GCS to on-prem, DataSpaces/global namespace across on-prem sites, GCS API compatibility requirement, Strong consistency challenges and write-lease semantics, Network throughput/egress feasibility for multi-Tbps replication, Pilot/POC scoping using real workloads (Trino/Presto, Spark; Delta/Hudi tables), Governance, multi-tenancy, auditing, and compliance requirements, BigQuery interoperability considerations

## Account Status

| Field | Value |
|-------|-------|
| **Status** | Active |
| **Industry** | Retail |

## Key Contacts

- [[Vandana]]

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
| [[Vandana]] |  | Walmart |
| [[Lior Genzel]] | Cloud ("cloud guy") |  |
| [[Jeff Denworth]] |  |  |
| [[Avi]] | Architecture (DataSpaces/replication/global namespace) |  |
| [[Paul]] | Sales Engineer (SE) for Mikey |  |
| [[Jason Vallery]] | Product management (cloud); partnerships with hyperscale cloud providers | VAST Data |

## Key Decisions

- ✅ Do not schedule an architecture/whiteboarding session until Walmart requirements are clarified.
- ✅ Lead with current capabilities plus forward hybrid roadmap narrative in the Mingming call.
- ✅ Escalate to a deeper technical session with additional SMEs only after requirement confirmation.
- ✅ Use SyncEngine for the pilot to replicate from GCS to on-prem VAST clusters.
- ✅ Pursue GCS API compatibility on the roadmap; S3 alone is insufficient for Walmart.
- ✅ Focus the pilot on real Walmart workloads (tables/queries), not synthetic benchmarks.
- ✅ Consolidate questions and send to Walmart before scheduling the design session.
- ✅ Do not prioritize building 'append blob' support speculatively for OpenAI; only consider if/when OpenAI asks or if pipelines will take years to move and VAST wants that data.
- ✅ Define Blob API MVP for Microsoft AI as AZCopy compatibility rather than full Blob API breadth.
- ✅ Carl will move to ProServe under Rob rather than supporting customer-facing PM work.

## Related People

- [[Matt]]
- [[Mikey]]
- [[Alon Horev]]
- [[Josh Wentzell]]
- [[Vandana]]
- [[Lior Genzel]]
- [[Jeff Denworth]]
- [[Avi]]
- [[Paul]]
- [[Jason Vallery]]

## Related

<!-- Wikilinks to related entities -->
