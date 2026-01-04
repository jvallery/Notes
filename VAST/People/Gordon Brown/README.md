---
type: people
title: Gordon Brown
created: '2026-01-03'
last_contact: '2025-10-29'
auto_created: true
tags:
- type/people
- needs-review
---

# Gordon Brown

## Profile

**Role**: Customer Success Manager (CSM) for CoreWeave at VAST Data (Customer Success)
**Relationship**: Internal collaborator; CoreWeave CSM

**Background**:
- Owns/knows CoreWeave SLA/SLO and legal penalty clause details; key source for response-time commitments (e.g., ~30-minute Sev1).
- Owns/knows details of CoreWeave (and referenced XAI) SLO/SLA commitments and legal penalty clauses; cited ~30-minute Sev1 response target (needs confirmation).

## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed AND contains(text, "Gordon Brown")
SORT due ASC
```

## Recent Context

- 2025-10-29: [[2025-10-29 - Intro 1-1 to understand Customer Success operations for CoreWeave and XAI and im]] - Weekly 1:1 intro with Rick Haselton to understand how Customer Success operates for the CoreWeave an... (via Rick Haselton)
- 2025-10-29: [[2025-10-29 - Jason introduced his cloud-first vision for VAST (VAST-as-a-Service, multi-cloud]] - 1:1 between Jason Vallery and Rick Haselton covering Jason’s cloud-first VAST-as-a-Service vision an... (via Rick Haselton)

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

## Background

_Career history, expertise, interests, personal details shared..._

## Related Customers

- [[CoreWeave]]

## Related Projects

- [[VAST-as-a-Service]]

## Related

---
*Last updated: *
