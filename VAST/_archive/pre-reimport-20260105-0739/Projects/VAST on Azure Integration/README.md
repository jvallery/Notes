---
type: projects
title: VAST on Azure Integration
last_contact: '2026-01-03'
created: '2026-01-03'
tags:
- type/projects
- generated
last_updated: '2025-12-18'
---

# VAST on Azure Integration

## Status

| Field | Value |
|-------|-------|
| **Status** | active |
| **Owner** | Myself |

## Overview

Architecture and GTM outline for integrating VAST with Microsoft Azure, including deployment variants (ODM/Edge, Azure IaaS, future Azure bare metal, hybrid), workload reference patterns, and a roadmap for Blob API compatibility, federation, networking, security, operations, and commercial packaging.

## Open Tasks

```tasks
path includes VAST on Azure Integration
not done
```

## Recent Context

- 2025-12-18: [[2025-12-18 - VAST Azure integration outline]] (via Microsoft)
## Key Facts

## Topics

## Blockers

- ❌ Managed VNet constraints for Azure first-party services (e.g., serverless/managed networking) may limit direct connectivity patterns.
- ❌ Blob API compatibility scope and semantics (auth, error model, throttling, SDK/tool expectations) require validation via conformance gates.
- ❌ Identity integration requirements (Entra ID/OAuth validation, managed identity patterns, RBAC/ACL mapping) are dependencies for MVP.
- ❌ Private Link / Private Link Service operational workflow (DNS, approvals, automation) is a dependency for private-first connectivity.
- ❌ Potential API drift and performance variance across Azure VM/storage options (Lasv4/Lasv5, NVMe locality, quotas/SKU availability).

## Related

<!-- Wikilinks to related entities -->
