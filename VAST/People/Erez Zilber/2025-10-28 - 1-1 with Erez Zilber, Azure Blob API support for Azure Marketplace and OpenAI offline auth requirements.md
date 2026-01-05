---
type: people
title: 1:1 with Erez Zilber, Azure Blob API support for Azure Marketplace and OpenAI offline auth requirements
date: '2025-10-28'
person: Erez Zilber
participants:
- Jason Vallery
- Erez Zilber
- Alon Horev
source: transcript
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-28 - Jason and Erez aligned on delivering Azure Blob API support in VAST to enable Az.md
tags:
- type/people
- generated
---

# 1:1 with Erez Zilber, Azure Blob API support for Azure Marketplace and OpenAI offline auth requirements

**Date**: 2025-10-28
**With**: Jason Vallery, Erez Zilber, Alon Horev

## Summary

Jason Vallery and Erez Zilber aligned on delivering Azure Blob API support in VAST to enable an Azure Marketplace offer and OpenAI GPU-adjacent storage scenarios. Key requirements include Entra ID managed identities with offline JWT validation via cached signing keys (including rotation) to survive 72-96 hours of network isolation, plus mapping Azure Blob RBAC/ABAC authorization semantics to VAST identity and bucket policies. Priority Blob features called out were Append Blob and PutBlobFromURL.

## Action Items

- [?] Send reading material to Jason Vallery on Azure Instance Metadata Service, Managed Identities, and relevant Entra ID and Microsoft Graph documentation to accelerate Blob auth design. @Erez Zilber 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Draft a functional requirements document (FRD) for Azure Blob API support in VAST Data, covering the auth model, RBAC/ABAC mapping, Append Blob, PutBlobFromURL, and offline token validation requirements. @Erez Zilber 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Design JWT verification plus Entra ID signing key caching and rotation handling so VAST Data can validate tokens for 72-96 hours without identity provider connectivity. @TBD 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Define the authorization mapping from Azure Blob RBAC/ABAC roles and scopes to VAST Data identity and bucket policies across protocols (including NFS and SMB consistency). @TBD 📅 2025-11-08 #task #proposed #auto

- [?] Coordinate a proof of concept plan with OpenAI to validate Azure Blob API behavior in VAST Data, including a simulated network isolation test to confirm uninterrupted operation during 72-96 hours of outage. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Schedule and send calendar invites for in-person working sessions in Tel Aviv during 2025-11-23 to 2025-11-26 for Blob API design and knowledge sharing. @Erez Zilber 📅 2025-11-08 #task #proposed #auto

- [?] Prepare an agenda and session plan for the Tel Aviv in-person working sessions focused on Azure Blob API requirements, auth, authorization mapping, and offline validation strategy. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Confirm exact dates and times for the Tel Aviv meetings during the week of 2025-11-23 and communicate them to attendees. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Set a follow-up design review meeting after Erez Zilber returns in mid-November 2025 to review the Blob API FRD and offline auth design. @Erez Zilber 📅 2025-11-08 #task #proposed #auto

- [?] Validate the exact Azure Blob feature set required by OpenAI beyond Append Blob and PutBlobFromURL to avoid under-scoping the POC and Marketplace MVP. @Myself 📅 2025-10-28 ⏫ #task #proposed #auto

- [?] Decide whether to support legacy Azure Storage account key authentication for the Azure Blob API implementation, and document any constraints if supported. @TBD 📅 2025-11-08 #task #proposed #auto

- [?] Send reading material on Azure Instance Metadata Service, Managed Identities, and relevant Entra ID and Microsoft Graph documentation to Jason Vallery. @Erez Zilber 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Draft an FRD for VAST Azure Blob API support covering authentication model, RBAC/ABAC mapping, Append Blob, PutBlobFromURL, and offline token validation requirements. @Erez Zilber 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Design JWT verification plus signing key caching and rotation strategy so VAST can validate Entra ID tokens for 72-96 hours without identity provider connectivity. @TBD 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Define authorization mapping from Azure Blob RBAC/ABAC roles and scopes to VAST identity and bucket policies across protocols. @TBD 📅 2025-11-08 #task #proposed #auto

- [?] Coordinate a POC plan with OpenAI that includes a simulated network isolation test to validate uninterrupted operation during 72-96 hours of offline conditions. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Schedule and send calendar invites for in-person working sessions in Tel Aviv during 2025-11-23 to 2025-11-26. @Erez Zilber 📅 2025-11-08 #task #proposed #auto

- [?] Prepare an agenda and session plan for the Tel Aviv in-person design and knowledge-sharing sessions. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Confirm exact dates and times for Tel Aviv meetings during the week of 2025-11-23. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Set a follow-up design review meeting after Erez Zilber returns in mid-November 2025. @Erez Zilber 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Validate the exact Azure Blob feature set required by OpenAI beyond Append Blob and PutBlobFromURL. @Myself 📅 2025-10-28 ⏫ #task #proposed #auto

- [?] Decide whether VAST will support legacy Azure Storage account key authentication for Blob API scenarios and document constraints if supported. @TBD 📅 2025-11-08 #task #proposed #auto

## Decisions

- Implement Azure Blob API support in VAST Data with initial emphasis on Append Blob and PutBlobFromURL to satisfy OpenAI and Azure Marketplace needs.

- Use Entra ID managed identities with JWT bearer tokens for OpenAI scenarios, and do not rely on Azure Storage account key authentication for that use case.

- Map Azure Blob RBAC and ABAC authorization semantics to VAST Data identity and bucket policies (reusing the existing cross-protocol policy model).

- Design offline JWT verification using cached Entra ID signing keys with rotation handling to meet OpenAI 72-96 hour network autarky requirements.

- For OpenAI scenarios, VAST will use Entra ID managed identities with JWT-based authentication and will not rely on Azure Storage account keys.

- VAST will map Azure Blob authorization semantics (RBAC and ABAC) to VAST identity and bucket policies rather than introducing a separate Blob-specific permission model.

- VAST will prioritize implementing Azure Blob API support with specific attention to Append Blob and PutBlobFromURL.

## Key Information

- Erez Zilber is a protocols architect at VAST Data, joined over 8 years ago, and leads protocol work by translating field requirements into engineering deliverables.

- Jason Vallery joined VAST Data on Monday 2025-10-20 ("last Monday" relative to 2025-10-28) after 13 years at Microsoft in the object storage team, covering Blob API, S3 API, multi-protocol access, SDKs/tools, tiering, pricing, and top-customer engagements including OpenAI.

- VAST Data intends to support the Azure Blob API not only for OpenAI but also to enable an Azure Marketplace offer and compatibility with Microsoft first-party services that integrate with Azure Blob Storage semantics.

- OpenAI uses Azure Blob API heavily due to being born on Azure and has a requirement for GPU-adjacent storage that can operate with network isolation (autarky) for 72-96 hours.

- For OpenAI scenarios, account key authentication is disabled and access is expected to use Entra ID managed identities with JWT bearer tokens.

- JWT validation for Entra ID must work offline by caching public signing keys and handling key rotation so that authentication continues during 72-96 hours without IdP connectivity.

- Azure Blob authorization uses RBAC and ABAC models that should be mapped to VAST identity and bucket policies rather than introducing a new permission model.

- Two Azure Blob features highlighted as important for OpenAI are Append Blob and PutBlobFromURL (service-to-service copy).

- Alon Horev informed Erez Zilber that Jason Vallery has relevant context on how OpenAI wants to use VAST Data as a Blob storage server.

---

- Erez Zilber is a protocols architect at VAST Data and has been at VAST for 8+ years, leading protocol work and translating field requirements into engineering deliverables.

- Jason Vallery joined VAST Data on Monday 2025-10-20 ("last Monday" relative to 2025-10-28) after 13 years at Microsoft working on object storage, including Azure Blob APIs, SDKs, client tools, multi-protocol access, tiering, pricing, and customer engagement.

- VAST Data intends to support the Azure Blob API not only for OpenAI but also to enable an Azure Marketplace offer and broader Azure ecosystem integrations with Microsoft first-party services.

- OpenAI's GPU-adjacent storage scenario requires continued operation during network isolation (autarky) for approximately 72-96 hours.

- OpenAI disables Azure Storage account key authentication and instead uses Entra ID managed identities with JWT bearer tokens for Azure Blob access.

- JWT validation for Entra ID must work offline by caching public signing keys and handling key rotation so VAST can validate tokens without IdP connectivity for 72-96 hours.

- OpenAI scopes data access by using a separate service principal per GPU cluster.

- Two Azure Blob API features highlighted as important for OpenAI are Append Blob and PutBlobFromURL (service-to-service copy).

- Erez Zilber prefers not to introduce a new authorization model for Blob and instead map Azure Blob RBAC/ABAC semantics to VAST identity and bucket policies used across protocols (including NFS and SMB).
