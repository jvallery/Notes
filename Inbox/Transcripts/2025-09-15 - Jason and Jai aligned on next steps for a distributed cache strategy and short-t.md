---
entities:
  people:
  - '[[Jai Menon]]'
type: transcript
source_type: unknown
date: '2025-09-15'
---

# 1:1 — Jai Menon — 2025-09-15

> [!info] Purpose
> Build trust, surface and remove blockers, align on priorities, coach & grow.

## Summary

Jason and Jai aligned on next steps for a distributed cache strategy and short-term actions. MAI currently prefers simple async copy of checkpoints from local NVMe to Blob and will only consider BlobFuse if it clearly improves performance and reduces complexity at MAI scale. They will evaluate BlobFuse+ACStore against alternatives (Manifold/Singularity, OpenAI TensorCache, Alluxio, JuiceFS, NVIDIA AIStore), structure use cases by fan-out writes, fan-out reads, fan-in reads, and treat KV cache separately. Jai will create a shared Teams space, coordinate a Manifold deep-dive, and plan the Oct 15 SVC offsite; Jason will test BlobFuse and TensorCache, review Manifold materials, and draft a scenario-based recommendation.

## Key facts learned

- Team offsite planned in Silicon Valley on 2025-10-15 for ~1.5 days (social/dinner on day 1; half-day on day 2).
- MAI checkpointing: write to local NVMe, async copy to Blob; no need for BlobFuse unless it proves clear benefits.
- BlobFuse private preview currently focused on fan-out writes; limited read caching maturity; recent 100-node CycleCloud test and deployment guide pending.
- Alternatives under review: Manifold (fka Singularity, led by Whipple), OpenAI TensorCache, Alluxio, JuiceFS, NVIDIA AIStore.
- Manifold vs TensorCache perf doc exists; Manifold reportedly outperforms TensorCache in shared results.
- Design questions: consistent hashing vs metadata store scalability; potential need for a high-TPS metadata/index store (e.g., FoundationDB).
- Implementation choices impact: Go vs C++, FUSE vs kernel client, and potential DPU/GPU offload for performance.
- Alluxio concerns: IP/China perception and Java stack implications.
- Inference team has been waiting ~2 months for BlobFuse bits after an initial intro; credibility risk.
- North Star: one solution covering fan-out write/read and fan-in read; treat KV cache separately; align with platform/hardware where practical.

## Outcomes

- Use-case framing agreed: fan-out writes, fan-out reads, fan-in reads; KV cache handled separately.
- Proceed to evaluate BlobFuse+ACStore against Manifold, TensorCache, Alluxio, JuiceFS, and AIStore with a clear recommendation.
- Create a shared Teams space for all related documents and links.
- Plan to include DPU and inferencing (e.g., Rajat Monga) sessions at the Oct 15 offsite.

## Decisions

- Jason will travel to the Silicon Valley offsite on 2025-10-15.
- Centralize collateral in a new Teams room for the distributed cache workstream.

## Action items (for Jai Menon)

- [x] Book travel for Silicon Valley team offsite (~1.5 days starting 2025-10-15). @Jason Vallery ⏫ ✅ 2025-10-26
- [x] Create a Teams room for distributed cache work; upload/doc links (Manifold/Singularity slides, comparison docs) and grant access to stakeholders (Jason, Jean, Jagan, etc.). @Jai Menon ⏫ ✅ 2025-10-26
- [x] Review Manifold materials (incl. Whipple’s perf comparison vs TensorCache) and prepare questions on consistent hashing and scaling. @Jason Vallery ⏫ ✅ 2025-10-26
- [x] Obtain and test BlobFuse private preview when available; validate fan-out write performance and any read caching behavior. @Jason Vallery ⏫ ✅ 2025-10-26
- [x] Obtain and test OpenAI TensorCache for comparative evaluation. @Jason Vallery 🔼 ✅ 2025-10-26
- [x] Draft a scenario-based recommendation (fan-out write/read, fan-in read; separate KV cache) and positioning per customer (e.g., MAI). @Jason Vallery ⏫ ✅ 2025-10-26
- [x] Plan Oct 15 offsite sessions (DPU topics, inferencing/KV cache) and social/dinner; confirm agenda and invites. @Jai Menon ⏫ 📅 2025-10-15 ✅ 2025-10-26
- [x] Share Manifold/Singularity slides and provide intro/contact for Whipple; add to the Teams room. @Jai Menon ⏫ ✅ 2025-10-26
- [x] Coordinate with Vishnu to ensure BlobFuse PP bits and deployment guide are shared with inference and evaluation teams. @Jai Menon ⏫ ✅ 2025-10-26
- [x] Decide flight timing adjustment to attend the Garish storage meeting if needed. @Jai Menon 🔽 ✅ 2025-10-26

## Follow-ups

- [x] Schedule a Manifold deep-dive with Vipul/Whipple’s team; circulate invite and pre-reads. @Jai Menon ⏫ ✅ 2025-10-26
- [x] Set up a focused call with MAI to capture concrete requirements, scale targets, and evaluation criteria for adopting a cache. @Jai Menon ⏫ ✅ 2025-10-26

## Risks

- BlobFuse private preview delays risk credibility with internal inference stakeholders.
- MAI may not adopt BlobFuse without proven performance benefits and reduced complexity at target scale.
- Consistent hashing approaches may complicate cluster scale-in/out and rebalancing.
- Potential performance limits with Go/FUSE vs a C++ kernel-mode client; hardware offload path increases scope and timeline.
- Open-source dependency risks (IP perception, security/patch velocity), especially with Alluxio.
- OpenAI TensorCache reported instability/churn could impede reliable evaluation.

## Open questions

- Specifically why can’t MAI use BlobFuse today (APIs, complexity, performance, operational constraints)?
- How does Manifold’s consistent hashing handle cluster scale-in/out and rebalancing with minimal disruption?
- Do we build our own high-TPS metadata/index store or rely on an external option (e.g., FoundationDB)?
- Are Go and FUSE sufficient for required performance, or should we target C++ and a kernel-mode client?
- What is the feasibility and timeline to leverage DPU/GPU offload for the cache datapath?
- Is Alluxio acceptable given IP/China perception risks and its Java stack?
- What are the benchmark targets and KPIs (throughput, latency, durability) MAI needs to justify adoption?
- Should we pursue one cache solution to cover fan-out write/read and fan-in read now, while treating KV cache separately?

> Next meeting (if any): (none)

---

<!-- ai:transcript:start -->

## Transcript (auto)

```text
[00:00:00.04] Remote : (mouse clicks) you You Jason. Jay, hello, sir. How are you? I'm doing all right. We're good.

[00:03:05.09] Jabra Speak 710 :  Jason ValleryFeels like a bit of a busy week, having to travel to Redmond tomorrow, but...

[00:03:06.05] Remote : I heard there's an LT off site. You've got to be kidding me. I'm not kidding. I'm not kidding. I'm not kidding. I'm not kidding. I'm not kidding. I'm not kidding. I'm not kidding. I'm not kidding. I'm not kidding. I'm not kidding. I'm not kidding.

[00:03:19.11] Jabra Speak 710 :  Jason ValleryI'm not kidding. I'm not kidding. I'm not kidding. probably got are you doing anything with the storage developer conference isn't that this week too

[00:03:26.56] Remote : Yeah i'm not doing anything with the storage developer conference thank gosh that would have been one more thing i couldn't handle i'll tell you you look like you look you look younger you know like i don't know what you like you know you're all Nicely shaven and shorn or something. I don't know what it is, but you look like you lost a few years, which is good

[00:03:51.86] Jabra Speak 710 :  Jason ValleryWell, that's that that primarily it's that you teased me when we spoke last because I hadn't shaved over the Sabbatical over the sabbatical. I just grew like a big bushy beard Uh, but now that i'm back at it meeting with folks i'd be like I have to look presentable again. So, uh, Yeah, definitely shaved and you know actually hopefully I'll see you in person soon enough but over the summer I did a lot of running

[00:04:13.17] Remote : And that sort of stuff so I lost some weight and you know I've got some energy going oh good good stuff yeah good good good I've been losing weight too so yeah that'll be good it'll be good to see

[00:04:23.35] Jabra Speak 710 :  Jason ValleryYou again actually that was one of the things on my agenda which is here there's some sort of team I got an email from Heather about it, but I haven't talked to you about it. Do you, should I be booking travel to come out to Silicon Valley?

[00:04:38.31] Remote : Yeah, yeah, yeah. That's right. Yeah, we're, we're having, October 15th, we're having a, we're having a, yeah, it's just one of those, you know, bring the team together, um, and it's like a day and a half. Yeah, I think. Yeah, that's right. I'd forgotten about that. But yes, it's happening October 15th. Yeah. Well, you know, I think we'll. Yeah. I think we have a budget. People can travel. Be a good thing for, you know. for us to get together as a team. We've got some diversity in work and projects now, so it'd be good to just have us all together. Yeah, I was planning to get a bunch of the... You know, the reason I'm having it in California Redmond, because the first option is obviously Redmond, fewer people get to travel, right? And I said, "No, we'll do it here," is I think, you know, also a good opportunity for people on my team to meet some of the DPU guys and just sort of get a sense of, okay, what's happening? When's the next chip? What's the next chip going to look like? And you know, what's the FunOS programming environment like, so if you wanted to do, you know, other interesting things with the DPU. So at least a set of the topics will be, will be, you know, related to that and it's just very convenient because all these guys are here. Yeah, I might reach out. I haven't done that. yet and I don't know whether it'll work out, but the inferencing guys are also here. There's a guy called Rajat Monga who leads some inferencing stuff. I'm going to try and see if I can get him to come and tell us what they're doing, you know, with KV caching, inferencing, how they fit into the OpenAI inferencing framework. work which is not open source. Um, if he ever did a KVCache, like what would, what kind of requests might he make to us? I mean, you know, just, I mean, just maybe not that level of detail, but enough to just have a, you know, just, just get a sense from him. So I, Maybe I'm thinking GPU folks, and... Yeah, so it's a day and a half. We'll probably have, you know, one or two sessions in the morning, a session in the afternoon, and then we'll, you know, we also get to either do some sort of social event together or maybe just go out to dinner together on the first day, and then the second day we'll just have one session so people can then fly out to their respective homes. uh right after you know yeah let him let him let him go right around noon and yeah we're not we're not planning early starts to the day or anything these are just fun casual you know let's get together kind of stuff so that's the plan yeah you should definitely yeah i think when we when we submitted the budget for this thing of course were not part of the team so your travel wasn't was not included but but how can I not include you so yes of course you must travel well I'm excited I'm excited to meet the team and get to

[00:08:05.13] Jabra Speak 710 :  Jason ValleryKnow you know everyone a little bit better and what everyone's working on um you know the last since we spoke last kind of that's what I've been focused on generally is reconnecting with folks and understanding kind of what happen. I did get the chance to meet with Ankit and kind of hear a little bit about what he's up to. I met with Lukash and learned about what's going on with Bifrost and so I've got some good updates from them and you know just looking forward to connect to the rest of the team and learning

[00:08:29.15] Remote : What they're doing. So yeah, it sounds good. Perfect, perfect. Yeah, no I think, yeah I think and you also bring a lot of background and knowledge that they don't have, so I think it'll be, it'll be super interesting for them as well. So, that sounds good.

[00:08:49.54] Jabra Speak 710 :  Jason ValleryI don't know what formal agenda you had for today. I mean, I could talk a little bit about where I'm at in my thinking around distributed cash and, you know, the paper you sent to Linda this morning and so forth.

[00:09:00.22] Remote : Let's talk about that, yeah, I'm super interested in, I mean, you were on the call today, right, with Pete Iming and so on? I mean, I mean, you know, what is it that we're, what is it that MAI wants that we're not building, and why is it that we're not building what they want, is kind of my question. That's one of the, I mean, you know, and you saw, I mean, you saw, I don't know if you got a chance to actually, you know, at least skim through the paper, but ultimately, you know, trying to make sure we make a decision around, you know, do we continue with BlobFuse or do we do, you know, something else? And the problem is that... you know, new kinds of caches keep popping up. Manish gets aware of them and then he says, "Why aren't we using that?" Right? So, there was a talk by Whipple last week on his Singularity cache, which is now called Manifold. I don't know why they keep changing the name of these things, but Singularity is now called Manifold, and then he's got this Manifold cache. sent me this paper which is referenced in the doc about his performance comparison of his manifold cache versus what OpenAI is doing which is I didn't I had not heard this name before but apparently it's called tensor cache and so uh yeah so he's got some performance numbers in there which Maybe not surprisingly, but Whipple's cash whips the shit out of TensorCache is what he's showing there. So we got that, and then Elixir is always lurking because any time you look at them, they've been around a while, they're pretty stable, more and more people are using them. them. They just came out with a clean solution for KV caching. So yeah, I'm just trying to sort through the options and part of the reason I built that table, and I did it last night, you know, I was like, was like, okay, you know, I just need to have some sense of How do these things compare and are we building the right thing? I mean, Nagender is a smart guy. He's also, I didn't know him from before, but he's also a little bit, you know, it's hard to change his mind on things. He's one of these guys that like, bullheaded, I mean, maybe that's a dirty word. you know, but it feels like he's doing things a certain way and like, you know, anything else, like, "Why should I change again?" kind of thing. But anyway, need to understand, you know, what he's doing. I mean, I'm sure he'll build something that's got good... performance. He seems to have a performance orientation, and, you know, but there's always been questions of, is Go the right language? Is Blobfuse the right interface? So all these things keep propping up, and the short summary of what I heard from Pete, to my question, was somehow MAI can't use BlobFuse, but I wasn't sure why. Yeah.

[00:12:31.68] Jabra Speak 710 :  Jason ValleryWell, I can probably give a little context on that as well as my bigger picture thinking. MAI was pretty clear even before I left that they have this working solution, which was copy, and the way they used it for checkpointing, now this is one of my macro pieces of feedback we'll get to in a second about the document, but for checkpointing rights specifically, what they already do in their existing CoreWave cluster where we deliver the premium blog for them to use, is they they just write to local NVMe on the GPU host, and then they have a background process that just easy copies the write from the local NVMe to Blob Storage. Super simple. Like it is just dead simple, all we have to do, write local, then copy it off async, and for them, like that is. simplicity they are familiar with and what they were going to continue to use, and I have the code they wrote actually. They wrote some Python code that does this, right? It uses put blob from URL to move things around and it uses copy APIs to move it from local up to blob, and for them, like that is what they are looking for. Just the simplicity of orchestrating. moving checkpoints from local storage up to blob storage, you know, they don't need all the complexities of blob fuse, and so I think that they're happy with

[00:14:01.64] Remote : Continuing down that path because... So on that one, is the write considered complete once it's in local or does it have to wait for the AZ copy to blob to complete because that would make the checkpoint slow, right? If you have to wait.

[00:14:17.23] Jabra Speak 710 :  Jason ValleryYou don't, there's no, they're not even related processes, like it writes to local MDME and moves on, there's something else just sitting like watching the folder and doesn't copy. Um, and the thing about these checkpoints is, is like worst case scenario, you've lost some component of it, like some chart of it, they just go to the previous one. It isn't a catastrophic loss. So I think like one of my pieces of feedback about the doc that you shared is that it doesn't really touch on the scenarios for distributed caching and then aligning what the solutions are for each. If it is purely distributed caching for rights, then yeah, BlobViews is probably overkill for MAI and you know, other customers. can probably do what MAI is doing if they needed to. It is really like, I think we should break the doc apart based on fan-out writes, which is sort of a checkpoint scenario, fan-out reads, and fan-in reads, and then have a separate treatment around KVCache, 'cause I think that's a whole other ball of wax to go solve. at the three key scenarios of fan-out-write, fan-out-read, fan-in-read, we may--

[00:15:28.50] Remote : What do you mean by fan-out-read and fan-in-read?

[00:15:31.79] Jabra Speak 710 :  Jason ValleryYeah, so fan-out-read is this scenario where you have one host who's reading data from a variety of objects at the same time. So this is primarily going to be the training data case where the data spread across the distributed cache and you've got replicas on a whole bunch of nodes. You have one node who's reading pieces of that across the distributed cache. Okay. Sure. Okay. You can read as the inverse scenario where you've got a whole bunch of nodes who all want to read the same piece of data,

[00:16:06.30] Remote : and that is why... model loading or what is that?

[00:16:11.55] Jabra Speak 710 :  Jason ValleryIt's going to be model loading or you've got some other large artifact that you're distributing out to the nodes, some user data, some library, whatever it is, right?

[00:16:21.34] Remote : Yeah, but I mean isn't the best way to do model loading, load it into one guy and then use the back-end network and get it out to all the other guys? I mean, why would I want to do...

[00:16:30.31] Jabra Speak 710 :  Jason ValleryThat's what they're doing, it's a fan and read, right? So they're doing that themselves already via different mechanisms, but ultimately,

[00:16:36.54] Remote : They're fan and read distributed cash kind of problem. - Yeah, yeah. But I mean, I think the thing I'm trying to avoid is creating three solutions for three problems, right? Because, you know, that's why if you read the doc and, you know, it was also based on other email threads with Manish, which, you know, I won't bore you with but ultimately, you know, we if we're going to build something we should build something that's satisfies all of those scenarios not something that says oh, you know for For training. Let's use this cache for model loading. Let's use, you know, the manifold cache, and then for, you know, checkpointing, let's use opening eyes cache. I mean, or at least if we're building something, we might as well build it to cover as many of the cases as we can. I mean, that seems like a reasonable goal to me. So that's what I've stated in the doc, right? I agree. I mean, from a North Star perspective,

[00:17:37.82] Jabra Speak 710 :  Jason ValleryBut if what we're trying to do is solve some of these short-term pain points, I think we should be intentional around what we're positioning, which customer, for which distributed campaign scenario, because there are existing examples that can be used, and where does Alexio fit in, what are the scenarios Blobviews are targeting. I met with Vishnu as well to kind of get an update on what's going on with Blobviews. I know there's a meeting about this too. tomorrow too, they've only focused on fan outrights. Like what they've got in this private preview is fan outrights. It has no read caching of any meaning capabilities, and they haven't done a lot of scale out testing on it yet either. So we haven't really seen how it'll play in sort of an MAI world yet. I'm anxious to get my hands on it. Vishnu said he'll be able to share it hopefully by the end of this week so we can do some testing with it, but you know they did.

[00:18:31.53] Remote : You know, I tell you, you know, I met with the inferencing guys here because they're just local here, they're at SVC And, you know, they were very interested in using BlobFuse, and this was like two months ago, and I set up, I mean, I set up a call, and I brought Vishnu in, and the inferencing guys, and we had a nice call, and they said, "Okay, you know, give us something, and we'll try it out." That was like two months ago, and we never sent them anything for, I mean, it's been like two months, and I mean, I feel a little embarrassed because, I mean, I set up the meeting and, "Oh, yeah, we've got this great thing. You guys should try it out. Oh, yeah, great. Send it over. We'll try it." And it's like, you know, "Oh, yeah." And we said, "Oh, yeah, yeah, it should be ready in the next week." Then radio silence. You know, then I learned Vishnu was in India and he wasn't responding to either my emails or texts until he came back from India and, you know, time passed then, you know. Anyway, yeah, I mean, so I'm holding my breath on, "Yeah, it's ready next week for you to try." I'm like, "Yeah, maybe." Well, I'll find out in the morning.

[00:20:02.86] Jabra Speak 710 :  Jason ValleryI talked to Vishen at the end of last week, and he said it sounds like it's pretty much ready. They just did a test with 100 nodes. So they spun up a CycleCloud cluster, 100 nodes, half a million nodes. It's pretty much ready. So they spun up a CycleCloud cluster, 100 nodes, half a million nodes. It's pretty much ready. They just did a test with 100 nodes. So they spun up a CycleCloud cluster, 100 nodes, half a million nodes. It's pretty much ready. So they spun up a CycleCloud cluster, 100 nodes, half a million nodes. It's pretty much ready. Bob views on it simulated checkpoint writing across the hundred nodes and have some performance numbers from that testing Based on their experience doing that they're finalizing a deployment guide and he said they hopefully will ship that this week I don't know if that was the gate to share with the inferencing guys that they wanted to have like that Indian deployment guide ready to go, but

[00:20:36.41] Remote : That was me just ranting a little bit little bit to you that's all I mean you know it's just we're we're here I can rant it's okay I'm allowed to rant once in a while it's it's nothing nothing serious it's just I'm just reminded of the fact when you said that I was just reminded of the fact that we promised something something to somebody like two months ago and nothing happened. But I mean, and I've been hearing forever, like, "Oh yeah, MA is about to, you know, try this thing. We're about to give this to MAI." And that's another reason I asked the question today, like, "Are we? Are we?" You know, like, and Pete's got a different point of view. Pete's opinion is.., and I don't even want it, you know, what we're not gonna give it to them. They don't even want it

[00:21:26.81] Jabra Speak 710 :  Jason ValleryI think that's his view. I mean Pete's obviously been more plugged in over the last couple months than I am. I'll say the perspective that I had from MAI when I brought this up most recently with them before I went out was that they were marching forward with their plan A to be just lazy copying of data and

[00:21:43.94] Remote : Yeah

[00:21:46.25] Jabra Speak 710 :  Jason Valleryto entertain blob views, if we could demonstrate to them that it would improve performance and reduce complexity, and so, if we have a compelling proposal to go to MAI and say, "Look, here's how blob views makes your life better compared to what you're doing today," they're probably not going to spend cycles on it. But if we can come up with a narrative that says, "What you're doing today is going to have these inefficiencies." and it's more complex, and here's the risks, and here's how Blocky solves them, and, oh, by the way, we already benchmarked it, and we know it's going to hit your scale points.

[00:22:16.32] Remote : Then they'll go and take your good. Yeah. Yeah. You know, I think that's great. I mean, I think you should get it. I think you should play with it. You should get TensorCache and play with it. I mean, you know. I don't know if you saw the garish email this morning, but I saw that and I'm like, "Me? Okay. Yeah. Yeah. I know." And I'm supposed to fly tomorrow to Redmond, and then he's called this meeting with just a few people, like five or six people, and I'm the storage guy in it. you know, I'm wondering now if I should change my flight time so I should, you know, so I can attend this call. I have to sort that out. So, I guess, I guess someone's told him I'm supposed to be the guy for storage or something because he's starting to pull me in here. We'll figure it out. Thank God you're on my team.

[00:23:15.42] Jabra Speak 710 :  Jason ValleryI'll do my best to help you, Jay. Let me know how.

[00:23:17.58] Remote : - Absolutely, you bet. First help me sort out the distributed cash thing and then we'll go from there.

[00:23:25.82] Jabra Speak 710 :  Jason Vallery- So my quick to-do list is I went and, what I also did while I was streaming out last is I went and took a deeper look at Biloxio, JuiceFS, what kind of opening-- or what NVIDIA is kind of talking about with AI store. I looked at, I think IMG, Coral Weaves, Loda thing, which by the way, that's a read cache only. Just to be clear on what--

[00:23:49.07] Remote : - That's a read cache only, yes, yes, yes. That's a read cache only.

[00:23:53.39] Jabra Speak 710 :  Jason Vallery- Yeah, like a reverse proxy. They're just proxying requests to object storage, and just kind of get a sense of the lay of the land to do. So I mean I feel like I've got a good head around where we stand as an industry. How do I take that forward.

[00:24:09.99] Remote : >> DIANE DEBACKER: Yeah I mean I think that. I mean. I mean, how do we compare these things, you know? Should we take a look at that table? Should we have other roles? Should we do something else? You know? I mean, ultimately, the endgame is we come out with a recommendation, right? That's what people are looking to me for, and I'm looking to you to help me sort out the answer of... Do we say yes continue with blobfuse? Do we say oh, why don't we just use? You know Alexio or why don't we just use Tensor cache or why don't we just use you know? I mean the latest one that got dropped into the into the maelstrom is this You know Whipple gave this very nice talk and everyone listened to him and he's like, "Okay, this sounds really interesting." And they don't have a metadata store, and so they claim it's super easy to use. In place of a metadata store, I guess they do some sort of consistent hashing to figure out where the object is.

[00:25:29.19] Jabra Speak 710 :  Jason ValleryAnd -- though, you can't scale the cluster in and out if you use consistent hashing, right? So that, well...

[00:25:35.79] Remote : Yes. Scaling, scaling, I mean, we need to understand, yeah, how the scaling would work, how they're doing it. According to him, OpenAI's cache had a metadata store and they've given up and gone to this hashing scheme because of... their discussion with you know with Whipple and team. So somehow he's convinced them it's apparently the right thing to do. So that's interesting and we should find out and then that's yeah help me find out how are they solving the scaling problem, right? You know it's not always going to be a static number of nodes. So what happens is you scale and... how do they adjust the consistent hash to make that work? I think those are the kinds of things that we need to understand before we can land on a on a decision. I mean it'd be helpful to knock things out quickly, like, okay, like for example, according to VIPL, the opening ice cache is still under active development it's changing every day and he's he's finding bugs in it it crashes that doesn't give me confidence that's something I should be using now if that's really the reality of what what's happening there so that might be an easy way to say well I can't use it that's not the answer

[00:27:02.14] Jabra Speak 710 :  Jason ValleryYou know, Sam Altman said publicly in the last couple of weeks that their engineering focus for GPT-6 is memory, and how we scale out long-term infinite context, and so you have to imagine there's a ton of churn happening on those layers of the system, because ultimately that's what supports memory for them. So I, that doesn't surprise me. Um, okay, well, a couple of things, can I get introductions, docs, wherever this stuff sits around the Singularity Manifold Catch, that's one I haven't looked at. I don't know where to turn to find out about that. So if you've got collateral or people I should go talk to, I'd appreciate it, and then you, I actually don't know who Whipple is, who's Whipple?

[00:27:51.84] Remote : Whipple is the guy, he's the VP in charge of the Singularity thing. Oh, so that's it, okay. Which is now Manifold, which is now Manifold, yeah, he's he's the Manifold guy. I mean, they changed their name from Singularity to Manifold, so that's just a new name for it, but be there. I mean, and yeah, and he did, I mean, there were, there was some, yeah, I need to get the slides that he shared, so I can, I can send them out. Yeah, I'll create a team room and just start putting everything in there, so everybody, you know, that way, you and others that I'm involving in thinking here, and, and also, you know, Jean. and Jagan can all like just give access to everybody so everybody's got the same same team room with all of the docs in it. Whatever docs I have I'll put in there. Vipul promised me on Friday or Thursday of last week that you know he he would set up a call for us so that rather than after we dox that he would have the team, you know, present and we could ask as many questions as we wanted. I think that's a good idea. So whenever that happens, I asked him if he could do it Monday or Tuesday, but I haven't heard from him and I'll be traveling tomorrow. So I assume it's not going to happen that quickly, but we'll sort out a time. when that can happen and invite everybody so that the doc that I shared with you there is there is a link to a comparison of singularities cache versus open AIs cache so that there is a doc there there's a link to a doc there that you can go look at did you did you see that or did you get a chance?

[00:29:40.92] Jabra Speak 710 :  Jason Vallery- The doc, I didn't see the link. I went through the doc, let me see. You also keep alluding to a table and I actually didn't see a table in it. So I'm wondering if I'm looking at the wrong doc.

[00:29:51.53] Remote : - Oh.

[00:29:52.27] Jabra Speak 710 :  Jason Vallery- I see it. It's an 11-page doc. It has a couple of appendices, but I actually see no table in this thing. Okay, it's the one you left in the email earlier, so I wonder if there's more than one doc or something?

[00:30:09.73] Remote : Can you like refresh or something? Is it, is it just, you're just looking at the, like, I think I put the doc in last, last night, so if you looked at it prior to that. You still don't see it

[00:30:28.13] Jabra Speak 710 :  Jason ValleryOh, I see kind of like a blurry screenshot at table It has metric block views plus AC store tensor cache manacle cache. Okay. Yeah, I just need to refresh the browser Okay, let me take a closer. Look at the table thing

[00:30:42.91] Remote : All right, I want to send it

[00:30:46.28] Jabra Speak 710 :  Jason ValleryIf you've got like two minutes, can I ask you a question?

[00:30:51.71] Remote : Yeah, go for it.

[00:30:53.70] Jabra Speak 710 :  Jason ValleryStrategy. When I think about what we want to position as we respond to this, you've got the open source ecosystem which has a mature set of options. Eluxio, JuiceFS, whatever we go and decide is out. there, and we've got the, we're going to build something internally, and I think the value of building internally is when we leverage platform primitives, we leverage hardware offloading, we leverage the things that are unique to our storage platform and where we're headed with our storage platform. So, you know, if we did something with Delta Zero or otherwise. So if I was to define a North Star vision, it would align to are we trying to go and take the best of the open source world and just productize it over top of our current stack, or is it are we truly trying to define a North Star that is integrated end to end with our hardware strategy with our service strategy.

[00:31:53.62] Remote : Yeah, I mean, so, yeah, so I mean, I think there's like three options, right? One is build our own, two is open source, and three is, you know, use something that's available in some other part of Microsoft, like Manifold or OpenAI fit into that category, So those are the three. Do our own, open source, or that, right? Those are the three options. I think that... I think even if you went down the open source path, it will ultimately become... I mean, the work involved will... similar to do it yourself, because we would never take true open source, right? I mean, at the end of the day, we would, just like AC Store did, right? I mean, they picked up some open source, but then they forked it, and then they owned it, and then it's theirs, and, you know, they can make any change they want, and if there's a life side issue, they can go fix it So ultimately, yeah, it's sort of a open source gives you a starting point, but there's still a lot of work to be done. I mean, when I talk to Krishnan, he talks about how much work it took for him to take this thing that was supposedly open source and make it AC Store. It was a lot of work, is the way I understood it to say. Once you do that, I think you have the same benefits as it being doing it yourself. Anyway, so to me, those two longer term, I think at the end of the day, they both give you the ability to integrate better with delta zero and all of these other things that we want to do. Right?

[00:33:45.72] Jabra Speak 710 :  Jason ValleryThe follow-on question was what you alluded to around this consistent hashing problem and how metadata gets stored and whatever challenges OpenAI had is, are we going to go build a high-performance, high-TPS index metadata store that we can leverage from a distributed cache, or is it we're just going to let that be an open-source ecosystem problem foundation DB, whatever that ends up being, and we're not gonna go there. Anyway, I think those are all the open questions.

[00:34:17.49] Remote : - Yeah, yeah, yeah, those are all. - Okay. - Those are all good questions. Those are all good questions. I mean, I don't have a strong point of view the other is absolutely, you know, in or out. I think that, I know that Jürgen had some issues with Alexio having to do with China and IP and stuff, which I don't know how real his concern is, but he had some. sort of a concern. Oh, you know, this is China, and can we trust? Or, even if we can trust, will our customers, once they learn that we're using some Chinese IP, is that a problem or not? I don't know if that's real or not. I mean, do you have a sense of whether that's a realistic concern?

[00:35:15.71] Jabra Speak 710 :  Jason VallerySure there's nothing in the code that is malicious in itself, we'll have those sorts of audits done. I think the bigger picture is, you know, are you dependent upon them for security fixes? Are you dependent on them for future hot fixes? Are you dependent on like that entire ecosystem such that you now don't have to choose your

[00:35:34.29] Remote : Own destiny?

[00:35:35.35] Jabra Speak 710 :  Jason ValleryLike that's where it becomes problematic. The other thing about Eluxio is that it's not just a platform. Maybe this is my own toxic reaction is it's java. So i'm like java. That's what we're going to build this on Um, so I think there's that dimension of it

[00:35:48.13] Remote : Um, it feel it just felt like when we did that is that still true that alexia was java

[00:35:53.49] Jabra Speak 710 :  Jason ValleryI mean these guys could have moved on my understanding is the metadata. So that's probably where some of the okay

[00:36:00.72] Remote : And scalability end up being. So, I don't know. Yeah, yeah. No, I mean, I think anything we can do to eliminate options and settle on the right option, the faster we do it, the better, as far as I'm concerned. I would love to just go back and say, okay, this is our decision. Done. Let's move on. Okay. That, I mean, help me get there as rapidly as possible. I'll be out. grateful. I mean, I don't want to make this a research project forever kind of thing. We need to decide and move quickly, trust our instincts, trust our gut, and do things. I think on Blobfuse things we need to get comfortable around. First of all, you know, Nagendra, he's doing a read and write cache, not just a read cache, so we need to sort that out, and then I think there's just a few performance things, you know. Is Go going to give us the performance we need? Do we need to, you know, move to something else like C++? at some point that's extra work. Is FUSE going to be fast enough? Do I need to go do a kernel client instead of FUSE client? You know, I mean, all those things, we've made some decisions, but you know, if all those things are true, then there's a lot more work than we thought in the beginning.

[00:37:27.76] Jabra Speak 710 :  Jason ValleryThat touches on what I was alluding to around if we go down a pathway... where hardware offload becomes part of the consideration. You know, if we're going to have GPUs in the GPU host that we're gonna need a kernel mode driver for, like that's gonna run in kernel mode and then we can push as much of that out of the CPU stack as possible, and I think that would be the best performance win across the board.

[00:37:51.31] Remote : But obviously, - Yeah.

[00:37:53.25] Jabra Speak 710 :  Jason Valleryto the highest risk, most resource-intensive project of the spectrum. So if we're going to go all in there, we need to go all in there, but we're probably not going to deliver that anytime soon. So it means what do we do in terms of time to market for now until we can get to that

[00:38:08.95] Remote : Vision? Yeah, exactly. Exactly, and that would be a fine solution. think we need to have something. I mean, MAI is clearly a very, very important customer. We got to find a way to have them start leveraging some of our technology. So what does it take to make it interesting for MAI to use whatever we build, I think? Otherwise, I don't know. OpenAI is not going to use our cache, MAI is not going to use our cache, okay, who the hell are we building this cache for then, right? It's not like we have a hundred other customers. We certainly don't have very large customers where, you know, there's no other foundation model builder that we have. Those are the only two foundation model builders. foundation model builders don't need our cash then why do we care about training and checkpointing because that's what you know foundation model builders do then we just care about model loading you know or something else and and so this is so yeah I think it's crucially important to understand win. I think if we win MAI, I think a lot of people will be happy. I think Girish will be happy. I think Maneesh will be happy. I think that makes me and you happy, you know. So I think we need to understand what these guys, what will they take? I mean, maybe can we set up a call with MAI and say, "What do you need? I know what you're doing now." But, you know, can we do something that, you know, that would help you? What do you need, right? Maybe that's what we need to do. I don't know. I mean, maybe Pete's having those calls, but I'm just not, you know, I don't know what the answer is or what the input is to this exercise. We need some input to this. exercise about what does it take to do something they want as opposed to we're building Blobfuse and then Pete tells me oh but they'll never use it. I'm like okay great why the fuck are we spending money to do this thing? I still think it's a good investment. I think Blobfuse has a

[00:40:28.88] Jabra Speak 710 :  Jason ValleryBright future for a bunch of scenarios. is we haven't talked on the data analytics and data pipeline case, but that also has clear benefit of a distributed cache if it performs well and can handle the TPS. So there are other cases out there that this will benefit a broad swath of customers. The initial focus was MAI and checkpointing, but I still think it's a good investment if we execute.

[00:40:53.34] Remote : Okay. I should, I should jump, but yeah, thanks. Good talking to you. Um, I, yeah, let me, let me just create a Teams thing with, with all the docs in there and then share it out to a bunch of people. So we're all, you know, talking. from the same set of docs and then anybody can put their docs in there and that's what I'll do. Sounds good. Awesome. Okay. Sounds good. See you. See you at least on October 15th. I'll talk to you next week. I know. Bye.
```

<!-- ai:transcript:end -->
