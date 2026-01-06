---
type: projects
title: 'Jonsi Stefansson comments on ''VAST and Azure Integration'' doc: cold data tiering format and DRR messaging'
date: '2026-01-02'
project: Cloud
participants:
- Jonsi Stefansson
source: email
source_ref: /Users/jason.vallery/Documents/Notes/Inbox/Email/2026-01-02_095616_6115_VAST-and-Azure-Integrationdocx.md
tags:
- type/projects
- project/cloud
- generated
---

# Jonsi Stefansson comments on 'VAST and Azure Integration' doc: cold data tiering format and DRR messaging

**Date**: 2026-01-02

**Project**: [[Cloud]]

**Attendees**: Jonsi Stefansson

## Summary

A Google Docs notification email captured two open comments from Jonsi Stefansson on the document 'VAST and Azure Integration.docx'. Jonsi questioned whether describing cold data tiering in VAST object format (not directly readable from Azure Blob) will be acceptable, and asked whether the doc should more firmly state how VAST DRR/efficiencies mitigate flash supply chain risk.


## Action Items


- [?] Review the 'VAST and Azure Integration.docx' section on cold data tiering to Azure Blob and decide whether to recommend VAST native opaque object format, native Azure Blob format, or a dual-mode approach, explicitly addressing Azure Blob direct readability and ecosystem accessibility tradeoffs. @Myself 📅 2026-01-09 ⏫ #task #proposed #auto

- [?] Propose updated wording for the 'VAST and Azure Integration.docx' section on flash supply constraints to more clearly state how VAST DRR/efficiency features reduce flash capacity requirements and mitigate component price volatility risk. @Myself 📅 2026-01-09 #task #proposed #auto






## Key Information


- Jonsi Stefansson raised a concern that tiering cold data to Azure Blob using VAST native opaque object formats would not be readable directly from Azure Blob, and suggested reconsidering to use native Azure Blob format instead.

- Jonsi Stefansson requested a firmer statement in the 'VAST and Azure Integration' document about how VAST DRR and efficiency features reduce exposure to flash supply constraints and rising flash prices.

- The 'VAST and Azure Integration' document includes a positioning statement that cold data can be transparently tiered to Azure Blob using either VAST native opaque formats (for maximum data reduction) or transparent open standard formats (for ecosystem accessibility), to enable infinite scale without flash price premium.

- The 'VAST and Azure Integration' document argues that constrained flash supply and rising prices make an all-flash exabyte-scale strategy economically risky, and that deep integration with Azure Blob allows customers to place the long-tail dataset on HDD-based object storage while keeping VAST flash for the GPU-adjacent working set.




---

*Source: [[2026-01-02_095616_6115_VAST-and-Azure-Integrationdocx]]*
