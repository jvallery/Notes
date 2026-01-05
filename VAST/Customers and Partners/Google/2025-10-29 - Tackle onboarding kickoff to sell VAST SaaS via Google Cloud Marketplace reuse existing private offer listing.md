---
type: "customer"
title: "Tackle onboarding kickoff to sell VAST SaaS via Google Cloud Marketplace (reuse existing private offer listing)"
date: "2025-10-29"
account: ""
participants: ["Dave Stryker", "Peter Kapsashi", "Ikki", "Jonsi Stephenson", "Jason Vallery", "A.K. Rapsone", "Huckney", "Pali", "Jotam"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-29 - Tackle and VAST kicked off onboarding to sell VAST’s SaaS via Google Cloud Marke.md"
tags:
  - "type/customer"
  - "account/"
  - "generated"

---

# Tackle onboarding kickoff to sell VAST SaaS via Google Cloud Marketplace (reuse existing private offer listing)

**Date**: 2025-10-29
**Account**: [[]]
**Attendees**: Dave Stryker, Peter Kapsashi, Ikki, Jonsi Stephenson, Jason Vallery, A.K. Rapsone, Huckney, Pali, Jotam

## Summary

VAST Data and Tackle kicked off onboarding to sell VAST’s SaaS through Google Cloud Marketplace using Tackle as middleware. The group aligned to start with GCP by reusing VAST’s existing private-offer-only listing and GCP project, then integrate Marketplace subscription events and entitlement metadata into VAST’s Polaris control plane and Salesforce for fulfillment, reporting, and overage handling.


## Action Items


- [?] Send Tackle platform invites to all meeting participants so VAST can access onboarding workflows and listing setup. @Peter Kapsashi 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Provide the existing GCP project name and Google Cloud Marketplace product number in Tackle Integrations so Tackle can connect to the correct listing. @A.K. Rapsone 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Upload the GCP service account JSON key for Tackle and grant the required IAM roles so Tackle can list and meter on VAST’s behalf in Google Cloud Marketplace. @A.K. Rapsone 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Enable Google Cloud Marketplace reporting export for Tackle ingestion to support reporting and reconciliation. @A.K. Rapsone 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Pre-populate listing content in Tackle based on VAST’s existing Google Cloud Marketplace listing to accelerate onboarding. @Peter Kapsashi 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Review and update Google Cloud Marketplace listing content (overview, identifiers, support documentation) and confirm whether the Marketplace EULA needs a refresh. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Define VAST policy for private offer pricing and overage behavior, including rates, discounts, and what happens when customers expand beyond contracted capacity (overage charge vs. new private offer). @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Decide on overage meter design for Google Cloud Marketplace via Tackle, including units, whether to use multiple meters, and whether to use a penny-based meter approach. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Design the entitlement and metadata model that ties fixed-price private offers to capacity entitlements (for example TB) and maps the same metadata into Salesforce for reporting and fulfillment. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Define the subscription and fulfillment event notification flow from Google Cloud Marketplace (via Tackle) into VAST Polaris, including the SSO approach for buyer access. @A.K. Rapsone 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Confirm in Google Cloud Marketplace whether overage meter discounts can be independent from fixed-price private offer discounts. @Peter Kapsashi 📅 2025-11-08 #task #proposed #auto

- [?] Share Tackle metering API documentation and CSV upload documentation with VAST so engineering can implement metering and reporting flows. @Peter Kapsashi 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Align on Salesforce data fields and integration approach for passing offer identifiers and entitlement metadata so fixed contract values can be mapped to capacity entitlements. @Myself 📅 2025-11-08 #task #proposed #auto




## Decisions


- Start onboarding with Google Cloud Marketplace as the first priority for selling VAST SaaS via Tackle; public offers may follow later.

- Reuse the existing Google Cloud Marketplace listing and the existing GCP project and product number, rather than creating a new GCP project.

- Use private offers as the initial sales motion, with Tackle supporting listing content population and technical integration once access is granted.




## Key Information


- Dave Stryker is the County Executive at Tackle and has been working with Lior Genzel and Ikki on the early phase of the VAST Data and Tackle partnership.

- Peter Kapsashi (PK) leads onboarding for vendors selling through cloud marketplaces at Tackle and previously worked at AWS Marketplace for about 7.5 to 8 years.

- Jonsi Stephenson is the GM of Cloud at VAST Data.

- Jason Vallery joined VAST Data around 2025-10-22 and runs product for VAST’s cloud offerings; he previously spent about 13 years running product for Microsoft’s object storage platform (Azure).

- A.K. Rapsone is VP of Cloud Engineering at VAST Data and owns integration work for the Cloud Marketplace control plane.

- VAST Data already has a published Google Cloud Marketplace offering that is private-offer-only, and the team intends to reuse it rather than create a new listing.

- The onboarding plan is to start with Google Cloud Marketplace first, then expand to other hyperscaler marketplaces later using Tackle’s middleware platform.

- VAST’s control plane is called Polaris and needs to receive Marketplace subscription and fulfillment event notifications to fulfill orders and gate entitlements.

- Initial go-to-market motion discussed is fixed-price private offers per deal, with a desire to support overage charging when usage exceeds contracted capacity.



---

*Source: [[2025-10-29 - Tackle and VAST kicked off onboarding to sell VAST’s SaaS via Google Cloud Marke]]*