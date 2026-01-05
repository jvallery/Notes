---
type: people
title: 'RFE 0482 (NVIDIA DGX Cloud): unified visibility across NCPs, dual-uplink and tenant-scoped visibility'
date: '2025-12-01'
participants:
- Brian Evans
- Jeff Denworth
- Mordechai Blaunstein
- Chuck Cancilla
- Paul Libenson
- Tomer Hagay
- Alon Horev
- Mike Slisinger
source: transcript
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Email/2025/2025-12-04_100559_9782_Re-RFE-Alert-RFE-0482---Existing-Feature-Enhancement-RFE-Sub.md
tags:
- type/people
- generated
person: Brian Evans
---

# RFE 0482 (NVIDIA DGX Cloud): unified visibility across NCPs, dual-uplink and tenant-scoped visibility

**Date**: 2025-12-01
**Attendees**: Brian Evans, Jeff Denworth, Mordechai Blaunstein, Chuck Cancilla, Paul Libenson, Tomer Hagay, Alon Horev, Mike Slisinger

## Summary

VAST PM received RFE 0482 from NVIDIA DGX Cloud Storage Team requesting a unified visibility layer across VAST clusters deployed at multiple NCPs, including dual-uplink visibility for a dedicated cluster (LAX-02) and tenant-scoped visibility for a multi-tenant cluster (LAX-03). Jeff Denworth flagged the request as complex and asked Mordechai Blaunstein to lead, who pointed to an in-flight approach: a new Service Aware VIP Pool enabling multi-VIP access to VMS interfaces (GUI/CLI/REST/SSH/CSI), tracked in ORION-261324.

## Action Items

- [?] Navigate to Salesforce RFE record https://vastdata.my.salesforce.com/a6HV40000009AOL and link RFE 0482 to the correct Related Feature in Salesforce. @TBD ⏫ #task #proposed #auto

- [?] Drive technical investigation and cross-team coordination for RFE 0482 (NVIDIA DGX Cloud unified visibility, dual-uplink and tenant-scoped visibility) and bring in required parties. @Mordechai Blaunstein ⏫ #task #proposed #auto

- [?] Confirm with Chuck Cancilla and Brian Evans whether the proposed "Service Aware VIP Pool" (multi-VIP access) approach satisfies NVIDIA DGX Cloud requirements for RFE 0482, and whether the tentative VAST 5.6 target meets NVIDIA timing or if a workaround is needed. @Mordechai Blaunstein ⏫ #task #proposed #auto

- [?] Navigate to Salesforce RFE 0482 record (https://vastdata.my.salesforce.com/a6HV40000009AOL) and link the RFE to the correct Related Feature in Salesforce. @TBD ⏫ #task #proposed #auto

- [?] Lead technical investigation and cross-team coordination for NVIDIA RFE 0482 (dual-uplink visibility for LAX-02 and tenant-scoped visibility for LAX-03), bringing in required parties. @Mordechai Blaunstein ⏫ #task #proposed #auto

- [?] Confirm with Chuck Cancilla and Brian Evans whether the in-flight 'Service Aware VIP Pool' approach (ORION-261324) satisfies NVIDIA RFE 0482 requirements and whether the (unconfirmed) 5.6 target timeline is acceptable or if a workaround is needed. @Mordechai Blaunstein ⏫ #task #proposed #auto

## Decisions

- Jeff Denworth assigned Mordechai Blaunstein to drive investigation and coordination for RFE 0482 due to complexity.

- Jeff Denworth assigned Mordechai Blaunstein to lead investigation and coordination for NVIDIA RFE 0482 due to complexity.

## Key Information

- RFE 0482 (Existing Feature Enhancement) was submitted to the VAST PM team for NVIDIA Corporation and approved by Brian Evans.

- RFE 0482 is associated with the NVIDIA Corporation account and the opportunity "DGX-C | Coreweave" (opportunity amount listed as 0; close date 2025-11-02).

- Chuck Cancilla is the Sales Engineer listed on RFE 0482 for NVIDIA Corporation.

- NVIDIA DGX Cloud Storage Team uses VAST across more than five NCPs and manages multiple petabytes of capacity, and expects continued expansion; inconsistent NCP telemetry/dashboards create fragmented visibility and operational friction.

- RFE 0482 requests dual-uplink visibility for a dedicated VAST cluster "LAX-02" so that both lambda.cloud.vastdata.com and nvidiadgxc.cloud.vastdata.com can receive visibility into the same cluster.

- RFE 0482 requests tenant-scoped visibility for a multi-tenant VAST cluster "LAX-03" so that nvidiadgxc.cloud.vastdata.com can access only NVIDIA DGX Cloud tenant data (metrics, workloads, configurations, health) without exposing other tenants or cluster-wide information.

- Jeff Denworth stated the RFE 0482 request is "super complex" and asked Mordechai Blaunstein to take ownership and involve the appropriate parties.

- Mordechai Blaunstein indicated VAST is already working on similar requests from multiple CSPs and is defining a new VIP pool type called "Service Aware VIP Pool" to allow multi-VIP access to VMS for GUI/CLI/REST/SSH/CSI.

- Mordechai Blaunstein referenced an internal Confluence page and Jira ticket ORION-261324 for the "Service Aware VIP Pool" work and noted a tentative target of VAST 5.6 that is not confirmed.

- RFE 0482 lists an estimated incremental value of $100,000,000 and 10,000 PB associated with the requested capability.

---

- RFE 0482 was submitted to the VAST PM team for NVIDIA Corporation and approved by Brian Evans.

- The RFE 0482 Salesforce record link is https://vastdata.my.salesforce.com/a6HV40000009AOL.

- RFE 0482 is categorized as an Existing Feature Enhancement with use case category 'HPC & AI - Other/Many'.

- Chuck Cancilla is the Sales Engineer associated with RFE 0482 for NVIDIA Corporation.

- NVIDIA DGX Cloud Storage Team uses VAST across more than five NCPs and manages multiple petabytes of capacity, and expects continued expansion.

- NVIDIA DGX Cloud reports inconsistent telemetry and dashboards across NCPs, which complicates troubleshooting and platform maintenance for VAST clusters.

- RFE 0482 requests dual-uplink visibility for a dedicated VAST cluster named LAX-02 so that both lambda.cloud.vastdata.com and nvidiadgxc.cloud.vastdata.com can see the same cluster.

- RFE 0482 requests tenant-scoped visibility for a multi-tenant VAST cluster named LAX-03 so that nvidiadgxc.cloud.vastdata.com can access only NVIDIA DGX Cloud tenant metrics, workloads, configurations, and health without exposing other tenants or cluster-wide information.

- RFE 0482 is marked as 'Deal Blocker: No' in the submission.

- The RFE submission claims potential incremental value of $100,000,000 and 10,000 PB associated with delivering the requested capability.

- Jeff Denworth stated the NVIDIA RFE 0482 request is 'super complex' and asked Mordechai Blaunstein to lead and involve appropriate parties.

- Mordechai Blaunstein indicated VAST is already working on similar requests from multiple CSPs and referenced an approach defining a new VIP pool type called 'Service Aware VIP Pool' to allow multi-VIP access to VMS interfaces (GUI/CLI/REST/SSH/CSI).

- Mordechai Blaunstein referenced internal tracking for the approach in ORION-261324 and a Confluence page https://vastdata.atlassian.net/wiki/x/lQDInQE.

- Mordechai Blaunstein stated the Service Aware VIP Pool work is targeting VAST release 5.6, but the timeline is not confirmed.
