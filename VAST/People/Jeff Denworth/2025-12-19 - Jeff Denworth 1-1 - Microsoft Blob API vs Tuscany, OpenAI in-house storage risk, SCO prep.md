---
type: people
title: Jeff Denworth 1:1 - Microsoft Blob API vs Tuscany, OpenAI in-house storage risk, SCO prep
date: '2025-12-19'
person: Jeff Denworth
participants:
- Jason Vallery
- Jeff Denworth
- Pete Eming
- Vamshi (last name unknown)
- John Mao
- Venkat (last name unknown)
- Manish Sah
source: transcript
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-12-19 - Jeff Denworth - Microsoft strategy and SCO prep.md
tags:
- type/people
- generated
---

# Jeff Denworth 1:1 - Microsoft Blob API vs Tuscany, OpenAI in-house storage risk, SCO prep

**Date**: 2025-12-19
**With**: Jason Vallery, Jeff Denworth, Pete Eming, Vamshi (last name unknown), John Mao, Venkat (last name unknown), Manish Sah

## Summary

Jason Vallery and Jeff Denworth discussed VAST Data's Microsoft strategy, focusing on whether to prioritize Azure Blob API compatibility versus Microsoft's internal project Tuscany, and how to scope an MVP versus a broader market play. They also assessed OpenAI's apparent move away from Azure Blob API toward an internal storage stack (Rockset, FoundationDB, RocksDB) and the strategic risk that Microsoft can reuse OpenAI-written IP across Azure services. Jeff asked Jason to focus less on a narrow OpenAI and Microsoft AI view and more on a broader, "in for a pound" approach, and they planned to cover SCO presentation preparation.

## Action Items

- [?] Align VAST Data's Microsoft strategy narrative around the trade-offs between Azure Blob API compatibility, Microsoft's internal Tuscany initiative, and the required feature surface area for an MVP versus a broader market solution. @Myself ⏫ #task #proposed #auto

- [?] Prepare the SCO presentation requested by Jeff Denworth, including key messages and positioning for VAST Data's Microsoft strategy and product direction. @Myself ⏫ #task #proposed #auto

- [?] Validate with appropriate Microsoft and OpenAI contacts whether OpenAI is materially reducing reliance on Azure Blob API and what that implies for VAST Data's Blob API investment priorities. @Myself #task #proposed #auto

- [?] Investigate and document what Microsoft project Tuscany is (scope, API expectations, and adoption path) to inform VAST Data's decision on Blob API versus Tuscany alignment. @Myself ⏫ #task #proposed #auto

## Key Information

- Jeff Denworth directed that VAST Data should not scope Azure Blob API work only around OpenAI and Microsoft AI, and instead should pursue a broader market approach ("in for a pound").

- Pete Eming (reports to Vamshi, last name unknown) previously worked with Jason Vallery at Amazon and took over ownership of the relationship between Azure Storage and OpenAI and Microsoft AI after Jason left.

- Pete Eming told Jason Vallery that OpenAI is replatforming away from Azure Blob API usage for some scenarios, including replacing a Blob-based data movement/replication engine with an approach using rclone and other tooling.

- Jason Vallery believes VAST Data's primary competition at OpenAI is OpenAI building an internal storage stack (influenced by Rockset acquisition) rather than external storage vendors.

- Jason Vallery stated that OpenAI's internal storage/capacity management stack uses L-series Azure VMs with local NVMe and includes RocksDB for capacity management, with FoundationDB providing a database layer and key-value API above it.

- Jason Vallery stated that OpenAI has an open source training SDK that abstracts multiple cloud object APIs including S3, Google Cloud Storage API, and Azure Blob Storage API.

- Jason Vallery stated that OpenAI is receiving additional infrastructure including bare metal L-series, bare metal UltraDisk, and Azure Blob Storage HDD clusters, and he suspects some will run OpenAI's internal Rockset-derived storage solution.

- Jason Vallery stated that Microsoft's deal with OpenAI grants Microsoft exclusive ownership and unlimited use of code written by OpenAI until OpenAI's board declares AGI, creating a strategic risk that Microsoft could reuse OpenAI storage IP in Azure services.

- Jeff Denworth expressed skepticism that a Rockset-derived team can successfully build a geoscale, hyperscale object store, noting VAST Data took a decade to build its own and still has reliability issues.

- Jason Vallery asserted that Microsoft AI (MAI) is less sophisticated operationally than OpenAI but currently leverages the Azure Blob API.

- The discussion framed a product decision trade-off between implementing Azure Blob API compatibility versus aligning to Microsoft's internal project Tuscany, and determining the breadth of surface area for an MVP versus a complete solution.

---

*Source: [[2025-12-19 - Jeff Denworth - Microsoft strategy and SCO prep]]*