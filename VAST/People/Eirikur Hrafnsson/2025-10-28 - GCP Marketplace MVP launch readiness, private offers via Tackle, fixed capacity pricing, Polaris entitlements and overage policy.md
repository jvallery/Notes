---
type: "projects"
title: "GCP Marketplace MVP launch readiness, private offers via Tackle, fixed capacity pricing, Polaris entitlements and overage policy"
date: "2025-10-28"
project: ""
participants: ["Eirikur Hrafnsson", "Helen Protopapas", "Jason Ainsworth", "Jonsi Stephenson", "Lihi Rotchild", "Lior Genzel", "Timo Pervane", "Tomer Hagay", "Jason Vallery", "Yancey"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-28 - Team aligned on MVP launch on GCP via private offers with fixed capacity pricing.md"
tags:
  - "type/projects"
  - "project/"
  - "generated"

---

# GCP Marketplace MVP launch readiness, private offers via Tackle, fixed capacity pricing, Polaris entitlements and overage policy

**Date**: 2025-10-28
**Project**: [[]]
**Attendees**: Eirikur Hrafnsson, Helen Protopapas, Jason Ainsworth, Jonsi Stephenson, Lihi Rotchild, Lior Genzel, Timo Pervane, Tomer Hagay, Jason Vallery, Yancey

## Summary

The team aligned to launch the VAST GCP Marketplace MVP using private offers only, with fixed capacity pricing at $0.07/GB and no BYOL. Tackle.io will generate private offers and sync them to Salesforce, while Polaris will be the system of record for entitlement, call-home registration, and usage metering. Open work includes finalizing overage handling (potentially 10% allowance) and EULA language, plus finance controls for billing, reconciliation, and reporting ahead of first transactions targeted for Nov-Dec 2025.


## Action Items


- [?] Review and draft marketplace EULA language that enables overage billing at PAYGO list pricing (if supported) for GCP Marketplace private offers using the Tackle.io workaround. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Invite finance (Jason Vallery) to the Tackle.io kickoff and ongoing implementation meetings for GCP Marketplace private offers. @Eirikur Hrafnsson 📅 2025-10-29 ⏫ #task #proposed #auto

- [?] Confirm with Tackle.io the feasibility and required configuration to support overage handling and pricing for GCP Marketplace private offers, given GCP Marketplace limitations on overage-at-PAYGO. @Eirikur Hrafnsson 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Implement automation to create Uplink organization endpoints from Salesforce metadata to support customer call-home registration into Polaris without manual setup. @TBD 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Design and implement internal alerting for Customer Success and Sales when customers approach or exceed entitlement limits, using Polaris and/or Uplink dashboards. @TBD 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Define the overage policy for the GCP Marketplace MVP, including thresholds (example discussed: 10%), grace behavior, and pricing, and ensure it is reflected in offer terms and EULA language. @Tomer Hagay 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Set up finance processes for marketplace billing, receivables reconciliation, reporting controls, and revenue recognition for fixed capacity pricing and any overage charges for GCP Marketplace transactions. @TBD 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Provide finance with access to GCP Marketplace reporting and portal views, including sample or mock payout reports needed for reconciliation and forecasting. @Eirikur Hrafnsson 📅 2025-11-08 #task #proposed #auto

- [?] Schedule and run a detailed walkthrough of the end-to-end Tackle.io to Salesforce private offer flow, including data sync fields and operational handoffs. @Eirikur Hrafnsson 📅 2025-11-08 #task #proposed #auto

- [?] Define VAST units of measurement for compute and capacity to support a future unit-based pricing model beyond the initial fixed capacity MVP pricing. @Tomer Hagay 📅 2025-11-08 #task #proposed #auto

- [?] Plan cloud Customer Success coverage to drive expansion and manage entitlement and usage for GCP Marketplace customers post-launch. @Lihi Rotchild 📅 2025-11-08 #task #proposed #auto

- [?] Prepare pipeline visibility for expected first GCP Marketplace transactions, including target timing (Nov-Dec 2025) and key dependencies for launch readiness. @Lior Genzel 📅 2025-11-08 #task #proposed #auto

- [?] Validate the proposed GCP overage-at-PAYGO approach and confirm the Tackle.io configuration path for implementing overage billing behavior. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Decide whether the GCP Marketplace MVP will permit automatic expansion beyond entitlement (with overage billing) or require account approval before expansion. @TBD 📅 2025-11-08 #task #proposed #auto

- [?] Outline the revenue recognition approach for a future hybrid on-prem to cloud licensing conversion model, including operational process implications. @TBD 📅 2025-11-08 #task #proposed #auto

- [?] Assess feasibility and policy for multi-cloud pooling and metadata roll-up to Salesforce for pricing, entitlement, and reporting across hyperscalers. @TBD 📅 2025-11-08 🔽 #task #proposed #auto




## Decisions


- VAST will transact the GCP Marketplace MVP exclusively through cloud marketplaces and will not support BYOL for the MVP launch.

- VAST will use Tackle.io to generate and manage GCP Marketplace private offers and integrate offer data with Salesforce opportunities.

- The GCP Marketplace MVP will use fixed capacity pricing at $0.07/GB for a fixed term and fixed price.

- Polaris will manage entitlement, call-home registration, and usage reporting for marketplace transactions, using token-based entitlements rather than license keys.

- The team will pursue an overage concept and investigate charging overage at PAYGO list pricing via a Tackle.io workaround due to GCP Marketplace limitations.




## Key Information


- VAST's GCP Marketplace MVP will use fixed capacity pricing at $0.07 per GB for a fixed term and fixed price, sold via GCP Marketplace private offers.

- For the GCP Marketplace MVP, VAST will transact exclusively through the marketplace and will not support BYOL (Bring Your Own License).

- Tackle.io will be used as middleware to generate GCP Marketplace private offers and sync offer data to Salesforce opportunities.

- Polaris will be the source of truth for customer entitlements, call-home registration, and usage metering for marketplace transactions, using token-based entitlements rather than license keys.

- GCP Marketplace does not natively support charging overage at PAYGO list pricing, and the team is investigating whether Tackle.io can provide a workaround.

- The team is considering an overage allowance concept (example discussed: 10% over entitlement) and needs marketplace offer terms and EULA language to enforce overage billing.

- Customer alerting exists when customers exceed entitlement limits, but internal CS and sales alerting for approaching or exceeding entitlement is not yet implemented.

- Finance will embed in the Tackle.io implementation to define billing, reconciliation, reporting controls, and revenue recognition processes for marketplace transactions.

- VAST plans to replicate the GCP Marketplace MVP approach to AWS and Azure after initial GCP transactions targeted for Nov-Dec 2025.

- Hybrid on-prem and cloud licensing conversion is expected to create complex revenue recognition requirements, and a conversion model may be needed later.

- Multi-cloud pooling is technically possible, but hyperscalers may resist cross-cloud messaging and positioning.

- Finance will not create a separate cloud P&L; cloud metrics will be reported within the overall company P&L.



---

*Source: [[2025-10-28 - Team aligned on MVP launch on GCP via private offers with fixed capacity pricing]]*