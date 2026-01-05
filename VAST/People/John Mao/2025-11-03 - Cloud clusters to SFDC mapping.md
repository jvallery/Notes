---
type: people
title: Cloud clusters to SFDC mapping
date: '2025-11-03'
person: John
participants:
- Jason Vallery
- Tomer
- Adar
- John
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-11-03 - Team reviewed how cloud clusters
  must map to Salesforce assets (AccountSitePSN.md
tags:
- type/people
- person/john
- generated
---

# Cloud clusters to SFDC mapping

**Date**: 2025-11-03
**With**: Jason Vallery, Tomer, Adar, John

## Summary

Team aligned on how VAST cloud clusters must map into Salesforce (Account → Site → Cluster asset with PSNT) to enable cluster-level call-home ("Godfather") and Uplink registration via a unique customer subdomain. Phase 1 will be single-tenant per customer via private offers, with Polaris as the deployment/onboarding hook and a near-term stop-gap manual onboarding flow needed for upcoming field POCs. Key concerns include telemetry/support-bundle egress costs and legal/data-custodian constraints on payload visibility for managed services.
## Action Items
- [ ] Draft Phase 1 cloud onboarding process (SFDC Account/Site/PSNT, Uplink subdomain, Polaris/Terraform hooks) and circulate for review @John 📅 2025-11-08 🔺 #task #proposed
- [ ] Define and publish a stop-gap manual flow for immediate field POCs to configure Salesforce assets and Uplink registration @Myself 📅 2025-11-08 🔺 #task #proposed
- [ ] Prepare a reusable template/checklist to create Uplink subdomains and link them to Salesforce accounts/opportunities @Adar 📅 2025-11-08 ⏫ #task #proposed
- [ ] Specify Terraform/Polaris changes to auto-register clusters with Uplink (subdomain injected at deploy time) @John 📅 2025-11-08 ⏫ #task #proposed
- [ ] Document PSNT-to-SFDC matching and Godfather handling, including required fields and error handling @Tomer Hagay 📅 2025-11-08 ⏫ #task #proposed
- [ ] Propose an approach to minimize telemetry egress (e.g., on-demand bundles, proxy via Polaris, S3 staging) with cost estimates @Tomer Hagay 📅 2025-11-08 ⏫ #task #proposed
- [ ] Decide workflow for public marketplace provisioning, including whether Tackle auto-creates Salesforce accounts/opportunities @John 📅 2025-11-08 🔺 #task #proposed
- [ ] Run legal review of call-home/Uplink payload content and operator visibility for managed service data-custodian obligations @TBD 📅 2025-11-08 🔺 #task #proposed
- [ ] Confirm and document policy on tenant-level opt-out in multi-tenant SaaS @Myself 📅 2025-11-08 ⏫ #task #proposed
- [ ] Evaluate feasibility and security posture of any future 'hello/adopt' endpoint for unregistered clusters @Tomer Hagay 📅 2025-11-08 ⏫ #task #proposed
- [ ] Audit existing VoC cloud customers for proper Salesforce and Uplink linkage; remediate gaps @Adar 📅 2025-11-08 🔺 #task #proposed
- [ ] Select the preferred telemetry transport path (direct to GCS vs proxy via Polaris vs S3 staging) and define activation criteria for support bundles @Tomer Hagay 📅 2025-11-08 ⏫ #task #proposed

## Decisions
- Phase 1 scope is single-tenant per customer deployments; no tenant-level call-home.
- No auto 'hello/adopt' endpoint for clusters at this time due to security concerns.
- Polaris will be the deployment mechanism and the hook point for future automation of registration.
- Cloud clusters must have Salesforce asset records with PSNT and an Uplink subdomain to enable support.

## Key Information
- Each VAST cluster has a single PSNT (serial-like identifier) used to match against Salesforce records.
- Call-home ("Godfather") operates at the cluster level; tenants are not aware of call-home.
- Uplink requires explicit registration with a unique customer subdomain and a matching Salesforce account; unregistered clusters send no Uplink data.
- On-prem onboarding is heavy; cloud needs a lighter, more automated onboarding path.
- Polaris is intended to deploy VAST on Cloud and can trigger onboarding/registration steps; Tackle is planned to integrate Salesforce private offers with deployment metadata/entitlements.
- Telemetry and support bundles create egress costs from the customer VPC; regular telemetry is small but non-zero; support bundles could be collected on-demand.
- Support bundles are currently stored on GCS; customers can access their Uplink portal via subdomain; Salesforce stores some Uplink data (e.g., cases).

---

*Source: [[Inbox/_archive/2025-11-03/2025-11-03 - Team reviewed how cloud clusters must map to Salesforce assets (AccountSitePSN.md|2025-11-03 - Team reviewed how cloud clusters must map to Salesforce assets (AccountSitePSN]]*

## Related

- [[Jason Vallery]]
- [[Cloud control plane]]
- [[Amazon]]
- [[Google]]
- [[Microsoft]]
- [[CoreWeave]]