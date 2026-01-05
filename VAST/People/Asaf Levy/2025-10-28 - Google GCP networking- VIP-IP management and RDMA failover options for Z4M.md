---
type: "customer"
title: "Google GCP networking: VIP/IP management and RDMA failover options for Z4M"
date: "2025-10-28"
account: ""
participants: ["Asaf Levy", "Billy Kettler", "Eirikur Hrafnsson", "Jonsi Stephenson", "Karl Vietmeier", "Lior Genzel", "Mordechai Blaunstein", "Olivia Bouree", "Ronnie Lazar", "Tomer Hagay", "Ben (Google PM, email: bengit@google.com)", "bobnapaa@google.com", "fanyanf@google.com", "hildebrand@google.com", "iraoren@google.com", "johndowney@google.com", "shengqiu@google.com", "wpien@google.com", "yardenh@google.com", "yevgenik@google.com"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-28 - The teams discussed IP management and failover approaches on GCP (alias IPs, rou.md"
tags:
  - "type/customer"
  - "account/"
  - "generated"

---

# Google GCP networking: VIP/IP management and RDMA failover options for Z4M

**Date**: 2025-10-28
**Account**: [[]]
**Attendees**: Asaf Levy, Billy Kettler, Eirikur Hrafnsson, Jonsi Stephenson, Karl Vietmeier, Lior Genzel, Mordechai Blaunstein, Olivia Bouree, Ronnie Lazar, Tomer Hagay, Ben (Google PM, email: bengit@google.com), bobnapaa@google.com, fanyanf@google.com, hildebrand@google.com, iraoren@google.com, johndowney@google.com, shengqiu@google.com, wpien@google.com, yardenh@google.com, yevgenik@google.com

## Summary

VAST and Google discussed GCP VIP and failover approaches (alias IPs, route-based failover, and ILB) and how upcoming RDMA-enabled Z4M shapes change constraints. The group believes alias IPs will not be supported with RDMA, with RDMA using a separate subnet/interface and requiring PSC interfaces for cross-project RDMA instead of VPC peering. Next steps are a shared pros/cons document, a follow-up with Google networking, and near-term testing plus longer-term customer volume projections for capacity planning.


## Action Items


- [?] Send Terraform snippets showing how static VIP IPs are provisioned and reserved on GCP (static IP reservation objects used for VIPs). @Ronnie Lazar 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Provide an estimate for adapting VAST testing and validation to the new RDMA-enabled Z4M shapes, including effort and scope assumptions. @Ronnie Lazar 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Share near-term testing projections and longer-term customer volume projections (including CI needs and client drivers) to support Google capacity planning. @Ronnie Lazar 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Initiate a shared document comparing ILB, alias IP, and route-based failover for VIP design on GCP, including pros/cons, pricing, and feature constraints (multi-tenant and QoS considerations). @Ben (Google PM, email: bengit@google.com) 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Schedule a follow-up session with Google networking team focused on RDMA networking and cross-project design constraints for Z4M. @Billy Kettler 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Confirm RDMA support details on GCP Z4M: whether alias IPs are supported, whether RDMA requires a separate subnet/interface, and whether route-based failover is feasible for RDMA workloads. @Billy Kettler 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Clarify Z4M NIC topology and bandwidth allocation details (number of physical/logical NICs, RDMA vs TCP interface bandwidth, and any efficiency benefits of dual NICs). @Ben (Google PM, email: bengit@google.com) 📅 2025-11-08 #task #proposed #auto

- [?] Evaluate Private Service Connect interface (PSC interface) requirements and implications for cross-project RDMA data plane, including performance and feature impact. @TBD 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Determine whether MIG-managed static IP pools can help reserve VIPs and mitigate the unassign/reassign race window during failover. @TBD 📅 2025-11-08 #task #proposed #auto

- [?] Quantify API execution time and network convergence time for route changes and IP reassignments on GCP to assess failover latency and client reconnect impact. @TBD 📅 2025-11-08 #task #proposed #auto




## Decisions


- Create a shared pros and cons document to re-evaluate GCP VIP and failover options (ILB, alias IP, and route-based failover) including pricing and feature implications.

- Engage Google networking for a focused follow-up deep dive on RDMA networking and cross-project connectivity constraints (including PSC interfaces vs VPC peering).

- Start sizing and capacity planning work by collecting near-term testing projections first, then longer-term customer volume projections.




## Key Information


- GCP does not provide a single API to move an IP directly between interfaces or VMs; the workflow is remove/unassign the IP and then reassign it, creating a race window where the IP may be considered free.

- Google Managed Instance Groups (MIGs) can be configured with a pool of reserved static IPs for primary addresses so that IPs are reused and not freed when instances are recreated; this likely does not apply to alias IPs.

- The team’s current understanding is that alias IPs will not be supported with RDMA on GCP Z4M shapes; RDMA is expected to use a separate subnet and separate interface from TCP.

- Z4M is expected to use two interfaces per instance, one for RDMA and one for TCP, potentially within the same VPC but on different subnets.

- Cross-project RDMA connectivity on GCP is expected to require Private Service Connect interfaces (PSC interfaces); VPC peering is not expected to be supported for RDMA cross-project connectivity.

- Route-based failover on GCP has latency and network convergence considerations that may impact client reconnect behavior during failover.

- Using GCP Internal Load Balancer (ILB) for failover introduces pricing and feature tradeoffs, especially for multi-tenant and QoS requirements that may require multiple load balancers per VM.

- Per-VM bandwidth is capped on the relevant GCP shapes; adding NICs does not increase aggregate bandwidth, though it may still affect efficiency (queues/kernel/stack).

- Initial testing scale discussed was roughly 10 to 30 instances, with CI and scale testing requiring more capacity later.

- Ben (bengit@google.com) is the new Google PM counterpart for this effort, replacing a prior PM named Ruben who left Google.



---

*Source: [[2025-10-28 - The teams discussed IP management and failover approaches on GCP (alias IPs, rou]]*