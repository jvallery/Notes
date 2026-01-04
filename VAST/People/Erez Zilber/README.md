---
type: people
title: Erez Zilber
last_contact: '2025-10-28'
created: '2026-01-03'
tags:
- type/people
- generated
---

# Erez Zilber

## Recent Context

- 2025-10-28: [[2025-10-28 - Jason and Erez aligned on delivering Azure Blob API support in VAST to enable Az]] - Weekly 1:1 between Jason Vallery and Erez Zilber aligning on delivering Azure Blob API support in VA...

## Profile

**Role**: Protocols Architect at VAST (Protocols)
**Location**: Tel Aviv (planned in-person sessions)
**Relationship**: Weekly 1:1 counterpart; protocol/architecture partner for delivering Azure Blob API support.

**Background**:
- Joined VAST 8+ years ago; leads protocol activities and field-driven protocol requirements; translating field requirements into implementable engineering work; currently ramping on Azure Blob API and mapping OpenAI requirements to VAST.

## Key Facts

- Erez Zilber is VAST Protocols Architect (8+ years) leading field-driven protocol requirements.
- Jason Vallery joined VAST ~1 week before 2025-10-28; previously 13 years at Microsoft object storage with deep Blob API expertise.
- VAST aims to offer Azure Blob API for Azure Marketplace and customers beyond OpenAI.
- OpenAI requires network autarky/offline operation for 72–96 hours for GPU-adjacent storage.
- OpenAI disables account key auth and uses Entra ID managed identities with JWT bearer tokens.
- JWT validation must work offline via cached public keys and must handle key rotation.
- Each GPU cluster has its own service principal to scope data access.
- Key Blob features of interest: Append Blob and PutBlobFromURL (service-to-service copy).
- VAST prefers mapping Blob RBAC/ABAC to existing identity and bucket policies across protocols.
- Planned POC will simulate network isolation to verify uninterrupted operation.

## Topics

Azure Blob API support in VAST, Azure Marketplace enablement, OpenAI storage requirements (GPU-adjacent, offline/network autarky 72–96 hours), Entra ID managed identities, JWT bearer token validation offline (key caching and rotation), Authorization model: mapping Blob RBAC/ABAC to VAST bucket policies, Blob feature requirements (Append Blob, PutBlobFromURL), POC planning with simulated network isolation, Potential MS Graph integration for Entra ID users/groups, In-person design/knowledge-sharing sessions in Tel Aviv (week of Nov 23), Legacy account key support scope decision, Non-Azure GPU facilities considerations (e.g., CoreWeave)

## Related

<!-- Wikilinks to related entities -->
