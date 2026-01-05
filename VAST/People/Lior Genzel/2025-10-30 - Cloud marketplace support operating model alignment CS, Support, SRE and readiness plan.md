---
type: "projects"
title: "Cloud marketplace support operating model alignment (CS, Support, SRE) and readiness plan"
date: "2025-10-30"
project: ""
participants: ["Jason Vallery", "Lior Genzel", "Yancey", "Rob Banga", "Daniel", "Timo Pervane", "Christina Hasson"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-30 - The group aligned on the cloud support operating model (Customer Success, Suppor.md"
tags:
  - "type/projects"
  - "project/"
  - "generated"

---

# Cloud marketplace support operating model alignment (CS, Support, SRE) and readiness plan

**Date**: 2025-10-30
**Project**: [[]]
**Attendees**: Jason Vallery, Lior Genzel, Yancey, Rob Banga, Daniel, Timo Pervane, Christina Hasson

## Summary

The team aligned on a cloud support operating model that separates proactive Customer Success, reactive Support, and 24/7 SRE on-call, with an operational readiness target of 2026-02-01. They confirmed hyperscaler priority order (GCP, then Azure, then AWS), a phased marketplace rollout (private offers first, then public offers, then SaaS in FY28), and identified key gating workstreams including Tackle-Salesforce-Polaris integrations, telemetry and analytics, and legal/compliance readiness. GCP challenged VAST TPU test results, and the team planned a review meeting with GCP stakeholders to defend methodology and results.


## Action Items


- [?] Draft a clear cloud support operating plan covering Customer Success, Support, and SRE responsibilities, including 24/7 support desk coverage and on-call rotations, aligned to private and public marketplace phases. @Rob Banga 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Begin recruiting initial SREs and support engineers with hyperscaler experience (Google Cloud Platform, Microsoft Azure, Amazon Web Services) to meet the 2026-02-01 readiness target. @Rob Banga 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Schedule an offline working session with Rob Banga to detail the SRE and support model and capture lessons learned from prior hyperscaler experiences (Microsoft and Oracle Cloud Infrastructure were referenced in notes). @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Schedule a Salesforce and Tackle integration deep-dive to cover customer registration, entitlements, and end-to-end data flows required for marketplace operations. @Christina Hasson 📅 2025-10-31 ⏫ #task #proposed #auto

- [?] Define the telemetry and metrics that must be pushed from Polaris into Tableau to support churn risk, feature utilization, and cloud customer health views. @Yancey 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Scope reporting and analytics needed for consumption forecasting for cloud marketplace offers and ensure resourcing is assigned. @Joe 📅 2025-11-08 #task #proposed #auto

- [?] Assess and confirm additional Salesforce and Tableau licenses or seats required to support cloud operations and marketplace workflows. @Timo Pervane 📅 2025-11-08 #task #proposed #auto

- [?] Evaluate Carl as the initial leader for cloud implementation and support, and define the initial team structure and responsibilities. @Rob Banga 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Propose a role-based access control and data segmentation model across Salesforce, Polaris, and support tooling to address data hygiene and customer experience risks. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Prepare an enablement and documentation plan for both end-customer usage and sell-to-hyperscaler motions, including content to be delivered at SKO. @Product Marketing 📅 2025-11-08 #task #proposed #auto

- [?] Consolidate notes and circulate action items from the 2025-10-30 cloud support operating model session to all participants. @Daniel 📅 2025-10-31 🔽 #task #proposed #auto

- [?] Initiate a legal and compliance workstream to define data custodian obligations for a future SaaS offering and to define the SOC 2 and FedRAMP certification path. @Legal 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Attend the Google Cloud meeting to defend TPU test methodology and results with Google stakeholders (Nirav and Rich Shanshee were named in notes). @Yancey 📅 2025-11-04 ⏫ #task #proposed #auto

- [?] Confirm the target customer list and proof-of-concept sequencing by hyperscaler, including Microsoft (MAI), UKMET via Microsoft, NBCU, Sigma, Jump Trading, Citadel, and Zoom exploring AWS. @Yancey 📅 2025-11-08 #task #proposed #auto

- [?] Define overage policy mechanics for private marketplace offers, including thresholds, pricing approach, and billing mechanics. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Detail metering, entitlement, and billing integration flows between Polaris, hyperscaler marketplaces, and ERP, including hourly utilization aggregation. @Yancey 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Plan SKO sessions for cloud go-to-market, the cloud support model, and SE enablement, and confirm deliverables and owners. @Benoit 📅 2025-11-08 #task #proposed #auto




## Decisions


- Prioritize hyperscaler execution order for VAST cloud marketplace as Google Cloud Platform first, Microsoft Azure second, and Amazon Web Services third.

- Proceed with a phased cloud marketplace rollout: private offers first, then public offers 6 to 8 months later, and plan for a full multi-tenant SaaS offering as an FY28 activity.

- Adopt a separated cloud operating model with proactive Customer Success, reactive Support, and 24/7 SRE on-call coverage.

- Target cloud support operational readiness (people, process, tooling) by 2026-02-01.

- Treat support requirements as the same for private offers and public offers because both are deployed in the customer tenant (not VAST-hosted SaaS).




## Key Information


- The hyperscaler priority order for VAST cloud marketplace efforts is Google Cloud Platform first, Microsoft Azure second, and Amazon Web Services third.

- The cloud marketplace rollout plan is phased: private offers are expected to start about two months after 2025-10-30, public offers are expected 6 to 8 months after private offers, and a full multi-tenant SaaS offering is targeted as an FY28 activity.

- For private and public marketplace offers, VAST cloud delivery is deployed inside the customer tenant (not VAST-hosted SaaS), with no hardware shipped, and the team expects significant networking complexity that may increase support ticket volume.

- The agreed cloud support operating model separates proactive Customer Success, reactive Support, and 24/7 SRE on-call coverage, with SRE responsibilities increasing materially for a future multi-tenant SaaS model.

- The operational readiness target date for the cloud support machine (processes, staffing, tooling) is 2026-02-01.

- Tackle will integrate with Salesforce for marketplace operations, and Polaris is the source of truth for metering and billing; metering is planned as hourly utilization with aggregates sent to hyperscalers and ERP.

- Cloud analytics requirements include Tableau dashboards for churn risk, feature usage, and consumption forecasting based on telemetry pushed from Polaris.

- Legal and compliance work is required to define data custodian obligations for a future SaaS offering and to define a SOC 2 and FedRAMP certification path.

- Google Cloud stakeholders challenged VAST TPU test results as 'too good to be true' and requested a review meeting; the challenge referenced a claim of about 23% better performance than Google Managed Lustre in their internal comparison.

- Jason Vallery stated that a future SaaS model requires a full SRE function because teams must manage infrastructure and deployments in a multi-tenant environment and be responsible for multiple customers simultaneously.



---

*Source: [[2025-10-30 - The group aligned on the cloud support operating model (Customer Success, Suppor]]*