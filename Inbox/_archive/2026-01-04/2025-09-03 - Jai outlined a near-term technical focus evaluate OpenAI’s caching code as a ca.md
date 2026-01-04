---
entities:
  people:
  - '[[Jai Menon]]'
type: transcript
source_type: unknown
date: '2025-09-03'
---

# 1:1 — Jai Menon — 2025-09-03

> [!info] Purpose
> Build trust, surface and remove blockers, align on priorities, coach & grow.

## Summary

Jai outlined a near-term technical focus: evaluate OpenAI’s caching code as a candidate for MAI’s unified cache, with training-first priority and eventual inference/KB caching support. Target scale is 100k nodes to support 400k GPUs (training) and 40k GPUs (inference) in two years, on AKS+Spark. Jason will confirm IP/access, review the code, assess scalability/integration, and compare against BlobFuse, Alluxio/DAX, and AC Store. Bifrost remains the near-term performance path for Blob (with a direct read path); DeltaZero is positioned as follow-on. Jason will speak with Ong on Friday about the snapshot and MAI needs, reconnect with relevant teams (Nagendra/Krishnan, Lukasz), and establish a regular cadence with Jai. Jai will send OpenAI IP details and MAI pain points docs (and Apollo when ready).

## Key facts learned

- MAI targets: 400k GPUs for training and 40k GPUs for inference within 2 years
- Cache must scale to ~100k nodes and run on AKS + Spark
- Preference: one cache for training and inference (including KB caching), pluggable across frameworks
- Options under evaluation: OpenAI cache IP, Alluxio/DAX, BlobFuse, AC Store (Krishnan’s team)
- OpenAI cache IP may be usable by Microsoft; need legal confirmation (Pete and Sila contacts)
- Bifrost adds a direct read path bypassing FE/table layers; DeltaZero is a potential follow-on
- Lukasz is building parts of Bifrost (direct path)
- Compute for AI moved to Brendan’s org; Kiki (CVP) leading AKS compute for MAI; Yumin interfacing
- Possible MAI requirement: multi-region logical cache pooling (to confirm)
- Jason to discuss snapshot outcome with Ong; may escalate to Manish and Wamshi

## Outcomes

- Agreed initial assignment for Jason: evaluate OpenAI caching approach for MAI
- Plan to verify OpenAI IP access and obtain code for review
- Agreement to prioritize training use cases first while designing for unified cache
- Jai to send OpenAI IP information and MAI pain points document (and Apollo doc when available)
- Plan to establish a regular 1-1 cadence

## Decisions

- Jason will lead the OpenAI cache evaluation and comparison against internal/external options
- Design preference is a single, pluggable cache for training and inference (framework-agnostic)
- Near-term product direction centers on Bifrost plus a distributed cache; DeltaZero positioned as follow-on

## Action items (for Jai Menon)

- [x] Confirm Microsoft’s legal/IP clearance and repository access for OpenAI’s cache code (coordinate with Pete and Sila) and request access @Jason Vallery 🔺 ✅ 2025-10-26
- [x] Review OpenAI cache code and document architecture, training vs inference/KB capabilities, and production readiness @Jason Vallery ⏫ ✅ 2025-10-26
- [x] Assess OpenAI cache scalability to ~100k nodes and fit with AKS + Spark; identify gaps vs MAI requirements @Jason Vallery ⏫ ✅ 2025-10-26
- [x] Meet with Ong to discuss snapshot feedback and MAI constraints; decide on escalation to Manish and Wamshi as needed @Jason Vallery ⏫ ✅ 2025-10-26
- [x] Re-engage with Nagendra/Krishnan teams to get latest on BlobFuse/AC Store proposals and performance data; compare to OpenAI cache @Jason Vallery 🔼 ✅ 2025-10-26
- [x] Confirm with MAI whether multi-region cache pooling is a requirement and capture any additional constraints @Jason Vallery 🔼 ✅ 2025-10-26
- [x] Connect with Lukasz to understand Bifrost direct read path design and implications for cache integration @Jason Vallery 🔼 ✅ 2025-10-26
- [x] Send OpenAI IP agreement details and MAI pain points document; share Apollo doc when available @Jai Menon ⏫ ✅ 2025-10-26
- [x] Set a regular 1-1 cadence with Jai @Jason Vallery 🔽 ✅ 2025-10-26

## Follow-ups

- [x] If IP is cleared, obtain OpenAI code artifacts and set up a review environment @Jason Vallery ⏫ ✅ 2025-10-26
- [x] After Ong discussion, schedule conversations with Manish and Wamshi if needed @Jason Vallery 🔼 ✅ 2025-10-26
- [x] Collect performance numbers and scaling plans from Alluxio/DAX and BlobFuse teams for side-by-side comparison @Jason Vallery 🔼 ✅ 2025-10-26
- [x] Review MAI pain points and Apollo documents to refine cache requirements @Jason Vallery 🔼 ✅ 2025-10-26

## Risks

- Uncertain legal/IP access to OpenAI cache code
- Scalability to 100k nodes and multi-region pooling may be challenging
- Integration fit with AKS + Spark and MAI workflows is unproven
- Fragmentation risk if multiple caches are pursued in parallel
- Maturity of alternative solutions (BlobFuse/AC Store/Alluxio) may not meet MAI timelines
- Potential morale/engagement risk from snapshot outcome if not addressed

## Open questions

- Can Microsoft legally access and use OpenAI’s cache code for Azure services, and what is the scope?
- Is OpenAI’s cache a single unified system or separate implementations for training and inference/KB caching?
- Will the OpenAI cache scale to ~100k nodes and integrate cleanly with AKS + Spark?
- Does MAI require multi-region logical cache pooling, and what are the latency/consistency expectations?
- What is the current maturity and performance of BlobFuse/AC Store and Alluxio/DAX for MAI-scale workloads?
- What frameworks should be prioritized first for cache integration (e.g., PyTorch, NVIDIA stack, OpenAI’s training framework)?
- What were the specific reasons behind the 'meets expectations' snapshot, and what adjustments are expected going forward?

> Next meeting (if any): (none)

---

<!-- ai:transcript:start -->

## Transcript (auto)

```text
[00:00:02.29] Remote : Silence you (silence)

[00:01:52.53] Jason Vallery :  Jason ValleryHey Jay, how you doing?

[00:01:56.21] Remote : Your beard has grown a little.

[00:01:58.37] Jason Vallery :  Jason ValleryA little, yeah. I've been threatened to shave it, actually. I was just telling my wife, like, maybe I should go back to work clean-shaven.

[00:02:04.77] Remote : But I haven't pulled the trigger. How was your sabbatical?

[00:02:11.13] Jason Vallery :  Jason ValleryUh, mixed. You know, it was good to get... the time to sort of decompress with all the opening eye stuff and just kind of take my mind off of all the chaos that was unfolding and step away from all that so I really enjoyed that but it really wasn't the sabbatical I expected. The first weekend my wife had an accident and she damaged her knee. She's had some knee issues for a number of years, and the only solution was a knee replacement. So right as soon as the sabbatical started, she had to have her knee replaced, and it meant I spent most of the summer taking care of her and the girls, and we didn't do damn thing, Jay. I didn't go anywhere. I spent the whole summer at home.

[00:02:52.98] Remote : - Oh, no.

[00:02:53.86] Jason Vallery :  Jason ValleryOkay. - She was stuck in bed for the summer. So, you know, I used it to spend some time. with the girls, my younger girls, and did a lot of learning. I really dug in on just agentic coding and playing around with it. My son's a computer science student at CU Boulder. He's a sophomore there. He and I kind of spent a bunch of time on a side project together for him and, you know, got to play around with Codex. and Claude and Co-Pilot and all that stuff, and it was fun.

[00:03:27.98] Remote : - Oh, that's great. That is awesome. - Yeah. - That's awesome. - Yeah.

[00:03:32.55] Jason Vallery :  Jason ValleryHow about you?

[00:03:33.34] Remote : - That's definitely good.

[00:03:35.25] Jason Vallery :  Jason Vallery- You took a couple of--

[00:03:36.08] Remote : - Well, I just took a couple of weeks off. I just came back from two weeks off. I mean, the only thing we, well. Well, we went to Portland, we had a family event in Portland, so that was one thing that we did. It wasn't exactly a vacation, but I mean, yeah, it's nice meeting family, and it was an event that we went to, so that was good, lots of people there, and then my wife and I. took the Amtrak down to Santa Barbara, because she said, "I've never been on Amtrak, always fly. Can we take the train for a change?" And that was a great experience, actually. Turned out to be a fun thing to do. The views are beautiful going down to Southern California, or going along the ocean for the last hour, hour and a half of the trip to Santa Barbara. Anyway, it was fun, and Santa Barbara was nice, you know, we did a bunch of stuff there. So just got back from that, so that was kind of our vacation.

[00:04:43.85] Jason Vallery :  Jason ValleryWe have an Amtrak to Denver over to Salt Lake, and it's been a number of years, but we've done that as well, kind of go through the mountains, and it's a beautiful kind of thing.

[00:04:52.70] Remote : Sit in the observation deck. Yeah, sit in that, yeah, sit in that lounge car thing with the big windows. Yeah, it's good to do, you know, once in a while. Once in a while, yeah. It's probably been 10 years since I did it, so, but yeah. Yeah, yeah, yeah. I had done one, like, 30 years ago or something. She had never done one. So she really wanted to do something different, so it was kind of fun to do it. But yeah, we won't do it many times.

[00:05:22.17] Jason Vallery :  Jason ValleryYou get there and you're a little stuck. You're like, "Man, I wish I had a car."

[00:05:26.70] Remote : Santa Barbara is okay that way. We just, you know, we found a place right in the middle of downtown and, you know, Stearns Beach is nearby. Yeah. A lot of places to eat nearby. Funk Zone is nearby. I mean, everything is parking distance, and then, yeah, we did take Uber to a bunch of places. We went to Montecito, where Harry and Megan hang out, and she found the address. So we gave the address of Harry and Megan's estate. to the limo, I mean, yeah, to the Uber guy, but I did the Uber limo, Uber XL thing just for fun, and, you know, he probably thought we were, we actually were going there to see that. We get to the front gate and he rings the thing. I'm like, "No, you can actually turn around now. So yeah, so let's talk about a few things. One is I sent you the snapshot yesterday itself. I just wanted to, you know, send it to you. I don't know if you had any questions, but

[00:06:40.60] Jason Vallery :  Jason Valleryum, I think it was, yeah, I mean, if you do, we need to talk.

[00:06:45.13] Remote : to Wamsi, but that's, you know, he was the guy that did it. But yeah, I mean, it's, um, I have

[00:06:50.97] Jason Vallery :  Jason ValleryTime with all on Friday. Um, you know, he scheduled a one-on-one with me. I know he sent me an invite a couple of weeks ago, actually. Um, yeah, I mean, I was shocked, uh, wildly disappointed and out of whack with what I thought reality was. um, and not really the spirit of what I thought was going to happen and where I was at with with Manish at least. I mean, Vanshi and I, you know, Vanshi and I or whatever, but yeah, so I don't know. I'm definitely curious to unpack what happened, but obviously that wasn't

[00:07:25.87] Remote : Your decision, so. Yeah, I mean, I'm happy to be in on the conversation with Wang Xi, or you can have it with Wang Xi, or Wang Xi and Ong? I mean, I assume you did not have this conversation with Ong since you probably didn't know at that point

[00:07:40.70] Jason Vallery :  Jason ValleryWhat the thing was going to be, but... - No, I talked to him this coming Friday. I haven't talked to him. - Okay, so you can bring it up. - Yeah. - I mean, if you're disappointed.

[00:07:52.65] Remote : I mean, from what I see, I don't know exactly, but I mean, it looks like you got a meets expectation thing, and yeah, so.

[00:08:09.69] Jason Vallery :  Jason Vallery- I'll talk to Hong, see how that goes, and then based on that, you know, with your permission,

[00:08:15.31] Remote : Like to speak to Manish, but, you know, we'll go. Yeah, I'm perfectly fine with making sure you get your opportunity to, yeah, speak to whoever you need to. Starting with Wabshi, if you want, Wabshi, Hong, Manish, all the above. Yeah, but yeah, I think both Ong and Manish make sense. I mean, if you feel like there should have been more recognition, then it's certainly worth understanding their point of view as well. Yeah. So, we should definitely do that.

[00:08:55.73] Jason Vallery :  Jason ValleryI mean, we're...

[00:08:56.74] Remote : Yeah, unfortunately, I'm sorry to be so transparent here. but I just, I just didn't, I don't have the background. So, you know, Wamshi did what he did. I did have a discussion with him about, you know, his, how his, this is before I even saw your snapshot. I, you know, I was like three weeks ago, four weeks ago, I did have a short conversation, and he said, "Look, I'm happy to present the snapshot to..." to him if you want and you know I thought about it and I'm like, you know, let me just, I just got back and I'm like, do I really want to, I'm not, you know, Wamshi's not the greatest with respect to scheduling things, I was worried that it wouldn't happen for a while if I asked him to schedule it, go ahead and, you know, do the snapshot. thing with you so I figured I'd just release it to you and then we can have a conversation so.

[00:09:50.73] Jason Vallery :  Jason ValleryYeah I mean with you I want to have the forward-looking conversation and I'll take the yeah retroactive conversation up with I think more arms and bums but you know however that plays out.

[00:10:02.54] Remote : Yeah yeah no I think since you're already you already set up time with him that that sounds. like the right place to have the discussion so yeah you should definitely yeah you should definitely do that and yeah if you care and if you need to i'm totally fine if you're talking

[00:10:21.69] Jason Vallery :  Jason Valleryto me as well no worries so what i do is what my new job is uh you know really a take on where I should be spending my time, you know, it's a, it's a quick.

[00:10:36.04] Remote : Yeah, let's have a dialogue on that. I mean, I feel like we should, you know, I mean, I think it would be good to, you know, figure out, I mean, I know some of your strengths, but I mean, I think in the, in this role on the engineering side, I'd like to see you more. you know, doing a little bit more, you know, not so much about managing relationships with open AI and all that kind of stuff, but more, you know, so an example of something that I thought about yesterday, I mean, I'm just, I'm just coming back to speed myself, but We have this, you know, Manisha's asked me to go figure out, like, what should our caching, AI caching strategy be? And there's a number of people with a number of different opinions on this and obviously there is a lot of views and there's work going on there. There is proposals that are being made by Krishnan and his team around use of a C-Store. There is, you know, potentially, I mean, Alexio is still on the table, Alexio/DAX is still on the table, in the sense that they more recently, in addition to the use of their cash per training they have. added support for inference caching including KB caching so that's a new thing that they did recently so they're a complete solution single same cache you can use it for training you can use it for inferencing KB caching they They have performance data that you can go look at, and the fourth option is OpenAI's IP also, and it appears that we do have access to their IP and that we can use it for any Microsoft service and that includes the cash is my understanding and Pete got that information talking to somebody he gave me the name of the guy he talked to and then also the the uh our lawyer guys uh sila um so You know one thing I did want to explore and maybe this this isn't this isn't a task that I thought maybe a good thing for you to think about or for you to look at is first confirm that yeah we can go look at this code and then number two is to get an understanding that code so that we can formulate an opinion about, you know, love views versus that? What would be the pros and cons? I mean, I have the to-do to actually come up with, you know, run this thing for a while and figure out all the... the options, but I would love for you to dive into the OpenAI piece of this to say, is it something that we could use or not? So that's a thought that I have. I wanted to have the dialogue with you. if that is something that made sense, it would be a good way for you to just get into something like this, and for us to get a sense of your interest in doing something like this, I mean, it would require you to go look at their code. and understand it, maybe talk to some other people or whatever you'd have to do to get a sense of, you know, is this real or did they just kind of cobble something together just for their purpose and we would never, you know, ship anything like that in our service. What their performance is, I mean, I think the Blockfuse guys are sharing performance numbers with me on... you know what what it is that they're seeing today and in particular I mean actually I'll be more specific you know I mean MAI is where we really want to to use this stuff and they're I have been given is that in two years they will have 400,000 GPUs with which is really 100,000 nodes or GPUs per node that's the that's what they'll have and so whatever this thing is needs to scale to 100,000 nodes. So whether it's BlobFuse or whether it's the OpenAI Cache, it needs to scale from a data plane perspective. It needs to scale to 100,000 nodes. So we need to make sure that that works, and number two is they're they're all going to be using Spark and AKS. it's Kubernetes, AKS, they're honed in on AKS and Spark, so how does what OpenAI has, you know, how well would it fit into that environment? I think those would be the two questions. Can does it scale to the extent that we scale? I think answers to that really help us sort out the question at hand. Separately, you know, we'll try to understand what the log fuse guys think they can do. Can they scale to a hundred thousand, can they? you know, how will they integrate into the AKS Spark frameworks, and similarly the AC Store guys, you know, whatever they have. Do we need it? And how would it meet? So I think that would be the first focus, I think, and You know, I don't know whether OpenAI took the same tack as Alexio did, which is, there's only one cache, you know. just plug into an inference framework and it does the KB caching thing. I plug into a training framework, whether it's, you know, PyTorch or whatever, and it does the training thing, you know, and or whether they ended up having two separate cache stories, one for the KB cache thing and one for the thing. I mean, I see some of the discussions with, you know, you, Pete and others leads me to suspect they have two different caches but you know but I you know maybe we can you know explore all that so maybe maybe that that angle you can help me out with I mean that's again like I said I'm I'm it's a dialogue you know we need to figure out a good assignment for you. I want to make sure it's a good assignment. But this is more like a, let's get you started on something, you know, as you come back, and this would certainly be

[00:18:57.26] Jason Vallery :  Jason VallerySomething very useful for us. Yeah, I'm happy to take some initial thoughts. Like what I knew about and maybe this is stale, it's three months ago, was that their training cap was part of the training frame. So it's not a standalone piece of code, it's components within their training, their in-house training, and so I think, you know, the first question we would want to look at is, are we trying to build something that gives... file system like abstraction over top of it and uses FUSE, or are we trying to build something that is a plug-in module or a training framework? And then if the latter, which training frameworks do we need to support? One of the things that I had heard MAI was looking at doing is actually using OpenAI's training framework, and if that's the case, then obviously that's a great fit for an AI, but all of a sudden you turn into a product.

[00:19:57.18] Remote : Yeah, yeah, yeah. You know, to be honest with you, I'll tell you where I'm coming from, right? And I'm trying to just write a requirements doc for this thing before, you know, trying to sort out the various issues. But where I'm coming from... is I mean I like the idea that we have one caching solution rather than you know oh let me do this thing called blob fuse and it'll only work for training and let me do this other thing and well it'll only work for inferencing and then maybe I need a third one for some other use case and so on because I mean we know how how things work at Microsoft, you know, if he can if he can do it once and satisfy, you know everything that that's It's more likely to get done than if we say oh, no I need I need I need two different projects and I need more people and so on and and we have an existence proof that it's possible to do one and and so the way I think about about it is, I think the caching layer needs to be something that can be plugged into different training frameworks and different inferencing frameworks, and shouldn't be really tied to those things, shouldn't be married to those things, right? I mean, but it should be pluggable into those things. That's that way. we can choose which training firm framework to prioritize first and which inferencing framework to prioritize first and if NVIDIA Dynamo is the thing we should do for inferencing or whatever but it shouldn't be yeah it shouldn't be like tied into the framework kind of thing it should it should have a standalone kind of API and you can call it from the framework or you can call it directly from your application or you know how I mean that's the way I'm thinking about it I mean I'm certainly willing to to have a debate on all of these issues but that just that's the way I've been thinking about it yeah and I think that's kind of

[00:22:03.27] Jason Vallery :  Jason Vallerya blog these guys were going down again three months tail but when I was looking they were pushing in terms of an architecture it seemed like it would have that level of abstraction how they got on over the last three months do you have a sense on the maturity of what they've built and they I know a lot of

[00:22:20.34] Remote : These guys the blockies Oh block use guys I think they're making progress I - I feel we're making progress. Have you, I mean, Nagendra sent me a document like late last week, it's like a 50-page document. You may have seen it because maybe you were driving these things.

[00:22:49.58] Jason Vallery :  Jason Vallery- Yeah, I mean, right before I went out, I got a demo from. from those guys and saw where they were that was into May, June. So I don't know what's happened since then. That's kind of what I'm curious about. So yeah, I'll check back in with them.

[00:23:02.83] Remote : Yeah, yeah. But yeah, but specifically, I think if you can go help us evaluate the OpenAI cache, be super helpful. Yeah, but I think, I think before you can look at the code, we just need to make sure that you're, you know, we have the right IP arrangements on that. So maybe you can start with Pete. Yeah, I know Wamshi also. I mean, Banshee's also trying to reach out to some SILA folks on this topic as well. But I'll send you the thing that he'd sent me that says, you know, here's the agreement. He seemed very confident that we can use it. So I'll send you what he sent me, but I think it's still worth it. poking at and he said we can you know he's ready to go ask for access to things because he feels like okay we should have access to things so so that's that I think I'll also send you this MAI I got a I got a 10 page from Ong about the things that MAI is finding frustrating about working with Microsoft infrastructure compared to what they were used to with Corleave, Fast, and other places. 10-page document, I think that's probably useful input. You know, if we say the primary focus, I think, for the whatever cache we build should be to support the training requirements of Microsoft AI, training, checkpointing, find data. kind of requirements. I think the, I think I like the same cache to also support the whole inferencing KB cache stuff as well over time, but it doesn't need to be the first priority. Um, so I think, uh, uh, but what I, yeah, and what I, the input I have from is that I gave you the 400k GPUs. There's also another piece of input that says for inferencing, it's 40k GPUs for inferencing. So 400k for training and 40k for inferencing. That's what they'll need. two years from today and that's what we need to be able to satisfy. So that's kind of our goal.

[00:25:57.61] Jason Vallery :  Jason ValleryWhen I last spoke to MAI, there were a couple of additional constraints. They were talking about that those GPUs would not all be in a single region and that they want to logically combine multiple regions, and so they're not saying what we're asking for is a distributed cache that can over the wind, such that they'll pool storage across multiple regions.

[00:26:19.87] Remote : - Okay, I have not heard that, but that could well be true. Yeah, that could well be true.

[00:26:28.03] Jason Vallery :  Jason Vallery- I have lunch on Friday anyway, so I'm gonna ask him a bunch of questions, but I was under the impression their first cluster would be live now. any success so far? Because they should have, based on the project schedule I was tracking before I went out, they should have their first GPU storage clusters live. Are they doing anything with them and are they having any success with Blob?

[00:26:52.15] Remote : Well, I thought a week ago they announced their first training models for DLLMs.

[00:27:00.49] Jason Vallery :  Jason ValleryThat was from Falcon, like that must have been what they trained on the cool wave cluster. Because they were supposed to start training like September kind of time frame, so I don't think they

[00:27:10.65] Remote : Would have been ready. Yeah, I think you're right. I think they were going to, yeah, I do remember that they were going to start in October and run for three months or something. I mean start in August and run for three months, something like that. Yeah, yeah.

[00:27:23.03] Jason Vallery :  Jason ValleryI'll touch base. Yeah, I'm not sure where things are standing. Yeah, yeah, um,

[00:27:30.96] Remote : so that's, you know, I think, I think taking a look at what opening has got would be super helpful. Um, I mean, yeah, I'm still trying to get you this Apollo dog. but Apollo seems to be, you know, I think the focus of Apollo's stuff is also MAI and that's, in fact, it's from some of that discussion that I got the 400k number and the 40k number, 400k for 400k GPUs for training, 40k for inferencing. So I think this is new as well. I think the compute for AI has moved out of the Arun Krishna organization and is now... in Brendan's org. He's the AKS Kubernetes guy, and that's because this is all bare metal, AKS kind of environment, and, And so there's a person you may know her. I don't know. I don't know her he He K or something like that q you up q I is the first name and ke is the last name Kiki something like that. She's a CVP. She works for Brendan. She's now running this side, the compute AKS and support of MAI, the compute side support of MAI, and so on our side, I mean, Yumin has been interacting with her because they have a relationship from the past. sort of AKS person with AC Store and everything else. So there's some interaction going on there between K'iche'ke and human. So I think all of these come together in the sense that I think in order to support 400K GPUs and that level of scale, first we need a distributed cache that can scale to 100,000 nodes in two years from now, and then I think we need to significantly enhance Blob's latency. and throughput performance numbers. So the current direction is Bifrost, which I think you were aware of before we left, and I've been positioning DeltaZero as the follow-on. That positioning is a work in progress in terms of. you know but but that's kind of the the the thinking but a lot of the at least for the next two years the focus will be by frost and then the distributed cash i think those are the two things we need to support what um what mai wants two years from now, that just seems to be, there may be more things we have to do, but I think those are at least two things we need to do, for sure. So, yeah, so I think--

[00:31:20.24] Jason Vallery :  Jason Vallery- I guess I don't have a full context on what was in scope for Bifrosting. My understanding is it's kind of like taking premium, upgraded Nix, and try to use-- the existing table layer? Is there more to it than that?

[00:31:33.89] Remote : - Yeah, I mean, I think that's a good summary, but in addition, there is a direct path that bypasses the FE and table layers to get to the capacity nodes directly for reads. not for writes, but for reads, there is a path directly that Bifrost allows for.

[00:32:00.10] Jason Vallery :  Jason ValleryFrom the GPU host? Like, the GPU host has awareness of where the bytes are on intelligent routing of some kind?

[00:32:09.50] Remote : Correct. Correct. Yeah. I mean, yeah. Yeah, there's some fetching. of location information, you know, from the table layer but then it's cached and then you can go directly kind of thing. For many of the read requests then you can bypass going through. By the way, I've got a guy on my team that is effectively part of, you know, the Bifrost team. So we can, you can, I can connect you to him. Lukasz, you know Lukasz.

[00:32:46.82] Jason Vallery :  Jason Vallery- Yeah, yeah, I know.

[00:32:48.33] Remote : - So Lukasz is actually building some of the Bifrost code, and in particular, he's building this direct path, you know, from the compute layer.

[00:32:59.00] Jason Vallery :  Jason VallerySo feel free to talk to him. and we had looked at the Enlightenment API and other things, so is that kind of what he's working on?

[00:33:07.64] Remote : Say that again, we had a point.

[00:33:10.82] Jason Vallery :  Jason ValleryRedirects and/or an Enlightenment API.

[00:33:13.64] Remote : Yeah, this is unrelated to that project. Yeah, that was a project we kind of had to, we didn't quite, we didn't quite do that. This is... yeah maybe it's a variant of that but that project we kind of but that's the same guy you're thinking of the right guy that's the guy um but yeah he's now building Bifrost code as well some some some parts of it he's working with Vishwajith on Jagan's team and so they're they're pairing up on they're doing there. Anyway, those are some initial thoughts, you know, for you to go poke at, but I'm also open, like, you know, as you explore and, you know, feel free to talk to Ong and others and, you know, if other good ideas pop up on things that you should be focusing on, I'm... I'm open, but I wanted to at least think about one very specific thing where I know I would find it useful, so, and, you know, it's a good kind of get-your-feet-wet exercise of, you know, get into the code and do some digging and, you know, give us some thoughts on what you think about it.

[00:34:30.66] Jason Vallery :  Jason ValleryI think that's yeah yeah no I mean it's certainly interesting I'm happy to kind of take that as a

[00:34:39.43] Remote : First set of tasks and see where it goes yeah and we can go we can see we can see where it goes I'm sure you know as we as we interact more there'll be more things I'll just figure out to throw at you but you know I think yeah it'll be depending on you know how these these things go I'm sure there's plenty for you to do but those are some thoughts for now.

[00:35:09.65] Jason Vallery :  Jason ValleryWell look I'm excited I mean I have a lot of you know time to think. over the last three months around where I was going and what I was doing and you know this is an exciting path. I just hope that you know I can overcome any of the historical challenges that have been present and build good working relationships with all the folks we're going to have to work with but you know I'm here and I'm excited to take this forward.

[00:35:38.18] Remote : I'm super excited. I think this is a, I mean, I think your background, you have a lot of knowledge in this space. I mean, I think everything that we have learned from OpenAI, I don't, you know, is all going to be totally 100% useful for what MAI needs, and that was a great training ground as I'm concerned for any other customer in this space and you know more about it than anybody else so yeah it should be it should be exciting and new stuff is happening every day in this area it's just kind of crazy NVIDIA comes out with new initiatives or some SCADA initiative they came out with and then they wanted they've Gone and told all the SSD vendors. I need a hundred million IOPS from you guys You know for SSD and this is a I mean every day. There's like some new shit happening All the the agentic stuff, which I'm glad to hear that you were mucking around in that space Not had time to muck around in that space, but you know, what does that mean for somebody? I mean, there's stuff there that would be super interesting to go explore.

[00:36:52.00] Jason Vallery :  Jason ValleryBut, I wish codecs, I was available at the beginning of my sabbatical it came out. Well, the VS code integration for codec CLI came out a week and a half ago, and it is just leaps and bounds above what clod. a pilot agent can do. It is just an amazing experience to give it a structured set of tasks, put it on full auto, walk away and come back, and it's done everything. It's done testing, it's validated it, it's deployed it. It's crazy. It's crazy.

[00:37:23.83] Remote : - I'm gonna have you, I'm gonna need you to walk me through some of this stuff one of these days. I'm jealous. But I just haven't had the time to do this Anyway, hey, I do have a 235 that I was supposed to go join but welcome back, and yeah, we can

[00:37:42.33] Jason Vallery :  Jason ValleryKeep going here you go, and I mean, let's Get a regular rhythm going and you know, yeah, let's get a regular rhythm going. Yeah can get this project. Okay Jay well. Okay and I'll keep sending stuff your way and

[00:37:59.04] Remote : You know we'll we'll feel our way through the initial week or two so. Okay. But you know feel free to at any time when you you know if you see something exciting that you think might be something you want to spend more time on It can also be accommodating, okay?

[00:38:19.51] Jason Vallery :  Jason Vallery- As I planned.

[00:38:20.34] Remote : - All right. Hey, welcome back.

[00:38:21.99] Jason Vallery :  Jason ValleryAwesome.

[00:38:22.83] Remote : - Thanks. - Thanks a lot. Yeah, take care. Goodbye. you You
```

<!-- ai:transcript:end -->
