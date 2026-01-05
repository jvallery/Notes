---
type: customer
title: 'Walmart requirements reset: hybrid namespace, GCS integration, Alluxio risk'
date: '2025-12-23'
account: Walmart
participants:
- Jeff Denworth
- Myself
source: transcript
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Email/2025/2025-12-23_061931_1979_Walmart---Unsettled.md
tags:
- type/customer
- generated
---

# Walmart requirements reset: hybrid namespace, GCS integration, Alluxio risk

**Date**: 2025-12-23
**Account**: [[Walmart]]
**Attendees**: Jeff Denworth, Myself

## Summary

Jeff Denworth relayed that Walmart restated requirements after an internal meeting: they need a long-term hybrid solution and the business rejected operating two disjoint namespaces. Walmart plans an internal big data POC limited to on-prem-only workloads, and any forward path requires integration with Google Cloud Storage (GCS), which may increase competitive risk from Alluxio. Jeff asked PM management to analyze the updated requirements and determine what should enter the VAST product plan, with the goal of a full estate takeover path.

## Action Items

- [?] Analyze Walmart's restated requirements from their internal requirements meeting (hybrid solution, unified namespace, GCS integration) and propose what changes should be incorporated into the VAST product plan. @Myself 📅 2026-01-10 ⏫ #task #proposed #auto

- [?] Coordinate with Mikey (full name unknown) and team to review Walmart requirements and align on a path to a full Walmart data estate takeover strategy for VAST Data. @Myself 📅 2026-01-10 ⏫ #task #proposed #auto

- [?] Assess competitive risk from Alluxio in the Walmart account given the requirement for Google Cloud Storage (GCS) integration, and identify mitigation actions (positioning, integration gaps, or roadmap items). @Myself 📅 2026-01-10 ⏫ #task #proposed #auto

- [?] Analyze Walmart's restated requirements from the 2025-12 internal requirements meeting and identify which requirements should be incorporated into VAST's product plan. @Myself 📅 2026-01-10 ⏫ #task #proposed #auto

- [?] Coordinate with 'Mikey' (full name not provided) and their team to review Walmart requirements and propose a path to a single-namespace hybrid solution with Google Cloud Storage (GCS) integration. @TBD 📅 2026-01-10 ⏫ #task #proposed #auto

- [?] Assess competitive risk from Alluxio given Walmart's GCS integration requirement and single-namespace constraint, and document mitigation options for VAST positioning and product gaps. @Myself 📅 2026-01-17 ⏫ #task #proposed #auto

## Key Information

- Walmart held an internal requirements meeting during the week of 2025-12-22 and restated that they need a long-term hybrid solution for their data team.

- Walmart was not successful in getting the business to accept operating two disjoint namespaces, indicating a requirement for a unified namespace across environments.

- Walmart plans to start an internal big data proof of concept (POC) sometime in 2025, but only for workloads that can run exclusively on premises.

- Walmart requires integration with Google Cloud Storage (GCS) for any solution they move forward with, or they would need significant lobbying at the database layer including potentially a hybrid cloud database.

- Jeff Denworth flagged that Walmart's GCS integration requirement could put Alluxio back in a leading position for the account, creating competitive risk for VAST Data.

---

- Walmart held an internal requirements meeting during the week of 2025-12-22 and restated that they need to build a long-term hybrid solution for their data team.

- Walmart was not successful in getting the business to accept two disjoint namespaces, so any acceptable solution must avoid separate namespaces.

- Walmart plans to start an internal big data proof of concept (POC) sometime in 2025, limited to workloads that can run exclusively on premises.

- Walmart requires integration with Google Cloud Storage (GCS) for any solution they move forward with, or they would need significant lobbying at the database layer including a hybrid cloud database.

- Jeff Denworth warned that Walmart's requirements could put Alluxio back in the driver seat as a competing approach, and VAST should be careful.
