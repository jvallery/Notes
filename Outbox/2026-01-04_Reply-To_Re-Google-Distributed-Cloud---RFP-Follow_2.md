---
status: draft
type: email-draft
original: "2025-12-15_183201_0409_Re-Google-Distributed-Cloud---RFP-Follow-up3-Encryption-key-.md"
created: "2026-01-04T18:58:59.581736"
to: "alon@vastdata.com"
to_name: "Alon Horev"
subject: "Re: Re: Google Distributed Cloud - RFP Follow-up3) Encryption key granularity across S3, NFS, and block"
reason: "Contains question"
topics: ["Google Distributed Cloud", "RFP", "encryption key granularity", "self-encrypting drives", "FIPS certification", "S3", "NFS"]
people_mentioned: []
vault_context_used: True
---

# Draft Reply: Re: Google Distributed Cloud - RFP Follow-up3) Encryption key granularity across S3, NFS, and block

**To:** Alon Horev <alon@vastdata.com>
**Subject:** Re: Re: Google Distributed Cloud - RFP Follow-up3) Encryption key granularity across S3, NFS, and block
**Context:** Contains question

---

Hi Alon,

Thanks for redirecting me to Violet for these encryption queries. I'll coordinate with her to ensure we have detailed and accurate responses for Google. 

Tomer's insights were helpful, especially regarding our software-based approach to encryption and the path-level key management capabilities. I’ll follow up with Violet to confirm any specifics about the self-encrypting drives and to clarify the SSE-C support details, particularly any nuances since version 5.4.

For your question about the unique key per encrypted path, it seems our support for encryption groups allows for such granularity. I'll work with Violet to ensure this is accurately represented in our documentation and provide a comprehensive view of how buckets, paths, and views integrate with customer-managed keys. 

Let me know if there's anything else you need, and I'll keep you updated on any new information.

Best,  
Jason

---

## Original Email

> From: Alon Horev <alon@vastdata.com>
> Date: 2025-12-15


---

## Vault Context Used

<details>
<summary>Context from notes that informed this draft</summary>

## People Context

### Tomer Hagay
**Role**: Leads field request triage team at VAST Data (Tel Aviv team)
**Location**: Tel Aviv
**Relationship**: Internal collaborator (PM)

**Background**:
- PM perspective: very low PM-to-engineer ratio (~4 PMs / ~400 engineers); need Cloud Design Qualifiers; Slack support should not become backlog funnel; global namespace write leases preview in 5.5.
- Listed as a candidate for weekly/monthly 1:1 cadence.
- Tagged to help ask Shachar to confirm AI-first development mandate, training cadence, a

**Recent interactions:**
- 2025-10-01: Discussed FRD templates/examples and access to PM SFDC RFE/Feature dashboards and Jira links. [[2025-10-01 - FRD templates and access]]

- 2025-11-07: Discussed need for org-wide PM discipline (OKRs/KRs, epic-to-task traceability, RoB cadence) and plan to socialize a skunkworks proposal with leadership after Tel Aviv.

- 2025-10-29: PM-led cloud model alignment; agreed on PM-led cloud approach and FRD qualifiers checklist; follow-up planned for pricing + Salesforce walkthrough ([[2025-10-29 - PM-led cloud model alignment]])

- 2025-10-24: [[2025-10-24 - AI-first dev and cloud maturity]] (via VAST)

- 2025-10-28: [[2025-10-28 - GCP MVP launch alignment]] (via Google)

- 2025-10-01: [[Pricing vTeam action list]] (via Pricing)

### Jason Vallery
**Role**: Product management (cloud); partnerships with hyperscale cloud providers at VAST Data (Cloud / Partnerships)
**Location**: Colorado (near Boulder)
**Relationship**: Internal collaborator

**Background**:
- Coordinated Microsoft-related collateral and validations (ROI data usage, BizDev education/intros, power-savings one-pager, marketplace offer assessment).
- Internal collaborator coordinating partner/customer requirements and meetings.
- Internal collaborator coordinating cloud/partn

**Recent interactions:**
- 2025-12-15: [[2025-12-15 - Google GDC RFP review]] (via Google)

- 2025-12-15: [[2025-12-15 - Microsoft MAI strategy and next steps]] (via Mic

</details>
