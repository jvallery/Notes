---
type: person
name: Erez Zilber
email: ''
company: VAST Data
title: Protocols architect
last_contact: '2025-10-28'
created: '2026-01-05'
tags:
- type/person
- needs-review
---

# Erez Zilber

## Key Facts

- Erez Zilber is a protocols architect at VAST Data and has been at VAST for 8+ years, leading protocol work and translating field requirements into engineering deliverables.

- Erez Zilber prefers not to introduce a new authorization model for Blob and instead map Azure Blob RBAC/ABAC semantics to VAST identity and bucket policies used across protocols (including NFS and SMB).
## Recent Context

- 2025-10-28: Jason Vallery and Erez Zilber aligned on delivering Azure Blob API support in VAST to enable an Azur...
## Tasks

```tasks
path includes Erez Zilber
not done
```

## Topics

- Azure Blob API support in VAST Data for Azure Marketplace enablement

- OpenAI GPU-adjacent storage requirements and network autarky (72-96 hours offline)

- Entra ID managed identities and JWT bearer token authentication

- Offline JWT validation via cached signing keys and key rotation handling

- Authorization mapping from Azure Blob RBAC/ABAC to VAST bucket policies

## Key Decisions

- For OpenAI scenarios, VAST will use Entra ID managed identities with JWT-based authentication and will not rely on Azure Storage account keys.

- VAST will map Azure Blob authorization semantics (RBAC and ABAC) to VAST identity and bucket policies rather than introducing a separate Blob-specific permission model.

- VAST will prioritize implementing Azure Blob API support with specific attention to Append Blob and PutBlobFromURL.