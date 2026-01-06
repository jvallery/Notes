---
type: projects
title: Comments on 'VAST and Azure Integration.docx' (Azure Blob tiering and flash supply-chain messaging)
date: '2026-01-02'
project: Cloud
participants:
- Jonsi Stefansson
source: email
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Email/2026/2026-01-02_095616_6115_VAST-and-Azure-Integrationdocx.md
tags:
- type/projects
- project/cloud
- generated
---

# Comments on 'VAST and Azure Integration.docx' (Azure Blob tiering and flash supply-chain messaging)

**Date**: 2026-01-02

**Project**: [[Cloud]]

**Attendees**: Jonsi Stefansson

## Summary

Google Docs notification email from Jonsi Stefansson with two open comments on the document 'VAST and Azure Integration.docx'. The comments question whether VAST cold data tiering should use VAST native object format versus native Azure Blob format, and whether the document should more strongly state that VAST data reduction efficiencies mitigate flash supply constraints and price volatility.


## Action Items


- [?] Review 'VAST and Azure Integration.docx' and respond to Jonsi Stefansson's open comment on whether cold data tiering to Azure Blob should use VAST native object format (not directly readable from Azure Blob) versus native Azure Blob format. @Myself 📅 2026-01-06 ⏫ #task #proposed #auto

- [?] Propose updated document language addressing Jonsi Stefansson's request for a firmer statement on how VAST data reduction ratio (DRR) and efficiencies mitigate flash supply-chain constraints and price volatility. @Myself 📅 2026-01-06 #task #proposed #auto






## Key Information


- Jonsi Stefansson left two open comments in the document 'VAST and Azure Integration.docx' on 2026-01-02 at 9:47 AM MST and 9:51 AM MST.

- The document text claims VAST 'Cold Data' can be transparently tiered to Azure Blob using either VAST native opaque formats (for maximum data reduction) or transparent open standard formats (for ecosystem accessibility).

- Jonsi Stefansson raised a concern that using VAST object format for tiering to Azure Blob would make the data not readable directly from Azure Blob, and asked whether the document should instead specify native Azure Blob format.

- The document argues that constrained flash supply and rising prices make an 'all-flash everything' strategy economically risky for exabyte-scale data, and that deep integration with Azure Blob lets customers keep the long-tail dataset on HDD-based object storage while reserving VAST flash for the GPU-adjacent working set.

- Jonsi Stefansson asked whether the document should make a firmer statement that VAST's data reduction ratio (DRR) and efficiencies reduce exposure to flash supply-chain constraints.




---

*Source: [[2026-01-02_095616_6115_VAST-and-Azure-Integrationdocx]]*
