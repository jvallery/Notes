---
type: people
title: Karl Vietmeier
last_contact: unknown
created: '2026-01-03'
tags:
- type/people
- generated
---

# Karl Vietmeier

## Recent Context

- unknown: [[Available Capacity Calculations]] - Internal note arguing against using a single fixed overhead percentage (e.g., 35%) for cloud deploym... (via Cloud)
- 2025-10-31: [[2025-10-31 - Introductory 1-1 aligning on VAST’s cloud strategy. Jason outlined a vision for]]

## Key Facts

- Provider-guaranteed sub-zonal failure domain counts differ materially: GCP up to 8 per zone (Spread Placement Policy), AWS 7 distinct racks/partitions per AZ (Spread/Partition placement groups), Azure 5 FDs per zone with static-fixed VMSS (Availability Sets: 3 FDs and 20 update domains), OCI exactly 3 FDs per availability domain.
- FD width affects erasure coding parity overhead for the same failure tolerance; a uniform overhead (e.g., 35%) can cause pricing/delivery surprises.
- Storage-optimized SKU capacity can be uneven across zones and even within sub-zonal domains; effective stripe width/capacity is limited by the least-populated FD used by the stripe.
- Azure maintenance semantics: only one Update Domain at a time for Availability Sets/Uniform VMSS; on GCP/AWS rolling update blast radius is controlled by user-set budgets (MIG/ASG).
- Local NVMe/instance store is ephemeral across providers; rebuild headroom requirements vary by provider and maintenance/failure patterns.
- Capacity reservations exist across clouds (AWS On-Demand Capacity Reservations, Azure Capacity Reservation, GCP Reservations, OCI Compute Capacity Reservations) but do not guarantee balanced capacity across FDs; skew must be modeled.
- Example max safe intra-zone EC widths based on FD guarantees: GCP width 8 (e.g., 7+1 overhead 14.3%, 6+2 overhead 33.3%); AWS width 7 (6+1 16.7%, 5+2 40%); Azure width 5 (4+1 25%, 3+2 66.7%); OCI width 3 (2+1 50%).
- Proposed computation: raw capacity per FD = instances_FD × ephemeral_TiB; stripe limiter = min(raw capacity across W FDs); usable zone capacity approximated by sum(raw_capacity_FD) × (k/W) minus rebuild and rolling-update headroom; then apply non-EC overheads; apply outer-code factor for zone-level HADR (e.g., 2+1 across three AZs).
- Karl’s sheet indicates approximate overhead components of ~8% filesystem and ~3% SCM.

## Topics

Cloud capacity/pricing overhead modeling, Failure domains and placement/spreading mechanisms (GCP Spread Placement Policy, AWS placement groups, Azure VMSS/Availability Sets, OCI FDs), Erasure coding stripe width and parity overhead tradeoffs, SKU availability and zone/FD capacity skew (e.g., Azure Ls-series), Rolling update and maintenance semantics (Azure Update Domains, GCP MIG, AWS ASG Instance Refresh), Ephemeral local storage behavior and rebuild headroom, Capacity reservations across cloud providers, Zone-level HADR vs intra-zone coding tradeoffs (latency/egress considerations)

## Related

<!-- Wikilinks to related entities -->
