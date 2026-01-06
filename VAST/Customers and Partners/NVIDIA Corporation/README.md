---
type: customer
title: NVIDIA Corporation
account_type: ''
status: ''
industry: _Unknown_
created: '2026-01-05'
last_contact: '2025-12-01'
tags:
- type/customer
- needs-review
---
# NVIDIA Corporation

## Account Status

| Field | Value |
|-------|-------|
| **Status** | _Unknown_ |
| **Industry** | _Unknown_ |

## Key Contacts

## Open Tasks

```tasks
path includes NVIDIA Corporation
not done
```

## Recent Context

- 2025-12-01: Brian Evans alerted the PM team that RFE 0482 for NVIDIA Corporation was submitted and approved, req...
## Key Facts

- RFE 0482 is associated with NVIDIA Corporation and the opportunity 'DGX-C | Coreweave' (opportunity amount $0, close date 2025-11-02).

- NVIDIA DGX Cloud Storage Team uses VAST across more than five NCPs and manages multiple petabytes of capacity, but lacks a unified operational view due to inconsistent telemetry and dashboards per NCP.

- RFE 0482 requests dual-uplink visibility for a dedicated VAST cluster 'LAX-02', allowing both lambda.cloud.vastdata.com and nvidiadgxc.cloud.vastdata.com to see the same cluster.

- RFE 0482 requests tenant-scoped visibility for a multi-tenant VAST cluster 'LAX-03', so nvidiadgxc.cloud.vastdata.com can access only NVIDIA DGX Cloud tenant metrics/workloads/config/health without exposing other tenants or cluster-wide information.

- RFE 0482 lists estimated incremental value of $100,000,000 and 10,000 PB, and is marked 'Deal Blocker: No'.
## Topics

- RFE 0482 for NVIDIA DGX Cloud: unified visibility across VAST clusters deployed at multiple NCPs

- Dual-uplink visibility for dedicated cluster LAX-02 (lambda.cloud.vastdata.com and nvidiadgxc.cloud.vastdata.com)

- Tenant-scoped visibility for multi-tenant cluster LAX-03 (NVIDIA-only tenant data via nvidiadgxc.cloud.vastdata.com)

- Service Aware VIP Pool concept for multi-VIP access to VMS (GUI/CLI/REST/SSH/CSI)

- Salesforce RFE hygiene: linking RFE to the correct Related Feature
## Key Decisions

- Jeff Denworth assigned Mordechai Blaunstein to lead the investigation of RFE 0482 and to bring in additional parties as needed.