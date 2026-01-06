---
type: projects
title: 'RFE 0482 (NVIDIA DGX Cloud): dual-uplink visibility and tenant-scoped visibility via Uplink'
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
- project/rfe-0482---nvidia-dgx-cloud-unified-visibility-dual-uplink-and-tenant-scoped-visibility
- generated
---

# RFE 0482 (NVIDIA DGX Cloud): dual-uplink visibility and tenant-scoped visibility via Uplink

**Date**: 2025-12-01

**Project**: [[Cloud]]

**Attendees**: Brian Evans, Jeff Denworth, Mordechai Blaunstein, Tomer Hagay, Alon Horev, Paul, Chuck Cancilla, Mike Slisinger

## Summary

Brian Evans alerted the PM team about RFE 0482 for NVIDIA DGX Cloud, requesting unified visibility across VAST clusters deployed at multiple NCPs, including dual-uplink access for a dedicated cluster and tenant-scoped visibility for a multi-tenant cluster. Jeff Denworth flagged the request as complex and asked Mordechai Blaunstein to drive analysis and pull in the right parties. Mordechai responded that VAST is already working on similar CSP requests via a proposed "Service Aware VIP Pool" (ORION-261324) enabling multi-VIP access to VMS services (GUI/CLI/REST/SSH/CSI), and asked whether a tentative 5.6 target meets the needed timeline or if a workaround is required.


## Action Items


- [?] Navigate to Salesforce RFE 0482 record (https://vastdata.my.salesforce.com/a6HV40000009AOL) and link the RFE to the correct Related Feature in Salesforce. @TBD ⏫ #task #proposed #auto

- [?] Lead technical/product analysis for RFE 0482 (dual-uplink visibility and tenant-scoped visibility for NVIDIA DGX Cloud) and pull in appropriate VAST stakeholders to define an approach. @Mordechai Blaunstein ⏫ #task #proposed #auto

- [?] Confirm with Chuck Cancilla and Brian Evans whether the proposed "Service Aware VIP Pool" approach (ORION-261324) satisfies NVIDIA DGX Cloud requirements and whether a workaround is needed if release 5.6 timing is not acceptable. @Mordechai Blaunstein ⏫ #task #proposed #auto




## Decisions


- Jeff Denworth assigned Mordechai Blaunstein to take ownership of analyzing RFE 0482 and to bring in additional parties as needed.




## Key Information


- RFE 0482 (Existing Feature Enhancement) was submitted to the VAST PM team for NVIDIA Corporation and approved by Brian Evans.

- RFE 0482 is linked to the Salesforce account NVIDIA Corporation and the opportunity "DGX-C | Coreweave" with opportunity amount $0 and close date 2025-11-02.

- Sales Engineer for RFE 0482 is Chuck Cancilla; use case category is "HPC & AI - Other/Many".

- NVIDIA DGX Cloud Storage Team uses VAST across more than five NCPs and manages multiple petabytes of capacity, but lacks a unified view because each NCP provides telemetry and dashboards differently.

- RFE 0482 requests dual-uplink visibility for a dedicated VAST cluster LAX-02 so that both lambda.cloud.vastdata.com and nvidiadgxc.cloud.vastdata.com can receive visibility into the same cluster.

- RFE 0482 requests tenant-scoped visibility for a multi-tenant VAST cluster LAX-03 so that nvidiadgxc.cloud.vastdata.com can access only DGX Cloud tenant data (metrics, workloads, configurations, health) without exposing other tenants or cluster-wide information.

- RFE 0482 states the feature is not a deal blocker and claims potential incremental value of $100,000,000 and 10,000 PB.

- Jeff Denworth characterized RFE 0482 as "super complex" and asked Mordechai Blaunstein to lead and involve appropriate parties.

- Mordechai Blaunstein stated VAST is already working on similar requests from multiple CSPs and is defining a new VIP pool type called "Service Aware VIP Pool" to allow multi-VIP access to VMS services (GUI/CLI/REST/SSH/CSI).

- Mordechai Blaunstein referenced internal documentation and Jira ORION-261324 for the "Service Aware VIP Pool" work and noted a tentative target of VAST release 5.6 that is not confirmed.




---

*Source: [[2025-12-04_100559_9782_Re-RFE-Alert-RFE-0482---Existing-Feature-Enhancement-RFE-Sub]]*
