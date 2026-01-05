---
type: customer
title: GCP path for VAST Z4M
date: '2025-10-31'
account: Google
participants:
- Jason Vallery
- Billy
- John Downey
- Lior
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-10-31 - GCP outlined the path to run VAST
  on storage-serving VMs (Z4M) with higher stora.md
tags:
- type/customer
- account/google
- generated
---

# GCP path for VAST Z4M

**Date**: 2025-10-31
**Account**: [[Google]]
**Attendees**: Jason Vallery, Billy, John Downey, Lior

## Summary

Google Cloud outlined an architecture and roadmap to run VAST on upcoming Z4M storage-serving VMs with higher storage/network density, co-placement via the Google Supercomputer (GSC) provisioning interface, and future RDMA/GPUDirect enablement (A5X GPUs first; TPU RDMA later). The group discussed tiering options (local SSD first, with HyperDisk/object-tier metadata offload later), and highlighted that inter-region/internal networking costs (e.g., ILB) and egress economics are major blockers for large-scale data movement. Next steps include coordinating in-person meetings at Supercomputing with key GCP stakeholders and preparing networking questions and commercial/pricing explorations.
## Action Items
- [ ] Schedule Supercomputing meetings and include Ilyas and Dean if possible @John 📅 2025-11-08 ⏫ #task #proposed
- [ ] Draft and share networking questions and formal requests for GCP ahead of Supercomputing @Myself 📅 2025-11-08 ⏫ #task #proposed
- [ ] Review the Cloud WAN link shared by GCP and assess applicability to VAST data movement @Myself 📅 2025-11-08 ⏫ #task #proposed
- [ ] Explore commercial constructs to mitigate inter-region and egress/internal networking costs for VAST and joint customers @Myself 📅 2025-11-08 ⏫ #task #proposed
- [ ] Confirm RDMA and GPUDirect Storage enablement details and cost implications for Z4M and A5X, and share the plan with VAST @Billy 📅 2025-11-08 #task #proposed
- [ ] Evaluate feasibility/timeline for a higher-performance object storage tier suitable for VAST metadata offload @GCP Storage 📅 2025-11-08 #task #proposed
- [ ] Analyze performance and design implications of metadata offload to object storage for VAST on GCP @Myself 📅 2025-11-08 #task #proposed
- [ ] Scope integration of VAST as a selectable storage option within the Google Supercomputer (GSC) provisioning flow, including auto-deploy and co-placement @Billy 📅 2025-11-08 #task #proposed
- [ ] Define path and timeline for RDMA enablement on TPUs and implications for VAST deployments @Billy 📅 2025-11-08 🔽 #task #proposed
- [ ] Engage GCP networking and pricing teams to reduce ILB/internal egress costs for storage-serving partner solutions @John 📅 2025-11-08 ⏫ #task #proposed

## Decisions
- Proceed with local SSD-based Z4M for initial VAST on GCP; evaluate object/HyperDisk tiers later.
- Coordinate in-person sessions at Supercomputing and include key GCP stakeholders (Ilyas, Dean).

## Key Information
- Z4M is the next GCP storage-serving VM after Z3, targeting higher storage and network density; CPU/RAM may be overprovisioned initially with planned pricing optimization.
- GCP is developing a Google Supercomputer (GSC) provisioning interface to improve co-placement of storage and accelerators and potentially enable VAST as a selectable/automated storage option.
- Local SSD is the initial choice for VAST on GCP due to latency; HyperDisk and GCS offer decoupled capacity/performance economics but higher latency.
- Anywhere Cache helps reduce intra-zone egress/operational cost but does not materially improve object-store latency.
- RDMA is planned for Z4M and A5X GPUs with GPUDirect Storage; TPU RDMA will come later.
- Internal networking constructs (e.g., ILB) can create egress-like costs that become prohibitive at very high throughput (multi-TB/s).
- Cross-region/CSP/neo-hyperscaler data movement economics (egress) are a major constraint; commercial constructs may be needed to make solutions viable.
- VAST marketplace launch on GCP is near; integration with Vertex/TPU is being considered.
- Customers often keep exabyte-scale data lakes in object storage and want mixed POSIX/S3 access patterns.

---

*Source: [[Inbox/_archive/2025-10-31/2025-10-31 - GCP outlined the path to run VAST on storage-serving VMs (Z4M) with higher stora.md|2025-10-31 - GCP outlined the path to run VAST on storage-serving VMs (Z4M) with higher stora]]*

## Related

- [[John Downey]]
- [[Lior Genzel]]
- [[Jason Vallery]]
- [[Microsoft]]
- [[Amazon]]
- [[CoreWeave]]