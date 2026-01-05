---
type: "group-meeting"
created: { { DATE } }
title: "20251103 0731 Parallels Transcription"
participants: [{ { PARTICIPANTS } }]
ai_extracted: true
transcript_path: "00 Inbox/Transcripts/20251103 0731 Parallels Transcription.txt"
tags: [meeting, group]
---

# 20251103 0731 Parallels Transcription

**Date:** 2025-11-03  
**Participants:** Jason Vallery, Tomer, Adar, John

## Summary

Team reviewed how cloud clusters must map to Salesforce assets (Account/Site/PSNT) to enable call-home and Uplink. Agreed Phase 1 targets single-tenant per customer via private offers, with cluster-level call-home and manual/automated setup via Polaris/Tackle. Identified immediate need for a stop-gap manual flow and longer-term automation, plus attention to telemetry egress costs and data custody/legal constraints.

## Key facts learned

- Each VAST cluster has a single PSNT (serial-like ID) used to match against Salesforce.
- Call-home ('Godfather') operates at the cluster level; tenants are not aware of call-home.
- Uplink requires explicit registration with a unique customer subdomain and a matching Salesforce account.
- Unregistered clusters send no Uplink data; no orphan telemetry is ingested.
- On-prem process is heavy; cloud needs a lighter, automated onboarding path.
- Polaris is intended to deploy VAST on Cloud and can trigger onboarding/registration steps.
- Tackle is planned to integrate Salesforce private offers with deployment metadata/entitlements.
- Support bundles and telemetry create egress costs from the customer VPC; regular telemetry is small but non-zero.
- Support bundles could be collected on-demand to reduce egress; current bundles stored on GCS.
- Customers can access their Uplink portal via subdomain; Salesforce holds some Uplink data (e.g., cases).

## Outcomes

- Shared understanding of required Salesforce structure: Account -> Site (e.g., AWS region) -> Cluster asset with PSNT.
- Alignment that Phase 1 will be single-tenant per customer using private offers; cluster-level call-home only.
- Identified need for an immediate stop-gap manual onboarding/config process for upcoming field POCs.
- Confirmed that Uplink data flow requires prior registration and Salesforce linkage; no 'hello/adopt' path exists today.
- Acknowledged telemetry egress cost and legal/data-custodian considerations to be addressed in design.

## Decisions

- Phase 1 scope: single-tenant per customer deployments; no tenant-level call-home.
- No auto 'hello/adopt' endpoint for clusters at this time due to security concerns.
- Polaris will be the deployment mechanism and the hook point for future automation of registration.
- Cloud clusters must have Salesforce asset records with PSNT and an Uplink subdomain to enable support.

## Action items

- [x] Draft Phase 1 cloud onboarding process (SFDC Account/Site/PSNT, Uplink subdomain, Polaris/Terraform hooks) and circulate for review. @John ⏫ ✅ 2025-11-08
- [x] Define and publish a stop-gap manual flow for immediate field POCs to configure Salesforce assets and Uplink registration. @Jason Vallery ⏫ ✅ 2025-11-08
- [x] Prepare a reusable template/checklist to create Uplink subdomains and link them to Salesforce accounts/opportunities. @Adar 🔼 ✅ 2025-11-08
- [x] Specify Terraform/Polaris changes to auto-register clusters with Uplink (subdomain injected at deploy time). @John 🔼 ✅ 2025-11-08
- [x] Document PSNT-to-SFDC matching and Godfather handling, including required fields and error handling. @Tomer 🔼 ✅ 2025-11-08
- [x] Propose an approach to minimize telemetry egress (e.g., on-demand bundles, proxy via Polaris, S3 staging) with cost estimates. @Tomer 🔼 ✅ 2025-11-08

## Follow-ups

- [x] Decide workflow for public marketplace provisioning, including whether Tackle auto-creates Salesforce accounts/opportunities. @John ⏫ ✅ 2025-11-08
- [x] Run legal review of call-home/Uplink payload content and operator visibility for managed service data-custodian obligations. @VoC ⏫ ✅ 2025-11-08
- [x] Confirm and document policy on tenant-level opt-out in multi-tenant SaaS. @Jason Vallery 🔼 ✅ 2025-11-08
- [x] Evaluate feasibility and security posture of any future 'hello/adopt' endpoint for unregistered clusters. @Tomer 🔼 ✅ 2025-11-08
- [x] Audit existing VoC cloud customers for proper Salesforce and Uplink linkage; remediate gaps. @Adar ⏫ ✅ 2025-11-08
- [x] Select the preferred telemetry transport path (direct to GCS vs proxy via Polaris vs S3 staging) and define activation criteria for support bundles. @Tomer 🔼 ✅ 2025-11-08

## Risks

- Legal/data custodian and payload visibility constraints for managed service operations.
- Telemetry/support-bundle egress costs from customer VPCs.
- Public marketplace provisioning without auto-created Salesforce records could leave clusters untracked.
- Reliance on manual setup increases operational load and error risk (e.g., paging Adar).
- Potential rework if multi-tenancy needs are not considered in early design.
- Security risks if adopting unauthenticated auto-registration patterns.

## Open questions

- How will Salesforce accounts/opportunities be created for public marketplace sign-ups without prior rep engagement?
- What telemetry payload elements are permissible under managed service legal and privacy constraints?
- What exact Salesforce object model and fields (Account, Site, Asset, PSNT) will be standardized for cloud clusters?
- Should support bundles be strictly on-demand in cloud to control egress, and who triggers collection?
- Do we need any tenant-level controls or visibility in a future multi-tenant SaaS model, and how would opt-out be handled?

---

## Transcript (auto)

```text
[00:00:00.00]   Remote(mouse clicking)

[00:00:22.97]  Jason ValleryGood morning. Hi, John. Hello. I just joined last month.

[00:00:43.74]   RemoteThat's wild. Yeah, yeah, yeah, with the A-key. Yep, also we steam here in Iceland. Yeah. So, let's see. Adar accepted as well, so let's give him another minute.Pause for group work10 seconds pause I can... oh, AKE in the decline, okay. It's a short meeting. I'll start, and if Adar joins, he joins. So, there was this back and forth on Slack, and this is a topic that has been open for a while. I'll give some background, right? So the mode in which we're spinning up vast clusters obviously varies a lot between on-prem and cloud, right? So for on-prem clusters, we have to ship hardware, right? Someone has to install it. You know, there's a lot of people involved, right? There's a process for that, it's a POC or an actual deployment, it is very involving, and then that's very structured, documented, it's tracked in Salesforce, right? So there's a document we sign with the customer prior to let's say a POC, right? create a record in Salesforce for that customer, and that site, and that asset, right, or set of assets, right, that goes to the customer, they deploy it, or RFC deploys it, help them deploy it, doesn't matter, a partner, right? And then everything, there's the record for the whole thing, right? So when the cluster comes up and it calls home, it has an ID that we can match with Salesforce records, right? So our call home system knows how to go to Salesforce and get those IDs, right? So when it sees the cluster, and that's the part that Adar takes care of, right? So when a cluster comes online and calls home. send that ID and say okay that ID matches a record in in Salesforce and we know it's you know customer XYZ right and that's how call home presents it and all that if I believe and that's again a dark and confirm or not that if there is no match there is no way to to show a data in call home, right? It will just be ignored. So anyone that sends call home data to Vast without a matching record in Salesforce, that call home data is ignored or put in a bucket maybe that is not parsed or whatever. So we've been doing. a lot of, you know, there's been a lot of activity around cloud POCs, mainly POCs, or partners using Vast on Cloud for a while, right? For almost two years, sometimes for API development, sometimes for, you know, for all sorts of reasons, right? It's, you know, with, you know, incentives. instantiated many, many instances of VAST on AWS mainly, and for those, since none of them were, you know, production and paying customers and things we had to support and, you know, have actual VAST support involved in, we, we kept things simple. simple without taking care of the whole assets recording in Salesforce for every every time you know Parkin just wanted to spin up a vast own cloud and check an API call or something right that it was it was it it went against the motions we had to support and we we figured that once we we will have a process that is suitable for cloud because the on-prem process is too heavy, right? You can just go to the marketplace and spin up a cluster. It's not the same as actually shipping hardware, having, you know, customer sign that they are responsible for the hardware and everything, right? So totally different processes. That's where we are right now, and John, as I understand, you're building that onboarding and this whole, you know, this whole how do we charge, how do we sync records to Salesforce and all that? And so the long story, I just, you know, long story short, we just need to make sure that. there is an asset record for a vast on-cloud instance or cluster and and as long as you do that and there is a record for a customer so let's say you create a an account record in Salesforce that account account has a site which is, you know, AWS or AWS region, blah, blah, blah, and that site has, um, um, cluster records with that, what we call it PSNT. Have you heard that? Thank you. Bye bye. PSNT is that identifier. It's like a serial number, essentially. I can show you, but as long as it has PSNT, that PSNT record in SFDC, the cluster, when it comes up and calls home, it will send that PSNT ID, and that PSNT, as long as it matches Salesforce, we will know how to treat that call home data. So I'll pause here.

[00:07:38.79]  Jason ValleryLet me ask a few questions, Tomer. How does this work in CoreWeave, given the multi-tenancy dimension? Because one of the things we'll have to think about in the cloud is multi-tenancy, and so if we have multiple customer deployments logical cloud deployment eventually, how would we track them?

[00:07:56.63]   RemoteSo CoreWeave, or every vast cluster out there, has a single PSMT and it sends its entire call home data for all the tenants, if there's more than one. Entire call home data set is... sent for that cluster. On the receiving side, on the call home, what we call the godfather, right? That's the name for our call home infrastructure. We can parse based on tenants, or based on features, or based on whatever, right? But the entire data set for the cluster, the call home package, sent from the cluster. It's not done per tenant. The tenants are not aware that there's even call

[00:08:44.37]  Jason ValleryHome. They don't see the setting for that. Right. So I guess what I'm getting at is maybe there's a couple of different milestones we have to go through, but we'll likely need the ability to set this at the tenant level in a multi-tenant world where we go to... because well first of all I'm assuming we'll have multiple opportunities one for each potential customer in the cloud and Salesforce and those I'll have to map back. Let me ask another question before I get too far in the solution.

[00:09:12.71]   RemoteBut I wouldn't I I don't know but let me just just on that point I don't think we need to have call home per tenant. The call home the purpose of call home is to make sure the cluster is healthy and whoever manages the cluster what we call the super admin of the cluster is the the persona responsible for the cluster's health and that that is the persona that will turn on turn off um you know it will decide okay i want to get online support from vast for that cluster to serve the tenants that I onboarded with the SLA I wanted to serve. So the tenants don't know what Call Home is.

[00:09:57.67]  Jason Vallery- Do we allow customers to opt out or if they're deployed in maybe an Auburn environment?

[00:10:07.79]   RemoteWe do, yes, and that's what's, I mean, that's the situation in the cloud today, right? All the kind of custom cloud instances, right? I mean, they're kind of opt out even though we didn't really build the infrastructure to opt them in. Yeah. So there is, yeah.

[00:10:30.18]  Jason ValleryThere's another issue, so just to conclude this thought, is there a one to many opportunity with Salesforce, meaning one cluster connected to multiple Salesforce opportunities?

[00:10:43.66]   RemoteI would say, like, the project we were building on, with AWS, we were building on a lot of is having the Polaris platform. One of the responsibilities is being a deployment mechanism for Vaston Cloud. The tackle integration that we are talking about may be kicked off this discussion. planning to use Tackle as a way to integrate with Salesforce, and when you create a private offer for a customer, you do that through Salesforce, funnel it into Tackle, and we will kind of be, or all of us will be notified when that offer is accepted, and the initial Polar is to deploy one instance of Vaston Cloud per customer. This will allow us to have access to that metadata from Salesforce about the entitlement, for example, and control the size of the cluster for that customer.

[00:12:05.28]  Jason Vallery>> Yeah, I guess what I'm focusing on this so much is because the vision is multi-tenancy. I completely agree that the first phase of this is that single tenant per customer deployment. But if there's an opportunity for us to make sure we're not going out of path, we'll have to rework it. to get to multi-tenancy later. I'd like to avoid that. So I think you're completely right. In this first phase of what we're building, this isn't going to become an issue. Yeah.

[00:12:33.90]   RemoteSo are you, Jason, are you referring to a situation where we have a multi-tenant environment, you know, served with through a SaaS offering and a single tenant there will say I don't want to I want to opt out of call home for my space.

[00:12:54.69]  Jason ValleryExactly, either that or even just don't.

[00:12:56.89]   RemoteI don't, yeah, so I'll be, maybe I'm a bit naive but I don't think that could be an option because, because it's, it's, the call... whole capabilities is like you could say I'm opting out of AWS monitoring the instances in my AZ right you can't do that right I mean it's like you know you want to have your cluster healthy you want to get service from from your subscription yeah you know this is this is what it is right I mean

[00:13:32.19]  Jason ValleryIt's probably another topic to take in a different meaning, but I'm also a little worried about what payloads are there, because there's another conversation that got spun up around end user licensing. One of the things that we'll deal with in the cloud that we haven't dealt with on prem is this notion of data custodian. When we become a managed service and we are really responsible for customers data, we take on a lot of obligations legally, what kind of data we have access to, what our operations team can see, all of that gets

[00:14:06.36]   RemoteScrutinized with a different legal lens, and so I'm also thinking about that. Yeah, yeah, no, I agree, I mean a lot of it will make the call home argument kind of a mute point because we, you know, the idea behind call home to begin with is a cluster that VaST does not own, right, that that VaST needs to manage or needs to ensure it's it's uptime, ADAR. So, so if someone, if a, you know, customer A deploys a cluster and we want to ensure the cluster is running and notify them if they're the failed drive or whatever, we get the call home. But if that customer is actually us in a SaaS environment, we don't really need call home. We already are there actively monitoring that cluster, right? So, I mean, that will have so many other ramifications, but I'd say that, so although I worked John and Jason on the kind of the PSNT, right, the fact we have a record in NSFDC, the Godfather matches the PSNT with what comes from the cluster, right. right, as part of the call home bundle and all that. So, we're good there. Now, of course, there's the mechanics, Adar, that you are an expert for and how things work in SFDC and what records need to be there and everything. I mean, you're the expert for that. The last point I wanted to say before, Adar, I'll hand it to you, maybe. can add whatever you think is relevant is the fact that call home part of the fact that we didn't pursue turning it on and and you know fixing that those record matching and everything of course i mean we didn't have those in production that we had to get a sufficient bass support that's one is that there is work to do on the call home data regardless because it's in the cloud when you when you run vast cluster in your vpc those call home bundles sent to vast are considered to be egress data of your vpc and you know out of aws right and that's costly so our bundles are not that small and you know we're not very efficient on how we you know how we bundle those and how we you know whatever right so so another part of this is to make sure that it actually makes sense from a financial perspective. financial standpoint to to turn those on because there is a cost to the customer so that's that's it might be an option to send it proxy it through the Polaris platform we we do have we are monitoring the clusters right we have eight on needs of the nodes yes so that's there's multiple ways of solving this right I mean we could upload it to s3 on AWS and then take it from there there's other other ways right now it just goes a door we're storing everything on GCS right Yeah, the bundles are still in... Can you hear me? Yeah, it's kind of going in and out. Sorry about that. There's another option. You don't have to start off right away with the bundles. Uplink itself can send all the... the object states and the metrics, regardless, to enabling or debugging. But bundlers are good for us when we need to debug. There was a failure, when something went bad, and we need to fetch the logs right now. So in theory, we can take the approach of, we just get the regular uplink telemetry. right I was six states and metrics and then you get and you enable the support bundle collection and only let's say when support actually needs the log they can go and request the logs from the system and then pull the bundle yeah so I was referring to the bundled but but also regular call home telemetry is also So, you know, external, you know, egress, right? It's much smaller, but still. - Yeah, some network traffic has to go out of the, to get the data to us at this point, yes. Uplink updates are very small. very lightweight, we're talking about a few kilobytes every few seconds, and yes we need uplink today is hooked up to our salesforce, meaning we need to have total tracking at this point for any DOC out there if you want it to be connected to uplink. Regardless, I would say that it would be good for us to have proper credit for that anyways. So, I'm trying to understand what will be the process of your... Today, Uplink connects Salesforce when there's a new system in the field. We hook it up to Uplink. We give it a subdomain. The subdomain... is on the account in Salesforce and that's basically how like abcnews.com so the customer can go on his uplink account he goes to abcnews@realestate.com and then he goes directly to see his customer right so that and in the back end it's all there's Salesforce stores some of the data, like cases, for example, but that's the end of it. Today, I don't think all VOC customers have accounts, proper accounts, that we can link. That's one big gap that we need to understand how we close, I think, if that makes sense. Makes sense to me. If you have any thoughts, because I heard you want to do Unity, take it from there.

[00:21:08.46]  Jason VallerySo let me ask a question on that point. If somebody goes into the marketplace, once we're a public offer, and provisions are asked on cloud, and we don't have a Salesforce entry, will we dynamically create a new Salesforce based on that and via TACO? I think that's a question for John really.

[00:21:27.02]   RemoteOh that's a question to John. Yeah, that's a good question. Honestly, maybe I just assumed that the size of the platform was such that we would always be going through private offers, but I just assumed that it, yeah.

[00:21:47.18]  Jason ValleryYeah, I think we definitely have to think through that workflow because that would be a case when we get to a public offer, even if it's not multi-tenanted, we won't necessarily know in advance.

[00:21:57.09]   RemoteGood question, I'm not sure. Yeah, the assumption we worked under so far was that, you know... I don't know, what are the chances that someone will come across the VAST offering on AWS? I mean, at these stages, for SAS, and say, "You know what? I want to get a VAST cluster without talking to VAST." But, you know, you can take this to any direction you want.

[00:22:30.46]  Jason ValleryYeah. I mean, it may not be the most common flow, but I would imagine it's possible.

[00:22:37.46]   RemoteYeah, technically, yes. I'm really looking for a way to implement it and it will be acceptable for everyone. - (laughs) I'm sorry, Paul, we can take it. Because right now, there's nothing. I don't know if there's opening opportunities there. I don't know, post it in some site, like you're saying, the marketplace, we need to take it from there. I just need to know from where we can kick off this process and where we should create the Salesforce account, create the Uplink account, link them. and then they can register to that uplink domain.

[00:23:18.96]  Jason Vallery- So at a macro level though--

[00:23:20.15]   Remote- Another important detail.

[00:23:21.87]  Jason Vallery- One of the problems I heard is that if we don't have a match with a Salesforce entity from an uplink cluster, where does that data go? Does it just go into some black hole or, I mean, that's a triage process where somebody's like, why is there a cluster out there that we don't know about? How do I link that back to a customer and an opportunity?

[00:23:42.52]   RemoteIf the cluster was never registered with Daplink, it doesn't send anything anywhere. You need to go actively on the system, click Register with Daplink, put the subdomain that we agreed on, the customer and us, right? There is like ABC News. their subdomain, it's unique key. We're giving them that and we're putting that into our Salesforce and uplink account. I can show, you wanna see it for a sec, just how it looks? - Yeah, yeah, that's the type of detail that I think is important, and also the PSNT, Adar, that... - Yeah, yeah, just a sec. I want to put it over here, and I'll make it bigger. So and that's exactly the part that I was about to say, right? So the other layer of detail or complexity that we need to take care of is once the cluster comes up in the cloud, someone needs to go and configure that. That's how it's done today on-prem. In the cloud, it makes less sense. The automation, the terraform that spins up the cluster, I see it as responsible to enter the uplinked data and perform those tasks, right? This is, unless the customer opt out or something. that, right? You know, there's many things that on-prem we do manually and in the cloud, Terraform does that. Here we have in Salesforce, coreweave account, right? Uplink subdomain is set here. This is done by the Uplink Backoffice system. When I go to Uplink Backoffice and I need to add a new customer now to Uplink, I need to give the customer a name. This is from basically just a name that you will have here in our Uplink Backoffice. The support.org name. This is the Salesforce account name that we need to match on. We select the subdomain the account will have, any administrator email from the customer side or from CS from the customer success side, and some special configuration regarding data retention, Slack or email communication, and if the customer will have the customer uplink portal accessible or not right and so customers could access their own uplink and view it as support I'm not gonna create a URL in the subdomain dot a plain vast data right here that's why we need a subdomain exactly so if I go now to our goddess specifically, then there's Agoda Cloud at vastdata.com. This, the customer can access himself. That means the external DNN is actually open for it, and not just vast personnel can access it. We both see the same stuff, right? So if I go here and, And so I'll see Agoda and this is what the customer will see from his side as well. See these clusters. Yeah. This is the uplink itself, I don't know if you saw that, but this is kind of a manager of managers for multiple vast clusters, right? And then you can click into a specific one and that's through the vast call home, right? It's not, you can do it from outside the org or outside the cloud. - Yeah, this is vast basically. this is off link the idea that you have a local DMS somewhere the local management and it's sinking it's itself into the cloud DMS under that domain so you see it as if you are on the system right it's a read-only view of course I can't change anything but I see everything from here no be no Of course the customer can enable authentication, so I won't see all the names here and stuff like that, but I can see all the configuration in VMS, basically, as if I'm on the local VMS. I can view analytics in real time. This is very helpful for support, I can tell you, or for any. telemetry understanding of our system and yeah no this is exactly what i uh so yeah on the back end what i want to say that we have a minute and uh i've stopped so JSON I mean obviously there's many decisions to do make here and then of course you know we can start without with with just manual configuration of a record in Salesforce a record you know like uplink configured on on the device right all the way to everything is automated Salesforce records created automatically based on private offer Terraform enters the subdomain or whatever right it's a there's a range here yeah I think we should have to

[00:29:34.34]  Jason ValleryThink through what the possible solutions are which is the best any we never did like a hello kind of endpoint where when a new cluster comes online even if it hasn't been registered it just announces itself to our endpoint so we know it's alive and then it gets adopted that way we know what's out there so we can kind of trigger our workflow based off of that

[00:29:53.21]   RemoteSomething like that was never implemented yeah And I can tell you that in the past, it was enough link. You need to, the only way is to register with there was a security thing behind it because what you're suggesting is basically customer can come in, send some hook somewhere, and we'll automatically ingest it and start processing it somehow. There was some security concerns with that in the past, a few years back, and there was like an obligation to go and do a registration process that enables the whole uplink in communication between a cluster and our cloud basically. Other than that I don't have any other insights on this. It was just never since Polaris is kind of triggering the deployment process we have I mean nothing will be deployed unless it goes through Polaris so we have the opportunity to collect that kind of data and trigger anything we want at that time, the whole life cycle is going through there. I gotta run, if you want to continue I can assign one of you as a host.

[00:31:24.42]  Jason ValleryI gotta go too.

[00:31:30.62]   Remoteup on this or we want to start some slick channel to discuss it because and I love the idea of it being automatic but I think we're gonna also need to develop something maybe in Boston Yeah, I don't know, I was trying to tell my… Yeah, so I think we need to follow up maybe, I mean we don't need to bug you for this, Adar. There has to be a decision of what, you know, what VOC can accommodate it, what… point uh i think i mean we need to start with with our goal and the finish and everything and see how we can develop it yes but right now you need to think of a really quick stop-gap solution for us because i know things coming up in the field and we need it I don't want to wake me up in the middle of the night to help them configure call home for VOC. Ah, come on. No no, Adar, what we're what we're solving for has to comply with the with the process on your side that's already in place, right? I agree, I agree. That's that's my approach. I'm going to refer you to the... I'm referring to develop on the VOC side, right? On the VOC and the SFDC and, you know, the process of onboarding a customer, we need to decide what we do phase one. Phase one, it could be, you know, the sale rep goes to SFDC, creates a record, agrees on a sub-domain, you know, whatever, right? It's just like, or maybe not. This is for us to decide, you know, we need to decide on those, but then we all gotta run. I don't think it's, I mean, for this session, what I wanted to do is to give John and Jason, I mean, it was more for John, to be honest, Jason, I thought of having a one-on-one with you on this, but, because there are some decisions to make, but really to understand. the complexity of this, or the, you know, it's not too complex, but really the details of this, and decide what we want to do. I will bug you for this decision. Sounds good.

[00:34:01.74]  Jason ValleryMakes sense. Next time we're right.

[00:34:04.16]   RemoteYeah, no, we need to. Okay. - Thanks, LeDoc, thanks everyone. - Thank you, bye-bye. How do y'all continually let Jonathan Hayes back in your country?
```
