---
entities:
  people:
  - '[[Kanchan Mehrotra]]'
type: transcript
source_type: unknown
date: '2025-10-28'
---

# 1:1 — Kanchan Mehrotra — 2025-10-28

> [!info] Purpose
> Build trust, surface and remove blockers, align on priorities, coach & grow.

## Summary

Jason and Kanchan aligned to pursue MAI and UK Met Office as flagship wins to unlock an Azure hardware shape suitable for VAST. Current Azure LSV4 economics and networking are poor; LSV5 is planned but far out and may still be bandwidth-limited for UKWe MO. Marketplace offers are progressing (Google first; Azure targeted soon), but a better hardware shape is required for real traction. Jason will meet MAI (Kushal) Friday, build an economics deck comparing VAST vs Blob vs LSV4/LSV5, and engage Igal. They will coordinate at Supercomputing (panels/booth/keynote slide) and plan a session with Nidhi to raise priority and align internal stakeholders. Neo cloud GPU-adjacent storage and VAST’s KV-store for long-term memory were flagged as additional opportunities.

## Key facts learned

- GPU supply constraints limit 3P deals; demand remains high.
- Azure LSV4 is the only current option; too many cores, weak networking, low drive density; poor $/perf for scale.
- VAST density claim: ~1 EB needs ~20 VAST racks vs ~240 Blob racks; power can be ~1/5 in MAI Falcon-type clusters.
- Azure Storage is unlikely to champion VAST; need support via Igal’s team and marquee customer pulls.
- Target lighthouse customers: MAI (existing relationships with Kushal and Vipin) and UK Met Office.
- UK Met Office is price-constrained; networking on planned LSV5 may still be insufficient for their target.
- LSV5 is committed by Igal’s team but is far out; Azure parity trailing AWS/GCP today.
- Marketplace control plane (from Yancey’s team) is being integrated; Google first; Azure targeted around February (unspecified year).
- MAI already has CoreWeave capacity; VAST capacity exists there; MAI interest in VAST on Azure remains.
- Neo cloud adjacency storage: keep GPUs productive during network disconnects; aim for a GPU-to-local-storage ratio.
- VAST has a high-performance KV-store (Undivided Attention) suited for long-term memory; Microsoft declined to build similar earlier.
- Sales push should follow a tangible offer; use Nidhi to amplify once listing and story are ready.

## Outcomes

- Alignment to prioritize MAI and UK Met Office as anchor wins to drive Azure hardware shape for VAST.
- Plan for Jason to meet MAI (Kushal) Friday and report back; then coordinate next steps with Kanchan.
- Agreement for Jason to produce an economics deck comparing VAST vs Blob vs LSV4/LSV5 and on‑prem.
- Coordinate Supercomputing/Ignite activities (panel, booth, keynote slide) and a follow-on session with Nidhi.
- Jason to connect with Igal to discuss LSV5, networking, and required shapes.
- Explore Neo cloud GPU-adjacent storage scenarios with Suresh/Anand when ready.

## Decisions

- Near-term focus on MAI and UK Met Office over broad sales motion.
- Pursue a dual-track: marketplace listing plus flagship customer escalations.
- Use Nidhi to re-energize internal advocacy once the story and offer are ready.

## Action items (for Kanchan Mehrotra)

- [x] Meet MAI (Kushal) on Friday and gather requirements/next steps. @Jason Vallery ⏫ ✅ 2025-11-08
- [x] Connect with Vipin Sachdeva to re-open MAI conversation and align with Kushal. @Jason Vallery 🔼 ✅ 2025-11-08
- [x] Build economics deck: 1 EB comparison across VAST on LSV4, LSV5, on‑prem, and Blob (HDD/Flash) for internal NDA sharing. @Jason Vallery ⏫ ✅ 2025-11-08
- [x] Share MAI meeting notes with Kanchan and propose joint plan. @Jason Vallery 🔼 ✅ 2025-11-08
- [x] Engage Igal to discuss LSV5 shape, networking needs, and customer-driven pipeline (MAI, UKMO). @Jason Vallery 🔼 ✅ 2025-11-08
- [x] Meet UK Met Office leaders (Mike Kiernan, Nico, Alan) at Supercomputing to push VAST approach. @Jason Vallery ⏫ ✅ 2025-11-08
- [x] Coordinate SC/Ignite joint story and VAST booth content with Kanchan/Lior/Andrew. @Jason Vallery 🔼 ✅ 2025-11-08
- [x] Set up session with Nidhi to review MAI + UKMO case and economics deck (post‑SC if needed). @Kanchan Mehrotra 🔼 ✅ 2025-11-08
- [x] Confirm if Suresh will attend Supercomputing and, if yes, schedule a discussion on Neo cloud GPU‑adjacent storage. @Kanchan Mehrotra 🔼 ✅ 2025-11-08
- [x] Advance Azure marketplace offer with Yancey’s team (control plane, listing, billing). @Jason Vallery 🔺 ✅ 2025-11-08

## Follow-ups

- [x] Sync next week after the MAI Friday call to decide support plan. @Jason Vallery 🔼 ✅ 2025-11-08
- [x] Verify Nidhi’s availability (SC or post‑SC) and confirm a meeting. @Kanchan Mehrotra 🔼 ✅ 2025-11-08
- [x] Check with Lior on outcomes from dinner with Igal and capture any asks. @Jason Vallery 🔽 ✅ 2025-11-08
- [x] Confirm Wave’s current GPU status and whether a VAST proposal is viable on Azure. @Kanchan Mehrotra 🔽 ✅ 2025-11-08
- [x] Validate UKMO networking constraints vs. planned LSV5 with Igal’s team. @Kanchan Mehrotra 🔼 ✅ 2025-11-08

## Risks

- Azure LSV4 economics and networking may block viable customer deals.
- LSV5 availability is far out and may not meet UKMO bandwidth/price targets.
- Marketplace on suboptimal SKUs risks sticker shock and poor traction.
- Internal conflict of interest with Azure Storage may slow partner progress.
- GPU capacity constraints limit 3P customer commitments.
- Unclear contracting/operational model for Microsoft use of Neo clouds.
- Information-sharing sensitivities around MAI deployments may slow coordination.

## Open questions

- What exactly is MAI’s new capacity/location plan (Azure region vs. Neo cloud) and how can VAST participate?
- When will LSV5 be available and with what networking, and can it meet UKMO’s price/perf targets?
- What is Microsoft’s contracting/operational model when consuming Neo cloud capacity, and how can VAST be deployed there?
- What is the concrete Azure marketplace timeline for VAST (month/year) and minimum viable SKU shape?
- Will Nidhi attend SC or prefer a post‑SC review, and who else should be in that session?
- Is Wave’s ask feasible on Azure without a better storage shape, or should we steer to alternate paths?

> Next meeting (if any): (none)

---

<!-- ai:transcript:start -->

## Transcript (auto)

```text
[00:00:00.04]   Remote- Hey Jason.

[00:00:02.06]  Jason Vallery- Koncha, hello, how are you?

[00:00:03.50]   Remote- I am good, so good to see you.

[00:00:08.11]  Jason Vallery- It's been a minute.

[00:00:08.93]   Remote- Wait a minute, one second, my video is still turning on, on. My God, why did the window disappear?

[00:00:19.55]  Jason Vallery- I see you now.

[00:00:22.50]   Remote- Yes, there you go, yeah. - Hey, so how are you doing?

[00:00:27.63]  Jason Vallery- Good.

[00:00:28.39]   Remote- Good to see you on the other side.

[00:00:29.95]  Jason Vallery- Yeah, it's been an interesting few months. Role transitions, I took a sabbatical and now I'm back at it, a couple of weeks at VAST and kind of assessing the land to land and getting to know folks and figuring out some value and yeah it's been interesting time but I'm excited about the futures.

[00:00:52.34]   RemoteGood, good. I'm excited for you as well. MAST is a good place. It's a good partner.

[00:01:00.21]  Jason ValleryI heard you have maybe some interest or like the overall team structure. I mean, I heard some rumors, I don't know what's all going on, what do you, what's changed for you?

[00:01:15.69]   RemoteSo for me, the main thing that is changing is I am also working a lot on OpenAI and, or starting to work more on MAIs, OpenAIs, and all those things. stuff that is 1P2, with all the 3P GPU capacity. You know this coming from Microsoft, so I can tell you, right?

[00:01:41.02]  Jason Vallery>> I know all of what you're up to, because that was my life for the last few years, so yeah.

[00:01:46.67]   Remote>> Yeah. So 3P GPU, obviously the capacity constraints and things. that we have limited capacity to give to 3P customers. Of course, things have slowed down a little bit on that, and for me, I don't know if I should call it slowed down because I still am in an escalation every second day, but new big deals have sort of come somewhat slowed down for that, right?

[00:02:15.03]  Jason ValleryThe demand is drying up or is that because supply is so scarce? It's not the demand, it's a supply,

[00:02:20.15]   Remoteit's a supply problem. Demand is like, that's the thing, like I'm trying to answer, give answers to everybody every single day, get a new demand, but we don't have enough supply to give to everybody.

[00:02:34.00]  Jason VallerySo on the one piece stuff there, I said, like, what's your role there? Are you capacity? Like, that seems to be like 95% of the role is.

[00:02:44.72]   Remote- No, no, no, no, no, no, no, no. Yeah, I know. Yeah, my team is injecting more on the technical side of things. So it's been, customer success has been mostly fluid in OpenAI engagement. and partly because they don't care, they don't work the way most customers do, but starting to sort of help the team solve some of those problems. MAI obviously is heating up quite a bit, right, so definitely they have been out for attention in some ways and of course I mean they're looking for more help. So those are places and then we did all these 3PGPU deals so my team will start working on some of those. How do we how do we? actually use those in Azure, so.

[00:03:47.78]  Jason Vallery- Well, I mean, it's a good segue into kind of why I wanted to chat with the team and I'm glad Nidhi connected me to you and Jack and others. You know, my goals are tied to making VAST successful across the hyperscalers. There's a number of things under that in terms of what it means. It's not just marketplace, it's what do we need from a platform perspective on Vast to truly build out global namespace? How do we do this in a cost to performance ratio that makes sense? And so the biggest constraint we have is the topology that's provided by the L-series VMs. So, you know, today, the only option and what we'll go to market with, not just on Azure, but in all of the hyperscalers is using compute SKUs that have NVMe on board to deploy VAST, and when you do the math behind it, it just doesn't cancel out. You know, the amount of. compute as a function of the amount of storage on those instance types, it's just financially never going to make sense. It's never going to scale to the kinds of capacity that customers like OpenAI and Microsoft AI need. You know, there are hundreds of petabytes, exabyte class deals, and, you know, you just, the laws of physics prevent that from ever being successful in L-series, let alone the costs. associated. So, you know, the first big constraint we have to overcome is how do we get the hyperscalers to offer a hardware shape that matches the demand, and so, for example, like when vast deployments on-premises and, you know, a perfect example is XA. Theoretically, VAST is the storage platform that Elon uses for XAI and for Tesla, right? And that's deployed into XAI's data centers. VAST is obviously a software-only company, but they have OEM/ODM relationships and qualify various hardware platforms from upstream providers, and so, you know, you could spec out... a vast deployment which would provide an exabyte of capacity and deliver tens of terabytes per second of throughput, read/write these variables, and we can get into the weeds of that, and here's the stunning fact. This was my biggest learning so far since I came across 2bast. When I delivering an exabyte of blob storage to OpenAI or Microsoft AI or any real customer. In practice, that is 240 racks of storage. That is something Vast can do with 20 racks. The density of VAST is 10X fewer racks than blob storage for the same logical storage capacity. Huge amount on the data center planning front. Then later on that, the power savings. So in one of these, like, you know, the MAI Falcon cluster is the perfect example. It's 1/5 the power consumption. So you can just imagine like when you're in one of these data center planning exercises, trying to build out one of these clusters, the amount of, I guess, hundreds of kilowatts, approaching a megawatt of power savings that you get by using VAST in one of these hyper dense. OEM provided hardware footprints is all, you know, opportunity to go deploy more GPUs in that same data center, and then you layer that with like just from a platform perspective, the global namespace and all the like management features and control plane simplicity that Vast has, and it like is actually just a no brainer. So the problem is, of course, Azure doesn't have it. a hardware SKU that looks like this, and so, you know, my biggest challenge is to try and figure out how to get alignment within Azure to give us a shape that looks like this, and I'll tell you, like, I'm just being upfront. When I think about the organizations inside of Azure that have skin in this game, you've got EGOL's team. they're probably not super incented to do this because they want it to be more of a general purpose compute kind of approach. They'll continue to put maybe a little bit more MDM in, but I don't think the EGOL is going to win this for us, and I'm sure as hell don't think Azure Storage has any interest in making us successful. Manish's crew is not going to sign up for this. So, you know, what I need. and I'm just being upfront about this is a couple of marquee customer wins that will get us the presence with Ronnie's team to go and try and qualify one of these clusters and get it put into you know an Azure delivery kind of pipeline. That's my goal and I'll tell you we're having conversations already that I'm sure you're already aware of, you know, the UKMAT opportunity is mine. We're going to have to do something there. But more interesting and probably more tangible is the MAI folks. You know, Microsoft AI was born on that. They were, as inflection, And I tell you, I sat in these meetings when I was over on the other side of the table, you know, they were drug kicking and screaming at each other, and when Falcon was planned, like the three exabytes of blob going into that thing was purely an artifact of trying to get enough storage throughput, wasted a ton of megabytes. MAI folks are reaching out to us, so you know, if your focus is on MAI, how do I help solve and bridge those gaps? I have, like frankly, I have a meeting with MAI this Friday, they reached out. Okay. What do we do? What do we do to make this successful? I can go get MAI going up to leadership, if I can get UKMAT team going up to leadership, and we can come together and say... we need to go have a hyper-converged, hyper-dense, vast kind of footprint to go and unlock lots more GPU opportunity and deliver better value, that's my goal.

[00:10:16.94]   Remote- Yeah, so I think the two of us are fully, fully aligned. In fact, I had brought up MAI last time I spoke and I brought it up with Karl. and I told him like, you guys should go talk to MAI, right? Because MAI was, he actually even pinged Kushal.

[00:10:39.54]  Jason Vallery- Kishore, I worked very closely with Kushal in my previous role, and then he saw that I started as VP product management at Bass, he pinged me, congratulating me. chat. We're connecting on Friday. Similarly, there was a guy over there named Rippin Sachdeva. He's a big Bass proponent. So there's existing relationships there.

[00:11:02.54]   RemoteSo I worked with Rippin as part of inflection, like my team worked with him as part of inflection. So I had pinged Kushal. Interesting enough, he told me, like this is when Vast was visiting here, I told him like we're doing this with Vast and I know you guys were interested in using Vast, so is there anyone I can connect the Vast team with to talk to you and see if this is still of interest, right? So I'll be honest, I went. out of the way and did it because I was like, oh my God, Sora, she was gonna be really angry at me that me too for doing this. Kushal somehow disappeared after saying, yes, they were interested. So if you can also connect with Vipin, like maybe that's why he did have it top of mind still, when you went to BASC but he had mentioned to me that there was interest and that again nothing happened to be honest. So but I feel that is really the path we should go after. Like UK Met Office obviously there is that path we need to use that. as one of the leavers. The problem there is timelines and how fast can we get it for them, right? So between MAI and UK Met Office, I think we'll be able to tell a much better story. We'll be able to get EGAL even to do more for us, it's not running, like we'll be able to get IGAR to do more. I feel like we're struggling because we don't have enough people yelling. I would actually connect with to your point, right, I feel like storage somehow, you know, my thoughts on this earlier tonight, when obviously there is this conflict of interest. I actually always is feel like it's tricky that Storysheim is driving partners too because there is a clear conflict of interest there, right, so Nidhi has been in the past a big advocate and that's why she keeps inserting me into vast engagements and she's kept me in there because she, has been advocating for getting, getting vast into Azure and like making, making it successful. So I do feel like you should use her more often. I feel like it kind of died down because like Ong has been sort of leading that part of the engagement. But I, I feel. like we should leverage her more often like even for these asks with Egal and others. So I think those those are things we can do to make faster progress here. One thing Jason I feel we also need to see we can do on on the vast side is right now, we don't, we've been asking, like, we've been hoping that we can do, like the lifter program is going to be, it's a big lift. Okay. So we need something interim to start sort of talking and start doing things versus talking. Right. Because this has actually gone for a very long time. Right. So, um, and one of the things we've been pushing for is like let's get it into marketplace right let's get a marketplace option with whatever non-optimal SKUs we have like we don't want to go with two customers and like sort of disappoint them and sell something that is not fully baked but get us an opportunity to talk more about the vast Microsoft sort of partnership, get people excited because then we will have people coming to get like, we'll get a pipeline at least, right? Right now if I can't talk about it, there's no pipe customer showing interest in it either. I don't know if it makes sense. Yeah, for sure.

[00:15:22.78]  Jason ValleryThe marketplace will come pretty quickly. I don't know who you met with when Bass visited. Have you met with Yancey yet? Do you know who Yancey is?

[00:15:31.06]   Remote- Yeah, I did, I did, yeah, yeah.

[00:15:32.51]  Jason Vallery- Yeah, so I mean, he joined and I joined and he and I are aligned. So I'm his PM counterpart now. You know, the hybrid scalers all are gonna get a marketplace solution pretty quickly. You know, I won't overshare, but we're a little bit further ahead with other hyperscalers we're about to launch on Google, and, you know, when you look at the current shape of the VM SKUs that we have to pick from, Azure is the least favorable. The LSV4 is our only option. They're just, it's way more compute cores than we need, crap networking and density on drives. So when you try to translate this back into a value proposition to a customer, it's just sticker stock, and it's going to be like, why can I, I can't afford that, and, you know, honestly, like that is true of the storage partners Microsoft has, and it's why like these marketplace solutions have never had any traction. I generally like, you know, being a little cynical about it. I've always just assumed this was Microsoft trying to prevent a third-party storage business from emerging in the marketplace. But we can set that aside. We have a commitment now from EGOL for an LSV5, which kind of brings, but it's a year out crunch on. oh, this will be, you know, end of calendar 26, you know, when that ships, a year from now, it'll bring Azure into parity with what Amazon and Google already have today. We'll go get the box for you. Like we're going to go and, you know, get these other cloud providers online first because there's actual customer demand and they have a better shape, not a great shape, but a better shape. and we can get some actual customer traction there. But, you know, then that's a fast follow to bring Azure online, and, you know, Johnson gives me February as a timeline and he's tracking for Azure, I believe in. So we'll have a marketplace offer out there, but it's not going to unlock business together until we have something that actually aligns with what customers need, and that's the city piece. So getting that ball rolling, like we have to have a dual track, and for me, if we can go win AI, you can add, you know, one-off deals, you know, that that then enables Azure to take a more serious look at the hardware problem, and just being upfront about this, and this is kind of one of these weird worlds because I know things that I maybe shouldn't know on the Microsoft side, but I'm over here, like one of the challenges that we were facing with OpenAI and MAI is like the proliferation of Microsoft's partnerships with the Neo clouds and the least data center providers and what that means in terms of bringing capacity online. One of the things that you know is acute and we hear about is the control plane problem and that you know taking a data center from core or a data center from Nebius and scale, whoever, and turning it into an Azure region is a huge lift, and, you know, ideally you're getting bare metal GPUs with a very thin Kubernetes control plane and not turning it into a blown Azure region. I want to call out that that's another opportunity for us. Azure Storage can't even deploy. So, you know, where you're coming across this Neo cloud problem, we think we can solve that for you in a way that I know Azure Storage can't solve today. What you're able to share there, like, what's the state of play around all of that?

[00:19:01.74]   RemoteYeah, I think that is a potential opportunity because, but I feel like, you know. not there yet on figuring out like what's the story, just to be very honest. But we had a conversation last time Vast was here. We invited Anand and Suresh, right? On the, they've been in all the 3PGPU deals to have that conversation. like if we if if there is an opportunity there. My understanding, Jason, is like all these Neo clouds do have vast already, am I right? Like maybe yes and or most of them at least.

[00:19:43.47]  Jason ValleryBoth of them didn't have a storage solution. We've asked to have partnerships primarily with CoreWeave, Crusoe. We're talking to the other ones. But it's really like there's a contractual and workload conversation that intersects the cloud provider here. So if you're going into one of these Neo clouds, the underlying question that I come to is, is this Microsoft going there as a lease provider or space power dropping Azure Kit and selling? through Azure, this capacity, or is Microsoft going there and deploying a internal 1P or customer workload leveraging the stack from the neoclient? And there's a fundamental difference in how you would use the infrastructure and certainly how you would contract the capacity. Like when CoreWeave goes to market and sells storage they are Vast as a white-label product versus how if Microsoft is deploying Vast into CoreWeave to support opening IRMA. So I think working through some of those weeds is what I'm interested in really understanding, and less about CoreWeave because that's sort of a known problem space but it's these new emergent ones. I mean there's I mean probably half a dozen of them that have just popped out of nowhere that I didn't even know existed a couple of months ago that are all going into this we want to be a Neo cloud space and then Microsoft is signing all these partnerships so I just don't have my head around what that looks like in terms of how is Microsoft using that capacity and going to market with that capacity.

[00:21:20.31]   RemoteOkay, so at least right. now we are mostly sort of evaluating which workloads would be able to run on those. We're a bit early in that conversation but Jason this is something let's let's hold on to it and we should talk about it. If we do meet with I don't know if Suresh is coming in to supercomputing or not, I will check. If he is, he would be somebody I think we should connect. If he's not, then we can connect with him a bit later in the cycle. I know I'm working on this first-hand, my team, with Suresh, so I know we're not there yet. but this would be something that we should have a conversation about.

[00:22:11.26]  Jason ValleryLet me play in your head the workload scenario that I see, and this is coming from my experience with OpenAI and hearing directly from them, but also other model builders. Fundamentally, if you're deploying a GPU cluster in one of these Neo clouds or wherever you're deploying it, You know, there's two workloads, inferencing and training, those two, right? And the thing about these NeoCloud data centers is that their network connectivity isn't as mature. They're probably in sites that don't have the same level of resiliency, you know, their quick builds, wherever the power's at, and so, you know, the way OpenAI has presented this historically, and I can tell you even recently, we're talking to them, is that it's about the network disconnect and autarky scenario. You know, if you've got a big fat pipe from one of these sites into a hyperscaler Azure central region, you know, you can pull the data across that pipe. Pretty great. It works pretty well. It's certainly good enough for inferencing and even for training, it works in most cases, assuming you can get enough terabytes, and in that world, you actually don't even really need local storage. But what they really worry about, and this is the primary use case of why they want local storage, is the network disconnect case, and so you've got 8,000 GPUs, 12,000, 16,000 GPUs in one of these facilities, and an idiot with a backbone digs it up, digs up the fiber line, and now you've got disconnected from the internet, disconnected from Azure, 12,000 GPUs, and if you're doing training on them. and there's enough local storage that can act as like a buffer capacity, those GPUs are still humming along and doing productive work, and so, you know, the opportunity is a fairly small storage investment in terms of rack count, dollars, and capex to ensure that when a network disconnect happens, you don't have... a multi-billion-dollar asset idle for 72 hours while they're fixing fiber. So OpenAI is really adamant about, they want a couple hundred petabytes of GPU-adjacent storage for every 8,000 GPUs wired in such a way that it survives network isolation. they can make those GPUs productive even when the big fat pipes to aggregate, and I think that's a trend that we see for all of these Neo clouds and all of these kinds of deployments. So, you know, what I'm pushing back on you is I'm sure you there's not a whole lot you can share here, but the idea you should think about is that there really should be some ratio between GPU count and GPU adjacent storage that fast can be come in and step in and provide wherever Microsoft is deploying GPUs when Azure Storage isn't an option.

[00:25:14.99]   RemoteThat's actually a good idea. It makes sense. It's funny, maybe I should ask you, I don't know, were you working with teams like AI Foundry or some of our one P teams when you were here at Microsoft, like from a storage perspective, Jason?

[00:25:36.06]  Jason ValleryA little bit. Actually, it was like, had I stayed at Microsoft, that I would have actually been my new role. I mean, a lot of politics went down. I don't need to bore you with it. It was a whole

[00:25:47.26]   RemoteThing. But when Manish was positioned- I was surprised you lasted this long. I know there was- so much craziness going on in your foot.

[00:25:56.33]  Jason Vallery- What Manish was positioning me for was to go work with Foundry on, you know, some of the caching and strategy around how we would support Foundry. I mean, again, some of the weeds around that, but yeah, and Project Apollo and how all of that would come together. So I didn't work with them a ton, but I did have a few meetings with them and I kind of understand what their goals in architecture were.

[00:26:21.79]   Remote- As I'm wondering, do you see a place for rest and like their scenarios?

[00:26:28.97]  Jason Vallery- Yeah, it's the key values, key value store, and so, when you look at the future of long-term memory models. What's happening is OpenAI has talked about this publicly. NVIDIA is pushing on this. In the open source world, this is really evolving the key value store space, and so when you've got happening or an agentic worker doing inferencing, you've got all these tokens that are being generated in the context state, and today there's like a cache that runs within the GPU host, so it's like a prompt cache and then a pre-fill cache that runs to store that state between terms. So like if I ask it a question and then I come back and ask it another question, it doesn't have to re-compute my previous inputs into the model. That's kind of the current state of affairs and Foundry has that capability today. But what's evolving, and so the first open source example of this is VLLM's page detention. DeepSeq published some research around this and OpenAI has talked about it publicly. It's this idea that your context window in the model can grow outside the scope of the inference window and be long-term memory, and so, you know, the model will run, it'll kind of like distill that information down and then store it, and then it'll be able to access that those previous tokens as necessary so that it really remembers everything, and that's ultimately a key value store. The way they do this is they're using L-series VMs with open-source RocksDB and FoundationDB. They're very disappointed in the shape of the L-series VM as well for the exact same reason, because it doesn't allow them to get an update. The Foundry team, they haven't talked about this problem, but I will expect that when the Foundry team... gets their hands on GPT-6 because OpenAI has talked publicly like this is the key feature of GPT-6 is long-term memory that what they'll actually be asking for is a key value store, and so fast as a head here, they built something called the undivided attention capability and it's a key value store that's very performant, and so what you know, opening eye came to me like a year ago and said we want Microsoft to build a key value store that's hardware optimized and can scale to many, many, many millions of TPS per petabyte. Like this very high transactions per second to data stored ratio and like give us everything the hardware can give. I took it to Manish, took it to, to the architects. We sat down and looked at it. I mean, he just sat on his hands and said, I don't want to take this opportunity, and so where I see another opportunity for Vast is they already built it. It exists. It's very performant. We could step in and provide a very high performance key value store that would support. these long-term memory workloads that OpenAI will have. They've already built their own solution because Microsoft said no, that I'm assuming the Foundry team will certainly have, and anyone else looking to build long-term memory into the context window will need this kind of capability. That's another opportunity to partner.

[00:29:59.08]   Remote>> OK. So, yeah, I think let's start with the MAI and e-commerce discussion. Jason, should we have a recurring or something? I don't know if you will or you will. There are some meetings that are recurring, like that are run by Karl and team. But I think-- We should iterate on some of these ideas that I've said I would love to have one-on-ones with you as well if it makes sense.

[00:30:30.28]  Jason ValleryYeah, on whatever frequency is appropriate. I mean, I'll be at super computing, so when we get coffee there, just get a side meeting. Yeah, yeah, I mean, I want to stay, so it sounds like MAI is an area. focus for you. I think that's the short-term opportunity because it overlaps both of our worlds and you know we can pursue that from different angles it would be great.

[00:30:52.16]   RemoteYeah yeah I think we should do that and then UK Met Office definitely because there's nobody contesting for it in a way. I feel like UK Met Office is going to be more of an easier win if we we can get. The platform like MAI will help us raise the priority of this, to be honest, if we can get them to say they want fast and they wanna support this, but yeah. So let's, yeah, let's share notes like once you have a conversation with.

[00:31:30.71]  Jason ValleryI'll talk to him on Friday and then maybe, you know, I'll reach out to you next week and get some time on your calendar to figure out what we do as next steps to support those guys. I mean, he made a cagey comment in the chat with him, it was like, you know, this isn't going to really be Azure. So that's kind of why I was pushing on the neoclip dimension. like, what's he talking about? I guess I'll find out on Friday, but if they're getting some capacity in core weave again or something, I'm not sure.

[00:32:02.16]   Remote- They already have core weave capacity.

[00:32:10.21]  Jason Vallery- Yeah, but they already have vast capacity in core weave too. It's more of like, what's that incremental opportunity? that he's alluding to, that's what I'm trying to figure out.

[00:32:19.17]   Remote- Yeah, yeah.

[00:32:20.75]  Jason Vallery- I mean, the issue is-

[00:32:21.59]   Remote- I think I know what he's talking about, but I don't know what I'm supposed to share or not.

[00:32:26.51]  Jason Vallery- I know, I'll let him tell me, but you know, that will happen.

[00:32:30.87]   Remote- I mean, I get sensitive to, like, if you share things about them, so I let him share if he's willing to share.

[00:32:38.13]  Jason ValleryI mean, the interesting thing is like how we in the long term get into Azure with Overlake and try to make the whole network play, because I mean, look, there's precedent, there's prior art. This is what NetApp Files is, right? NetApp Files is NetApp's hardware running bare metal in Azure with network offload, direct

[00:32:59.38]   RemoteBye.

[00:33:00.90]  Jason ValleryThat's the model. Like it wouldn't be vast hardware, it would be OEM ODM hardware that we qualify, but that's the model we seek, is the ability to go and dock our stuff with our partners and sell that in a multi-tenanted way to Azure customers.

[00:33:18.14]   Remote- Yeah. - Yeah. Cool, so on UKBetOffice, are you talking to Mike Kiernan already or no?

[00:33:30.94]  Jason ValleryI pinged him, I haven't heard back from him, but you know, what's funny, I'm assuming you know Nico. Nico and I go way back.

[00:33:37.67]   RemoteHe just, yeah, joined his team as well.

[00:33:40.49]  Jason ValleryYeah, so Nico's on point now and on Mike's team. I talked to Nico this morning and it was good to catch up because I hadn't probably talked in six months or more and uh sounds like he's going to be the key storage um person for mike so i'm you know i'll run in the bathroom but uh i haven't talked to mike in a while it's probably a year since i've talked to mike but um i'm assuming he'll be at super convenient i'll try to grab

[00:34:00.34]   RemoteCoffee with him or something yeah he he will be i know mike and uh allen both will be at supercomputing. So it'll be good to meet with them and like if we could meet with them and push them. They will need yeah they'll need some support internally as well. I know they were trying to push for the EGALS right. I mean for them that's the main problem with my office right there. There are price constraints. So if we don't have the right SKUs, like one of the things that we were looking at, even with LSV-5 was the networking, the network bandwidth is like, the networking planned for LSV-5 was still not enough to drive the price low enough for. UK Met Office. So they were that, that's, that's the battle that we were sort of trying to fight there. I don't know if Egal, did you meet with Egal? I didn't, Lior did. After you joined?

[00:35:08.55]  Jason ValleryUh, I haven't, no. So last night, apparently Egal's in Israel right now. So Lior is the, be a person for VAS that's been running a Microsoft relationship for a while. So I know Leora had dinner with EGOL last night, but I haven't met EGOL since I've been over here.

[00:35:25.80]   Remote- Yeah, EGOL took them on a different track as well. So talk to him. I think you should talk to EGOL for sure. I know he's supportive and I've had a few conversations and he's like, "I want to support this." I feel like he'll also need that push and the pipeline, right? To be able to push it beyond what he's able to do right now. But talk to a girl, I would say.

[00:35:57.47]  Jason Vallery- Okay. customer name that came across my inbox, Wave. I mean, I dealt with him many times over the past. They're knocking at the door again. What can you share about what's going on with Wave? It sounds like they're struggling to get GPUs. I don't know what's happening. Is there anything that we-

[00:36:16.91]   RemoteSo they, I think we've resolved that. They were supposed to get, they were fighting for GPU. and then they reduced their demand. As far as I know, we actually met what they needed, but I know they were another customer who were coming up and there were discussions with West. I don't know what they are sharing there.

[00:36:45.76]  Jason Vallerypepabyte pitch on how we invest in Azure and even 40 pepabytes when you run it on LXP4 is again going to be prohibited. So, you know, I remember dealing with Wave, it was like Blob never met their throughput requirements. They, there's different architecture. We just never got to what would make them happy on Blob. So I assume it's a continuation of that. But you know one of the vast sales folks had pinged the other day saying that Wave was back at the table looking for us to propose a marketplace solution to Wave at that 40 megabyte volume. Again, it's the same problem like it's just not going to work.

[00:37:22.41]   RemoteI know we had included them in the pipeline that we've been sharing with you all, like UK Met Office, Wave. You know a couple others but they we did include that I know for sure. What was not included was MAI obviously because we did not got in any kind of. Confirmation from them like another than the unofficial yes we are interested. I got. Right, so I have not mentioned MAI officially. I know that.

[00:38:05.48]  Jason Vallery- And then I guess the last question is, in my previous role and then kind of now evolving here, wanna keep tabs on what the repeat opportunities there are co-sell. we can do together. Your opening statement was that that is drying up. I'll tell you the, I talked to our friend Kirk and he was saying that's his new gig. It is like pre-qualifying 3B. Yes. Interesting role. I mean I had been working with Mike Gollin's team and Mike continues... I touched base with him not that long ago. What's that cycle looking like? Where do you see that evolving? Is Microsoft going to go after a 3BGPU business and model builders? There's this enthropic thing. Is there somewhere we should be pursuing on that front?

[00:38:52.57]   Remote- We will be. The thing is, right now, the capacity constraints are... stopping us from going all in, right? The demand comes in, it goes through, it's like our pipe for how many, like if you remember like in the past year or two, right? We were very restricted about which ones are we saying yes to versus not. There was a whole DWR process. around 3P customers, right, which are the deals we're going to sign versus not. The pipe has gotten smaller. There are still deals that are going through, but again, because we don't have as much capacity. It's always a conversation about like if 1P was versus 3P prioritization. So I think we should continue to push in that direction because at least the kind of customers that are winning may still be the customers who would wanna use large scale set of storage, like vast. We'll have to make sure that VAST is top of mind for the sellers. So I had actually introduced, I had asked a VAST team to meet with Kurt when they came last time. So they did meet with Kurt. So I would actually suggest that we keep that connection. So it's top of mind for sales, right? And one thing that I've always told all our partners, like storage partners in the past too, like I feel like we don't do a good job of telling the story, the differentiation story. Like you started this meeting with the biggest differentiation you can tell me, right? On why best is sort of. is helpful for our customers or for Azure, right? I feel like we don't tell that story to our sales teams and they, of course, if we don't tell that, they don't know and they don't share that with the, sell it with that much rigor. So I think we should work the next few days to build that story. But then again, Jason, like the thing that you're gonna be stopped at is where's the product, right? And that's why I was like saying, like, I feel like we'll have to start. So we'll have to do something about that. I see yours. stance on this, or best stance on this, but I feel like anybody in sales is not going to take this conversation seriously unless they have something to sell.

[00:41:50.34]  Jason ValleryYeah, fair point. I mean, the marketplace offer is a P0. You know, the idea behind what's going on here, and actually I don't know what you know about Yancey and his business before. was acquired by like July, August, and what he was building was a marketplace control plane. So, you know, we pre-integrated with the Google marketplace, the AWS market, the Azure, the OCI marketplaces. So all of the plumbing, all of the integrations were there with a common control plane that sat over it, that managed the. the deployments of the infrastructure, the pricing, the charge back, the discounting, integrated into Salesforce, integrated into licensing, and so he was building that product and then Vast came along and just bought that up, and now what we're doing is turning that into the Vast management layer for deployment across all of the hyperscalers. work is quite mature, but you know it'll go in domino where Google is first and then Azure AWS, maybe Azure next, you know, and so we'll get there. It'll just probably take a few more months.

[00:42:59.92]   RemoteYeah, yeah, so yeah, I think that I would, I would face it as such like for me. the priority of like, based on the things we spoke about, right, the priority would be like, let's get UK Met Office, MAI sort of story tied together, like last would be sales for me at this time, right now, just because of where we are in this sort of journey, but also because of like the 3P GPU sort of situation, at least right now. So you want to get the top-layer customers right now that are, that we know are getting GPUs.

[00:43:44.99]  Jason ValleryOkay, well here's my actions. I'm going to talk to Kushal. I'm putting together a PowerPoint deck right now that would show a hypothetical 1X, and across that, I will compare what it would need to deploy 1 exabyte of VAST on LXV4, LXV5 if it's been sold to us for next year, VAST on-prem, and then this is where it'll be a little dicey, but what that would look like for blob storage on hard drives and blob storage on flat, and when you have that sort of comparison table, I can… I wouldn't share this outside of the NDA and Microsoft vast world, but I think we can go and take that inside of Microsoft and share. These are the real economics of the situation and why vast on-prem is superior to all of the available Azure offerings and why we need to focus on a joint hardware way.

[00:44:38.40]   Remote- Actually, now I don't know. I think Nidhi backed out of supercomputing completely. I don't know if she did, but I think so. Otherwise, it would have been great if we--

[00:44:50.88]  Jason Vallery- Can I ask why--

[00:44:54.30]   Remote- Brought an engineering meeting.

[00:44:56.63]  Jason Vallery- Yeah.

[00:44:57.51]   Remote- And like brought her in and presented this. to her as well.

[00:45:03.17]  Jason Vallery- I mean, we don't have to do it at Supercomputing. I can come up and then we can have the conversation. You know, why on earth is Ignite the same week as Supercomputing? 'Cause I'm trying to double book that too.

[00:45:16.74]   Remote- Every year, every year, we are tired of this. Our team always gets torn between like Supercomputing. and Ignite. I know last year or the year before, like I had to literally run halfway through supercomputing, come here, present at Ignite. I'm like, it's ridiculous. Yeah. But I feel like, so yeah, I think the story is that Microsoft like things, IGNITE is a much broader conference for them. HPC is only one piece of it, so I don't think they think about marketing things about all this.

[00:45:57.44]  Jason ValleryI don't know if Nidhi was planning on IGNITE, if that was the reason she backed out, but you know, let me know if we can make that happen at Supercomputing. I'd love to pitch there. If not, I'll come up to Redmond and we'll have a conversation. and we can kind of look at it again.

[00:46:10.52]   Remote- Let's, yeah, let's do that, and I think let's tee it up with the Met Office story and everything, right? Like Nidhi is obviously one of the key stakeholders there as well. So let's tee it up and then plan a meeting with her.

[00:46:27.94]  Jason Vallery- Okay, sounds good to me. - Hello.

[00:46:32.44]   RemoteAll right.

[00:46:33.29]  Jason Vallery- How's everything else?

[00:46:34.12]   Remote- Yeah, no, same here, good.

[00:46:35.86]  Jason Vallery- How's the rest of your life going and everything else, you good?

[00:46:39.18]   Remote- Yes, yes, it's been good. It's been, yeah, it's been hectic overall, but yeah, my kids, kids are like 10 and 13, - Keeps me busy as well. Keeps me on my toes. My son is in these things like Science Olympiad and all of that stuff. So like, it's a lot of work outside of work.

[00:47:08.73]  Jason Vallery- Yeah, keeps us well balanced. My daughters are nine and 11 and I have a 19 year old in college. science major and that's the more like what it means to be a software developer in the future where we don't have software developers anymore like that's a whole wild situation. He's watching agent decoding come along and completely erase a discipline and he's sitting there studying in school I'm like I told you to go be a computer science major but I'm not sure that's gonna pay off. We'll see. I don't know what will happen there.

[00:47:41.51]   RemoteCool. Are you planning any trips to Redmond anytime soon?

[00:47:46.14]  Jason ValleryI will make one. I'm still working out my travel schedule. Jeff, the founder here, I report to him and he's got me on the road basically from now until Christmas. He's got me going all over the place. Dev team is in Tel Aviv, so I've been to Tel Aviv, but not since the conflict, so I'm like, "Really? I'm going to Tel Aviv? Okay." And then Yancey's team is all out in Iceland, so I'm going to Iceland, and then supercomputing, we've got an internal conference, we've got some other customer meetings, so I'm basically stacked up for the next several weeks of travel. But one of the key things that I certainly see is trying to make FaceTime with all the hyperscalers, and so I want to come and spend a few days in Redmond and reconnect with folks. I generally want to avoid building 43 in Azure Storage, though, because I don't think I'll be very welcome there. But everyone else, I'm like, the thing about leaving, right? It's like, everyone at Microsoft, I think, really appreciated me, except for my own team. So I will. support that team. Otherwise, I'll go meet with everyone. Yeah, no, definitely. Let's meet if

[00:48:51.50]   RemoteYou're around, and by the way, on for supercomputing, right, we do plan, there was a meeting earlier today as well. So I don't know if you know, Joe Green said from my team, like he was on Evan's team. He used to own the H series as the product manager for that. I know he's fun. my team. So he's organizing all the supercomputing stuff with Andrew this year. So there was a meeting earlier today also to discuss like what are we going to do with VAST both Ignite and supercomputing. So I know Andrew is going to be part of a panel. This is the one that to be in there, and Nidhi backed off, and now, because she's going to Ignite and presenting on the same day, so Andrew was already sort of plan B. Bass did a good job of keeping a plan B, knowing Nidhi's schedule, and then, like, I just got pinged to... do something on the VAST booth and then like VAST will present at our booth. In fact, we should probably connect before that as well to see like what story we want to tell together for VAST. I know Lear was gonna help on some of it, but I think it'll be good to have you.

[00:50:16.11]  Jason Vallery- I did get a note this morning that Igal wants a slide in his keynote about VAST, which is super exciting. So.

[00:50:24.76]   Remote- Yeah, yeah, yeah. So that was something that we were discussing as well. So yeah, I think.

[00:50:31.45]  Jason Vallery- I'll be to plug in and help where I can, and generally for the BD side of it, I'll let Lior leave. because I've got it up on my plate, and I'm very focused on how do we make the product work and, you know, the truths around that, so, but we'll tag team it. It'll be good.

[00:50:48.73]   RemoteSounds good. All right. Cool.

[00:50:51.73]  Jason ValleryTalk to you later.

[00:50:52.73]   RemoteTalk soon.

[00:50:53.81]  Jason ValleryBye.

[00:50:54.73]   RemoteBye.
```

<!-- ai:transcript:end -->
