---
type: projects
title: 'RFE 0482 (NVIDIA DGX Cloud): unified visibility across NCPs, dual-uplink and tenant-scoped Uplink access'
date: '2025-12-01'
project: ORION-261324
participants:
- Brian Evans
- Jeff Denworth
- Mordechai Blaunstein
- Chuck Cancilla
- Tomer Hagay
- Alon Horev
- Paul
- Mike Slisinger
source: email
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Email/2026/2025-12-04_100559_6688_Re-RFE-Alert-RFE-0482---Existing-Feature-Enhancement-RFE-Sub.md
tags:
- type/projects
- project/orion-261324
- generated
---

# RFE 0482 (NVIDIA DGX Cloud): unified visibility across NCPs, dual-uplink and tenant-scoped Uplink access

**Date**: 2025-12-01

**Project**: [[ORION-261324]]

**Attendees**: Brian Evans, Jeff Denworth, Mordechai Blaunstein, Chuck Cancilla, Tomer Hagay, Alon Horev, Paul, Mike Slisinger

## Summary

Brian Evans alerted the PM team to RFE 0482 for NVIDIA Corporation (opportunity: "DGX-C | Coreweave") requesting unified operational visibility across VAST clusters deployed in multiple NCPs, including dual-uplink visibility for a dedicated cluster (LAX-02) and tenant-scoped visibility for a multi-tenant cluster (LAX-03). Jeff Denworth flagged the request as complex and asked Mordechai Blaunstein to drive investigation and pull in the right parties; Mordechai responded that VAST is already working on a related approach involving a new "Service Aware VIP Pool" to enable multi-VIP access to VMS interfaces, with a tentative target of VAST release 5.6 (not confirmed).


## Action Items


- [?] Open Salesforce RFE 0482 record (https://vastdata.my.salesforce.com/a6HV40000009AOL) and link the RFE to the correct Related Feature. @TBD ⏫ #task #proposed #auto

- [?] Drive technical investigation and cross-team coordination for RFE 0482 (NVIDIA DGX Cloud unified visibility, dual-uplink and tenant-scoped visibility) and involve the appropriate internal parties. @Mordechai Blaunstein ⏫ #task #proposed #auto

- [?] Confirm with Chuck Cancilla and Brian Evans whether the "Service Aware VIP Pool" approach (multi-VIP access to VMS for GUI/CLI/REST/SSH/CSI) satisfies NVIDIA DGX Cloud requirements for RFE 0482, and determine if a workaround/shortcut is required for timeline needs. @Mordechai Blaunstein ⏫ #task #proposed #auto




## Decisions


- Jeff Denworth assigned Mordechai Blaunstein to lead investigation/coordination for RFE 0482 and to bring in additional parties as needed.




## Key Information


- RFE 0482 is an "Existing Feature Enhancement" RFE associated with account NVIDIA Corporation and opportunity "DGX-C | Coreweave" (opportunity amount $0, close date 2025-11-02).

- Brian Evans approved RFE 0482 and asked the PM team to open the Salesforce RFE record and link it to the correct Related Feature.

- Sales Engineer for RFE 0482 is Chuck Cancilla.

- NVIDIA DGX Cloud Storage Team uses VAST across more than five NCPs and manages multiple petabytes of capacity, and expects continued expansion; inconsistent NCP telemetry/dashboards create fragmented visibility and operational friction.

- RFE 0482 requests dual-uplink visibility for dedicated VAST cluster LAX-02 so both lambda.cloud.vastdata.com and nvidiadgxc.cloud.vastdata.com can receive visibility into the same cluster.

- RFE 0482 requests tenant-filtered visibility for multi-tenant VAST cluster LAX-03 so nvidiadgxc.cloud.vastdata.com can access only NVIDIA DGX Cloud tenant metrics/workloads/config/health without exposing other tenants or cluster-wide information.

- Jeff Denworth stated the RFE 0482 request is "super complex" and asked Mordechai Blaunstein to take ownership and involve the appropriate parties.

- Mordechai Blaunstein said VAST is already working on similar requests from multiple CSPs and is defining a new VIP pool type called "Service Aware VIP Pool" to allow multi-VIP access to the VMS for GUI/CLI/REST/SSH/CSI; he referenced an internal wiki page and Jira ORION-261324.

- Mordechai Blaunstein indicated a tentative target to support the "Service Aware VIP Pool" work in VAST release 5.6, but explicitly noted it is not confirmed and asked whether it meets the timeline or if a shortcut/workaround is needed.




---

*Source: [[2025-12-04_100559_6688_Re-RFE-Alert-RFE-0482---Existing-Feature-Enhancement-RFE-Sub]]*
