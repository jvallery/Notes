# Re: Google Distributed Cloud - RFP Follow-up3) Encryption key granularity across S3, NFS, and block

- Exported: 2025-12-16 10:37:25
- Messages: 2
---

## 2025-12-15 17:47:47 — Alon Horev <alon@vastdata.com>
**Subject:** Re: Google Distributed Cloud - RFP Follow-up3) Encryption key granularity across S3, NFS, and block

> You should be working with Violet on these matters.
> 
> On Mon, Dec 15, 2025 at 7:27 PM Jason Vallery <jason.vallery@vastdata.com> wrote:
> Hi Alon/Tomer —
> 
> We had a walk through call of the RFP with Google today and a few follow-up questions came up which I could use your help answering:
> 
> 1) Do we have a FIPS-certified QLC option? Specifically, they are looking for self-encrypting drives. Have we ever validated any specific drives?
> 2) Broadly, does our software stack have the ability to work with self-encrypting drives? Can we do key management, etc?
> 3) Do we have a good doc which walks through encryption key granularity across S3 and NFS?
> 
> A few points to verify --
> 
> Customer Managed Keys can be configured as “Encryption Groups” aligned to the tenant level
> Encrypted Paths provide a new encryption group applied to a sub-directory within a tenant.  
> Can we have a unique key per encrypted path? That isn’t clear to me from the support doc Managing Encrypted Paths
> We do support S3 Server-Side Encryption with Customer-Provided Keys (SSE-C) via x-amz-server-side-encryption-customer-* headers? Any gotchas? 
> How do buckets, encrypted paths, and views all come together with customer managed keys and the associated policiy? Is there anything that describes how this works in a multi-tenant way? (E.g., S3 supports per-bucket and per-object level key references which can be specified at the time of the PUT).  
> 

---

## 2025-12-15 18:32:01 — Tomer Hagay <tomer.hagay@vastdata.com>
**Subject:** Re: Google Distributed Cloud - RFP Follow-up3) Encryption key granularity across S3, NFS, and block

> Violet is indeed the expert. Here are some answers in the meantime:
> 
> 1. SED - We do not want to be restricted by HW capabilities or availability, and therefore focus on software-based encryption that could also be FIPS certified.
> 3. Encryption keys are at the path or tenant level. "Path" includes any protocol, including S3 buckets and NFS exports. It's described here, under encryption groups: https://support.vastdata.com/s/document-item?utm_source=google.com&bundleId=vast-cluster-administrator-s-guide5.3&topicId=managing-data/encryption-of-data-at-rest/managing-encryption-groups-and-keys.html&_LANG=enus
> Re:SEDs in general - do you know where the requirement comes from? If SEDs are used to meet FIPS 140-3 data at rest encryption to protect against drive removal, VAST SW that uses the same FIPS-compatible encryption algorithms should meet that requirement.
> 
> - An encryption group can be assigned to a path to support having a unique key for that path.
> - SSE-C - What do you mean by gochas? We do support the x-amz-server-side-encryption-customer-* headers starting from 5.4. covered in the release notes: https://support.vastdata.com/s/document-item?bundleId=vast-cluster-5.4-release-notes&topicId=vast-cluster-5-4-0-release-notes/new-features-in-5-4-0.html&_LANG=enus
> 
> Tomer
> 
> 
> 
> On Mon, Dec 15, 2025 at 6:47 PM Alon Horev <alon@vastdata.com> wrote:
> You should be working with Violet on these matters.
> 
> On Mon, Dec 15, 2025 at 7:27 PM Jason Vallery <jason.vallery@vastdata.com> wrote:
> Hi Alon/Tomer —
> 
> We had a walk through call of the RFP with Google today and a few follow-up questions came up which I could use your help answering:
> 
> 1) Do we have a FIPS-certified QLC option? Specifically, they are looking for self-encrypting drives. Have we ever validated any specific drives?
> 2) Broadly, does our software stack have the ability to work with self-encrypting drives? Can we do key management, etc?
> 3) Do we have a good doc which walks through encryption key granularity across S3 and NFS?
> 
> A few points to verify --
> 
> Customer Managed Keys can be configured as “Encryption Groups” aligned to the tenant level
> Encrypted Paths provide a new encryption group applied to a sub-directory within a tenant.  
> Can we have a unique key per encrypted path? That isn’t clear to me from the support doc Managing Encrypted Paths
> We do support S3 Server-Side Encryption with Customer-Provided Keys (SSE-C) via x-amz-server-side-encryption-customer-* headers? Any gotchas? 
> How do buckets, encrypted paths, and views all come together with customer managed keys and the associated policiy? Is there anything that describes how this works in a multi-tenant way? (E.g., S3 supports per-bucket and per-object level key references which can be specified at the time of the PUT).  
> 

---

