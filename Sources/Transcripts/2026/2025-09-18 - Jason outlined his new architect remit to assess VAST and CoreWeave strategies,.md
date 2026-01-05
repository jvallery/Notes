---
entities:
  people:
  - '[[Jack Kabat]]'
type: transcript
source_type: unknown
date: '2025-09-18'
---

# 1:1 — Jack Kabat — 2025-09-18

> [!info] Purpose
> Build trust, surface and remove blockers, align on priorities, coach & grow.

## Summary

Jason outlined his new architect remit to assess VAST and CoreWeave strategies, NVIDIA’s DGX-driven direction, and gaps in Microsoft’s storage stack, with Project Apollo likely in scope. They contrasted VAST’s GPU-adjacent flash and global namespace (DataSpaces) with OpenAI’s model using local NVMe on GPU hosts and blob for cheap/deep, noting OpenAI’s proprietary global/regional sync built atop Azure data movement. Jack emphasized Azure’s multi‑region realities and the need for a layered approach and capabilities independent of OpenAI. Both acknowledged Microsoft’s execution slowness and the risk of being commoditized by NVIDIA’s roadmap. They identified an internal VAST SME to consult and agreed Jason would proceed with a deep dive and return with recommendations.

## Key facts learned

- Jason is back from a 3-month sabbatical and moved into an architect role carved out by Manish.
- Initial focus: deep dive on VAST and CoreWeave capabilities, NVIDIA alignment, and Azure gaps; Project Apollo likely relevant.
- CoreWeave positions VAST as preferred storage but also built its own object storage to avoid full vertical coupling.
- NVIDIA is pushing DGX architecture and hardware-level optimizations that integrate with VAST; NVIDIA is not a storage company and fills that gap via partners.
- OpenAI’s approach: keep storage on GPU hosts (local NVMe) and lazily move data to/from blob; Fairwater exemplifies this.
- OpenAI’s global/regional synchronization IP sits above Azure’s data movement; Azure lacks this as a native storage primitive.
- VAST provides a global namespace (DataSpaces) with cross-region data locking and strong consistency; focuses on high-performance flash, not HDD-based cheap-and-deep.
- Azure’s 70+ regions and convergence of training and inference require a layered storage design and distributed consistency.
- Microsoft lacks storage maturity for these workloads and risks being commoditized by NVIDIA’s roadmap; execution has historically been slow.
- Project Apollo creates uncertainty (innovation path vs duplicative effort).
- UK Met Office Gen 2 came up in context of VAST but with no detail.
- Jack affirmed Jason’s prior impact; Jason reported 100% rewards despite a highly impactful year.

## Outcomes

- Alignment that Jason will perform a deep dive on VAST and CoreWeave and assess Azure gaps.
- Identified an internal VAST point of contact (name sounded like "Khan Channel") to consult.
- Shared view that Azure needs capabilities akin to a global namespace/consistency layer independent of OpenAI.
- Agreement that a layered storage approach is necessary to balance performance and cost at Azure scale.

## Decisions

- Jason to proceed with the VAST/CoreWeave strategy deep dive as his first task in the new architect role.

## Action items (for Jack Kabat)

- [x] Conduct deep dive on VAST and CoreWeave strategies, capabilities, NVIDIA alignment, and Azure gaps; propose direction. @Jason Vallery ⏫ ✅ 2025-10-26
- [x] Evaluate storage architecture options (GPU-adjacent flash/VAST-style versus OpenAI local NVMe + blob) and recommend a layered approach for Azure-scale, including global namespace needs beyond OpenAI IP. @Jason Vallery ⏫ ✅ 2025-10-26
- [x] Identify and engage internal VAST SMEs (e.g., the contact referred to as "Khan Channel"); gather insights and any offsite materials. @Jason Vallery 🔼 ✅ 2025-10-27
- [x] Assess Project Apollo implications and integration points with the proposed storage strategy. @Jason Vallery 🔼 ✅ 2025-10-26
- [x] Schedule a follow-up with Jack to review findings and recommendations. @Jason Vallery 🔼 ✅ 2025-10-26

## Follow-ups

- [x] Share correct contact details for the VAST SME ("Khan Channel") and any relevant offsite notes. @Jack Kabat 🔽 ✅ 2025-10-26
- [x] Provide any context on UK Met Office Gen 2 and its relation to VAST engagements. @Jack Kabat 🔽 ✅ 2025-10-27
- [x] Check with NVIDIA contact (Vlad) for current DGX Cloud storage deployment patterns relevant to Azure strategy. @Jack Kabat 🔽 ✅ 2025-10-27

## Risks

- Microsoft may be caught flat-footed due to storage maturity gaps and slow execution.
- Over-reliance on NVIDIA’s roadmap risks commoditization.
- Dependence on OpenAI’s proprietary sync IP leaves Azure without a native global namespace capability.
- Cost risk of all-flash, GPU-adjacent storage without a layered approach.
- Internal fragmentation (e.g., Apollo vs Azure) could dilute focus.
- Customer sophistication gap relative to OpenAI may strain delivery.

## Open questions

- Should Azure build a first-class global namespace/strong-consistency capability (akin to VAST DataSpaces) as a native primitive?
- What balance should Azure strike between GPU-adjacent flash and cheap-and-deep blob with local NVMe to meet performance and cost goals?
- How should Project Apollo align with or feed back into the Azure stack versus run as a separate path?
- How critical is MAI relative to OpenAI in prioritizing storage investments and features?
- What execution ownership, budget, and timeline will back the required storage investments?

> Next meeting (if any): (none)

---

<!-- ai:transcript:start -->

## Transcript (auto)

```text
[00:00:45.01] Parallels Desktop : You YouBLANK youBLANK you you youBLANKAUDIO you Hey, Jason. Sorry I'm late, Ben. How are you?

[00:08:05.02] Jason Vallery :  Jason ValleryNo worries. How are you, Jack? Good to see you.

[00:08:09.21] Parallels Desktop : Um, I'm, you know, I don't know what day it is, but, uh, you know.

[00:08:15.17] Jason Vallery :  Jason ValleryThursday

[00:08:17.19] Parallels Desktop : No, it's it's nuts and it's you know, it's it's a typical changing you know, there's obviously the pressures of everyday things and then you kind of step back for a second and See just how many changes there are the world's, you know at Microsoft is always so on like you thought you knew things yesterday and then today it's so different you know we just haven't finished having like a you day off sites it just kind of needs team and the managers and you know you come off of this and you're like saying wow okay so what does this mean right i mean i think we as microsoft have i think probably over indexed for kind of being the operational cloud as a As opposed to like, you know, I asked myself, where's the innovation, where is the product design and planning versus just, you know, rack and ship GPUs, you know, I mean, you know, and, and, you know, and even on the customer front, it's so skewed to the few rights that are selected at some top level. and everybody else is like, "Sorry, no space. Use Copilot instead," so that's... Those are just.., and again, I'm just kind of being raw because you asked the question in the middle of kind of trying to do a little bit of thinking, and then there's all these new initiatives coming out, some other team. There's this project, Apollo, who's going to make AI Cloud better than whatever Azure is, you know, just, and you're like, do I pay attention to this? Is this noise or am I just being replaced tomorrow? You know what I mean?

[00:09:54.22] Jason Vallery :  Jason Vallery- Well, it's actually good you bring that up because it's really what I wanted to talk about. I mean, it's always good to shoot the shit and see how you're doing, but, you know, coming back, I was on Spaticle for three months. I'm coming back into a new role that Manish carved out for me as an architect really look at where we're headed. Project Apollo will likely be a key part of that, and my first task is really to do a little bit of a deep dive into the strategy behind VAST and the strategy behind CoreWeave and what capabilities they've delivered and where our gaps are. and you know where we wanna go, and when I was sitting down and thinking about how to tackle this problem, the first thought to my mind was, you know, NVIDIA is driving the hardware roadmap. We've got, you know, when you look across the hyperscalers and these Neo clouds like PowerWeave and the others that are sort of emerging, you know, they're all kind of marching to the NVIDIA vision at this point,

[00:10:52.87] Parallels Desktop : and that makes us commoditized. It's more than that Jason, right? Because even think of something like Oracle. Oracle, like, I mean, you're deep in this, right? So you know about Fairwater, but Oracle's delivering another Fairwater site that will talk together, right? On the OCI, right? So sometimes I'll talk to NVIDIA folks who are in the middle seeing it from both sides, and they're basically saying how different it is on Oracle. Oracle people are basically connecting. It's like having DC Ops, and then NVIDIA operationalizes the cluster, and OpenAI uses it. There isn't that layer we have, and it's interesting, because... I think opening I sometimes wants that but then other times they're like, oh my god We couldn't have done Inglewood and bring up chibi 200s without you guys. You know what I mean? So It's a very weird space and and and and what these guys provide is really interesting because on the core we've signed on the one hand I mean It's kind of neat because it's a curated experience, you know, your control plane and your job plane are integrated so you can do, again, stupid things but so important like maintenance, aware of how much of your jobs are actually running where and synchronize that versus having these walls between things we deal with an Azure, but they're also evolving and. at their acquisition path they're buying a lot of little software startups as if you know so they're trying to definitely expand what that stack is so then if you take what i just said prior to that their customers are trying to have the least of stack possible right but even core weave is trying to figure out how the hell do i have a plane here and And how do I make my stack be more value-add even though it's a focus stack, right? So I think everybody's kind of struggling a little bit with this, and it's super fast in terms of how it's evolving.

[00:13:00.86] Jason Vallery :  Jason VallerySo I mean, to Korwee's point, they went and built their own object storage platform that sits alongside Vast. they position VaST as their preferred storage platform, but clearly CoreWeave sees that as the vertical integration thread of we're gonna be completely tied to VaST if we don't have a different storage platform. What's your take on VaST and what NVIDIA is saying, 'cause they're pushing them for the DGX architecture, they're doing a lot of hardware level optimizations to tie into the VaST stack. What's your take on Vast?

[00:13:32.08] Parallels Desktop : So, I don't have a good one, because it's not an area I'm really focused on. I would say, I don't know if you get value, so let me say that up front, but Khan Channel would probably be the closest on our team to look at that. So I don't have a point of view from a technology perspective. I think from an NVIDIA perspective, it makes sense. because NVIDIA is equally stamping out, and it's funny because Vlad still keeps calling me from NVIDIA to say hi and how things are going, right? But Vlad went, you know who Vlad is, right? He was my kind of, you know, superhero in deployment side, right? The superpower. But he went to NVIDIA and he works in their, And they're professional services that basically deploys their DGX cloud all over the world, right? So kind of the same role here, except he's happy over there because he's the boss, and he has contractors working for him versus trying to work with everybody else with Microsoft to make this happen. Anyway, so we'll talk about that, and they're busy deploying this all over the world. But, but NVIDIA is not a storage company, right? So I think they have just a hole to fill, and they fill it with somebody who they feel that will either be aligned with them or is technically good enough and cheap enough, and probably not one that's gonna step on their toes, but listen to where they wanna go. So I think that's a strategy from an NVIDIA perspective, but I don't have much of an insight from a technology perspective. What I am actually on the off-site, Conchon was talking a lot about Vast and I thought we're also beginning to kind of get into bed with them too, right? And I don't know if that's just a reaction because CoreWeave has them, so we have to have them. But there was some discussion about – because this also is coming up. in the context of the UK Met Office, are you familiar with that? The Gen 2 stuff?

[00:15:28.24] Jason Vallery :  Jason ValleryI heard that they were-

[00:15:30.34] Parallels Desktop : Anyway, yeah, so, but sorry, I don't have much, I don't want to tell you bullshit because I don't have that stuff.

[00:15:39.54] Jason Vallery :  Jason ValleryI mean, I look at it from the technology lens primarily, and I see a very mature platform with a global- namespace, more compelling caching strategy, clearly much deeper tie into the hardware network offload layers and optimization. So, you know, I think that we have a huge amount of work in front of us if we're going to go and compete with VAST or deliver the same level of value that VAST has in their stack today. fundamental questions that emerged, though, is if that's the kind of platform you need, or if you do what OpenAI did, and so the industry had, you know, as an inflection point in the storage, like OpenAI was, we'll put all the storage on the GPU host, and we'll just lazily move things in and out of dumb blob storage, and it'll work really well, and that scaled, and that's what obviously Fairwater is. But everybody else is... saying that's not the way to go. We need high performance storage adjacent to the GPUs. That seems to be NVIDIA's story. That's obviously VAST's story, and so it's an inflection of like, will the industry be able to go the way OpenAI did and will leverage GPU local NVMe? Or does NVIDIA have this right and we need to go and deliver a really high performance GPU adjacent?

[00:16:53.25] Parallels Desktop : Storage. Do you have a sense? Yeah, I mean, so yeah, I mean, I think I think it's a it's a scale problem, and what I mean by that is opening up like that strategy that you mentioned from an NVIDIA perspective makes sense if you are, I don't know, BFL, if you're MAI, if you have a site opening eyes doesn't have a site. a world footprint right so that doesn't work at all from their perspective they need to have more of a distributed global storage that they're buying millions of cores of cpus for data processing which means they're fundamentally looking at that as a like they're not going to do that on the gpu are going to do that in some kind of in and out of blob storage, prepare that, and only move it as needed into the actual large training jobs. What I think becomes super interesting, and I actually know a lot of this because of your paper, of just how this inference and training are becoming one, right? I also now have to think of how do I work in the world where? Like again, think of Azure 70 plus regions from friggin Norway to South Africa, and how do I bring? The knowledge from inferencing in those worlds to inform our my, you know, post training updates. I think that's. That's the problem OpenAI is trying to think about, which is probably different than the problems... That doesn't happen on CoreWeave. It happens... Each thing is an island, right? And so is DGX Cloud, right? I think Fairwater, which means Oracle will have some version of what we have for Fairwater because they have... I mean, you'd have to look at them as merged, right, where each site has a level of duplication. But I think you have to think of a layered approach, right? I mean, I don't know how else you're going to manage this, like, again, because I worry about these other solutions. They really fall apart where, like what is their story on this distributed view where there isn't necessarily one master?

[00:19:18.15] Jason Vallery :  Jason Vallery- That's actually vast. We kind of bolted it together with OpenAI and frankly, all the IP that does all the global regional synchronization is OpenAI. it's built into their stack, and they built it on top of our data movement capabilities. Whereas if you look at VAST, what they actually have is this thing they call data spaces, and it is a global namespace. It is the namespace where you can have your objects in a variety of different regions, and it has cross-region data locking so that you have strong consistency and data can move freely across different systems, and so, you know, we don't have that opening, I have that. We don't have that as a core primitive in the storage platform, VAST does have it, and so what they do, but the big key difference is that VAST doesn't do hard drive based storage. They don't do the, you know, cheap and deep, they do the fast high performance flat, and so that's kind of more the question is like. How much of this ends up being GPU-adjacent flash, because that's where the industry is moving, and that's where NVIDIA is pushing the industry, because that's what they see, versus the cheap and deep OpenAI approach, and then they get the performance out of the

[00:20:31.59] Parallels Desktop : Stores on the GPUs themselves. is actually super helpful because if you put it in the terms you just did, I think it is critical for us to have the capability without OpenAI there. Because our OpenAI relationship is all over the place, but I also think it's not the only one. Like, we're, you know, what about MAI? How are they going to solve this problem? They're not, right? - Exactly, so, yeah, and I mean, the challenge will be, and is, is MAI really important, right? And you can't even ask that question, because if you ask that question, you've already upset somebody. But I think that's the way to think about it, Jason, because if OpenAI has this as. their IP, that is a differentiator. But I do think you're spot on that. You have to then bring it across the stack. So it's economical, right? Like it can't all be just like, like these data sets are insanely big because. You're not just looking at world data. Now you're looking at generated data, right? and inference-based data, right? So you'll have to have layers of storage because otherwise no one can pay for this.

[00:21:55.15] Jason Vallery :  Jason Vallery- It seems like to me, we've got a pretty big problem on our hands that we just don't have the storage maturity that we need to deliver these kinds of workloads and we're gonna get caught flat footed 'cause our customers aren't gonna have the sophistication that OpenAI has.

[00:22:08.09] Parallels Desktop : What you just said right now, I think you could have said, I think, "In the eight years I've known you." It's just the maturity keeps going, and we always are a step behind, because it's not like we're standing still either, right?

[00:22:23.09] Jason Vallery :  Jason ValleryRight. Well, we're very slow. I mean, just to point the obvious out, it's not like we didn't know this, it's not like every quarter and look at and put in the SharePoint library to say one day we'll get to that. It's not like these are new ideas, it's failure to execute and we just haven't actually made hard decisions and follow through with them and that's kind of where we sit. That's just historical Microsoft.

[00:22:47.54] Parallels Desktop : Well, yeah, and I mean, and this is the thing to think about. I mean, look. So, Apollo, you know, I don't know what to think about Apollo right because in one hand, like, well, what I think about Apollo is the old days of Steve Ballmer, where you had four projects all chasing the same thing and see who wins. That's one way to look at it that's maybe more of a pessimistic view at least in my mind as I say that. I think another way to say it is. It's probably hard for, which ties into the point you just had, it's very hard for us to innovate at Microsoft when you have all this baggage and have to have the whole stack bringing with you. So maybe that's one way to unlock them, and I don't know if that means you unlock them to innovate. I'm not sure what they come up with. the final solution or you can actually take some of their stuff and put it back in the thing I mean those are people way above me who have those things and everybody will be told their own story because if everybody knows the final game then not everybody will you know no one wants to be used to to another mean right so like this is __ probably the same story that the Maya people have heard all the time, right, where they're going to be the accelerator, right, and you have to keep going and, you know, no one's telling them, no, we're going to just deploy one cluster of your stuff for Maya 200. Well, I guess they probably know that because they know the wafer starts. But you know what I mean, like, the whole point is you have to keep because you're still learning things sometimes the right outcome is things you've learned you know and I guess the one positive thing about Microsoft is seldom there is the one thing that fails and the whole company implodes, right?

[00:24:38.28] Jason Vallery :  Jason ValleryWell, how's everything outside of work? How's life otherwise? You doing good?

[00:24:44.45] Parallels Desktop : Doing good, you know. doing busy again and i'm like telling you like you go to these things and you're like And he starts bleeding into places elsewhere. You're like, well, I don't know. I mean You know I I missed those days of senior pm where it seemed like, you know, you'd work on something You know, um, that's weird and it's I thought so. I mean, I am so jealous of your sabbatical. I ended up cashing out because I was like, there's no way I can do this and I've dragged it for too long, and they're, they're definitely pushing for us to make a choice. So, you know, I got my two little weeks of vacation that I took and, you know, Sagar's vacation. me feel bad for taking it, but it was nice. We went to Turkey for two weeks, a bit of in Istanbul, but mostly by the waters, so kind of just enjoying that. But yeah, back in for it, it's getting nuts again. What's interesting is, I think, you know, you've been a participant in Supercomputing and those things and I think we're probably pitting pivoting again back to ignite being a bigger thing and supercomputing being a smaller thing But you know all the kids are in school now, so it's also a little different at home two of them have graduated

[00:26:15.46] Jason Vallery :  Jason ValleryYeah, for me on this radical front, it was, uh, I was, I've been eligible for a number of years. I never cashed it in. I debated it at one point. I'm like, yeah, maybe someday I'll have a chance to take it, and then, you know, with everything that went down and, you know, role change and all that, I was like, well, screw it. Now's the time to take it. I don't know. I'm transitioning all my responsibilities. I'll go take a couple months off and come back. and see what happens now. But what happened is that like a week in to my sabbatical, my wife had an injury and had her knee replaced. So instead of all of our plans, if we were going to travel and do some other things this summer, like she ended up being in rehabilitation all summer for a knee replacement surgery. So we were pretty much home all summer, but it was still good, and you know did some projects and that sort of thing. So I still enjoy being on

[00:27:03.40] Parallels Desktop : How you know I and I'll probably have to drop in two minutes, but I You know, I only heard secondhand. I don't actually know what happened to you what I what I can tell you is there are many meetings and we're like Fuck if we only had Jason in this meeting So you are sorely missed You're missed in a lot of the places that I don't fully know what happened, well, I mean, I can kind of extrapolate what happened, but you're definitely sorely missed and I feel it's one of those stupid ways of how Microsoft works and the politics of it.

[00:27:41.98] Jason Vallery :  Jason ValleryWell, I mean, that's exactly it. with Juergen. I actually talked to Juergen last week. It was really good to catch up, and when he left, I didn't have that relationship at all, and the great thing about Juergen is he gave me the air cover I needed to work with Vamshi. Vamshi, I respect the guy. It's been a love-hate relationship for a long time. in many different ways, and, you know, Ong didn't, you know, see the same value in me that Juergen did, and really just put all of his chips in Vamshi's basket, and then when you layer that onto, Vamshi got a real sense of FOMO. Like Vamshi was an AI denier from the beginning. He's like, there's never an opportunity here. This is a party trick. There's nothing to it, right? And then suddenly I put all my chips in the AI basket, and he saw me winning and getting invited to meetings that he didn't get invited to, and he got a big sense of FOMO, and it was just clear that he was pushing me aside, and look, I will say this, Vamsi plays the Microsoft politics game a million times better than I ever will, and for that, more power to him. But ultimately, it was just a collision course in destiny that was inevitable, and I went to Manish and said, "Look, I just can't operate in this environment anymore. I want to know that I have a manager who has my back, and I know I don't have that in Vamshi." I went to Ong multiple times and said, "I want that in you, Ong," and Ong said, "Basically, no." So I went to Manish, and I said, "Neither Vamshi or Ong. I have my back, what do I do Manish?" Manish said, "We'll put you in an architect."

[00:29:20.07] Parallels Desktop : - Yeah, the only thing I can tell you is sorry because you fucking did some awesome work and the thank you for that should be very different than what you got.

[00:29:34.16] Jason Vallery :  Jason Vallery- You know what really pissed me off, Jack? When I left on sabbatical, Manish said, to go talk to Garish about partner budget because I'm 67. You know what I came back to? 100% rewards for everything I did last year.

[00:29:46.06] Parallels Desktop : That's fucking insane.

[00:29:53.67] Jason Vallery :  Jason Vallery100%-- probably, objectively, the most impactful year of my 13 years at Microsoft was last year. I was convinced I had like Top rewards coming my way and I come back and I got

[00:30:06.45] Parallels Desktop : All right, I would love to catch up more I gotta go but welcome back Jason and for whatever it's worth definitely saw the value definitely appreciated you being part of the team and I know it doesn't carry anything of the things that how you should be rewarded, but just for what it's worth

[00:30:27.75] Jason Vallery :  Jason ValleryI appreciate you, Jack Bye

[00:31:30.55] Parallels Desktop : (clicking)BLANK
```

<!-- ai:transcript:end -->
