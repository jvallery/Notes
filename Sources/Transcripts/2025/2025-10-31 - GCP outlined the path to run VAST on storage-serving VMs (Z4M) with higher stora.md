---
entities:
  customers:
  - '[[Google]]'
type: transcript
source_type: unknown
date: '2025-10-31'
---

# 20251031 0933 Parallels Transcription

**Date:** 2025-10-31  
**Participants:** Jason Vallery, Billy, John Downey, Lior

## Summary

GCP outlined the path to run VAST on storage-serving VMs (Z4M) with higher storage/network density, co-placement via the upcoming Google Supercomputer (GSC) interface, and future RDMA/GPUDirect enablement with A5X GPUs (TPU RDMA later). Discussion focused on decoupling capacity (HyperDisk), object-tier offload for metadata, and handling multi-region/neo-hyperscaler data movement economics. Anywhere Cache helps cost but not performance; local SSD remains the initial choice due to latency. Parties agreed to meet at Supercomputing, involve GCP stakeholders (Ilyas, Dean), and for Jason to draft networking questions; GCP shared a link on Cloud WAN.

## Key facts learned

- GCP Z3 exists; Z4M is the next storage-serving VM with higher storage and network density.
- Z4M targets storage-serving use cases; CPU/RAM may be overprovisioned but pricing optimization is planned.
- GCP aiming to match storage bandwidth to network bandwidth for storage VMs.
- Co-placement and provisioning via a new Google Supercomputer (GSC) interface are in development.
- Local SSD chosen initially for VAST on GCP due to latency vs HyperDisk/GCS.
- HyperDisk decouples capacity and performance but has higher latency than local SSD.
- Anywhere Cache reduces intra-zone egress and operational cost but not object-store latency.
- GCP supports erasure across availability domains; target is larger AD counts (currently 8).
- RDMA enablement planned for Z4M and A5X GPUs; GPU Direct Storage to be supported.
- TPU RDMA will follow GPUs.
- Internal networking features (e.g., ILB) can add significant egress-like costs at high throughput.
- VAST marketplace launch on GCP is near; integration with Vertex/TPU considered.
- Customers often keep exabyte-scale data lakes in object storage and need mixed POSIX/S3 access.
- Cross-region/CSP/neo-hyperscaler data movement economics (egress) are a major constraint.

## Outcomes

- Agreed to meet in person at Supercomputing.
- Plan to set meetings with Ilyas (cluster program) and Dean (CTO/expert) during SC.
- Jason will prepare and share networking questions and formal requests with GCP.
- GCP shared a link about Cloud WAN for Jason to review.
- Acknowledged need to explore commercial constructs to mitigate egress/internal networking costs for partner storage.
- Consensus to evaluate object-tier metadata offload for performance and economics.

## Decisions

- Proceed with local SSD-based Z4M for initial VAST on GCP; evaluate object/HyperDisk tiers later.
- Coordinate in-person sessions at Supercomputing and include key GCP stakeholders (Ilyas, Dean).

## Action items

- [x] Schedule Supercomputing meetings and include Ilyas and Dean if possible. @John Downey ⏫ ✅ 2025-11-08
- [x] Draft and share networking questions and formal requests for GCP ahead of SC. @Jason Vallery ⏫ ✅ 2025-11-08
- [x] Review the Cloud WAN link shared by GCP and assess applicability to VAST data movement. @Jason Vallery 🔼 ✅ 2025-11-08
- [x] Explore commercial constructs to mitigate inter-region and egress costs for VAST and joint customers. @Myself #cloud ⏫ ✅ 2025-11-08
- [x] Confirm RDMA and GPUDirect Storage enablement details and cost implications for Z4M and A5X, and share the plan with VAST. @Billy 🔼 ✅ 2025-11-08

## Follow-ups

- [x] Evaluate feasibility/timeline for a higher-performance object tier (e.g., S3 One Zone–like or Premium Blob–equivalent) suitable for VAST metadata offload. @GCP Storage 🔼 ✅ 2025-11-08
- [x] Analyze performance and design implications of metadata offload to object storage for VAST on GCP. @Jason Vallery 🔼 ✅ 2025-11-08
- [x] Scope integration of VAST as a selectable storage option within the Google Supercomputer (GSC) provisioning flow, including auto-deploy and co-placement. @Billy 🔼 ✅ 2025-11-08
- [x] Define path and timeline for RDMA enablement on TPUs and implications for VAST deployments. @Billy 🔽 ✅ 2025-11-08
- [x] Engage GCP networking and pricing teams to reduce ILB/internal egress costs for storage-serving partner solutions. @John Downey ⏫ ✅ 2025-11-08

## Risks

- High inter-region and cloud egress costs could block feasible data movement at scale.
- Object storage latency may not meet performance needs for metadata unless a higher-performance tier exists.
- Overprovisioned CPU/memory on storage VMs may impact cost efficiency until pricing is optimized.
- Internal networking constructs (e.g., ILB) can incur prohibitive costs at multi-TB/s throughput.
- RDMA for TPUs is not available initially; timeline uncertainty affects planning.
- Customer willingness to adopt a VAST-managed SaaS model is unclear.

## Open questions

- Will GCP offer a low-latency, high-performance object storage tier suitable for VAST metadata offload, and when?
- What commercial construct can reduce inter-region and egress costs for partner-led data movement?
- What are the GA timelines and prerequisites for RDMA and GPUDirect Storage on Z4M and A5X, and for TPUs afterward?
- Can HyperDisk satisfy latency requirements for metadata/control paths or future tiers of VAST?
- How will GSC automate storage–accelerator co-placement and VAST auto-deployment for customers?
- What networking architecture (e.g., Cloud WAN) best supports multi-region and neo-hyperscaler data movement for VAST?
- Is there customer appetite for a VAST-managed SaaS on GCP, and what compliance/trust requirements would apply?
- What AD/erasure coding configurations will be available to partners on Z4M to optimize durability and cost?

---

## Transcript (auto)

```text
[00:00:00.04]  Jason Vallery>> Nice to meet you. I see Leora is kind of here. Are you here, too?

[00:00:07.00]   Remote>> Sorry, who was that? You broke up.

[00:00:10.09]  Jason Vallery>> I was asking if Leora was here. I see him, but I don't hear him.

[00:00:14.01]   Remote>> Hey, I'm here.

[00:00:15.00]  Jason Vallery>> Hi.

[00:00:16.00]   Remote>> I am. Sorry, I was just on the same chat that you were on, sending you a message to And then I forgot to put to open the video Okay, so set up Jason just joined from Microsoft Microsoft experts of many years or VP of product management Billy is the most amazing partner. We have from all CSPs on the technical front business front partnership front and we spoke earlier this week and at that stage where we're about to launch we have the marketplace, Polaris, Billy knows all the details, the data plane, the cluster we're building and at this stage I wanted Billy to expose to you his two cents on how do you take kind of having something that works to being fully integrated as a solution on GCP so we can start. start prioritizing the next step of our partnership, and since you guys are both at supercomputing, you should also meet in person come supercomputing.

[00:01:17.57]  Jason Vallery- Yeah, that sounds great. Go ahead, Billy.

[00:01:20.19]   Remote- I was just gonna say, yeah, we should definitely try to meet in person. I was just actually gonna see if John could help schedule some meetings that week. if you'll be around. Lior, are you going or no? Supercomputing? Yeah. I'm presenting in your booth, so I guess that's right. All right. Yeah. You said it as if you weren't going anymore, so I was just confirming. No, no, no, no, no. It's like we have, we have Billy presenting in our booth. Thank you, Billy. I'm presenting in yours, and I am coming to supercomputing. I just think that, again, I'm happy to have a VP of Product Management on our side that really understands cloud before you understand storage. So I think we can take it to the next level and to figure out how do we move forward from here. Yeah.

[00:02:05.57]  Jason ValleryI think that makes sense. Yeah. So, I mean, you know, my background is I've been working at Microsoft the last 13 years up until two weeks ago, focused on Azure, and so part of the product management leadership team in various hats and so got a lot of cloud knowledge, a lot of storage knowledge in particular, and, you know, my goals here are how do we make Vast on Cloud, you know, the best experience for our Vast customers. Yeah, really excited about Google and understanding what we need to do there, and so that's a learning opportunity. for me because I have less experience running on GCP. Pretty good understanding of Google's storage platform, I've done plenty of competitive analysis work in the past around GCS, but the broader Google platform in terms of marketplace and VM instance types and all of that is something I have less familiarity around, so I'm looking forward to it. of picking up that knowledge and then just learning how we integrate ourselves with you guys. That's

[00:03:05.99]   RemoteWhere I'm at. Very cool. Great to meet you. I've been here at Google for the past, let's see, what is it? October. So I think in about two weeks, I'll have eclipsed five years at Google. Before that, I spent a number of years... at a company called Scality, and then a company called Nexenta, and then several years at Dell. So most of my background is almost entirely in storage backup and DR. So a ton of experience with storage, both hands-on engineering roles and partner-facing roles. Yeah, so maybe some I'm trying to think where to start. I think the best maybe the best best way to start is to give some context about where we started, where we're going. So I started speaking with VAST probably two plus years ago. At the time it was Tomer and John Mao who were primarily interacting with me directly and we have gone back and forth. We've gone back and forth for, I think, almost a year, 18 months on what a vast architecture on cloud would look like. At the time, Google had what I would consider compute-optimized instances. We didn't really have storage-optimized instances, and late last year, that changed with the launch of Z3. Z3 is our-- our first storage optimized VM, and I use the word storage optimized here to mean that it's optimized for, primarily optimized for compute workloads that are leveraging local storage. I think it's a step in the right direction for storage serving use cases because we have. a larger storage density per VM, we also have a larger network density per VM, but we recognize that this shape is likely still not the right shape for long-term where we want to be for the storage serving use case, and so we over the The last 6-12 months have been engaging tightly with VaST to define what our next gen, actually first gen, storage serving VM will look like. The idea is that we continue to ramp up the storage density as well as the network density and we try to match the storage. bandwidth to the network bandwidth because as a storage serving VM anything that comes off disk is going to hit the network to a client somewhere, and the end goal would eventually be that we also right size CPU and memory. Now I don't think we're getting there with the Z4M, but ultimately the the I think the goal would be that we get the pricing right, and so when you look at like a Z3 or even the Z4M, it's way over provisioned from a compute and memory perspective. But with the Z4M, what we're gonna do is find a way to optimize cost for these storage serving use cases, even though, even though. it's way over provisioned from a vCPU and memory perspective. So that's kind of where we're going. In addition to that, we have also been working on, how do we make these VMs-- so how do we look at the kind of end-to-end workload? So with AI, ML-- HPC, we have these storage VMs and then we have these accelerators or compute VMs and today you provision those VMs with no knowledge of one another and they land in the data center somewhere and then they you attempt to connect them and you realize that hey they might not have been optimized from a from a speed of light you know. location, proximity, perspective, and so where we're going, and so as part of the Z4M program, there's a number of things we're doing to optimize kind of co-placement. So when you look at like training or inference, and you actually provision one of these, what we're calling them supercomputers, we're gonna have this new interface. It's called the Google Supercomputer, and it actually might be called something else. We changed the name so many times, so forgive me, but you might hear it called GSC or Google Supercomputer, and it might even be called something else at this point. But really, it's this new interface for provisioning HPC, AI/ML infrastructure, and as part of that, the Z4M, and Vast as a partner has the option to be integrated, and so when a partner, when a customer comes in and says, I want TPUs and my storage solution is Vast, they can make it, put in a request and we optimize that for TPU placement. We, and then where I think one of the places we want to go can also work on automating the deployment of VaST as, I'll say, kind of like a first party citizen within the UI for customers who want to use it as their storage option. So in addition to that, we're also looking at how do we continue to make storage more persistent on Google Cloud. right? You probably have local local ephemeral storage. These Z4Ms are based on what we call local SSD. We're also, you know, putting a lot of effort into how do we make these more persistent? How do we give partners like yourself the ability to provision across what we call availability domains? So think of them as like logical racks, right? So when you lay out your storage, you want code across racks and different failure domains so that we do maintenance or on the top of racks which fails we don't take the entire cluster down. GTP has eight zones compared to Azure which is only three that's already a bit of starting point here. Yeah so we have eight and we continue to explore how we can increase that even further right because I think the the bigger AD count we can support, the more cost-optimized we can be, 'cause we can use a larger erasure coating stripe, which means we have less overhead for durability. So yeah, that's kind of directionally where we've been collaborating and where we're going, and I think as we launch on Marketplace, we can then kind of branch out and start to think about how we integrate more broadly with the Google ecosystem. So as an example, we did some, some TPU testing recently, more like AI infra type testing. We could also, you know, begin to look at how, how vast could integrate with Vertex, which is our AI platform for things like. RAG, or inference, depending on what your customers or Google customers are asking for. Yeah, so I'll stop there. I kind of did a lot.

[00:10:19.88]  Jason ValleryAny thoughts on decoupling capacity from the VMs and offloading an object here and being able to scale out the data? sets and you know where that evolves and any recommendations or thoughts on how best to do

[00:10:36.02]   RemoteThat within Google's platform? Yeah so I talked exclusively about local SSD you know as we as you know we also have Google Cloud Storage and we also have we just launched our next and block platform I think last year called HyperDisk. which is a persistent block storage layer and it decouples capacity and performance so customers can independently provision storage capacity and storage performance. I think the big difference and one of the reasons why we didn't go that way here amongst us is that the latency profiles are different for HyperDisk which is of network-attached storage and GCS, which is obviously network-attached as well, versus local SSD. So I think, again, where VASP was with their architecture and the lift and shift we did from on-prem, I think it made sense to lead with local SSD. I think 100%, I'd love to get to a point where we do support that. like object storage to augment the the economics of the solution right so we didn't have to keep everything in in a primary tier we can move it out to object store at two less than two cents a gig um i think that that could be uh that could be very interesting

[00:12:01.87]  Jason Vallerydo you have a high performance object storage tier kind of in thinking

[00:12:06.46]   Remotein terms of low-latency premium blog yeah we don't have so there are some things on the roadmap I don't know that they I'd be happy to bring in I don't I'm not educated enough on them at the moment I think to talk about it intelligibly but I think we we do have some things on the roadmap that, uh, I think more directly relate or, uh, compete with, uh, I think the S3, S3 single zone. Yeah. One zone or, or I don't know, Azure is Azure premium blob kind of a, do you consider that an equivalent or.

[00:12:40.57]  Jason ValleryYeah. Azure, I can have a little bit of pride in it. Yeah. We ship premium. off five years ago when it's all SSD-backed object, and then not follow up with Express One's own, and then I didn't see anything out of Google, so I was just curious if that was going to be an option for us. Because certainly, when you think about offloading capacity and you're trying to be performance-optimized, placing metadata there and being able to rehydrate from that So I'm just curious where your roadmap sits.

[00:13:11.89]   RemoteYeah, we could definitely explore that together. We have a couple of things. So we have Anywhere Cash, which at least at inception, the idea was that it would be both a opportunity to optimize operational cost and reduce inner zone egress costs in a region. and egress costs, as well as performance. It ended up launching only targeting, solving for the first two, and then, but I think there's still some work being done there with Anywhere Cache, as well as kind of an S3, one zone Azure premium blob plan as well, and again, we can explore that if, if, if. if that's an area of interest.

[00:13:54.41]  Jason Vallery- Yeah, we need to do some analysis on true performance benefits in our scenarios, but it's certainly a direction I'm gonna push towards is for metadata offload to leverage an object tier that gives us a little better latency. I don't know, what else should I know about the platform that'll help guide? our thinking as we evolve this. I mean, I'm sure Liora and others have shared the vision, but it goes in multiple click stops of what's going on in market today. I mean, if we're all honest with each other, it looks a little bit like lift and shift to a offer that'll be much more deeply integrated in the cloud primitives, and in that world, what are the opportunities for us? to have a differentiated product on Google.

[00:14:39.84]   Remote- Good question. - TPUs is one of them. TPU integration is one. Our AI stack, carving out what swim lane you really wanna focus in on, specific to the AI stack. Differentiation in the context across Pipers, Jason, by the way, I'm John Downey, good to meet you.

[00:15:09.43]  Jason VallerySorry I'm late.

[00:15:10.40]   RemoteNice to meet you. I'm the partner manager. Billy's my partner in crime, managing VASA. I have all the high-performance file systems and primary storage players.

[00:15:17.10]  Jason ValleryGotcha.

[00:15:17.72]   RemoteSince I was going to compliment Billy of being a great partner, John is an amazing partner So this is the best thing to work with. Like we don't have a team as strong as that with any of the other CSPs. - Excellent. - Go again, go. - We're all storage geeks here, Jason. So I was EMC for about eight and a half years, NAS overlay for Solera, ha ha. Then Atmos for, you know, three years, ran the enterprise storage strategy for AWS. I had storage 2011, 2014, then a bunch of startups and then landed here, so that's my quick and dirty. So my job with Billy is to focus not only on co-selling and driving revenue together, but co-innovation is the big one. So TPUs is definitely a big one in our mind. There's some other solutions that I'd love to be first to market with, or attempt to be first to market with, kind of creating hybrid neo-hyperscaler solutions, which I'm not saying there's a ton of incoming requests from the field. It's one of those things that are already kind of happening. It's going to continue to happen, and I feel like the quicker that we solidify real solutions and architectures, showing hybrid with neo-hyperscaler. or maybe on-prem, I think that's gonna be of interest to many people moving forward, especially where training may be happening in venue A and inferencing may be happening in venue B. You could be using GPUs over in CoreWeave and then in the namespace, flip over to Google Cloud, use TPUs for inferencing, which are cheaper. They're cheaper. TPUs do less than GPUs. There's less in the stack itself. so it's cheaper. There's a play there. But yeah, so there's a lot of directions we can go from a co-innovation perspective. So yeah, we'll have to do the best that we can to educate you on our

[00:17:07.24]  Jason ValleryPlatform and kind of co-ideate on where to take that. So, I mean, one of the things I certainly look at is. I think you kind of touched on this, my experience coming from the Microsoft side is there's customers who have multi exabyte data lakes sitting in some central cloud region and they're getting GPUs across the globe in many, many different cloud regions. They're getting GPUs in the Neo clouds, they're maybe deploying their own GPUs and bringing their data to. where their view capacity exists is a key store mobile namespace problem. Google's got anywhere can. But, you know, what I see there is that's pretty much going to work within Google, and you kind of touched on this, maybe Neo cloud hyperscaler kind of scenario. I run into two problems. You know, I think Vast can help you. capabilities we bring, and, you know, cloud economics of egress fees and data movement and all of that. Like, where's that going and how do we work better on making this a end-to-end customer value proposition that makes sense versus, you know, just the crazy numbers associated with pulling data out of the cloud.

[00:18:22.86]   Remote- Great, great question. I'm not even necessarily set on where's the source and where's the target. So it could be, you know, sources in Neo and we extend namespace to do inferencing. So we wouldn't have any egress or it could be reversed or we would have egress that we'd have to maybe work on some sort of commercial construct to reduce that. I don't know how we would do that, but certainly it's all on the table to tinker with and think about.

[00:18:52.37]  Jason ValleryThe burst-to-cloud scenario that you refer to and the train-to-inference kind of burst-to-cloud scenario, they're interesting, but what I'm actually seeing is if you think about the actual data pipelines that the model builders are using, they're actually CPU-heavy. You know, they're running Databricks and Spark, and they're running, you know, a bunch of data transformation and ETL, feature extraction kind of processes at scale, and those things kind of naturally fit in a hero cloud region, because that's where that capacity is. It's also kind of spin up, spin down, and you know, the Neo clouds aren't deploying large quantities of CPUs. So what I'm more concerned about is like all of the data ingestion, the data source of truth is likely to sit in Hero Cloud CSP regions, and then getting that data from there to other regions within the same CSP to other CSPs and into the Neo clouds. So that's where I, you know, we could do a lot on caching, but that only solves the problem so far.

[00:19:52.94]   RemoteWhat do you mean by Zero Cloud?

[00:19:55.07]  Jason Vallery- I mean, you know, there's no secrets. Like what's happening here is all the hyperscalers have really big regions, a US East, as an example, and easy enough to go and deploy many exabytes of storage capacity and many millions of CPU cores in those places, and so when you think about large scale AI scenarios, that's where they're at, right? They're in the US East. U.S. East, U.S. West kind of regions with lots and lots of compute and lots and lots of storage. But then, you know, there's, oh, we're going to go spin up a small scale, small scale, you only region in Portugal, I don't know why I made that up, and how do you move the data from the central regions to where the GPU are, GPUs are efficiently from a network transport perspective, but also then just from an economics perspective. perspective. That's the open question I'm trying to think about.

[00:20:42.45]   RemoteWell, Billy, are you fluent on our networking cloud way and stuff? I mean, that's a potential little thing we could add in here. I don't think it's solving any major problems of physics, but we do have a nice little networking play, but I can't really articulate it. I'm not sure exactly. Well, I'm not sure what you're talking about, John. So we'll have to follow up on that. But I think the bigger problem is cost. Jason's saying like, when we're talking about moving large quantities of data around, we're always going to have the inter-region egress costs within cloud or the cloud to somewhere else, egress fees, if we go from cloud to, say, neocloud. or cloud to on-prem as an example and I think to John's point, Jason, I think we'd have to we have to come up with a commercial construct to solve for that and I will say that we haven't we used to have something like this for partners who are operating under a very specific partner model. So I think it's something that we could we could definitely explore if this is like if this is a use case we think we want to go and target. I will say like the one other thing I I think I'm seeing at least for some of our larger customers that the VAST is not able to do today is that a lot of a lot of these customers want to have their large data lake. in something like object store, but in NATO format, and then they have multiple different use cases internally. Some of them consume object direct, some of them actually want to consume through POSIX or NFS or et cetera, and so the ability to read and write data, we have one file, one object type thing. and from from vast objectories and hydrate from object into vast is also a use case where we're seeing. I think you're alluding to that sort of use case.

[00:22:43.47]  Jason Vallery- Yeah, I mean, what I'm specifically calling out a scenario I've seen quite a bit of Microsoft where there's customers who are reading and writing from their GPUs into some adjacent store. This looks like actually the GCS Anywhere Cash. Like, actually, I think you guys are ahead here, where they're able to get a local representation of a bucket that's sitting in a different Google Cloud region or in the multi-region storage class. It's that scenario, fundamentally, and being able to kind of replicate that, the economics of being a third party are a disadvantage, frankly. Google can offer Anywhere Cash, but then you've got your own pricing model for data movement versus what it means for a customer to take on those costs.

[00:23:23.20]   RemoteYeah, and I think, I think we're, so, you know, a couple of things to that, to that statement. One, I think Anywhere Cash, again, solves, solves the cost component. It doesn't necessarily solve the performance component. You still have object, objects. storage performance. So I think that's one advantage that Vast would still have in that scenario, and where, so two things we can, we could explore. One, we're actually doing this right now for, I guess, part of, so this is happening internally. We're launching, I think one thing I forgot to mention to you earlier is that as part of the Z4M. program. We also will be launching or supporting RDMA, and so Z4M plus our next-gen GPU instance, A5X, will be the first two GPU and storage instances that are RDMA-enabled, and GPU direct storage will be capable once those two things launch.

[00:24:23.18]  Jason Vallery- Will that work with the TPUs as well?

[00:24:26.86]   Remote- TPU, RDMA for TPUs will come after GPUs.

[00:24:34.27]  Jason Vallery- Okay.

[00:24:36.60]   Remote- Well, I lost my train of thought. Where was I going with that? I think where I was going with, yeah, where I was going with that is that, you know, when we do launch RDMA, there are some different networking features that we'll need to leverage to support certain models, and those networking features come with a cost today, but those costs, their egress costs, internally egress costs, because they leverage things like ILB, which is not economical for these use cases. we're talking about pushing like five terabytes a second, we're talking hundreds of thousands of dollars a month. So we're already working through, ideating on how we solve for these cost issues in customer tenant for 3P vendors such as yourself, and I think we could potentially piggyback on that in the future on how we solve this for, If we want to continue down the VM based model for serving, for providing that's the customers. Now, where I think this can get a lot easier would be if the customers have an appetite for SAS, and I think that's something that you, a conversation you probably want to have with your customers to understand. I've heard conflicting things in the market about whether some of these large customers would be willing to trust their data with a third-party provider. But if they were, and Vast wanted to go down the SaaS route, I think negotiating these things and building constructs with Vast one-time. is much simpler than trying to solve for this in a programmatic fashion across, you know, the entire customer base, as an example.

[00:26:23.44]  Jason Vallery- Yeah, completely agree. Yeah, makes sense. Well, I'm looking forward to meeting in supercomputing. Are you both going to be there?

[00:26:31.76]   Remote- Yes.

[00:26:34.24]  Jason Vallery- Excellent.

[00:26:35.14]   Remote- I'll be there. - Did you book, John? I know you're still... - Yeah, I'm going from New York to Chicago and I'm going from Chicago to St. Louis and it's, you know, nothing simple these days. So yes, I'll be there, I'll figure it out. - What about setting up a meeting with Elias? Elias, the guy who was responsible for the cluster program so we can have a discussion with him. I know he's going to be busy, but again, it's a good opportunity to meet him. - I'll chat him right now, sure. So, I think Ilyas, I'd also like to try to get Dean in a conversation. I know he hasn't been updated in a while. I agree. So, maybe both at the same meeting or different meetings. So, Dean is kind of the CTO, the expert, the guy that whispers to everyone and everybody listens to him. Extremely knowledgeable and extremely supportive. So, that's an important one, Dean. and yeah the guy who is with the program of the super cluster or whatever the name is going to be

[00:27:28.92]  Jason ValleryAnd what is um well i mean because i have a lot of questions about networking obviously it would be useful to talk to somebody on your wan team or will any but probably nobody from your wan team will be there huh since it's supercomputing and not network world or whatever they do i don't know

[00:27:44.46]   RemoteAll right yeah i doubt it Maybe I'll be good, I don't think we'll have anybody from networking there, Jason, but if you if you have some ideas, like some rough ideas of what you're thinking and what we want to talk through, maybe we could start there and then we'll pull in the right teams to start those

[00:28:02.24]  Jason ValleryConversations. Okay, yeah, let me noodle on it still some more and then we'll come up with a more formal set of requests. Okay. Yeah. Okay.

[00:28:11.10]   RemoteAPL win, I guess, right? You're going to celebrate tonight. Go for it. Yeah. I'll be, uh, I'll be trick-or-treating for, uh, I don't know. Hopefully I can convince my kids to, to call it early. can't really see it in the day but it's lights up. It's the worst costume ever but I literally didn't have time to get a costume so this thing like lights up and I'm just gonna be like, I don't know, a tech man or some stupid shit like that. I have no idea. New York's the best place to be for Halloween. It's incredible. How does that work? Do people just, everyone just pull out a lawn chair and sit outside or what? The whole, some of these neighborhoods... You literally can't even drive people have kegs on the sidewalks and these townhomes are just completely covered and Halloween stuff It looks like a movie set it's it's it's so intense So yeah around three, I'm gonna probably cut out and we're gonna camp out at this little corner restaurant. Just watch watch people That'd be fun so share a couple of pictures. I've never seen Halloween in New York. If there are interesting stuff to take a picture of, share a couple of pictures. - Absolutely. Oh, it's incredible, man. It's like, it's a whole other level here. People get really into it. - Okay.

[00:29:29.25]  Jason Vallery- I got to go, I'm standing at a call, sorry. We'll talk soon.

[00:29:31.95]   Remote- Cool, cool. Yeah, did you see the link John shared, Jason? I'm just clicking on it. That was cool. I'll take a look. - Yeah, grab that link. our cloud way offering which I'm not very articulate well but we can we can

[00:29:45.12]  Jason ValleryVisit that as well. I'll take a look at it. Thanks guys.

[00:30:00.78]   Remote(clicking)

[00:30:24.00]  Jason ValleryHey, what's up, man?

[00:30:32.38]   RemoteOh, let me get this fixed here. How's it going?

[00:30:40.61]  Jason ValleryHey. Hey.

[00:30:42.61]   RemoteHow's life? Yeah. Crazy busy. moved across the country and
```
