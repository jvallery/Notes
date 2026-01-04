---
type: customer
title: Align on Azure Blob API
date: '2025-10-28'
account: OpenAI
participants:
- Jason Vallery
- Erez Zilber
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-10-28 - Jason and Erez aligned on delivering
  Azure Blob API support in VAST to enable Az.md
tags:
- type/customer
- account/openai
- generated
---

# Align on Azure Blob API

**Date**: 2025-10-28
**Account**: [[OpenAI]]
**Attendees**: Jason Vallery, Erez Zilber

## Summary

Jason and Erez aligned on delivering Azure Blob API support in VAST to enable Azure marketplace use and OpenAI GPU-adjacent storage scenarios. Key requirements include Entra ID managed identities, JWT validation with cached keys to survive 72–96 hours of network isolation, and mapping Blob RBAC/ABAC semantics to VAST bucket policies; Append Blob and PutBlobFromURL were highlighted as important Blob features. They planned an OpenAI POC to validate offline operation and agreed to schedule in-person working sessions in Tel Aviv the week of 2025-11-23.
## Action Items
- [ ] Send reading material on Azure Instance Metadata Service, Managed Identities, and relevant Entra ID/MS Graph documentation. @Myself 📅 2025-11-08 🔺 #task
- [ ] Draft FRD for Azure Blob API support covering auth model, RBAC/ABAC mapping, Append Blob, PutBlobFromURL, and offline token validation. @Erez Zilber 📅 2025-11-08 ⏫ #task
- [ ] Design JWT verification plus public-key caching/rotation strategy to operate 72–96 hours without IdP connectivity. @VAST Protocols team 📅 2025-11-08 🔺 #task
- [ ] Define authorization mapping from Blob RBAC/ABAC to VAST identity and bucket policies across protocols. @VAST Protocols team 📅 2025-11-08 ⏫ #task
- [ ] Coordinate POC plan with OpenAI, including a simulated network isolation test to validate uninterrupted operation. @Myself 📅 2025-11-08 🔺 #task
- [ ] Schedule and send calendar invites for Tel Aviv face-to-face sessions (Nov 23–26). @Erez Zilber 📅 2025-11-08 ⏫ #task
- [ ] Prepare agenda and session plan for Tel Aviv visit and knowledge sharing sessions. @Myself 📅 2025-11-08 ⏫ #task
- [ ] Confirm exact dates/times for Tel Aviv meetings during the week of 2025-11-23. @Myself 📅 2025-11-08 ⏫ #task
- [ ] Set a follow-up design review after Erez returns mid-November. @Erez Zilber 📅 2025-11-08 ⏫ #task
- [ ] Decide scope and constraints for any legacy account key authentication support. @VAST Engineering 📅 2025-11-08 ⏫ #task

## Decisions
- Use Entra ID managed identities with JWT-based authentication for OpenAI scenarios (no account keys).
- Proceed with mapping Blob RBAC/ABAC authorization semantics to VAST identity and bucket policies.

## Key Information
- Erez Zilber is VAST protocols architect (8+ years) focused on field-driven protocol requirements.
- OpenAI requires GPU-adjacent storage that can continue operating during network isolation for ~72–96 hours.
- OpenAI disables account key authentication and relies on Entra ID managed identities and JWT bearer tokens.
- Offline operation depends on JWT validation using cached public keys and handling key rotation without IdP connectivity.
- Each OpenAI GPU cluster uses its own service principal to scope data access.
- Append Blob and PutBlobFromURL are key Blob API features of interest (PutBlobFromURL enables service-to-service copy).
- VAST wants Azure Blob API support for Azure marketplace enablement beyond OpenAI.

---

*Source: [[Inbox/_archive/2025-10-28/2025-10-28 - Jason and Erez aligned on delivering Azure Blob API support in VAST to enable Az.md|2025-10-28 - Jason and Erez aligned on delivering Azure Blob API support in VAST to enable Az]]*

## Related

- [[Microsoft]]
- [[CoreWeave]]
- [[Oracle]]
- [[Amazon]]
- [[Erez Zilber]]
- [[Jason Vallery]]
- [[OpenAI VAST POC (CoreWeave cluster)]]
