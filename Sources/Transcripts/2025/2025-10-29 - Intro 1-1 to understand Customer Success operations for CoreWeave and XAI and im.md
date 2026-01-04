---
entities:
  people:
  - '[[Rick Haselton]]'
type: transcript
source_type: unknown
date: '2025-10-29'
---

# 1:1 — Rick Haselton — 2025-10-29

> [!info] Purpose
> Build trust, surface and remove blockers, align on priorities, coach & grow.

## Summary

Intro 1-1 to understand Customer Success operations for CoreWeave and XAI and implications for a future VAST-as-a-Service model. Rick described a managed-services/SRE-style engagement with Slack-first communication, tickets in Salesforce/JIRA, and proactive monitoring. XAI and CoreWeave run on-prem clusters (XAI ‘Colossus/Colossus 2’), primarily storing raw training data in very large object clusters; checkpointing/inferencing patterns vary. Common issues are networking and node failures; hardware RMAs go to VAST depots; on-call coverage rotates globally with some staffing strain; legal SLAs (e.g., ~30-minute Sev1) and penalties exist.

## Key facts learned

- Rick is tech lead for CoreWeave (#1) and XAI (#3) accounts.
- Both accounts are on-prem; XAI pulls cloud data down to on-site clusters.
- XAI requested one large cluster across four; VAST supports S3 sync replication and site-to-site global namespace but not a single file system across clusters.
- XAI object clusters are ~314 PB used per cluster storing raw training data (e.g., YouTube, Instagram).
- GPU-adjacent storage acts as cache/checkpointing; checkpoints show periodic spikes (~10–15 minutes).
- Managed-services/SRE engagement; alarms flow into Slack; urgent issues move to live calls.
- Ticketing: Salesforce for CS; JIRA (Orion) with vForce for engineering escalations.
- Common issues: networking; C-node/D-node failures; Kubernetes/CSI integration questions.
- Hardware: prefer full C-node replacement; some D-node FRUs (fans) are field-replaceable; CoreWeave DC techs assist.
- RMA flow returns hardware to VAST depots (Campbell or Sacramento) for repair/refurb.
- Coverage: XAI has weekday on-site support; APJ/EMEA cover off-hours; weekends lighter; aim for proactive outreach on incidents.
- Legal SLAs/SLOs in place (e.g., ~30-minute Sev1 response) with penalties; Gordon Brown is CoreWeave CSM.

## Outcomes

- Established Rick as point-of-contact and workload expert for XAI.
- Captured operating-model insights to inform a future cloud/SaaS approach.
- Clarified support processes, common failure modes, and RMA workflow.
- Noted presence of formal SLAs/SLOs with potential penalties.

## Decisions

- (none)

## Action items (for Rick Haselton)

- [x] Connect with Gordon Brown to review CoreWeave/XAI SLAs, SLOs, and penalty clauses. @Jason Vallery ⏫ ✅ 2025-11-08
- [x] Draft an initial SRE/managed-services operating model for a future VAST-as-a-Service. @Jason Vallery 🔼 ✅ 2025-11-08
- [x] Document XAI workload patterns (checkpointing, inferencing, GPU-adjacent vs central storage) to inform product roadmap. @Jason Vallery 🔼 ✅ 2025-11-08
- [x] Outline a remediation plan for recurring networking issues at XAI. @Rick Haselton 🔼 ✅ 2025-11-08

## Follow-ups

- [x] Introduce Jason to Gordon Brown (CoreWeave CSM) to share SLA/SLO details. @Rick Haselton 🔼 ✅ 2025-11-08
- [x] Confirm which cloud provider(s) host XAI’s off-site data and share specifics. @Rick Haselton 🔽 ✅ 2025-11-08
- [x] Provide recent capacity and I/O pattern snapshots for XAI Colossus and Colossus 2 clusters. @Rick Haselton 🔽 ✅ 2025-11-08
- [x] Verify whether object clusters are used for checkpointing at XAI and any planned changes. @Rick Haselton 🔽 ✅ 2025-11-08

## Risks

- Small team and heavy load may impact responsiveness and sustainability of the managed-services model.
- After-hours/weekend coverage gaps could jeopardize SLAs.
- Frequent networking issues drive incidents and latency.
- Lack of single file system across clusters may block XAI’s desired architecture.
- SLA penalty exposure if availability thresholds are breached.
- Rapid raw data growth may stress capacity and operations.

## Open questions

- Which cloud provider(s) currently host XAI’s off-site data?
- What are the exact SLA/SLO terms and associated penalties for CoreWeave and XAI?
- Can VAST’s roadmap enable a single file system or stronger global namespace across multiple clusters?
- How will staffing and on-call scale to meet SLAs as deployments grow?
- What is the plan to reduce networking-related incidents at XAI?
- To what extent is checkpointing returning at XAI sites and what is driving the change?
- How will VAST support GPU-adjacent caching versus central storage in a multi-tenant cloud service?

> Next meeting (if any): (none)

---

<!-- ai:transcript:start -->

## Transcript (auto)

```text
[00:00:00.04]  Jason ValleryI can. Okay. Yeah, let me let me switch over to camera here as well.

[00:00:22.50]   RemoteI'm just going to keep my headset on, it's just easier. No worries.

[00:00:26.04]  Jason ValleryPleasure to meet you. I reached out, I'm a little over a week here at NAST and starting to meet the team and I had some questions of customer success and I was given your name, so I thought I'd set up 30 minutes to introduce myself and kind of learn a little bit more about what you and that end in customer success journey workflow, how it all works.

[00:00:48.93]   RemoteSo that's okay. Well, first I need to ask first, who gave you my name?

[00:00:53.09]  Jason ValleryYeah, I heard it from a couple different folks, actually. So yeah, I had some different questions around just how the account team structure works as it relates to the technical enablement and then post-sale customer. and they're saying, hey, you should go meet Rick. So maybe you can introduce, well, let me start. I'll introduce myself, and then I'll have you kind of walk me through what you own and how that relates to sort of the things I'd like to learn. So I'm reporting to Jeff as VP of Cloud Product Management, and I spent the last 13 years at Microsoft. through that, almost all of it was focused on product management for Microsoft's object storage platform. So, you know, I ran blob storage from every different dimension you could think of, and, you know, Jeff has me looking at what does it take for VaST to really be a cloud-first platform and enable customers to burst to the cloud, but not just that, be primary in the cloud, multi-cloud, connecting data back to Neo clouds, just truly that like global data platform with data spaces and you know so there's a lot of work to go do, obviously partnering with Yancey and the core team to build out the right set of capabilities to enable that vision. That's why I'm here and you know a lot of the... I have are around what, you know, how we support our existing customers, how that has to evolve in a cloud-first world, and so those questions led me to your name, so there we go.

[00:02:28.03]   RemoteOkay, good introduction. So I handle two of the three largest customers. tech lead for these customers right now. Number one, CoreWeave, and number three, XAI. Both of them, of course, CoreWeave is, you know, it's new to the Neo cloud infrastructure business, but I mean, maybe not so new. It's been a few years now, but they are new as far. the the industry is concerned. XAI of course is even newer, but both of them are, everything they have is on site. It's not a, they don't really do anything in the cloud of course, they migrate data between clusters, but everything for them is on site and in fact anything they want to do. know that XAI has a lot of data in the cloud. I'm not sure if it's in GCP or-- because I know they've talked about Google. Anyway, when they want to do some of that work, they actually bring it down to us, which is we just installed a whole lot of clusters. uh in their second site and so they they migrated a lot of that data down to these large clusters to actually do check pointing and inferencing and what have you as needed so right now um you know that would be nice if you know i i like your vision hopefully we can get That's more information and more data sitting in the cloud, but currently everything we do is on premise. Account team, what do you want to know? Like, I mean, we work with the account teams.

[00:04:22.31]  Jason ValleryWhat do you want to know there? - I don't know. You know, we're obviously pursuing open AI. a big opportunity for Vast. I'll give you another lens of my background, which is at Microsoft, I own the storage relationship, and so a deep understanding about how they think about data, their data lakes, you know, data movement to and from GPUs. This is a part of this that I'd really like to unpack the XAI workload and what level of detail you have there and what learnings we've had from this. So maybe that's also a good use of our conversation. What I can say on the OpenAI side is that the way their infrastructure gets managed and deployed by Microsoft probably looks very different than what XAI does, in that OpenAI a couple of locations where they have literally several exabytes, many exabytes of their core data assets, and those are not near any GPUs, actually. They're big Azure regions where there's lots of CPU capacity for running Spark jobs, data-- bricks, transformation pipelines. We do a lot of feature extraction, data normalization, those sorts of tasks to prepare the data and managing the central way, and then Microsoft, they give opening eye GPUs across the globe. So opening eyes GPUs in 50 something Azure regions, and then they're getting capacity in CoreWeave, all the other Neo clouds, Oracle, there was a bunch of press yesterday about now Microsoft no longer has priority decision making on where OpenAI runs its workloads, and so the way OpenAI thinks about this is that they have two real classes of storage. There's central storage, which is kind of cool to warm-ish category, where it's mostly supporting these analytics and data transformation pipelines, and then GPU adjacent storage, which is really kind of a cache, so that the GPUs have a local place to checkpoint and then async, move that back to central storage, and then the GPUs can like stage training data adjacent to the GPUs, such that the real goal there is isolation protection. So like if you've got a 16,000 GPU cluster or something running somewhere and that thing has a loss connectivity on the WAN back to where their central data is, they want it to be able to continue to train, they don't want to have to deal with a multi-billion dollar asset sitting idle waiting for network recovery. So that's the real use case for the GPU adjacent storage, and so, you know, data is distributed out kind of cached adjacent to the GPUs, if you will, and then moved back into central storage. Obviously, XAI has like Colossus and Colossus 2, like, how does that work for them? How does that evolve? How should we be thinking about supporting them?

[00:07:24.45]   Remote>> You know, one of the things that they had asked when they were or when we call it the two lane site, Colossus 2, whatever you want to call it, they had asked for one large cluster. So if we could take, you know, the four that we were building out, or it was eight really, but if we could take those four file and four object, which is what they were earmarked for, and use them as one large cluster. That was the idea that they wanted was to basically have these four clusters act as one. Of course, that's not exactly how we work. We can do synchronous replication now as long as it's S3 bucket data. but we can't exactly work as a single file system across multiple clusters like this. We do have global namespace as well, which technically is something that they could use here, but it's not, again, it's only site-to-site, not across. us for disparate clusters. They do-- so in the beginning, a lot of this, they used us for both checkpointing and the inferencing. Recently, I haven't seen-- at their I/O patterns, a lot of this, you know, when I see the checkpoint, I see, you know, very low bandwidth and then, you know, big spikes every, you know, 10, 15 minutes, whatever, you know, whatever they have it on for the cycle. But they've gone away from that, and actually now I have seen that a little bit come back in Colossus. The two-lane site, Colossus 2, is mostly, so they've got both NFS and object storage there. Their object storage is, how large are these? Actually, let me look at somebody else. Free total. Yeah. Close to. What is that? Well, that's used. To. Oh, that's used to, but I don't know what that is. 100, no, sorry, I'll do a little quick math here. So yeah, 313, 314 petabytes per cluster on those objects, and they use these mainly for data storage, just like you said. GPU adjacent I don't know that they're doing a whole lot of checkpointing right now with those object clusters but they're just they're filling them up

[00:10:50.20]  Jason ValleryVery very fast with the storage so you know what they what are they storing do you know is not the if they're not checkpoints training data or is it

[00:11:00.97]   RemoteTraining data. So the cool thing about this is, is you can see, let me actually log into one of these and then I'll show you really quick. Let's go. H5 object. So, yeah, let's share this.AUDIO (whispering) So, if we go here to the capacity, we can we can typically see some of what they're, you know, based upon their. names.

[00:12:19.47]  Jason ValleryYeah.

[00:12:20.20]   RemoteBut yeah. But yeah, um... So in this case, this one's YouTube video I've seen before, Instagram, you name it.

[00:12:33.47]  Jason VallerySo this is raw. This is the raw data versus processed data. Makes sense.

[00:12:39.87]   RemoteCorrect. Correct. They basically take from the web. You know anything they don't have yet and they just start to pull it down and store here. Yeah

[00:12:51.29]  Jason VallerySo, you know connecting this to the customer success side of this How do you and I don't know if this is a statement just around the XCI account because it's uniqueness or if this is more broadly like how do you think about your relationship with the customer, your relationship with Internal Vast Engineering, like, is it, you know, you're kind of virtually badged as an XAI employee, so to speak, where you're just on Slack with those guys all day and answering questions and bouncing those back against core engineering, or how do you position yourself?

[00:13:26.76]   Remote- Partially, yes. So, we look at ourselves in this pod specifically for Core, we have an XAI as managed services, where everybody else in CS, they work through tickets. We still do work through tickets, don't get me wrong, but we have to have a much closer relationship with the customer. we're taking these things down. We are managing this hardware, this software. Well, I mean, they do handle some of their own stuff as far as creating what they need in the UI, but for the most part, if things break, they expect us to be there within minutes, if not faster. We have to be aware, we have to know. everything. We have specific channels that get all of their alarms in Slack and so we have to watch that specifically. It's a very different relationship than the rest of CS has with their customers, and don't get me wrong, others are, you know, we call them co-pilots. But yeah, we're more of a managed services. We handle all of this. Like today, I had to do some maintenance work and I let them know, "Hey, if we're doing this, just want to let you know, it's not a big deal." You know, and they give the thumbs up. When they do have questions, we answer them. If we can't, then absolutely. We do have to go to vForce typically on a... I wouldn't say immediately, but it's a little bit closer as far as the need there. Yeah.

[00:15:08.55]  Jason VallerySo, as we evolve towards a cloud platform where the goal, and it's going to take us a little while to get there, is vast as a service, a software-as-a-service kind of model where don't have their own clusters and their own tenants, they're just connecting into an endpoint that's running in a multi-tenanted vast deployment in the hyperscalers and wherever we need the capacity. That shifts sort of like the customer success model where we effectively have an SRE kind of team, and I think you're probably the best example of it. what I would classically, you know, using my Microsoft hat, look at as an SRE, because you're ultimately managing the infrastructure on behalf of the end customer. Um, that's correct. What kinds of issues in the vast world do you run into? Like, what's the common ticket? What's the common problem? What's the, you know, you most frequently have to get yourself involved in?

[00:16:12.13]   RemoteNetworking. For example, we're just trying to clean up a lot of networking issues at XAI right now. C-node failures, D-node failures. I mean, mostly software. We still do deal with the hardware quite a bit, But yeah, mostly networking. If things come down to it, then we also deal with actual integration with them. Say, hey, we've got some Kubernetes stuff. How does this plug in to your CSI plug-in? that's a bit deeper and a lot of times at that point we have to go to vForce or R&D and get some answers. But yeah, mostly networking, mostly hardware right now. How does it work if you have

[00:17:06.04]  Jason ValleryYou know a cNode, dNode vendor, your hardware fit, or do you take that node out of it and trigger some sort of RMA process with a hardware vendor? like what's that virtual look like?

[00:17:18.15]   Remote- Yes, if it's a hardware failure, we will determine that first, make sure that it really is a hardware failure, not just something that we can bring it back into service. We check various things, sensors, hardware pieces need and if it is determined that it is a hardware issue then yeah we just create an RMA and our ops team you know gets that automatically based upon what we ask they'll send it out to our shipping address and then for us we have somebody that's on site not 24/7 but you know at least during the the daytime of the week. and we'll just have them replace it. For other, like for core weave, for C-node or D-node failures, if it's an RMA, then we usually get their data center technicians involved. Because it's not that difficult to, you know, hey, unplug these cables, make sure you get where they were before they should have labels. slide the new piece in, and plug the cables back in.

[00:18:26.77]  Jason Vallery- Is it done at the full node level typically, or are there component level failures that are done on site?

[00:18:34.06]   Remote- Node, so especially, so we've tried to do piecemeal components. component replacements in the past, like a DIMM or a fan. For D-nodes, we can absolutely replace fans. Some of those are field replaceable units, but for the DIMMs, we don't do that anymore. We just replace the C-nodes. If it's internal components, then yeah, we just replace the whole node.

[00:19:07.96]  Jason ValleryI assume that's a hardware vendor, like you can ship back to them and then they deal with repairs and sending it back out as necessary, or how does that all work?

[00:19:16.70]   RemoteActually, no, it goes to our labs. So in Campbell, California or Sacramento, I think is where we have our large depot here in the U.S. It goes direct back there, and then, you know, if we say, hey, it's a bad fan or it's a bad dim or something like I believe we'll take that and the folks there at the depots will. switch those out as needed and then do their own hardware checks and then put it back into service.

[00:19:49.98]  Jason ValleryAnd is that just exclusively for.

[00:19:52.94]   RemoteXAI and CoreWeave? No, no, that's that's across the board. So if I imagine if there's, you know, deeper issues, then they would absolutely involve the hardware vendor at that point and say, "Okay, what can be done here?" But for the most part, yes, if it's a bad DIMM or a bad boot drive or, you know, a bad fan, something like that, that normally... they can replace in a clean environment, you know, no problem, then we do that.

[00:20:21.40]  Jason ValleryInteresting. I didn't realize that was happening. Ah, a lot to learn here. What else should I know about your role and how you guys engage with these customers? I mean, in some ways, I think of CoreWeave as a partner, not a customer.

[00:20:37.95]   RemoteYeah, good question. You know, I liked your description. We really are SREs at this point because everything we do is their infrastructure and we have to talk to them almost on a daily basis. So yeah, we're constantly, whether it's fixing network or replacing hardware or just helping them out with various questions, SRE is a good description there. We don't get too much into their workload other than if they have latency or if they have failures. hey we'll tell them you know there was a hardware failure here's the reason why everything is back in service but if we have latency then then you know a lot of times we'll go in and we'll look at what are you guys doing are you writing to the same file over and over and over which is something we've seen before you know hey your io pattern is is causing this latency can you guys you know and look at the directory, the files. Here's where you're actually doing this workload I/O pattern. Can you check to see who's running this job here? Because it usually has a username on it, and we'll fix that. Or at least have them go look into it and fix it. Those are the main things, yeah.

[00:22:14.93]  Jason ValleryIt's an interesting model, you know, coming from the hyperscalers and how we sort of engaged with customers and, you know, covering all customers and multi-tenanted system versus what is effectively a swarm team for a small number of audiences. customers where they're managed, they have their own hardware running in their own data centers, and you're kind of just a piece of the puzzle. So yeah, interesting learnings there.

[00:22:37.72]   RemoteYou know, I will say this, you know, because CoreWeave does have a lot of, you know, their own customers that sometimes we have to get involved with, you know, whether it be CZI or Jane Street or Microsoft. Microsoft, those are the main ones because we talk to them on a I know we we update them on a daily basis. Hey, here's what happened during the day, nothing changed, etc. But yeah, Microsoft is is one of their, you know, main customers there and so we're, we're talking to them on a daily basis as well. imagine as as we get more into 5354 that we will be I can imagine more handling it like you're describing and and uh okay you know here's these tenants and let's just handle it uh as needed but you know for the main customer core weave itself but yeah we're still we're on that

[00:23:37.99]  Jason ValleryTrack I guess you could say yeah how's the I guess it all done through slack like is that where you communicate with core wave and where XAI said and like

[00:23:48.12]   RemoteSaid how you kind of manage the workflow that is the main the main channel where communication is handled if anything is urgent enough of course we'll open up a or a Google Meet if there's anything that you know if it's not just a quick you know a flip of a switch then we have to open up our own tickets both CoreWeave and XAI and and then of course you know write down for the CS tickets of Salesforce or for Orion's in JIRA with vForce. We'll handle that on the back end. But yes, all the ticket opening comes from Slack communication first, and then we handle the back-end communication, of course.

[00:24:36.01]  Jason ValleryDo you have turnaround times, out of hours? Do you have on-call rotations? What are the commitments to and Coral Wave, and then how do you staff that to make sure you guys can take vacations and sleep through the night?

[00:24:50.52]   RemoteSo, okay, so I'll answer some of that. Other points maybe, you know, a point of not contention, but just, you know, soreness, I guess you could say, simply because. it is a, you know, we do have a small team, but these customers do keep us busy. Gordon Brown is the CSC, excuse me, the CSM for CoreWeave. If you haven't talked to him, he can answer a lot of the questions on SLOs and SLAs for them, because we just created something with legal that we absolutely we have to answer within a certain amount of time, and I believe, you know, for SEV1 issues, it's like a 30 minute SLA or SLA. I'm not exactly sure which one actually fits here. But based upon that, we also have issues or an agreement. So if they have, you know, if they go under a certain percentage, then this legal doc actually has, you know, some penalties written into it. So you may want to, you know, I'm not exactly sure what the details are there. But that's actually a first for me. I've never actually heard of it.

[00:26:15.51]  Jason VallerySeen that myself. How does that mean? So from a staffing perspective, how do you manage your team? You know, how does your rotations, what's the commitment? Like maybe that's what the contention

[00:26:30.54]   RemotePoint you raised is at, but what's that look like? Right. Thank you for reminding me. I was like, you were asking. So for making sure that things are staffed, we do have an on-site, excuse me, for XAI we have an on-site, just because we handle the hardware specifically, and they're there just during the week. In a desperate emergency, I'm sure we could call them and wake them up and get them. on-site as needed. For CoreWeave and XAI, outside of that, of course we have APJ and EMEA that takes over during when we're off-shift, but being off-shift for us, because we're more of a managed services type engagement. a little bit difficult to answer that honestly because they may not have all the details bringing them in and bringing them up to speed whether it's an install or an expansion or something like that it may be faster to just do it

[00:27:38.84]  Jason ValleryOurselves at that point I guess yeah let me just play a scenario it's too am and the vast cluster is supporting a big training job for xai just shit the bed what happens okay at 2 a.m my time i assume you mean sure yeah 2 a.m whenever xai cares about it okay um

[00:28:02.57]   RemoteThen we get alarms um most likely I would hope that our team would reach out first and say, hey, we can see that this cluster is down. We've already got people looking into it. Let us know if you have any questions. You know, we just had power outage last night at the two lane site, the XAI-2. So we have people, you know, that are... that are constantly watching and getting these alarms. So yeah, anything that comes in like that, we should have people on shift. Weekends may not be as, when I say may not, they're not as staffed heavily, of course, but there are still people that are on shift.

[00:28:53.22]  Jason ValleryWatching, and so the idea is you are proactively reaching XCI before they reach you. That is the hope, absolutely. I appreciate the time. I have a lot to think through in terms of how we approach an operating model for the cloud and so this was good learning.

[00:29:15.56]   RemoteI will continue to do so. Thanks for giving me your insights. Yeah, no worries. Hopefully, yeah, hopefully it actually works and this information does help. I may not be the most articulate. Oh, you're good. Just thinking about other things right now. But yeah, hopefully it

[00:29:35.00]  Jason Vallery- It did, you know, I'm going to bounce to that. but we'll stay in touch and I'll learn more as we kind of go, and I'm going to consider you my workload expert for XEIs. I try to probe on some of those things. So we'll go there. Awesome.

[00:29:48.44]   RemoteOK.

[00:29:48.99]  Jason ValleryThanks for talking.

[00:29:50.79]   RemoteYep. See you.
```

<!-- ai:transcript:end -->
