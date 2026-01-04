---
type: people
title: Erez Zilber
last_contact: '2025-11-07'
created: '2026-01-03'
tags:
- type/people
- generated
---

# Erez Zilber

## Recent Context

- 2025-10-28: [[Sources/Transcripts/2025/2025-10-28 - Jason and Erez aligned on delivering Azure Blob API support in VAST to enable Az.md|Jason and Erez aligned on delivering Azure Blob API support in VAST to enable Az]] — Jason and Erez aligned on delivering Azure Blob API support in VAST to enable Azure marketplace use ...

- 2025-11-07: [[2025-11-07 - We reviewed the org landscape and aligned on my near-term focus. Jeff outlined k]] - 1:1 with Jeff Denworth to review the org landscape, clarify key stakeholders, and align on the autho... (via Jeff Denworth)
- 2025-11-07: [[2025-11-07 - We aligned on hyperscaler strategy across Google and Microsoft. On Google, GDC i]] - 1:1 strategy sync with Jonsi Stephenson aligning VAST’s hyperscaler approach across Google and Micro... (via Jonsi Stephenson)
- 2025-10-28: [[2025-10-28 - Jason and Erez aligned on delivering Azure Blob API support in VAST to enable Az]] - Jason Vallery and Erez Zilber aligned on implementing Azure Blob API support in VAST, primarily to e...

## Profile

**Role**: Protocols architect at VAST Data (Protocols)
**Location**: Tel Aviv
**Relationship**: Internal stakeholder (pricing)

**Background**:
- Not directly discussed in transcript; included in known entities but not referenced in this note's narrative.
- Referenced as part of current cloud pricing approach discussions.
- Protocols architect at VAST for 8+ years; leads field-driven protocol requirements and translates them into engineering deliverables; currently ramping on Azure Blob API semantics and requirements mapping for OpenAI.

## Key Facts

- Erez Zilber is VAST protocols architect (8+ years) leading field-driven protocol requirements.
- Jason Vallery joined VAST about a week prior; previously spent ~13 years at Microsoft in object storage product leadership.
- OpenAI requires GPU-adjacent storage that can operate through 72–96 hours of network isolation (network autarky).
- OpenAI disables account key authentication and uses Entra ID managed identities with JWT bearer tokens.
- Offline JWT validation requires cached public keys and handling key rotation without IdP connectivity.
- Each OpenAI GPU cluster uses its own service principal to scope access.
- Key Blob features of interest: Append Blob and PutBlobFromURL.
- VAST intends to map Blob RBAC/ABAC semantics to existing VAST identity and bucket policies across protocols.
- In-person working sessions planned in Tel Aviv during the week of Nov 23 (Nov 23–26).
- John runs alliances/partnerships and is the go-to for AMD/NVIDIA and conventional channel partnerships (non-cloud).

## Topics

Azure Blob API support in VAST, Azure Marketplace enablement via Blob API compatibility, Entra ID managed identities and Instance Metadata Service, JWT bearer token validation, offline operation, and key caching/rotation, RBAC/ABAC authorization mapping to VAST bucket policies, OpenAI GPU-adjacent storage and network autarky requirements, Blob feature requirements (Append Blob, PutBlobFromURL), Potential native Entra ID user/group integration via Microsoft Graph, POC planning with simulated network isolation, Org map and key leaders/roles, Cross-cloud platform strategy and homogenization across providers, Cloud GTM plays and integrations (Foundry/Bedrock/Vertex), Cataloging in-flight deals by product requirements, Control-plane partnerships and 'cloud-in-a-box' for Tier-2 clouds, Customer requirements/FRDs documentation in Confluence

## Key Decisions

- ✅ Use Entra ID managed identities with JWT-based auth for OpenAI scenarios (no account keys).
- ✅ Proceed with RBAC/ABAC-to-bucket-policy mapping for Blob authorization in VAST.
- ✅ Carl will move to ProServe under Rob rather than supporting customer-facing PM work.
- ✅ Set a monthly touchpoint with Brandon to align on cloud platform priorities.
- ✅ Customer requirement docs and FRDs will be authored and maintained in Confluence.
- ✅ Prioritize building a first-class cross-cloud platform and GTM versus ad hoc deal chasing.
- ✅ Pursue deeper integration with Google Distributed Cloud and aim to be part of the GDC SKU.
- ✅ Treat Microsoft Azure as a distinct sell-to motion (first-party/Storage HW) separate from marketplace sell-through.
- ✅ Use real-workload benchmarks (not synthetic) as the standard for TPU/storage evaluations with Google.

## Related Customers

- [[Microsoft]]
- [[OpenAI]]

## Related Projects

- [[Pricing]]
- [[Cloud]]

## Related

<!-- Wikilinks to related entities -->
