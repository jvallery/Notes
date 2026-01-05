---
type: "Partners"
title: "VAST–Microsoft alignment on Nebius MAI storage"
date: "2025-11-20"
partner: "Microsoft"
folder: "Partners/Microsoft"
participants: "Lior, Bilal, Jason Vallery"
tags:
  - "type/partners"
  - "partner/Microsoft"
source: "00 Inbox/Transcripts/20251120 1259 Parallels Transcription.txt"
---

# VAST–Microsoft alignment on Nebius MAI storage
**Date:** 2025-11-20 · **Partner:** Microsoft · **Folder:** Partners/Microsoft

> [!summary] Executive Summary
Microsoft (Bilal) and VAST (Jason, Lior) aligned on storage options for MAI’s large-scale Nebius deployment (~100K–120K GPUs). MAI strongly prefers file-based storage with NFS/RDMA and GPU Direct Storage; Azure Blob has forced tool refactors and lacks required protocol/performance features. VAST outlined its software-defined platform (file and object) with NFS over RDMA, S3 over RDMA, and GDS, plus tunable compute/data node ratios to meet per‑GPU throughput targets. Microsoft’s current plan-of-record is ~1.6 exabytes all-flash across ~400 Gen10.3 racks delivering ~192 Tbps; an incremental or pivot path to VAST is under consideration. Network integration was discussed: if VAST can sit on the physical GPU front-end network, Sirius overlay gear (and cost) could be avoided, pending security/compliance. VAST can integrate with AAD, provide a dedicated management plane, and will size clusters once MAI confirms per‑GPU throughput and capacity. Near-term steps: Bilal will debrief MAI today, coordinate a three-way engineering workshop, and explore VAST participation in the early‑December site survey. Suresh will act as DRI while Bilal is OOO in early December.

## Alliance Context & Key Facts
- MAI prefers file-based access; Azure Blob creates friction for their tooling.
- VAST supports NFS over RDMA, GPU Direct Storage, and S3 over RDMA.
- NVIDIA is increasing per‑GPU storage throughput requirements each generation.
- Microsoft POR: ~1.6 exabytes all-flash, ~192 Tbps total, ~400 Gen10.3 racks (~15 kW/rack), CX7 NICs.
- VAST can tune compute (C) vs data (D) node ratios to hit throughput/capacity targets.
- VAST deduplication can increase effective capacity (observed ~1.7x at an MAI cluster).
- VAST offers a full management plane and can integrate with Azure Active Directory.
- VAST is not yet an Azure hardware provider; Marketplace on Lsv4 is not viable at this scale.
- Potential cost savings if VAST connects on the physical GPU front-end network (bypassing Sirius overlay), pending approvals.
- Early December on-site site survey is planned; VAST requested inclusion.
- Bilal is OOO roughly Dec 3–16; Suresh will be DRI.
- An internal bake-off comparing VAST and Lustre on future Azure hardware is underway.

## Outcomes (Alignment, motions, artifacts)
- Shared POR numbers and rack/power profile for the current Blob-based plan.
- Agreed that MAI requirements (per‑GPU throughput, read/write mix, capacity) will drive VAST sizing.
- Identified integration path to avoid Sirius overlay if security/compliance permits.
- Aligned to set a three-way workshop (Microsoft, MAI, VAST) for requirements and site design.
- VAST requested participation in the early-December site survey; Microsoft to explore agenda space.

## Decisions (Ownership, gates, handoffs)
- Suresh will serve as DRI while Bilal is out in early December.
- Proceed with a requirements-first approach, followed by site design and a site survey.

## Risks (channel conflict, roadmap gaps, certification)
- Plan-of-record for Blob is already in motion; pivot or supplement may face program gating.
- Uncertain ability to place VAST on the physical GPU front-end network; security/compliance approval required.
- Network topology details (front-end/back-end, non-blocking across data halls) not yet confirmed.
- Supply chain timing for large flash volumes and qualified hardware may constrain the 2026 ramp.
- Rack adjacency/row isolation preferences may conflict with early 2026 space constraints across 14 data halls.
- Owner availability risk: Bilal OOO in early December during critical planning window.

## Open Questions
- What are MAI’s exact per‑GPU throughput targets (read/write) and usable capacity requirements by tranche?
- Will Microsoft deploy VAST on Azure storage hardware or bring qualified VAST ODM hardware?
- Can VAST be allowed on the physical GPU front-end network (bypassing Sirius), and what security controls are required?
- What is the confirmed site survey date and attendee list in early December?
- Is the Nebius deployment location Dallas, New Jersey, or multiple sites; how does that affect logistics?
- What are the detailed Gen10.3 hardware specs (rack counts, NICs, power per rack, usable PB per rack)?
- Is the inter-hall front-end network non-blocking at the required throughput for storage traffic?
- Will MAI want Blob–VAST tiering or API compatibility (e.g., Blob API over VAST), and what is the priority/timeline?

---

## Joint Action Items
> Express ownership in the line (e.g., “Partner: …” / “Us: …”), add due dates `📅`, and use priority `🔺⏫🔼🔽⏬` as needed.  
- [ ] Debrief MAI today on VAST option and validate file-based, per‑GPU throughput, read/write, and capacity requirements; confirm pivot vs supplement posture. @Bilal 📅 2025-11-20 🔺
- [ ] Share VAST sizing examples, performance/capacity design options, and management/API documentation with Microsoft (Bilal, Suresh). @Jason Vallery ⏫
- [ ] Schedule a three-way technical workshop (Microsoft, MAI, VAST) to capture requirements and draft the site design. @Suresh ⏫
- [ ] Confirm Nebius front-end/back-end network topology and whether storage can attach to the physical GPU network without Sirius overlay; document security/compliance controls. @Suresh ⏫
- [ ] Provide detailed Gen10.3 POR specs (rack counts, CX7 NICs, power per rack, usable PB, total Tbps) and Sirius overlay limits. @Bilal ⏫
- [ ] Validate VAST supply chain and lead times for 2026 ramp (flash, C/D node quantities) and propose tranche sizing aligned to MAI dates. @Jason Vallery 🔼
- [ ] Coordinate VAST participation in the early‑December Nebius site survey and align agenda time. @Bilal 🔼
- [ ] Decide deployment model (Azure storage hardware vs qualified VAST ODM hardware) with pros/cons, cost, and performance implications. @Suresh 🔼
- [ ] Draft rack adjacency/row allocation plan for VAST given constraints across 14 data halls. @Suresh 🔼
- [ ] Align on deduplication planning assumptions to set effective capacity targets for MAI datasets. @Lior 🔽

### Follow‑Ups
- [ ] Send meeting notes and VAST design tables to MAI stakeholders. @Jason Vallery 🔼
- [ ] Confirm the exact site survey date, location, and attendees; circulate logistics. @Bilal ⏫
- [ ] Book in-person workshop (Redmond or site) with Microsoft, MAI, and VAST engineering. @Suresh ⏫
- [ ] Introduce Kajan and other stakeholders into the working thread and invite to the workshop. @Bilal 🔽

### Next Check‑in
- Next meeting (if scheduled): **(none)**

---

## Task Views (this note only)
```tasks
not done
filter by function task.file.path === query.file.path
group by priority
sort by due
```

## Original Transcript
[00:00:22.50]   Remote(keyboard clacking) I don't know if you can see it, but we're going to have a Q and A session in just a minute. So, if you have any questions, feel free to ask them in the Q and A session, and we'll be back in just a minute. Thank you. Thank you.

[00:01:17.84]  Jason Vallery>> You are, can you hear me?

[00:01:25.91]   Remote>> Yes, yes I can.

[00:01:28.75]  Jason Vallery>> Excellent.

[00:01:30.05]   RemoteExcellent, excellent. It's only us, right Jason?

[00:01:40.38]  Jason ValleryNo, well, us and two different note takers, whoever those are, Zoom and Vast Data Note

[00:01:45.30]   RemoteTaker. Yeah, yeah, I saw that, it's so strange, like we have both working with us.

[00:01:52.78]  Jason ValleryOr maybe against us. We have to do you know we're two days up. Yeah, I was keeping us on track

[00:01:57.47]   RemoteSo either way while we wait I have a meeting in about a few hours with one of the KBB They saw the blackmail people at Microsoft some of them didn't attend dinner with you guys last night any advice What I want to get out of it Okay, he's joining, we'll talk about it later, he's joining, he reports to Quartz. Okay. Whoa.

[00:02:24.12]  Jason ValleryHello, hello, Jason, how are you doing?

[00:02:28.03]   RemoteHey, it's been a while.

[00:02:31.03]  Jason ValleryHow's it going?

[00:02:32.37]   RemoteYeah, it is, but I don't know that I knew for sure that you had left, so.

[00:02:39.03]  Jason ValleryOh you didn't. I'm sorry that I didn't send a note. Yeah I left at the end of June on to sabbatical. Came back from sabbatical and then turned around and actually left and joined VAST

[00:02:49.70]   RemoteAbout a month ago. Got it. So I knew about the sabbatical and so I knew you were kind of out for that and then I think I missed the other piece but no that's great. Congratulations. It's great to see, great to be able to connect with you, so that's a good thing.

[00:03:05.40]  Jason ValleryYeah, it sounds like we're going to get to keep working together, rumors that I hear. Yeah. Tell me what's going on.

[00:03:11.37]   RemotePossibly, yeah. Yeah, I'm coming into this fairly cold. I tried to get an opportunity to review a little bit of this yesterday, but I didn't get a chance. So, yeah, I'm coming in soon. Super, super cold just because child has mentioned it to me over the last couple of weeks like hey, let's look at bass. Hey, could we do fast here and I'm just like I have no idea so looks like it came full circle and he connected with you and he had you connect the dots to get with me.

[00:03:37.56]  Jason ValleryAnd so yeah, we can kind of go from there. Do you want to share any of what you know, Lior, or how we start this?

[00:03:48.42]   RemoteYeah, so we met with Nidi yesterday and she dropped the bomb that she's leaving at the end of the month. I guess it's not news for you, and then I asked her, so who do we follow up with? And that's the intro came to you. So, the way I understand it from yesterday, there was a decision that was made for MAI of consuming one of the NeoCloud's GPUs on a project that is going to be effective immediately. I mean, it's a fast-forward project. values right and in your cloud and it's going to be in the New Jersey Data Center and The numbers I heard about the GPU scale. There is something around 100 plus thousand two GPUs and What ma is asked for again? This is all based on the conversation. I said it would maybe is since you know since it's going to be outside of Microsoft, they want it to be vast. That kind of goes along the same background and satisfaction that they have with us by using us indirectly at Core for many, many years. So we decided that we connect, where we kind of get to work with you to understand the the requirements like. basically you know what is required on performance, on capacity, on scale, on timeline and get to understand the data center. I think it's a power-cooled data center so for us to suggest the right bill of material that will fit the bill for these needs all the way to creating the bill of material and pricing so there will be clear kind of pricing behind it, a solution, pricing, and everything, and she also suggested that we'll work with you to to connect with MAI to understand what other requirements or what other things should we do on engineering to engineering collaboration to make it ready the way it needs to work when they are in production. One topic was mentioned as an Maybe adding so we have a much how much how much you know of us by the way. I know I don't know anything about this Okay, so we need to do the vast education as well, right? But right now let's just assume that you know of us but adding as you blob interface to vast to enable ease of data movement between Azure blob into that data center and into the vast system so so again An open kimono discussion with them and she dropped up the fact that there is a side survey happening I think on the first week of december And so she already asked if we can be a part of the site survey so we can again Add to eliminate any showstopper if any And that's give or take the story. So, um Everything is on in your lens simple no pressure no pressure at all. No, I thank you for that overview. You definitely, you're well-informed, so no corrections on sort of the overview of the NEBIUS program and sort of the plan of record right now with it being Azure Blob and sort of we are talking about a supercomputer of roughly 100K GPUs, maybe a little more than that, and so, yeah, right now, what we've designed, we've designed a SSD solution, first party Azure storage or a blob to accommodate MAIs like current requirements, which are somewhat evolving. They're thinking about future workloads or future model training in the current requirements probably not being up to par to accommodate future training, right? This is a cluster that they'll be operating over the next, you know, let's say five years? Yeah, and so, um, let's see. So, I mean, that's now where we are kind of going through a review of thinking through that long term and not that like it has to be solution you know today in 2026 or 2026 or 2030 31 but the thinking was thinking through that and maybe that would then require a foundation. foundational, fundamental change from Blob to Vest. Maybe that's some of the thinking, but again, I'm coming in code. I don't know why they would consider that 'cause I don't have the experience of what you did with them at CoreWeave or with Inflection or whoever kind of has this background with Vest. - So on that point, probably we wanna have a freeway with MAI where they will expand. requirements better but the basic reason why is because they're file-based use case and a Zublob is object and BaaS is object and file and many other things and that's what they're trying to get to and there is another project by the way which you might be aware of and there is Cheek and the city of Kubernetes that reports to Brendan who reports to Girish. She's actually running right now a bake-off. This is kind of futuristic. Just a POC where she's putting side-by-side solutions for MAI on the same hardware. So that's kind of future Azure hardware. On one side, she's putting vast and testing vast, and on the other side he's putting luster. not Azure Blob because Lustre is file-based okay so so I think MAI is going into forward with file and that's why I get Azure Blob is for them it is problematic. I really hope that since it's an external project but again I'm

[00:09:39.22]  Jason ValleryNot a Microsoft expert like you guys. Let me give you context from my perspective. So, Björn is absolutely right on point A, which is that MAI vastly prefer file-based NFS access over object. They've had to refactor a bunch of their tools to use blob storage. It's been painful. It's not insurmountable. It isn't the only reason. There's a performance component, and we can subdivide performance into software and hardware. Performance on the software stack, there's key differentiations from a protocol perspective. In addition to having NFS, it has NFS over RDMA and GPU direct storage, something Blob can't do, and S3 over RDMA. So even if they go down an object pass, they also have the RDMA outputs. So that's software stack. There's also just efficiencies in the system that make it perform better. Then on the hardware dimension, you know, VASP runs on, if you're running on VAST ODM hardware, kind of latest and greatest kit. So, you know, when you compare that to the Azure Blob storage hardware profile, we're talking about newer NICs, higher density QoC and NVMe, better CPU-to-memory-to-storage capacity ratios that are more tunable. and there are defined NVIDIA recommended sort of throughput per GPU numbers that you're supposed to hit, right. So when Kushal shared with me in the past, he's always come to me and said here's my throughput target for each GPU in a read basis and a write basis, and what we're learning, and we're learning this at BAST at the same time, is that NVIDIA is ratcheting up those requirements. The amount of throughput the storage system needs to deliver for each generation. So, it's doubling from GB300 to Vera Rubin, for example. Vault has no pathing. So, MAI clearly sees the need to build high-performance storage. Now, there's two questions that I have that kind of follow through on this. of record that's to deploy a certain amount of blob capacity. I heard eight timelines, I heard December timelines. I'd love to know what hardware SKU and what quantity you have targeted there, and then, to layer on to that, the question becomes, is the intent for Fast to run on Azure storage hardware? That's an option. We're fully committed to supporting that. we'll come in and pave all that hardware and run our software stuff on it. They'll still have the downsides of the hardware that I talked about. Or is the intent for us to partner with one of our suppliers to bring in vast hardware and deploy a best solution, best of classroom solution?

[00:12:15.06]   RemoteYeah, so no, that's super, super helpful, Jason. just really quickly double click on better understanding the piece of you paving Azure storage racks and running your software stack on top of that. So that's one thing I'm asking that's pretty straightforward I got that you say basically hey we're limited to your hardware kit but we're just more not what we're not OS and our software stack on top of that and kind of you get the best solution. So that's one thing. Help me, let me ask a second piece to that. Is there a solution where you work in Tangent or supplement Azure Storage? So where the customer has sort of a blob and a vast together and they work together, where the vast is like on the front end of that, Again, just work on the tangent in terms of one large storage pool. I just want to understand that piece.

[00:13:12.54]  Jason ValleryLet's talk about today and tomorrow. So today, those aren't features we have in the platform. So today, they would be side-by-side solutions. It doesn't mean that you couldn't copy data to and from them, right? They're sitting in the same data center. We have a copy engine. We can make sure data can move between them, but it isn't transparent. It isn't like they tier to each other. That's something we plan on implementing. So we will, and this is in our road map, and depending on this project, timeline, shape, what we can get in our engineering, I'll just say VAST executes much, much, much faster than Microsoft on these kinds of things. We will have the ability to tier from VAST to object storage including We are very much willing to implement a blob storage API over VAST to ensure that tooling works. Admittedly, both of those things require engineering on our side, and we'll have to prioritize them and put them into our development plan, and I can't make commitments on timelines today, but I can tell you those are real things we can execute on fairly quickly.

[00:14:15.35]   RemoteGot it, okay, okay. So then, all right, so, and just real quick, going back to a painting of Azure hardware, obviously back then would give MAI access to the file-based storage, which they are primarily seeking, along with some of the other special sauce that you have under the hood, but the file-based storage then is... are surfaced up for them to leverage for their workload. Is that a fair assumption?

[00:14:42.61]  Jason Vallery- Yeah, I mean, the devil's in the details. We haven't actually done this. We're committed to doing it. Azure Storage Hardware, well, I mean, please share with me. Are these Gen9 XIO Storage Fast Clusters?

[00:14:56.29]   Remote- Gen10, Gen10.3 is.., and that's what the documents will be starting off with.

[00:15:03.80]  Jason Vallery- Will they have CX7 NICs?

[00:15:05.40]   Remote- Yeah.

[00:15:07.73]  Jason Vallery- What's, can you, I mean, can you speak, I mean, what I would, before I made any firm commitments here, what I would want is a hardware specification quantity and design. - Okay, we would run it, right. - But broadly speaking, you know, we would run on that hardware, and away we go, we can make that happen. >> Okay.

[00:15:26.47]   Remote>> Honestly, Jason, that's probably not even in the realm of possibility, just because we haven't deployed it yet, and to me, it would seem very odd for us to do all that deployment and then just pave over it with that. I was just trying to understand kind of the. the big picture, but let's deny understand that you need to do some additional sort of understanding of the hardware stack that we're deploying to be able to assess that further. We don't have to spend a lot of time on that. I just wanted to understand, I'm trying to develop a model of like this vast thing and how it works and so far I've got it. It makes

[00:16:01.66]  Jason Vallerya lot of sense. I mean, well, you should.

[00:16:03.61]   RemoteLet's, I want to.

[00:16:04.70]  Jason ValleryLet me get the high level context. VAST is the Azure storage. software stack equivalency, right? It is software-only solution. We can run on a set of hardware. We have hardware we prefer to run on that we validate, qualify, and test provided by a variety of manufacturers. We can also run in a virtualized environment, Azure. We announced that just a couple of days ago at Ignite. But we prefer, our preferred, the best experience is on qualified hardware and I think that's where we need to go here given the scale and shape of what we're doing. Ultimately, the question is you can design a VAST system to be capacity optimized where we give you the maximum amount of usable capacity in terms of petabytes. We can design the VAST system to be the maximum performance system where we give you an amount of throughput and we can dial that needle all the way between it and what we'll come up with is a shape of a storage cluster or clusters that we would want to deploy, and ultimately the way I would shape that is likely driven off of whatever math Vishal wants to give us based on target throughput per GPU multiplied by the

[00:17:07.87]   Remote120,000 GPUs he shared will be in Nebvius. Got it. So I'll take, so I want to get to that. Like that's super important that we get to what the current engineering requirement is and kind of what the plan of record is. I can describe that. Before I get to that, I want to go back to understanding two things. So you're not currently like a vendor that, you know, for example, Jaycee, you'll know this, where NetApp is a partner. and we will actually run that at filers in our DC. There's vast admin type relationship with Azure already in that capacity with--

[00:17:46.14]  Jason Vallery- Not a hardware provider yet. This will be our first opportunity to convince Microsoft to make us one. - Okay.

[00:17:53.69]   RemoteSo you're essentially right now, okay. But you're like a virtual, like an appliance right now where a customer can go spin up an appliance in the-- Azure Marketplace and run your software, your software in one of the end, is that?

[00:18:05.59]  Jason ValleryYeah, that's right. So we run on compute instances though, the LSV4 today, and when you think about, when you're talking about hundreds of petabytes and you're talking about terabytes per second of throughput, like you would be talking about 40 megawatts of compute SKUs to pull that off. To pull that off, right.

[00:18:22.94]   RemoteWhich wouldn't make sense. Yeah, got it, got it, got it.

[00:18:24.63]  Jason ValleryOkay.

[00:18:25.54]   RemoteAll right, and so then the other piece, as it pertains to what you've done with MAI and CoreWeave and how I think about Nebbius and this NeoCloud that we're talking about, this is a specific scenario. So in those instances, I'm going to assume that you were running under the control plane of CoreWeave or the NeoCloud, not within Azure. So, has MAI been consuming the storage or consuming VAST through CoreWeave? How was that working?

[00:18:55.05]  Jason ValleryKind of two models here. VAST has a very robust API for management, and so, CoreWeave has a multi-tenant version of VAST that they sell to their customers. We provide all the storage for CoreWeave. world they have a management plane that's built into CoreWeave's control plane for those customers. But in MAI's example, and when they use this in CoreWeave, and there are other large-scale customers inside of CoreWeave, they get dedicated clusters, and when you get a dedicated VaST instance, you get cluster level access, and VaST has a full management interface. So we have our own portal system that gives logging, monitoring... telemetry, management of the shares, management of the namespace, IAM, all of that stuff is all directly built into a management plane that we provide via VaST. Expectation here is that's what MAI is going to want because that's what they get in CoreWeave today. Yeah, and then, but does that

[00:19:46.54]   RemoteAPI plug into the Azure control plane or how does it work? I'm trying to understand where this actually sits in terms of access to the API.

[00:20:09.54]  Jason ValleryThe API runs on our same hardware, so it runs in the same converged storage tenant, so there'll be an endpoint that they'll connect to. We can connect back up to Azure Active Directory for authentication, so they have a seamless authentication experience, and they'll hit a vast management endpoint tied to an IP address. associated with our storage cluster.

[00:20:28.07]   RemoteGot it. Okay. Got it. All right. So then that's the answer to the question I have. Again, I think I have the model now. Let's jump into what actually is happening in NetBeans in terms of what the current plan of record is. So at the end of the day, what we're going to provide then with the Gen10 SSD racks from your old group, is roughly 192 T of throughput, overall throughput, and that gets them to about 1.6 Gbps per GPU throughput.

[00:20:50.89]  Jason Vallery192 terabits?

[00:20:54.32]   RemoteYeah.

[00:20:54.68]  Jason ValleryWhat are we rating Gen10 as per 10-20 rack unit in terms of throughput there? Or maybe better said is like, I guess the dimensions I'd want to know is rack count.

[00:21:06.51]   RemoteIn total usable petabytes, and like, yeah, or petabyte usable petabytes it's roughly 1.6 exabytes, roughly, let me, let me just pull up something in a second. We're talking roughly 1.6, and I'll tell you the amount of racks. I mean, I think the amount of racks really, I'll give you the information. What I'm curious to know is on a rack-by-rack basis for a bass, what does that look like in terms of just, I mean, just right off the bat, could you just tell me the profile of rack you would be thinking about for this solution? Is this a 20 kW rack, a 15 kW rack, a 50 kW rack?

[00:21:51.98]  Jason ValleryWhat do you have in mind? So if you actually-- if we're going to design and optimize this stuff, there's a difference between C nodes and D nodes, and these are two different SKU types. The C nodes have far more compute in them, and the D nodes are basically-- data nodes, compute nodes, data nodes, and we can change the ratio of those based on throughput targets and capacity targets independently. This is one of the killer things VaST has that Azure Storage doesn't. Azure Storage is a monolithic deployment. There's a defined ratio between capacity and throughput, whereas we can set that to a specific number. We can say we want to get, you know, two terabytes per second per 10 megabytes. or whatever the numbers end up being as the optimal ratio, and so what we'll want to get to is that sweet spot that makes Kushal happy. He's got the throughput he needs to keep his 120,000 GPUs running, and he's got enough petabytes to store his data, and so getting to that will give us the tuned number. What I can say is we're all flash, and so when you tell me 1.6 exabytes, is that all flash or have they got hard drives in there?

[00:22:53.02]   RemoteThat's a shit ton of flasks. All flat. So we have 1.6 megabytes. So I'm saying 192 TDPS of overall throughput. The actual number is more like 200. But we're only going to offer them 192 based on some limitations. We have a series and some other stuff, and we're talking roughly 400 storage racks that I'm deploying to get-- of these numbers, and so that number meets MAI's requirement today. Again, I think, based on you all educating me about the vast file system, along with some of the other options to sort of tune the file system to do different things based on the need, I think this really was probably attracting them, and so that's your sort of... base model, I'm offering 192, 1.6 petabytes of storage, exabytes of storage, I'm sorry, in 400 storage racks. Ideally, that would be sort of your, the lower bound of what you need to hit, and then you tell me, based on that footprint, what that would look like. If you're not telling me now, but I'm saying, here goes how we should start thinking about this.

[00:23:57.51]  Jason Vallery- Let me pull up, I mean, let me just start framing the reference for you. You're giving me some new numbers here that are helpful for me to put in context where Gen 10 is at. Obviously, that information postdates my knowledge from when I was at Microsoft. Let me pull up what I know and give you a reference example. These aren't final, but hold on one sec. Share, screen, window, tab, window, this thing, share. So, let's take a look at this example, and what you'll find here is we're in a lot better spot, I'm imagining, from a power perspective. How many watts per rack are you getting out of your Gen10? Were you at 20? Is that what you were thinking?

[00:24:46.75]   RemoteLike 15.

[00:24:47.50]  Jason VallerySo, this is me assuming 1 exabyte of usable capacity. sort of specced it out at two versions, a performance-optimized version and a capacity-optimized version. Now, the difference here is that the performance-optimized version is leveraging the throughput characteristic targets that NVIDIA would use for their current reference DGX design, whereas capacity-optimized does not hit those same numbers. So, what this practically means is the ratio of C nodes to D nodes, as well as using higher density NVMe on the capacity optimized. As a result, to get to 1 exabyte of usable capacity, these are the numbers, 2.4 megawatts in 90 racks or 610 kilowatts in 21 racks. So you can see if we go with a much. higher density capacity and sacrifice some performance, we can do this in a very small footprint. But if we hit some high-level performance targets, then we're going to push those numbers out because we're putting a lot more of the compute-oriented SKUs in it. The other point I'll call out here is this data reduction ratio. This is something that is unique to VaST. has no capability here. So this is deduplication of data, two types of deduplication, real byte-wise deduplication, and there's also differencing-based deduplication. So what this means is if you've got a one exabyte cluster, you can really store two exabytes in it, and what I will say is that observed in the MAI Condor cluster in Portland that they have, from VAST, they're getting about 1.7 exabytes. So in this world, if we deploy 1 exabyte of flash for them, they're probably able to store about 1.7 exabytes of data on it. So what we really need from this to spec this out and come up with the quick answer you're looking for is how much data do they want to store? How much throughput per GPU do they want? and we can come back with a proposal of where we sit in this spectrum.

[00:26:44.81]   Remote- I see. So let me just, no, this is great, Jason, thank you. So right now though, with your performance optimize, which are usable, there it goes. So your performance optimize here. what is your, what's your, you're basing this off of how many GPUs you want to get.

[00:27:07.88]  Jason ValleryAll of these calls are per GPU, not per output, an exabyte index. So the design here was me just trying to give a apples-to-apples view of five different hardware options at an exabyte, where the goal was to achieve an exabyte of usable capacity. Now, we also have... much higher levels of granularity in our design where obviously you're quite aware that blob gets deployed in 20 rack tranches, we can deploy 24 racks, we can deploy 47 racks, we can deploy whatever we need to hit a target throughput and

[00:27:35.66]   RemoteCapacity ratio, and what's the front-end requirement in terms of it? I mean like in this scenario when I deploy Azure Storage at I'm bringing the full armada of, like, Azure front-end networking to support that, to get it back into the control plane. What do I have to do to accommodate that? Am I putting this on the front-end fabric of the GB200? Am I deploying a separate fabric? How do I even connect this up?

[00:28:05.61]  Jason ValleryI'd like to answer that question myself. Well, let me tell you what we've got is we obviously can deploy on the physical network. That's how we typically deploy for our customers. We have physical IPs tied to the NICs on our front ends that come from a configuration we set into the switches. Obviously, if this is Azure Storage, it's got Overlake. we're doing. overlay networks and we're connecting back into a virtual network. So if the requirement is we need to translate from an Azure virtual network that's running inside the GPU hosts, which I'm unclear on, into a physical network running onto VaST, we need to solution that. Now I think, I'll first comment, I'm not the expert in this domain. but we have some folks on our side, and I certainly know some folks on your side. We want to get together in some room to come up with a plan. That's kind of the problem that I can see emerging. But if you tell me the GPU hosts, if their front-end network have finite access into the underlying RDMA network, then that's a win because we can just do bare-metal addressing. But I don't know what that looks like either in Nebia. or how you plan to deploy there, and if we need to support overlay networks, and if we need to support Microsoft.

[00:29:23.69]   RemoteSo, right now, the storage RDMA bandwidth requirements are not accounted for in the GPIO. front-end network. I'm not saying that the capacity is not there to accommodate, I'm just saying that that is not the current architecture. So this is a blind spot, this is a gap for me in terms of, well, if I drop you in, I'm making no assumptions that I can put you on the Azure control plane because I don't think that's going to work. So that means you've got to come in through a single the Nambius front-end network. Remember, in this scenario, Jason, for Nambius, the front-end network of the GPUs is sort of an outside entity to me. Like, that's a separate entity, and I connect to that over like a border switch, right? They have a border switch that connects over to Azure Dedicated, and that's how I get access to the GPUs.

[00:30:23.32]  Jason Vallery...serious appliances in Denebious? Is that what it is?

[00:30:26.32]   RemoteI didn't get you. What was that, Mike?

[00:30:28.32]  Jason VallerySerious appliances in Denebious? Is that what they're using?

[00:30:31.32]   RemoteWe are, yeah.

[00:30:32.47]  Jason ValleryIs that how, so, then what would have to happen is you'd have to size the serious appliances based on the total throughput of storage target, which is a shit ton of serious, that'd be very expensive, but if you...

[00:30:43.32]   RemoteNo, yeah, we totally do it. That's playing a record. Yeah, that's so right. So I'm saying that's how we're doing it to accommodate Blob. So that's, I mean, you actually bring up another question, like, we don't, would that still be required for VAST?

[00:30:55.99]  Jason ValleryNo, we could, we can sit on the other side of the Sirius network and just be on the physical network, assuming that passes your security and compliance validation requirements from MAI.

[00:31:04.07]   RemoteYeah, right, and so then Sirius is doing the translation and then we don't really care.

[00:31:08.35]  Jason Valleryon the other side. Okay. What that actually means is it just saved you an ass ton of money because

[00:31:13.31]   RemoteYou don't have to deploy all that networking gear. Yeah. Okay. Well, I've got, so, uh, no, I still have to deploy enough networking gear so that, remember, remember I said that the 192 TPPS. That's really the Sirius limit, where I'm putting enough Sirius to accommodate that, which meets the current requirement.

[00:31:36.91]  Jason ValleryBut what I'm saying is that you only need that because you're going into the overlay network and you're supporting overlay, and the Sirius is translating physical to virtual. If we can sit on the other side of it and be on the same physical network as the GPUs, and...

[00:31:48.85]   RemoteOn the GPUs, that's what you're saying. Yeah, yeah, yeah, yeah. Got it, got it, got it.

[00:31:53.36]  Jason VallerySo just to be clear, that's how we deploy in CoreWeave. If that gets the sign off of Microsoft security and whatever kind of controls and AI are gonna require, then you've just saved yourself all of that serious gear.

[00:32:05.90]   Remote- Yeah, all the serious stuff, which is great. I mean, honestly, I don't want to pull all the serious. It's a big fucking edit. So yeah, got it, okay. All right, this is really interesting. I want to pull Kajan into the conversation because she wanted to be in the discussion. I do have a meeting with MAI later today on this topic, so let's figure out next steps. I want to first debrief them and then also better understand and make sure there's alignment between what. I think a good understanding of what their needs are. I haven't talked to them at that level of depth. I want to make sure those two things are aligned and then let's start, I think, bridging the gaps and bringing everyone together to start looking at it as a solution. Let me say this. So right now, let's just say in a scenario where we do a complete pivot to vets. I've got to start deploying storage capacity to support, let's say the first 9K of GPU by Jan 15, Feb 1, I got to have racks landed and being built. out. What is your supply chain and sort of build out time?

[00:33:30.54]  Jason ValleryBuild out time issue. I mean, we'll airlift engineers in and pull this off as fast as possible. There's no timeline issues on the build up. What I won't make a firm comment on is what it takes to get 1.6 exabytes of flash. I'll have to make some phone calls.

[00:33:44.33]   RemoteNo, that's a that's a ramp. So that's the 1.6 is at the end of this, at the end of the deployment period. I got to get up and be at 1.6, but that gets ramped over time. Right. So I, I deploy it in increments. I would say beginning in Jan 15th, Feb 1, and then let's say like every month, and then there's like a month that I'll skip and then I'll look for another, another set. But we can talk about the ramping into those details. 1.6 really, I don't get to that until we're talking, Jan of, hold on, sorry, here we go. It goes the right way. So we're talking like, I deployed my first set in February 26th. set to deploy another 9.6K or 9.2K of GPU in June. I need another set in July, another set in September, and I apologize, that's the date that I need the storage live. That would be a work back date, right? So we're saying June 1, 26, I need enough to support 18K of GD300 to hit. the per GPU throughput as well along with the read and write requirements and the capacity requirements then your work back would be from June 1 how many days you would need to have something landed and enough engineers to get it like up and operational and I can give you a table showing you those dates but yeah I would love to just understand like realistically do you have

[00:35:15.92]  Jason Valleryto to meet that ramp across next year? One difference in terms of how we'll want to deploy, I'm not saying it's the only option, compared to your experience with Blob is that in an ideal world to get the maximum performance of our system, we want all of our nodes converged into the same adjacent set of racks so that we can deliver the networking kit. in the same effectively t0 network. To make that happen we would almost certainly just say well let's just deploy all 1.6 exabytes at once. Now that would put them all in the same set of rows I mean if it's you know probably be three rows four rows of capacity we would want those four rows isolated in the data center and carved off for us. we could just deploy. Now we could potentially deploy them one row at a time but from a space planning perspective our preference here would of course be that these are all adjacent rows.

[00:36:10.59]   RemoteGot it that's that's good to know. All right so let me let me look at something give me a second. It's nice to see two people who know everything about each other and about the project talking. each other. So, it's very nice to be a fly on the wood. Thank you Jason for joining us. Jason and I have been in the trenches before with this customer. I'm trying to figure stuff out. I am enjoying it. I'm really enjoying it. Interesting. So, I'll just, I'll leave you with this, gentlemen. I gotta run. I think I'm late for a meeting or something. But-- I could see this going realistically a different way, just because of a few things. I could see, so I mean, I was very interested in doing something incremental to the 1.6 exabytes of blob that we currently have in the plan of work. I think there's plenty of capacity to do essentially. another one or two exabytes of that on the backend of this deployment, but it would be more, but in order to meet that requirement, Jason, to get you all consolidated into like one or two data holes, like in a nice neat, you know, row. I know I can't do that up front, like for the first half of 2026. I can't do that for a number of different reasons. But as something to supplement if you know I was interested in supplementing the best. That is something we certainly could do I just don't know how I would feel about having like a block who would have asked who may not be something they want to do. So obviously we need to have some further discussion and yet that's what then we all need to have discussions and talk to you a little further. the deployment model, but I know we're up front the first, the first, let me just tell you, so I've got a total of 14, 14 data hauls at NEPIUS. 14 data hauls

[00:38:07.75]  Jason VallerySpread across data centers. I imagine each one is like a data center. Yeah, but more about the interconnect, like how they connect to each other from a back-end network perspective? Like is it all? Oh yeah I mean this is

[00:38:21.09]   RemoteThis is like super high density. They're like sitting on top of each other. So these are like townhouses right? Like they're they're like roll houses. They're right on top of each other. Let

[00:38:28.27]  Jason Valleryme ask you a different way. From a switching perspective, what are the layers of hierarchy in the network? And are we going to see any bottlenecks? Is it is it? a non-blocking network between all of the data holes?

[00:38:41.54]   Remote- There is, yeah.

[00:38:43.52]  Jason Vallery- Single non-blocking back-end network and front-end network between the data holes?

[00:38:47.64]   Remote- Back-end, that's a different conversation, but I'm focused on front-end for this conversation. Yeah, it's... Let me hold that, let me hold on that, hold on. I believe it's non-blocking, but I need... to double click on that because we're not talking about for the Microsoft network we're talking about for the GPU network. For the GPU network that's why I said we had not planned on running anything any high throughput through the GPU network so what we didn't plan on having anything sitting on the GPU network for example the storage compute nothing was sitting in that network. Everything was sitting outside of that network. So that's why I'm saying, I'm not even tracking some of those details on whether or not it's non-blocking or not. Like that's a detail I need to go back and confirm.

[00:39:34.80]  Jason Vallery- I see. - With that.

[00:39:36.27]   RemoteYeah.

[00:39:37.41]  Jason Vallery- Ultimately, I think we can do this. I mean, I think that's the high level sentiment. What I think is a clear next step is a lot more conversations with MAI and us to bring some. of our engineering folks into a war room with yourself to just plan out the data center, the build out and work with our suppliers to see what's possible on what timeline. If that's the next step, like I'll book a plane ticket to Redmond, I'm on my way, let's get it done.

[00:40:01.17]   Remote- Yeah, no, I agree. Again, there's a meeting tonight with work later this afternoon with MAI on this topic So this was I mean it was great for me now to have this conversation with you to come into that meeting to have some frame of reference. The real objective that meeting for me is to better understand align what you're saying in terms of your understanding of their requirements and what they're looking for, and to make sure that they're saying the same thing and say let's connect the dots and to your point let's just all get together and see if you can figure this out. There's a lot that. that's going to happen here. Like there's, the plans have been made to deploy this blob storage. So, but plans can be changed. I've seen it before. So, I think that's the proper next step. Let me get with caution on this and then circle back with you all. Let's get something set up. I'm unfortunately, like after next week, I'm out of pocket. I'm in the Middle East for the like all of December. So like after there is an on-site meeting with NEBIUS, NMAI, December 1? - You wanna-- - I don't know.

[00:41:04.09]  Jason Vallery- Well, I would request that you make, that VAS would like to be there to do the site survey with you and a few of us will come out.

[00:41:11.85]   Remote- Yeah, so I think on that one, no problem, we'll do. But let's not, I don't want us to see that as the only opportunity. I think if there's value in having you all come out and just see the site, like we can still plan that. It doesn't have to be on that date. What's unique about that date is MEI will happen to be there on that date, and that agenda is already pretty full. So, but I'll certainly fill that out there and see if that's something that folks are interested in doing. But there's a lot of people with their hands. that agenda already but there's still opportunity to go see neighbors i can facilitate that okay we'll

[00:41:42.99]  Jason VallerySee the site there's no i see two workshops we definitely need a site survey to make sure we know how we're deploying into the site in advance of that or in parallel with that what we want to make sure we're doing is the site design and the site design is ultimately fundamentally not only just where things are going but when they're going there and then That translates back to functional workload requirements from MAF. So we need to know the requirements, then we can come support you in building out a site design, and then we can go validate the site design as plausible with a site survey. All three things need to happen as fast as possible.

[00:42:17.48]   Remote>> Yep, agreed. Yeah, so I will, I'll coordinate with you again, I think after. Oh, after Thanksgiving, I have very few days that I will be available. Suresh will probably be taking point on a lot of this and will be, I guess, bringing in some other people. But I'll be gone from basically December, like, 3rd until, like, the 15th or 16th, whatever that Monday is. So I'll be out of pocket, unfortunately, for a little bit of time. I'm going to be honest, like I'm without me being here, there's a lot going on, I'm the person that's closest to it. It's going to be a little difficult to pull this off and to kind of make, you know, a lot of headway on this, but Suresh will be, who's my manager, will be, will be sort of the DRI while I'm out, and I'll make sure that he's looped into this conversation.

[00:43:06.22]  Jason ValleryCan I ask, are there other in-converse seats? sites beyond the nebulous site in Dallas? 'Cause I got some interesting pings from some other Neo clouds that are all, what the hell is going on with Microsoft and what are we doing? Like, to the extent you're sharing, is MAI getting capacity outside of nebulous in Dallas?

[00:43:23.42]   Remote- No, the focus for nebulous right now, I mean, for MAI right now is nebulous. I've had some other, I'm involved with a lot. different deal clouds right now and it's funny one of them did brought you all up as an option and like for that particular engagement it like it wasn't something that that Microsoft wanted to do but other clouds have been mentioning vast to me it's just again I didn't know what I didn't know what it was so I was like no no when I understood we're we have like we already had plans for those sites um but yeah. Right now, all the focus is on Nebbius right now.

[00:43:56.07]  Jason VallerySo, Nebbius is a big eyesore. - Since we're going to be friends, we already were friends, Bilal. We're going to be best friends now. - Best friends, sure. - What I want to say is like, Vast partners with basically all the neoclubs, right? So when you think about their business and go to market, they don't have an Azure storage, so they come to us, and so we've already got Bell 2 relationships with Cori, Vinscale, you name it, they're probably Crusoe, they're all vast customers at some level, and so they're all sort of like, well, what's the storage requirement in terms of all this capacity that Microsoft is getting? So as you and Suresh think through this, like, let's have a consistent answer and make sure we're working on getting the neocloud.

[00:44:38.73]   Remoteit's a consistent experience. Yeah, for sure. No, that's good to know. I appreciate the data points. If you guys can share this table or any other documentation, that's super helpful just for me to continue to spin up and just ask additional questions. But no, this was super helpful. I really appreciate the time. I've got to run, I'm like super late for another call. What's the next step here? Yeah, let me let me have the conversation in the eye today, and again, I need to. I need to speak with caution as well, so let me speak to her. She's she's the other key person here that I need to coordinate with. So let me talk to her, fill her back, fill her in on this conversation, and then we'll figure out next step.

[00:45:18.91]  Jason ValleryOK, thank you.

[00:45:19.57]   RemoteAlright, thanks guys. Bye guy. (paper rustling)


