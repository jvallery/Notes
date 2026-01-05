---
type: customer
title: GCP RDMA IP failover options
date: '2025-10-28'
account: Google
participants:
- Asaf Levy
- Ben (bengit@google.com)
- Billy Kettler
- bobnapaa@google.com
- Eirikur Hrafnsson
- fanyanf@google.com
- hildebrand@google.com
- iraoren@google.com
- John Downey
- Jonsi Stephenson
- Karl Vietmeier
- Lior Genzel
- Mordechai Blaunstein
- Olivia Bouree
- Ronnie Lazar
- shengqiu@google.com
- Tomer Hagay
- wpien@google.com
- yardenh@google.com
- yevgenik@google.com
source: transcript
tags:
- type/customer
- account/google
- generated
---

# GCP RDMA IP failover options

**Date**: 2025-10-28
**Account**: [[Google]]
**Attendees**: Asaf Levy, Ben (bengit@google.com), Billy Kettler, bobnapaa@google.com, Eirikur Hrafnsson, fanyanf@google.com, hildebrand@google.com, iraoren@google.com, John Downey, Jonsi Stephenson, Karl Vietmeier, Lior Genzel, Mordechai Blaunstein, Olivia Bouree, Ronnie Lazar, shengqiu@google.com, Tomer Hagay, wpien@google.com, yardenh@google.com, yevgenik@google.com

## Summary

Teams reviewed GCP IP management and failover approaches (alias IPs, route-based failover, ILB) and the implications of upcoming RDMA-enabled Z4M shapes. Current expectation is alias IPs will not be supported with RDMA; Z4M instances will have separate RDMA and TCP interfaces (likely same VPC, different subnets), and cross-project RDMA will require Private Service Connect interfaces rather than VPC peering. Next steps include a shared pros/cons document, engaging Google networking, and providing testing plus longer-term volume projections for capacity planning.
## Action Items
- [ ?] Send Terraform snippets showing how static VIP IPs are provisioned/reserved. @Ronnie 📅 2025-11-08 ⏫ #task #proposed
- [ ?] Provide estimate for adapting and testing new RDMA (Z4M) shapes. @Ronnie 📅 2025-11-08 🔺 #task #proposed
- [ ?] Share testing and customer volume projections (include CI needs and client drivers) to support capacity planning. @Ronnie 📅 2025-11-08 🔺 #task #proposed
- [ ?] Initiate shared document comparing ILB, alias IP, and route-based failover (pros/cons, pricing, features). @Ben 📅 2025-11-08 ⏫ #task #proposed
- [ ?] Schedule follow-up session with Google networking team on RDMA networking and cross-project design. @Billy 📅 2025-11-08 🔺 #task #proposed
- [ ?] Confirm RDMA support details: alias IP status, separate subnet/interface model, and feasibility of route-based failover. @Billy 📅 2025-11-08 🔺 #task #proposed
- [ ?] Clarify Z4M NIC topology and bandwidth allocation (number of physical/logical NICs; per-interface bandwidth). @Ben 📅 2025-11-08 ⏫ #task #proposed
- [ ?] Evaluate PSCI requirements and implications for cross-project RDMA data plane. @Google networking team 📅 2025-11-08 ⏫ #task #proposed
- [ ?] Determine if MIG-managed static IP pools can help reserve VIPs and mitigate the unassign/reassign race window. @Google networking team 📅 2025-11-08 ⏫ #task #proposed
- [ ?] Quantify API execution time and network convergence for route changes and IP reassignments. @Google networking team 📅 2025-11-08 ⏫ #task #proposed
- [ ?] Advise whether dual NICs provide kernel/queueing efficiency benefits despite no extra bandwidth. @Google networking team 📅 2025-11-08 🔽 #task #proposed
- [ ?] Confirm cross-project RDMA constraints (PSCI required; VPC peering unsupported) and performance impact. @Google networking team 📅 2025-11-08 ⏫ #task #proposed

## Decisions
- Create a shared pros/cons document to re-evaluate VIP/failover options (ILB, alias IP, route-based).
- Engage Google networking for a follow-up deep dive on RDMA and cross-project connectivity.
- Begin sizing work starting with testing projections, then customer projections.

## Key Information
- GCP IP reassignment requires remove then reassign, creating a short race window where the IP may be considered free.
- MIGs can use a pool of reserved static IPs for primary addresses; alias IP behavior differs from primary IPs.
- Alias IPs are expected to be unsupported with RDMA; RDMA will use a separate subnet/interface.
- Z4M is expected to launch with inter-node RDMA; GPU-direct storage RDMA is a separate effort.
- Z4M instances are expected to have two interfaces (RDMA and TCP), potentially in the same VPC but different subnets.
- Cross-project RDMA will require Private Service Connect interfaces; VPC peering will not be supported.
- Route-based failover has latency/convergence considerations; ILB introduces pricing/feature tradeoffs.
- Per-VM bandwidth is capped; adding NICs does not increase aggregate bandwidth.
- Initial test scale target is roughly 10–30 instances; CI and scale testing will require more.
- Ben is the new Google PM counterpart for this effort.

---

*Source: [[Inbox/_archive/2025-10-28/original.md|original]]*

## Related

- [[John Downey]]
- [[Jonsi Stephenson]]
- [[Lior Genzel]]
- [[Mordechai Blaunstein]]
- [[Olivia Bouree]]
- [[VIP]]