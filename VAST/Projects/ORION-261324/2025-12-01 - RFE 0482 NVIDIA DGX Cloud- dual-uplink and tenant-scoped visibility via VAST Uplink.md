---
type: projects
title: 'RFE 0482 (NVIDIA DGX Cloud): dual-uplink and tenant-scoped visibility via VAST Uplink'
date: '2025-12-01'
project: ORION-261324
participants:
- Brian Evans
- Jeff Denworth
- Mordechai Blaunstein
- Alon Horev
- Tomer Hagay
- Paul
- Chuck Cancilla
- Mike Slisinger
source: email
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Email/2026/2025-12-04_100559_6688_Re-RFE-Alert-RFE-0482---Existing-Feature-Enhancement-RFE-Sub.md
tags:
- type/projects
- project/orion-261324
- generated
---

# RFE 0482 (NVIDIA DGX Cloud): dual-uplink and tenant-scoped visibility via VAST Uplink

**Date**: 2025-12-01

**Project**: [[ORION-261324]]

**Attendees**: Brian Evans, Jeff Denworth, Mordechai Blaunstein, Alon Horev, Tomer Hagay, Paul, Chuck Cancilla, Mike Slisinger

## Summary

Brian Evans forwarded RFE 0482 for NVIDIA Corporation (DGX-C | Coreweave) requesting unified operational visibility across VAST clusters deployed at multiple NCPs. The RFE specifically asks for dual-uplink visibility for a dedicated cluster (LAX-02) and tenant-scoped visibility for a multi-tenant cluster (LAX-03). Jeff Denworth flagged the request as complex and asked Mordechai Blaunstein to drive investigation; Mordechai pointed to an in-flight approach using a new "Service Aware VIP Pool" (ORION-261324) enabling multi-VIP access to VMS services (GUI/CLI/REST/SSH/CSI).


## Action Items


- [?] Open Salesforce RFE record https://vastdata.my.salesforce.com/a6HV40000009AOL and link RFE 0482 to the correct Related Feature in Salesforce. @TBD ⏫ #task #proposed #auto

- [?] Investigate RFE 0482 technical feasibility and approach for dual-uplink visibility (LAX-02) and tenant-scoped visibility (LAX-03), and bring in required VAST stakeholders to drive solution definition. @Mordechai Blaunstein ⏫ #task #proposed #auto

- [?] Review proposed "Service Aware VIP Pool" design (wiki link https://vastdata.atlassian.net/wiki/x/lQDInQE and Jira ORION-261324) and provide feedback on whether it meets NVIDIA DGX Cloud timeline needs or if a workaround/shortcut is required. @Chuck Cancilla #task #proposed #auto

- [?] Review proposed "Service Aware VIP Pool" design (wiki link https://vastdata.atlassian.net/wiki/x/lQDInQE and Jira ORION-261324) and provide feedback on whether it meets NVIDIA DGX Cloud timeline needs or if a workaround/shortcut is required. @Brian Evans #task #proposed #auto




## Decisions


- Jeff Denworth assigned Mordechai Blaunstein to take ownership of investigating RFE 0482 and to pull in additional parties as needed.




## Key Information


- RFE 0482 is associated with NVIDIA Corporation and the opportunity "DGX-C | Coreweave" (opportunity amount $0, close date 2025-11-02).

- NVIDIA DGX Cloud Storage Team uses VAST across more than five NCPs and manages multiple petabytes of capacity, and expects continued expansion.

- RFE 0482 requests dual-uplink visibility so both lambda.cloud.vastdata.com and nvidiadgxc.cloud.vastdata.com can access the same dedicated VAST cluster LAX-02 (single-tenant DGX Cloud deployment).

- RFE 0482 requests tenant-scoped visibility so nvidiadgxc.cloud.vastdata.com can see only the NVIDIA DGX Cloud tenant data inside multi-tenant cluster LAX-03, without exposing other tenants or cluster-wide information.

- The RFE value proposition claims incremental value of $100,000,000 and 10,000 PB if the requested visibility capability is delivered.

- Jeff Denworth stated the NVIDIA RFE 0482 request is "super complex" and asked Mordechai Blaunstein to lead investigation and involve appropriate parties.

- Mordechai Blaunstein said VAST is already working on similar requests from multiple CSPs and is defining a new VIP pool type called "Service Aware VIP Pool" to allow multi-VIP access to the VMS for GUI/CLI/REST/SSH/CSI; he referenced Jira ORION-261324 and an internal wiki page.

- Brian Evans requested the PM team navigate to the Salesforce RFE record and link RFE 0482 to the correct related feature.




---

*Source: [[2025-12-04_100559_6688_Re-RFE-Alert-RFE-0482---Existing-Feature-Enhancement-RFE-Sub]]*
