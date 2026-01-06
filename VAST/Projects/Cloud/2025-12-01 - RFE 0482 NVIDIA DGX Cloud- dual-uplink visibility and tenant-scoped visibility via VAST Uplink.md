---
type: projects
title: 'RFE 0482 (NVIDIA DGX Cloud): dual-uplink visibility and tenant-scoped visibility via VAST Uplink'
date: '2025-12-01'
project: Cloud
participants:
- Brian Evans
- Jeff Denworth
- Mordechai Blaunstein
- Tomer Hagay
- Alon Horev
source: email
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Email/2025/2025-12-04_100559_9782_Re-RFE-Alert-RFE-0482---Existing-Feature-Enhancement-RFE-Sub.md
tags:
- type/projects
- project/rfe-0482---nvidia-dgx-cloud-unified-visibility-dual-uplink-and-tenant-scoped-visibility
- generated
---

# RFE 0482 (NVIDIA DGX Cloud): dual-uplink visibility and tenant-scoped visibility via VAST Uplink

**Date**: 2025-12-01

**Project**: [[Cloud]]

**Attendees**: Brian Evans, Jeff Denworth, Mordechai Blaunstein, Tomer Hagay, Alon Horev

## Summary

Brian Evans alerted the PM team about RFE 0482 for NVIDIA DGX Cloud requesting unified visibility across VAST clusters deployed at multiple NCPs, including dual-uplink access for a dedicated cluster and tenant-scoped visibility for a multi-tenant cluster. Jeff Denworth flagged the request as complex and asked Mordechai Blaunstein to drive it; Mordechai responded that VAST is already working on a related approach (Service Aware VIP Pool) tracked in ORION-261324 and asked whether a tentative 5.6 target meets NVIDIA's timeline.


## Action Items


- [?] Navigate to Salesforce RFE record https://vastdata.my.salesforce.com/a6HV40000009AOL and link RFE 0482 to the correct 'Related Feature' in Salesforce. @TBD ⏫ #task #proposed #auto

- [?] Lead technical investigation for RFE 0482 (dual-uplink visibility and tenant-scoped visibility via VAST Uplink) and bring in required parties across VAST engineering/product as needed. @Mordechai Blaunstein ⏫ #task #proposed #auto

- [?] Confirm with Chuck Cancilla and Brian Evans whether the proposed 'Service Aware VIP Pool' approach (ORION-261324) satisfies NVIDIA DGX Cloud requirements and whether a VAST 5.6 target (not confirmed) meets the customer timeline or if a workaround is required. @Mordechai Blaunstein ⏫ #task #proposed #auto




## Decisions


- Jeff Denworth assigned Mordechai Blaunstein to lead the technical investigation and coordination for RFE 0482.




## Key Information


- Brian Evans approved RFE 0482 (Existing Feature Enhancement) submitted to the VAST PM team for NVIDIA Corporation, associated with the opportunity 'DGX-C | Coreweave' (opportunity amount $0, close date 2025-11-02).

- RFE 0482 was submitted by Sales Engineer Chuck Cancilla and categorized as 'HPC & AI - Other/Many' for NVIDIA DGX Cloud operational visibility across VAST clusters deployed at more than five NCPs.

- NVIDIA DGX Cloud Storage Team requested dual-uplink visibility so that the dedicated VAST cluster 'LAX-02' can be visible via both uplinks 'lambda.cloud.vastdata.com' and 'nvidiadgxc.cloud.vastdata.com'.

- NVIDIA DGX Cloud requested tenant-scoped visibility for the multi-tenant VAST cluster 'LAX-03' so that 'nvidiadgxc.cloud.vastdata.com' can access only DGX Cloud tenant metrics, workloads, configuration, and health without exposing other tenants or cluster-wide information.

- Jeff Denworth stated that RFE 0482 is 'super complex' and asked Mordechai Blaunstein to lead the investigation and involve the appropriate parties.

- Mordechai Blaunstein said VAST is already working on similar requests from multiple CSPs and is defining a new VIP pool type called 'Service Aware VIP Pool' to allow multi-VIP access to the VMS for GUI/CLI/REST/SSH/CSI, tracked in Jira ORION-261324 and an internal wiki page.

- Mordechai Blaunstein indicated a tentative target to support the 'Service Aware VIP Pool' capability in VAST release 5.6, but stated it is not confirmed and asked whether it meets NVIDIA's timeline or if a shortcut/workaround is needed.




---

*Source: [[2025-12-04_100559_9782_Re-RFE-Alert-RFE-0482---Existing-Feature-Enhancement-RFE-Sub]]*
