---
entities:
  people:
  - '[[Karl Vietmeier]]'
type: transcript
source_type: unknown
date: '2025-10-31'
---

# 1:1 — Karl V — 2025-10-31

> [!info] Purpose
> Build trust, surface and remove blockers, align on priorities, coach & grow.

## Summary

Introductory 1-1 aligning on VAST’s cloud strategy. Jason outlined a vision for a planet-scale, multi-tenant/SaaS platform spanning hyperscalers and neo-clouds, emphasizing GPU-adjacent storage, global namespace, smart caching, and cloud-first economics. Karl shared background (Sun/NetApp/Cisco/WWT/Intel/Microsoft), recent GDC (Google Distributed Cloud) RFP via Cisco, and strong interest in AI/ML integrations and automation. Both aligned that cloud team should own GDC/neo-cloud single-tenant GPU storage opportunities and that S3/object offload and upstream integrations are critical. Plan to sync at Supercomputing and for Jason to finalize org planning with Jeff.

## Key facts learned

- Jason recently took on cloud product responsibility reporting to Jeff; focus: make VAST best on cloud and toward true multi-tenant SaaS across hyperscalers and neo-clouds.
- Jason’s background: Microsoft Azure Blob storage; led AI storage for hyper-scale, managed storage relationship with OpenAI.
- Karl’s background: Sun, NetApp, Cisco, WWT, Intel, Microsoft; deep Linux/distributed systems; Ceph/OpenStack; operated as TME/SE driving POCs and automation.
- Google Distributed Cloud (GDC) RFP surfaced via Cisco; interest in VAST as storage for GDC sites; needs API/monitoring/billing integration with Google control plane.
- Potential deployment patterns: single-tenant GPU-adjacent storage per customer/cluster (e.g., OpenAI/MAI/NSA/NATO), akin to neo-clouds and Microsoft extended/edge zones.
- Edge zone/extended zone challenges: large footprint (≈60–80 racks), poor scale-down, dependencies on parent region connectivity (backhaul/fiber cut risk).
- VAST differentiation in cloud must extend beyond file shares to upstream integrations (Spark, Trino, Vertex AI, Bigtable) and pipeline simplification.
- Critical requirement: scale capacity independently of performance via object/S3 offload; current resistance to “tiering” must be addressed for cloud viability.
- Global namespace demo with TPUs (with Kartik) showcased portability and avoidance of data gravity issues by placing compute where available.
- Karl is hands-on (bash/PowerShell/Terraform/Ansible; some Python), heavy automation, and uses AI tools for coding, editing, and technical search.

## Outcomes

- Alignment that cloud team should drive GDC/neo-cloud single-tenant GPU-adjacent storage opportunities.
- Agreed need to engage Jonesy’s team for GDC API/monitoring/billing integrations.
- Jason to proceed with org planning with Jeff and clarify cloud ownership and potential reporting lines.
- Plan to meet at Supercomputing to continue discussion.

## Decisions

- P0 priority: enable capacity scaling independent of performance via object/S3 offload for cloud.
- Cloud team to spearhead GDC-style opportunities, coordinating required integrations.

## Action items (for Karl V)

- [x] Obtain and review the GDC RFP and clarify whether VAST is requested as a managed service offering vs. backend distributed storage for GDC sites. @Karl V ⏫ ✅ 2025-11-08
- [x] Loop in Jonesy’s team to assess API, monitoring, and billing integration requirements for a GDC-aligned VAST deployment. @Jason Vallery ⏫ ✅ 2025-11-08
- [x] Finalize cloud product ownership and org plan with Jeff, including potential reporting line for Karl. @Jason Vallery 🔼 ✅ 2025-11-08
- [x] Define and document cloud ‘now what’ use cases and upstream integrations (Spark, Trino, Vertex AI, Bigtable) to showcase differentiated workflows. @Karl V ⏫ ✅ 2025-11-08
- [x] Drive design and plans for capacity/perf decoupling via object/S3 offload with Yancey’s team. @Jason Vallery 🔺 ✅ 2025-11-08
- [x] Coordinate coffee sync at Supercomputing to continue cloud strategy and GDC planning. @Jason Vallery 🔽 ✅ 2025-11-08

## Follow-ups

- [x] Share Karl’s GitHub repo link with Jason for review of automation and tooling. @Karl V 🔽 ✅ 2025-11-08
- [x] Provide notes/artifacts from the TPU global-namespace demo to inform cloud workflow examples. @Karl V 🔼 ✅ 2025-11-08
- [x] Confirm whether Google intends to procure VAST via Cisco for GDCs and the expected commercial model. @Karl V 🔼 ✅ 2025-11-08

## Risks

- Without object/S3 offload, VAST lacks a viable cloud cost/perf model versus competitors.
- Insufficient upstream integrations (Spark/Trino/Vertex/Bigtable) weakens differentiation and the “now what” story.
- Control-plane integration complexity (APIs, monitoring, billing) with GDC may delay adoption if not resourced.
- Organizational ambiguity on ownership and roles could slow execution.
- Edge/extended zone-like dependencies on parent-region connectivity can undermine site resiliency for GPU clusters.

## Open questions

- Will Karl formally report to Jason after org planning with Jeff?
- Does the GDC RFP require VAST as a managed service offering, or as backend storage embedded in GDC sites?
- What exact API, monitoring, and billing integrations will Google require for GDC-managed operations?
- Can VAST leverage cloud object storage for capacity offload in target clouds, and are there constraints by provider?
- Is first-party VAST hardware in cloud data centers feasible for certain deployments?
- How will control-plane resiliency be handled for GDC/edge sites during parent-region connectivity loss?

> Next meeting (if any): (none)

---

<!-- ai:transcript:start -->

## Transcript (auto)

```text
[00:00:00.04]  Jason ValleryI'm on the West Coast, L.A. I figured that based on it being 930, but where in L.A.?

[00:00:10.11]   RemoteL.A. I'm in the L.A. area.

[00:00:12.00]  Jason ValleryGood, good. Okay.

[00:00:15.00]   RemoteIf you know L.A. at all.

[00:00:17.00]  Jason ValleryNot, but I don't know exactly where that's at.

[00:00:22.50]   RemoteI'm in the Inland Empire, just south of Pomona, just east of Diamond Bar.

[00:00:29.97]  Jason ValleryI've been to a lot of Diamond LA, normally I'm there for like some random business trip and it's in and out of the city, or did a lot of trips there for the media and entertainment industry, so you know, going out to Burbank or Disney. you know, wherever, that's where I probably would never.

[00:00:47.31]   RemoteYeah, you wouldn't come out. Yeah.

[00:00:50.49]  Jason VallerySo, uh, well, I figured it would be good to just meet and introduce myself, and, uh, you know, you had some good thoughts on VMware and it sounds like you were just on a Google call. So just kind of connect on how we can work best together. Um, you know, I don't quite, you've heard about me, but just. about, I guess, two weeks ago now, reporting to Jeff. I am really looking at how do we make VAST best on cloud, and there's a bunch of things underneath that, with the current work in flight around the marketplace, offerings, but then, like, long-term, what does the platform need to... to an eventual state where what we really have is true multi-tenant and SaaS kind of platform that spans hyper scalers and the Neo clouds and can you know move data around transparently and all of that. So there's a lot of there's a big vision and roadmap behind you know baby steps that we're taking today with Google and then Microsoft. My background I spent the last 13 I feel without the first 10 years of my career I was a software developer so I'm very hands-on technical kind of guy I really like to get into the weeds understand how things work I have a strong understanding of systems architecture distributed systems and then you know my journey at Microsoft has been on the object storage platform so while I was at Microsoft I wore pretty much every product hat within the Blob storage team. Culminating in the last few years really just focused, my team was really focused on AI storage and supporting you know hypercell supercomputers and multi-exabyte namespaces for OpenAI, and I owned the storage relationship between Microsoft and OpenAI, and that all went through me and my team, and so that was kind of a wild ride to be on, and, you know, why I've asked, I have a ton of respect for the platform. I've done competitive analysis. I, you know, know a few folks. I suppose you may know Glenn Lockwood. He came over and we had worked together quite a bit and I really respect his opinion and my own opinions about that. and I think it's really just a well-architected platform that sets many of the hyperscale AI customers up for long-term success and so yeah it's the next step it's all like a cool opportunity and here we are so that's me yeah well so I just so I I was so I actually was at Microsoft for

[00:03:17.78]   RemoteAbout a year and a half okay I was a um I was a global black belt GBB yeah so I got hired so I know Carl from NetAppDix so we know each other pretty well and I was at Intel and for whatever reason I just felt like I wanted to make a change and I was hired to do advanced storage global black belt but a month after I got there they decided that they didn't need that team anymore yeah, so they

[00:03:56.96]  Jason ValleryDissolved us and punted us over to Azure Virtual Desktop. I mean I had some meetings in those days with the storage GBB team, was it Broan? Broan Daly? That's right, Broan Daly. He's awesome, by the way. There's another guy I can't think of now. Kelbley yeah yeah John Kelbley yeah yeah yeah yeah and I remember being a little

[00:04:18.76]   RemoteFrustrated by that for one reason because I worked at NetApp for like four years and I knew NetApp very very well and all the A&F people I when I went in the room I knew about half the people in room. They're all SCEs, CSEs from when I was a NetApp, but they, it's like, well, why don't you just put me on the ANF team with Roam? Why are you wasting my experience and connections? And they stuck me on Azure Virtual Desktop for a year. So I left, I went back to Intel. Microsoft's a tough place to go mid, late in career. with no connect no network to support you right so it just it just i had i i've known a couple other people did the same did similar and left pretty quickly because of it yeah because if you have no one to back you up and they give you connections when when the musical chairs happens at the end of the year right it's it can be it's tough. For sure. I mean, Intel wanted me to come. I had some people at Intel that kind of wanted me to come back, so I went back to Intel to work on the telco team, supporting Microsoft. So I was, you know, the Azure for Operators solution? Yeah. So I was, I was on, on the Intel, I was on the Intel team, At Intel, I was working with the Microsoft Intel team, supporting and doing design in and sell with stuff with Azure for Operators.

[00:05:53.58]  Jason Vallery- You know, a bunch of Azure for Operators used to be on the storage work. So I don't know if you worked with like Jason Hogue or Peter Pareto or any of those guys. Like they were OG storage. folks that have been left to go do the Azure for Operators project. Yeah, interesting.

[00:06:07.87]   RemoteBut that project never, I don't think that, I was told by a couple of colleagues that I still stay in contact with, that project, the Azure for Operators, kind of, this sort of...

[00:06:19.44]  Jason ValleryThey, what I would say is like, they were a bunch... bunch of these Azure bets that Jason Zander, who led that part of the organization, was making around, you know, Azure for space, Azure for operators, Azure for, you know, the edge, and then when, you know, there was a clear inflection moment where Microsoft just economically. they weren't playing out, there was retractions happening, and Microsoft basically just went and re-collapsed a bunch of those teams back into Azure Core and, you know, ended up with those back. So, yeah, exactly. That team still kind of exists, but they're focus-pivoted, and I don't think Azure Private MEC exists.

[00:07:07.67]   RemoteI think they pivoted around to private mech.

[00:07:10.21]  Jason ValleryWell, that makes sense. Extended product now, too, that I think they're trying to put in there, too.

[00:07:16.37]   RemoteAnd I mean, I don't want to go too far into that, but the big problem that we had and that Microsoft had with that solution was-- I don't know if you know the telco industry very well, but the people running the 5G packet cores-- at telcos are they are hardcore linux distributed system people okay on-prem hardware openstat kubernetes right linux kernel and microsoft you were gonna have to come and sell them two things you had to sell them a packet core because maybe they're not running the affirmed packet core right they're running somebody else's like like an Ericsson or something, and you have to sell them Azure at the same time. So you have to sell the Packet Core teams Azure because you're shifting the control plane and everything, and it's all Azure Arc managed. So, and you're asking them to put Azure Arc into their 5G Packet Core, which is their moneymaking, right? I mean, that's the part of the... where that's like their assembly line. It's like if Ford Motor Company, right, has an IT department and the place and the assembly line is where they make their revenue and money. That's what the, that's what the, the, like the packet core networks and stuff and telcos are. So they don't mess around with that space. They are, they're very, very resistant to change. I mean, I was in some of the conversations with eMobile and some others, and it was a tough sell. They liked the idea, but just the institutional inertia to overcome that was, but great idea.

[00:08:52.03]  Jason ValleryI mean, shifting everything to arc-managed, and I mean, I loved it, but anyway, it's actually top of mind thing for me as it relates to the neoclouds and really where Microsoft sits there because one of the issues Microsoft has and where I think VaST will play a key role is they're building out all of these, well Microsoft's going in and leasing capacity from data center providers, they're going in and procuring capacity from these neoclouds. The problem is that like you can't make those in Azure region, you know when you make, when you take one, like you've got a 4k, 8k, 12k GPU cluster and it's you know a full data center of capacity that you're getting from one of these providers and it's not an Azure facility. Microsoft needs to be able to go into that facility and put a control plan. over that capacity and deploy storage into those environments and Azure as it exists today, you know, it just you can't do that like there's six. It doesn't scale down well. Exactly, yeah, Azure doesn't scale down well and it has all of these internal dependencies and Azure Storage and it's running Windows Server and it's a whole thing.

[00:10:05.07]   RemoteSo this is what they tried to do with Edge Zones.

[00:10:08.21]  Jason ValleryThat's exactly the problem, but today, that is still 60, 80 racks of equipment, minimum footprint for an extended zone, and that's just eating up a bunch of the space and power in those facilities, and it's not resilient. If the fiber or the connectivity back to the parent Azure region is down, then everything in that site is down. got a multi-billion dollar GPU cluster running inside of this building and somebody with a backhoe digs it up, you take our GPU cluster and hide it. AT&T actually has one of those running. What's that, an extended zone? There's a handful of them. I mean, open your eyes, it's a bunch of them. So this is very important, so this is good

[00:10:49.08]   RemoteThat you brought that up because I need to talk to you, so I'll give you my need to talk to you about this call I was on this morning. You should have been on this call, and it's exactly what you just talked about. So I don't know if you've heard of Google Distributed Cloud. It's basically their results. It's almost the exact same thing. Actually, when I was at Intel, they deployed one at T-Systems in Italy, because Italy wanted a, they wanted a sovereign Google Cloud in Italy. So what the solution was, don't build a new data center. T-Systems, if you've ever been to Togo data centers, they have a lot of extra floor space, 'cause everything's shrunk over the years, right? So they just dropped one right into the T-Mobile, into the T-Systems data center in Italy. and boom you automatically have a sovereign cloud I mean subset of things but here's the thing Cisco came to us we have an RFP and Google has come to us asking us and this is not vast and this is not vast on cloud this is vast in cloud because they want there's an RFP for using VAST as the storage in these GDCs, and so there was Olivia was on the call, I was on the call, it was mostly all the kind of usual suspects, Ross Cooper Smith, right, some other folks, Jeff was on the call, Tomer was on the call. I think you're going to largely, you're going to kind of offload some. of the cloud stuff from Tomer.

[00:12:24.61]  Jason Vallery- Yeah, I mean, Jeff and I are planning meetings next week to figure out exactly how it's all gonna play out, but that's all.

[00:12:29.46]   Remote- Okay, 'cause yeah, 'cause he's been the, he's kind of been the cloud guy for a while, right?

[00:12:36.80]  Jason Vallery- Yeah, I mean, he's been everything.

[00:12:37.62]   Remote- But anyway, this is very, very interesting, and I think this is something, and I think what's happened is that you... usual suspects took it and the accounting, they went to Ross and they went to the usual people because it feels very much like an on-prem Cisco vast opportunity. But it's not, really. It's more like a Corweave type sale. This is Google-want-it-or-don't-want-it. to purchase through cisco fast to deploy in their gdcs now i'm going to get the rfp document and look at it because what's not clear to me is whether and this is an important distinction right is whether they are they want to have a vast offering in the gdc just like azure net app files for example right so net app in cloud? Is that what they want, like a core weave? Or are they looking for a distributed storage solution to drop into these GDCs to layer their storage on top of?

[00:13:41.60]  Jason ValleryI would like to see a potential third scenario, because at least in the way this plays out at Microsoft, is that these environments are single customer, single tenant. where it's like, "Oh, we have this 4K, 8K, 12K GPU cluster." This whole cluster is going to go to OpenAI. This is going to go to MAI, this is going to go to whatever customer, and so in that world- - It's going to go to the NSA,

[00:14:04.80]   Remoteor it's going to go to like NATO or somebody, yeah.

[00:14:07.38]  Jason Vallery- Sure, yeah. So in that world, it's likely that they're just saying, "This customer needs some GPU adjacent storage, and it's going to be single customer." single tenant vast plus whatever compute that Google's delivering into that facility for whatever customers buying. I think these opportunities you we need to own those I think. That's right like that's part of the strategy and I mean I don't know Google's scenario but what I'll imagine is that Microsoft doesn't have a good solution for this and if Google's in the same boat where they deploy Google storage racks for whatever control plane reasons, networking reasons, or performance characteristics.

[00:14:44.84]   RemoteWe have the same problem. I did Ceph, so kind of into my background, so I spent a lot of time working on Ceph projects at Intel and at Cisco. I have a distributed systems background like you. I'm a kind of Linux guy. I worked at Ceph. Sun Microsystems, NetApp, Cisco, WWT, Intel, and Microsoft. So that's kind of my background, and in all of those places, I've always been a technical specialist overlay focusing on open source Linux solutions, distributed systems, things like, and stuff no one else knew how to do, like Microsoft Media Room, for example. So when I was at Sun... Cisco, I worked on all the-- I was responsible for all the Microsoft Media Room projects that went on Cisco UCS, stuff like that. Because no one else knew what that was. You couldn't stick the SAP guy on that, because he's the SAP guy. So you stick Carl, who is the distributed systems platform guy, that can figure it out. So that's the kind of stuff I did. I was an OpenStack-- but I did a lot of Seth and Seth doesn't scale down well and all of these distributed systems that you're running your storage on top of I've seen the white papers for Azure storage for example it's a complex it's a distributed cluster of right I mean and so you can't just take a little piece of

[00:16:03.83]  Jason ValleryThat let's stick it somewhere and expect it to perform well

[00:16:08.48]   RemoteI mean, they're looking for something and man, I'm telling I mean we get that That's a gift that keeps on giving right because every time they sell a GDC or Microsoft sells, right? Yeah, we Kitchen, right and I just we need to I think we need to own those

[00:16:25.34]  Jason ValleryIt's you right that cloud team. Well, it is because then they they connect back to the cloud. I mean, the pattern that OpenAI is...

[00:16:33.89]   RemoteWell, no, Jonesy's team is going to have to get involved here because in the RFP, right, is API integration. So they're going to want to be able to... no one's going to... they're not going to want to run into... run the VMS and use VCLI, right? It's going to need to integrate into Google's management framework. API framework, it's going to need to in their monitoring system, right? It's going to need to tie into all of that to really be successful. Yeah, I mean, you know

[00:17:01.95]  Jason ValleryIt has to like the billing control plane Management model has to be simplified and all integrated totally get that the the pattern that I see Emerging is what open AI for a while. They have like central data lakes that are multi-exabyte and scaled running on object storage in big hero regions, but then they get GPU capacity around the globe. They have like 50-something Azure regions where they get GPUs, plus now all these Neo clouds, plus all these new facilities, Oracle otherwise, and it really is like the GPU adjacent storage has to be like an extension of the central data. data spaces, plus our ability to have a common management plane, plus you know really smart caching is ultimately that holy grail that enables that topology to just make sense. Like that's actually what OpenAI built for themselves.

[00:17:52.47]   RemoteKartik and I just did a quick demo. We did it using TPUs. We wanted to run some TPU workloads. them to vast storage and it's hard to find those things and but the global namespace allowed us to i had a cluster set up in one region i knew it was there and we had it running and the tpus we secured them and then i just cast around to where i could find z3s and and tpus in the same region and then we stood them up global namespace boom running your tests and then shut it down. It was perfect. It was a great use case demo of, and I kind of like to call it, you know, escaping the data gravity well.

[00:18:32.52]  Jason ValleryYeah. Sorry. I just, I'm thinking about summation and make sure I wasn't ignoring him.

[00:18:37.69]   RemoteYeah. I do want to ask you something before we, we, so Lior was hinting about something that I would work for you?

[00:18:46.95]  Jason Vallery- I've heard rumors about that. I was waiting until Jeff finalized everything to mention it. Yeah, I think, you know, Jeff and I are sitting down next week for a couple of days to really do organizational planning stuff and figure all of that out. So, you know, I don't wanna make any assumptions at this point, but I think that's a potential outcome.

[00:19:06.09]   Remote- Okay, 'cause I get, people can. with an SE sometimes, and I think, but that's what Lior needs going forward. I think they're going to need that.

[00:19:14.53]  Jason ValleryBut anyway, I just was wondering. - I mean, yeah, okay, you know, the focus is, there's a bunch of different product things in flight. I don't know. What's your take on product ownership versus, you know, what you've been doing and, you know, what kind of thoughts do you have and how you could- I mean, it's about, it's much more about like taking what we hear from customers and what the SEs and fields are reporting as challenges, aligning that to a vision and strategy, and then driving that work through Yancey's team and Tel Aviv and making sure that we've got good discipline on tracking and holding them accountable and, you know, good definition requirements and you know, launching product by documentation, like all of that, that's the product name of what we need to get done is, is somebody who can wrangle Yancey's team plus wrangle Tel Aviv to a, you know, committed set of outcomes. That's, that's what is in front of me to go solve.

[00:20:13.29]   RemoteOkay. Yeah. know that we've needed that. I over the last year have probably operated quite a bit very much like a TME in a sense because we haven't had a product to sell. So I've been basically all the any POCs that happen, I've been doing a lot of testing in the field testing so I've uncovered a lot of bugs. You know, when you're doing stuff in a CI pipeline, they're deploying in the same regions all the time. I mean, just recently, I mean, when we were doing this project, I deployed in a new region and all the Terraform blew up because they're using Cloud Functions version 2.0, we're using 1.0. Engineering never saw that because they just keep deploying in that one same region all the time. to do their to do their QA. So I've known a lot of that and again all the all the customer POCs have produced a lot of documentation. Most of the documentation that's out there is I think now for me and I have so I've created POC guide, requirements documents, some how-to's on setting up some different things in the cloud. I mean that kind of that kind of stuff.

[00:21:23.14]  Jason ValleryWell, part of the vast stack and the vision that I shared, you know, excites you, you know, if there's one area of this entire problem space, because there's a lot of things you touch, where do you find passion?

[00:21:41.25]   RemoteI really think it's in the, well. I mean, I used to be a hardware guy. I was a hardware guy for a long time, and so that's-- but that's not relevant in the cloud. It's really the data space and how we integrate with the upstream tools. Upstream, that's our huge gap that we have in the cloud is use cases, is what do we use it for? I mean, so I think we have a what now problem. which is, you've installed Vast in the cloud, now what? We don't really, we can't answer that now what question right now, and we need to be more than just a file system in the cloud. If we're just gonna be another file system in the cloud, Cumulo, manage Cumulo in Azure, you go in, click, click, click, say how much you want, how fast. you want it, and then you get 10 IP addresses to mount an NFS file share on. Great. Where's the differentiation? If that's all we're going to be, then we're, I mean, where's our differentiation, right? Our differentiation is in the upper layers, right? It's in the Spark Trino, it's in the integration with Vertex, Bigtable, you know, these kinds of tools. how do we we have a lot of messaging around stream streamlining and simplifying pipelines well what does that look like in the cloud i don't think we know that yeah and so that's somewhat wrangling some of the the ai ml folks and the that was some of what kartik and i were

[00:23:09.76]  Jason Vallerywe're doing where's your technical passion like where do you are you hands on keyboard you want to Do you ever write code? Do you ever kind of get really, really dirty?

[00:23:19.30]   Remote- You should look at my, you can go look at my GitHub repo and that should answer that question.

[00:23:24.13]  Jason Vallery- Okay.

[00:23:24.94]   Remote- I'm definitely a hands-on. Python, I'm sort of, I can do Python, but I'm a bash, PowerShell, Terraform, Ansible. I love automating everything. I love automating stuff. things when before it was cool to automate them. I turned my laptop at Sun

[00:23:43.96]  Jason ValleryInto a jumpstart server to install E25K domains. How do you feel about AI in this world and how it helps you or hurts you in terms of productivity both from just day to day I'm gonna use it with my email versus I'm going to use it to write phone, like where do you see it?

[00:24:04.94]   RemoteYeah, so I use it in really, I think, three different ways, primarily. One is email. So let's say I run into a bug or I run into some kind of issue and I want a clear, concise, you know, no voice message. I'll type stuff up and dump it in and it'll, you know, kind of clean it up for me, and so I use it for that. of stuff writing code so if I'm you know what I mean I know I could write the terraform but it's going to take me five days if I do it from scratch right versus just saying here you know I already have a whole bunch of templates and stuff so I just drop them into chat gpt or gemini boom in a day I've got what I need right same with writing like Python scripts and things to automate stuff I mean so I these days if you're not using it you're you're you just you know now I don't know what young people like people just brand-new to coding or how that impacts them for someone like myself that's experienced I you know when I look at writing doing something it's kind of like okay here we go it's gonna take me four days versus now with the AI tools I can have it done in a day right or less but that's because I but I'm not I already know how to do it so I'm just leveraging the tool to make my work more efficient and faster and then the third one I use it be honest with you a search engine for example I'm I have to sit right now I'm working on a project where I have to set up a VPN tunnel between Azure and GCP it's I don't know how I got sucked into it but it's a smoke test for NCSU where they want to connect SAS via to a vast cluster just for just to test a couple simple things have a solution in Azure, I can spin up clusters in GCP all day long, reliably, quickly. So we determined, well, we can just set up a-- they said, hey, we'll set up a site-to-site VPN. So I have to set that up, and just debugging, getting that working, I mean, it's much faster than searching Google. Because you search Google, you're-- going to get someone's four-year-old blog post or medium article that's inaccurate, right? And using Gemini or PGPT, it searches the actual documentation and it gives you commands and stuff. So yeah, I love it. I think I could do my job just fine without it, but it would take me

[00:26:34.26]  Jason Vallerya lot longer. Yeah, I mean, you get more done in a day. my experience. My son is a sophomore computer science major right now and I just don't even know what his future looks like, but we'll see.

[00:26:49.92]   RemoteThree ways really just yeah an editing tool to clean up sensitive emails and things like that, writing code though I haven't integrated it with any of like I I love it. I'm a Windows guy. I went all in on Windows a long time ago because of Intel. They made it hard to use a Mac, so I switched up and so I've just been doing this a long now. It's hard to switch back, but yeah, I mean, I just, but I use them all the time, so yeah, it's pretty cool, and then Kartik and I, that was our project, so we were doing... that's one area where I want to focus more is the AI/ML workloads and utilities and things. I feel that that's an area where someone with my background, perhaps your background, can more easily slide in and learn that because it's, I have a degree in geology, so you know, I've taken linear algebra, physics, calculus, so I'm kind of not really a math guy, but I'm math versus say oh I'm going to go become a database person. It's hard to get there. Much easier. You know I and besides I like the AI. I mean it's cool. I mean they're I like the distributed systems. It's just another it's another big distributed system right.

[00:28:01.57]  Jason VallerySo I yeah I think it's fun. Oh I think that's the I mean the way to think about where we're going is it's a planet-wide distributed system. That's what we have to build, and so that's kind of the way I think about architecture for what the next storage platform should look like, is how do we build a client-wide version of NAST.

[00:28:19.97]   RemoteSo how do you-- let me ask you, so how do you-- so you're going to find-- and this is what I found when I first got here-- is, though it's less-- not as bad now, but to use the word tiering-- at vast is a really bad thing they don't like it but in the cloud we i i i'm beginning and i think leor was hinting that they're finally starting to realize that we we may need to fork orion in the cloud and refactor it basically nobody cares i mean yes we have a beautiful beautiful, very elegant, well-designed distributed flash translation layer that lets us give you a 10-year warranty on a QLC drive. Unheard of, right? But nobody cares, that doesn't matter in the cloud. None of that matters in the cloud, and if we want to be competitive from a price point, I mean, like Nasu... Uni, Cumulo, NetApp, Weka, maybe not so much NetApp, but Weka, Cumulo, they all write to S3. They can all write to S3 on the backend.

[00:29:26.31]  Jason Vallery- That's the problem. That's one of my like P zeroes, is if we can't scale capacity independently of performance, there's no play in the cloud. Being able to offload object storage is critical on that path, so. You know, we'll convince folks. I mean, there's a bunch of different things here that'll happen beyond just scaling out to an object that have to happen. Like, there's talks about even potentially other, like first-party, our hardware going into cloud data centers as potential outcomes. So all of that has to come into play to be successful there.

[00:29:56.02]   RemoteWell, there was a lot of resistance when I first got here. I mean, I had a number of conversations with people. So I worked for John Mao when I first got here, and there was a lot of resistance to the vast in-cloud type solution. That's gone now, I think. I think people are realizing, like this meeting we had today, now that Jonsi's team is here. I mean, they're bringing that expertise and that experience with them. I mean, and frankly--

[00:30:23.95]  Jason ValleryThat's kind of a gift that you keep giving. Yeah, Brendan and Jeff made it very clear to me. They're all in on the cloud. So that's my problem to go solve and figure out, and I'll partner with Yancey on that, and we'll figure it out. I got it, but like, let's find some more time. Like, I really appreciated meeting you. We'll, I'm traveling a bunch by the next few weeks with like supercomputing and meeting with Jeff. - So I'm gonna be at Supercomputing. - Great, we'll get coffee there and get to know each other better in person. Thanks for the time, man. Talk to you soon. Okay. - Okay, bye.

[00:30:56.88]   Remote- Bye. (mouse clicking) You (mouse clicking) You (mouse clicking) (mouse clicking) (mouse clicking) I'm going to play a little bit of the music, so I'm going to play you a little bit of the music. Here we go. You So, we're going to go ahead and close this out, and I'm going to open it up to questions. So, I'm going to open it up to questions, and I'm going to open it up to questions, and I'm going to open it up to questions, and I'm going to open it up to questions, and I'm going to open it up to questions, and I'm going to open it up to questions, and I'm going to open it up to questions, and I'm going to open it up to questions, and I'm going to open it up to questions. You You You YouNO SPEECHNO SPEECHNO SPEECH You you YouPause for group work Thank you so much for joining us. Thank you. Thank you. Thank you. YouBLANKBLANK you You (silence) You You (mouse clicking)Pause for group workBLANK (audience laughing) Yousilence You You www.circlelineartschool.com You (upbeat music)BLANK
```

<!-- ai:transcript:end -->
