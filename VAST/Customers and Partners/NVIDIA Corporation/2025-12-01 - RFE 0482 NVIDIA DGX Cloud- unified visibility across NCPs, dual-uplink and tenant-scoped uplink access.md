---
type: customer
title: 'RFE 0482 (NVIDIA DGX Cloud): unified visibility across NCPs, dual-uplink and tenant-scoped uplink access'
date: '2025-12-01'
account: NVIDIA Corporation
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
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Email/2025/2025-12-04_100559_9782_Re-RFE-Alert-RFE-0482---Existing-Feature-Enhancement-RFE-Sub.md
tags:
- type/customer
- account/nvidia-corporation
- generated
---

# RFE 0482 (NVIDIA DGX Cloud): unified visibility across NCPs, dual-uplink and tenant-scoped uplink access

**Date**: 2025-12-01

**Account**: [[NVIDIA Corporation]]

**Attendees**: Brian Evans, Jeff Denworth, Mordechai Blaunstein, Chuck Cancilla, Tomer Hagay, Alon Horev, Paul, Mike Slisinger

## Summary

Brian Evans alerted the PM team about RFE 0482 for NVIDIA DGX Cloud, requesting unified operational visibility across VAST clusters deployed in multiple NCPs. The RFE specifically asks for dual-uplink visibility for a dedicated cluster (LAX-02) and tenant-scoped visibility for a multi-tenant cluster (LAX-03). Jeff Denworth flagged the request as complex and asked Mordechai Blaunstein to drive investigation and pull in the right parties; Mordechai responded with an existing related effort (Service Aware VIP Pool) and asked whether a 5.6 target timeline works or if a workaround is needed.


## Action Items


- [?] Navigate to Salesforce RFE record https://vastdata.my.salesforce.com/a6HV40000009AOL and link RFE 0482 to the correct 'Related Feature' field. @TBD ⏫ #task #proposed #auto

- [?] Investigate RFE 0482 technical requirements (dual-uplink visibility for LAX-02 and tenant-filtered visibility for LAX-03) and coordinate with the necessary internal teams to propose an implementation approach. @Mordechai Blaunstein ⏫ #task #proposed #auto

- [?] Confirm with Chuck Cancilla and Brian Evans whether the 'Service Aware VIP Pool' approach (tracked in ORION-261324) satisfies the NVIDIA DGX Cloud RFE 0482 requirements, and collect any additional feedback or constraints. @Mordechai Blaunstein #task #proposed #auto

- [?] Validate timeline expectations for delivering the RFE 0482 capability, specifically whether targeting VAST release 5.6 (not confirmed) is acceptable or whether a shortcut or workaround is required. @Mordechai Blaunstein ⏫ #task #proposed #auto




## Decisions


- Jeff Denworth assigned Mordechai Blaunstein to take ownership of investigating RFE 0482 and to bring in additional parties as needed.




## Key Information


- RFE 0482 is an 'Existing Feature Enhancement' request associated with the account NVIDIA Corporation and the opportunity 'DGX-C | Coreweave' in Salesforce.

- RFE 0482 was submitted to the VAST PM team and approved by Brian Evans.

- Sales Engineer for RFE 0482 is Chuck Cancilla.

- NVIDIA DGX Cloud Storage Team uses VAST across more than five NCPs and manages multiple petabytes of capacity, but lacks a unified view because each NCP provides telemetry and dashboards differently.

- For dedicated VAST cluster LAX-02 (single-tenant, DGX Cloud only), NVIDIA requests dual-uplink visibility so both lambda.cloud.vastdata.com and nvidiadgxc.cloud.vastdata.com can see the same cluster.

- For multi-tenant VAST cluster LAX-03, NVIDIA requests tenant-filtered visibility so nvidiadgxc.cloud.vastdata.com can access only the DGX Cloud tenant data (metrics, workloads, configurations, health) without exposing other tenants or cluster-wide information.

- Jeff Denworth stated the RFE 0482 request is 'super complex' and asked Mordechai Blaunstein to lead investigation and involve appropriate parties.

- Mordechai Blaunstein indicated VAST is already working on similar requests from multiple CSPs and is defining a new VIP pool type called 'Service Aware VIP Pool' to allow multi-VIP access to VMS for GUI, CLI, REST, SSH, and CSI.

- Mordechai Blaunstein referenced internal tracking for the related work: Confluence page https://vastdata.atlassian.net/wiki/x/lQDInQE and Jira ticket ORION-261324.




---

*Source: [[2025-12-04_100559_9782_Re-RFE-Alert-RFE-0482---Existing-Feature-Enhancement-RFE-Sub]]*
