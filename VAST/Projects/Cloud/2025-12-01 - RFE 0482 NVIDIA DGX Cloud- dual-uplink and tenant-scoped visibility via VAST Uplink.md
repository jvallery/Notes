---
type: projects
title: 'RFE 0482 (NVIDIA DGX Cloud): dual-uplink and tenant-scoped visibility via VAST Uplink'
date: '2025-12-01'
project: Cloud
participants:
- Brian Evans
- Jeff Denworth
- Mordechai Blaunstein
- Tomer Hagay
- Alon Horev
- Paul
- Chuck Cancilla
source: email
source_ref: /Users/jason.vallery/Documents/Notes/Inbox/Email/2025-12-04_100559_6688_Re-RFE-Alert-RFE-0482---Existing-Feature-Enhancement-RFE-Sub.md
tags:
- type/projects
- project/cloud
- generated
---

# RFE 0482 (NVIDIA DGX Cloud): dual-uplink and tenant-scoped visibility via VAST Uplink

**Date**: 2025-12-01

**Project**: [[Cloud]]

**Attendees**: Brian Evans, Jeff Denworth, Mordechai Blaunstein, Tomer Hagay, Alon Horev, Paul, Chuck Cancilla

## Summary

Brian Evans alerted the PM team about RFE 0482 for NVIDIA DGX Cloud requesting unified visibility across VAST clusters deployed at multiple NCPs, including dual-uplink visibility for a dedicated cluster and tenant-scoped visibility for a multi-tenant cluster. Jeff Denworth flagged the request as complex and asked Mordechai Blaunstein to drive investigation and pull in the right parties. Mordechai responded that VAST is already working on a similar approach (Service Aware VIP Pool, ORION-261324) and asked whether a tentative 5.6 target meets NVIDIA's timeline or if a workaround is needed.


## Action Items


- [?] Navigate to Salesforce RFE record https://vastdata.my.salesforce.com/a6HV40000009AOL and link RFE 0482 to the correct 'Related Feature' in Salesforce. @TBD ⏫ #task #proposed #auto

- [?] Lead investigation of RFE 0482 (NVIDIA DGX Cloud dual-uplink and tenant-scoped visibility) and involve appropriate internal parties to assess feasibility and approach. @Mordechai Blaunstein ⏫ #task #proposed #auto

- [?] Confirm with Chuck Cancilla and Brian Evans whether the proposed 'Service Aware VIP Pool' approach (ORION-261324) addresses NVIDIA DGX Cloud requirements and gather any additional feedback or constraints. @Mordechai Blaunstein #task #proposed #auto

- [?] Determine whether a tentative target of VAST release 5.6 (not confirmed) meets NVIDIA DGX Cloud timeline expectations for RFE 0482, or identify a shortcut/workaround if needed. @Mordechai Blaunstein ⏫ #task #proposed #auto




## Decisions


- Jeff Denworth assigned Mordechai Blaunstein to lead the investigation of RFE 0482 and to bring in additional parties as needed.




## Key Information


- Brian Evans approved RFE 0482 (Existing Feature Enhancement) submitted to the VAST PM team for NVIDIA Corporation.

- RFE 0482 is associated with NVIDIA Corporation and the opportunity 'DGX-C | Coreweave' (opportunity amount listed as 0, close date 2025-11-02).

- Sales Engineer for RFE 0482 is Chuck Cancilla.

- NVIDIA DGX Cloud Storage Team uses VAST across more than five NCPs and manages multiple petabytes of capacity, and they lack a unified view across these environments due to inconsistent telemetry and dashboards per NCP.

- RFE 0482 request component 1: allow dual-uplink visibility so both lambda.cloud.vastdata.com and nvidiadgxc.cloud.vastdata.com can receive visibility into the same dedicated VAST cluster LAX-02 (single-tenant DGX Cloud).

- RFE 0482 request component 2: enable tenant-filtered visibility so NVIDIA's uplink nvidiadgxc.cloud.vastdata.com can see only DGX Cloud tenant data from multi-tenant cluster LAX-03 without exposing other tenants or cluster-wide information.

- Jeff Denworth assessed RFE 0482 as 'super complex' and asked Mordechai Blaunstein to lead investigation and involve appropriate parties.

- Mordechai Blaunstein stated VAST is already working on similar requests from multiple CSPs and is defining a new VIP pool type called 'Service Aware VIP Pool' to allow multi-VIP access to VMS for GUI/CLI/REST/SSH/CSI.

- Mordechai Blaunstein referenced internal tracking for the approach: ORION-261324 and an internal wiki page (vastdata.atlassian.net/wiki/x/lQDInQE).

- Mordechai Blaunstein indicated a tentative target to support the Service Aware VIP Pool approach in VAST release 5.6, but stated it is not confirmed.




---

*Source: [[2025-12-04_100559_6688_Re-RFE-Alert-RFE-0482---Existing-Feature-Enhancement-RFE-Sub]]*
