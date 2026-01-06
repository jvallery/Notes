---
type: projects
title: 'RFE 0538: Update VAST OS 5.3+ documentation to state tenant name underscore restriction (NTT DATA Japan Corporation)'
date: '2026-01-05'
project: Cloud
participants:
- Rob Benoit
- Masashige Mito
source: email
source_ref: /Users/jason.vallery/Documents/Notes/Inbox/Email/2026-01-05_091947_6182_RFE-Alert-RFE-0538---Documentation-RFE-Submitted-to-PM---NTT.md
tags:
- type/projects
- project/cloud
- generated
---

# RFE 0538: Update VAST OS 5.3+ documentation to state tenant name underscore restriction (NTT DATA Japan Corporation)

**Date**: 2026-01-05

**Project**: [[Cloud]]

**Attendees**: Rob Benoit, Masashige Mito

## Summary

Rob Benoit forwarded an approved Documentation RFE (Salesforce RFE 0538) tied to NTT DATA Japan Corporation. The request is to update VAST OS 5.3 and later documentation to explicitly state that tenant names cannot include underscores, and to link the RFE to the correct Related Feature in Salesforce.


## Action Items


- [?] Open Salesforce RFE 0538 (https://vastdata.my.salesforce.com/a6HV4000000A6c1) and link it to the correct Related Feature for tracking and prioritization. @Myself ⏫ #task #proposed #auto

- [?] Coordinate with Documentation owners to update VAST OS 5.3 and later docs (Administrator Guide, CLI Command reference, and any tenant creation/configuration docs) to explicitly state allowed tenant name characters and that underscores are not supported. @Myself #task #proposed #auto

- [?] Review the referenced internal Slack thread (https://vastdata.slack.com/archives/C05DWBEGGES/p1765790620090499) for additional context, impacted workflows, and exact doc locations to update for the VAST OS 5.3+ tenant naming restriction. @Myself #task #proposed #auto




## Decisions


- Salesforce RFE 0538 (Documentation) for NTT DATA Japan Corporation was submitted to the PM team and approved by Rob Benoit.




## Key Information


- Rob Benoit approved Salesforce RFE 0538, a Documentation RFE associated with NTT DATA Japan Corporation, and requested the PM team link the RFE to the correct Related Feature in Salesforce.

- Masashige Mito is the Sales Engineer listed on Salesforce RFE 0538 for NTT DATA Japan Corporation.

- Starting with VAST OS 5.3, tenant names no longer support underscores ('_'); VAST OS 5.2.x allowed underscores, but VAST OS 5.3+ returns an error stating only English letters, digits, '-' and '.' are allowed.

- The tenant name character restriction for VAST OS 5.3+ is not explicitly stated in current documentation (Administrator Guide, CLI Command reference), causing customers to discover it during configuration and potentially delaying deployments.




---

*Source: [[2026-01-05_091947_6182_RFE-Alert-RFE-0538---Documentation-RFE-Submitted-to-PM---NTT]]*
