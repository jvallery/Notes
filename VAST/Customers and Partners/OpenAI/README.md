---
type: customer
title: OpenAI
last_contact: '2025-12-19'
created: '2026-01-03'
tags:
- type/customer
- generated
---

# OpenAI

## Recent Context

- 2025-12-19: [[2025-12-19]] - Jason Vallery and Jeff Denworth discuss strategy around supporting the Azure Blob API versus Microso... (via Jeff Denworth)

## Key Facts

- Pete Eming reports to Vamshi and currently owns the Azure Storage relationship with OpenAI and Microsoft AI (previously owned by Jason).
- OpenAI is reportedly replatforming away from Azure Blob API for some scenarios and building their own solution using rclone and other tools.
- Discussion claim: Microsoft’s deal with OpenAI gives Microsoft exclusive ownership/rights to every line of code written at OpenAI until AGI is declared by OpenAI’s board; Microsoft can reuse that IP for Azure services.
- Per discussion, OpenAI’s likely competition is internal (in-house storage/capacity management) rather than external vendors like Weka.
- OpenAI infrastructure mentioned: L-series VMs, potential bare metal L-series, bare metal UltraDisk, and Blob Storage HDD clusters.

## Topics

Blob API vs Tuscany trade-offs, MVP vs broader market surface area ('crawl, walk, run'), OpenAI moving away from Blob API, OpenAI internal storage stack and Rockset/RocksDB, Microsoft rights to OpenAI IP and AGI clause risk, Competitive landscape (internal vs external vendors)

## Open Tasks

- [ ] Discuss with OpenAI the idea of providing a sync engine/data movement capability (in response to OpenAI moving away from Blob’s replication engine).

## Account Status

| Field | Value |
|-------|-------|
| **Status** | Prospect |
| **Industry** | AI / Technology |

## Key Contacts

_No key contacts identified._

## Opportunities

- Potential conversations about providing a sync engine / storage capabilities
- Blob API compatibility and/or alternative integration paths

## Blockers

- ❌ OpenAI reportedly replatforming away from Blob API in some scenarios
- ❌ OpenAI may build in-house storage stack reducing need for external solutions

## Key Decisions

- ✅ Initial framing decision: avoid focusing only on OpenAI and Microsoft AI as the only customers; aim for a broader 'in for a pound' approach (directional preference stated by Jeff).

## Related

<!-- Wikilinks to related entities -->
