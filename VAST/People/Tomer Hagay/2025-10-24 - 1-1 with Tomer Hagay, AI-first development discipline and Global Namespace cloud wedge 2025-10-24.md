---
type: "people"
title: "1:1 with Tomer Hagay, AI-first development discipline and Global Namespace cloud wedge (2025-10-24)"
date: "2025-10-24"
person: ""
participants: ["Jason Vallery", "Tomer Hagay"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-24 - Jason and Tomer discussed accelerating AI-driven software development practices.md"
tags:
  - "type/people"
  - "person/"
  - "generated"

---

# 1:1 with Tomer Hagay, AI-first development discipline and Global Namespace cloud wedge (2025-10-24)

**Date**: 2025-10-24
**With**: Jason Vallery, Tomer Hagay

## Summary

Jason Vallery and Tomer Hagay aligned that VAST should codify AI-first software development workflows and use the Cloud initiative as a wedge to raise process maturity and accountability. They reviewed VAST's RFE-to-feature-to-Jira flow, customer support model (Tier-3 co-pilots and per-customer Slack), and Global Namespace design (strict consistency with read leases today and write leases targeted for 5.5 preview). Jason will get hands-on with VAST via OVA or SC lab and they plan to continue the discussion next week.


## Action Items


- [?] Ping Josh Wentzell (Office of the CTO) to obtain VAST OVA access and onboarding for local lab testing. @TBD 📅 2025-10-27 ⏫ #task #proposed #auto

- [?] Coordinate with Andy Perlsteiner to obtain SC lab access as a backup or quick-start environment for hands-on testing. @Myself 📅 2025-10-27 #task #proposed #auto

- [?] Set up a local cluster using the VAST OVA to test Global Namespace behavior, caching and prefetch, and GPU-related workflows. @Myself 📅 2025-10-27 #task #proposed #auto

- [?] Review Google Anywhere Cache documentation and compare its policy and prefetch capabilities to VAST Data Global Namespace caching and prefetch. @Tomer Hagay 📅 2025-10-26 #task #proposed #auto

- [?] Ask Shachar to confirm whether VAST Data will mandate AI-first development, including training cadence and measurable adoption targets. @Tomer Hagay 📅 2025-10-27 ⏫ #task #proposed #auto

- [?] Draft VAST Cloud SaaS operating model requirements, including DevOps and LifeSite rotations, telemetry requirements, and 24x7 support expectations. @Myself 📅 2025-10-27 #task #proposed #auto

- [?] Schedule the next 1:1 with Tomer Hagay for the following week to continue alignment on cloud plan and process changes. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Meet with Customer Success leadership (example mentioned: Rich, last name not provided) to understand end-to-end account support workflows. @Myself 📅 2025-10-27 🔽 #task #proposed #auto

- [?] Confirm with Brendan (last name not provided) and Jeff Denworth that Cloud is P0 and clarify resourcing expectations. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Clarify VAST Data end-to-end development lifecycle, including gates, signoffs, source control, CI/CD, and release process, with Eyal Traitel and Noah Cohen or via documentation. @Myself 📅 2025-10-27 ⏫ #task #proposed #auto

- [?] Review and align on Global Namespace write-lease design and read redirection behaviors with the Tel Aviv engineering team for the 5.5 preview. @Tomer Hagay 📅 2025-10-27 🔽 #task #proposed #auto

- [?] Work with IT to assess feasibility and timeline for Slack multi-channel polling capability and report back. @Tomer Hagay 📅 2025-10-26 🔽 #task #proposed #auto






## Key Information


- VAST Data engineering has approximately 400 software developers.

- VAST Data release execution is described as waterfall-like with frequent schedule slips and limited accountability, for example the 5.4 release slipped from June 2025 to October 2025.

- Microsoft Azure Storage was cited as having approximately 1,600 software developers and Microsoft is enforcing structured AI-first development workflows including biweekly forced AI training days.

- VAST Data RFEs are captured in Salesforce, require SE manager approval, are triaged by Jonathan Hayes, and PMs aggregate RFEs into Features linked to Jira; Epics are not consistently used.

- VAST Data support model includes a Tier-3 'co-pilot' per account, a separate customer Slack workspace with per-customer channels, and a vForce team that builds hotfixes.

- VAST Data Global Namespace is designed for strict consistency and currently uses read leases with cache and prefetch; multi-protocol access on satellites includes NFS, SMB, and S3; write leases are targeted for a 5.5 preview.

- VAST Data 5.4 includes async replication plus Global Namespace, enabling active-active read and write access with point-in-time snapshots.

- For VAST Cloud, a pure lift-and-shift approach is considered unlikely to meet requirements; the approach discussed is a performant layer over cloud object storage with a region-spanning namespace and caching, using Google multi-region and caching patterns as a reference.

- Tomer Hagay observed that only a subset of VAST Data engineers, described as the strongest engineers, have adopted AI coding tools aggressively, while most engineers had not as of roughly August 2025; Tomer Hagay was unsure whether Shachar has set measurable AI adoption targets.

- Jason Vallery stated that OpenAI publicly claims approximately 95% of its code is written by AI and described personal experimentation with agentic coding tools (Anthropic Claude and OpenAI Codex) that can implement requirements, deploy to Kubernetes, run tests, and iterate on fixes with minimal human interaction.



---

*Source: [[2025-10-24 - Jason and Tomer discussed accelerating AI-driven software development practices]]*