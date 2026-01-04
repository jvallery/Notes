---
type: "1-1"
created: { { DATE } }
status: "done"
counterpart: "[[Erez Zilber]]"
role: ""
team: ""
company: ""
series: "1-1/Erez Zilber"
cadence: "Weekly"
meeting_mode: "Video"
location_or_link: ""
calendar_url: ""
start_time: ""
duration_min: "30"
privacy: "internal"
ai_extracted: true
transcript_path: "00 Inbox/Transcripts/20251028 0901 Parallels Transcription.txt"
tags: [meeting, "1-1"]
---

# 1:1 — Erez Zilber — 2025-10-28

> [!info] Purpose
> Build trust, surface and remove blockers, align on priorities, coach & grow.

## Summary

Jason and Erez aligned on delivering Azure Blob API support in VAST to enable Azure marketplace use and OpenAI scenarios. Priorities include managed identities via Entra ID, JWT validation with key caching/rotation to survive network outages (72–96 hours), and mapping Blob RBAC/ABAC to VAST bucket policies. Key Blob features of interest are Append Blob and PutBlobFromURL. They will plan a POC with OpenAI to validate offline operation and schedule in-person working sessions in Tel Aviv the week of Nov 23.

## Key facts learned

- Erez is VAST protocols architect (8+ years) leading field-driven protocol requirements.
- Jason joined VAST last week; deep object storage and protocol background from Microsoft.
- VAST aims to offer Azure Blob API for Azure marketplace and customers beyond OpenAI.
- OpenAI uses GPU-adjacent storage with network autarky requirements (72–96 hours).
- OpenAI disables account key auth; uses Entra ID managed identities with JWT bearer tokens.
- JWT validation must work offline via cached public keys and accommodate key rotation.
- Each GPU cluster has its own service principal to scope data access.
- Desired Blob features include Append Blob and PutBlobFromURL for service-to-service copy.
- VAST prefers mapping Blob RBAC/ABAC to existing identity and bucket policies across protocols.
- Planned POC will simulate network isolation to verify uninterrupted operation.

## Outcomes

- Alignment to support Azure Blob API with focus on Append Blob and PutBlobFromURL.
- Agreement to use Entra ID managed identities and JWT-based auth (no account keys for OpenAI).
- Agreement to map Blob RBAC/ABAC semantics to VAST identity and bucket policies.
- Plan to validate offline token verification via cached Entra ID keys and rotation handling.
- In-person sessions planned in Tel Aviv week of Nov 23 for deeper design/knowledge sharing.

## Decisions

- Use Entra ID managed identities with JWT-based auth for OpenAI scenarios (no account keys).
- Proceed with RBAC/ABAC-to-bucket-policy mapping for Blob authorization in VAST.

## Action items (for Erez Zilber)

- [x] Send reading material on Azure Instance Metadata Service and Managed Identities, and relevant Entra ID/MS Graph docs. @Jason Vallery ⏫ ✅ 2025-11-08
- [x] Draft FRD for Blob API support covering auth model, RBAC/ABAC mapping, Append Blob and PutBlobFromURL, and offline token validation. @Erez Zilber 🔺 ✅ 2025-11-08
- [x] Design JWT verification and key caching/rotation strategy to operate 72–96 hours without IdP connectivity. @VAST Protocols team ⏫ ✅ 2025-11-08
- [x] Define authorization mapping from Blob RBAC/ABAC to VAST identity and bucket policies across protocols. @VAST Protocols team 🔼 ✅ 2025-11-08
- [x] Coordinate POC plan with OpenAI, including a simulated network isolation test. @Jason Vallery ⏫ ✅ 2025-11-08
- [x] Schedule and send calendar invites for Tel Aviv face-to-face sessions (Nov 23–26). @Erez Zilber 🔼 ✅ 2025-11-08
- [x] Prepare agenda and session plan for Tel Aviv visit and knowledge sharing. @Jason Vallery 🔼 ✅ 2025-11-08

## Follow-ups

- [x] Confirm exact dates/times for Tel Aviv meetings the week of 2025-11-23. @Jason Vallery 🔼 ✅ 2025-11-08
- [x] Set a follow-up design review after Erez returns mid-November. @Erez Zilber 🔼 ✅ 2025-11-08
- [x] Validate exact Blob feature set required by OpenAI beyond Append Blob and PutBlobFromURL. @Jason Vallery ⏫ ✅ 2025-10-28
- [x] Decide on scope for legacy account key support (if any) and constraints. @VAST Engineering 🔼 ✅ 2025-11-08

## Risks

- Failure to meet network autarky if JWT expiry or key rotation handling is insufficient.
- Complexity and lead time to implement native Entra ID (MS Graph) user/group integration.
- Azure-specific managed identity patterns may be harder to replicate in non-Azure GPU facilities.
- Divergence between Blob and S3 semantics increases implementation surface and testing burden.
- OpenAI relies on extended token cache behaviors not generally public in Azure, which VAST must replicate.

## Open questions

- What is the minimum viable Blob feature set for the Azure marketplace offering and for OpenAI beyond Append Blob and PutBlobFromURL?
- What JWT expiry and key-cache TTL policies are required to guarantee 72–96 hours of offline operation?
- How will managed identity scenarios be handled in non-Azure GPU facilities (e.g., CoreWeave)?
- Which exact RBAC/ABAC roles and scopes must be supported and how do they map to VAST bucket policies?
- Should VAST integrate with MS Graph directly for Entra ID users/groups, and what objects/claims are needed?
- Are there any Azure-only token caching behaviors OpenAI depends on that VAST must replicate explicitly?

> Next meeting (if any): 2025-11-23

---

<!-- ai:transcript:start -->

## Transcript (auto)

```text
[00:00:00.40]   RemoteFine, yes.

[00:00:02.02]  Jason ValleryNice to meet you.

[00:00:04.25]   RemoteYeah, you too. When did you join?

[00:00:07.00]  Jason ValleryJust over a week ago, last Monday was my first day. So, I'm still learning the ropes around here, meeting folks, and yeah, all that good stuff. Maybe we should do a formal interview. Tell me a little bit more about your role in VAST. you know, can answer any questions about mine.

[00:00:24.82]   Remote- Yeah, sure. So I'm protocols architect at Fast. Joined like eight plus years ago and led the protocols activity, and during the last three, four years, technical side, trying to understand the requirements from the field, digesting it so that engineering can implement new features.

[00:01:01.31]  Jason ValleryWell, I think we're going to become great friends because I have a lot of opinion about protocols. So, I don't know what you know about me, so Jason Valerie, I just joined from Microsoft. You know, I spent the first 10 years of my career in software development, so I'm a very technical product manager, hands-on kind of guy. I really like to get into the weeds, so that's why I have opinions about protocols, I suppose. Last 13 years at Microsoft in the object storage team. know, I was in the leadership at the conclusion of my journey at Microsoft, but over my time there in those 13 years, I owned from a product management lens, APIs, SDKs, client tools, multi-protocol access, tiering, pricing, customer engagement. I've worked in the weeds with all of Microsoft's top customers, including OpeningEye, and I've seen all the scenarios that have been the cloud, a deep understanding of the blob API, the S3 API, NFS as a protocol, and iSCSI, and probably a whole bunch of other storage protocols that I'm not

[00:02:02.13]   RemoteThinking about. So that's me. Okay, so Alon told me that you may have some understanding about how OpenAI want to use the VaST as a blob storage server. I started I know a bit about S3 and now I started reading about the blob storage try to summarize what I know already know. in a conference page and I'm trying to understand how we can map OpenAI's requirements on VAST.

[00:02:50.46]  Jason ValleryWell, so a couple things. I think it's broader than just opening up. You know, we're doing a major push here at VAST towards the cloud, as I'm sure you're aware. When we get to a full-blown Azure deployment, other customers will want a Blob API beyond just OpenAI. OpenAI, obviously, they do heavily leverage the Blob API, just given that they were born on Azure. I will tell you, the first mistake that Microsoft made and that I this battle the entire time I was there was not to just to just adopt the S3 API. The blob API itself is a bizarre thing in that Microsoft is the only provider that actually supports it and Microsoft doesn't support the S3 API which every other hyperscaler, every other on-prem storage vendor, you know everyone who's doing object storage supports S3. So it's a big miss on Microsoft's for a variety of institutional reasons behind that. We don't have to get into them. But the idea behind the Blob API is that it generally has parity in terms of features and functions with the S3 API, it's just a different shape. There are a few exceptions, and we can kind of dig into those exceptions as necessary. But, generally speaking. API doesn't even really use them. The one that I think stands, or I guess there's two that stand out, but they're less API but more capability. The Appendable API, they do use this. Not a lot, so it's not like a major scenario and use case for them, and then there's a key API that is unique in the public cloud which I'm going to push really hard for us to deliver on, called PutBlobFromURL, which allows service-to-service data

[00:04:36.95]   RemoteMovement.

[00:04:37.77]  Jason ValleryThose two APIs in the Blob Surface, I think, are the ones that are most interesting to OpenAI. But more broadly speaking, the whole semantics around the Blob API and so forth, we'll likely just want to support for our Marketplace offer because what that enables is once we get to an Azure deployment, any of the Microsoft first-party services that integrate with the data layer could then just directly connect to Blob or to our Blob API without the necessity of them supporting some intermediary. So that's kind of the bigger picture. I don't know, I can talk about opening eyes. workloads, if that's useful, and how they think about object more generally. What would be the best topic for me to start with?

[00:05:25.33]   Remote- I'm trying to understand which blob features we will need to implement. I can say that-- I don't want to add another permission model and since Blob Storage doesn't have ACLs, they have roles which we can more or less map to S3 identity and bucket. policies and since we support identity and bucket policies for all protocols, I mean, also for NFS and SMB, I don't see a reason why we wouldn't do that also for blob storage.

[00:06:16.58]  Jason Vallery- One of the, so I--

[00:06:20.32]   Remote- What's your opinion about it?

[00:06:22.61]  Jason ValleryOne of the, so GloB supports a couple of different ACL models, authorization models. There's role-based attribute control, or access control. There's a, sorry, there's a role-based access control and an attribute-based access control. I think both of those are interesting models. I think they generally can be mapped to. bucket policies. The one thing that gets interesting for OpenAI, and this is actually, I don't know how deep you are on the authentication authorization layer, but one of the big use cases that OpenAI have for VAST is to provide what they refer to as GPU adjacent storage. We could get in kind of weeds, but the way they do it... think about capacity and storage today is that they have central data lakes in Azure and these are like there's three key Azure regions where OpenAI have literally many exabytes of blob capacity for the sort of authoritative central copy of their important data assets and those Azure regions don't even necessarily have GPUs. more CPU workloads sitting there for like analytics, Databricks, Sparks, data processing pipelines. Those all sit up in these big Azure Qo regions, and then OpenAI get GPUs all over the planet. So they have 50 something Azure regions that have GPUs in them. You know, obviously they're getting GPUs in CoreWeave and now other third parties, Oracle, et cetera, and so where they get those GPUs around the planet, these are typically very like purpose-built data centers that only have GPUs in them for doing training and processing. Now, the key scenario where storage comes into play and where vast opportunity is, is in those facilities, imagine this is a CoreWeave facility with 8,000 GPUs in it. it. They want a small amount of storage, and when I say small amount I mean like a couple hundred terabytes, that they can stage checkpoints on and stage training data, and most importantly, and this is where the network authentication security controls come into play, they want the ability for that entire data set to survive a network outage, they call it a network auto. Where those GPUs, like some idiot with a backhoe, digs up a fiber path from this random CoreWeave facility in the middle of nowhere, or random whatever provider facility in the middle of nowhere, and now that entire site has no network connectivity. The most important thing for them is that those GPUs don't become hybrid, and if they're running a training job, and they still have local adjacent storage, they can still checkpoint, they can still read the training data, and they can survive some amount of time. So, why this matters. If we're doing bearer-based token authentication, and we're using cloud-based identities, role-based access control, bucket policies, how long do they last? those tokens last? How do permissions get validated? When does expiry happen? What is the outage case? When does the whole thing fall apart? And so Microsoft did this for them and put in a whole bunch of cash expiry policies, then extended them and made them configurable for OpenAI. These are features that aren't even public in Azure to make sure. that in that case where those 8,000 12,000 GPUs have no network connectivity to the internet and therefore no network connectivity to the token issuer, that tokens continue to be accepted. So how that all layers together is an important point. Important point two is that each one of these islands of GPU capacity in their world has a service principle associated with it, such that they can apply different policies to each one of these compute clusters and then they can layer that into their central storage and say like this cluster has this principle and then it can access this subset of the data for its job to hydrate and copy local. So all of these like nested groups of principles end up being an important component of how they layer all their security controls together, and then again, those things have to be cached and those things have to survive a network outage for 72, 96 hours kind of timeframe while connectivity is restored. That's generally their security cluster.

[00:10:52.69]   RemoteOkay, so what I read is that the Azure support, you can authenticate with a JWT but of course

[00:11:24.17]  Jason ValleryToken can expire yes um but to be clear like in order to have all of those um groups in because it's all backed by microsoft's intra id which is formally known as azure active directory like you define all these compute groups within there microsoft has something um called a managed service identity and AWS has this, others have it, but what that looks like is you've got a process running on a compute host in Azure, and in this case this would be a GPU node, that process can query a non-routable IP address, it's like a 169 IP address, that then connects to process running on the hypervisor of that host that is called the instance metadata server. That instance metadata server can issue a bearer token that says I'm a trusted process running on a trusted host within the Azure Enclave and then they can use that token to authenticate to storage. through a bearer token that has that end-to-end Azure trust implicitly because it's all running on Azure infrastructure, and that, my entire point is that enclave needs to work even when it's disconnected from the central Internet ID system through token caching, and so what that practically means is VaST running in one of these facilities will have to validate those tokens and cache them against EntraID for a timeout period to continue to work. Account key-based authentication is disabled across the world. I think we'll have to support it just for legacy customers, but OpenAI doesn't use account key-based authentication. It all is tied back into this secure enclave.

[00:13:07.73]   RemoteToken lock so that I are using a barrier token yeah they don't use account keys

[00:13:16.97]  Jason ValleryBecause they're not secure like you can't really secure an account key you can't force expiry you can't type after the instance yeah you can't apply role based access control to it so all of those capabilities are super important

[00:13:28.41]   Remoteso you could say that this is more or less equivalent to a STS yeah it is an STS and that's why

[00:13:39.79]  Jason ValleryLike the the off-blow there requires the consumer of the token to validate it against the token issuer and again the token issuer is the chain root of trust from the compute back to Intra-ID and that's why like the implementation here matters in that if you're trying to validate those tokens real-time against Intra-ID and VaST can't talk to Intra like the whole thing breaks when there's

[00:14:09.70]   Remotea network outage. - Wait, with JWT, you don't need to talk to Entry ID as long as you cache the public keys.

[00:14:25.09]  Jason Vallery- Right, so how long those public keys cache and then the expiry of the token that, because there's a claim within the JWT that say like how long it's good for, and so when it's created, it has to have an expiry. like well out into the future, and then the cash public keys, how long those are revalidated, or how often those

[00:14:44.36]   RemoteAre revalidated, becomes kind of the constraint. Yeah, but with EnterIT, you can have more than one public key. previous, current, and next keys, and with SDS, we cache them, and then we can validate the JWT against any of those public keys. So I guess that even during a network outage, and even if keys were rotated, we should be good. and we don't need to talk to the OIDC provider.

[00:15:26.95]  Jason Vallery- Okay.

[00:15:27.67]   Remote- Yeah, so this is what we did with FTS today.

[00:15:31.65]  Jason Vallery- That is one of the, so we're talking about doing a POC with them, and this is one of the things they will validate. They will want to simulate network autarky and ensure that BAST continues to function. and that there's no interruptions in the service when we are isolated from any internet connected.

[00:15:51.51]   RemoteOkay. Okay, I think we need to spend... I have like three minutes before I have to go. I think we need to spend some time talking about users and groups in EnterID. I will say that we want to add support for... Today we support Active Directory. We held up, we want to add support for Enter ID. I understand that most customers don't want to use ADDDS and we need to support, we need to have native support of Enter ID with, I think it's called Graph API, and this is something we want to do so that we can fetch users and groups from Entrity. If you have some reading material that I can use, that would be helpful. as we try to build an FRD for a Blobstart support.

[00:17:20.19]  Jason Vallery- Yeah, so what I would recommend starting point is an understanding of the instance metadata server service as it relates to the compute hosts in Azure and then how that translates to managed identities and managed machine identities, because ultimately that is how they... organize their groups and organize all their resources and then what happens is that like there's an intrinsic trust between a given compute cluster and a given storage resource in the blob API that then does not require them to manage any tokens or credentials like the underlying plumbing handles that in the end because of those two different trusts against

[00:18:02.17]   RemoteOkay, so I will go over that and I guess I will set a follow-up meeting with you. This will take a while because I'm going on vacation tomorrow evening and we'll be back around mid-November.

[00:18:23.20]  Jason ValleryWhere are you based? Are you in Tel Aviv?

[00:18:26.41]   RemoteYes.

[00:18:26.91]  Jason ValleryI'm gonna come to Tel Aviv. We should meet up face to face. I'm still kind of working through the calendar, but the week of the 24th, so the 23rd through the 26th, I'll come visit you, and we should find some time face to face.

[00:18:38.07]   RemoteNovember?

[00:18:38.82]  Jason ValleryYeah, November 23rd through 26th. Are you around?

[00:18:40.82]   RemoteYes, yes. This is one week after I'm from vacation great can you put something in the calendar yeah I'm gonna

[00:18:56.05]  Jason VallerySort that whole week I think we're gonna come up with an agenda and there'll probably be a few different sessions I can invite you to where we'll do some knowledge sharing as well

[00:19:07.83]   RemoteActually let me put let me put something in the calendar before I forget so the week of the 23rd yes okay okay I will send something Okay, thanks a lot. I need to go. It's been very helpful.

[00:19:34.94]  Jason ValleryPleasure meeting you. Looking forward to it. Good luck.

[00:19:37.73]   RemoteThank you. Yeah, good luck. Thank you. Bye. Bye-bye.
```

<!-- ai:transcript:end -->
