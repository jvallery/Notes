---
type: customer
title: VAST Tackle GCP onboarding kickoff
date: '2025-10-29'
account: Google
participants:
- Dave Stryker
- Peter Kapsashi
- Jonsi Stefansson
- Jason Vallery
- A.K. Rapsone
- Ikki
- Huckney
- Pali
- Jotam
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-10-29 - Kickoff of VAST’s onboarding to
  Tackle to connect an existing GCP Marketplace li.md
tags:
- type/customer
- account/google
- generated
---

# VAST Tackle GCP onboarding kickoff

**Date**: 2025-10-29
**Account**: [[Google]]
**Attendees**: Dave Stryker, Peter Kapsashi, Jonsi Stefansson, Jason Vallery, A.K. Rapsone, Ikki, Huckney, Pali, Jotam

## Summary

Kickoff meeting to onboard VAST’s existing Google Cloud Marketplace listing into Tackle to enable private offers and optional metered overages, while reusing the current GCP project and product number. Key discussion areas included required GCP access (service account JSON key, IAM roles, reporting export), pricing/overage strategy (including a “penny-meter” approach), and defining subscription event notifications/SSO and metadata flow into Salesforce and VAST’s Polaris control plane.
## Action Items
- [ ] Send Tackle platform invitations to meeting participants @Peter Kapsashi 📅 2025-11-08 🔺 #task #proposed
- [ ] Provide GCP project name and product number in Tackle integrations @TBD 📅 2025-11-08 ⏫ #task #proposed
- [ ] Create/provide GCP service account JSON key and assign required IAM roles for Tackle @TBD 📅 2025-11-08 ⏫ #task #proposed
- [ ] Enable GCP Marketplace reporting export and connect it to Tackle @TBD 📅 2025-11-08 🔺 #task #proposed
- [ ] Copy existing GCP listing content into Tackle and propose plans/metrics configuration @Peter Kapsashi 📅 2025-11-08 🔺 #task #proposed
- [ ] Review and update the GCP listing EULA if needed @TBD 📅 2025-11-08 ⏫ #task #proposed
- [ ] Define pricing and overage strategy (units, discounts, finance treatment) for private offers @Myself 📅 2025-11-08 ⏫ #task #proposed
- [ ] Specify required metadata for Salesforce and Polaris to reflect capacity sold vs dollar amounts @A.K. Rapsone 📅 2025-11-08 🔺 #task #proposed
- [ ] Outline subscription event notifications and SSO flow options from marketplace to Polaris @Peter Kapsashi 📅 2025-11-08 🔺 #task #proposed
- [ ] Confirm Polaris endpoints and schema to receive subscription and usage events @A.K. Rapsone 📅 2025-11-08 🔺 #task #proposed
- [ ] Clarify Google behavior on applying private-offer discounts to metered overage lines @Peter Kapsashi 📅 2025-11-08 🔺 #task #proposed
- [ ] Share Tackle documentation for GCP IAM roles, reporting setup, and metering APIs @Peter Kapsashi 📅 2025-11-08 ⏫ #task #proposed
- [ ] Provide examples of multi-meter configurations (TB, seats, CPU) and penny-meter pattern @Peter Kapsashi 📅 2025-11-08 ⏫ #task #proposed

## Decisions
- Reuse the existing GCP Marketplace listing and existing GCP project/product number (no new project).
- Launch with a private offer–led sales motion; enable metering for overages as needed.
- Use Tackle as middleware to manage listing integration/migration and support private offers and metering.

## Key Information
- Starting cloud is Google Cloud (GCP) and VAST already has a live Marketplace listing.
- Tackle requires a GCP service account JSON key plus broad IAM roles to manage listing/metering on VAST’s behalf.
- GCP Marketplace reporting export must be enabled to feed Tackle reporting.
- VAST’s Polaris control plane needs subscription/usage event notifications; SSO flow from Marketplace to SaaS must be defined.
- Finance/Salesforce needs metadata mapping to represent capacity sold (e.g., TB/PB) vs dollar-only contract amounts.
- Tackle supports fixed-price contracts plus metered overage; overage can be discounted per private offer; a penny-meter approach was suggested for flexibility.
- Multiple meters are supported (e.g., TB, seats, CPU), but Google prefers clear customer-friendly units.
- Risks noted: access/roles delays, unclear discount behavior for overages, incomplete metadata mapping, IAM role security review, and unfinished SSO/event flow.

---

*Source: [[Inbox/_archive/2025-10-29/2025-10-29 - Kickoff of VAST’s onboarding to Tackle to connect an existing GCP Marketplace li.md|2025-10-29 - Kickoff of VAST’s onboarding to Tackle to connect an existing GCP Marketplace li]]*

## Related

- [[Microsoft]]
- [[Amazon]]
- [[VAST]]
- [[Cloud control plane]]
- [[Jonsi Stephenson]]
- [[Jason Vallery]]