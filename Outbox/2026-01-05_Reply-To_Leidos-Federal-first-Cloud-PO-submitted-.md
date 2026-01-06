---
type: draft-reply
status: pending
created: "2026-01-05T19:52:39.381645"
urgency: "normal"
to: "Jeff Denworth <jeff@vastdata.com>"
subject: "Re: Leidos Federal first Cloud PO submitted (FOpp-4197, $96,808.14) and request to track customer expectations"
source_file: "/Users/jason.vallery/Documents/Notes/Sources/Email/2025/2025-12-30_162801_0557_Re-Re-EXTERNAL-EXTERNAL-Re-OA-Alert-FOpp-4197---9680814---A-.md"
ai_model: "gpt-5.2"
ai_temperature: 0.3
prompt_file: "Outbox/_prompts/2026-01-05_Reply-To_Leidos-Federal-first-Cloud-PO-submitted-.prompt.json"
---

# Draft Reply to Jeff Denworth

**Regarding**: Leidos Federal first Cloud PO submitted (FOpp-4197, $96,808.14) and request to track customer expectations
**Urgency**: normal

---

## Key Points to Address

Acknowledge Jeff Denworth's request to track Cloud POs. Confirm you will capture Leidos Federal FOpp-4197 details (software-only GovCloud deployment, on-prem connectivity for resilient demo) and propose a lightweight tracking mechanism (owner, customer expectations, UX feedback, product gaps, BD learnings). Ask for any specific format or stakeholders Jeff wants included.

---

## Draft Response

Hi Jeff,

Bottom line, I agree we should treat every Cloud PO like a product signal and track it end-to-end. I will start with Leidos Federal FOpp-4197 and stand up a lightweight tracker so we capture expectations, UX, gaps, and BD learnings in a consistent way.

For FOpp-4197, what I have so far is:
- Leidos Federal, “Leidos DoD Cloud,” FOpp-4197, $96,808.14
- GovCloud deployment, software-only
- Intended to connect to the on-prem system to support a resilient “Golden Dome” demo narrative (hybrid, comms disruption tolerance, “submarine mentality”)

Two quick clarifications I will confirm and then log:
- HW component: Greg’s note says SW-only, but I will validate there is no hidden infra dependency (BYO compute/storage assumptions, networking, interconnect, etc.) and close that loop by EOD Wednesday, January 7.
- Success criteria: I will get the specific “Golden Dome” expectations documented (RPO/RTO targets, replication/mesh topology, identity/ABAC requirements, audit/compliance constraints, and any disconnected or degraded-mode expectations) and have a first pass written up by Friday, January 9.

Tracking mechanism I will put in place this week:
- A single shared Cloud PO tracker with one row per PO and these fields:
  - Customer, segment, CSP and region, offer type (marketplace/private offer/direct), SW-only vs bundled, and target architecture (cloud-only vs hybrid)
  - “Definition of done” from the customer, including SLOs and operational expectations
  - Day-0 to day-2 experience notes (procurement, entitlement, install, onboarding)
  - Product gaps and asks (ranked by severity and revenue impact)
  - BD outcomes (reference potential, expansion path, partner motion, next deal)
  - Named internal owner for follow-through (PM plus field counterpart)

If you want this to be more than a tracker, I can also run a 20-minute monthly review starting Thursday, January 15 at 10:00am PT with you, Jenn, and the deal owner(s) to keep it tight and action-oriented.

Tell me who you want included on visibility for this (Gaston, Tiffany, Jenn, Greg, Lior, others), and whether you prefer the tracker to live in Salesforce as a report/dashboard or as a simple shared sheet with a weekly digest email.

Thanks,  
Jason Vallery  
VP, Product Management, Cloud  
VAST Data

---

## Original Summary

Jeff Denworth forwarded an OrderAdmin alert thread indicating VAST's first US Federal sector Cloud PO for Leidos Federal (FOpp-4197, $96,808.14) for a software-only deployment in Leidos GovCloud. Jeff Denworth asked Jason Vallery to ensure these Cloud POs are tracked to understand customer expectations, user experience, cloud product implications, and business development angles.

---

*This draft was auto-generated. Edit and send via your email client.*
