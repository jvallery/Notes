---
type: customer
title: 'RFE 0482 (NVIDIA DGX Cloud): unified multi-cluster visibility, dual-uplink and tenant-scoped views'
date: '2025-12-01'
account: NVIDIA Corporation
participants:
- Brian Evans
- Jeff Denworth
- Mordechai Blaunstein
- Chuck Cancilla
- Alon Horev
- Tomer Hagay
- Paul
- Mike Slisinger
source: email
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Email/2026/2025-12-04_100559_6688_Re-RFE-Alert-RFE-0482---Existing-Feature-Enhancement-RFE-Sub.md
tags:
- type/customer
- account/nvidia-corporation
- generated
---

# RFE 0482 (NVIDIA DGX Cloud): unified multi-cluster visibility, dual-uplink and tenant-scoped views

**Date**: 2025-12-01

**Account**: [[NVIDIA Corporation]]

**Attendees**: Brian Evans, Jeff Denworth, Mordechai Blaunstein, Chuck Cancilla, Alon Horev, Tomer Hagay, Paul, Mike Slisinger

## Summary

Brian Evans alerted the PM team that RFE 0482 for NVIDIA Corporation was submitted and approved, requesting enhanced VAST Uplink visibility across DGX Cloud clusters deployed in multiple NCPs. Jeff Denworth flagged the request as complex and asked Mordechai Blaunstein to lead investigation and pull in the right parties. Mordechai responded that VAST is already working on a similar approach (Service Aware VIP Pool enabling multi-VIP access) and asked whether a tentative 5.6 target meets NVIDIA's timeline or if a workaround is needed.


## Action Items


- [?] Navigate to Salesforce RFE 0482 (https://vastdata.my.salesforce.com/a6HV40000009AOL) and link the RFE to the correct 'Related Feature' record in Salesforce. @TBD ⏫ #task #proposed #auto

- [?] Lead technical investigation of RFE 0482 (NVIDIA DGX Cloud multi-cluster visibility, dual-uplink and tenant-scoped visibility) and bring in required VAST parties to define approach and feasibility. @Mordechai Blaunstein ⏫ #task #proposed #auto

- [?] Review existing internal proposal for 'Service Aware VIP Pool' (https://vastdata.atlassian.net/wiki/x/lQDInQE) and ORION-261324 to assess fit for NVIDIA RFE 0482 requirements and identify gaps. @Mordechai Blaunstein ⏫ #task #proposed #auto

- [?] Confirm with Chuck Cancilla and Brian Evans whether a tentative target of VAST release 5.6 (not confirmed) meets NVIDIA DGX Cloud timeline expectations, or whether a shortcut/workaround is required. @Mordechai Blaunstein ⏫ #task #proposed #auto




## Decisions


- Jeff Denworth assigned Mordechai Blaunstein to lead the investigation of RFE 0482 and to bring in additional parties as needed.




## Key Information


- Brian Evans approved RFE 0482 (Existing Feature Enhancement) submitted to the VAST PM team for NVIDIA Corporation (DGX Cloud).

- RFE 0482 is associated with NVIDIA Corporation and the opportunity 'DGX-C | Coreweave' (opportunity amount $0, close date 2025-11-02).

- Chuck Cancilla is the Sales Engineer listed on RFE 0482 for NVIDIA DGX Cloud visibility enhancements.

- NVIDIA DGX Cloud Storage Team uses VAST across more than five NCPs and manages multiple petabytes of capacity, but lacks a unified operational view due to inconsistent telemetry and dashboards per NCP.

- RFE 0482 requests dual-uplink visibility for a dedicated VAST cluster 'LAX-02', allowing both lambda.cloud.vastdata.com and nvidiadgxc.cloud.vastdata.com to see the same cluster.

- RFE 0482 requests tenant-scoped visibility for a multi-tenant VAST cluster 'LAX-03', so nvidiadgxc.cloud.vastdata.com can access only NVIDIA DGX Cloud tenant metrics/workloads/config/health without exposing other tenants or cluster-wide information.

- Jeff Denworth assessed RFE 0482 as 'super complex' and asked Mordechai Blaunstein to lead investigation and involve appropriate parties.

- Mordechai Blaunstein stated VAST is already working on similar requests from multiple CSPs and is defining a new VIP pool type called 'Service Aware VIP Pool' to allow multi-VIP access to VMS for GUI/CLI/REST/SSH/CSI.

- Mordechai Blaunstein indicated tentative targeting for the 'Service Aware VIP Pool' work in VAST release 5.6, but stated it is not confirmed and asked whether it meets NVIDIA's timeline or if a workaround is needed.

- RFE 0482 lists estimated incremental value of $100,000,000 and 10,000 PB, and is marked 'Deal Blocker: No'.




---

*Source: [[2025-12-04_100559_6688_Re-RFE-Alert-RFE-0482---Existing-Feature-Enhancement-RFE-Sub]]*
