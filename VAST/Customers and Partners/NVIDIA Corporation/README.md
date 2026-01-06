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

- 2025-12-21: Mentioned in: CES 2026 planning: NVIDIA Live (Jan 5), embargo timing, and Microsoft Jay Parikh meeting
- 2025-12-01: Brian Evans alerted the PM team about RFE 0482 for NVIDIA DGX Cloud, requesting unified operational ...
- 2025-12-21: Mentioned in: CES planning: NVIDIA Live (Jan 5), embargo timing, and Microsoft Jay Parikh meeting request
- 2025-12-01: Mentioned in: RFE 0482 (NVIDIA DGX Cloud): unified visibility across NCPs, dual-uplink and tenant-scoped Uplink access
- 2026-01-01: Mentioned in: Zoom invite: Urgent training on KV Cache opportunity and NVIDIA Context Memory Extension (CME)
- 2026-01-01: Mentioned in: Urgent training invite: KV Cache opportunity and NVIDIA Context Memory Extension (CME) for AI sellers
- 2026-01-04: Mentioned in: VAST and OpenAI weekly account pursuit update, POC touch base and Nvidia enablement (week ending 2026-01-02)
## Key Facts

- RFE 0482 is associated with NVIDIA Corporation and the opportunity 'DGX-C | Coreweave' (opportunity amount $0, close date 2025-11-02).

- NVIDIA DGX Cloud Storage Team uses VAST across more than five NCPs and manages multiple petabytes of capacity, but lacks a unified operational view due to inconsistent telemetry and dashboards per NCP.

- RFE 0482 requests dual-uplink visibility for a dedicated VAST cluster 'LAX-02', allowing both lambda.cloud.vastdata.com and nvidiadgxc.cloud.vastdata.com to see the same cluster.

- RFE 0482 requests tenant-scoped visibility for a multi-tenant VAST cluster 'LAX-03', so nvidiadgxc.cloud.vastdata.com can access only NVIDIA DGX Cloud tenant metrics/workloads/config/health without exposing other tenants or cluster-wide information.

- RFE 0482 lists estimated incremental value of $100,000,000 and 10,000 PB, and is marked 'Deal Blocker: No'.

- NVIDIA is hosting an event called "NVIDIA Live" at CES on January 5, 2026 starting at 1:00pm PT at the Fontainebleau; it is open to anyone and is not a press conference.

- The embargo for NVIDIA's CME announcement lifts at 3:00pm PT on January 5, 2026, which is when VAST blog, demo, and press release content can be announced.

- NVIDIA is doing a 90-minute closed media-only press conference at CES; the goal is to have VAST shown as the "first/best/only" solution in the media briefing and amplify it online.

- NVIDIA sent VAST two additional press releases requesting VAST inclusion: the NVIDIA Rubin press release and the Open Models press release; VAST has a supporting blog post in progress for Open Models with Lior Cohen from NVIDIA.

- NVIDIA is not asking VAST for quotes in the referenced CES-related press releases, only approval of VAST mentions.

- RFE 0482 is an 'Existing Feature Enhancement' request associated with the account NVIDIA Corporation and the opportunity 'DGX-C | Coreweave' in Salesforce.

- NVIDIA DGX Cloud Storage Team uses VAST across more than five NCPs and manages multiple petabytes of capacity, but lacks a unified view because each NCP provides telemetry and dashboards differently.

- For dedicated VAST cluster LAX-02 (single-tenant, DGX Cloud only), NVIDIA requests dual-uplink visibility so both lambda.cloud.vastdata.com and nvidiadgxc.cloud.vastdata.com can see the same cluster.

- For multi-tenant VAST cluster LAX-03, NVIDIA requests tenant-filtered visibility so nvidiadgxc.cloud.vastdata.com can access only the DGX Cloud tenant data (metrics, workloads, configurations, health) without exposing other tenants or cluster-wide information.

- NVIDIA Live at CES is scheduled for January 5, 2026 starting at 1:00pm PT at the Fontainebleau and is open to anyone (not a press conference).

- The embargo for NVIDIA's CME announcement lifts at 3:00pm PT on January 5, 2026, which is when VAST blog, demo, and press release can be announced.

- Marianne Budnik stated NVIDIA is doing a 90-minute media-only press conference at CES and nothing from that event will be shown broadly.

- Kirstin Bordner stated NVIDIA sent VAST two additional press releases where NVIDIA would like VAST included: the NVIDIA Rubin press release and the Open Models press release.

- Kirstin Bordner stated NVIDIA is not asking for a quote from VAST in these announcements, only approval of the VAST mentions.

- RFE 0482 is an "Existing Feature Enhancement" RFE associated with account NVIDIA Corporation and opportunity "DGX-C | Coreweave" (opportunity amount $0, close date 2025-11-02).

- NVIDIA DGX Cloud Storage Team uses VAST across more than five NCPs and manages multiple petabytes of capacity, and expects continued expansion; inconsistent NCP telemetry/dashboards create fragmented visibility and operational friction.

- RFE 0482 requests dual-uplink visibility for dedicated VAST cluster LAX-02 so both lambda.cloud.vastdata.com and nvidiadgxc.cloud.vastdata.com can receive visibility into the same cluster.

- RFE 0482 requests tenant-filtered visibility for multi-tenant VAST cluster LAX-03 so nvidiadgxc.cloud.vastdata.com can access only NVIDIA DGX Cloud tenant metrics/workloads/config/health without exposing other tenants or cluster-wide information.

- NVIDIA is making major KV Cache storage announcements at CES and announced Context Memory Extension (CME) impacting inference infrastructure.

- NVIDIA is expected to make major KV Cache storage announcements at CES during the week of January 5, 2026, including an announcement related to Context Memory Extension (CME).

- VAST is working on additional education for the Nvidia team that works with OpenAI.
## Topics

- RFE 0482 for NVIDIA DGX Cloud: unified visibility across VAST clusters deployed at multiple NCPs

- Dual-uplink visibility for dedicated cluster LAX-02 (lambda.cloud.vastdata.com and nvidiadgxc.cloud.vastdata.com)

- Tenant-scoped visibility for multi-tenant cluster LAX-03 (NVIDIA-only tenant data via nvidiadgxc.cloud.vastdata.com)

- Service Aware VIP Pool concept for multi-VIP access to VMS (GUI/CLI/REST/SSH/CSI)

- Salesforce RFE hygiene: linking RFE to the correct Related Feature

- RFE 0482 for NVIDIA DGX Cloud: unified visibility across VAST clusters deployed in multiple NCPs

- Dual-uplink visibility for a dedicated cluster (LAX-02) via lambda.cloud.vastdata.com and nvidiadgxc.cloud.vastdata.com

- Tenant-scoped visibility for a multi-tenant cluster (LAX-03) via nvidiadgxc.cloud.vastdata.com

- Salesforce RFE workflow: link RFE to the correct Related Feature
## Key Decisions

- Jeff Denworth assigned Mordechai Blaunstein to lead the investigation of RFE 0482 and to bring in additional parties as needed.

- Jeff Denworth assigned Mordechai Blaunstein to take ownership of investigating RFE 0482 and to bring in additional parties as needed.