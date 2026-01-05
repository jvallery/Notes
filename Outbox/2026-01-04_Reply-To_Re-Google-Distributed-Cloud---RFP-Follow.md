---
status: draft
type: email-draft
original: "2025-12-15_183201_0409_Re-Google-Distributed-Cloud---RFP-Follow-up3-Encryption-key-.md"
created: "2026-01-04T21:05:50.989386"
to: "alon@vastdata.com"
to_name: "Alon Horev"
subject: "Re: Google Distributed Cloud - RFP Follow-up on Encryption Key Granularity"
reason: "Contains question"
topics: ["Google Distributed Cloud", "RFP", "encryption key granularity", "self-encrypting drives", "FIPS certification", "S3", "NFS"]
people_mentioned: []
vault_context_used: True
recipient_type: "technical_team"
urgency: "medium"
stakes: "medium"
---

# Draft Reply: Re: Google Distributed Cloud - RFP Follow-up3) Encryption key granularity across S3, NFS, and block

**To:** Alon Horev <alon@vastdata.com>
**Subject:** Re: Google Distributed Cloud - RFP Follow-up on Encryption Key Granularity
**Context:** Contains question
**Classification:** technical_team | urgency: medium | stakes: medium

---

Hi Alon and Tomer,

Thanks for your insights on the RFP follow-up questions. Here's a consolidated response to the queries we received from Google:

1. **FIPS-certified QLC Option**: As Tomer mentioned, we focus on software-based encryption, which aligns with FIPS certification requirements. This approach ensures flexibility and independence from hardware constraints, which is important for meeting the needs of Google’s Distributed Cloud.

2. **Software Stack Compatibility with SEDs**: While our primary strategy is software-based, our software stack can indeed work with self-encrypting drives. Key management capabilities are built into our stack, offering robust encryption solutions that are competitive with hardware-based options.

3. **Encryption Key Granularity Documentation**: We provide encryption at both the path and tenant levels across all protocols, including S3 and NFS. This setup supports having unique encryption keys per path, enhancing security and flexibility. For further details, the documentation linked by Tomer is comprehensive and should cover most of Google's needs.

4. **Unique Key per Encrypted Path**: Yes, an encryption group can indeed be assigned to a path, allowing for unique keys. This is a key feature that supports advanced security configurations.

5. **S3 Server-Side Encryption with Customer-Provided Keys (SSE-C)**: We support the x-amz-server-side-encryption-customer-* headers starting from version 5.4, as detailed in our release notes. This capability ensures compatibility with customer-managed keys for S3.

6. **Integration of Buckets, Paths, and Views with Customer Managed Keys**: Our system is designed to handle multi-tenant scenarios with policies that integrate buckets, encrypted paths, and views effectively. This is detailed in the linked support documents, which should be referenced in any proposals or discussions with Google.

**Next Steps**:
- **Violet's Expertise**: I'll coordinate with Violet to ensure any further technical clarifications are addressed. She can provide deeper insights if any specific technical details need further exploration.

- **Documentation and Support**: I will review the current support documents to ensure they are up-to-date and reflective of our capabilities as per Google's requirements. I will aim to have this review completed by next Tuesday, December 19th.

Please let me know if there are additional areas where we can provide further clarity or support. Looping in Violet for her expert input seems prudent given the technical depth of these questions.

Best,
Jason

---

## AI Reasoning

> The strategy is to provide comprehensive answers to Google's queries while leveraging internal expertise, specifically Violet, for any deeper technical clarifications required. This ensures we present a unified and competent front in response to the RFP follow-up.

## Action Items (Extracted)

- [ ] Coordinate with Violet for further technical clarifications @me 📅 2025-12-19
- [ ] Review support documents to ensure alignment with Google's requirements @me 📅 2025-12-19

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
*Path: VAST/People/Tomer Hagay/README.md*

#### Full Profile (README.md)
```markdown
---
type: people
title: Tomer Hagay
last_contact: '2025-10-01'
created: '2026-01-03'
tags:
- type/people
- generated
email: tomer.hagay@vastdata.com
company: VAST Data
---

# Tomer Hagay

## Profile

**Role**: Leads field request triage team at VAST Data (Tel Aviv team)
**Location**: Tel Aviv
**Relationship**: Internal collaborator (PM)

**Background**:
- PM perspective: very low PM-to-engineer ratio (~4 PMs / ~400 engineers); need Cloud Design Qualifiers; Slack support should not become backlog funnel; global namespace write leases preview in 5.5.
- Listed as a candidate for weekly/monthly 1:1 cadence.
- Tagged to help ask Shachar to confirm AI-first development mandate, training cadence, and measurable adoption targets.

## Open Tasks

```tasks
path includes Tomer Hagay
not done
```

## Recent Context

- 2025-10-01: Discussed FRD templates/examples and access to PM SFDC RFE/Feature dashboards and Jira links. [[2025-10-01 - FRD templates and access]]

- 2025-11-07: Discussed need for org-wide PM discipline (OKRs/KRs, epic-to-task traceability, RoB cadence) and plan to socialize a skunkworks proposal with leadership after Tel Aviv.

- 2025-10-29: PM-led cloud model alignment; agreed on PM-led cloud approach and FRD qualifiers checklist; follow-up planned for pricing + Salesforce walkthrough ([[2025-10-29 - PM-led cloud model alignment]])

- 2025-10-24: [[2025-10-24 - AI-first dev and cloud maturity]] (via VAST)

- 2025-10-28: [[2025-10-28 - GCP MVP launch alignment]] (via Google)

- 2025-10-01: [[Pricing vTeam action list]] (via Pricing)
## Key Facts

## Topics

- RFE
- NVIDIA Corporation
- DGX Cloud
- VAST Data
- cluster visibility

- Google Distributed Cloud
- RFP
- encryption key granularity
- self-encrypting drives
- FIPS certification
## Key Decisions

## Related Customers

## Related Projects

## Related

<!-- Wikilinks to related entities --

</details>
