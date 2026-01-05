---
type: "projects"
title: "GCP Marketplace MVP launch readiness, private offers via Tackle, fixed capacity pricing and Polaris entitlements"
date: "2025-10-28"
project: ""
participants: ["Eirikur Hrafnsson", "Helen Protopapas", "Jason Ainsworth", "Jonsi Stefansson", "Lihi Rotchild", "Lior Genzel", "Timo Pervane", "Tomer Hagay", "Jason Vallery", "Yancey"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-28 - Team aligned on MVP launch on GCP via private offers with fixed capacity pricing.md"
tags:
  - "type/projects"
  - "project/"
  - "generated"

---

# GCP Marketplace MVP launch readiness, private offers via Tackle, fixed capacity pricing and Polaris entitlements

**Date**: 2025-10-28
**Project**: [[]]
**Attendees**: Eirikur Hrafnsson, Helen Protopapas, Jason Ainsworth, Jonsi Stefansson, Lihi Rotchild, Lior Genzel, Timo Pervane, Tomer Hagay, Jason Vallery, Yancey

## Summary

The team aligned to launch the VAST GCP Marketplace MVP using private offers only, with fixed capacity pricing at $0.07/GB and no BYOL. Tackle.io will generate private offers and sync them to Salesforce, while Polaris will be the source of truth for entitlements, call-home registration, and usage metering. Key remaining work includes overage handling (including EULA language), internal alerting, and finance controls for billing, reconciliation, and reporting ahead of first transactions targeted for Nov-Dec 2025.


## Action Items


- [?] Review and draft marketplace EULA language that enables overage billing at list PAYGO pricing using a Tackle.io workaround for GCP Marketplace private offers. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Invite finance (Jason Vallery) to the Tackle.io kickoff and ongoing implementation meetings for GCP Marketplace private offers. @Eirikur Hrafnsson 📅 2025-10-29 ⏫ #task #proposed #auto

- [?] Confirm with Tackle.io the feasibility and required configuration to support overage handling and pricing for GCP Marketplace private offers (including overage-at-PAYGO behavior). @Eirikur Hrafnsson 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Implement automation to create Uplink organization endpoints from Salesforce metadata to support call-home registration for marketplace customers. @TBD 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Design and implement internal alerting for Customer Success and Sales when customers approach or exceed entitlement limits in Polaris/Uplink. @TBD 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Define the overage policy (thresholds, grace, pricing) and ensure it is reflected in GCP Marketplace offer terms and the marketplace EULA. @Tomer Hagay 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Set up finance processes for GCP Marketplace billing, receivables reconciliation, and revenue recognition for fixed capacity pricing and any overages. @TBD 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Provide finance with access to GCP Marketplace reporting portal and sample or mock payout reports to validate reporting and reconciliation workflows. @Eirikur Hrafnsson 📅 2025-11-08 #task #proposed #auto

- [?] Schedule and run a detailed walkthrough of the end-to-end Tackle.io to Salesforce private offer flow, including data sync fields and system-of-record decisions. @Eirikur Hrafnsson 📅 2025-11-08 #task #proposed #auto

- [?] Define VAST units of measurement for compute and capacity to support a future pricing model beyond the initial fixed capacity MVP. @Tomer Hagay 📅 2025-11-08 #task #proposed #auto

- [?] Plan cloud Customer Success coverage to drive expansion and manage entitlement and usage for marketplace customers. @Lihi Rotchild 📅 2025-11-08 #task #proposed #auto

- [?] Prepare pipeline visibility for expected first GCP Marketplace transactions and associated timelines for Nov-Dec 2025 launch window. @Lior Genzel 📅 2025-11-08 #task #proposed #auto

- [?] Validate the GCP overage-at-PAYGO approach and confirm the Tackle.io configuration path for implementing overage billing behavior. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Set a working session to define billing, invoicing, payout cadence, and reconciliation across Polaris, Tackle.io, and GCP Marketplace. @TBD 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Decide whether to permit automatic expansion beyond entitlement (with overage billing) or require account approval for expansion beyond entitlement in the GCP Marketplace MVP. @TBD 📅 2025-11-08 #task #proposed #auto

- [?] Outline a revenue recognition approach for a future hybrid on-prem to cloud licensing conversion model (including conversion mechanics and accounting treatment). @TBD 📅 2025-11-08 #task #proposed #auto

- [?] Assess feasibility and policy for multi-cloud pooling of entitlements and metadata roll-up to Salesforce for reporting and forecasting. @TBD 📅 2025-11-08 🔽 #task #proposed #auto




## Decisions


- For the GCP Marketplace MVP, VAST will transact exclusively through cloud marketplaces and will not support BYOL (Bring Your Own License).

- VAST will use Tackle.io to generate and manage GCP Marketplace private offers and integrate offer data with Salesforce opportunities.

- The GCP Marketplace MVP will use fixed capacity pricing at $0.07/GB (list price) for private offers.

- Polaris will manage entitlement, call-home registration, and usage reporting for the GCP Marketplace MVP.




## Key Information


- The VAST GCP Marketplace MVP will use fixed capacity pricing with a list price of $0.07 per GB for a fixed term and fixed price private offer.

- For the GCP Marketplace MVP, VAST will transact exclusively through the cloud marketplace and will not support BYOL (Bring Your Own License).

- Tackle.io will be used as middleware to generate GCP Marketplace private offers and sync offer data to Salesforce opportunities.

- Polaris will be the source of truth for customer entitlements, call-home registration, and usage metering for the GCP Marketplace MVP, using token-based enforcement rather than license keys.

- The team is considering an overage allowance (example discussed: 10%) and charging overage at list PAYGO pricing if the marketplace and Tackle.io configuration can support it.

- GCP Marketplace does not natively support overage-at-PAYGO for a fixed capacity private offer, so a Tackle.io workaround may be required.

- Customer-facing alerting exists when customers exceed entitlement limits, but internal CS and sales alerting for approaching or exceeding entitlement was not yet implemented at the time of the meeting.

- Finance intends to embed in the Tackle.io implementation to define billing, receivables reconciliation, reporting controls, and revenue recognition processes before first GCP Marketplace transactions.

- First GCP Marketplace transactions were targeted for Nov-Dec 2025, with an intent to replicate the approach to AWS and Azure after the GCP MVP is operational.

- Finance will not operate a separate cloud P&L; cloud metrics will be reported within the overall company P&L.

- Hybrid on-prem and cloud licensing conversion was identified as a future complexity for revenue recognition and may require a conversion model later.

- Multi-cloud is technically possible, but hyperscalers may resist cross-cloud messaging, creating GTM positioning risk.



---

*Source: [[2025-10-28 - Team aligned on MVP launch on GCP via private offers with fixed capacity pricing]]*