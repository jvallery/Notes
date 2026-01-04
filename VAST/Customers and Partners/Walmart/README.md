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

## Recent Context

- 2025-11-14: [[2025-11-14 - Internal sync to align on Walmart’s big data initiative, clarify requirements, a]] - Internal team sync to align on Walmart’s big data initiative, focusing on clarifying disaster recove...
- 2025-11-06: [[2025-11-06 - Internal prep to shape an architecture whiteboarding session with Walmart’s Lake]]
- 2025-11-05: [[2025-11-05 - Walmart Analytics]] - Note captures Walmart’s hybrid analytics storage/replication requirements for moving a hot working s...

## Key Facts

- Architecture/whiteboarding session is gated on receiving definitive requirements from Walmart.
- Key DR ambiguity: Walmart may need full VAST namespace access in cloud vs only a copy of data.
- VM-based approaches in public cloud are not viable at the anticipated scale.
- Hybrid roadmap is being driven, including deeper/more native Google Cloud Storage (GCS) integration.
- Jason plans to meet engineering in Tel Aviv the week after next to shape the roadmap, with Walmart as a marquee design partner.
- Walmart has ~1–1.5 months to choose between a minimum configuration and a larger phase-one proposal (main difference: D-boxes/capacity).
- Opportunity scale discussed up to ~500 PB and framed as potentially up to a $300M deal.
- A 30-minute expectations/vision call with Mingming is planned for 2025-11-14 after 2 pm PT.
- Primary ingestion and processing is in BigQuery on GCP.
- Hot working set must be replicated into two Walmart-owned/managed facilities for analytics processing.

## Topics

Walmart big data initiative alignment, Disaster recovery (DR) requirements clarification, Architecture/whiteboarding session gating criteria, Hybrid cloud roadmap strategy, Native Google Cloud Storage (GCS) integration requirements, Proposal options: minimum config vs phase-one (D-box/capacity differences), Customer timeline and decision process, Scaling limitations of VM-based cloud deployments, Customer expectations/vision call planning, Hybrid cloud analytics architecture (GCP + on-prem active/active), Replication of hot working set from BigQuery/GCP to on-prem, Consistency models (strong consistency vs latency/write-rate constraints), WAN latency impact between on-prem sites, RPO/RTO and tolerance for small data loss, Trino/Presto and Spark analytics processing on replicated data

## Related

<!-- Wikilinks to related entities -->
