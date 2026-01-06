---
type: projects
title: Comments on 'VAST and Azure Integration.docx' (Azure Blob tiering format and DRR messaging)
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

# Comments on 'VAST and Azure Integration.docx' (Azure Blob tiering format and DRR messaging)

**Date**: 2026-01-02

**Project**: [[Cloud]]

**Attendees**: Jonsi Stefansson

## Summary

Google Docs notification email shows two open comments from Jonsi Stefansson on the document 'VAST and Azure Integration.docx'. The comments question whether VAST cold data tiering should use VAST object format versus native Azure Blob format, and whether the document should more strongly state how VAST DRR and efficiency reduce flash supply chain risk.


## Action Items


- [?] Respond to Jonsi Stefansson's open comment in 'VAST and Azure Integration.docx' with a recommendation on whether cold data tiering to Azure Blob should use VAST object format (opaque) or native Azure Blob format, including tradeoffs for data reduction vs direct Azure readability and ecosystem access. @Myself 📅 2026-01-06 ⏫ #task #proposed #auto

- [?] Propose updated wording for 'VAST and Azure Integration.docx' that more firmly quantifies or explains how VAST DRR and efficiency reduce flash capacity requirements and mitigate flash supply constraint risk, and add it as a comment or edit for review by Jonsi Stefansson. @Myself 📅 2026-01-06 #task #proposed #auto






## Key Information


- Jonsi Stefansson raised a concern that tiering cold data to Azure Blob using VAST object format would not be readable directly from Azure Blob, and asked whether the design should instead use native Azure Blob format.

- Jonsi Stefansson suggested strengthening the document's messaging to more firmly state that VAST DRR and efficiency reduce exposure to flash supply constraints and rising prices.

- The document text claims VAST cold data can be transparently tiered to Azure Blob using either VAST native opaque formats (for maximum data reduction) or transparent open standard formats (for ecosystem accessibility), positioning this as enabling infinite scale without flash price premium.

- The document text argues that constrained flash supply and rising prices make an 'all-flash everything' strategy economically risky for exabyte-scale data, and that deep integration with Azure Blob lets customers keep the long tail on HDD-based object storage while reserving VAST flash for the GPU-adjacent working set.




---

*Source: [[2026-01-02_095616_9612_VAST-and-Azure-Integrationdocx]]*
