---
type: "projects"
title: "UK Met Office Gen2 storage/compute working session, pilot planning and Azure SKU dependency"
date: "2025-10-28"
project: ""
participants: ["Jason Vallery", "Niko Dukic", "Lior Genzel"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-28 - Working session on UK Met Gen2 storagecompute plan. VaST to run a pilot to vali.md"
tags:
  - "type/projects"
  - "project/"
  - "generated"

---

# UK Met Office Gen2 storage/compute working session, pilot planning and Azure SKU dependency

**Date**: 2025-10-28
**Project**: [[]]
**Attendees**: Jason Vallery, Niko Dukic, Lior Genzel

## Summary

Internal working session between Jason Vallery, Niko Dukic, and Lior Genzel on the UK Met Office Gen2 storage and compute approach and how VAST should run a pilot to validate mandatory requirements. The team is waiting on Microsoft Azure to confirm a compute VM SKU meeting ~300 TB per node and ~800 Gb NIC requirements by 2025-11-15, with an interim option to start testing on 100 Gb VMs. A fallback path is ODM or bare metal with an SDN intermediary, but it is considered operationally complex and adds an extra network hop.


## Action Items


- [?] Confirm availability and exact Azure VM SKU name for VMs with high-speed NICs that meet UK Met Office Gen2 requirements, and provide the expected readiness date. @Niko Dukic 📅 2025-10-28 ⏫ #task #proposed #auto

- [?] Share the UK Met Office Gen2 email thread with Mike and Anand, then schedule and run a configuration meeting to align on the pilot test setup. @Lior Genzel 📅 2025-10-29 ⏫ #task #proposed #auto

- [?] Align with Mike to confirm Anand is waiting on the minimal test configuration and to greenlight staging for the UK Met Office Gen2 pilot. @Niko Dukic 📅 2025-10-29 ⏫ #task #proposed #auto

- [?] Propose a minimal viable UK Met Office Gen2 pilot test configuration, including node count and per-node capacity and compute, sufficient for functional validation and initial scale testing. @Lior Genzel 📅 2025-10-29 ⏫ #task #proposed #auto

- [?] Obtain written confirmation from Microsoft Azure and a timeline for VMs supporting approximately 300 TB per node and approximately 800 Gb NICs for UK Met Office Gen2. @Niko Dukic 📅 2025-11-15 ⏫ #task #proposed #auto

- [?] Prepare to ship and deploy a small VAST ODM cluster for UK Met Office Gen2 pilot testing if the Azure VM SKU path is delayed or not viable, prioritizing rapid turn-up. @Lior Genzel 📅 2025-11-08 #task #proposed #auto

- [?] Provide initial UK Met Office Gen2 IO workload details, including sequential vs random behavior, read-write mix, and typical file sizes, once available. @Niko Dukic 📅 2025-11-08 #task #proposed #auto

- [?] Decide between the Azure VM path and the bare metal plus SDN intermediary path for UK Met Office Gen2 based on Microsoft SKU outcome and delivery timelines. @Niko Dukic 📅 2025-11-15 ⏫ #task #proposed #auto

- [?] Validate whether Azure HBv5 with InfiniBand is viable for backend storage connectivity for the UK Met Office Gen2 deployment. @Niko Dukic 📅 2025-11-08 #task #proposed #auto

- [?] If the full high-speed Azure VM SKU is delayed, confirm starting UK Met Office Gen2 tests on a 100 Gb VM SKU and define the migration path to the target SKU. @Niko Dukic 📅 2025-10-29 #task #proposed #auto

- [?] Confirm that UK Met Office Gen2 pilot validation criteria map directly to the contract's mandatory requirements (and separate nice-to-have requirements). @Myself 📅 2025-11-08 #task #proposed #auto






## Key Information


- UK Met Office Gen2 is a replacement for the current ClusterStore and is not an archive project.

- The original UK Met Office contract was described as scaling up to 3x, but whether the full 3x scale applies is still under discussion with the Met Office and internally.

- Two deployment paths are being evaluated for UK Met Office Gen2: (1) Azure-provided compute VMs with high-speed NICs (preferred) or (2) ODM or bare metal with an SDN intermediary/bridge (more complex).

- The requested Azure VM node specification for UK Met Office Gen2 includes approximately 300 TB per node and approximately 800 Gb NICs; the previously proposed LSv5/LSP5 option does not fit the requirement.

- Microsoft Azure asked for time until 2025-11-15 to propose a new VM SKU that meets the UK Met Office Gen2 requirements.

- Lior Genzel reported a conversation with Igal Figlin indicating Microsoft intends to build VMs with high-speed networking for UK Met Office Gen2, but the team needs written confirmation and a delivery timeline.

- An interim plan discussed is to start pilot testing on an available 100 Gb Azure VM SKU and migrate to the full high-speed VM SKU when it becomes available.

- The UK Met Office Gen2 workload was described as large files with mostly sequential IO and roughly a 50/50 read-write mix, with detailed IO characterization still pending.

- Niko Dukic stated he officially joined Mike's team on 2025-10-28, after a planned 2025-10-15 transition date.

- Lior Genzel stated he was in Eilat, Israel during the meeting and planned to return to the United States in about 10 days.



---

*Source: [[2025-10-28 - Working session on UK Met Gen2 storagecompute plan. VaST to run a pilot to vali]]*