---
type: customer
title: Tackle onboarding kickoff to sell VAST SaaS via Google Cloud Marketplace (reuse existing private offer listing)
date: '2025-10-29'
account: Google
participants:
- Dave Stryker
- Peter Kapsashi
- Ikki
- Jonsi Stephenson
- Jason Vallery
- A.K. Rapsone
- Huckney
- Pali
- Jotam
- Lior Genzel
- Egi
source: transcript
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-29 - Tackle and VAST kicked off onboarding to sell VAST’s SaaS via Google Cloud Marke.md
tags:
- type/customer
- generated
---

# Tackle onboarding kickoff to sell VAST SaaS via Google Cloud Marketplace (reuse existing private offer listing)

**Date**: 2025-10-29
**Account**: [[Google]]
**Attendees**: Dave Stryker, Peter Kapsashi, Ikki, Jonsi Stephenson, Jason Vallery, A.K. Rapsone, Huckney, Pali, Jotam

## Summary

VAST Data and Tackle kicked off onboarding to sell VAST SaaS through Google Cloud Marketplace using Tackle as middleware. The group aligned to start with GCP by reusing VAST's existing private-offer-only listing and GCP project, then connect Tackle via a GCP service account and IAM roles, enable reporting export, and design metering, entitlement metadata, and subscription event notifications into VAST Polaris and Salesforce.

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

- [?] Send Tackle platform invites to all meeting participants so VAST Data can access the Tackle onboarding workspace for Google Cloud Marketplace integration. @Peter Kapsashi 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Provide the existing GCP project name and Google Cloud Marketplace product number in Tackle Integrations to ensure Tackle connects to the correct existing listing. @A.K. Rapsone 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Upload the GCP service account JSON key for Tackle and grant the required GCP IAM roles so Tackle can list and meter on VAST Data's behalf for Google Cloud Marketplace. @A.K. Rapsone 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Enable Google Cloud Marketplace reporting export so Tackle can ingest reporting data for billing and analytics. @A.K. Rapsone 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Pre-populate listing content in Tackle based on VAST Data's existing Google Cloud Marketplace private-offer listing to accelerate onboarding. @Peter Kapsashi 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Review and update Google Cloud Marketplace listing content (overview, identifiers, support documentation) and confirm whether the marketplace EULA needs a refresh before expanding sales motion. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Define VAST Data pricing policy for Google Cloud Marketplace private offers, including overage behavior when customers expand beyond contracted capacity, and how finance will handle overage billing versus requiring a new private offer. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Decide on overage meter design for Google Cloud Marketplace, including unit labels, whether to use multiple meters (for example TB, seats, CPU), and whether to use a penny-based meter to simplify variable pricing. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Design the entitlement and metadata model that ties fixed-price private offers to capacity entitlements (for example TB) and maps those entitlements and offer identifiers into Salesforce for reporting and fulfillment. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Define the subscription and fulfillment event notification flow from Google Cloud Marketplace into VAST Polaris control plane, including the SSO approach for buyer access and how entitlements are enforced. @A.K. Rapsone 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Confirm in Google Cloud Marketplace whether overage meter discounts can be configured independently from fixed-price private offer discounts, to support separate commercial levers for base contract and overage. @Peter Kapsashi 📅 2025-11-08 #task #proposed #auto

- [?] Share Tackle metering API documentation and CSV upload documentation with VAST Data engineering so VAST can implement metering and reporting integration correctly. @Peter Kapsashi 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Align on Salesforce data fields and integration approach for passing Google Cloud Marketplace offer identifiers, contract values, and entitlement metadata from Tackle and/or Polaris into Salesforce. @Myself 📅 2025-11-08 #task #proposed #auto

## Decisions

- Start onboarding with Google Cloud Marketplace as the first priority for selling VAST SaaS via Tackle; public offers may follow later.

- Reuse the existing Google Cloud Marketplace listing and the existing GCP project and product number, rather than creating a new GCP project.

- Use private offers as the initial sales motion, with Tackle supporting listing content population and technical integration once access is granted.

- Start onboarding with Google Cloud Marketplace first, using Tackle as middleware for listing and metering.

- Reuse the existing Google Cloud Marketplace private-offer listing and the existing GCP project and product number, and do not create a new GCP project.

- Use private offers as the initial sales motion, and explore adding overage metering for usage beyond contracted entitlements.

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

- Peter Kapsashi ("PK") leads cloud marketplace onboarding at Tackle and previously worked at AWS Marketplace for about 7.5 to 8 years.

- Jason Vallery joined VAST Data about one week before 2025-10-29 and is responsible for cloud product, including structuring cloud offers and pricing; he previously spent 13 years running product for Microsoft's object storage platform.

- VAST Data already has a published Google Cloud Marketplace offering that is private-offer oriented, and the plan is to modify and reuse it rather than create a new listing.

- The onboarding approach is to start with Google Cloud Marketplace first and reuse the existing GCP project and product number, rather than creating a new GCP project.

- Tackle acts as middleware between VAST Data and hyperscaler marketplaces, supporting listing, order notifications, fulfillment workflows, and metering, with the ability to automate fulfillment over time.

- VAST Polaris is VAST Data's control plane and needs to receive marketplace subscription and fulfillment event notifications to gate access, manage entitlements, and track usage.

- The initial commercial motion discussed is fixed-price private offers per deal, with a desire to support overage charging when usage exceeds contracted capacity; this requires internal VAST policy and finance handling decisions.

- Salesforce metadata linkage is required so fixed contract dollar amounts from private offers can map to capacity entitlements (for example, TB) for fulfillment and reporting.
