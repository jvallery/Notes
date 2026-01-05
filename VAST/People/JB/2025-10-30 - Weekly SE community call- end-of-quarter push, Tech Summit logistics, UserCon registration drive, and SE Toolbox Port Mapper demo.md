---
type: people
title: 'Weekly SE community call: end-of-quarter push, Tech Summit logistics, UserCon registration drive, and SE Toolbox Port Mapper demo'
date: '2025-10-30'
participants:
- JB
- Rob Banga
- Deandre Jackson
- Stacy
- Jeff Moeller
- Andrew Stack
- Andy Bernstein
- Tim
- Paul
- Parker
- Travis
source: transcript
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-30 - Weekly SE community call covering end-of-quarter push, Tech Summit logistics, an.md
tags:
- type/people
- generated
person: JB
---

# Weekly SE community call: end-of-quarter push, Tech Summit logistics, UserCon registration drive, and SE Toolbox Port Mapper demo

**Date**: 2025-10-30
**Forum**: [[]]
**Attendees**: JB, Rob Banga, Deandre Jackson, Stacy, Jeff Moeller, Andrew Stack, Andy Bernstein, Tim, Paul, Parker, Travis

## Summary

Weekly SE community call focused on end-of-quarter execution, Tech Summit logistics and policy reminders, and driving UserCon registrations for already-sold tickets. The call also launched the SE Toolbox series with Jeff Moeller demoing a Python GUI tool (Port Mapper) to automate switch port mapping, config generation, and Lucidchart overlays for converged or split networking designs.

## Action Items

- [?] Drive UserCon registrations for customers with sold or bundled tickets by coordinating with AEs and starting outreach immediately. @TBD 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Share a dashboard showing UserCon ticket sales and registrations by account with the SE team. @Rob Banga 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Send the Tech Summit agenda email to attendees. @Deandre Jackson 📅 2025-10-30 ⏫ #task #proposed #auto

- [?] Fix Tech Summit hotel confirmation email verbiage and ensure hotel confirmation emails are sent by Tuesday 2025-11-04. @Deandre Jackson 📅 2025-11-04 ⏫ #task #proposed #auto

- [?] Re-send the Tech Summit expense policy reminder to Tech Summit attendees. @Stacy 📅 2025-11-08 #task #proposed #auto

- [?] Prepare and distribute sign-up sheets for the Tech Summit Sportsplex gaming night. @Deandre Jackson 📅 2025-11-08 #task #proposed #auto

- [?] Add an Arista 24-port switch profile to the Port Mapper tool. @Jeff Moeller 📅 2025-11-08 #task #proposed #auto

- [?] Establish versioning and hosting for Port Mapper (for example, GitHub) to support distribution and change control. @Jeff Moeller 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Schedule recurring SE Toolbox slots (target 1-2 per month) and collect submissions from SEs for future sessions. @JB 📅 2025-11-08 #task #proposed #auto

- [?] Consider scheduling an SCO session to cover the Port Mapper tool and its usage. @JB 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Try the Port Mapper tool and provide feedback to Jeff Moeller on usability and gaps (including IPv6 and offline workflows). @TBD 📅 2025-11-08 #task #proposed #auto

- [?] Open a networking field request whenever network architecture guidance is needed (for example, converged vs split networking decisions and MLAG boundaries). @TBD 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Drive UserCon registrations for customers with sold or bundled tickets by coordinating with AEs and starting customer outreach. @TBD 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Share a dashboard showing UserCon ticket sales and completed registrations by account so SEs can target outreach. @Rob Banga 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Fix Tech Summit hotel confirmation email verbiage and ensure hotel confirmation emails are sent by Tuesday, 2025-11-04. @Deandre Jackson 📅 2025-11-04 ⏫ #task #proposed #auto

- [?] Re-send the Tech Summit expense policy reminder to Tech Summit attendees emphasizing no reimbursement outside official events. @Stacy 📅 2025-11-08 #task #proposed #auto

- [?] Establish versioning and hosting for the Port Mapper tool (for example, GitHub) to support distribution and change control. @Jeff Moeller 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Schedule recurring SE Toolbox slots (1 to 2 per month) and collect submissions from SEs for future sessions. @JB 📅 2025-11-08 #task #proposed #auto

- [?] Consider scheduling an SCO session to cover the Port Mapper tool in more depth. @JB 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Try the Port Mapper tool and provide feedback to Jeff Moeller on usability, missing switch profiles, and workflow gaps. @TBD 📅 2025-11-08 #task #proposed #auto

- [?] Open networking field requests whenever architecture guidance is needed (for example, converged vs split networking decisions and MLAG boundaries) instead of ad hoc designs. @TBD 📅 2025-11-08 🔽 #task #proposed #auto

## Decisions

- Launch an 'SE Toolbox' segment on the weekly SE community call on an approximately monthly cadence (targeting 1-2 sessions per month).

- Set Tech Summit evening events as: Day 1 reception, Day 2 OPA tavern event, Day 3 Sportsplex gaming event with prizes.

- Enforce a strict Tech Summit expense policy with no reimbursement for spending outside official Tech Summit events.

- Assign SEs responsibility to drive UserCon attendance by converting sold or bundled tickets into completed registrations in coordination with AEs.

- Launch an 'SE Toolbox' segment on the SE community call on an approximately monthly cadence (targeting 1 to 2 sessions per month).

- Enforce a strict Tech Summit expense policy: no reimbursement for spending outside official Tech Summit events.

## Key Information

- The VAST Data SE community is approximately 175 people, with about 50 attending this weekly SE community call.

- The organization was in the last week of the quarter (referred to as 'end of Q3') with multiple large deals still in flight.

- Tech Summit was stated to be in two weeks from 2025-10-30, and Tech Summit hotel confirmation emails were due by Tuesday 2025-11-04.

- UserCon registration status as of 2025-10-30: 19 registered, about 40 tickets sold, and about 100 additional tickets expected to close in the next few days; a dashboard will be shared to show ticket sales and registrations by account.

- Tech Summit evening events were set as: Day 1 reception, Day 2 OPA tavern event, and Day 3 Sportsplex gaming event with prizes.

- A strict Tech Summit expense policy was reiterated: no reimbursement for spending outside official Tech Summit events.

- Jeff Moeller presented 'Port Mapper' as part of the SE Toolbox, describing it as a Python-based GUI that automates switch port mapping, configuration generation, Lucidchart PNG overlays, and planning for converged or split networking with per-rack bandwidth validation.

- Port Mapper supports switch selection for NVIDIA/Mellanox, Cisco, and Arista; supports JSON import/export; can generate legacy install commands; and depends on VPN connectivity to enforce the latest switch configuration templates.

- Port Mapper handles Cisco ASIC slice balancing and Arista physical port ordering, but does not support IPv6 yet.

- SEs were reminded not to plug clients into southbound switches and to use the networking field request process for network architecture guidance.

---

- The VAST SE community is approximately 175 people, with about 50 attending this weekly SE community call.

- VAST is in the last week of the quarter (referred to as 'end of Q3') with multiple large deals still in flight.

- Tech Summit is scheduled for approximately two weeks after 2025-10-30, and logistics are in final preparation.

- UserCon status as of 2025-10-30: 19 registrations completed, about 40 tickets sold but not yet registered, and about 100 additional tickets expected to close within a few days.

- Tech Summit evening events were defined as: Day 1 reception, Day 2 OPA tavern event, and Day 3 Sportsplex gaming event with prizes.

- Jeff Moeller introduced 'Port Mapper', a Python-based GUI tool that automates switch port mapping, configuration generation, and Lucidchart PNG overlays for network planning.

- Port Mapper supports switch selection for NVIDIA/Mellanox, Cisco, and Arista, includes cell planning, per-rack bandwidth validation, JSON import/export, and can generate legacy install commands.

- Port Mapper handles Cisco ASIC slice balancing and Arista physical port ordering.

- Port Mapper does not support IPv6 as of 2025-10-30.

- Port Mapper auto-config generation depends on VPN connectivity to enforce the latest switch configuration templates; offline usage requires manual steps.

- SEs were reminded not to plug clients into southbound switches and to use the networking field request process for architecture and design guidance.
