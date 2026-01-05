---
type: people
title: 1:1 with Rick Haselton, CS ops for CoreWeave and xAI and implications for VAST-as-a-Service
date: '2025-10-29'
person: Rick Haselton
participants:
- Jason Vallery
- Rick Haselton
source: transcript
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-29 - Intro 1-1 to understand Customer Success operations for CoreWeave and XAI and im.md
tags:
- type/people
- generated
---

# 1:1 with Rick Haselton, CS ops for CoreWeave and xAI and implications for VAST-as-a-Service

**Date**: 2025-10-29
**With**: Jason Vallery, Rick Haselton

## Summary

Jason Vallery met 1:1 with Rick Haselton to understand Customer Success operations for CoreWeave and xAI and what a managed-services/SRE-style model implies for a future VAST-as-a-Service offering. Rick described Slack-first incident handling, Salesforce and JIRA escalation workflows, common failure modes (networking and node failures), and formal SLA/SLO obligations with potential penalties. The discussion also covered xAI workload patterns and architectural constraints, including xAI’s desire for a single large cluster across multiple clusters and VAST’s current limitations.

## Action Items

- [?] Connect with Gordon Brown to review CoreWeave and xAI SLA/SLO terms and any penalty clauses so Cloud Product Management can incorporate requirements into VAST-as-a-Service planning. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Draft an initial SRE and managed-services operating model for a future VAST-as-a-Service offering, based on current CoreWeave and xAI Customer Success practices (Slack-first, ticketing, on-call, escalation). @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Document xAI workload patterns relevant to product planning, including checkpointing cadence, inferencing behavior, and the split between GPU-adjacent storage and central/object storage. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Outline a remediation plan for recurring networking issues impacting xAI operations, including likely root causes, mitigations, and escalation paths. @Rick Haselton 📅 2025-11-08 #task #proposed #auto

- [?] Introduce Jason Vallery to Gordon Brown (CoreWeave CSM) to share CoreWeave and xAI SLA/SLO details and operational expectations. @Rick Haselton 📅 2025-11-08 #task #proposed #auto

- [?] Confirm which public cloud provider(s) host xAI’s off-site data (for example, Google Cloud Platform) and share specifics needed for hybrid and data-movement planning. @Rick Haselton 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Provide recent capacity and I/O pattern snapshots for xAI Colossus and Colossus 2 clusters to inform sizing, caching, and operational model decisions. @Rick Haselton 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Verify whether xAI object clusters are currently used for checkpointing and whether any planned changes will shift checkpointing back to object clusters. @Rick Haselton 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Connect with Gordon Brown to review CoreWeave and xAI SLA/SLO terms and any penalty clauses so Cloud Product Management can incorporate requirements into a future VAST-as-a-Service operating model. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Draft an initial SRE and managed-services operating model proposal for a future VAST-as-a-Service offering, based on current CoreWeave and xAI Customer Success practices (Slack-first, ticketing, on-call, monitoring). @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Document xAI workload patterns, including checkpointing cadence, inferencing behavior, and the split between GPU-adjacent storage and central/object storage, to inform cloud product roadmap requirements. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Outline a remediation plan for recurring networking issues impacting xAI clusters, including likely root causes, mitigations, and operational runbooks for Customer Success. @Rick Haselton 📅 2025-11-08 #task #proposed #auto

- [?] Introduce Jason Vallery to Gordon Brown (CoreWeave CSM) to share CoreWeave and xAI SLA/SLO details and escalation expectations. @Rick Haselton 📅 2025-11-08 #task #proposed #auto

- [?] Confirm which public cloud provider(s) host xAI off-site data (for example, whether it is Google Cloud Platform) and share specifics with Jason Vallery for cloud strategy alignment. @Rick Haselton 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Provide recent capacity and I/O pattern snapshots for xAI Colossus and Colossus 2 clusters to help Cloud Product Management model caching, checkpointing, and replication requirements. @Rick Haselton 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Verify whether xAI uses object clusters for checkpointing today and whether there are planned changes to checkpointing architecture, then report back to Jason Vallery. @Rick Haselton 📅 2025-11-08 🔽 #task #proposed #auto

## Key Information

- Rick Haselton is the technical lead in Customer Success for two of VAST Data’s three largest customers, CoreWeave (largest) and xAI (third largest).

- CoreWeave and xAI deployments supported by VAST Data are on-premises; xAI also has data in a public cloud and pulls that data down to on-site clusters for work such as checkpointing and inferencing.

- Rick Haselton was unsure which cloud provider hosts xAI’s off-site data, but noted xAI has discussed Google (potentially Google Cloud Platform).

- xAI requested that multiple VAST clusters (described as four clusters, and also referenced as eight total across file and object) operate as one large cluster, but VAST Data does not currently support a single file system spanning multiple disparate clusters.

- VAST Data supports synchronous replication for S3 bucket data and supports a site-to-site global namespace, but not a single file system across multiple clusters.

- xAI object clusters are approximately 314 PB used per cluster and store raw training data (examples mentioned: YouTube and Instagram).

- xAI checkpointing I/O patterns observed by Rick Haselton show low baseline bandwidth with periodic spikes roughly every 10 to 15 minutes.

- Customer Success engagement for CoreWeave and xAI is run in a managed-services/SRE style: alarms flow into Slack, and urgent issues move to live calls.

- Ticketing workflow: Salesforce is used for Customer Success ticketing; JIRA (referred to as Orion) is used for engineering escalations with vForce involvement.

- Common operational issues for CoreWeave and xAI include networking problems, C-node and D-node failures, and Kubernetes/CSI integration questions.

- Hardware service preference is full C-node replacement; some D-node FRUs (for example, fans) are field-replaceable, and CoreWeave data center technicians assist with replacements.

- RMA workflow returns failed hardware to VAST Data depots in Campbell or Sacramento for repair or refurbishment.

- Support coverage model described: xAI has weekday on-site support; APJ and EMEA teams cover off-hours; weekend coverage is lighter; the team aims for proactive outreach during incidents.

- CoreWeave and xAI have formal legal SLA/SLO obligations, including an approximately 30-minute Sev1 response target and potential penalties for breaches.

- Gordon Brown is the Customer Success Manager (CSM) for the CoreWeave account at VAST Data.

---

- Rick Haselton is the technical lead in Customer Success for two of VAST Data's three largest accounts, CoreWeave (largest) and xAI (third largest).

- CoreWeave and xAI deployments supported by VAST Data Customer Success are primarily on-premises; xAI may keep some data in a public cloud but pulls that data down to on-site clusters for checkpointing and inferencing workflows.

- xAI requested that multiple VAST clusters (planned as separate file and object clusters) operate as one large cluster; VAST supports S3 synchronous replication and a site-to-site global namespace, but does not support a single file system spanning multiple disparate clusters.

- xAI object clusters are approximately 314 PB used per cluster and store raw training data (examples mentioned: YouTube and Instagram data).

- xAI checkpointing behavior observed by Customer Success shows periodic I/O spikes roughly every 10 to 15 minutes, with low bandwidth between spikes.

- VAST Data Customer Success for CoreWeave and xAI operates like a managed-services/SRE model: alarms flow into Slack, urgent issues escalate to live calls, and work is tracked via tickets.

- Ticketing and escalation flow: Salesforce is used for Customer Success case tracking; JIRA (referred to as Orion) is used for engineering escalations with vForce involvement.

- Common operational issues for CoreWeave and xAI include networking problems, C-node and D-node failures, and questions related to Kubernetes and CSI integration.

- Hardware support preference is often full C-node replacement; some D-node FRUs (for example, fans) are field-replaceable, and CoreWeave data center technicians can assist with on-site work.

- Support coverage model described: xAI has weekday on-site support; APJ and EMEA teams cover off-hours; weekend coverage is lighter; Customer Success aims for proactive outreach during incidents.

- CoreWeave and xAI have formal legal SLAs and SLOs (example mentioned: approximately 30-minute Sev1 response) with potential penalties for non-compliance.
