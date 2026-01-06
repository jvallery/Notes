---
type: projects
title: Jonsi Stefansson comments on 'VAST and Azure Integration.docx' (Azure Blob tiering and DRR messaging)
date: '2026-01-02'
project: Cloud
participants:
- Jonsi Stefansson
source: email
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Email/2026/2026-01-02_095616_9612_VAST-and-Azure-Integrationdocx.md
tags:
- type/projects
- project/cloud
- generated
---

# Jonsi Stefansson comments on 'VAST and Azure Integration.docx' (Azure Blob tiering and DRR messaging)

**Date**: 2026-01-02

**Project**: [[Cloud]]

**Attendees**: Jonsi Stefansson

## Summary

A Google Docs notification email captured two open comments from Jonsi Stefansson on the document 'VAST and Azure Integration.docx'. Jonsi questioned whether describing cold data tiering in VAST object format (not directly readable from Azure Blob) will be acceptable, and suggested strengthening messaging about VAST DRR and efficiency benefits to mitigate flash supply chain risk.


## Action Items


- [?] Respond to Jonsi Stefansson's open comment in 'VAST and Azure Integration.docx' with a recommendation on whether cold data tiering to Azure Blob should use VAST native object format (not directly readable from Azure Blob) versus native Azure Blob format, including tradeoffs (data reduction vs ecosystem accessibility). @Myself ⏫ #task #proposed #auto

- [?] Propose updated wording for 'VAST and Azure Integration.docx' to more explicitly connect VAST DRR/efficiencies to reduced flash capacity requirements and lower exposure to flash supply constraints and rising prices. @Myself #task #proposed #auto






## Key Information


- Jonsi Stefansson raised a concern that tiering cold data to Azure Blob using VAST native opaque object formats would make the data not directly readable from Azure Blob, and asked whether the document should instead specify native Azure Blob format.

- Jonsi Stefansson suggested strengthening the document's statement about how VAST data reduction and efficiency (DRR) can reduce exposure to flash supply constraints and rising flash prices.

- The document text claims cold data can be transparently tiered to Azure Blob using either VAST native opaque formats (for maximum data reduction) or transparent open standard formats (for ecosystem accessibility), positioning this as enabling infinite scale without flash price premium.

- The document text claims integrating with Azure Blob allows customers to keep the long-tail dataset on HDD-based object storage while reserving VAST flash for the GPU-adjacent working set, as a hedge against flash component price volatility.




---

*Source: [[2026-01-02_095616_9612_VAST-and-Azure-Integrationdocx]]*
