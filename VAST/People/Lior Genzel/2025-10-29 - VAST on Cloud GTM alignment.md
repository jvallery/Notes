---
type: "people"
title: "VAST on Cloud GTM alignment"
date: "2025-10-29"
person: "Lior Genzel"
participants: ["Lior Genzel", "Tiffany Stonehill", "Olivia Bouree", "Paul", "Jason Vallery", "Arik Kishner", "Director Hampson", "Beth", "Madhu"]
source: "transcript"
source_ref: "Inbox/_archive/2025-10-29/2025-10-29 - Team aligned on positioning and go-to-market for VAST on Cloud. Current MVP is a.md"
tags:
  - "type/people"
  - "person/lior-genzel"
  - "generated"
---

# VAST on Cloud GTM alignment

**Date**: 2025-10-29
**With**: Lior Genzel, Tiffany Stonehill, Olivia Bouree, Paul, Jason Vallery, Arik Kishner, Director Hampson, Beth, Madhu

## Summary

Team aligned on positioning and go-to-market for VAST on Cloud, emphasizing the global namespace as the key differentiator and using a Slack channel as the intake path for cloud opportunities. The current MVP is an 8-node VM/NVMe-based cluster per customer tenant with marketplace deployment and private offers planned; VM-shape limits and cost are current blockers for multi-PB deployments. Specific follow-ups were assigned for Visa-scale requirements, genomics opportunity mechanics, tenant-level peering roadmap, and hyperscaler engagements (e.g., AWS FSx, larger Azure VM shapes).
## Action Items
- [ ] Add Jason Vallery to the VAST-on-Cloud Slack channel used for deal intake. @Tiffany 📅 2025-11-08 🔺 #task
- [ ] Schedule and conduct a deep-dive on Visa’s ~20 PB cloud copy requirements, cost, and architecture. @Arik 📅 2025-11-08 🔺 #task
- [ ] Provide a roadmap answer/timeline for tenant-level peering for multi-tenant clusters replicating to separate cloud clusters. @Lior 📅 2025-11-08 🔺 #task
- [ ] Post genomics customer details and requirements in the Slack channel and coordinate next steps/POC. @Madhu 📅 2025-11-08 ⏫ #task
- [ ] Share AWS marketplace fulfillment steps and current collateral with Madhu’s genomics opportunity. @Lior 📅 2025-11-08 ⏫ #task
- [ ] Confirm marketplace GA/transactable dates and private-offer process for AWS/Azure/GCP. @Tiffany 📅 2025-11-08 🔺 #task
- [ ] Drive hyperscaler engagements (VM shapes, AWS FSx first-party path) and provide periodic updates to the field. @Jason 📅 2025-11-08 🔺 #task
- [ ] Confirm Azure large-VM (e.g., ~300 TB) shape availability timeline. @Jason 📅 2025-11-08 ⏫ #task
- [ ] Share prior customer learnings/info on Slack as referenced on the call. @Director Hampson 📅 2025-11-08 ⏫ #task

## Decisions
- Use the designated Slack channel as the primary intake route for VAST on Cloud deals and support (Tiffany for AWS/Azure; Olivia for GCP/OCI).
- Lead with the global namespace message to position data mobility across on-prem, public cloud, and NeoClouds.
- Proceed with marketplace-based deployment and private offers to enable commit burn-down and smoother fulfillment.
- Showcase VAST on Cloud demos at Supercomputing to drive awareness and pipeline.

## Key Information
- Current VAST on Cloud MVP is an 8-node cluster running on cloud VMs with local NVMe; intended as a lift-and-shift, performance-oriented deployment per customer tenant.
- Initial marketplace automation starts with GCP; Azure and AWS expected to follow within ~3 months (as stated in the meeting notes).
- AWS currently supports ~120 TB VM shapes; VM cost cited at ~$0.20/GB-month, roughly ~20x on-prem hardware cost for equivalent capacity.
- Azure VM shape cited at ~23 TB today; Microsoft discussing ~300 TB VM shapes targeting late next year.
- Improving cloud TCO and multi-PB scalability depends on integrating cloud object storage (e.g., S3) in future releases; not in the initial release.
- Pushing AWS toward an FSx first-party program is viewed as a lever to unlock better economics and larger shapes.
- Marketplace private offers are expected to burn down customer cloud commits once GA/transactable.
- Example field learning: ICE/NYSE evaluated bursting to AWS but leaned toward VAST on-prem after cost/complexity review; Visa is exploring ~20 PB copy in AWS; genomics use case is ~100 TB ephemeral data with AWS as target cloud.
- Cloud engineering headcount increased from ~5 to ~25, indicating accelerated roadmap velocity.

---

*Source: [[Inbox/_archive/2025-10-29/2025-10-29 - Team aligned on positioning and go-to-market for VAST on Cloud. Current MVP is a.md|2025-10-29 - Team aligned on positioning and go-to-market for VAST on Cloud. Current MVP is a]]*

## Related

- [[Lior Genzel]]
- [[Tiffany Stonehill]]
- [[Olivia Bouree]]
- [[Jason Vallery]]
- [[Arik Kishner]]
- [[Director Hampson]]
- [[Amazon]]
- [[Google]]
- [[Microsoft]]
- [[Oracle]]
- [[CoreWeave]]
