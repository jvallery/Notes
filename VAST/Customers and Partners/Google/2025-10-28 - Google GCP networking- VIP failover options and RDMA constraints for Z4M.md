---
type: "customer"
title: "Google GCP networking: VIP failover options and RDMA constraints for Z4M"
date: "2025-10-28"
account: ""
participants: ["Asaf Levy", "Billy Kettler", "Eirikur Hrafnsson", "Jonsi Stephenson", "Karl Vietmeier", "Lior Genzel", "Mordechai Blaunstein", "Olivia Bouree", "Ronnie Lazar", "Tomer Hagay", "Ben (Google PM, last name unknown)", "Unknown Google contact (bengit@google.com)", "Unknown Google contact (bobnapaa@google.com)", "Unknown Google contact (fanyanf@google.com)", "Unknown Google contact (hildebrand@google.com)", "Unknown Google contact (iraoren@google.com)", "Unknown Google contact (johndowney@google.com)", "Unknown Google contact (shengqiu@google.com)", "Unknown Google contact (wpien@google.com)", "Unknown Google contact (yardenh@google.com)", "Unknown Google contact (yevgenik@google.com)"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-28 - The teams discussed IP management and failover approaches on GCP (alias IPs, rou.md"
tags:
  - "type/customer"
  - "account/"
  - "generated"

---

# Google GCP networking: VIP failover options and RDMA constraints for Z4M

**Date**: 2025-10-28
**Account**: [[]]
**Attendees**: Asaf Levy, Billy Kettler, Eirikur Hrafnsson, Jonsi Stephenson, Karl Vietmeier, Lior Genzel, Mordechai Blaunstein, Olivia Bouree, Ronnie Lazar, Tomer Hagay, Ben (Google PM, last name unknown), Unknown Google contact (bengit@google.com), Unknown Google contact (bobnapaa@google.com), Unknown Google contact (fanyanf@google.com), Unknown Google contact (hildebrand@google.com), Unknown Google contact (iraoren@google.com), Unknown Google contact (johndowney@google.com), Unknown Google contact (shengqiu@google.com), Unknown Google contact (wpien@google.com), Unknown Google contact (yardenh@google.com), Unknown Google contact (yevgenik@google.com)

## Summary

VAST and Google discussed VIP/IP management and failover approaches on Google Cloud Platform, comparing alias IPs, route-based failover, and Internal Load Balancer (ILB) tradeoffs. Key constraint: alias IPs are expected to be unsupported with RDMA on upcoming Z4M shapes, which likely require a separate RDMA subnet or interface and Private Service Connect interfaces (PSCI) for cross-project RDMA instead of VPC peering. The group agreed to create a shared pros and cons document, involve Google networking, and provide short-term testing projections plus longer-term customer volume projections for capacity planning.


## Action Items


- [?] Send Terraform snippets showing how VAST provisions and reserves static VIP IPs in Google Cloud Platform. @Ronnie Lazar 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Provide an estimate for adapting VAST deployment and test plans to the new RDMA-enabled GCP Z4M shapes, including expected effort and key validation steps. @Ronnie Lazar 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Share near-term testing projections and longer-term customer volume projections for GCP Z4M RDMA validation, including CI needs and client driver requirements, to support Google capacity planning. @Ronnie Lazar 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Initiate and share a collaborative document comparing ILB, alias IP, and route-based failover for VAST VIP design on GCP, including pros and cons, pricing, feature constraints, and operational complexity. @Ben (Google PM, last name unknown) 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Schedule a follow-up session with Google networking team focused on RDMA networking and cross-project design constraints for Z4M. @Billy Kettler 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Confirm RDMA support details on GCP Z4M relevant to VIP failover, including alias IP support status, separate subnet or interface model, and feasibility of route-based failover under RDMA. @Billy Kettler 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Clarify Z4M NIC topology and bandwidth allocation, including number of physical and logical NICs and per-interface bandwidth for RDMA vs TCP interfaces. @Ben (Google PM, last name unknown) 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Evaluate Private Service Connect interfaces (PSCI) requirements and implications for cross-project RDMA data plane, including performance and feature constraints. @Google networking team 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Determine whether MIG-managed static IP pools can help reserve VIPs and mitigate the unassign then reassign race window during failover. @Google networking team 📅 2025-11-08 #task #proposed #auto

- [?] Quantify API execution time and network convergence time for route changes and IP reassignments on GCP to assess route-based failover viability for client reconnect latency targets. @Google networking team 📅 2025-11-08 #task #proposed #auto

- [?] Advise whether dual NICs provide kernel or queueing efficiency benefits for RDMA and TCP separation even if aggregate per-VM bandwidth does not increase. @Google networking team 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Confirm cross-project RDMA constraints on GCP, specifically that PSCI is required and VPC peering is unsupported, and document expected performance impact. @Google networking team 📅 2025-11-08 ⏫ #task #proposed #auto




## Decisions


- Create a shared pros and cons document to re-evaluate GCP VIP and failover options (alias IP, route-based failover, and Internal Load Balancer) including pricing and feature tradeoffs.

- Engage Google networking for a focused follow-up deep dive on RDMA networking design and cross-project connectivity constraints.

- Start sizing and capacity planning work by collecting near-term testing projections first, then longer-term customer volume projections.




## Key Information


- Google Cloud Platform does not provide a single API to move an IP directly between interfaces or VMs; the workflow is remove/unassign then reassign, creating a race window where the IP can be briefly unallocated.

- Google Managed Instance Groups (MIGs) can be configured with a pool of reserved static IPs for primary addresses, but this does not necessarily apply to alias IPs.

- VAST provisions and reserves VIP-related static IPs in Google Cloud Platform using Terraform by creating named IP address objects, even when not attached to a VM.

- Alias IPs are expected to be unsupported with RDMA on GCP Z4M shapes; RDMA is expected to use a separate subnet or interface from TCP.

- Z4M is expected to launch with inter-node RDMA (Z4M to Z4M); GPU-direct storage RDMA between GPUs and Z4M is a separate enablement effort.

- Cross-project RDMA connectivity on GCP is expected to require Private Service Connect interfaces (PSCI); VPC peering is not expected to be supported for RDMA cross-project connections.

- Per-VM bandwidth is capped on the new shapes; adding NICs does not increase aggregate bandwidth, though it may still affect efficiency (queues or kernel behavior).

- Ben (Google PM, last name unknown) is the new Google product manager counterpart for this effort after the prior PM (Ruben, last name unknown) left Google.



---

*Source: [[2025-10-28 - The teams discussed IP management and failover approaches on GCP (alias IPs, rou]]*