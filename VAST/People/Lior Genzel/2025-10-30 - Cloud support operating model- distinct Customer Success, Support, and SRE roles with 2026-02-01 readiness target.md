---
type: "projects"
title: "Cloud support operating model: distinct Customer Success, Support, and SRE roles with 2026-02-01 readiness target"
date: "2025-10-30"
project: ""
participants: ["Jason Vallery", "Lior Genzel", "Daniel", "Rob Banga", "Yancey", "Timo Pervane", "Joe", "Kartik", "Nirav", "Rich Shanshee", "Shansi"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-30 - The group aligned on establishing distinct Customer Success, Support, and SRE ro.md"
tags:
  - "type/projects"
  - "project/"
  - "generated"

---

# Cloud support operating model: distinct Customer Success, Support, and SRE roles with 2026-02-01 readiness target

**Date**: 2025-10-30
**Project**: [[]]
**Attendees**: Jason Vallery, Lior Genzel, Daniel, Rob Banga, Yancey, Timo Pervane, Joe, Kartik, Nirav, Rich Shanshee, Shansi

## Summary

The team aligned on a cloud operating model with distinct Customer Success (proactive), Support (reactive), and SRE (24/7 operations and on-call) responsibilities, targeting operational readiness by 2026-02-01. Near-term hyperscaler focus shifted to Microsoft Azure due to demand, with Google Cloud and AWS following, and the group identified key dependencies including Tackle-Salesforce-Polaris integration, Salesforce data hygiene and access controls, and Tableau-based customer telemetry.


## Action Items


- [?] Draft and circulate a simple cloud support plan defining Customer Success, Support, and SRE responsibilities, 24/7 coverage expectations, and phasing from private offers to SaaS. @Rob Banga 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Start recruiting initial SRE and cloud support hires to build the cloud support 'machine' needed for marketplace offers and future SaaS operations. @Rob Banga 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Sync offline to refine the Customer Success, Support, and SRE model and define on-call rotations for cloud operations. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Define Tableau telemetry and analytics requirements for cloud customer views, including churn indicators, feature usage, and required data feeds. @Yancey 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Plan the Tackle-Salesforce-Polaris integration needed for marketplace offers, customer registration, and entitlement and role management. @Yancey 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Confirm leadership for cloud implementations, including aligning with Carl as a potential implementation lead and scoping the initial team. @Rob Banga 📅 2025-11-08 #task #proposed #auto

- [?] Prepare enablement and documentation for Sales Engineers, Support, and Customer Success for cloud offers, including content to present at SKO. @TBD 📅 2025-11-08 #task #proposed #auto

- [?] Define metering evidence requirements and internal control requirements for Polaris hourly usage data with Finance and auditors to support revenue recognition and compliance. @TBD 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Outline the overage policy for private offers and evaluate SaaS pricing unit model options, coordinating with Jason Vallery for product alignment. @Yancey 📅 2025-11-08 #task #proposed #auto

- [?] Schedule and run a Salesforce and Tackle deep-dive to understand current marketplace flows, gaps, and required changes for registration and entitlements. @Cristina Hasson 📅 2025-10-31 ⏫ #task #proposed #auto

- [?] Complete legal review of data custodian obligations, EULA updates, and compliance roadmap including SOC2 and FedRAMP considerations for future SaaS. @TBD 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Attend the Google Cloud meeting to review TPU test setup and defend benchmark results challenged by Google Cloud contacts. @Lior Genzel 📅 2025-11-04 #task #proposed #auto

- [?] Validate Salesforce access and role model for customers and internal users, and define Salesforce data hygiene rules and validation requirements. @TBD 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Confirm hyperscaler prioritization and the near-term target account list for execution across Azure, Google Cloud, and AWS. @Yancey 📅 2025-11-08 #task #proposed #auto




## Decisions


- Adopt a distinct cloud operating model separating Customer Success (proactive), Support (reactive), and SRE (24/7 operations and on-call rotations).

- Prioritize Microsoft Azure opportunities in the near term due to demand, with Google Cloud and AWS following.

- Use Polaris as the metering source of truth with hourly usage reporting for cloud marketplace offers.

- Reaffirm phased cloud marketplace plan: private offers first, public offers 6 to 8 months later, and full multi-tenant SaaS targeted for FY28.

- Prepare cloud enablement and documentation content for SKO.




## Key Information


- The cloud operating model discussed separates responsibilities into Customer Success (proactive best-practices and adoption), Support (reactive ticket handling), and SRE (24/7 operations and on-call rotations for cloud infrastructure).

- The team set a target date of 2026-02-01 to have the cloud support 'machine' operationally ready, including roles, rotations, and processes.

- Marketplace go-to-market is phased: private offers first (approximately 2 months from 2025-10-30), public offers 6 to 8 months after private offers, and a full multi-tenant SaaS offering targeted for FY28.

- Private and public marketplace offers are expected to have the same support model because both are deployed within the customer's cloud tenant; the major support model change occurs with future multi-tenant SaaS, which requires SRE-style operations.

- Hyperscaler prioritization shifted toward Microsoft Azure due to near-term demand and large opportunities; Google Cloud and AWS follow after Azure in near-term execution focus.

- Polaris is intended to be the metering source of truth with hourly usage reporting, and private offers are planned as fixed capacity with an overage model.

- A Tackle-Salesforce-Polaris integration is required to support marketplace flows including customer registration, entitlements, and role management.

- Cloud deployments are expected to generate more networking-related support tickets and fewer or no hardware-related tickets compared to on-prem deployments.

- Google Cloud challenged VAST's TPU test results and requested a meeting to review the exact test setup because results appeared approximately 23% better than Google Managed Lustre; Lior Genzel planned to attend with Kartik to defend the methodology.

- A Google Cloud contact named Shansi, described as having a reporting relationship to Nirav and as someone Lior Genzel worked with during a prior Google first-party offering, is involved in the TPU test review meeting.



---

*Source: [[2025-10-30 - The group aligned on establishing distinct Customer Success, Support, and SRE ro]]*