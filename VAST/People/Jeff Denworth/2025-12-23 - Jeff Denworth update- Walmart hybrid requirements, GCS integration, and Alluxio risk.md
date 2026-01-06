---
type: people
title: 'Jeff Denworth update: Walmart hybrid requirements, GCS integration, and Alluxio risk'
date: '2025-12-23'
person: Jeff Denworth
participants:
- Jeff Denworth
- Myself
source: email
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Email/2026/2025-12-23_061931_8689_Walmart---Unsettled.md
tags:
- type/people
- person/jeff-denworth
- generated
---

# Jeff Denworth update: Walmart hybrid requirements, GCS integration, and Alluxio risk

**Date**: 2025-12-23
**With**: Jeff Denworth, Myself

## Summary

Jeff Denworth shared an update from Walmart's internal requirements meeting: Walmart still needs a long-term hybrid solution and the business rejected operating two disjoint namespaces. Walmart plans an on-prem-only big data POC in 2025 and any forward solution must integrate with Google Cloud Storage (GCS), creating competitive risk from Alluxio and requiring VAST PM leadership to re-evaluate requirements for the product plan.


## Action Items


- [?] Analyze Walmart's re-stated requirements from their internal requirements meeting and propose what changes are needed in the VAST product plan to support Walmart's long-term hybrid solution and Google Cloud Storage (GCS) integration requirements. @Myself ⏫ #task #proposed #auto

- [?] Coordinate with Mikey and the broader team to validate Walmart's constraints (no disjoint namespaces, on-prem-only POC in 2025, GCS integration requirement) and define a clear path for VAST to win the full Walmart data estate over time. @Myself ⏫ #task #proposed #auto

- [?] Assess competitive positioning versus Alluxio for Walmart's hybrid + GCS integration requirements and identify mitigation actions (product gaps, integrations, messaging, or partner strategy). @Myself #task #proposed #auto




## Decisions


- VAST Product Management leadership will analyze Walmart's re-stated requirements and determine what should be incorporated into the VAST product plan for Walmart's hybrid and GCS integration needs.




## Key Information


- Walmart held an internal requirements meeting during the week of 2025-12-22 and reiterated they need a long-term hybrid solution for their data team.

- Walmart was not successful in getting the business to accept operating two disjoint namespaces, so any acceptable solution must avoid that model.

- Walmart plans to start an internal big data proof of concept (POC) sometime in 2025, limited to workloads that can run exclusively on premises.

- Walmart requires integration with Google Cloud Storage (GCS) for any solution they move forward with, or they would need significant lobbying at the database layer including potentially adopting a hybrid cloud database.

- Jeff Denworth flagged that Walmart's GCS integration requirement could put Alluxio back in a leading position for Walmart, creating competitive risk for VAST.




---

*Source: [[2025-12-23_061931_8689_Walmart---Unsettled]]*
