---
entities:
  people:
  - '[[Rosanne Kincaid–Smith]]'
type: transcript
source_type: unknown
date: '2025-10-22'
---

# 1:1 — Rosanne Kincaid–Smith — 2025-10-22

> [!info] Purpose
> Build trust, surface and remove blockers, align on priorities, coach & grow.

## Summary

Rosanne outlined Dhammak’s rapid data center and GPU cloud buildout and interest in a marquee Microsoft partnership. Jason shared candid guidance on Microsoft’s in-house bias, risk-shifting to neoclouds, lease dynamics, and workload/placement constraints (training vs inference; fiber to hyperscaler hero regions). They discussed timing, risks, and positioning. Jason also highlighted VAST’s global namespace advantage for data following compute.

## Key facts learned

- Rosanne is based in Dubai; traveling from the Bay Area.
- Dhammak/Dimac diversified into data centers ~4 years ago.
- Dhammak has acquired nearly 5 GW of land/power and is constructing capacity.
- Approximately 500 MW to come to market by early next year.
- Plan to scale in gigawatt increments across Asia, the US, and Europe.
- Dhammak is building a vertically integrated cloud to serve AI workloads (GPUs).
- Seeking a marquee tenant relationship with Microsoft akin to CoreWeave/Nscale models.
- Lior is facilitating a Microsoft conversation with Anand.
- Jason recently joined VAST; previously led Microsoft Storage Platform and worked closely with OpenAI.
- Microsoft prefers in-house build but uses neoclouds to hedge risk and accelerate capacity.
- Microsoft pushed capex/asset risk onto neocloud partners rather than carrying GPUs on its balance sheet.
- Lease pullbacks were finance-driven uncertainty; leases resumed as demand materialized.
- Hardware life cycles are viewed on ~5-year horizons; depreciation viability is uncertain given accelerator roadmap pace.
- Workload mix (training vs inference) and multi-tenancy shape cluster design and placement.
- Sites without strong fiber to hyperscaler hero regions are effectively limited to inference.
- Neoclouds increasingly build near power sources; network backhaul becomes a bottleneck.
- Municipal permitting can delay hyperscaler builds (e.g., pushback in traditional metros).
- VAST’s global data namespace enables bringing data to distributed compute locations.

## Outcomes

- Rosanne validated alignment with Microsoft/neocloud market dynamics and timing considerations.
- Jason provided positioning guidance: act as capital partner absorbing GPU risk and ensure site fungibility and strong fiber.
- Shared perspective reduced board concern context by distinguishing lease risk vs neocloud risk-transfer models.

## Decisions

- (none)

## Action items (for Rosanne Kincaid–Smith)

- [x] Define Microsoft partnership positioning that emphasizes Dhammak absorbing GPU capex/risk with flexible, fungible clusters. @Rosanne Kincaid–Smith ⏫ ✅ 2025-10-26
- [x] Assess fiber/backhaul plans from candidate sites to hyperscaler hero regions to enable training-grade throughput. @Rosanne Kincaid–Smith ⏫ ✅ 2025-10-26
- [x] Model workload mix (training vs inference, single-tenant vs multi-tenant) per site to guide cluster design and customer targeting. @Rosanne Kincaid–Smith 🔼 ✅ 2025-10-26
- [x] Prepare an internal brief addressing board concerns on co-location vs neocloud risk-transfer models for Microsoft. @Rosanne Kincaid–Smith 🔼 ✅ 2025-10-26

## Follow-ups

- [x] Proceed with Microsoft discussions via Anand and update Jason on outcomes/timing. @Rosanne Kincaid–Smith 🔼 ✅ 2025-10-26
- [x] Share site connectivity and timeline assumptions to validate workload feasibility (training vs inference). @Rosanne Kincaid–Smith 🔼 ✅ 2025-10-26

## Risks

- Demand uncertainty for sustained GPU utilization over a 5-year depreciation horizon.
- Microsoft’s preference to keep builds in-house may limit neocloud allocations.
- Lease models place balance sheet risk on Microsoft, causing periodic pullbacks.
- Insufficient fiber connectivity to hyperscaler hero regions constrains sites to inference-only workloads.
- Rapid accelerator roadmap (NVIDIA GB/H series, TPUs/ASICs) risks asset obsolescence.
- Municipal permitting and siting challenges delay capacity timelines.
- Board nervousness about plain co-location given prior Microsoft lease step-backs.
- Potential margin constraints if capacity is mistimed or misallocated.

## Open questions

- What timing and capacity profile will Microsoft prioritize for Dhammak sites?
- Will Microsoft prefer a neocloud risk-transfer model or pursue plain co-location in the near term?
- Which workloads (training vs inference) will be targeted for initial clusters?
- Are planned sites able to secure sufficient diverse fiber paths to hyperscaler hero regions?
- Can GPUs be monetized/depreciated effectively over five years given rapid accelerator cycles?
- What permitting or regulatory constraints could affect Dhammak’s earliest capacity coming online?

> Next meeting (if any): (none)

---

<!-- ai:transcript:start -->

## Transcript (auto)

```text
[00:00:00.01] Jason Vallery :  Jason ValleryHi, can you hear me?

[00:00:01.80] Remote : Before I start speaking, yeah, sorry, I was just, I was on mute, so before you had to tell me I was on mute, so I just took a moment.

[00:00:08.75] Jason Vallery :  Jason ValleryHi, where are you from?

[00:00:10.75] Remote : Hi, nice to meet you. Yeah, I'm loving your retro styling in the background, this is very cool. It's like proper 70s, modern.

[00:00:20.85] Jason Vallery :  Jason ValleryI live in a, all kind of... historic house. So it's kind of a fun office that I have here. Yeah, that's good, and you're in the Bay Area right now. Is that what I read from the note?

[00:00:31.07] Remote : I, yeah, but I mean, this is just the Hilton in the background. I'm actually flying out this evening. I'm based in Dubai, and, but I seem to spend an awful lot of time Yeah, I suppose for obvious reasons, but I've been here since Sunday and I'm flying out

[00:00:54.77] Jason Vallery :  Jason ValleryAgain this evening. Well, I'm in my first week at Bass, so I don't know how much you know about me, Leora sent the introduction. I just joined VAST. I was most recently product lead for Microsoft Storage Platform and supporting all of their AI initiatives and the storage relationship with OpenAI, and I worked historically very closely with OpenAI, and so, you know, I know a bunch of the folks at VAST and decided to come over to this side and help them. them kind of with their vision around expansion into the hybrid scalers and expansion into sort of the frontier model builders and supporting all of that, and so my new role and I'm on day three at VAST is you know owning the product management organization to accomplish that mission. So that's kind of where I sit and what I'm up to. I'd love to hear from you like how I

[00:01:54.22] Remote : I can support what you're trying to accomplish. - Well, and Lior, just for your FYI, we're singing your praises. I think they're very happy to have you on board, so. (laughs) So I've known the Vast guys while I've worked with them for many years. My background is actually predominantly private equity and tech portfolio. and so I've spent a lifetime in technology and a couple of other interesting things along the way including banking, but the sort of use of scale, CPUs, GPUs for a variety of applications has been at the centre of a lot of my broader, bigger roles and then very most recently before I I was running a cloud business called Tiger, and that's where I got particularly well acquainted with the vast team. I left there about a year ago and just recently joined Dimac after spending an extraordinarily long time in the garden. I was bored to tears, but it was still good to rest before you start. start your new job and Dhammak is quite an interesting environment for a number of different reasons and predominantly because the group Dhammak group is actually a luxury residential real estate and quite complex community infrastructure so they build communities across Dubai. About four years ago, our chairman and the founder of DMACC diversified the business into data centers, and over the last three years has acquired nearly 5 gigawatts of power and land and has started to construct, and we will bring to market some 500 megawatts of capacity by early next year. and then sort of rolling gigawatts at a time across Asia, the US, and Europe, and because he's not one to stop at just that point of diversification, and obviously because he's now 75 years old and he is clearly bored. (laughs) He decided he's also going to start a GPS, and that's where I sort of came in, but of course, I've sort of moved the business along a little bit in terms of, well, we're not just going to do GPUs, actually, we're going to have a fully functioning vertically integrated cloud platform, which will obviously serve as AI applications. However, and the reason that, um, uh... Lyle connected us and so I have some sort of pending ongoing interactions with Microsoft because one of the core tenets of setting up a successful GPU business and certainly a cloud business is having a marquee tenant for your clusters and so in the same sort of fashion as what Microsoft have partnered with Core, Weave and Nscale and others, we have a a broader conversation with them to do the same, because a lot of the capacity that we can bring to market is next year, it's significantly earlier than some of the other players, so we're in a good position to have those conversations, and also, as I say, for a business of this nature, coming out the gates in that way is a very compelling proposition and catapults you into the main arena, I guess. which I think is imperative for the success of this business. So Lior is facilitating a conversation with Anand, alongside the other conversations that I was having, and he said we should connect because you know Microsoft really well, and how they have proceeded with some of these, I mean, obviously don't tell me things you can't tell me. me, but how they have sort of proceeded with these deals and on what basis, what does the sort of like cluster tech look like and I don't know, anything you can share with me that will help me to position both of our business as well, I think is where he thought you might, we could have a sort of productive conversation.

[00:06:00.16] Jason Vallery :  Jason ValleryWell, so a few things. You know, I'll be a little blunt about my take on the strategy here. You know, Microsoft prefers to keep as much of this in-house as possible. Like, you know, the mentality is to minimize the amount of capacity that they're buying from the Neo clouds but overlaying that with risk mitigation and hedges, right? So what that practically means, and also just looking at the realities of what the kind of deficits they have in terms of construction schedules and bringing new megawatts online themselves, and so Microsoft has a portfolio of data center expansion projects. They have an in-house data center team, in-house data center designs, construction contracts. supply chain contracts like that is Azure's bread and butter and something that they've been doing really well for 15 years now as Azure and even longer than that just supporting the Microsoft key infrastructure and so Microsoft still sees that as its path forward like it wants to do as much this in-house as they can but this sudden onrush of demand has caught, you know, all of this hyperscalers a little flat-footed, right? The way this historically worked was they would have data center plans five years in advance, right? Because, you know, from green light to construction to first power being brought online, it's a five-year construction schedule that they would have historically been operating on, and so you imagine most of the data centers that Microsoft is building. and owning themselves, you know, those projects were green lit, you know, five years ago, and so, you know, suddenly there's this world where the hyperscalers need to bring as much GPU capacity online as possible, and then they start looking at partners like CoreWeave and Scale, Nebius, et cetera. So that's part, part B, and then there's public reporting. that's even come out kind of about some information on the information, some leaks recently around Microsoft strategy on this and, you know, it's pretty much accurate of, you know, Microsoft is publicly traded. There's a lot of risk in this CapEx, you know, there was an interview with Satya where he kind of even alluded to this, like maybe six months ago, you know, key decisions were made around the expansion of, you know, should Microsoft go all in? in and make these Microsoft relationships, own the GPUs that go into them and effectively go to market with the Neo clouds in a model where all of the risk sits with Microsoft, meaning they're buying and they've got the deal with NVIDIA, they've got the deal with the supply chain, they're just dropping Azure Kit inside of it. of the data centers, and in that world, it's just a data center lease, right? Microsoft is space power, and they're leasing the space power from a third party provider that can bring it online faster than they can build it, and Microsoft does this. So there are a whole bunch of examples where Microsoft leases data center capacity from various providers around the world, and continue to do this and continue to expand in this model. But that then sits on Microsoft's balance sheet and becomes a risk in a world where they're overbuilt on the infrastructure side. Like if you look at the actual costs of what go into these data centers, the space power isn't the thing. It's the GPUs, right? And carrying all those GPUs on the balance is a risk that Microsoft didn't want to take, and so then they pushed that. risk on to the neocloud, and that's potentially going to pay off for those neoclouds. You saw reporting around this in terms of Oracle talking about how do you monetize one of these GPUs over a time horizon of the lifespan of it. Microsoft certainly thinks about hardware life cycles at five-year time horizons. So if you're going to make an investment in a GPU cluster or... storage cluster or a networking of the networking kit, you want to depreciate that asset over a five-year period, and so then there's all these questions emerging today around when you look at the pace of NVIDIA and their roadmap, you look at the diversification of accelerators with TPUs and ASICs and Broadcom's roadmap and Microsoft's first party roadmap and OpenAI. wanting to build their own accelerators and all of that coming into play, it starts to bring into question of like, can you actually depreciate a H100 or a GB200 over a five-year time horizon and continue to extract value out of it in a way that allows that whole picture to translate into margin positive revenue over five years? And can you continue to sell it in a way? that there's demand for it, and so the uncertainty around demand has led them to do a lot more of these partnerships. Um, that's pretty obvious to me. So what does that mean? Like, I think that you're coming into this from a perspective, like if you're coming into it with that ground truth of knowledge, that what you're really doing is you're a capital fund that allows Microsoft to remove itself from the risk matrix. Like If you're fully invested there, I think that you can make that partnership successful. That would be the first. Then the second point is like, what's the workload? So the other thing that happens when all these sites come online is that, you know, there's a bunch of things that kind of constrain which customers could go into which cluster to support which scenarios, and like broadly speaking, you've got training, you've got inferencing, and you've got customers that want to do both, and then you've got, you know, the multi-tenancy dimensions of that potentially as well. If you're talking about, I want to support a lot of smaller scale customers, or if I want to go into like one hero cluster and give that to one customer, like I'm going to go and give 12,000 GB200s in one facility to one customer. The maximum utility here is if you have flexibility, fungibility of how you deploy those data centers over time and be able to use different scenarios so that in that future state where you're leasing these things out to Microsoft and they don't need them anymore, you can repurpose them, reallocate them and continue to extract value. What that means then. and this is where I see a lot of interesting things happening in the neocloud space, at least here in the US, is that the neoclouds that are happening here, I'll give you Caruso as the primary example, they're going out and building infrastructure where the energy is at, right? So for in the US, that means like literally Caruso is going out to natural gas fields, building the data center on the natural gas field, and then figuring out how to connect it to the network. Like the InScale example in Portugal looks a little like this too, and then you've got this problem, right? Because the way the workloads actually behave is that the data, and we're talking about potentially many exabytes of data, is already going to be located, its primary system of record, the durability of it, is already going to be located in one of the hyperscalers, Hero. regions, and these are the traditional regions, the U.S. East, the U.S. West of the world, and so then the question becomes, how much fiber can you get from this random site in the middle of Portugal, this random site in the middle of Wyoming, to one of these hero cloud regions to interconnect it and deliver the throughput needed to move that data in and out of the GPUs? And so you have look at that problem, and so if you're deploying an asset in a place where that network fiber doesn't exist, it'll limit you to pretty much inferencing only kinds of workloads. But if you're deploying that asset in a place where you can go and connect it back to large fiber paths into one of these hero cloud regions, then you have diversification of the types of that can run it, and so understanding those dimensions are also key to how you place your investments and where they're at physically in the world. Yeah. That's

[00:13:39.31] Remote : my two cents. Okay. No, that's super helpful. I mean, I think that's very consistent with my overall understanding of where Microsoft ads and what the market is doing and that sort of thing. that's sort of helpful and very validating. I guess it's sort of, I mean, if I could say, it's all kind of down to timing, right? The interaction with Microsoft and what we can do together will be pretty much dictated by that timing. I think the other thing that we are, I mean, obviously it doesn't suit my business line, but of course we do have. data center business too, we do obviously have capacity that we could lease for co-location. Now, there was a little bit of, and I'm interested in your view here, nervousness I guess from our board around engaging Microsoft for actual co-location, that plain co-location capacity, and hence, but obviously because because I have a relationship, I've been talking about the GPU stuff, but because they stepped back on a number of leases a little while ago, but based on what you're saying is that maybe that's because there's been some acceleration in their own construction schedule. I mean,

[00:14:53.38] Jason Vallery :  Jason ValleryThere's a variety of things that happened there. I think that actually Microsoft made some mistakes there and then they unwound about a bunch of those decisions pretty quickly. quickly after making them, the step back on the leases was driven out of this uncertainty that the LT at Microsoft had, Sacha, actually mostly coming out of the CFO, Amy Hood. They were looking at this purely from a balance sheet perspective, going out to street and hitting earnings per share in a world where they were going to take on all of these leases. they weren't convicted that they had a customer for them, and that they would be able to fully utilize the capacity, and so they stepped back from those leases, but then subsequently that demand is materializing, and so what's that's meant is that then they go back out and they're signing more leases, and so I think, the lease model also, like I highlighted, has this inherent risk that Microsoft is on the hook from a balance sheet perspective for all of the infrastructure in the facility, and so this NeoCloud option allows them to diversify that risk and push it back to the NeoCloud and the NeoCloud's investors instead of carrying it at Microsoft, and so it's just shrewd finance. financial planning from the CFO versus a statement of demand.

[00:16:12.84] Remote : Interesting. Okay. We like a shrewd CFO.

[00:16:21.20] Jason Vallery :  Jason ValleryLike she's the rockstar of the industry. I've had the pleasure of meeting her a couple of times.

[00:16:27.56] Remote : Microsoft's pioneered this kind of... this kind of contract provision, this kind of engagement, they've pioneered it, haven't they? I mean, that's obviously her good thinking, helps manage the balance sheet. (laughs)

[00:16:40.79] Jason Vallery :  Jason Vallery- I mean, how it plays out may, like, I don't see Microsoft as being overly exposed as a result of this. I see them potentially missing out on margin opportunity, being put in a constraint in terms of capacity as a result of this kind of thinking.

[00:16:57.58] Remote : - I mean, I think this game is very much about market share, right? If you've got the capacity when the customer and that becomes the longer term play, managing, having a slightly lower margin, it's kind of absorbed because you've got scale. - Yeah.

[00:17:15.32] Jason Vallery :  Jason ValleryIts own challenges, and these are public things that are reported in the press around its expansion and its traditional locations. You know, Microsoft has historically invested in real estate in major metros around the U.S. that are well connected to the Internet and they haven't gone with the crew. So I'm going to build in the middle of nowhere model, and so there's a lot of pushback from municipalities. I mean, notoriously, like Microsoft has a huge investment in Wisconsin, and it's been all over the press and, you know, Wisconsin's turning down permitting approvals and things like that because of, you know, what it means to be a noisy neighbor. There's a lot of that going on too, and so that means a shift in strategy as well and, you know, trying to develop new locations that puts timeline pressure on them because those weren't necessarily projects in flight.

[00:18:00.39] Remote : Happening as well, that puts them in a bit of a bind. Yeah, agreed. Okay, that's very helpful. So, how have you found your first few weeks at Vast? Well, you know, I

[00:18:13.58] Jason Vallery :  Jason ValleryObviously have known the guys at Vast for a little while and folks that I've worked with in the past have already made the transition to Vast. I mean, it's great. I wouldn't be here if I wasn't I'm a storage engineer and I've looked at this problem space and what it takes to train models at scale. Like I said, I worked closely with OpenAI and when I look at all of the vendors out there, VAST is just light years ahead of everyone else, including the hyperscalers in terms of the technology they have in the stack, and then the key-- The key market opportunity that Vast has that none of the hyperscalers have is that when you look at the problem you and I just discussed around diversity of locations where compute is going and being deployed, these things are going into, you know, ad hoc data centers are going into these NeoCloud, you know, when you're a large scale customer, you need to have a single global namespace of your data. data that is connected to the compute, and, you know, that is a unique set of capabilities that BaaS really bring to market. One of the things that Hyperspace said for years, and this is kind of like the design strategy of the cloud is that if you bring the data to the cloud, data has gravity, and then the compute follows the data. So this is like the paradigm that. Azure and AWS and Google have been built on, like it's why they have such high egress charges is you get the customer to take all their data to the cloud. Once it's there, then you just sell them all the compute in the world to go and process, analyze, whatever that means in terms of the data. But that world is just fundamentally been flipped upside down because now the compute is chasing the power. What that means is you need a storage platform that can bring the data to the compute and VaST is really the only one that has that with the global data namespace. So for me, that was the key selling advantage of why I should come to VaST is because I know they already have the technology that's going to take us through this next wave of infrastructure build-out and we'll be differentiated in the market.

[00:20:12.79] Remote : Yeah, I've been very impressed actually. by the development of what Vast offers. I mean when I first met the guys it was pretty like, not very different to pure storage. If I remember them pitching me and being, I was like this is not any different to what we had already, but it's now I mean what they've what they've showed me over the past few weeks I've very impressed by it. It's large years ahead of where others are and certainly where they were a couple of years ago.

[00:20:45.62] Jason Vallery :  Jason ValleryYep, I think it's going to be a wild ride. The amount of growth in front of AST is huge.

[00:20:51.80] Remote : Yeah, exactly. Well, thank you very much for your time, Amir.

[00:20:57.34] Jason Vallery :  Jason ValleryUh-oh, I lost you.

[00:21:00.40] Remote : Thank you. Thank you.

[00:21:05.14] Jason Vallery :  Jason ValleryThank you.

[00:21:06.39] Remote : Thank you. Thank you. (computer mouse clicking) YouSilence from 1 minute to 1 minute 40 seconds (upbeat music)BLANKAUDIO

[00:24:45.46] Jason Vallery :  Jason Vallery(bell dings)

[00:25:07.96] Remote : You I don't know if you can hear me, but I want to thank you for the opportunity to be part of this. I'm sure you've all been watching this. I'm sure you've all been listening to this. You (keyboard clacking)MUSIC
```

<!-- ai:transcript:end -->
