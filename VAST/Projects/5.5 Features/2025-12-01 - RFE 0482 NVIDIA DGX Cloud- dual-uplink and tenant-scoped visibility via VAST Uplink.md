---
type: "projects"
title: "RFE 0482 (NVIDIA DGX Cloud): dual-uplink and tenant-scoped visibility via VAST Uplink"
date: "2025-12-01"
project: ""
participants: ["Brian Moore", "Jeff Denworth", "Mordechai Blaunstein", "Chuck Cancilla", "Brian Evans", "Alon Horev", "Tomer Hagay", "Paul Libenson", "Mike Slisinger"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Email/2025/2025-12-04_100559_9782_Re-RFE-Alert-RFE-0482---Existing-Feature-Enhancement-RFE-Sub.md"
tags:
  - "type/projects"
  - "project/"
  - "generated"

---

# RFE 0482 (NVIDIA DGX Cloud): dual-uplink and tenant-scoped visibility via VAST Uplink

**Date**: 2025-12-01
**Project**: [[]]
**Attendees**: Brian Moore, Jeff Denworth, Mordechai Blaunstein, Chuck Cancilla, Brian Evans, Alon Horev, Tomer Hagay, Paul Libenson, Mike Slisinger

## Summary

An RFE (0482) was submitted for NVIDIA DGX Cloud requesting unified visibility across VAST clusters deployed at multiple NCPs, including dual-uplink visibility for a dedicated cluster (LAX-02) and tenant-scoped visibility for a multi-tenant cluster (LAX-03). Jeff Denworth flagged the request as complex and asked Mordechai Blaunstein to drive investigation and coordination. Mordechai responded that VAST is already working on a similar solution (Service Aware VIP Pool, ORION-261324) and asked whether a tentative 5.6 target meets NVIDIA's timeline or if a workaround is needed.


## Action Items


- [?] Navigate to Salesforce RFE record https://vastdata.my.salesforce.com/a6HV40000009AOL and link RFE 0482 to the correct Related Feature. @TBD ⏫ #task #proposed #auto

- [?] Lead technical investigation for RFE 0482 (dual-uplink visibility and tenant-scoped visibility for VAST Uplink) and pull in required stakeholders across PM and engineering. @Mordechai Blaunstein ⏫ #task #proposed #auto

- [?] Confirm with Chuck Cancilla and Brian Evans whether the tentative target of supporting the Service Aware VIP Pool capability in VAST release 5.6 meets NVIDIA DGX Cloud timeline, or whether a shortcut/workaround is required. @Mordechai Blaunstein ⏫ #task #proposed #auto




## Decisions


- Jeff Denworth assigned Mordechai Blaunstein to lead investigation and coordination for RFE 0482 and to bring in additional parties as needed.




## Key Information


- RFE 0482 was submitted to the VAST PM team for NVIDIA Corporation and was approved by Brian Evans.

- RFE 0482 is categorized as an Existing Feature Enhancement and the Sales Engineer listed is Chuck Cancilla.

- NVIDIA DGX Cloud Storage Team uses VAST across more than five NCPs and manages multiple petabytes of capacity, and expects continued expansion.

- RFE 0482 requests dual-uplink visibility for a dedicated VAST cluster named LAX-02 so that both lambda.cloud.vastdata.com and nvidiadgxc.cloud.vastdata.com can receive visibility into the same cluster.

- RFE 0482 requests tenant-filtered visibility for a multi-tenant VAST cluster named LAX-03 so that nvidiadgxc.cloud.vastdata.com can access only NVIDIA DGX Cloud tenant data without exposing other tenants or cluster-wide information.

- The RFE states it is not a deal blocker and claims potential incremental value of $100,000,000 and 10,000 PB associated with the request.

- Jeff Denworth assessed RFE 0482 as 'super complex' and asked Mordechai Blaunstein to take ownership and involve additional parties as needed.

- Mordechai Blaunstein stated VAST is already working on similar requests from multiple CSPs and referenced a proposed solution: a new VIP pool type called 'Service Aware VIP Pool' enabling multi-VIP access to VMS for GUI, CLI, REST, SSH, and CSI.

- Mordechai Blaunstein referenced internal tracking for the solution in Atlassian as ORION-261324 and a related Confluence page (https://vastdata.atlassian.net/wiki/x/lQDInQE).

- Mordechai Blaunstein indicated a tentative target to support the Service Aware VIP Pool capability in VAST release 5.6, but explicitly noted it is not confirmed.



---

*Source: [[2025-12-04_100559_9782_Re-RFE-Alert-RFE-0482---Existing-Feature-Enhancement-RFE-Sub]]*