---
type: "customer"
title: "Tackle onboarding kickoff to connect VAST existing GCP Marketplace listing and enable private offers with overage metering"
date: "2025-10-29"
account: ""
participants: ["Dave Stryker", "Peter Kapsashi", "Jonsi Stephenson", "Jason Vallery", "A.K. Rapsone", "Ikki", "Huckney", "Pali", "Jotam", "Lior Genzel", "Egi"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-29 - Kickoff of VAST’s onboarding to Tackle to connect an existing GCP Marketplace li.md"
tags:
  - "type/customer"
  - "account/"
  - "generated"

---

# Tackle onboarding kickoff to connect VAST existing GCP Marketplace listing and enable private offers with overage metering

**Date**: 2025-10-29
**Account**: [[]]
**Attendees**: Dave Stryker, Peter Kapsashi, Jonsi Stephenson, Jason Vallery, A.K. Rapsone, Ikki, Huckney, Pali, Jotam, Lior Genzel, Egi

## Summary

VAST and Tackle kicked off onboarding to connect VAST's existing live Google Cloud Marketplace listing to Tackle, enabling private offers first and optionally metered overages. The group aligned on reusing the existing GCP project and product number, required GCP service account and IAM access, reporting export, and defining subscription event notifications and SSO flow into VAST Polaris. VAST will finalize pricing and overage strategy, review the listing EULA, and define metadata mapping into Salesforce and Polaris for finance visibility.


## Action Items


- [?] Send Tackle platform invitations to the meeting participants so VAST can access the Tackle onboarding workspace. @Peter Kapsashi 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Provide the existing GCP project name and Google Cloud Marketplace product number to Tackle for integration setup, ensuring the existing listing is reused. @TBD 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Create or provide a GCP service account JSON key and assign the required GCP IAM roles to enable Tackle to manage the Google Cloud Marketplace listing and reporting integration. @TBD 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Enable Google Cloud Marketplace reporting export and connect the export to Tackle so transactions and usage can be reported in Tackle. @TBD 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Copy the existing Google Cloud Marketplace listing content into Tackle and propose initial plans and metering configuration (including fixed price plus overage options). @Peter Kapsashi 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Review and update the Google Cloud Marketplace listing EULA as needed to support the Tackle-managed listing, private offers, and any metering terms. @TBD 📅 2025-11-08 #task #proposed #auto

- [?] Define VAST's private offer pricing and overage strategy for Google Cloud Marketplace, including meter units, discounting approach, and finance treatment of overages. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Specify the required metadata fields that must flow into Salesforce and Polaris so finance can track capacity sold (for example TB, seats, CPU) in addition to contract dollars. @A.K. Rapsone 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Outline subscription event notification options and SSO flow options from Google Cloud Marketplace into VAST Polaris, including what events are emitted and how VAST should fulfill orders. @Peter Kapsashi 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Confirm the Polaris endpoints and event schema required to receive subscription and usage events from the marketplace integration. @A.K. Rapsone 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Clarify Google Cloud Marketplace behavior for how private-offer discounts apply to metered overage line items to avoid billing confusion. @Peter Kapsashi 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Share Tackle documentation for GCP IAM roles, reporting export setup, and metering APIs with VAST Cloud Engineering. @Peter Kapsashi 📅 2025-11-08 #task #proposed #auto

- [?] Provide examples of multi-meter configurations (for example TB, seats, CPU) and the penny-meter pattern for flexible discounting and overage handling on Google Cloud Marketplace. @Peter Kapsashi 📅 2025-11-08 #task #proposed #auto




## Decisions


- VAST Data will start with Google Cloud Marketplace and reuse the existing live listing, including reusing the existing GCP project and product number, rather than creating a new GCP project.

- VAST Data will lead with private offers for the initial sales motion on Google Cloud Marketplace, with optional metered overage capability; a public offer can follow later.

- Tackle will manage the marketplace integration workflow, including listing content migration into Tackle and configuration for private offers and metering.




## Key Information


- VAST Data has an existing live Google Cloud Marketplace listing and intends to connect that existing listing to Tackle rather than creating a new listing or GCP project.

- Tackle acts as middleware between VAST Data and hyperscaler marketplaces, managing listing operations, private offers, and metering integrations as a service.

- The initial go-to-market motion for VAST Data on Google Cloud Marketplace is private offers to cross-sell existing on-prem customers, with a public offer later.

- Tackle onboarding for GCP requires a GCP service account JSON key and assignment of required IAM roles, plus enabling Google Cloud Marketplace reporting export for transaction reporting into Tackle.

- VAST Data's cloud control plane is named Polaris and needs to receive subscription lifecycle events (for example, private offer acceptance and fulfillment) and potentially usage events from the marketplace integration.

- Peter Kapsashi (PK) has 7.5 to 8 years of AWS Marketplace experience and has been at Tackle for about 4.5 years, serving as a multi-cloud marketplace onboarding and integration lead.

- Jason Vallery joined VAST Data about one week before this meeting and previously spent 13 years running product for Microsoft's object storage platform, bringing deep marketplace and cloud offer experience.

- A.K. Rapsone is VP of Cloud Engineering at VAST Data and owns integration work for the cloud marketplace control plane, including subscription event notifications, SSO flow, and Salesforce metadata mapping needs.

- Tackle can support fixed-price contracts with metered overage, and can support multiple meters (for example TB, PB, seats, CPU), but Google Cloud Marketplace prefers clear units; a penny-meter pattern was suggested for flexibility and discounting.

- VAST Data needs Salesforce metadata mapping so finance can see capacity sold (for example TB or seats) rather than only contract dollar amounts from marketplace transactions.

- The GCP Marketplace listing EULA may require legal review and updates as part of connecting the listing to Tackle and enabling private offers and metering.



---

*Source: [[2025-10-29 - Kickoff of VAST’s onboarding to Tackle to connect an existing GCP Marketplace li]]*