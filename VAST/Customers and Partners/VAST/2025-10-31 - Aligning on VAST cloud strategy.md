---
type: "customer"
title: "Aligning on VAST cloud strategy"
date: "2025-10-31"
account: "VAST"
participants: ["Jason Vallery", "Karl Vietmeier"]
source: "transcript"
source_ref: "Inbox/_archive/2025-10-31/2025-10-31 - Introductory 1-1 aligning on VAST’s cloud strategy. Jason outlined a vision for.md"
tags:
  - "type/customer"
  - "account/vast"
  - "generated"
---

# Aligning on VAST cloud strategy

**Date**: 2025-10-31
**Account**: [[VAST]]
**Attendees**: Jason Vallery, Karl Vietmeier

## Summary

Jason and Karl aligned on a cloud-first strategy for VAST, including a long-term vision toward a planet-scale multi-tenant/SaaS platform spanning hyperscalers and neo-clouds, with emphasis on GPU-adjacent storage, global namespace, smart caching, and cloud economics. They discussed a Google Distributed Cloud (GDC) RFP surfaced via Cisco and the need for control-plane integrations (API/monitoring/billing), plus a critical product requirement to decouple capacity from performance via object/S3 offload. Next steps include reviewing the GDC RFP, engaging Jonesy’s team for integration requirements, and syncing at Supercomputing while Jason finalizes org/ownership planning with Jeff.
## Action Items
- [ ] Obtain and review the Google Distributed Cloud (GDC) RFP and clarify whether VAST is requested as a managed service offering vs backend distributed storage for GDC sites @Karl Vietmeier 📅 2025-11-08 ⏫ #task
- [ ] Loop in Jonesy’s team to assess API, monitoring, and billing integration requirements for a GDC-aligned VAST deployment @Jason Vallery 📅 2025-11-08 ⏫ #task
- [ ] Finalize cloud product ownership and org plan with Jeff, including potential reporting line for Karl @Jason Vallery 📅 2025-11-08 ⏫ #task
- [ ] Define and document cloud 'now what' use cases and upstream integrations (Spark, Trino, Vertex AI, Bigtable) to showcase differentiated workflows @Karl Vietmeier 📅 2025-11-08 ⏫ #task
- [ ] Drive design and plans for capacity/performance decoupling via object/S3 offload with Yancey’s team @Jason Vallery 📅 2025-11-08 ⏫ #task
- [ ] Coordinate a coffee sync at Supercomputing to continue cloud strategy and GDC planning @Jason Vallery 📅 2025-11-08 #task
- [ ] Share Karl’s GitHub repo link for review of automation and tooling @Karl Vietmeier 📅 2025-11-08 🔽 #task
- [ ] Provide notes/artifacts from the TPU global-namespace demo to inform cloud workflow examples @Karl Vietmeier 📅 2025-11-08 #task
- [ ] Confirm whether Google intends to procure VAST via Cisco for GDCs and the expected commercial model @Karl Vietmeier 📅 2025-11-08 #task

## Decisions
- P0 priority is to enable capacity scaling independent of performance via object/S3 offload for cloud viability.
- Cloud team will spearhead GDC/neo-cloud single-tenant GPU-adjacent storage opportunities and coordinate required integrations.

## Key Information
- Jason recently took on cloud product responsibility reporting to Jeff Denworth, focused on making VAST best on cloud and progressing toward a true multi-tenant SaaS platform across hyperscalers and neo-clouds.
- A Google Distributed Cloud (GDC) RFP surfaced via Cisco; success likely requires API, monitoring, and billing integration with Google’s control plane.
- Edge/extended-zone style deployments have large minimum footprints (~60–80 racks) and can be non-resilient if connectivity to a parent region fails.
- VAST cloud differentiation must extend beyond file shares to upstream integrations (e.g., Spark/Trino/Vertex AI/Bigtable) and simplified AI/ML pipelines.
- Without object/S3 offload to decouple capacity from performance, VAST may lack a competitive cloud cost/performance model versus vendors that write to S3.

---

*Source: [[Inbox/_archive/2025-10-31/2025-10-31 - Introductory 1-1 aligning on VAST’s cloud strategy. Jason outlined a vision for.md|2025-10-31 - Introductory 1-1 aligning on VAST’s cloud strategy. Jason outlined a vision for]]*

## Related

- [[Google]]
- [[Cisco]]
- [[Microsoft]]
- [[Intel]]
- [[Sun]]
- [[NetApp]]
- [[Amazon]]
- [[Oracle]]
- [[OpenAI]]
- [[Google Distributed Cloud RFP]]
- [[Jason Vallery]]
- [[Karl Vietmeier]]
- [[Jeff Denworth]]
- [[Jonsi Stephenson]]
