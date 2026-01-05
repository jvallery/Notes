---
type: "projects"
title: "VAST on Cloud positioning, marketplace automation, and hyperscaler constraints (global namespace focus)"
date: "2025-10-29"
project: ""
participants: ["Lior Genzel", "Tiffany Stonehill", "Olivia", "Jason Vallery", "Paul", "Arik Kishner", "Director Hampson", "Beth", "Madhu"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-29 - Team aligned on positioning and mechanics for VAST on Cloud. Emphasis on using g.md"
tags:
  - "type/projects"
  - "project/"
  - "generated"

---

# VAST on Cloud positioning, marketplace automation, and hyperscaler constraints (global namespace focus)

**Date**: 2025-10-29
**Project**: [[]]
**Attendees**: Lior Genzel, Tiffany Stonehill, Olivia, Jason Vallery, Paul, Arik Kishner, Director Hampson, Beth, Madhu

## Summary

Internal team aligned on VAST on Cloud positioning centered on VAST's global namespace to place data where compute runs across on-prem, public cloud, cross-cloud, and Neo clouds. The team reviewed current cloud VM shape and cost constraints, near-term marketplace automation plans (GCP first), and the need to push hyperscalers for larger shapes and programs (including AWS FSx). Several field scenarios were discussed (NYSE/ICE, Visa 20 PB copy, AWS genomics POC), with follow-ups on tenant-level peering and object storage integration to improve multi-PB TCO.


## Action Items


- [?] Follow up with Arik Kishner on Visa's approximately 20 PB cloud copy use case in AWS, including architecture and cost options given current VM shape constraints. @Lior Genzel 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Ensure cloud opportunities are registered in Salesforce and posted with details in the dedicated VAST on Cloud Slack channel to trigger rapid support. @TBD 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Share prior large-scale customer details and known limitations of current VAST on Cloud VM shapes and costs in the VAST on Cloud Slack channel for team visibility. @Director Hampson 📅 2025-11-08 #task #proposed #auto

- [?] Coordinate with Lior Genzel and Tiffany Stonehill on next steps for the AWS genomics use case, including POC sponsorship and marketplace path. @Madhu 📅 2025-11-08 #task #proposed #auto

- [?] Add Jason Vallery to the VAST on Cloud Slack channel and share the channel details so field sellers can access it. @Tiffany Stonehill 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Provide a roadmap update on tenant-level peering support for multi-tenant VAST clusters replicating to distinct customer-owned cloud clusters. @Lior Genzel 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Finalize VAST on Cloud positioning assets, battle cards, and talk tracks and publish them to the field when ready. @TBD 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Deliver an SE training deck before the Supercomputing event and ensure collateral is ready for Supercomputing demos. @TBD 📅 2025-11-08 #task #proposed #auto

- [?] Complete marketplace automation for Azure and AWS after the GCP marketplace automation rollout for VAST on Cloud cluster deployment into customer tenants. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Drive AWS FSx partnership discussions and push hyperscalers for larger VM shape support to improve VAST on Cloud cost and scalability. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Confirm if and when cloud object storage integration (for example, Amazon S3) will be available in VAST on Cloud to materially reduce TCO at multi-PB scale. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Assess feasibility and timeline for OCI support driven by the Zoom project and report back to the team. @Olivia 📅 2025-11-08 #task #proposed #auto

- [?] Evaluate SyncEngine as a near-term bridge for moving data in and out of cloud object storage while native integration is not yet available. @TBD 📅 2025-11-08 #task #proposed #auto




## Decisions


- Use the dedicated VAST on Cloud Slack channel as the primary intake mechanism for cloud opportunities, with Tiffany Stonehill leading AWS and Azure engagement and Olivia leading GCP and OCI engagement.

- Proceed with the VAST on Cloud MVP approach of deploying 8-node HA VAST clusters via marketplace automation, starting with GCP and then extending to Azure and AWS.

- Actively pursue hyperscaler programs and larger VM shapes, including pursuing AWS FSx first-party program alignment, to improve VAST on Cloud cost and performance.




## Key Information


- Tiffany Stonehill covers AWS and Azure hyperscaler engagements for VAST on Cloud.

- Olivia covers GCP and OCI hyperscaler engagements for VAST on Cloud.

- Jason Vallery joined VAST Data as VP of Product Management for Cloud and reports to Jeff Denworth.

- Jason Vallery previously led product management for Microsoft's object storage platform for 13 years.

- VAST's global namespace is positioned as the key differentiator for VAST on Cloud because it enables placing data where compute runs across on-prem, public cloud, cross-cloud, and Neo clouds.

- Initial supported AWS VM shapes for VAST on Cloud are described as 120 TB nodes.

- Azure VM shapes for VAST on Cloud are described as approximately 23 TB nodes, with discussions for approximately 300 TB nodes in the following year.

- Current cloud VM cost for VAST on Cloud was stated as approximately $0.20 per GB-month, roughly 20x on-prem hardware costs.

- The VAST on Cloud MVP is described as an 8-node HA VAST cluster running on cloud VMs, using the same product as on-prem but optimized for ease of deployment and performance.

- Marketplace automation is planned to deploy VAST clusters into customer tenants, with GCP first and Azure and AWS targeted to follow in approximately three months.

- Cloud provider proof-of-concept sponsorship is commonly available, and VAST cloud spend can burn down customer cloud commits.

- VAST is pursuing the AWS FSx first-party program as a hyperscaler program path for VAST on Cloud.

- The VAST cloud engineering team reportedly grew from approximately 5 to approximately 25 engineers, increasing delivery velocity.

- NYSE/ICE evaluated bursting from on-prem to AWS but chose VAST on-prem after cost and complexity analysis, and the team considered this a VAST win enabled by having a credible cloud story.

- Visa is described as seeking an approximately 20 PB copy in AWS, requiring higher scalability and better TCO than current cloud VM shapes allow.

- SyncEngine was mentioned as a potential near-term bridge to move data in and out of cloud object storage while native integration matures.



---

*Source: [[2025-10-29 - Team aligned on positioning and mechanics for VAST on Cloud. Emphasis on using g]]*