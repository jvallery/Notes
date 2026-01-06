---
type: projects
title: Google Docs comments on 'VAST and Azure Integration.docx' (Azure Blob tiering and DRR messaging)
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

# Google Docs comments on 'VAST and Azure Integration.docx' (Azure Blob tiering and DRR messaging)

**Date**: 2026-01-02

**Project**: [[Cloud]]

**Attendees**: Jonsi Stefansson

## Summary

A Google Docs notification email captured two open comments from Jonsi Stefansson on the document 'VAST and Azure Integration.docx'. The comments question whether describing cold data tiering in VAST object format (not directly readable from Azure Blob) will be acceptable, and whether the document should more strongly state how VAST DRR/efficiencies mitigate flash supply chain and pricing risk.


## Action Items


- [?] Review 'VAST and Azure Integration.docx' and decide whether the cold data tiering description should use VAST native opaque object format or native Azure Blob/open formats to ensure Azure Blob direct readability and ecosystem accessibility. @Myself #task #proposed #auto

- [?] Propose updated wording for the flash supply constraint section to explicitly connect VAST DRR/efficiency benefits to reduced flash capacity requirements and lower exposure to flash price volatility. @Myself #task #proposed #auto






## Key Information


- Jonsi Stefansson raised a concern that describing cold data as transparently tiered to Azure Blob using VAST native opaque object formats may be undesirable because data would not be readable directly from Azure Blob, and suggested reconsidering use of native Azure Blob format.

- Jonsi Stefansson suggested strengthening the document's messaging to more firmly state how VAST DRR and efficiency features reduce exposure to flash supply constraints and rising prices.

- The document text claims cold data can be tiered to Azure Blob using either VAST native opaque formats (for maximum data reduction) or transparent open standard formats (for ecosystem accessibility), positioning this as enabling infinite scale without flash price premium.

- The document text argues that constrained flash supply and rising prices make an 'all-flash everything' strategy economically risky for exabyte-scale data, and proposes using Azure Blob (HDD-based object storage) for the long tail while reserving VAST flash for the GPU-adjacent working set.




---

*Source: [[2026-01-02_095616_9612_VAST-and-Azure-Integrationdocx]]*
