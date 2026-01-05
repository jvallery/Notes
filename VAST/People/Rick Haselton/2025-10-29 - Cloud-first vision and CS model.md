---
type: people
title: Cloud-first vision and CS model
date: '2025-10-29'
person: Rick Haselton
participants:
- Jason Vallery
- Rick Haselton
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-10-29 - Jason introduced his cloud-first
  vision for VAST (VAST-as-a-Service, multi-cloud.md
tags:
- type/people
- person/rick-haselton
- generated
---

# Cloud-first vision and CS model

**Date**: 2025-10-29
**With**: Jason Vallery, Rick Haselton

## Summary

Jason Vallery shared a cloud-first VAST-as-a-Service vision and interviewed Rick Haselton on how Customer Success operates for CoreWeave and XAI, which are managed-services/SRE-style engagements with heavy Slack-based collaboration and strict response expectations. They discussed XAI’s request for a single filesystem across multiple clusters (not supported today), current replication/global-namespace options, common operational issues (networking, C-node/D-node failures), and the RMA/depot process. A key follow-up is to confirm formal SLA/SLO targets and any legal penalties with the CoreWeave CSM, Gordon Brown.
## Action Items
- [ ?] Connect with Gordon Brown to review CoreWeave/XAI SLAs, response targets, and penalty clauses. @Myself 📅 2025-11-08 🔺 #task #proposed
- [ ?] Draft an initial operating model for VAST-as-a-Service (SRE vs CS roles, on-call, communications, SLAs). @Myself 📅 2025-11-08 ⏫ #task #proposed
- [ ?] Deep-dive with Rick on XAI workload patterns (checkpointing, GPU-adjacent caching, data flows) to inform cloud design. @Myself 📅 2025-11-08 ⏫ #task #proposed
- [ ?] Assess feasibility/roadmap options for XAI’s multi-cluster single-namespace/filesystem request. @Myself 📅 2025-11-08 ⏫ #task #proposed
- [ ?] Obtain and review the legal SLA document and any penalty clauses for CoreWeave/XAI. @Myself 📅 2025-11-08 🔺 #task #proposed
- [ ?] Validate the current after-hours and weekend coverage model across APJ/EMEA for critical incidents. @Myself 📅 2025-11-08 ⏫ #task #proposed
- [ ?] Confirm details of XAI’s cloud data location/provider and how data is repatriated to VAST clusters. @Myself 📅 2025-11-08 🔽 #task #proposed
- [ ?] Review Slack alarm channel configurations and escalation paths to support proactive outreach. @Myself 📅 2025-11-08 🔽 #task #proposed

## Key Information
- Rick Haselton is the tech lead for two of VAST’s largest customers: CoreWeave (#1) and XAI (#3).
- CoreWeave and XAI primarily operate on-prem clusters; XAI may keep some data in the cloud but repatriates it to on-prem VAST clusters for work.
- XAI requested a single large cluster/filesystem spanning multiple clusters; VAST does not support a single filesystem across clusters today.
- VAST supports synchronous replication for S3 buckets and a site-to-site global namespace (not a single filesystem across disparate clusters).
- XAI object clusters are ~313–314 PB used per cluster and are rapidly filling with raw training data (e.g., YouTube/Instagram).
- CS engagement for these accounts is managed-services/SRE-like: primary comms via Slack, urgent issues via live calls, and tickets tracked in Salesforce (CS) and Orion/Jira (vForce).
- Common operational issues include networking problems and C-node/D-node failures; deeper Kubernetes/CSI questions are routed to vForce/R&D.
- RMAs are handled via VAST depots (Campbell or Sacramento); field work typically swaps whole nodes rather than replacing internal components (fans are an exception).
- Formal SLAs/SLOs exist with legal penalties; an example cited was ~30-minute response for Sev1 (needs confirmation).
- Staffing includes weekday onsite coverage at XAI and APJ/EMEA off-hours coverage; weekends are lighter but monitored, with a goal of proactive incident notification.

---

*Source: [[Inbox/_archive/2025-10-29/2025-10-29 - Jason introduced his cloud-first vision for VAST (VAST-as-a-Service, multi-cloud.md|2025-10-29 - Jason introduced his cloud-first vision for VAST (VAST-as-a-Service, multi-cloud]]*

## Related

- [[Rick Haselton]]
- [[Jason Vallery]]
- [[Jeff Denworth]]
- [[Gordon Brown]]
- [[CoreWeave]]
- [[Microsoft]]
- [[Google]]
- [[Oracle]]
- [[XAI]]
- [[OpenAI]]
- [[Databricks]]