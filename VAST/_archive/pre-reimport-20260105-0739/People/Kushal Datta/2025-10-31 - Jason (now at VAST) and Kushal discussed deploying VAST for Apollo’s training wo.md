---
type: "1-1"
created: { { DATE } }
status: "done"
counterpart: "[[Kushal Datta]]"
role: ""
team: ""
company: ""
series: "1-1/Kushal Datta"
cadence: "Weekly"
meeting_mode: "Video"
location_or_link: ""
calendar_url: ""
start_time: ""
duration_min: "30"
privacy: "internal"
ai_extracted: true
transcript_path: "00 Inbox/Transcripts/20251031 1235 Parallels Transcription.txt"
tags: [meeting, "1-1"]
---
``
# 1:1 — Kushal Datta — 2025-10-31

> [!info] Purpose
> Build trust, surface and remove blockers, align on priorities, coach & grow.

## Summary

Jason (now at VAST) and Kushal discussed deploying VAST for Apollo’s training workloads on Azure infrastructure. They compared options: Azure compute-based builds (not viable due to power/rack inefficiency), running VAST bare metal on Azure Gen9 Blob/XIO hardware, and VAST-qualified ODM hardware with C-node/D-node architecture. Kushal outlined needs at exabyte scale with ~120k GPUs per site, ~1–2 TB/s write and ~24 TB/s read, ~100 PB/day checkpoints, and tight power/rack budgets. Dallas HDD capacity arrives Jan; a larger April capacity is coming; Richmond was replaced. Plan is likely an apples-to-apples test on Gen9 XIO (Azure Storage stack vs VAST bare metal). Kushal will draft crisp requirements (throughput, capacity, power, rack) and explore swapping Dallas HDD to premium SSD. VAST can deliver ODM hardware within ~30 days once requirements are set, supports NFS, GDS, S3, and can add a Blob API if needed. Risks include Azure hardware qualification pace, internal politics, NIC/DPU choices (Fungible vs BlueField), and facility policies on third-party hardware.

## Key facts learned

- Jason moved from Microsoft Azure Storage to VAST Data to drive hyperscaler penetration
- Kushal is on Microsoft Apollo team
- Dallas capacity (HDD) landing Jan; larger new capacity expected April
- Richmond site replaced by a larger capacity site
- Target scale per site: ~1 exabyte usable (potentially ~7 exabytes for 350 MW site) and ~120,000 GPUs
- Checkpoint writes ~100 PB/day; peak write 1–2 TB/s; required read ~24 TB/s
- VAST offers single namespace, optimized NFS client, GPU Direct Storage, S3 API; exploring Azure Blob API
- VAST architecture uses C-nodes (compute/network) and D-nodes (flash) with tunable ratios
- Azure Gen9 XIO uses CX5 NICs (~40 Gbps), likely a throughput bottleneck
- BlueField-3 supported and BlueField-4 in progress; Fungible NIC can be qualified if required
- Azure compute-based storage SKUs (e.g., LSP) are inefficient for exabyte storage due to compute:storage ratio and power
- Planned apples-to-apples test: Azure Storage vs VAST bare metal on Gen9 XIO

## Outcomes

- Shared preliminary performance/power/rack tradeoffs for VAST on Azure hardware vs VAST ODM SKUs
- Agreed that read bandwidth needs likely drive a performance-optimized SKU
- Confirmed feasibility to ship VAST-qualified ODM hardware within ~30 days after order for April timeline
- Alignment to pursue an apples-to-apples Gen9 XIO test comparing Azure Storage and VAST bare metal

## Decisions

- (none)

## Action items (for Kushal Datta)

- [x] Draft and circulate a crisp requirements doc (throughput, capacity, power, rack tiles) to drive storage selection @Kushal Datta ⏫ ✅ 2025-11-08
- [x] Start an internal thread to assess swapping Dallas Blob HDD to Premium SSD and feasibility of running VAST bare metal @Kushal Datta ⏫ ✅ 2025-11-08
- [x] Provide detailed read/write throughput per GPU and final capacity targets (per site and aggregate) for ~120k GPUs @Kushal Datta ⏫ ✅ 2025-11-08
- [x] Prepare a proposal/BOM for VAST-qualified ODM hardware (perf-optimized vs capacity-optimized) once requirements are received @VAST Data (Jason Vallery) 🔼 ✅ 2025-11-08
- [x] Support and advocate for an apples-to-apples test on Gen9 XIO (Azure Storage stack vs VAST bare metal) @Kushal Datta 🔼 ✅ 2025-11-08
- [x] Stand up VAST bare metal on Gen9 XIO for the A/B test when scheduled @VAST Data 🔼 ✅ 2025-11-08
- [x] Determine DPU path and qualification plan (Fungible NIC vs BlueField) aligned with Azure networking requirements @VAST Data Engineering 🔼 ✅ 2025-11-08
- [x] Confirm whether a Blob API on VAST is required alongside NFS/S3 for existing data loaders @Kushal Datta 🔼 ✅ 2025-11-08
- [x] Scope and plan Blob API support on VAST if required @VAST Data Engineering 🔼 ✅ 2025-11-08

## Follow-ups

- [x] Clarify Azure storage offerings available in Jan and April timeframes for the target sites @Kushal Datta 🔼 ✅ 2025-11-08
- [x] Schedule a follow-up meeting after requirements are finalized @Kushal Datta 🔽 ✅ 2025-11-08

## Risks

- Azure hardware qualification and procurement timelines may delay needed SKUs
- Internal politics within Azure Storage (competing stakeholders) could impede VAST adoption
- Dallas hardware may be locked to HDD, limiting performance
- NIC/DPU constraints (CX5 40 Gbps) may cap throughput on Gen9 XIO
- Overlay/multi-tenancy networking on DPUs may require additional engineering
- Facility policies may restrict third-party ODM hardware deployment
- Power/rack constraints can strand capacity or limit GPU expansion

## Open questions

- Can Dallas storage be switched from HDD to Premium SSD in time without impacting schedule?
- Will Azure permit VAST to run bare metal on Gen9 XIO clusters in production?
- Will third-party VAST-qualified ODM hardware be allowed in the target facilities by April?
- What are the exact per-GPU read/write targets and final exabyte capacity per site?
- What are the definitive rack tile and power budgets per site?
- Which DPU/NIC path will Azure require (Fungible vs BlueField), and what overlay/multi-tenancy features are mandatory?
- Is a Blob API on VAST a hard requirement given existing loaders, or will NFS/S3 suffice?
- What is the timeline and ownership for the apples-to-apples Gen9 XIO performance test?

> Next meeting (if any): (none)

---

<!-- ai:transcript:start -->

## Transcript (auto)

```text
[00:00:00.04]  Jason Vallery- Good to see you, how are you doing?

[00:00:03.18]   Remote- I'm doing good, I'm doing good. I think that overall the Falcon 1 is delivered. People are using the capacity great to see. So I think a lot of the work that we did is seeing results now. So anyway, I think we have started training models. How are things going with you? Vast, huh?

[00:00:26.06]  Jason ValleryYeah, so I'm going to jump over. I mean, you know, I think we talked maybe around May or so, but Azure Storage Organization was and is kind of a pain point. Like the leadership changes over there. I don't know, I don't need to drag anyone through the mud, but you know, my champion, my sponsor was a guy. name Juergen Willis. I don't know if you ever came across him. He was the CVP of Azure story up until like 18 months ago, and he retired and kind of maybe more got pushed. There were some political things, and so after he left, I didn't really have a good champion in the org, so I was looking for ways out. Worked a lot with folks that passed in the past. Glenn, I don't know if you've ever met Glenn Lockwood, but he and I worked really closely at OpenAI. He left in July and came over to Vast, and so I started having some conversations over the summer. I took my Microsoft, you know, MSAA sabbatical because I'd been there long enough. I took the summer off, and then, you know, they made an interesting offer for me. I made the jump, and now I'm over here, so I'm running product management. for the cloud. It's actually broader than that. It's really like, how does VAST penetrate the hyperscalers? What are the product improvements that need to happen? How do we get to like frontier model builders at scale with exabyte class namespace stuff and build a, you know, marketplace offering on top of AWS, Azure and GCP? So there's like a lot baked into that. and yeah I mean our worlds are colliding because literally my last call was with the AKS team so Chi I don't know if you are working with her yet but yeah we literally had five minutes ago dropped off a call with her because you know obviously we need to help out on the Apollo side. I haven't stayed at Microsoft funny I would have been in would have been architect for, I don't know if you've worked much yet with the Apollo team on the storage side, but like Jay Menon and figuring out what Microsoft was going to do to meet the storage requirements of Apollo.

[00:02:28.12]   Remote- I'm working with them. I'm one of the Apollo team members.

[00:02:31.84]  Jason Vallery- Well, there you go. We would have been on the same team had I stayed and it sounds like maybe it would be on the same team, but I'll be on a different app. I mean, she just said, I don't know, maybe all over spill and share beans, I shouldn't, but she just sort of dropped on us like, what would it look like to just drop VAST on top of an Azure Storage Cluster bare metal? Well, let's go figure that out. So share with me what you can, tell me how we work together and how VAST can help.

[00:02:56.46]   Remote>> Okay. Well, I. what do you know like so here's the thing i would love a shared file system view and the view that we have in the conduct clusters with core weave is still one of our best clusters ever having said that i think we have many discussions on the single points of failure right so vast metadata server field or something and it it has taken time. I mean Corvue does a massive amount of work to support us so it has been you know disruptive but I think it has been contained. Question is that how do I alleviate those because Girish keeps on telling me you have the storage hardware you can drop in any file system you want. Is that because Manish tells me that's not the case. So I hear these conflicting things and then in the midst of this all, Fungible has come in and Pradeep is like, all this is bullshit. These guys are giving you miniscule bad news.

[00:03:59.43]  Jason Vallery- Okay, so let me show you a slide, and I, well, I mean, I'll show it to you. I think there's some, a lot to unpack. First I'll point out is that, The current Gen 9 Azure storage hardware, the flash hardware, well, let me back up. Which hardware are you referring to when you say, "Garish says you have the storage hardware, you can use whatever you want"? What are you referring to?

[00:04:20.81]   RemoteNo, I mean, Phoenix was hardware, HDD based. Let's say Falcon 2, which is Dallas, if that becomes a, that is indeed a, this is a HDD but have you heard about this larger deal? I don't know if she told you about or not.

[00:04:37.37]  Jason Vallery- She didn't mention a larger deal, but I knew you guys were getting capacity in Dallas and Richmond before I left.

[00:04:43.64]   Remote- So Richmond is now off the table, been replaced by a larger capacity. That site, we are planning the storage the conversation is in that we will have premium HDD the throughput requirements that we have premium SSD right so sorry premium SSD my bad premium SSD and we have I think the in DC local storage capacity is a question we can preferably preferably have that whole data archived in the storage that we have in Dallas and Phoenix. So in that scenario, what about a vast interface or vast file system there? That's what I'm thinking.

[00:05:32.24]  Jason VallerySo, I mean, there's a few things to unpack. The first point about, and I don't know, did my screen share? see something? I don't have teams to this table. Okay, so there's a bunch of different ways we could deploy this. The official Azure solution, which is painful as can be, is actually deploying on top of Azure Compute, and you asked me about this in our chat the other day. The LSP for instance and the LSP coming. LSP5 instance next year just make no sense because of the compute to storage ratio. I mean in example what I'm looking at here is what does it take to get to a usable exabyte of capacity and what is the associated performance. You're talking about 1700 racks of compute to deliver one exabyte of current Azure Compute offerings that are storage dense. That doesn't even get better next year substantially where it goes from 1700 to 300 racks and it's still 8 megawatts of power. So in my mind, an Azure Compute-based solution makes no sense for VaST on Azure any time in the future. I don't have the flash numbers in. here, but Blob HDD Gen 9 is the stuff that you guys got in Phoenix and that's kind of like what you ultimately look at is, and you're well aware of these numbers, I've shared them with you in the past, to get to a usable exabyte you're talking two and a half megawatts of power and you're talking about 180 racks of capacity. The thing that blew my mind when I came over here is just the numbers around the VAST ODM hardware, and so the thing about VAST is that actually it's a software platform, it's not a hardware platform. VAST partners with a variety of different manufacturers and can configure hardware SKUs in a variety of different ways based on performance criteria, capacity criteria, and the various different white label ODM that they can go partner with, like, you know, HPE, Supermicro and others. But, you know, a couple of canonical reference examples of ways that clusters could be configured are the far-right columns, perf-optimized and capacity-optimized. If you go capacity-optimized, you can fit an exabyte of capacity in 21 records, and more importantly, one-fifth of capacity. power of hard drives. So you can get very dense, and even when you like compare the performance characteristics between what you're getting from Blob HPD and Vast's capacity optimized queue, it's still double the performance on read and a bit better on write. So that is like capacity oriented, and then if you switch to the performance oriented, there in that set of representations in that column is NVIDIA's reference architecture. So this is what NVIDIA says is the right ratio of throughput per GPU per petabyte in a one exabyte cluster and then yeah it's similar in terms of the power characteristics of blah but it still is half the rack count and obviously way better performance in terms of how much you're getting, and then I'm sure maybe the capacity optimize or are you still talking about the performance of the tool so like if you look at this like what I would say is if you look at the megawatt numbers for capacity compared to the performance optimized queue you know these are it's 5x so you're kind of in line with what blob HDD does. Oh I see, makes sense. So this is Cloud HD, this is a performance, this is like the NVIDIA reference architecture of how we would deploy VAST for performance optimized, and then this is like the high density version of what we could do with VAST. You know, if we really wanted to squeeze this down in terms of racks and power, you can still get your exabyte. Like, I guess maybe what I wasn't clear of is all of these columns represent. a different hardware type, what would it take to get to 1 exabyte of usable capacity? And so, you know, what we've got is, I think, this solution still beats the perf you're getting on blob storage with 1/5 the power and, you know, whatever that is.

[00:09:42.95]   RemoteI see. Okay. ISO usable capacity, the benefit is really in the power and the total performance that I'm getting in between these two SKUs.

[00:09:55.05]  Jason ValleryRight. So, we could deploy, and really what it is is that VaST has this concept of C nodes and D nodes, and C nodes are where all of the compute and network traffic get terminated, and D nodes just a bunch of flash that are connected over NDM over fabric and so you can change the ratio of how many C nodes you want and how many D nodes you want based on what your performance targets are and then you can even sub out on the D nodes a much higher density flash module that increases that density even further. So to usable capacity as your primary decision frame, you can go and do that in a much more dense way than even the NVIDIA reference architecture and still probably hit the performance goals that you've had. It's kind of the key message. But what I don't have in here is the BLOB Gen9 XIO flash cluster that I'm sure Manishan could are pitching you. What I can tell you just based on my own knowledge of those is that they use CX5 NICs, so your throughput limit is fundamentally the network path because they're, I think they only have like 40 gigabit NICs on them. So we could go deploy BAST on a Gen 9 XIO cluster and that's what Gee just asked us to do and we'll do that, but it's not... going to be the same as had you gone with Bluefield plus a vast configured Cnode/Dnode qualified SKU that has the characteristics I just showed you in that table. So, but you'll probably beat the pants off of Azure Storage. I'm confident in that on the same hardware for hardware apples to apples kind of shootout. So, what are your goals, like how much capacity do you need, what are the throughput goals, and you know, that's going into this Dallas cluster?

[00:11:49.44]   RemoteOh, do we have possibility to change things in Dallas cluster, because I think they are really close to the time, right? Dallas, the first Dallas instance is coming. coming in Jan, so I think that's already started to rack and stack.

[00:12:04.05]  Jason Vallery- This is premium? This is the SSD cluster?

[00:12:07.09]   Remote- No, this is HTT, Dallas is all HTT.

[00:12:09.85]  Jason Vallery- Yeah, okay.

[00:12:10.69]   Remote- I wonder how much flexibility I have to make it to, well, that's a separate conversation.

[00:12:15.37]  Jason Vallery- The question--

[00:12:16.21]   Remote- I'm talking about this separate--

[00:12:17.59]  Jason Vallery- Back to George's team, my predecessors, but like, if you could swap out blobbing-- HDD for blob premium there, if that's an interesting option for you, and then we could, we could then pave those clusters and run VAST bare metal on them.

[00:12:32.89]   RemoteI see. Okay. That's a, I'll, I'll start a thread on that internally to figure out whether that's possible, and then I will involve VAST. I think at the moment, I just don't know how much of. that will impact our schedule, but interestingly, the other place I have, that's where I'm thinking because there we are power constrained and I would love a performance optimized where I get this much bandwidth of read and write. So, these are cumulative, right? I think this aligns very well. The performance-optimized numbers you're showing for a 2 petabyte, sorry, 2 exabyte, I think it aligns with what my demands are.

[00:13:24.02]  Jason ValleryThe, I think maybe Vipin's now aware of this. I think in that table, I'm showing a two-to-one So it's a, you know, when you think about this, you're saying if about 1.3 exabytes of raw disk, then when you erase your code that it's down to 1 exabytes of usable capacity, and then vast has some really powerful that Azure storage has none of this deduplication and differenciation of the resources. that allows you to even do further data reduction, and so we looked at the Condor cluster and looked at what the data reduction ratio is. You're getting like 1.7 something to one reduction on that. So if you think you go 1.3 to one for usable, and then you can bump that up to about 1.7 after data reduction, effective capacity.

[00:14:15.42]   RemoteGot it, got it, got it. Okay. Makes sense, makes sense. So we will have VAST in Apollo. Is that kind of determined or we are exploring?

[00:14:27.74]  Jason ValleryI mean, I think you need to go advocate for that. What I, the takeaway I got from that call I was just on is that they're going to do an apples to apples shootout. So I mean, I'm reading between the lines here, but what I imagine is going to happen is there's going to be a Gen 9 Azure Storage XIO cluster spun up somewhere in a lab. They're going to performance test that running the current Azure Storage software stack, and then they're going to pave it, run VAST bare metal on it, performance test the same hardware with the VAST software on top. to use that as ammunition to make a decision.

[00:15:02.75]   Remote- I see, okay, okay.

[00:15:05.51]  Jason Vallery- But I can tell you, we don't (indistinct) but you know, we still should prove it out, right? I mean, but I think there's an internal politics game you're facing and that she is facing because Maneesh is obviously not gonna want that to happen.

[00:15:22.96]   RemoteAt the end of the day, the number should matter. The interface has been, so this is a consistent question to me that, what interface do you want? I mean, it's such a weird question, right?

[00:15:34.94]  Jason Vallery>> What I'll tell you, you get with VAST is single namespace that you can access with the highly optimized NFS client. and get GPU direct storage today, like that's already in the product, and you can access that same data estate using theinaudible

[00:15:55.40]   Remote>> The GPU direct storage is in the product.

[00:15:58.03]  Jason Vallery>> Look, we're talking about building a Blob Storage API on top of Vast. So if you came back to Vast and said, "We want Blob API as well as that's already there faster build that for you quick.

[00:16:11.59]   RemoteI think that's a good because you know to support Azure blob. We appended our whole, you know, framework, data loaders, everything to blob now that has been a significant amount of work, but but it works at the moment it's performant it works. That's the reason it's a weird question to me because two months ago, I'm not saying you, but you know, I just said, hey, change everything to blob. Now I did there like, which API do you want?

[00:16:42.02]  Jason ValleryYeah, I mean, I think that's a question. We're for a variety of reasons, we're considering building a blob API on top of Ass today, and you obviously already get all of the S3 API today, which is where all of the other frameworks and tools support that today. So, you know, you get the best of both worlds at VAST. Obviously, Azure Storage doesn't have that today.

[00:17:06.71]   Remote- Yeah. Okay, cool. I got it. I got the message. What else? I think this has been very, very useful for me.

[00:17:15.47]  Jason ValleryYeah, I mean, obviously we're trying to get to a point where a vast optimized hardware SKU gets qualified by Azure and can be just generally deployed based on capacity needs. So, you know, any advocacy that you have within your forums to help us push for that is useful because ultimately the current Azure storage SKUs, even if we deploy vast bare metal on Gen 9 aren't going to be that impressive compared to your experience on CoreWeave. Azure is just so slow in qualifying next-generation hardware. I think the next key part of that is what happens on the DPU side. Obviously, Pradeep and Jay and everybody are going to be pushing the fungible NICs. If that's the path forward, okay. but we need to help on the VAS side qualify the fungible NIC and figure out how we leverage it. I'm sure we can get our engineering teams lined up to do that. On the other side, obviously, we're aligning ourselves to NVIDIA's reference architecture and already support Bluefield-3 and are working on Bluefield-4 with NVIDIA, and you're going to get a well-proven path going that direction.

[00:18:22.99]   RemoteSo the NVMe Fabric client that actually runs on the Bluefield now, it's not going to run on the host?

[00:18:29.42]  Jason ValleryWell, that's the, so this is one of the topics that just came up is the NVMe over Fabric client today, like there's no multi-tenancy in the way these things work in most places, right? So you, we don't have to program the DPU to set routing paths and our, you know, isolate network paths and so forth. There's no overlay network. So when VASP runs out of Bluefield 3, we're using NVIDIA's reference design, DPU offload, and VM over fabric. If we were to go and put this into Azure, then Azure's got this entire overlay network, and then there's all this programming that has to happen on the DPU to support packeting. absolution, overlay, and all of that. If we have to go down that path, that's engineering that BaaS needs to do. But the only reason you do that is because you're trying to solve or allowing multi-tenancy and network isolation between tenants.

[00:19:20.81]   Remote- Yeah, yeah. For me, I don't think multi-tenancy is really not the top of my mind, but I see what you're saying. Got it. Okay, so from the advocacy point of view, I think for me, then the big capacity that's coming that's on top of my mind. I will see how much of this will be reasonable. I think the slowness in Azure is the point. Is there any way I can do to make it faster? In what way? Can you help there if need be?

[00:19:53.03]  Jason ValleryMake the existing hard drive capacity faster?

[00:19:56.82]   RemoteNo, have like the, if let's say we want to have vast in that new capacity, that's still being built, so there is some time there, and then if we decide to buy the storage hardware that you are proposing, which one will the

[00:20:15.61]  Jason ValleryWould that be? Yeah, I mean, so what we could do is, if you came to us with capacity and performance requirements, we could put a proposal together to ship you ODM hardware that VAST is qualified, and I'm sure if you're talking about January, I'm sure within that timeline we can get the hardware to you. It's a matter of you getting the institutional will to let third-party hardware go into that facility and be able to connect it up.

[00:20:38.05]   Remoteup? Oh, not January. I'm talking about April. The capacitor I'm talking about is not coming in

[00:20:43.55]  Jason ValleryJanuary, but April, yeah. Oh, I mean, we can get hardware, like, within 30 days from an order, typically. I think that we partner with, like, Solidigm and Micron, so we would have to obviously go talk to the vendors to make sure we could pull it off, but it's not the kind of timeline. that you're familiar with in terms of supply chain issues and getting public qualified. But it's also, it's ultimately like, can you get the organizational, do you have the organizational pull to get your people into these facilities?

[00:21:13.26]   Remote- I can make that happen if I can, if I see the value though. So I need to go back and so I know the requirements pretty well I think this meets it when you say organizational value you mean like so the problem that will be there Azure Stack wouldn't work in this Azure Blob Stack wouldn't work is that true or no?

[00:21:41.46]  Jason ValleryWhat's the what's the required give me a give me a capacity number and a performance number that I can work with.

[00:21:46.56]   RemoteThe capacity would be in the range of, let's say. Yeah, I would I would. say in the range of exabyte or exabyte per if I say that is per site then yeah so the I'll give you more detail at the the I have not fully done the analysis. I have the analysis per model requirement, but I need to close on the total capacity requirement. It comes to me something like seven exabytes in that site for the first 350 megawatt. So I have to go back and see whether I was thinking of optimizing it, not have super high bandwidth. to the Blobstore right to this DC local capacity, whatever that is, which is all premium SSD, have high bandwidth there, and then, you know, I can keep backing up my checkpoints into the Blobstore periodically. That model, I think, will work.

[00:23:13.16]  Jason Vallery- So you then, in that world, performance optimized SKU to--

[00:23:18.25]   Remote- Correct, not at capacity, that's right.

[00:23:20.03]  Jason Vallery- What's the GPU throughput requirement then? How many GPUs and how much throughput per GPU are you looking to achieve?

[00:23:27.71]   Remote- Correct, yeah. - Do you have a number? - Oh, you're asking the question.

[00:23:32.27]  Jason ValleryI, can I tell you though? I can check. - Let me know what you can tell me, I don't. - I mean, the summary point is in that timeline--

[00:23:41.51]   Remote- So roughly around, I can give you a rough number. So it's roughly around 120,000 GPUs.

[00:23:46.92]  Jason Vallery- Okay, in one site? - Correct. - You want to check for 120,000 GPUs, and then what's the ratio of read per GPU, write per GPU, and terabytes per second?

[00:23:59.16]   Remote- Yeah, so, yeah. I'll tell you so it's not true that all hundred twenty thousand GPUs are going to write at the same time we have some laxity there right all grow ranks are not going to write so the largest the total bytes written on checkpoint is roughly in the order of 100 petabytes okay in a day per day

[00:24:23.32]  Jason ValleryBut so what's the peak throughput that you need to make that happen? Are you staging them on the GPU hosts first and then copying into this storage or?

[00:24:31.59]   RemoteThe peak write bandwidth I need per 100,000 GPU is roughly around one petabyte per one petabyte per second.

[00:24:42.79]  Jason ValleryPetabyte per second? Yeah sorry that is that is not uh that hold on. I would expect like eight to ten terabytes per second kind of frame of mind.

[00:24:56.02]   RemoteUh hold on hold on the yeah so sorry sorry that that was the that was some of the bytes not the throughput. Okay, let me give you the throughput. - The throughput will be something, the right throughput would be something in the order of, so if it's that right bandwidth required, yeah, sorry, in the order of, I would say one to two terabytes per second.

[00:25:26.53]  Jason Vallery- Oh, that's very, so I think, you know, you're likely to be able to get to that with Azure Gen 9 hardware. Depending on how much of it you deploy, the problem will be the density because the Azure Gen 9 hardware is, uh, I mean, it's like 16 terabyte flash. Uh, and so I, you know, back in napkin in my head, if you're saying you. on a hundred petabytes of that, you're probably looking at like a hundred racks or something like that.

[00:26:00.83]   Remote- Which, yeah, so your write bandwidth is pretty good. The read bandwidth is not going to match on the capacity optimized. The read bandwidth required is in the order of 24 terabytes per second. So that kind of falls. where your read bandwidth perf-optimized SKU is at. That's the determining factor here, not the write. Write is substantial. I think either will fit.

[00:26:29.81]  Jason VallerySo, I'm confident we can build a design that will beat Azure Storage every day of the week. What do we do as next steps to make it more formal and helpful?

[00:26:38.15]   RemoteI really need to understand the organizational thing that you just mentioned because, I mean, you know, right, it has happened before that. I wanted premium storage, sorry, SSDs, but that didn't happen. We had to fall back to HDDs because that were kind of the only hardware that was available at the time frame. So what is that? the Azure storage offering in that timeframe is not very clear to me. So I have to get that data and once I have that, then I can, you know, then I can make a call that which serves better.

[00:27:12.78]  Jason ValleryWhat I would recommend you do is really write up the CRISP requirements in terms of throughput capacity and power availability. So basically say I need this much throughput in this much capacity, and here's how many rack tile locations I'm willing to sacrifice and how many megawatts I'm willing to sacrifice to get there, and bundle that up in a way that you can evangelize it with Manish, Ong, Kui, Qi, and just say, "Hey, this is the real world requirements, give me a storage solution that solves this.

[00:27:49.52]   RemoteThat's what I'm doing at the moment, correct.

[00:27:53.97]  Jason ValleryYeah, but I think you should be opinionated about the power envelope you have to work with because, you know, you don't want to, you're ultimately sacrificing GPUs for every inefficient deployment you make, and I'll tell you, Jason, the amount of

[00:28:08.23]   RemoteThe power that I strain on Phoenix is just mind blowing because there I. Azure cannot give me a way to scale my GPUs into the strain power. I have like 4 megawatts sitting idle. There's nothing there.

[00:28:24.05]  Jason ValleryJust mega watts. Can you imagine that's what so you can't put any more GPU pods in it or you can't?

[00:28:30.70]   RemoteI cannot put more GPU pods in it and because we are, we don't have enough room to put IVE mods. Oh, so that's the problem.

[00:28:40.46]  Jason ValleryPut some CPU, you connect it for some other resources, you can put more storage in it, I guess.

[00:28:45.00]   RemoteBut then what's the point? It's not going to be used, right?

[00:28:48.81]  Jason ValleryYeah. Oh, it's a bummer.

[00:28:53.46]   RemoteBut that's the situation I want to avoid because it is possible in this new SKU that we are more power constrained because their design is locked in space. The non-negotiable here is that the GPU design that they have, they have, yeah, that won't be changed, and they didn't, they, these guys. design the system or data centers for inference, not for training. So they do not have much power for storage or general purpose. It's minuscule. So I'm trying to work with them to figure out what is reasonable and that's what I'm trying to get to, yeah.

[00:29:31.32]  Jason ValleryWell, let me know how I can help. So I can give you those numbers once I have them. another call. Really great seeing you. Really exciting opportunity. It's going to be a fun project and FAST is certainly excited about it. We've got the engineering muscle. We can turn things around quickly. So just let us know what you need, and say hi to John, John Mill, because

[00:29:54.38]   RemoteYou know, we keep on running into each other in conferences but never get a chance to say hi or Satan talks, so yeah.

[00:30:01.95]  Jason Vallery- I will mention that, and I think, Asby, you're not going to supercomputing?

[00:30:06.14]   Remote- No, not this time. I won't be.

[00:30:08.77]  Jason Vallery- Bummer. - Okay, well, sounds good. Stay in touch. Talk soon.

[00:30:13.07]   Remote- All right, you too. (keyboard clacking) you
```

<!-- ai:transcript:end -->
