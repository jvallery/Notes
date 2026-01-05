---
type: "customer"
title: "Kickoff: Tackle onboarding to connect existing GCP Marketplace listing and enable private offers with overage metering"
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

# Kickoff: Tackle onboarding to connect existing GCP Marketplace listing and enable private offers with overage metering

**Date**: 2025-10-29
**Account**: [[]]
**Attendees**: Dave Stryker, Peter Kapsashi, Jonsi Stephenson, Jason Vallery, A.K. Rapsone, Ikki, Huckney, Pali, Jotam, Lior Genzel, Egi

## Summary

VAST and Tackle kicked off onboarding to connect VAST's existing live Google Cloud Marketplace listing to Tackle, enabling private offers first and optionally metered overages. The group aligned on reusing the existing GCP project and product number, required GCP access and reporting exports, and defining subscription event notifications and SSO flow into VAST Polaris. VAST will finalize pricing and overage strategy, update EULA as needed, and map marketplace metadata into Salesforce and Polaris for finance visibility.


## Action Items


- [?] Send Tackle platform invitations to the meeting participants so VAST Data can access onboarding workflows and listing configuration. @Peter Kapsashi 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Provide the Google Cloud project name and Google Cloud Marketplace product number to Tackle for connecting the existing listing. @TBD 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Create and provide a GCP service account JSON key and assign the required IAM roles for Tackle to manage Google Cloud Marketplace integration. @TBD 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Enable Google Cloud Marketplace reporting export and connect the export to Tackle reporting so transactions surface in Tackle. @TBD 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Copy or reuse the existing Google Cloud Marketplace listing content inside Tackle and propose initial plans and metering configuration options. @Peter Kapsashi 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Review the Google Cloud Marketplace listing EULA and update it if needed to align with the Tackle-managed private offer and metering model. @TBD 📅 2025-11-08 #task #proposed #auto

- [?] Define VAST Data pricing and overage strategy for Google Cloud Marketplace private offers, including units, discounting approach, and finance treatment for overages. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Specify the required marketplace metadata that must flow into Salesforce and VAST Polaris so finance can see capacity sold in addition to contract dollar amounts. @A.K. Rapsone 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Outline subscription event notification options and the SSO flow from Google Cloud Marketplace to VAST Polaris for customer access and order fulfillment. @Peter Kapsashi 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Confirm the Polaris endpoints and event schema required to receive subscription and usage events from the marketplace integration. @A.K. Rapsone 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Clarify Google Cloud Marketplace behavior for how private-offer discounts apply to metered overage line items to avoid billing confusion. @Peter Kapsashi 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Share Tackle documentation covering required GCP IAM roles, reporting export setup, and metering APIs for Google Cloud Marketplace. @Peter Kapsashi 📅 2025-11-08 #task #proposed #auto

- [?] Provide examples of multi-meter configurations (for example TB, seats, CPU) and the penny-meter pattern for flexible overage pricing on Google Cloud Marketplace. @Peter Kapsashi 📅 2025-11-08 #task #proposed #auto




## Decisions


- VAST Data will start with Google Cloud Marketplace and connect the existing live listing to Tackle rather than creating a new GCP project or new product listing.

- VAST Data will lead with private offers for initial sales motion, with optional metered overage capability as part of the offer structure.

- Tackle will manage the listing connection and onboarding workflow, including migrating or reusing listing content within the Tackle platform.




## Key Information


- VAST Data is onboarding to Tackle to connect an existing live Google Cloud Marketplace listing and enable private offers with optional metered overages.

- Tackle acts as middleware that connects a SaaS product to hyperscaler marketplaces and can manage listing operations, private offers, and metering integrations.

- The initial cloud marketplace priority for VAST Data in this onboarding is Google Cloud Marketplace, with urgency around listing timelines.

- VAST Data already has a published Google Cloud Marketplace offering and intends to modify and connect that existing listing to Tackle rather than creating a new listing from scratch.

- The agreed sales motion is to start with private offers to cross-sell existing on-prem customers, then expand to public offers and new-logo motion later as the cloud product matures.

- Tackle onboarding for Google Cloud Marketplace requires a GCP service account JSON key and assignment of required IAM roles, plus enabling Google Cloud Marketplace reporting export for transaction reporting into Tackle.

- VAST Data's cloud control plane is called Polaris and must receive subscription/order notifications (for example, private offer fulfillment) to automate or support provisioning and entitlement workflows.

- A.K. Rapsone is VP of Cloud Engineering at VAST Data and owns integration work for the cloud marketplace control plane side, including subscription event ingestion and metadata flows.

- Jonsi Stephenson is GM of Cloud at VAST Data.

- Peter Kapsashi (PK) leads onboarding at Tackle for cloud marketplace selling and previously worked at AWS Marketplace for about 7.5 to 8 years.

- Jason Vallery joined VAST Data about one week before 2025-10-29 to run cloud product management and previously spent 13 years running product for Microsoft's object storage platform.

- Huckney is a principal engineer on Egi's team at VAST Data and will work on integration with endpoints for the marketplace-to-Polaris flow.

- Pali works on Egi's team at VAST Data and will support integration work for the marketplace onboarding.

- A key requirement is mapping marketplace transaction and capacity metadata into Salesforce so finance can understand capacity sold, not only contract dollar amounts.



---

*Source: [[2025-10-29 - Kickoff of VAST’s onboarding to Tackle to connect an existing GCP Marketplace li]]*