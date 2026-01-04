---
type: customer
title: Silk
last_contact: '2025-09-29'
created: '2026-01-03'
tags:
- type/customer
- generated
---

# Silk

## Recent Context

- 2025-09-29: [[2025-09-29 - Jason shared disappointment with his rewards and anxiety about scope and support]] - Weekly 1:1 between Maneesh Sah and Jason Vallery focused on Jason’s dissatisfaction with rewards, re... (via Maneesh Sah)
- 2025-09-15: [[2025-09-15 - Silk briefed Jason on its cloud storage architecture optimized for databases and]] - Weekly 1:1 where Silk briefed Jason on its software-defined cloud storage architecture for high-perf...
- 2025-09-15: [[2025-09-15 - Silk briefed Jason on its software-defined cloud storage for high-performance re]] - Silk briefed Jason on its software-defined cloud storage architecture for high-performance relationa...
- 2025-09-15: [[2025-09-15 - Silk briefed Jason on their software-defined cloud storage for databases, emphas]] - Silk briefed Jason on their software-defined cloud storage for database workloads, focusing on low-l...

## Key Facts

- Silk is software-defined cloud storage optimized for database and single source-of-truth workloads.
- Typical scale cited: up to ~1 PB per data pod with tens of GB/s throughput and sub-ms latency.
- Silk cited ~2–3M TPS with 64k transactions and noted single-VM DB performance is often the limiting factor.
- Architecture: performance layer near DB VMs (PPG) with read cache; durable layer on Azure PV2 with added erasure coding or on VMs with ephemeral media; compression and optional dedupe.
- Silk often competes with Azure NetApp Files and claims it can outperform ANF Ultra at lower cost for certain DB workloads.
- Silk wants RDMA on the front end of Azure L-series to reduce CPU overhead; they are working with Gal Piglin’s team.
- AI workloads (RAG/agentic) are increasing unpredictable access to production relational databases (SQL/Oracle/Postgres).
- Two access patterns discussed: maximize production DB performance vs create near-real-time copies (tens of seconds) for AI access.
- Silk is software-defined cloud storage optimized for structured relational DB workloads across Azure/GCP/AWS.
- A single Silk data pod supports ~1–500 databases up to ~1 PB with n+x resilience and read cache (cNodes).

## Topics

Silk cloud storage architecture for databases, Performance characteristics (throughput, latency, TPS), AI-driven access to systems of record (real-time vs near-real-time), Positioning vs Azure native storage (Azure NetApp Files), RDMA requirement on Azure L-series and CPU overhead, Executive introduction planning (Jay Menon via Ong), Silk architecture (performance layer, cache, durability options), AI-driven load on production relational databases (systems of record), Performance limits (TPS, throughput, latency) and IO sizing, Approaches: accelerate production DB vs near-real-time clones, RDMA support on Azure L-series / Duo Boost and CPU overhead reduction, Competitive context (Azure NetApp Files) and cost/performance positioning, Silk software-defined cloud storage for databases, Azure performance characteristics (Boost VMs, PV2, PPG), AI-driven load spikes on transactional systems of record

## Account Status

| Field | Value |
|-------|-------|
| **Status** | Active |
| **Industry** | Software-defined cloud storage |

## Key Contacts

- [[Jai Menon]]

## Opportunities

- Potential collaboration/positioning for Azure customers needing higher performance than Azure native storage (e.g., ANF) can provide
- Enablement request: RDMA on Azure L-series front end to reduce CPU overhead and improve performance
- Position Silk for customers whose relational DB workloads exceed Azure native storage/network performance ceilings
- Potential enablement via RDMA support on Azure L-series front end to reduce CPU overhead and improve performance
- Position Silk for customer workloads where native Azure storage cannot meet low-latency/high-throughput database performance requirements
- Potential joint work contingent on enabling RDMA access on Azure L-series front end to reduce CPU overhead

## Blockers

- ❌ Unclear timeline/feasibility for RDMA front-end support on Azure L-series
- ❌ No clear Azure timeline for RDMA support on L-series/Duo Boost
- ❌ Unclear feasibility/timeline for RDMA support on Azure L-series for Silk front end

## Collaborators

| Person | Role | Company |
|--------|------|---------|
| [[Jai Menon]] |  |  |
| [[Jason Vallery]] | Product management (cloud); partnerships with hyperscale cloud providers | VAST Data |

## Key Decisions

- ✅ Proceed with connecting to Jai Menon through Ong.
- ✅ Proceed with setting up a CEO-level introduction to Jai Menon.
- ✅ Evaluate use case fit per customer: accelerate production DB vs near-real-time cloned copies.

## Related People

- [[Jai Menon]]
- [[Jason Vallery]]

## Related

<!-- Wikilinks to related entities -->
