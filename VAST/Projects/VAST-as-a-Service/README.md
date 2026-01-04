---
type: projects
title: VAST-as-a-Service
created: '2026-01-03'
last_updated: ''
status: proposed
auto_created: true
tags:
- type/projects
- needs-review
- status/proposed
last_contact: '2025-10-29'
---

# VAST-as-a-Service

## Overview

Future cloud/SaaS operating model for VAST (multi-tenant service) informed by current managed-services/SRE-style support for large on-prem AI customers (CoreWeave, XAI).

## Status

| Field | Value |
|-------|-------|
| **Status** | proposed |
| **Owner** | Jason Vallery |

## Current Blockers

- ❌ Small CS/SRE team and heavy load may impact responsiveness and sustainability
- ❌ After-hours/weekend coverage gaps could jeopardize SLA commitments
- ❌ Frequent networking issues drive incidents and latency
- ❌ XAI desire for a single file system across multiple clusters is not currently supported (only site-to-site global namespace; S3 sync replication)
- ❌ SLA/SLO penalty exposure if availability thresholds are breached

## Next Steps

- [ ] Draft an initial SRE/managed-services operating model for VAST-as-a-Service
- [ ] Document XAI workload patterns (checkpointing/inferencing; GPU-adjacent vs central storage) to inform roadmap
- [ ] Review CoreWeave/XAI SLAs, SLOs, and penalty clauses with Gordon Brown
- [ ] Outline remediation plan for recurring networking issues at XAI
- [ ] Confirm which cloud provider(s) host XAI off-site data
- [ ] Collect recent capacity and I/O pattern snapshots for XAI Colossus/Colossus 2
- [ ] Draft initial operating model (SRE vs CS roles, on-call, comms, SLAs)
- [ ] Review legal SLA document and penalty clauses for CoreWeave/XAI as input to VaaS model

## Collaborators

| Person | Role | Company |
|--------|------|---------|
| [[Rick Haselton]] | Customer Success tech lead (managed services / SRE-style) | VAST Data |
| [[Gordon Brown]] | Customer Success Manager (CSM) for CoreWeave |  |
| [[Jeff Denworth]] |  | VAST Data |
| [[Yancey]] |  | VAST Data |
| [[Jason Vallery]] | Product management (cloud); partnerships with hyperscale cloud providers | VAST Data |

## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed
SORT due ASC
```


## Key Decisions

_Important decisions made on this project..._


## Key Facts

- Rick Haselton is the CS tech lead for CoreWeave (#1) and XAI (#3) accounts and operates in a managed-services/SRE model.
- Support model is Slack-first with alarms into dedicated channels; urgent issues move to live calls; tickets tracked in Salesforce (CS) and JIRA/Orion with vForce for engineering escalations.
- Both CoreWeave and XAI deployments are on-prem; XAI pulls cloud-hosted data down to on-site clusters for processing.
- XAI requested one large cluster spanning multiple clusters; VAST supports S3 synchronous replication and site-to-site global namespace but not a single file system across multiple clusters.
- XAI object clusters store raw training data; examples include YouTube and Instagram; approximately 313–314 PB used per object cluster.
- Checkpointing shows periodic spikes (~10–15 minutes) and has varied over time; GPU-adjacent storage behaves like cache/checkpointing while central/object storage holds raw data.
- Common incident drivers: networking issues, C-node/D-node failures, and Kubernetes/CSI integration questions.
- Hardware RMA process: prefer full C-node replacement; some D-node FRUs (fans) are field-replaceable; failed parts return to VAST depots (Campbell or Sacramento) for repair/refurb.
- Coverage model: XAI has weekday on-site support; APJ/EMEA cover off-hours; weekends are lighter; goal is proactive outreach before customer reports incidents.
- Formal legal SLAs/SLOs exist (e.g., ~30-minute Sev1 response) with potential penalties; Gordon Brown is CoreWeave CSM and key source for details.

## Topics / Themes

Customer Success operating model for large AI customers, Managed services / SRE-style engagement and proactive monitoring, Slack-first support workflow and ticketing (Salesforce, JIRA/Orion, vForce), XAI workload patterns: raw training data, checkpointing spikes, inferencing, GPU-adjacent storage vs central storage patterns, Networking and node failure incident patterns, Kubernetes/CSI integration questions, RMA and depot repair workflow, On-call coverage, staffing strain, and SLA/SLO penalty risk, Implications for future VAST-as-a-Service (multi-tenant SaaS), VAST cloud-first vision (VAST-as-a-Service, multi-cloud), Customer Success operating model vs SRE model, CoreWeave and XAI on-prem operations, XAI workload patterns (training data, checkpointing, inferencing), Multi-cluster single filesystem/namespace limitations

## Related People

- [[Rick Haselton]]
- [[Gordon Brown]]
- [[Jeff Denworth]]
- [[Yancey]]
- [[Jason Vallery]]

## Related Customers

- [[CoreWeave]]

## Recent Context

- 2025-10-29: [[2025-10-29 - Intro 1-1 to understand Customer Success operations for CoreWeave and XAI and im]] - Weekly 1:1 intro with Rick Haselton to understand how Customer Success operates for the CoreWeave an... (via Rick Haselton)
- 2025-10-29: [[2025-10-29 - Jason introduced his cloud-first vision for VAST (VAST-as-a-Service, multi-cloud]] - 1:1 between Jason Vallery and Rick Haselton covering Jason’s cloud-first VAST-as-a-Service vision an... (via Rick Haselton)

## Artifacts

```dataview
TABLE file.mtime as "Modified"
FROM ""
WHERE type != "readme" AND type != "projects"
SORT file.mtime DESC
```

---
*Last updated: *