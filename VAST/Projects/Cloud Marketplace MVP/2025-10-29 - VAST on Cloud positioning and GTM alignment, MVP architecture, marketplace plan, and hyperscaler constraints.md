---
type: "projects"
title: "VAST on Cloud positioning and GTM alignment, MVP architecture, marketplace plan, and hyperscaler constraints"
date: "2025-10-29"
project: ""
participants: ["Lior Genzel", "Tiffany Stonehill", "Olivia", "Paul", "Jason Vallery", "Arik Kishner", "Director Hampson", "Beth", "Madhu"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-29 - Team aligned on positioning and go-to-market for VAST on Cloud. Current MVP is a.md"
tags:
  - "type/projects"
  - "project/"
  - "generated"

---

# VAST on Cloud positioning and GTM alignment, MVP architecture, marketplace plan, and hyperscaler constraints

**Date**: 2025-10-29
**Project**: [[]]
**Attendees**: Lior Genzel, Tiffany Stonehill, Olivia, Paul, Jason Vallery, Arik Kishner, Director Hampson, Beth, Madhu

## Summary

Internal team aligned on leading VAST on Cloud with the global namespace value proposition and routing all cloud opportunities through a dedicated Slack intake channel. The current MVP is an 8-node VM plus local NVMe cluster per tenant, with marketplace-based deployment and private offers planned, but multi-PB scale is constrained by VM shape limits and high VM cost versus on-prem. Follow-ups were assigned for Visa-scale architecture, tenant-level peering, marketplace transactability, and hyperscaler engagements (including AWS FSx and larger Azure VM shapes).


## Action Items


- [?] Add Jason Vallery to the VAST on Cloud Slack channel used for deal intake. @Tiffany Stonehill 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Schedule and conduct a deep-dive on Visa's approximately 20 PB cloud copy requirements, cost model, and target architecture for AWS. @Arik Kishner 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Provide a roadmap answer for tenant-level peering support for multi-tenant clusters replicating to separate cloud clusters. @Lior Genzel 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Post genomics customer details and requirements in the VAST on Cloud Slack intake channel and coordinate next steps for a potential POC. @Madhu 📅 2025-11-08 #task #proposed #auto

- [?] Share AWS marketplace fulfillment steps and current collateral to support Madhu's genomics opportunity. @Lior Genzel 📅 2025-11-08 #task #proposed #auto

- [?] Finalize and distribute VAST on Cloud positioning, battle cards, and talk tracks to the field. @Product Marketing 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Drive hyperscaler engagements to improve VAST on Cloud viability, including larger VM shapes and the AWS FSx first-party path, and provide periodic updates to the field. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Advance cloud object storage integration (for example Amazon S3) and SyncEngine capabilities to improve VAST on Cloud TCO and multi-PB scale. @Engineering 📅 2025-11-08 #task #proposed #auto

- [?] Register cloud opportunities in Salesforce and announce them in the VAST on Cloud Slack intake channel, especially multi-PB opportunities, to influence hyperscaler engagement early. @Field Sales 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Prepare Supercomputing conference booth demos for Microsoft Azure and Google Cloud Platform scenarios for VAST on Cloud. @Events Team 📅 2025-11-08 #task #proposed #auto

- [?] Share prior customer learnings and relevant information in the VAST on Cloud Slack intake channel as referenced during the call. @Director Hampson 📅 2025-11-08 #task #proposed #auto

- [?] Confirm marketplace GA and transactability status and document the private-offer process for AWS, Azure, and GCP. @Tiffany Stonehill 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Provide an update on the AWS FSx first-party path and expected milestones relevant to VAST on Cloud economics and scaling. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Share the latest VAST on Cloud collateral deck before SE training and the Supercomputing conference. @Product Marketing 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Confirm the Microsoft Azure large-VM shape availability timeline (for example approximately 300 TB shapes) relevant to VAST on Cloud scaling. @Myself 📅 2025-11-08 #task #proposed #auto




## Decisions


- Use a designated Slack channel as the primary intake route for all VAST on Cloud opportunities and support, with Tiffany Stonehill triaging AWS and Azure and Olivia triaging GCP and OCI.

- Lead VAST on Cloud positioning with the global namespace value proposition to move data to where compute runs across on-premises, public cloud, and NeoCloud providers.

- Proceed with marketplace-based deployment and private offers to enable commit burn-down and smoother fulfillment once offers are GA and transactable.

- Showcase VAST on Cloud demos at the Supercomputing conference to drive awareness and pipeline.




## Key Information


- VAST on Cloud differentiator is VAST Data's global namespace, enabling data mobility across on-premises, public cloud, and NeoCloud providers so customers can move data to where compute runs.

- The current VAST on Cloud MVP architecture is an 8-node VAST cluster per cloud tenant running on cloud VMs with local NVMe, positioned as a lift-and-shift performance product.

- Initial marketplace automation for VAST on Cloud starts with Google Cloud Platform (GCP), with Microsoft Azure and Amazon Web Services (AWS) planned to follow in approximately three months (timing stated in meeting notes, not a committed roadmap date).

- AWS VAST on Cloud deployments are currently constrained to approximately 120 TB VM shapes, with VM cost cited as about $0.20 per GB-month, roughly 20x the cost of on-prem hardware for equivalent capacity.

- Microsoft Azure VAST on Cloud deployments are currently constrained to approximately 23 TB VM shapes; Microsoft is discussing approximately 300 TB VM shapes targeting late next year (timing stated in meeting notes, not a committed roadmap date).

- A key path to improved cloud TCO and scale for VAST on Cloud is integrating hyperscaler object storage (for example Amazon S3) in future releases, supported by capabilities like SyncEngine for object moves.

- VAST is pushing AWS to approve an AWS FSx first-party path to unlock better economics and larger shapes for VAST on Cloud.

- Engineering headcount focused on cloud grew from 5 to 25, enabling faster roadmap velocity for VAST on Cloud.

- Marketplace private offers for VAST on Cloud are intended to burn down customer cloud commits once the offers are GA and transactable.

- ICE (Intercontinental Exchange, including NYSE) evaluated bursting from on-prem to AWS but leaned toward VAST on-prem after reviewing cloud cost and complexity, using the cloud offering as part of the competitive positioning.

- Visa is seeking an approximately 20 PB copy in AWS; the current VM-only scaling model is expected to be costly, requiring roadmap and architecture discussions.

- A genomics customer scenario discussed involves approximately 100 TB of ephemeral data, potentially served via on-prem S3 access or VAST on Cloud if performance requirements demand it.

- Tiffany Stonehill has been with VAST Data for just over 1.5 years and covers AWS and Azure hyperscaler engagements; she previously covered Oracle Cloud Infrastructure (OCI).

- Olivia covers Google Cloud Platform (GCP) and Oracle Cloud Infrastructure (OCI) hyperscaler engagements for VAST Data (exact title not stated).

- Paul is a new VAST Data employee (month four) and is working a customer exploring moving workloads off Google Cloud Platform (GCP) back to an on-premises data center, potentially using VAST on Cloud for hybrid or migration scenarios.

- Jason Vallery joined VAST Data about one week before this meeting, is VP of Product Management for Cloud reporting to Jeff Denworth, and previously spent 13 years at Microsoft leading product management for Microsoft's object storage platform.



---

*Source: [[2025-10-29 - Team aligned on positioning and go-to-market for VAST on Cloud. Current MVP is a]]*