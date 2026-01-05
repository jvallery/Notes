---
type: "projects"
title: "Cloud operations org design: distinct Customer Success, Support, and SRE roles with 2026-02-01 readiness target"
date: "2025-10-30"
project: ""
participants: ["Jason Vallery", "Lior Genzel", "Daniel Levy", "Rob Banga", "Yancey", "Timo Pervane", "Joe"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-30 - The group aligned on establishing distinct Customer Success, Support, and SRE ro.md"
tags:
  - "type/projects"
  - "project/"
  - "generated"

---

# Cloud operations org design: distinct Customer Success, Support, and SRE roles with 2026-02-01 readiness target

**Date**: 2025-10-30
**Project**: [[]]
**Attendees**: Jason Vallery, Lior Genzel, Daniel Levy, Rob Banga, Yancey, Timo Pervane, Joe

## Summary

The team aligned on a distinct operating model for cloud deployments with separate Customer Success (proactive), Support (reactive), and SRE (24/7 operations and on-call rotation) responsibilities, targeting operational readiness by 2026-02-01. Near-term execution prioritizes Microsoft Azure marketplace opportunities, with Google Cloud Platform and AWS following, and requires Tackle-Salesforce-Polaris integration plus improved Salesforce data hygiene, access controls, and Tableau telemetry/analytics.


## Action Items


- [?] Draft and circulate a simple cloud support plan defining Customer Success vs Support vs SRE responsibilities, 24/7 coverage expectations, and phased approach for private offers, public offers, and FY2028 SaaS. @Rob Banga 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Start recruiting initial SRE and cloud support hires to build the cloud support machine required for 2026-02-01 readiness. @Rob Banga 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Sync offline to refine the Customer Success, Support, and SRE model and define on-call rotations for cloud operations. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Define Tableau telemetry and analytics requirements for cloud customers, including churn indicators, feature usage, and required data feeds. @Yancey 📅 2025-11-08 #task #proposed #auto

- [?] Plan the Tackle-Salesforce-Polaris integration needed for marketplace offers, customer registration, and entitlement and role management. @Yancey 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Confirm leadership for cloud implementations, including alignment with Carl (last name unknown) and scoping the initial implementation team. @Rob Banga 📅 2025-11-08 #task #proposed #auto

- [?] Prepare enablement and documentation for Sales Engineers, Support, and Customer Success for cloud, including SKO content. @Product Marketing 📅 2025-11-08 #task #proposed #auto

- [?] Define metering evidence requirements and internal controls for Polaris hourly usage data with Finance and auditors to support marketplace billing and revenue recognition. @Finance 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Outline the overage policy for private offers and evaluate SaaS pricing unit model options. @Yancey 📅 2025-11-08 #task #proposed #auto

- [?] Schedule and run a Salesforce and Tackle deep-dive to understand current marketplace flows and identify gaps for integration with Polaris. @Cristina Hasson 📅 2025-10-31 ⏫ #task #proposed #auto

- [?] Meet offline to refine cloud org design and on-call rotations for Customer Success, Support, and SRE. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Complete legal review of data custodian obligations, EULA updates, and compliance roadmap including SOC2 and FedRAMP considerations for future SaaS. @Legal 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Attend the Google Cloud Platform meeting to review TPU test setup and defend benchmark results. @Lior Genzel 📅 2025-11-04 #task #proposed #auto

- [?] Validate Salesforce access and role model for customers and internal users, and define Salesforce data hygiene rules and validation requirements. @Sales Operations 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Confirm hyperscaler prioritization and the near-term target account list for execution across Azure, Google Cloud Platform, and AWS. @Yancey 📅 2025-11-08 #task #proposed #auto




## Decisions


- Adopt a distinct cloud operating model with separate Customer Success, Support, and SRE responsibilities, including 24/7 SRE on-call coverage for SaaS operations.

- Prioritize Microsoft Azure opportunities in the near term due to pent-up demand and large opportunities, with Google Cloud Platform and AWS following.

- Use Polaris as the metering source of truth with hourly usage reporting for cloud marketplace offers.

- Reaffirm the phased cloud commercialization plan: private offers first, public offers next, and full SaaS targeted for FY2028.

- Prepare cloud enablement and documentation content for SKO for Sales Engineering, Support, and Customer Success.




## Key Information


- The cloud go-to-market plan is phased: private marketplace offers first (approximately 2 months from 2025-10-30), public marketplace offers 6-8 months after private offers, and a full multi-tenant SaaS offering targeted for FY2028.

- For cloud operations, the team is adopting three distinct roles: Customer Success (proactive best practices and adoption), Support (reactive ticket handling), and SRE (24/7 operations, on-call rotation, and multi-tenant operational ownership for SaaS).

- The team set a target date of 2026-02-01 to be operationally ready with a 'cloud support machine' including 24/7 coverage expectations.

- Hyperscaler prioritization shifted toward Microsoft Azure due to near-term demand and large opportunities; Google Cloud Platform and AWS are planned to follow.

- Polaris is intended to be the metering source of truth with hourly usage reporting for cloud marketplace offers.

- Marketplace readiness requires integration across Tackle, Salesforce, and Polaris for marketplace flows, customer registration, and entitlement and role management.

- Cloud support is expected to see more networking-related tickets and fewer or no hardware-related tickets compared to on-prem deployments.

- Google Cloud Platform challenged VAST's TPU test results and requested a meeting to review the exact test setup because results appeared approximately 23% better than Google Managed Lustre; the VAST team believes the comparison may have been against managed SSD rather than Managed Lustre.

- A Google contact named 'Shansi' (last name unclear) is described as having reported directly to Nirav and having worked closely with VAST during a prior Google first-party offering; Nirav and Rich (last name unclear) were involved in the TPU test follow-up meeting invite.



---

*Source: [[2025-10-30 - The group aligned on establishing distinct Customer Success, Support, and SRE ro]]*