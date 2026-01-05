---
status: draft
type: email-draft
original: "2025-12-15_183201_0409_Re-Google-Distributed-Cloud---RFP-Follow-up3-Encryption-key-.md"
created: "2026-01-04T18:28:05.143646"
to: "alon@vastdata.com"
to_name: "Alon Horev"
subject: "Re: Re: Google Distributed Cloud - RFP Follow-up3) Encryption key granularity across S3, NFS, and block"
reason: "Contains question"
---

# Draft Reply: Re: Google Distributed Cloud - RFP Follow-up3) Encryption key granularity across S3, NFS, and block

**To:** Alon Horev <alon@vastdata.com>
**Subject:** Re: Re: Google Distributed Cloud - RFP Follow-up3) Encryption key granularity across S3, NFS, and block
**Context:** Contains question

---

Hi Alon,

Thanks for pointing me towards Violet. I've reached out to her for more detailed insights. In the meantime, here's a summary based on Tomer's input and additional findings:

1. **FIPS-certified QLC Option:** Our strategy leans towards software-based encryption which can achieve FIPS certification, rather than relying on hardware like self-encrypting drives (SEDs). This approach aligns with our aim to avoid hardware limitations.

2. **Software Stack and SEDs:** While we focus on software encryption, our stack is capable of integrating with self-encrypting drives for key management. I'll confirm the specifics of any prior validations with Violet.

3. **Encryption Key Granularity Documentation:** You can find a detailed explanation of encryption key granularity across S3 and NFS in our support documentation [here](https://support.vastdata.com/s/document-item?utm_source=google.com&bundleId=vast-cluster-administrator-s-guide5.3&topicId=managing-data/encryption-of-data-at-rest/managing-encryption-groups-and-keys.html&_LANG=enus). This includes how Customer Managed Keys and encryption groups function at the tenant and path levels.

For SSE-C support, we indeed support the x-amz-server-side-encryption-customer-* headers starting with version 5.4. For any further details, especially around multi-tenancy, I recommend discussing with Violet or checking the 5.4 release notes [here](https://support.vastdata.com/s/document-item?bundleId=vast-cluster-5.4-release-notes&topicId=vast-cluster-5-4-0-release-notes/new-features-in-5-4-0.html&_LANG=enus).

Let's coordinate a follow-up discussion with Violet to ensure all bases are covered. I'll keep you updated on my findings.

Best,  
Jason

---

## Original Email

> From: Alon Horev <alon@vastdata.com>
> Date: 2025-12-15

