---
type: "customer"
title: "VAST x Tackle GCP onboarding"
date: "2025-10-29"
account: "Google"
participants: ["Dave Stryker", "Peter Kapsashi", "Ikki", "Jonsi Stefansson", "Jason Vallery", "A.K. Rapsone", "Huckney", "Pali", "Jotam"]
source: "transcript"
source_ref: "Inbox/_archive/2025-10-29/2025-10-29 - Tackle and VAST kicked off onboarding to sell VAST’s SaaS via Google Cloud Marke.md"
tags:
  - "type/customer"
  - "account/google"
  - "generated"
---

# VAST x Tackle GCP onboarding

**Date**: 2025-10-29
**Account**: [[Google]]
**Attendees**: Dave Stryker, Peter Kapsashi, Ikki, Jonsi Stefansson, Jason Vallery, A.K. Rapsone, Huckney, Pali, Jotam

## Summary

Tackle and VAST kicked off onboarding to sell VAST’s SaaS via Google Cloud Marketplace, using Tackle as middleware and reusing VAST’s existing private-offer-only GCP listing and project. The group aligned on a fixed-price private offer motion with potential overage metering, discussed meter design (including a penny-based meter), subscription/fulfillment event notifications into VAST’s Polaris control plane, SSO approach, and ensuring offer/entitlement metadata flows into Salesforce. Next steps focus on granting Tackle access (service account + IAM roles), enabling Marketplace reporting export, and populating/updating listing content and pricing policy (including possible EULA refresh).
## Action Items
- [ ] Send Tackle platform invites to all meeting participants @Peter Kapsashi 📅 2025-11-08 🔺 #task
- [ ] Provide GCP project name and product number in Tackle Integrations @A.K. Rapsone 📅 2025-11-08 ⏫ #task
- [ ] Upload GCP service account JSON key for Tackle and grant required IAM roles @A.K. Rapsone 📅 2025-11-08 ⏫ #task
- [ ] Enable Google Marketplace reporting export for Tackle ingestion @A.K. Rapsone 📅 2025-11-08 🔺 #task
- [ ] Pre-populate listing content in Tackle based on the existing GCP listing @Peter Kapsashi 📅 2025-11-08 🔺 #task
- [ ] Review and update listing content (overview, identifiers, support docs) and confirm if EULA needs refresh @Jason Vallery 📅 2025-11-08 ⏫ #task
- [ ] Define pricing and overage policy for private offers (rates, discounts, behavior on expansion) @Jason Vallery 📅 2025-11-08 ⏫ #task
- [ ] Decide on meter design (units, multiple meters, penny-based approach) for overage charging @Jason Vallery 📅 2025-11-08 🔺 #task
- [ ] Design metadata model to tie fixed-price offers to capacity entitlements and map to Salesforce @Jason Vallery 📅 2025-11-08 🔺 #task
- [ ] Define subscription/fulfillment event notification flow from Marketplace to Polaris (including SSO approach) @A.K. Rapsone 📅 2025-11-08 🔺 #task
- [ ] Confirm in GCP whether overage meter discounts can be independent from fixed-price private offer discounts @Peter Kapsashi 📅 2025-11-08 ⏫ #task
- [ ] Share Tackle metering API and CSV upload documentation with VAST @Peter Kapsashi 📅 2025-11-08 🔽 #task
- [ ] Align on Salesforce data fields and integration for passing offer and entitlement metadata @Jason Vallery 📅 2025-11-08 ⏫ #task

## Decisions
- Start with Google Cloud Marketplace first; public offers may follow later.
- Reuse the existing GCP listing and project; do not create a new GCP project.
- Initial sales motion will be private offers; Tackle will be used for technical integration and listing content population.

## Key Information
- VAST already has a live private-offer-only listing on Google Cloud Marketplace; Producer Portal and Google Payments are set up.
- Tackle requires a GCP service account JSON key and specific IAM roles to list and meter on VAST’s behalf; Google’s required roles are broad and may raise security/compliance concerns.
- Marketplace reporting export must be enabled so Tackle can ingest reporting rather than relying on manual CSV downloads.
- Target commercial model is fixed-price private offers per deal, with a desire to support overage charging when usage exceeds contracted capacity.
- Tackle supports overage metering, per-offer discounts, multiple meters, and a penny-based meter approach to simplify variable pricing.
- Google displays fixed prices as monthly equivalents even if billed upfront/annually; private offers can control payment cadence.
- VAST’s Polaris control plane needs subscription/fulfillment event notifications and entitlement metadata to gate expansion and track usage.
- Salesforce linkage is needed so fixed contract dollar amounts map to capacity/entitlements (e.g., TB).
- Legal may need to refresh/review the EULA because the listing was created ~1–2 years prior.

---

*Source: [[Inbox/_archive/2025-10-29/2025-10-29 - Tackle and VAST kicked off onboarding to sell VAST’s SaaS via Google Cloud Marke.md|2025-10-29 - Tackle and VAST kicked off onboarding to sell VAST’s SaaS via Google Cloud Marke]]*

## Related

- [[Jonsi Stephenson]]
- [[Lior Genzel]]
