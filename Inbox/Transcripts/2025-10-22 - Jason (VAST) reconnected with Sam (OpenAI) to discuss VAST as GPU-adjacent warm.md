---
entities:
  people:
  - '[[Sam Hopewell]]'
type: transcript
source_type: unknown
date: '2025-10-22'
---

# 1:1 — Sam Hopewell — 2025-10-22

> [!info] Purpose
> Build trust, surface and remove blockers, align on priorities, coach & grow.

## Summary

Jason (VAST) reconnected with Sam (OpenAI) to discuss VAST as GPU-adjacent warm storage, NDA boundaries, global namespace/caching, and a pending POC. Sam outlined bandwidth constraints due to firefighting and a goal to enable research on applied clusters via local storage to isolate from network/Azure variability. Possible in-person sync in San Francisco Nov 4–6; Jason will follow up.

## Key facts learned

- Jason now leads VAST strategy/direction for hyperscalers and cloud platforms.
- OpenAI tiering view: Azure cold storage, VAST warm storage, on-GPU hot storage.
- Goal: use local storage to enable moving Applied clusters to Research despite weak connectivity.
- Strong resistance to non-OpenAI components on GPU nodes unless throughput is clearly improved.
- OpenAI exploring its own global namespace; concerns about metadata scale and SPOF.
- VAST willing to add features (e.g., Blob-compatible API, global namespace, KV cache); CEO committed to closing gaps quickly.
- POC cluster (CoreWeave) is pending go-ahead; OpenAI bandwidth currently constrained by firefighting.
- Recent storage performance issues traced to firmware/kernel config; now resolved.
- Org: Udi is above Rory and Sam; Rory owns Frontier clusters; Udi reports to Greg.
- Melissa handles Neo clouds/CoreWeave hardware (Kevin Park’s team); team added Misha (London).
- DAC may want to test the cluster once available.
- VAST targets multi-exabyte namespaces; OpenAI skeptical due to metadata scaling limits.

## Outcomes

- Shared understanding of VAST as candidate GPU-adjacent storage and potential global namespace/caching role.
- Agreement that Jason will follow up to coordinate a possible Nov 4–6 SF visit with VAST founder and architect.
- POC acknowledged as desirable but timing deferred due to OpenAI bandwidth constraints.

## Decisions

- (none)

## Action items (for Sam Hopewell)

- [x] Work with OAI on possible in-person meeting in San Francisco Nov 4–6. @Jason Vallery 📅 2025-11-04 ✅ 2025-10-27
- [x] Share a concise POC plan and required features (e.g., Blob-compatible API, caching/global namespace) for review. @Jason Vallery ✅ 2025-10-27
- [x] Confirm internal bandwidth and provide a target window to start the VAST POC (CoreWeave cluster). @Sam Hopewell ✅ 2025-10-26
- [x] Loop in DAC/Applied to test the cluster once it is available. @Sam Hopewell ✅ 2025-10-27

## Follow-ups

- [x] Clarify NDA boundaries on what prior workload/context knowledge Jason can leverage. @Sam Hopewell ✅ 2025-10-26
- [x] Evaluate viability and reliability of VAST global namespace and metadata scale for multi-exabyte use. @VAST Engineering ✅ 2025-10-26
- [x] Assess whether a Blob-compatible API over VAST is required/preferred for GPU-node access. @Sam Hopewell ✅ 2025-10-27
- [x] Prepare POC environment details and staging requirements (e.g., CoreWeave cluster) for kickoff. @Jason Vallery ✅ 2025-10-26

## Risks

- Global namespace is a single point of failure and has heavy metadata scaling demands.
- Running additional agents on GPU nodes risks interfering with workloads.
- OpenAI firefighting and limited bandwidth could delay POC start.
- Multi-exabyte namespace scalability and networking constraints may be limiting factors.

## Open questions

- When can OpenAI start the VAST POC (specific date/window)?
- Will OpenAI adopt VAST’s global namespace or manage its own?
- Can VAST reliably support multi-exabyte namespaces under OpenAI metadata/IO patterns?
- Is a Blob-compatible API on VAST required for GPU-node integration?
- What are the exact NDA boundaries for Jason’s prior knowledge when engaging on this work?

> Next meeting (if any): (none)

---

<!-- ai:transcript:start -->

## Transcript (auto)

```text
[00:00:01.04] Sam Hopewell : Silence from 1 minute to 1 hourBLANK You You you you

[00:03:45.06] Jason Vallery :  Jason VallerySam, hello. I can't hear you.

[00:03:54.06] Sam Hopewell : Long time no see.

[00:03:55.06] Jason Vallery :  Jason ValleryYeah, it's been a few months. How's work?

[00:04:00.11] Sam Hopewell : Oh, great. - Yeah, we are super busy. I thought we were busy before, but it turns out we weren't.

[00:04:12.55] Jason Vallery :  Jason ValleryI imagine you've got a lot of capacity going online that needs to be handed over to some researchers to get work done.

[00:04:20.21] Sam Hopewell : Yeah, we've got a lot of capacity that is on fire that needs to be extinguished and then reassembled and then handed over to researchers that do their work.

[00:04:30.13] Jason Vallery :  Jason ValleryOur content. Well, thankfully I'm not on the other side of those panicked iams anymore and I have a little bit more relaxed life at the moment. So, you know, things are a little different for me and I'm pretty happy about it. I'm glad to connect. You know, I'll be specific about the agenda. The role I'm taking over is strategy and direction for VAST as it relates to building out on the hyperscalers, the broader cloud platform, and how to support workloads like yours, and the team's obviously aware of our background working together. what it might take on, you know, what it's going to take to win a customer like OpenAI, and so I wanted to make sure we just connected everything's on the up and up level. You know, first, just the pointy question is I obviously know a lot, like I know a lot about your workload, about your pain points, about, you know, historical. relationships with Microsoft and so forth. I certainly don't want to violate any of the NDAs between myself and Microsoft and the things that I acquired in terms of knowledge working with you. So I just wanted like your candid take of like, what should I forget? And what is it okay that I know?

[00:05:54.52] Sam Hopewell : - That's a great question, I have no idea. Um, I mean, I mean, I think it's okay for you to know that we store exabytes of data and that, that we're not going to store any less data tomorrow than we did yesterday, and, uh, that all things being equal, faster is better. you know, high expectations for, like, list operations and, you know, throughput, and yeah, I mean, the basics, right, like I think.

[00:06:38.75] Jason Vallery :  Jason ValleryLike the things that I think are most interesting to Vast and the scenarios in front of us. are a little bit more on the workload characteristics and the diversity of workloads, between data acquisition, training, the workload patterns associated with training, the diversity of the topology in terms of where you deploy capacity, how you think about central storage versus GPU adjacent storage. Like those characteristics, I think are an important piece of the architecture when we present an offer to you and a solution to you. that I would want to carefully represent. I don't want to get into speeds and feeds and numbers and pricing and commercials. That's certainly something that I consider off limits, but it's more of like the end-to-end data flow across OpenAI and how I know those things come together to deliver an end-to-end solution for you.

[00:07:24.04] Sam Hopewell : - Yeah, I mean, I think, I mean, where I see vast fitting in is like if i were to retcon how we describe things i would call azure cold storage vast warm storage and sort of on gpu storage like you know hot local storage or something

[00:07:52.63] Jason Vallery :  Jason Valleryor something like that, right? - Ultra storage or something like that, use Microsoft's terminology, the ultra is here.

[00:07:56.82] Sam Hopewell : - And so I think what we're trying to figure out with VAST is like, is it a good solution for near to large numbers of GPUs storage, that is, efficient, high throughput, and a place where we can cram a bunch of stuff that we, like, may not have the capacity to soar on the GPUs all the time, but are going to want to be able to, like, pretty quickly say, like, "Hey, let's get as much of this onto the GPUs as possible," and some of it we might be actually we don't care how fast this data is, we will just access it, you know, from VaST directly. So I think that's where I see it fitting into sort of our pattern, is that it would provide like, chunks of storage, like. that basically isolate GPU fleets from the vagaries of network and Azure slowness.

[00:09:08.83] Jason Vallery :  Jason VallerySo, network autarky, staging checkpoints, staging training data, the classic model that you had in Azure of the GPU-adjacent storage, VASP. like, you know, just to give you a little step back a little bit, talk about like, where my next steps landed me, and one of the reasons why I'm excited about Vast is you and I had this conversation many times about a huge proponent of the idea of a global namespace and removing a whole bunch of the complexity of moving data, you know, in and out of what we are now calling cold storage, central storage, and the diversity of places. that you have GPUs across Azure, across third-party fleet, I think it has some really interesting capabilities, and so while the data will certainly continue to sit in blob, is there an opportunity for you to think about global namespace, global data movement, intelligent caching capabilities that we're at fast-freeing? to make your entire workflow a little bit more optimized, leveraged data deduplication, all of those capabilities that have asked for this?

[00:10:17.00] Sam Hopewell : - I mean, maybe, I think, I mean, I think, you know, we are doing, even work on global namespace stuff ourselves. I suspect that we're, because we have a converged layer and then like multiple potential like clusters. cloud object stores on top of it that we are probably going to want to manage our own global state. I don't know what you guys offer in terms of global state management and its performance.

[00:11:07.81] Jason Vallery :  Jason ValleryWell, there's a bunch of capabilities in the platform today. You know, what I'll actually broadly made this this statement. is the marching order from Vast CEO Renan is we'll do whatever it takes, we'll pivot the company to make OpenAI 100% on best. Even if that means the underlying infrastructure is provided by third party Azure, OCI, whoever. The abstraction layer, the namespace, the platform features, the data like whatever it takes to make you successful, he wants that in the platform, and so he's kind of given this carte blanche statement to me, like if you can come up with a set of features that fill an open AI gap, we'll implement it, and one of the things that it brought me a lot of enthusiasm about VAST is they have a ton of engineering muscle, really smart guys, they move fast, they show examples of like turning features... feature requests around in days versus years, which is obviously the experience you've had with Microsoft. So what I'll tell you is like, I think there's a good set of capabilities in the platform today, and if there are gaps, like you have vast commitment to close those gaps quick.

[00:12:13.55] Sam Hopewell : - Okay, that's useful to know. I mean, I think, yeah, I mean. Yeah, obviously our fleet is getting quite heterogeneous as Sam buys literally every watt and silicon wafer on the planet. Like the real Sam.

[00:12:41.32] Jason Vallery :  Jason ValleryYou're the real Sam in my book, bud.

[00:12:45.22] Sam Hopewell : But yeah, like, our, our like, turn up schedule just kind of gets like more and more complicated. We're like, whoa, holy crap, stop buying stuff, man. How are we going to turn this all on? So I think, so yeah, I think we are trying to be, we are trying to get really opinionated about what everything outside of the GPUs looks like because I mean I think there's obviously not a tremendous amount of wiggle room on what GPUs end up where at this point because those. deals are all made at the stratospheric level. But what else arrives in a data center is more within our control. I think the shape of storage SKUs and the shape of compute SKUs and things like that are-- and I mean, obviously, we get to weigh in on what the shape of the GPU SKU is, but I think it's-- much more driven by research demand and and what we think we can make stick yeah

[00:13:59.46] Jason Vallery :  Jason ValleryI mean I think fast is deeply committed to a partnership with Microsoft you can imagine different folks at Microsoft have different perspectives on a partnership but you know what that practically means is that hyperscalers will be a first-class citizen in the vast ecosystem, and so having that set of capabilities and then abstracting away to a common data platform, common global namespace across your providers, seems like a huge win in terms of operational simplicity for you, and that's the vision I kind of see that we should be pushing towards, recognizing that we're not there today. Like, is that something that you even see on the table?

[00:14:37.80] Sam Hopewell : I mean, it really depends on what kind of scale and what kind of reliability, right? Because global namespace comes with the caveat of, like, if there is a problem in your global namespace, everything is down, and also comes with the caveat of... of like the metadata scale is huge. - Yeah.

[00:15:06.35] Jason Vallery :  Jason ValleryYeah, I mean, the Vast architecture has some different scaling challenges than Blob. Just, you know, we could have lots of conversations on this, but you know, it scales in some dimensions far better than Blob and other dimensions not as well. Just the days architecture thing, which I don't know. you've kind of looked at. But so, I mean, a lot to think through and work through there. Just kind of want to get your read on it. Appreciate it.

[00:15:30.72] Sam Hopewell : Yeah. I mean, I think, I think to sort of set, like, expectations, operations on on the GPU nodes are contentious. Basically, anything running on the GPU node that is not the workload is stared at with evil eyes because the purpose of the GPU machines is to feed the research. thing, and you can spend resources on that node if you can say, "I guarantee you that this will improve the throughput of the job." But you have to have a very clear story of, "I'm not interfering with normal operation of the GPU machine." And so I think there's a lot of hesitancy to do anything but open AI. stack on the GPU machines.

[00:16:32.32] Jason Vallery :  Jason ValleryIs that still Boosted Blob primarily?

[00:16:40.53] Sam Hopewell : It's not exclusively Boosted Blob. Like there's now more Rust running and things like that. So there's data coming directly from non-Blob.

[00:16:53.93] Jason Vallery :  Jason ValleryPython binaries into into the storage stack does that statement kind of binds you towards

[00:16:59.01] Sam Hopewell : Standard protocols like nfs versus object and moving that no no i think i think more is just like that that the that there's strong resistance to taking something off the shelf and putting it the storage node or sorry on the GPU node and so like basically putting something that would be like a global namespace component into the GPU node would have to be like very carefully there's nothing like the way it would

[00:17:31.87] Jason Vallery :  Jason ValleryWork is the global namespace would be managed by the vast servers and they would impose a local today 3 endpoint, but a full commitment to go and build a blob API over top of Vast, if that makes your life easier. So you'd have an object API that you continue to access against those local Vast machines that would give you a bucket that is behind the scenes synchronized across the

[00:17:51.68] Sam Hopewell : Code. Okay. Yeah. Yeah. I mean, I think, I think it, yeah, I mean, I think it's-- yeah, it's tricky, because of performance constraints, and sort of converged storage, and the desire to abstract converged storage. So anyway.

[00:18:24.03] Jason Vallery :  Jason ValleryIt is a bit awkward getting to the core of the weeds that I wanted to get to today. I really just wanted to kind of figure out like where you're at in your head around the VAST POC. You know, I've talked to the team here and I know there's like, I think a cluster in core weave that's kind of waiting for some go-aheads to spin it up so you can actually kick the tires. Like how can VAST support your work here?

[00:18:45.34] Sam Hopewell : Yeah, I mean, I think, so we are doing some other experiments right now, and we're trying to figure out exactly when we're going to have bandwidths because of a bunch of other fires that are happening right now, and so I think that's where we are right now. is kind of unfortunately stuck in a firefight, which is kind of blocking some of our bandwidths to engage elsewhere in the stack, and I think we're getting through the backlog of like decisions that need to be made about like timings and things like that, and I think that's probably. what we need to push through to get like the right answers about when to start

[00:19:36.12] Jason Vallery :  Jason ValleryLike spinning up something with vast and in a cluster here. I would imagine like a decision is tied to some tranche of GPUs coming somewhere that needs some adjacent storage like are there hard milestones in this project?

[00:19:53.28] Sam Hopewell : I mean, so right now, we have, for better or for worse, we are starved for GPUs in Applied and in Research, and so for places where we want to-- we basically want to enable moving clusters from Applied to Research. and that's what we are trying to to unblock by doing this is to like take some clusters that were not the right shape for research because they don't have enough connectivity or reliable enough connectivity or bursting up connectivity and basically insulate them from that connectivity with local storage, so such that we can actually train research on them, and so that's basically the target for this project right now is to sort of enable sort of this flexibility in places where there is otherwise a lack of flexibility and that would give us the ability to. but to basically enable more clusters for research use and have the only thing that decides that basically be business decisions about what makes more sense right now to spend compute on. - Yeah.

[00:21:16.69] Jason Vallery :  Jason ValleryMaybe you could update me a little bit on the org chart. Who's this guy, Udi, and where does he sit relative to you and Rory?

[00:21:23.49] Sam Hopewell : He is above Rory and I.

[00:21:26.88] Jason Vallery :  Jason ValleryOkay, so he is Rory and Rory is reporting to Uday. What does Rory own? What does Uday own? What can you share there?

[00:21:35.88] Sam Hopewell : So, I don't know how much I can share there. I mean, roughly Rory still owns like Frontier. clusters, and Uday reports to Greg, right, and covers like a pretty broad swath of things.

[00:21:54.66] Jason Vallery :  Jason ValleryAny opportunities here with applied data acquisition or data platform? Are they looking at similar problem spaces?

[00:22:08.22] Sam Hopewell : Dak is always looking at things. I think, if we spin up a cluster here, Dak is going to want to kick the tires of it to see how it performs for their anti-patterns, or at least Azure anti-patterns, but not actual anti-patterns. So I think there is... potential there. I think, yeah, I mean, obviously, they are still trying to fill all the bites in their own universe. So, I think we'll have to figure out. Like, I think they've got to, like, they've already invested a fair amount of software making. somewhat performant layers above blob to to sort of mask the the otherwise terrible abuse that they would do to blob so I'm not sure like where they are right now and they're like we desperately need something better than blob but I know that they they have in the past been in that place but I think they've just spent a whole bunch of engineering work getting out of it

[00:23:17.44] Jason Vallery :  Jason ValleryI mean, I think one of the things Vast clearly has is crazy high TPS per pebble byte, which was their crazy numbers. I mean, Vast is invested in the KV cash, so there's a KV abstraction over Vast that delivered good performance. So, I mean, there's a bunch of the things you've asked me for and Louie's asked me for and others in the past that are already in the platform, I think, for their scenarios. those dots when we get the opportunity and see if there's support there.

[00:23:41.81] Sam Hopewell : Yeah, I mean, I think the big issue for, like, I think the IOPS, like, per pebbabyte would be, you know, appealing to Louie's team. I think the other side of that is, like, I'm not sure if the pebbabytes per pebbabyte scaling of... a Vast is ready for the insanity that they want to inflict on it.

[00:24:06.04] Jason Vallery :  Jason ValleryWhat do you mean by pebble bites per pebble bite? Like just capacity? Total capacity in a name?

[00:24:09.42] Sam Hopewell : Yeah, so just like raw giant capacity.

[00:24:12.26] Jason Vallery :  Jason ValleryYou know, I was shocked. This is something I didn't know before I joined Vast, but I've looked at some of their hardware SKUs and they're like super dense, and so you can get like an exabyte in like 20 rounds. and that's all finished, and delivers the throughput. It's just, that's insane to me that you can get an exabyte of FLAF in 20 racks of storage. Namespace challenges when you get to the upper bounds because of the way the networking works, it's a networking constraint really. But I think that the opportunity to get to multi-exabyte namespace is certainly plausible.

[00:24:45.85] Sam Hopewell : Yeah, yeah, I think This is this is like the most famous statement in storage is like Multi-examined namespaces are certainly plausible The only people for whom they're like multi-examined namespaces are a thing is Google and I think AWS S3, we'll say it. But I'm not even sure how confident they are about it. Because, yeah, metadata problems are so awful. >> You can get an exabyte and a

[00:25:25.46] Jason Vallery :  Jason ValleryBlob account, but you've got to be there by now if you're not. >> No, no, no.

[00:25:30.47] Sam Hopewell : Can get an exabyte. What I said is multi exabyte. I just want I just want to store four exabytes in this region and it's like great. How many IOPs do you want? Lots? Like okay you just need 37 accounts and you'll be fine.

[00:25:48.25] Jason Vallery :  Jason ValleryFair. I mean one of the things, I mean I was talking to the architect on Vash. and I mean, I made it like I told him we should be striving for 10 exabytes in a namespace like that should be our north star that we're shooting for in the short term. He felt like it was achievable. I mean, we're going to run into, you're going to run into hardware issues and networking issues before you run into namespace issues, and that's the biggest challenge. So, but point taken. What's up with your team? I know Andrew's moving to Boston. he said, and you're going to be one very important team member. Has your team changed or grown?

[00:26:20.68] Sam Hopewell : So we've grown. We picked up another person, Misha, who is actually out of the London office right now, and yeah, we're still hiring folks. I don't know, I think we've grown a little bit since last time we were here, but yeah.

[00:26:43.32] Jason Vallery :  Jason Vallery- And there's a Melissa, what's her role?

[00:26:47.65] Sam Hopewell : - She wrangles Neo clouds roughly. So I think like helps like line up. uh like all the arrival of car weave hardware and stuff like that is she rory's team or elsewhere not elsewhere she's like in the she's in like uh kevin's team kevin park's team yeah oh okay

[00:27:17.83] Jason Vallery :  Jason ValleryGotcha i'm looking forward to working with you guys again. I'm going to be in San Francisco on the 4th, 5th, 6th of November with our founder and with our architect. Would it make sense for us to swing by and say hello?

[00:27:35.68] Sam Hopewell : Uh, of November? Um, maybe. Let me see what, what our current sprint looks like. Yeah. So we have very ambitious plans for baking new models in new hardware regions that are, as I said, on fire, and so that is-- like, I spent the last two weeks-- with like five other deeply technical people trying to diagnose a stupid firmware bug. What turned out to be like multiple, multiple firmware and kernel configuration issues that were like impacting storage performance.

[00:28:28.02] Jason Vallery :  Jason Vallery- On the GPU host?

[00:28:30.72] Sam Hopewell : So we were in the BPF filters and us tracing the programs and catching network packets and yeah, it got crazy. But it works now, so hooray!

[00:28:53.46] Jason Vallery :  Jason ValleryWell fun. It seems like you're in the weeds then, hopefully you can go prepare and work on the longer term problems together. Well, anything else I should know or be updated on or can help you with?

[00:29:07.03] Sam Hopewell : No, it's great to see you again. I'm glad you found somewhere that is more useful. your speed and maybe moves at a pace faster than I can. - Sure.

[00:29:20.11] Jason Vallery :  Jason Vallery- Far less politics, man. The politics at Microsoft got so ugly. You know, this is a breath of fresh air in that sense. Like, these are good guys to work with and they're just focused on the engineering and that, the rest of it gets left behind. So, pretty excited about that culture difference. Yeah, well, I'm looking forward to working with you, I'll ping you with more specificity around the fourth to six, maybe if you can spare a chance, we'd love to swing by and say hi, and I can introduce you to the founder of vast and the architect, you know, we can try to be tactical and work on the POC and come up with a more specific agenda if you guys are ready, and just know that you've I have clear commitment from the CEO to do whatever it takes to win you and make you successful and great engineering team ready to go and take your requirements and turn them into reality.

[00:30:12.51] Sam Hopewell : Okay. Awesome. Thank you, Jason. It's great talking to you. Bye. Bye. You
```

<!-- ai:transcript:end -->
