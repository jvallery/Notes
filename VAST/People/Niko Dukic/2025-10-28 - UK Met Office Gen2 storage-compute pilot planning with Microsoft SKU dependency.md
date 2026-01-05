---
type: "projects"
title: "UK Met Office Gen2 storage/compute pilot planning with Microsoft SKU dependency"
date: "2025-10-28"
project: ""
participants: ["Jason Vallery", "Niko Dukic", "Lior Genzel", "Igal Figlin", "Mike (unknown last name)", "Anand (unknown last name)"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-28 - Working session on UK Met Gen2 storagecompute plan. VaST to run a pilot to vali.md"
tags:
  - "type/projects"
  - "project/"
  - "generated"

---

# UK Met Office Gen2 storage/compute pilot planning with Microsoft SKU dependency

**Date**: 2025-10-28
**Project**: [[]]
**Attendees**: Jason Vallery, Niko Dukic, Lior Genzel, Igal Figlin, Mike (unknown last name), Anand (unknown last name)

## Summary

Jason Vallery, Niko Dukic, and Lior Genzel aligned on running a VAST pilot to validate UK Met Office Gen2 mandatory requirements while Microsoft finalizes an Azure compute VM SKU that can meet high-capacity and high-NIC bandwidth needs. Two deployment paths remain open, Azure-provided VMs (preferred) versus ODM/bare metal with an SDN intermediary (higher complexity), with interim testing potentially starting on lower-bandwidth VMs.


## Action Items


- [?] Confirm the exact Azure VM SKU name and availability date that meets approximately 300 TB per node and 800 Gb NIC requirements for UK Met Office Gen2, and provide written confirmation and timeline. @Niko Dukic 📅 2025-11-15 ⏫ #task #proposed #auto

- [?] Share the UK Met Office Gen2 email thread with Mike (unknown last name) and Anand (unknown last name), schedule a configuration meeting, and propose a minimal viable test configuration (node count, per-node capacity, and compute) sufficient for functional and initial scale testing. @Lior Genzel 📅 2025-10-29 ⏫ #task #proposed #auto

- [?] Align with Mike (unknown last name) to confirm Anand (unknown last name) is waiting on the minimal test configuration and to greenlight staging for UK Met Office Gen2 pilot testing in a Microsoft data center. @Niko Dukic 📅 2025-10-29 ⏫ #task #proposed #auto

- [?] Prepare to ship and deploy a small VAST ODM cluster for UK Met Office Gen2 testing in a Microsoft data center if the Azure VM SKU path is delayed or does not meet requirements, prioritizing rapid turn-up. @Lior Genzel 📅 2025-11-08 #task #proposed #auto

- [?] Confirm that UK Met Office Gen2 pilot validation criteria map to contract mandatory requirements (separate mandatory requirements from nice-to-have requirements). @Myself 📅 2025-11-08 #task #proposed #auto






## Key Information


- UK Met Office Gen2 is a replacement for the current ClusterStore and is not an archive project.

- The original UK Met Office contract language envisioned scaling up to 3x, but whether the full 3x scale applies is still under discussion with the UK Met Office and internally.

- Two compute deployment paths are being considered for UK Met Office Gen2: Azure-provided compute VMs (preferred) versus ODM/bare metal with an SDN intermediary, which adds operational complexity and an extra network hop.

- VAST requested an Azure VM node specification of approximately 300 TB per node and 800 Gb NICs for the UK Met Office Gen2 design.

- Microsoft indicated it would come back by 2025-11-15 with a new Azure compute VM SKU proposal because the previously proposed LSv5/LSP5 option does not fit the UK Met Office Gen2 requirements.

- Igal Figlin told Lior Genzel informally that Microsoft is committed to building Azure VMs with high-speed NICs (discussion referenced 800 Gb and possibly 400 Gb) and the required capacity, but written confirmation and timeline are still needed.

- Lior Genzel reached out to Anand (unknown last name) and stated VAST wants to place ODM hardware in a Microsoft data center so Microsoft can start testing VAST capabilities for UK Met Office Gen2; Anand is waiting for a minimal required configuration and a greenlight from Mike (unknown last name).



---

*Source: [[2025-10-28 - Working session on UK Met Gen2 storagecompute plan. VaST to run a pilot to vali]]*