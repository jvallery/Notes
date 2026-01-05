---
type: "projects"
title: "VAST on Cloud positioning and GTM alignment, marketplace MVP and hyperscaler constraints"
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

# VAST on Cloud positioning and GTM alignment, marketplace MVP and hyperscaler constraints

**Date**: 2025-10-29
**Project**: [[]]
**Attendees**: Lior Genzel, Tiffany Stonehill, Olivia, Paul, Jason Vallery, Arik Kishner, Director Hampson, Beth, Madhu

## Summary

Internal team aligned on VAST on Cloud positioning and go-to-market, leading with VAST's global namespace for data mobility across on-prem, public cloud, and NeoClouds. The current MVP is an 8-node VM plus local NVMe cluster per tenant with marketplace-based deployment and private offers planned, but multi-PB scale is constrained by VM shapes and cost until object storage integration and hyperscaler programs improve TCO.


## Action Items


- [?] Add Jason Vallery to the VAST on Cloud Slack channel used for deal intake. @Tiffany Stonehill 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Schedule and conduct a deep-dive on Visa's approximately 20 PB AWS copy requirements, including cost model and target architecture options for VAST on Cloud. @Arik Kishner 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Provide a roadmap answer and plan for tenant-level peering support for multi-tenant clusters replicating to separate cloud clusters. @Lior Genzel 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Post genomics customer details and requirements in the VAST on Cloud Slack channel and coordinate next steps for a potential POC. @Madhu 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Share AWS marketplace fulfillment steps and current collateral to support Madhu's genomics opportunity. @Lior Genzel 📅 2025-11-08 #task #proposed #auto

- [?] Finalize and distribute VAST on Cloud positioning, battle cards, and talk tracks to the field. @Product Marketing 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Drive hyperscaler engagements to improve VAST on Cloud economics and scale, including larger VM shapes and AWS FSx first-party path, and provide periodic updates to the field. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Advance object storage integration (for example, Amazon S3) and SyncEngine capabilities to improve VAST on Cloud TCO and multi-PB scale. @Engineering 📅 2025-11-08 #task #proposed #auto

- [?] Register cloud opportunities in Salesforce and announce them in the VAST on Cloud Slack channel early, especially multi-PB cases, to influence hyperscaler engagement and internal prioritization. @Field Sales 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Prepare Supercomputing conference booth demos for Microsoft and Google cloud scenarios for VAST on Cloud. @Events Team 📅 2025-11-08 #task #proposed #auto

- [?] Share prior customer learnings and relevant information in the VAST on Cloud Slack channel as referenced during the call. @Director Hampson 📅 2025-11-08 #task #proposed #auto

- [?] Confirm marketplace GA and transactability status and document the private-offer process for AWS, Azure, and GCP. @Tiffany Stonehill 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Provide an update on the AWS FSx first-party path and expected milestones relevant to VAST on Cloud economics and scaling. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Confirm the Azure large-VM shape availability timeline (for example, approximately 300 TB shapes) and share implications for VAST on Cloud multi-PB deployments. @Myself 📅 2025-11-08 #task #proposed #auto




## Decisions


- Use a designated Slack channel as the primary intake route for all VAST on Cloud opportunities and support, with Tiffany Stonehill triaging AWS and Azure and Olivia triaging GCP and OCI.

- Lead VAST on Cloud positioning with the global namespace value proposition, enabling data to move to compute across on-premises, public cloud, and NeoCloud providers.

- Proceed with marketplace-based deployment and private offers for VAST on Cloud to enable commit burn-down and smoother fulfillment once GA and transactable.

- Showcase VAST on Cloud demos at the Supercomputing conference, including Microsoft and Google cloud scenarios, to drive awareness and pipeline.




## Key Information


- VAST on Cloud positioning differentiator is VAST Data's global namespace that enables data mobility across on-premises, public cloud, and NeoCloud providers so customers can move data to where compute runs.

- The current VAST on Cloud MVP architecture is an 8-node VAST cluster per cloud tenant running on cloud VMs with local NVMe, positioned as a lift-and-shift performance product.

- Initial marketplace automation for VAST on Cloud starts with Google Cloud Platform (GCP), with Microsoft Azure and Amazon Web Services (AWS) planned to follow within approximately three months.

- On AWS, the current VAST on Cloud approach uses approximately 120 TB VM shapes and is estimated at about $0.20 per GB-month for VM storage, roughly 20x the cost of on-premises hardware.

- On Azure, the current largest VM shape discussed is approximately 23 TB, and Microsoft is discussing approximately 300 TB VM shapes targeting late next year.

- A key path to improved cloud TCO and multi-PB scale for VAST on Cloud is integrating cloud object storage (for example, Amazon S3) in future releases, including capabilities like SyncEngine for object moves.

- VAST Data is pushing AWS to approve an AWS FSx first-party path to unlock better economics and larger shapes for VAST on Cloud deployments.

- Engineering headcount focused on cloud at VAST Data grew from 5 to 25, indicating increased roadmap velocity for cloud features.

- Marketplace private offers for VAST on Cloud are intended to allow customers to burn down existing cloud commits once the offers are GA and transactable.

- ICE (New York Stock Exchange) evaluated bursting from on-prem into AWS but leaned toward VAST on-prem after reviewing cloud cost and complexity and learning VAST capabilities.

- Visa is seeking an approximately 20 PB copy in AWS, and the current VM-only scaling approach is expected to be costly, requiring roadmap and architecture discussions.

- A genomics customer scenario discussed involves approximately 100 TB of ephemeral data and may use on-prem S3 access or VAST on Cloud if performance requirements demand it.

- Tiffany Stonehill has been with VAST Data for just over 1.5 years and currently covers AWS and Azure (previously covered OCI).

- Olivia covers Google Cloud Platform (GCP) and Oracle Cloud Infrastructure (OCI) for VAST on Cloud hyperscaler engagement and field support.

- Paul is new to VAST Data (about four months) and is working a customer exploring moving workloads off Google Cloud Platform back to an on-premises data center, considering hybrid options.

- Jason Vallery joined VAST Data about one week before 2025-10-29 as VP of Product Management for Cloud, reporting to Jeff Denworth, and previously spent 13 years at Microsoft leading product management for Microsoft's object storage platform.



---

*Source: [[2025-10-29 - Team aligned on positioning and go-to-market for VAST on Cloud. Current MVP is a]]*