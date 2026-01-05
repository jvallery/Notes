---
type: "people"
title: "1:1 with Tomer Hagay, using cloud initiative to drive AI-enabled engineering process maturity"
date: "2025-10-24"
person: ""
participants: ["Jason Vallery", "Tomer Hagay"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-24 - Jason and Tomer discussed accelerating VAST’s engineering maturity and cloud str.md"
tags:
  - "type/people"
  - "person/"
  - "generated"

---

# 1:1 with Tomer Hagay, using cloud initiative to drive AI-enabled engineering process maturity

**Date**: 2025-10-24
**With**: Jason Vallery, Tomer Hagay

## Summary

Jason Vallery and Tomer Hagay aligned on using VAST’s cloud initiative as leverage to improve engineering maturity, including AI-enabled development workflows, clearer planning, and stronger release accountability. They contrasted Microsoft and OpenAI AI-first development practices with VAST’s current RFE-driven, waterfall-ish process and discussed Global Namespace technical direction as a key cloud enabler.


## Action Items


- [?] Align with Shachar on AI development program goals and adoption metrics for VAST Data engineering. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Draft a proposal for an AI-enabled development workflow at VAST Data, including PR and audit standards, coding agent usage patterns, and a training cadence. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Validate Cloud P0 prioritization and resourcing with Brendan and Jeff Denworth. @Myself 📅 2025-10-27 ⏫ #task #proposed #auto

- [?] Review and document the current end-to-end VAST Data development lifecycle, including gates and tooling from Salesforce RFE to SFDC Feature to Jira to Release. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Contact Andy Perlsteiner to obtain SE lab access for hands-on evaluation of VAST Data capabilities. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Coordinate with Josh (Office of the CTO) to obtain OVA and software bits for local testing. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Read Google Anywhere Cache documentation and compare it to VAST Data Global Namespace, then summarize gaps and opportunities. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Set up a local VAST Data OVA on a home cluster, move test data, and validate GPU workflows. @Myself 📅 2025-10-27 🔽 #task #proposed #auto

- [?] Schedule a follow-up 1:1 meeting with Tomer Hagay for the week after 2025-10-24. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Plan a Tel Aviv discussion focused on Global Namespace write-lease semantics and the redirection model. @Tomer Hagay 📅 2025-10-27 #task #proposed #auto

- [?] Connect with Rich to map the full VAST Data customer support structure and escalation paths. @Myself 📅 2025-10-26 🔽 #task #proposed #auto

- [?] Share FRD templates and examples with Jason Vallery for review. @Tomer Hagay 📅 2025-10-27 #task #proposed #auto

- [?] Introduce Jason Vallery to Eyal Traitel and Noah Cohen to align on planning cadence and scoping. @Tomer Hagay 📅 2025-10-27 #task #proposed #auto

- [?] Provide Jason Vallery access to PM Salesforce RFE and Feature dashboards and associated Jira links. @Tomer Hagay 📅 2025-10-27 #task #proposed #auto

- [?] Send Google Anywhere Cache reference links to Tomer Hagay. @Myself 📅 2025-10-26 🔽 #task #proposed #auto




## Decisions


- Proceed with OVA and SE lab onboarding so Jason Vallery can evaluate VAST Data Global Namespace and cloud workflows firsthand.

- Schedule a follow-up 1:1 meeting the following week to continue alignment on cloud prioritization and engineering process improvements.




## Key Information


- VAST Data engineering organization is approximately 400 software developers.

- Microsoft Azure Storage has approximately 1,600 software developers, and Microsoft leadership is enforcing AI training and standardized workflows (planning cadence, PR process, audits, and tracking) to improve productivity.

- OpenAI publicly claims that approximately 95% of its code is written by AI (developers primarily direct coding agents rather than hand-writing most code).

- VAST Data releases have slipped without clear consequences, and releases have had many hotfixes (examples cited: VAST 5.4 slipped by months; VAST 5.2 had many hotfixes).

- VAST Data product development intake is highly RFE-driven via Salesforce (SFDC), with Jira used at the ticket level and inconsistent use of epics; SFDC features aggregate multiple RFEs and sync to a Jira fixed version.

- Jonathan Hayes leads RFE triage for VAST Data’s Salesforce RFE pipeline.

- VAST Data support model includes Tier-3 Co-Pilots assigned per account and dedicated Slack channels per customer for support.

- VAST Data Global Namespace provides strict consistency with lease-based caching; NFS, SMB, and S3 are served on satellites; read leases exist now and write leases are targeted for VAST 5.5 preview.

- VAST Data 5.4 includes async replication plus Global Namespace, enabling active-active read-write with snapshot history.

- Jason Vallery believes cloud success for VAST Data is unlikely to come from lift-and-shift; it likely requires a high-performance layer over object storage with a global cache.

- Jason Vallery was introduced to Josh (Office of the CTO) for OVA and lab onboarding, and Andy Perlsteiner oversees SE labs for hands-on evaluation.

- Tomer Hagay reported that VAST Data has a reputation in Israel for being difficult to get into as a software developer, with a high bar for talent; VAST recently started hiring some younger engineers.

- Tomer Hagay referenced an engineering leader named Albert who leads platform management plus UI/UX and API components, and noted that a subset of very strong engineers adopted AI tools quickly while most engineers had not (as of roughly two months before 2025-10-24).

- Jason Vallery stated he took a sabbatical starting around June 2025 and used the summer to learn modern AI-assisted software development tools (Anthropic Claude agents and OpenAI Codex), including agentic workflows that can deploy to Kubernetes, run tests, analyze logs, fix bugs, and redeploy with minimal human interaction.



---

*Source: [[2025-10-24 - Jason and Tomer discussed accelerating VAST’s engineering maturity and cloud str]]*