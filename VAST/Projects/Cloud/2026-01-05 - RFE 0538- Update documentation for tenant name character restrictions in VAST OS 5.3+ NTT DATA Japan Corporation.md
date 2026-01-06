---
type: projects
title: 'RFE 0538: Update documentation for tenant name character restrictions in VAST OS 5.3+ (NTT DATA Japan Corporation)'
date: '2026-01-05'
project: Cloud
participants:
- Rob Benoit
- Masashige Mito
source: email
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Email/2026/2026-01-05_091947_6182_RFE-Alert-RFE-0538---Documentation-RFE-Submitted-to-PM---NTT.md
tags:
- type/projects
- project/cloud
- generated
---

# RFE 0538: Update documentation for tenant name character restrictions in VAST OS 5.3+ (NTT DATA Japan Corporation)

**Date**: 2026-01-05

**Project**: [[Cloud]]

**Attendees**: Rob Benoit, Masashige Mito

## Summary

Rob Benoit forwarded an approved Documentation RFE (RFE 0538) tied to NTT DATA Japan Corporation. The request is to update VAST OS 5.3+ documentation to explicitly state that underscores are not supported in tenant names and to link the Salesforce RFE to the correct Related Feature.


## Action Items


- [?] Open Salesforce RFE 0538 (https://vastdata.my.salesforce.com/a6HV4000000A6c1) and link the RFE to the correct Related Feature so it is properly tracked by Product Management. @Myself ⏫ #task #proposed #auto

- [?] Coordinate with Documentation owners to update VAST OS 5.3+ docs (Administrator Guide and CLI Command Reference) to explicitly state tenant name character restrictions, including that underscores '_' are not supported and only English letters, digits, '-' and '.' are allowed. @Myself #task #proposed #auto

- [?] Review the internal Slack thread for additional context on the tenant name underscore restriction (https://vastdata.slack.com/archives/C05DWBEGGES/p1765790620090499) and capture any specific doc locations or product behavior details needed for the documentation update. @Myself #task #proposed #auto




## Decisions


- RFE 0538 (Documentation) was approved by Rob Benoit for submission to the Product Management team.




## Key Information


- RFE 0538 is a Documentation RFE for NTT DATA Japan Corporation requesting that VAST OS 5.3 and later documentation explicitly state tenant name character restrictions, specifically that underscores '_' are not supported and only English letters, digits, '-' and '.' are allowed.

- In VAST OS 5.2.x, underscores '_' in tenant names worked, but starting in VAST OS 5.3 the system rejects underscores and returns the error: "Only following symbols are allowed: all English letters, digits, special characters '-' and '.'".

- Rob Benoit approved RFE 0538 and requested the PM team to open the Salesforce RFE record and link it to the correct Related Feature.

- Masashige Mito is the Sales Engineer associated with RFE 0538 for NTT DATA Japan Corporation.




---

*Source: [[2026-01-05_091947_6182_RFE-Alert-RFE-0538---Documentation-RFE-Submitted-to-PM---NTT]]*
