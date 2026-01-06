---
type: projects
title: 'RFE 0482: NVIDIA DGX Cloud requests dual-uplink and tenant-scoped visibility across VAST clusters'
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
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Email/2026/2025-12-04_100559_6688_Re-RFE-Alert-RFE-0482---Existing-Feature-Enhancement-RFE-Sub.md
tags:
- type/projects
- project/rfe-0482-nvidia-dgx-cloud-unified-visibility-via-vast-uplink
- generated
---

# RFE 0482: NVIDIA DGX Cloud requests dual-uplink and tenant-scoped visibility across VAST clusters

**Date**: 2025-12-01

**Project**: [[Cloud]]

**Attendees**: Brian Evans, Jeff Denworth, Mordechai Blaunstein, Tomer Hagay, Alon Horev, Paul, Chuck Cancilla, Mike Slisinger

## Summary

Brian Evans alerted the PM team about RFE 0482 for NVIDIA Corporation (opportunity: "DGX-C | Coreweave") requesting unified operational visibility across VAST clusters deployed at multiple NCPs. Jeff Denworth flagged the request as complex and asked Mordechai Blaunstein to drive investigation and coordination. Mordechai responded that VAST is already working similar CSP requests via a new "Service Aware VIP Pool" concept (ORION-261324) to enable multi-VIP access to VMS services (GUI/CLI/REST/SSH/CSI), with a tentative target of VAST 5.6 (not confirmed).


## Action Items


- [?] Navigate to Salesforce RFE 0482 record (https://vastdata.my.salesforce.com/a6HV40000009AOL) and link the RFE to the correct Related Feature in Salesforce. @TBD ⏫ #task #proposed #auto

- [?] Lead technical investigation and coordination for RFE 0482 (dual-uplink visibility and tenant-scoped visibility for NVIDIA DGX Cloud) and bring in relevant parties as needed. @Mordechai Blaunstein ⏫ #task #proposed #auto

- [?] Confirm with Chuck Cancilla and Brian Evans whether the tentative target of supporting "Service Aware VIP Pool" in VAST 5.6 meets NVIDIA DGX Cloud timeline requirements, or whether a shortcut/workaround is required. @Mordechai Blaunstein #task #proposed #auto






## Key Information


- Brian Evans approved RFE 0482 (Existing Feature Enhancement) submitted to the VAST PM team for NVIDIA Corporation.

- RFE 0482 is associated with NVIDIA Corporation and the Salesforce opportunity "DGX-C | Coreweave" (opportunity amount $0, close date 2025-11-02).

- Sales Engineer for RFE 0482 is Chuck Cancilla.

- NVIDIA DGX Cloud Storage Team uses VAST across more than five NCPs and manages multiple petabytes, and they lack a unified visibility layer across these environments due to inconsistent NCP telemetry and dashboards.

- RFE 0482 requests dual-uplink visibility for a dedicated VAST cluster "LAX-02" so both lambda.cloud.vastdata.com and nvidiadgxc.cloud.vastdata.com can see the same cluster.

- RFE 0482 requests tenant-scoped visibility for a multi-tenant VAST cluster "LAX-03" so nvidiadgxc.cloud.vastdata.com can see only NVIDIA DGX Cloud tenant data (metrics, workloads, configuration, health) without exposing other tenants or cluster-wide information.

- Jeff Denworth stated that RFE 0482 is "super complex" and asked Mordechai Blaunstein to lead investigation and bring in relevant parties.

- Mordechai Blaunstein stated VAST is already working on similar requests from multiple CSPs and is defining a new VIP pool type called "Service Aware VIP Pool" to allow multi-VIP access to the VMS for GUI/CLI/REST/SSH/CSI; he referenced internal wiki and Jira ORION-261324.

- Mordechai Blaunstein indicated a tentative target to support the "Service Aware VIP Pool" capability in VAST release 5.6, but explicitly noted it is not confirmed.

- RFE 0482 lists potential incremental value as $100,000,000 and 10,000 PB, and is marked as not a deal blocker.




---

*Source: [[2025-12-04_100559_6688_Re-RFE-Alert-RFE-0482---Existing-Feature-Enhancement-RFE-Sub]]*
