---
type: "people"
title: "Intro 1:1 on CS ops"
date: "2025-10-29"
person: "Rick Haselton"
participants: ["Rick Haselton", "Jason Vallery"]
source: "transcript"
source_ref: "Inbox/Transcripts/2025-10-29 - Intro 1-1 to understand Customer Success operations for CoreWeave and XAI and im.md"
tags:
  - "type/people"
  - "person/rick-haselton"
  - "generated"
---

# Intro 1:1 on CS ops

**Date**: 2025-10-29
**With**: Rick Haselton, Jason Vallery

## Summary

Jason met with Rick to understand Customer Success operations for CoreWeave and XAI and how that maps to a future VAST-as-a-Service/SRE operating model. Rick described a managed-services engagement (Slack-first, tickets in Salesforce/JIRA with vForce escalations), common incident drivers (networking and node failures), and the RMA workflow back to VAST depots. They also discussed XAI workload/storage patterns and the existence of formal SLAs/SLOs (including ~30-minute Sev1 response) with potential penalties.
## Action Items
- [ ] Connect with Gordon Brown to review CoreWeave/XAI SLAs, SLOs, and penalty clauses @Myself 📅 2025-11-08 ⏫ #task
- [ ] Draft an initial SRE/managed-services operating model for a future VAST-as-a-Service @Myself 📅 2025-11-08 ⏫ #task
- [ ] Document XAI workload patterns (checkpointing, inferencing, GPU-adjacent vs central storage) to inform product roadmap @Myself 📅 2025-11-08 ⏫ #task
- [ ] Outline a remediation plan for recurring networking issues at XAI @Rick Haselton 📅 2025-11-08 ⏫ #task
- [ ] Introduce Jason to Gordon Brown (CoreWeave CSM) to share SLA/SLO details @Rick Haselton 📅 2025-11-08 ⏫ #task
- [ ] Confirm which cloud provider(s) host XAI’s off-site data and share specifics @Rick Haselton 📅 2025-11-08 🔽 #task
- [ ] Provide recent capacity and I/O pattern snapshots for XAI Colossus and Colossus 2 clusters @Rick Haselton 📅 2025-11-08 🔽 #task
- [ ] Verify whether object clusters are used for checkpointing at XAI and any planned changes @Rick Haselton 📅 2025-11-08 🔽 #task

## Key Information
- Rick is the tech lead for CoreWeave (#1) and xAI (#3) accounts.
- Both CoreWeave and xAI deployments discussed are on-prem; xAI pulls some cloud-hosted data down to on-site clusters for work.
- xAI requested a single large cluster spanning multiple clusters; VAST supports S3 sync replication and site-to-site global namespace but not a single filesystem across disparate clusters.
- xAI object clusters are approximately 313–314 PB used per cluster and primarily store raw training data (e.g., YouTube, Instagram).
- Checkpointing patterns (when present) show periodic spikes roughly every 10–15 minutes; usage has varied over time.
- Engagement model is managed-services/SRE-like: alarms flow into Slack; urgent issues move to live calls; tickets are created in Salesforce (CS) and JIRA/Orion with vForce for engineering escalations.
- Most common issues are networking and C-node/D-node failures; some questions involve Kubernetes/CSI integration.
- RMA workflow: hardware is returned to VAST depots (Campbell, CA or Sacramento, CA) for repair/refurb; preference is full C-node replacement; some D-node FRUs (e.g., fans) are field-replaceable.
- Coverage model includes weekday on-site support for xAI hardware; APJ/EMEA cover off-hours; weekends are less staffed; goal is proactive outreach before customer reports incidents.
- Formal SLAs/SLOs exist (example mentioned: ~30-minute Sev1 response) with potential penalties if thresholds are breached; Gordon Brown is CoreWeave CSM.

---

*Source: [[Inbox/Transcripts/2025-10-29 - Intro 1-1 to understand Customer Success operations for CoreWeave and XAI and im.md|2025-10-29 - Intro 1-1 to understand Customer Success operations for CoreWeave and XAI and im]]*

## Related

- [[Rick Haselton]]
- [[Jason Vallery]]
- [[Gordon Brown]]
- [[CoreWeave]]
- [[xAI]]
- [[Microsoft]]
- [[Google]]
- [[Oracle]]
