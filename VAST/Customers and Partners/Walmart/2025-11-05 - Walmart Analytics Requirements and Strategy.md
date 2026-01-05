---
type: "customer"
title: "Walmart Analytics Requirements and Strategy"
date: "2025-11-05"
account: ""
participants: ["Unknown"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Inbox/Transcripts/2025-11-05 - Walmart Analytics.md"
tags:
  - "type/customer"
  - "account/"
  - "generated"

---

# Walmart Analytics Requirements and Strategy

**Date**: 2025-11-05
**Account**: [[]]
**Attendees**: Unknown

## Summary

The meeting discussed Walmart's analytics requirements, focusing on data ingestion and processing via BigQuery in GCP, and the need for a hybrid cloud solution with active/active replication across GCP and Walmart facilities. The discussion included technical challenges such as strong consistency, latency tolerance, and the need for a GCS-like API on-prem. A POC for VAST is ready, with a decision goal by the end of CY26.




## Decisions


- POC for VAST is ready to begin with a decision goal by end of CY26.




## Key Information


- Walmart uses BigQuery on GCP for primary data ingestion and processing.

- Walmart requires active/active replication across GCP and two on-prem facilities.

- Walmart's data lake is approximately 500 PiB with 10% daily churn.

- Walmart has a strong preference for a GCS-like API on-prem to avoid refactoring.



---

*Source: [[2025-11-05 - Walmart Analytics]]*