---
status: draft
type: email-draft
original: "2025-12-15_183201_0409_Re-Google-Distributed-Cloud---RFP-Follow-up3-Encryption-key-.md"
created: "2026-01-04T18:33:53.034846"
to: "alon@vastdata.com"
to_name: "Alon Horev"
subject: "Re: Re: Google Distributed Cloud - RFP Follow-up3) Encryption key granularity across S3, NFS, and block"
reason: "Contains question"
topics: ["Google Distributed Cloud RFP", "Encryption key granularity", "FIPS-certified QLC option", "Self-encrypting drives", "Software stack compatibility with self-encrypting drives", "Customer Managed Keys", "S3 Server-Side Encryption with Customer-Provided Keys (SSE-C)"]
people_mentioned: ["Alon Horev", "Jason Vallery", "Tomer Hagay", "Violet"]
vault_context_used: True
---

# Draft Reply: Re: Google Distributed Cloud - RFP Follow-up3) Encryption key granularity across S3, NFS, and block

**To:** Alon Horev <alon@vastdata.com>
**Subject:** Re: Re: Google Distributed Cloud - RFP Follow-up3) Encryption key granularity across S3, NFS, and block
**Context:** Contains question

---

Hi Alon,

Thanks for pointing me towards Violet for expertise on these matters. I'll coordinate with her to ensure we address the nuances of encryption key management effectively.

In the meantime, Tomer has provided valuable insights, which I'll build upon. It seems our approach to encryption prioritizes software-based methods that meet FIPS standards, which aligns with our strategy to avoid hardware limitations. I'll work on clarifying the specific requirements for FIPS-certified self-encrypting drives and how our current capabilities match these needs.

Regarding the documentation on encryption key granularity across S3 and NFS, I'll review the resources Tomer mentioned to ensure they cover all aspects of our multi-tenant setup, especially the integration of buckets, paths, and views with customer-managed keys.

Lastly, I'll confirm our support for S3 Server-Side Encryption with Customer-Provided Keys (SSE-C) and identify any potential issues, as Tomer indicated this support was introduced in version 5.4.

I'll follow up with Violet and consolidate these points into a comprehensive response for our RFP requirements with Google.

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
