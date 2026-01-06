---
type: projects
title: 'RFE 0482 (NVIDIA DGX Cloud): multi-uplink and tenant-scoped visibility via VAST Uplink'
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
- Mike Slisinger
source: email
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Email/2025/2025-12-04_100559_9782_Re-RFE-Alert-RFE-0482---Existing-Feature-Enhancement-RFE-Sub.md
tags:
- type/projects
- project/cloud
- generated
---

# RFE 0482 (NVIDIA DGX Cloud): multi-uplink and tenant-scoped visibility via VAST Uplink

**Date**: 2025-12-01

**Project**: [[Cloud]]

**Attendees**: Brian Evans, Jeff Denworth, Mordechai Blaunstein, Tomer Hagay, Alon Horev, Paul, Chuck Cancilla, Mike Slisinger

## Summary

Brian Evans alerted the PM team about RFE 0482 for NVIDIA Corporation requesting unified operational visibility across VAST clusters deployed in multiple NCPs, including dual-uplink access for a dedicated cluster and tenant-scoped visibility for a multi-tenant cluster. Jeff Denworth flagged the request as complex and asked Mordechai Blaunstein to drive investigation and coordination. Mordechai responded that VAST is already working on similar CSP requests via a new "Service Aware VIP Pool" concept (Jira ORION-261324) enabling multi-VIP access to VMS services (GUI/CLI/REST/SSH/CSI), with a tentative target of VAST release 5.6 (not confirmed).


## Action Items


- [?] Navigate to Salesforce RFE 0482 record (https://vastdata.my.salesforce.com/a6HV40000009AOL) and link the RFE to the correct Related Feature in Salesforce. @TBD ⏫ #task #proposed #auto

- [?] Review RFE 0482 requirements (dual-uplink visibility for LAX-02 and tenant-scoped visibility for LAX-03) and align them with the "Service Aware VIP Pool" approach tracked in Jira ORION-261324; confirm whether the approach satisfies NVIDIA DGX Cloud needs. @Mordechai Blaunstein ⏫ #task #proposed #auto

- [?] Confirm with Chuck Cancilla and Brian Evans whether a tentative target of VAST release 5.6 (not confirmed) meets NVIDIA DGX Cloud timeline needs for RFE 0482, or whether a shortcut or workaround is required. @Mordechai Blaunstein ⏫ #task #proposed #auto




## Decisions


- Mordechai Blaunstein will drive investigation and coordination for RFE 0482 due to its complexity, bringing in additional parties as needed.




## Key Information


- RFE 0482 is an "Existing Feature Enhancement" request associated with NVIDIA Corporation and the Salesforce opportunity "DGX-C | Coreweave" (opportunity amount $0, close date 2025-11-02).

- RFE 0482 was submitted to the VAST PM team and approved by Brian Evans.

- The NVIDIA DGX Cloud Storage Team uses VAST across more than five NCPs and manages multiple petabytes of capacity, and they lack a unified view of telemetry and dashboards across those environments.

- RFE 0482 requests dual-uplink visibility for a dedicated VAST cluster named LAX-02 so that both lambda.cloud.vastdata.com and nvidiadgxc.cloud.vastdata.com can access visibility into the same cluster.

- RFE 0482 requests tenant-scoped visibility for a multi-tenant VAST cluster named LAX-03 so that nvidiadgxc.cloud.vastdata.com can see only the NVIDIA DGX Cloud tenant data (metrics, workloads, configurations, health) without exposing other tenants or cluster-wide information.

- RFE 0482 is marked as not a deal blocker and includes an estimated incremental value of $100,000,000 and 10,000 PB associated with the request.

- Jeff Denworth stated that RFE 0482 is "super complex" and asked Mordechai Blaunstein to take ownership and involve additional parties as needed.

- Mordechai Blaunstein stated VAST is already working on similar requests from multiple CSPs and is defining a new VIP pool type called "Service Aware VIP Pool" to allow multi-VIP access to VMS services (GUI/CLI/REST/SSH/CSI).

- Mordechai Blaunstein referenced internal documentation and tracking for the "Service Aware VIP Pool" work in Atlassian wiki and Jira ticket ORION-261324.

- Mordechai Blaunstein indicated a tentative target to support the "Service Aware VIP Pool" capability in VAST release 5.6, but explicitly noted it is not confirmed.




---

*Source: [[2025-12-04_100559_9782_Re-RFE-Alert-RFE-0482---Existing-Feature-Enhancement-RFE-Sub]]*
