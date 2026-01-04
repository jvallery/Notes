---
type: transcript
title: Strategy sync on VAST, Apollo, and MAI
date: '2025-11-06'
entity: Kanchan Mehrotra
folder: People/Kanchan Mehrotra
participants: Myself, Kanchan Mehrotra
tags:
- type/people
- entity/Kanchan Mehrotra
source: 00 Inbox/Transcripts/20251106 1259 Parallels Transcription.txt
entities:
  people:
  - '[[Kanchan Mehrotra]]'
source_type: unknown
---

# Strategy sync on VAST, Apollo, and MAI
**Date:** 2025-11-06 · **Person:** Kanchan Mehrotra · **Folder:** People/Kanchan Mehrotra

> [!summary] Executive Summary
Discussion centered on accelerating VAST adoption within Microsoft programs (MAI, Apollo) and navigating internal hardware/storage paths. Jason shared major momentum: VAST’s ~$1.2B software-only deal with CoreWeave. Apollo (via Qi) asked VAST for two POCs: (1) urgent VAST-on-VAST hardware (rack already shipped), and (2) running VAST bare metal on Azure storage hardware; specs include Fungible DPU and NVIDIA BlueField-3. Concerns were raised about Fungible readiness and political dynamics under Manish’s org. For MAI, Dallas capacity tranches are coming (Dec and April), and there’s interest in exploring VAST on classic Azure (Overlake/SDN) to meet performance and timing. NVIDIA’s DGX Cloud reference storage requirements strongly favor VAST (and Weka), suggesting a leverage point with leadership (Nidhi, Renan). A pragmatic path is to engage Michael Myrah (Azure Storage Hardware) to co-design a VAST-optimized Azure storage SKU, with Kanchan seeding this with Nidhi and sounding out Kushal on feasibility for Dallas. Potential meeting at/around Ignite with a deeper follow-up in Redmond was proposed.

## Relationship Context & Key Facts
- VAST signed a ~$1.2B software-only licensing deal with CoreWeave (press same day).
- Apollo asked for two POCs: urgent VAST-on-VAST hardware and VAST bare metal on Azure storage hardware.
- Azure storage hardware specs shared include variants with Fungible DPU and NVIDIA BlueField-3.
- Fungible production use in Azure storage is still not broadly delivered, creating risk.
- MAI is the initial single-tenant customer for Apollo; long-term goal is multi-tenant/3P.
- UK Met Office: VAST POC interest via Mike Kiernan in a Canary region (separate from Apollo).
- MAI Dallas capacity: first tranche in December and a larger tranche in April; storage plan not finalized for April.
- Classic Azure path would require VAST bare metal on Azure storage hardware with Overlake/SDN integration.
- NVIDIA DGX Cloud reference storage throughput requirements: only VAST and Weka pass today.
- VAST argues Lsv4/Lsv5 VM deployments are impractical for exabyte-scale (power/rack inefficiency).
- Proposed path: co-engineer a VAST-optimized Azure storage SKU under Michael Myrah’s team.
- VAST is open to an all-you-can-eat software license model for Microsoft.

## Outcomes (What moved forward)
- Aligned to explore a hardware-led path via Azure Storage Hardware (Michael Myrah) for VAST bare metal.
- Agreed Kanchan will discreetly seed the idea with Nidhi and confirm support before engaging Myrah.
- Kanchan to reach out to Kushal to gauge MAI appetite to push VAST-on-classic-Azure for Dallas.
- Identified NVIDIA DGX reference storage requirements as key leverage in leadership discussions.
- Tentative plan to set a focused session with Nidhi/Renan (around or outside Ignite) for a deeper dive.

## Decisions (Agreements & rationale)
- Prioritize a storage-hardware path (Myrah’s team) over VM-based approaches for VAST performance and scale.
- Use MAI-driven demand (via Kushal) to advance the Dallas April window for a VAST bare-metal option.
- Position NVIDIA DGX storage compliance as strategic justification in executive conversations.
- Avoid opening a direct thread with Myrah until Nidhi’s support is secured.

## Risks (Interpersonal or dependency)
- Political resistance from Manish’s org to non-Blob, bare-metal VAST on Azure storage hardware.
- Fungible DPU readiness remains uncertain; dependency could stall Apollo timelines.
- April Dallas timeline is aggressive; engineering and networking integration may slip without quick alignment.
- Cross-organizational coordination gaps (MAI, Apollo, Storage, Dedicated) could create ownership confusion.
- Insufficient leadership air cover could block hardware SKU changes needed for VAST.
- Capacity planning without adjacent storage could constrain future GPU workloads.

## Open Questions
- Will Kushal sponsor a formal exploration of VAST bare metal on classic Azure for Dallas (Dec/April)?
- What exact POR hardware is scheduled for Dallas, and can it be adapted for a VAST-optimized SKU?
- Will Nidhi support engaging Myrah’s team to co-design a VAST-on-Azure storage hardware path?
- What networking/SDN constraints must be solved for VAST bare metal in classic Azure (Overlake, isolation)?
- How will Apollo reconcile Fungible vs BlueField-3 in the storage NIC/DPU path?
- Is there an active NVIDIA ask to Azure Storage for DGX storage benchmarking/compliance?
- What is the right executive forum and timing to brief Nidhi/Renan (Ignite vs dedicated Redmond session)?

---

## Action Items (You & Counterpart)
> Tasks are standard Obsidian Tasks checklist lines. If you use a global filter (e.g., `#task`), ensure it appears in each line.  
> Common metadata: `📅` due · `⏳` scheduled · `🛫` start · `🔁` recurrence · priority `🔺⏫🔼🔽⏬`.  
- [x] Reach out to Kushal to gauge willingness to push VAST bare metal on classic Azure for Dallas and align next steps. @Kanchan Mehrotra ⏫ ✅ 2025-11-08
- [x] Quietly brief Nidhi on the VAST-optimized Azure storage hardware path and secure her support. @Kanchan Mehrotra ⏫ ✅ 2025-11-08
- [x] If Nidhi aligns, coordinate an intro with Michael Myrah to discuss a co-designed VAST-optimized Azure storage SKU. @Kanchan Mehrotra ⏫ ✅ 2025-11-08
- [x] Ask Azure Storage team if NVIDIA has requested DGX storage benchmarking/compliance and relay findings. @Kanchan Mehrotra 🔼 ✅ 2025-11-08
- [x] Circle with Lior on framing the Nidhi/Renan session, emphasizing DGX storage requirements and bare-metal path. @Jason Vallery 🔼 ✅ 2025-11-08

### Follow‑Ups & Check‑ins
- [x] Confirm Nidhi’s availability and schedule a focused deep-dive with Renan/Lior and VAST leadership. @Kanchan Mehrotra ⏫ ✅ 2025-11-08
- [x] Update on Kushal conversation and whether MAI will sponsor the Dallas classic-Azure VAST exploration. @Kanchan Mehrotra ⏫ ✅ 2025-11-08
- [x] Track status of Apollo POC hardware arrival and start of VAST testing in the target Azure data center. @Jason Vallery 🔼 ✅ 2025-11-08

### Next 1:1 / Touchpoint
- Next meeting (if scheduled): **(none)**

---

## Task Views (this note only)
```tasks
not done
filter by function task.file.path === query.file.path
group by priority
sort by priority
sort by due
```

## Original Transcript
[00:00:22.61]   Remote(mouse clicking) (mouse clicking) (papers rustling) you YouSilence from 1 minute to 1 minute 30 secondsPause for group workoutBLANK (clicking) How are you?

[00:05:37.60]  Jason Vallery- You're doing great, how about yourself?

[00:05:40.33]   Remote- Good, good, yeah, yeah, these meetings don't pop up on my calendar, so I almost lost track. I was like, I had to meet Jason at noon. Why is it not popped up? And I saw it was, oh my God, 12.05.

[00:05:57.67]  Jason Vallery- You have no idea where I'm going. through. Like having obviously been a Teams, Microsoft Office 365 user my entire career, I mean, and its predecessors, and I'm over here trying to deal with Google email, Google calendaring, Google drive, Slack, Zoom. I am in like productivity hell. I don't know how to do anything. So I'm, I'm still, I haven't learned all those ropes, like Google slides. It's what am I doing? I just can't figure it out yet. I'm too.

[00:06:25.58]   RemoteSorry, I'll get my camera on in a few minutes. I'm just finishing up lunch when I have time. So I'll get on the camera soon.

[00:06:36.03]  Jason ValleryNo worries. Okay, I have actually quite a few things I wanted to bring up with you and get your take on. I'll start off with what I think is like fantastic news. I put a link in the zoom chat. Uh, if you haven't seen, uh, vast signed last week, a deal with core weave, um, the press came out this morning. It is a one point just shy of $1.2 billion software licensing only deal with core weave. It is just transformational for the company. Uh,

[00:07:07.65]   Remote- Amazing, yeah.

[00:07:08.65]  Jason Vallery- It is, I mean, I can't believe the timing, I think, to come work over here because they've really got some momentum. Yeah, I just thought I'd drop that note there in case you want to share it with anyone else in the team. But I think it's a great testament to the investment that Corweave is putting in VaST and the trust that they're putting in VaST because they're effectively betting their business on VaST's platform. platform by making this deal so hopefully that can you know it'll build confidence in vast. I think as we continue our partnership together.

[00:07:40.76]   RemoteThat's that's awesome Jason. I think I saw this pop up like maybe on my LinkedIn and stuff but yeah thanks for putting it in because it's giving like the I'll give. attention to it. I, yeah, I, I, I, I did have a, I did have an over question for you and we'll first bring your topics. But what about the MAI meeting? How did that go? I'm actually curious.

[00:08:10.67]  Jason ValleryYeah, so this is my next set of topics. There's, there's been a few. MAI meetings? Well, let me say this, an MAI meeting and Apollo meetings. I mean, how plugged in on Apollo are you? Are you part of the Apollo V team? Are you aware?

[00:08:27.03]   RemoteI mean, I am not, not in the, in the circle, but I know, know about Apollo.

[00:08:36.26]  Jason VallerySo-- And she, who's the CVP of Azure Kibuneti, scheduled time with us, and we met with her, and she sort of formally shared Project Apollo to us. They even used the word Apollo. Yeah, interesting, and they've asked for two things. we're actively working on. The first thing they asked for was the ability to do a vast POC urgently and what we've done is we've drop-shipped a rack of our hardware to a Microsoft target data center for them to be able to test and I believe that's already in route. I think our team already shipped it, and so they're going to spin up VAST on VAST hardware, VAST ODM hardware urgently to start doing some testing. The second thing they did, and this was, you know, coming from having been on both sides of this, is asked us to run VAST bare metal on Azure storage hardware and wants to do a POC of that and they share the specification of the next generation Azure storage hardware stack that they want us to come in and deploy

[00:10:01.91]   Remoteso they can benchmark VASP running on Azure hardware. What does it mean on a

[00:10:07.86]  Jason ValleryStorage hardware stack, running it on storage. - Right, because this is fungible NICs. So this is Microsoft 1P DPUs.

[00:10:21.09]   Remote- Oh, got it. Okay.

[00:10:24.22]  Jason Vallery- This is Microsoft, and so, you know, obviously I came from the team, so I know this well. When we deploy blob storage, or for that matter, managed disks into Azure, like, you know, disk software, it runs on storage fast XIO clusters. Obviously, these are not general purpose compute SKUs, they're storage optimized, and they're designed by Manisha's org, and then they're built by Ronnie's org and delivered. She wants us to take one of those clusters. an Azure storage cluster and run vast bare metal, meaning ripping the Azure storage software stack off, ripping Windows off, running Linux and vast bare metal on Azure storage hardware.

[00:11:04.85]   Remote>> That is interesting.

[00:11:08.76]  Jason Vallery>> I mean, I'll tell you, like sitting here, like if I was, I mean, I'll just play Apollo. with you. I know the people, the players. If I was Manish, I'd be pretty pissed off about that.

[00:11:19.97]   RemoteYes, and actually, I'll be honest with you, and this is where I was going with, like, I want to talk to you about something because I can, because you know all the stuff involved here. I had actually asked about the fungible thing in that some of the... teams earlier, storage members earlier, because I know one of our other partners was also asked to go test and use it and try it out, okay, and I didn't get, I got a very lukewarm sort of reception to it. So I was like, okay, I don't know if I can recommend it.

[00:12:00.31]  Jason Valleryto anyone. The other thing that she did is she gave us two versions of that hardware spec. One with the fungible GPU, or DPU, and one with NVIDIA's Bluefield 3, and so I think, here's me connecting other dots, I believe that Pradeep, who was the founder of fungible, is part of the Apollo V team. So he's, I mean, this is me playing. in tea leaves and maybe knowing too much, so I have to be careful. But I believe what's happening is he's pushing Apollo to adopt the fungible stack. But I mean, you know, very well. Fungible was--

[00:12:34.21]   Remote- It's coming from the, oh my God. I think it's coming from Mustafa's team as well. It's coming from, Who's the other guy, Jay Parikh's team as well, by the way, like the other one. I know the person, the other partner was led to Fungible through that channel, so it could be that too. I'm not sure a hundred percent, but it could be.

[00:13:06.49]  Jason ValleryYou know, what's interesting and this is. So this is just kind of a broad take. I think we acquired, Microsoft acquired, I'll figure out the right way to describe that. I still have a hard time not thinking of myself as a Microsoft employee. I still haven't fully figured that out. Anyway, Microsoft acquired Fungible in 2019. You know, in my time there, Fungible, and it sits within Manisha's org, right? team for Fungible as part of Misha's team. You know, in my time there, there were these just milestones that kept getting set and pushed back, and Fungible was supposed to have broad production rollout two or three years ago by now, and not a single storage tenant in the world has a Fungible DPU in it today, and so I also have to just like think there's some hedge of bets going on there. in the sense that fundable team just hasn't delivered on any roadmap or timeline that has been set historically. So to take a dependency on it for Apollo seems like a very high risk thing, given their trend.

[00:14:03.27]   Remote- Yeah, yeah. So yeah, that would be interesting. I would love to keep sort of keep an eye on like Apollo. how that turns out like I was then I'm listening to this. I'm wondering if the work you're doing here is that going to help fast track anything that we can do for Met Office? Well, I mean so

[00:14:26.43]  Jason ValleryUK Met conversations are going on. We're going to do a POC based on the most recent conversation we have is Mike Kiernan in the McNary region. I haven't heard from our team on this super recently, but the plan was Mike was going to come back on if we could deploy VaST hardware into an Azure Canary region for an independent POC from what we just shipped to a cheese team for Apollo. So, I mean, I think there's a bunch of different players who are very interested in VaST hardware right now and bringing that, like, where I can lean on you is to help us connect all the dots in Microsoft and make sure all the different stakeholders know what's going on and how to work best together with VAST. You know, I don't know what Mike knows about Apollo, you know, I don't know what's my place to bring it into that. I don't know what MAI knows about all of this. So that, let me give you the third leg, which is. I'm sure you know our friend Kushal Bhatta, I've worked with him plenty in the past, and he's a V Team member of Apollo, so he's part of the Apollo program.

[00:15:34.79]   RemoteIt's being done for MEI, I don't know if she gave you that background, but MEI is the first sort of customer they're looking at. and they are building or starting this whole initiative too, right? So, yes, yeah.

[00:15:52.57]  Jason ValleryShe definitely made it. I mean, this was the statement I got from Chi was, first customer, single tenant, MAO. The vision is multi-tenant, 3P, super-configured customers for So, you know, this is a broad Azure offering, not a just one and done for MAP.

[00:16:17.69]   RemoteYeah, yeah, yeah, exactly, yeah.

[00:16:22.61]  Jason VallerySo Kushal shared with me, and I'm assuming you're working closely with him, because I think you said last time you own that scope now.

[00:16:30.35]   RemoteLike capacity liaison for Kushal or what is your role with Kushal? Not fully, but Sunidhi's team is leading the customer success sort of part of with playing that customer success role with MAI, similar to what we did for OpenAI. So John Lee's team is doing a lot of stuff there. I have been pulled in recently because they needed more help, like MEI needs more help, so some of the technical delivery pieces are going to be owned by my team. So,

[00:17:04.15]  Jason ValleryI'm starting to get engaged there. Right. Kushal shared with me that Falcon is growing. are not super happy with Blob Storage. Obviously, they're big proponents of VaST. They used VaST quite extensively in their Condor cluster and as inflection. There's a number of stakeholders within MAI that would prefer a VaST-based storage solution. He shared that December, the, I think it's first tranche of capacity in Dallas. is going live, and then there's a much larger build out that goes live in Dallas I think in April. The plan of record for storage there is still a little up in the air, particularly the April tranche, and he would love to see if there's an opportunity for that to be vast. Now I know more than Fushal about what's possible here. So he's kind of just looking at it from a business owner lens, which is great. My, you know, setting aside the timeline that we got from Chi was like, first MAI deployment of Apollo is September, October next year. So it's, you know, end of calendar year 26, right? So this capacity that's going into Dallas is not Apollo, it would be classic Azure, and so in practice, what would it mean for VaST to be the storage solution in Dallas for Kushal is something I want to explore. I mean, I know very well that would mean a really aggressive program to try and qualify VaST running on Azure Storage. storage hardware, probably some change in flight of which racks go there based on, I don't know the POR, and obviously he didn't either in terms of what hardware type was going into Dallas. But my expectation is that the team is either putting Blob storage hardware-based racks, so like Blob HDD Gen 9 kind of hardware spec, or they've transitioned to the Flash-based which is still like a previous generation hardware. As a next step, like what I challenged Vishal to do is kind of go push back and say he'd like to formally explore if VaST could run bare metal on the planned storage. That's a different work stream for us too, because we're gonna run into networking challenges, and so, you know, the way this would all work in classic Azure, not Apollo, would be Overlake is present, you have the SDN stack, and that would likely mean we'd have to come in and figure out what would be necessary for us to play nicely, bare metal, with classic Azure I can tell you vast will sign up for the engineering work. Like everybody is all in. How do we go do that? So if there's an opportunity to make this real We do need to get started now to get an April timeline So I pinged Kushal this morning to say like is this gonna turn into a thing? Should we be lighting up teams to kind of go do with a POC of vast? on classic Azure, not vast on Apollo, looks like to try and hit some April timeline to bring him capacity there. That's where that sits. I haven't heard back from Kushal yet. I'd be interested in your take on the political landscape around that and the feasibility of that and how to push that one forward.

[00:20:38.03]   Remotea tricky one and I what I can do is Jason I will reach out to Kushal and talk to him about it because this is where I was telling you like I reached out to him like on the side because I was like there is a lot of political problems that I can get into if I am the one sort of proposing vast and pushing MAI towards vast right so I was. testing out with him as like, are you guys still interested? Right, and, um, because it coming from them is where we can get any traction to be honest right now, and that's how Apollo is getting it, and all of those things, right. It's making progress there because it's like, MAI is, is the one I, I believe that's standing behind it too. Right. and that's where she's getting it from, nowhere else. So yeah, I think this will be the political battle, right, of how do we get this into the Azure plans. Let me talk to, should I approach Kushal and see if I, yeah. if I can test it out with him on what he is willing and not willing to do here. Yeah, please. But I mean, to me, it did make sense even then, like earlier, when we were talking to MEI and now as well. You know the politics better than I, better than me at all. which is where I feel like we'll struggle, honestly.

[00:22:12.41]  Jason Vallery- I mean, Manisha's not going to stand for it. So it's a matter of, you know, CVP's duking it out at that point. Like if Kushal- - Somebody, yeah. - Mustafa and Jay Parikh and, you know, Jason Taylor to say we need to do this because this is the right thing for the program. Manish isn't going to have a leg to stand on, but I, you know, if this is all things equal, he'll try to battle it, which is actually a good segue that's sort of the next point, which is NVIDIA browser. So I had the fortunate opportunity to spend the day with NVIDIA yesterday. I just got home this morning and You know, we're hearing a lot. about where they're going with GB300 and VeraRubin in terms of the DGX cloud, and I don't know how much this gets pushed into your world and then back into the storage org, but we get, we've asked, got very, very clear if you want to be a DJ. xCloud provider, here is the specifications to be a signed off and certified storage provider, and it comes with very specific and aggressive throughput numbers per GPU, and so they're publishing a spec that says you must be able to read and write data at this rate, by the number of GPUs multiplied by the kind of GPU or generation of GPU in order to be a DGX cloud provider, and so what they've done is they've created this reference design of what it means to go build a Neo cloud to build a Nebias, CoreWeave, Lambda, Crusoe and the 30 other ones that seem to exist every day that pop up that I didn't know about before. they're going out to all of these providers and they're saying if you build your infrastructure to meet this minimum set of capabilities then if you have spare GPUs we'll lease them back for you. So NVIDIA de-risks all these NeoClouds basically saying look you know I know you can't guarantee you're going to have business to lease out all these GPUs you're buying from us if for whatever Whatever reason your GPUs are idle, if you've at least designed your infrastructure with this minbar set of capabilities, then we'll use them for NVIDIA first-party research projects and we'll lease them back from you. This is NVIDIA's new play to de-risk all emerging neoclouds. But in order for that to work out, they need to know they've got a performing storage system. I don't know what the current state of DGX cloud on Azure is, I know there was an initially a program around that but then I think it got killed. Regardless, like what I think there should be an opportunity to evangelize and to push on the storage org and maybe even bring this to other levels of leadership within Azure is that, you know, you should be compliant with this DGX reference. architecture, and you should have a storage solution that hits these throughput numbers, and I'll tell you, there's literally only two vendors that NVIDIA has qualified. It's Vast and Weka, and Weka has disadvantages in a number of ways. Like those are the only two storage vendors that can hit their very aggressive set of requirements. Azure storage is so far off at these performance numbers, it's not even funny. So I'd love to, you know, understand how that's playing out in your team and with NITI, and if there's an opportunity to bring more visibility to NVIDIA's reference design for DJX and what storage specifications they're publishing and what that roadmap looks like, we went up like 50% during the transition from GP2 NITI. to GB300, the amount of throughput per GPU they need from storage. I'll pause.

[00:25:57.14]   RemoteInteresting. So, we've done a few, as you mentioned, right? We did work with, like, DGX Cloud is actually one of our customers, like my team's customers, because, and then I believe so I could mention it to you like they use AMLFS and everything right on on Azure so storage team is involved with them. We haven't done much on so this was H100 and A100s basically we've not done more with them on the GBs yet uh so uh. nothing there yet. We've done a bunch of benchmarking with them from a GPU point of view. The storage one was a little bit of news for me. I have not heard them ask us to do storage benchmarking of any sorts. Maybe that's coming or it's coming to some other part of the organization where they may be talking. I will ask our a storage team if they've heard anything. I don't know I I've I've had my mixed feelings about the NVIDIA reference architecture. I'd heard about this from another vendor earlier like they were trying to do some benchmarking around it. I have been mixed feelings around it like it's a good to have and do some kind of benchmarking with it but I don't know where it where it helps.

[00:27:34.31]  Jason ValleryYeah I mean if you've got one of the things that we're pushing on is with all these neo clouds like you know it's crazy because I I'm seeing all these wins with all these small, they're smaller deals, like OhCore 42 and TwoSigma, like all of these smaller players because they want to go play in the DGX space, you know, they need a storage solution, and one of the things, you know, I'm interested to understand is what Microsoft is even doing in many of these deals that it's signing with these Neo clouds, like recently the Irene one and the other ones. with nebulous and in scale, where, you know, these, these, these NCPs, they want fungibility of the capacity. They're going to go build out a data center, fill it full of GPUs and lease that capacity back to Microsoft, um, on a, you know, I don't know the commercial terms I'm assuming it's probably something like they're paying to rent the GPUs on an hourly. monthly, yearly basis back to Microsoft. But, you know, the workload characteristics that you could use with those GPUs will have some amount of variance. They could be used for training. They could be used for inferencing. It could be agentic inferencing versus real-time inferencing. A variety of different use cases could emerge for those GPUs, and they're being sold as a service. you know, they have a five-year depreciation cycle, it's impossible to really forecast over that five-year term all of the scenarios those GPUs could be used for, and so it's important that you've got a general purpose, highly performant storage system applied adjacent to those GPUs to handle any of the types of future scenarios they could be used for. It's very myopic to think. we're going to deploy them for inferencing today, we don't need any GPUs, we don't need any adjacent storage, we can go and we'll be good without it, because then tomorrow that might change and you really do need storage, and I'm sure you're well aware. My experience here is that that's kind of a one-way door, like once you've built a data center, you've crammed it full of GPUs, you've used every last kilowatt in the entire data center, and every one of those GPUs is going to go to or that last tile location, or rack location, you're not gonna suddenly come in and drop in 20 racks of storage. There's no room for it and there's no power for it. So, you know, it's important that when you're designing these clusters, you design the space power for storage from an outset, and that's the key message that we're asking those NCPs to take back to Microsoft when these... lease back partnerships are happening and in the general case all of them are already doing this like in the cases where they're not leasing capacity implicitly from Microsoft they're already going and deploying you know 20 racks of fast for every 8,000 GPUs or whatever it is to make sure they've got some flexible storage solution to support whatever kinds of workloads emerge for that capacity in the future. So, I mean, that's the point of a reference architecture. We're essentially saying these GPUs get this much throughput. Therefore, you should probably size at least this much GPU-adjacent storage so that no matter what emerges, you'll have a storage platform there to support the workload.

[00:30:38.14]   RemoteYeah. Frankly speaking, I would not even bother about, like, I mean, I think you should do the benchmarking for sure. But I feel like this will be more of a we know it kind of thing. What you are going to struggle with like I feel like the 3P like the 3P capacity that we're getting like that's really a place where we should see if we can bring some partnership here. You will still you will again. see the same political piece of it, which is right now the plan is to go and use Azure services just to get the GPUs, right? So you're going to have the same kind of challenge that we were talking about earlier, right? I think one thing that may help. - Jason is, I don't know if, I know Lior has some time, he's requested with Nidhi, with Renan. - Yeah. - I think this should be the main topic that you, like Vash should grill on with her. - I will, yeah, I'm already starting to seep in these ideas and I'm also starting to share internally, but I think that should be the main topic where I see most opportunity, and you don't need benchmarks for it, I'll be honest. You don't need NVIDIA to endorse this. At least my take.

[00:32:15.77]  Jason ValleryYeah, I think I would just sort of like if you need ammunition to go and say look Manish you don't have a storage system that even can play ball here. But fast is already blessed by NVIDIA for this scenario. That's why those benchmarks are useful. But agree. Let me show you a slide that I've been working on that, you know, I think will certainly be part of the conversation that Renan brings. Let me pop this open. So I think I alluded to building something like this when we spoke last time. I have to be a little careful here because again, I've got this two hat problem, but this is a reference exabyte. So let's just imagine that the capacity we're going to go deploy is one exabyte. It's just a nice, easy round. number. These numbers scale up and down linearly, and why the current solution for VAST on Azure makes literally no sense for either side. You know, today the only way we can deploy VAST is on LSV4 and LSV5. This is EGOL's compute instances. LSV4 is GA today. LSV5 is GA a year from now, and so for context, to So if you deploy an exabyte of vast using that solution, you're talking about 40 megawatts of power. That is 18,000 GB 200s worth of power to get one exabyte of storage, which is insane, makes no sense, that's the CAPEX involved, the wasted power involved, nobody is ever going to make that deployment happen. you've locked vast out of opportunity to even deploy today. The road map is that much better. Comparison point is the center column and this is where I get, you know, that those aren't actually public stats. They're stats that I just happen to have in my head. But if you were to deploy an Exabyte of blob storage, you know, you do that with 2.5 megawatts of power and a hundred and And you would only be getting, let's round up and be generous, three terabytes per second of throughput out of those, and two million transactions per second. Compare that to vast what we can do with ODM hardware. You've got two versions. One's performance optimized, where we've went in with the NVIDIA reference architecture and prioritized-- PERF, and the other one is capacity optimized, where we've said we're willing to sacrifice some of the performance in exchange for higher density, lower cost, better utilization of power. You're talking about the same amount of power to get, well, what is that, six times more performance on write and 12 times more performance on read. You're talking about 2 million to 450 million transactions per second, I mean, just insane orders of magnitude, and you're talking about half the rack count, going from 180 racks down to only 90 racks and roughly the same power. If you went with just a vast, like, our hardware SKU and our software stack, and then if you pivoted to the full capacity optimization. where you're willing to sacrifice some of the power, you're talking about one fifth of the power to get still double the performance on one exabyte of storage. So this is the message that we have to land across Azure, across MAI, across Apollo of like, it makes no sense to use Azure storage block. HDV hardware. It's not even economically viable for either company to consider Azure compute instances to deploy VAST. The only path is to have a co-engineered, co-developed hardware platform that allows us to run bare metal for any Azure customer, be it UKMAT, running inside of an Azure first party data center for a 3B customer like, no matter what, we have to go down a path together of getting to hardware optimized deployments for our shared customers.

[00:36:15.39]   RemoteNow, I know this is a good story, Jason. I will ask you one. other question of if you had to play the put the Microsoft hat right what's in it for Microsoft and how do we make that more amiable for is there any way to or like somebody like Manish?

[00:36:50.10]  Jason Vallery- I mean, it's gonna be a hard pill to swallow. I mean, Manish is the one that has the most to lose, where everyone else has everything to gain. You know, the problem is that you've got Azure Storage, which is a software stack that has been in the making since the first days of Windows Server. Like, Azure Storage was never designed for this kind of scale and performance requirements, and Manish's biggest challenge is he's not pulled the trigger on building something equivalent to VaST, which is just a fundamentally different architecture, and you know, look, had Manish pulled the trigger on something like this a few years ago when we were asking him to? I wouldn't have left because we would have actually had something to compete with in these opportunities. But he didn't, and so, you know, he's left with a unfortunate situation of time to market means that customers are demanding this kind of performance and he doesn't have anything on the truck today. How do you make this amenable to him? The only, the only like saving grace. only like thing that I think feels like maybe a win for him is if this ends up being his team that owns the hardware and his team has a there's a good hardware team under Michael Myra that we'd love to go partner with on designing the SKU and getting qualified we have no skin in the game on the hardware like we want to fully embrace whatever I hardware will give us, it just needs to be tuned and running bare metal VAST on top of it, and so if we can go partner with Manish's org and Myra and get a VAST optimized version of the SKU going, that would meet CHI's requirements, that would meet MAI's requirements, that would meet UKMET's requirements, and that could be broadly deployed in the Azure. fleet that'd be a huge win and I'll tell you the last point I would I would make here is you know and you know this is maybe a little off the record but I'll tease this with you because I imagine this is what Renan will say to Nitti is that the core we've deal is simple and this is the deal that Renan wants to go sell everyone at this scale it is a all-you-can-eat license of vast but Renan doesn't want to get into a model where he's Trying to sell this customer or that customer and he's engaging and he's you know Getting a few hundred pebble bites there a few hundred pebble bites there an exabyte over here charging per gate None of that Renan just wants to come to Microsoft and say here's a big number you pay me that number. Here's the vast software have at it, you do what you want with it. As many customers, as much of it, all you can eat, we'll support you. It's a support contract and an unlimited use license. That's the model VaST wants here, is to basically let Microsoft solve Manish's problem with one big license fee.

[00:39:39.78]   RemoteI am liking the direction you're going in with the hardware part. Who is this? Actually I was trying to place who you mentioned. Is it under Manish, you said?

[00:39:53.84]  Jason ValleryHis name is Michael Myra, M-Y-R-A-H. He is a partner PM who owns Azure Storage Hardware.

[00:40:05.80]   RemoteOkay. - Michael, oh, I've seen Michael.

[00:40:10.75]  Jason Vallery- He's part of Long's team, Max.

[00:40:13.59]   Remote- Oh, he is part of Long's team. - Yeah. - Can we tease this out a bit more? I feel like unless that happens, we will keep hitting this roadblock unless somebody comes and bypasses Manish, right? because like it's almost impossible to get vast broadly enough if we don't get past this.

[00:40:38.29]  Jason ValleryLet's, let me just game theory this with you. I would love to sit down and have this conversation with Myra. I have been tempted to reach out with him and schedule time. I know Michael very, very, very well. Um, I have reserved from doing it because as soon as I open that can of worms he's going to go to Angamanesh and he's going to tell him there's you know there's a vast play at work we have to defend our turf and so I don't want to be the one that opens that can of worms but I'd be more than happy for you to open it and if you want me to be on that call and explain it to Myra I would be super excited to do so.

[00:41:15.87]   RemoteTempted to. I want Nidhi to be on board though like if I like I will I will I will relay it to her on the side too but I think this is the story you tell like yeah I feel like you're already building this right um we should seed this idea into her as well yeah uh because we need her support like otherwise it's like I yeah it's above my pay grade to make this

[00:41:47.14]  Jason ValleryHappen. So we want to come and talk to Nidhi. I'll circle with Lior because I wasn't sure when did he reach out about the meeting with Renan because we had

[00:41:57.33]   RemoteTalked about it. Yeah he did yesterday and Nidhi was traveling, so we've not come back on this yet, and her time is limited at Ignite, so I'm hoping that it will, let's see if it'll work out.

[00:42:15.33]  Jason Vallery- Oh, it's time to do, what Jeff had told me is we should try to just come up to Ryn. Like, if we can get a time set up for this, like. we'll send a delegation, we'll all come up to Redmond, we'll spend the day together, let's make or whatever we need, we'll like let's make good use of it though and we can have the right pitch and the right meeting set up and who do we need to talk to. But it doesn't have to be gated on Ignite, we could do it sooner than Ignite, do it after Ignite, like we'll work our schedules to figure out the right way to make this happen. will be at Ignite, and I think it would be a great opportunity for them to connect. But if we want to get into the details, we need to have a separate follow-up.

[00:42:54.25]   Remote>> Did you know Anand and team when you were here at Microsoft, like the dedicated team, Azure dedicated?

[00:43:01.57]  Jason Vallery>> I didn't, like, not well. I knew who they were, and I maybe was on a handful of meetings, but I didn't have to engage with them much.

[00:43:08.40]   RemoteMeaningful way. Okay, you probably know I've understood where I'm going with this like I don't know but I was going with like if it can be something like a dedicated hardware. It's I don't like the idea to be honest like because of all our experience with cluster store, I'm forgetting the name to know, because like putting all dedicated hardware. It takes time, right? And if you want scalable cloud, it's not my favorite solution, to be honest, but that could be a part as well.

[00:43:47.54]  Jason ValleryYeah, I mean, you know, I've been engaged with the EGOLS team around the... I'd worry that Anand would be in a similar mindset of like, let's go give a virtual machine that has maybe a different shape to it that's better than these two instances, but we really don't want to be in an environment where we're running virtualized, you know, the way you're going to get the most performance.

[00:44:20.12]   RemoteHe's not, his team is, so I, his team is actually purely. about dedicated hardware, like bare metal, they put it in Azure data centers and that's his charter. So he is actually invested in not virtualizing it.

[00:44:32.53]  Jason Vallery- Okay. Well, I think that's a parallel thread. I think the opportunity, as it seems to me, from Apollo would be to work more with Myra's team on how do we make Azure storage hardware.

[00:44:42.24]   Remote- I think so, yeah.

[00:44:43.06]  Jason Vallery- There should be one story here, like Microsoft shouldn't have competing scenarios.

[00:44:46.66]   Remote- Now, the other thing is, if Qi is already going around them and doing this for Apollo, right? It's in Manish's interest that he keeps something in his 


team, right? um that that keeps it on storage turf uh like i i i would i would see it that way too uh but i think knowing she like she'll she'll still go around and do it yeah so >> DIRECTOR MACK: Okay. No this is yeah this is helpful. So I have action items. Sorry I didn't take a look at my meetings I hope I was not supposed to be anywhere. I've been. Yeah no I'm good.


