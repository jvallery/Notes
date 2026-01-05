---
type: people
title: VAST on Cloud alignment
date: '2025-10-29'
person: Lior Genzel
participants:
- Lior Genzel
- Tiffany Stonehill
- Olivia Bouree
- Jason Vallery
- Paul
- Arik Kishner
- Director Hampson
- Beth
- Madhu
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-10-29 - Team aligned on positioning and
  mechanics for VAST on Cloud. Emphasis on using g.md
tags:
- type/people
- person/lior-genzel
- generated
---

# VAST on Cloud alignment

**Date**: 2025-10-29
**With**: Lior Genzel, Tiffany Stonehill, Olivia Bouree, Jason Vallery, Paul, Arik Kishner, Director Hampson, Beth, Madhu

## Summary

Team aligned on positioning for VAST on Cloud, emphasizing the global namespace to place data where compute runs across on-prem, public cloud, cross-cloud, and Neo clouds. Key constraints are current VM shapes and cloud cost (~$0.20/GB-month), with roadmap focus on marketplace automation, larger VM shapes via hyperscalers, and future object storage integration to improve TCO. Field was directed to route opportunities through Salesforce and a dedicated Slack channel, with follow-ups on Visa’s 20PB use case, AWS genomics POC mechanics, and tenant-level peering for multi-tenant clusters.
## Action Items
- [ ] Follow up with Arik on Visa’s ~20 PB cloud copy use case and propose architecture/cost options. @Lior Genzel 📅 2025-11-08 🔺 #task #proposed
- [ ] Register cloud opportunities in Salesforce and post details in the VAST on Cloud Slack channel for rapid support. @TBD 📅 2025-11-08 🔺 #task #proposed
- [ ] Share prior large-scale customer details and current limitations in Slack for team visibility. @Director Hampson 📅 2025-11-08 ⏫ #task #proposed
- [ ] Coordinate with Lior/Tiffany on AWS genomics use case next steps (POC and marketplace path). @Madhu 📅 2025-11-08 ⏫ #task #proposed
- [ ] Add Jason Vallery to the VAST on Cloud Slack channel. @Tiffany Stonehill 📅 2025-11-08 🔽 #task #proposed
- [ ] Provide a roadmap update on tenant-level peering for multi-tenant clusters replicating to distinct customer cloud clusters. @Lior Genzel 📅 2025-11-08 🔺 #task #proposed
- [ ] Finalize VAST on Cloud positioning assets (battle cards and talk tracks). @TBD 📅 2025-11-08 🔺 #task #proposed
- [ ] Deliver SE training deck before Supercomputing and ensure collateral is ready for Supercomputing demos. @TBD 📅 2025-11-08 ⏫ #task #proposed
- [ ] Complete marketplace automation for Azure and AWS following the GCP rollout. @TBD 📅 2025-11-08 🔺 #task #proposed
- [ ] Drive AWS FSx partnership discussions and push hyperscalers for larger VM shape support. @Myself 📅 2025-11-08 🔺 #task #proposed
- [ ] Confirm if/when cloud object storage integration (e.g., S3) will be available to reduce cloud TCO at multi-PB scale. @Myself 📅 2025-11-08 ⏫ #task #proposed
- [ ] Share the Slack channel details and ensure all field sellers have access. @Tiffany Stonehill 📅 2025-11-08 🔽 #task #proposed
- [ ] Assess feasibility and timeline for OCI support driven by the Zoom project. @Olivia 📅 2025-11-08 ⏫ #task #proposed
- [ ] Evaluate SyncEngine as a near-term bridge for moving data in/out of cloud object storage. @TBD 📅 2025-11-08 ⏫ #task #proposed

## Decisions
- Use the VAST on Cloud Slack channel as the primary intake for opportunities, with Tiffany (AWS/Azure) and Olivia (GCP/OCI) leading engagement.
- Proceed with MVP 8-node HA VAST on Cloud clusters delivered via marketplace automation (GCP first, Azure/AWS to follow).
- Actively pursue hyperscaler programs (e.g., AWS FSx) and larger VM shapes to improve cost/performance.

## Key Information
- Tiffany covers AWS and Azure; Olivia covers GCP and OCI.
- Jason Vallery joined as VP of Product Management for Cloud; previously led Microsoft object storage PM for ~13 years.
- Global namespace is positioned as the key differentiator to move data to where compute runs across on-prem, public cloud, cross-cloud, and Neo clouds.
- Current supported AWS VM shapes are ~120 TB nodes; Azure is ~23 TB nodes with discussions for ~300 TB nodes next year.
- Cloud VM cost is cited at roughly ~$0.20/GB-month (~20x on-prem hardware cost).
- MVP is an 8-node HA VAST cluster on cloud VMs; same product as on-prem, optimized for ease of deployment and performance.
- Marketplace automation: GCP first; Azure and AWS targeted within ~3 months.
- Large-scale cloud competitiveness is expected to improve with future integration of cloud object storage (e.g., S3); not in initial GA.
- Cloud providers often sponsor POCs; VAST cloud spend can burn down customer cloud commits.
- AWS FSx first-party program is being pursued; more field opportunities help accelerate hyperscaler support.
- Tenant-level peering limitations are a blocker for multi-tenant Neo cloud to public cloud data movement.
- Supercomputing will feature demos and collateral; SE training deck planned ahead of the event.

---

*Source: [[Inbox/_archive/2025-10-29/2025-10-29 - Team aligned on positioning and mechanics for VAST on Cloud. Emphasis on using g.md|2025-10-29 - Team aligned on positioning and mechanics for VAST on Cloud. Emphasis on using g]]*

## Related

- [[Lior Genzel]]
- [[Tiffany Stonehill]]
- [[Olivia Bouree]]
- [[Jason Vallery]]
- [[Arik Kishner]]
- [[Director Hampson]]
- [[Jeff Denworth]]
- [[Amazon]]
- [[Google]]
- [[Microsoft]]
- [[Oracle]]
- [[CoreWeave]]