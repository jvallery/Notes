---
entities:
  people:
  - '[[Tomer Hagay]]'
type: transcript
source_type: unknown
date: '2025-10-29'
---

# 1:1 — Tomer — 2025-10-29

> [!info] Purpose
> Build trust, surface and remove blockers, align on priorities, coach & grow.

## Summary

Jason and Tomer aligned on shifting cloud work toward a PM-led model and the need for cloud-oriented design qualifiers. They discussed current decision flows (via Shahar through Noah/Eyal), constraints of a small PM team, and multi-tenancy limitations affecting cloud timelines. They plan a follow-up to cover pricing and a Salesforce walkthrough.

## Key facts learned

- Current flow: PM prioritizes; architects/engineering drive specs/FRDs; decisions funneled via Noah/Eyal to Shahar.
- Team scale: ~4 PMs supporting ~400 engineers.
- Past attempts at classic PM model were blocked by founder-driven decision changes.
- Cloud is a new serious investment area; opportunity to set proper PM-led model.
- Multi-tenancy gaps: data spaces configured at cluster (not tenant) level; auth/replication inconsistencies mentioned.
- 5.5 plan currently lacks cloud-critical multi-tenancy items.
- Suggested cloud design qualifiers for FRDs (e.g., call home/instrumentation, GUI analytics, multi-tenancy).
- Multi-tenancy today is feature/customer-driven MVPs; not a strategic, end-to-end initiative.
- Customers using multi-tenancy include CoreWeave, Lambda, and Caruso (varying models: admin-only vs self-managed).
- Jason needs face time with Sahar; potential sit-down with Jeff to align ownership and priorities.

## Outcomes

- Alignment that cloud should adopt a PM-led model for definitions, architecture alignment, and release planning.
- Agreement in principle to create a cloud design qualifiers checklist (including multi-tenancy) to attach to FRDs.
- Plan to assess multi-tenancy gaps vs cloud requirements.
- Plan to schedule a Friday session to discuss pricing model and Salesforce usage.

## Decisions

- Schedule a follow-up on Friday to cover pricing and a Salesforce demo.

## Action items (for Tomer)

- [x] Schedule a 1-hour Friday meeting to discuss pricing model and Salesforce demo @Jason Vallery 🔼 ✅ 2025-11-08
- [x] Prepare and deliver Salesforce walkthrough (dashboards, feature/request tracking) @Tomer 🔼 ✅ 2025-11-08
- [x] Draft initial cloud design qualifiers checklist (multi-tenancy, call home/instrumentation, GUI analytics) for inclusion in FRDs @Jason Vallery ⏫ ✅ 2025-11-08
- [x] Compile current multi-tenancy gaps across features (e.g., data spaces per-tenant, auth, replication) to inform backlog @Tomer ⏫ ✅ 2025-11-08
- [x] Review 5.5 plan with Sahar to align and prioritize cloud-critical items @Shachar 🔺 ✅ 2025-11-08
- [x] Arrange face time with Sahar in Tel Aviv to align on PM model and cloud requirements @Jason Vallery ⏫ ✅ 2025-11-08
- [x] Set up a sit-down with Jeff (and potentially Noah/Eyal) to clarify ownership boundaries for cloud vs core @Jason Vallery ⏫ ✅ 2025-11-08

## Follow-ups

- [x] Consolidate multi-tenancy issues raised by Leora and Iki into a succinct findings doc @Jason Vallery 🔼 ✅ 2025-11-08
- [x] Provide a list of customers using multi-tenancy and their models (self-managed vs admin-only) @Tomer 🔽 ✅ 2025-11-08
- [x] Confirm whether multi-tenancy will be mandated as a qualifier for all new features going forward @Tomer 🔼 ✅ 2025-11-08

## Risks

- Founder-driven decision changes may override PM plans.
- Small PM team limits depth across all features.
- Multi-tenancy limitations may block cloud timelines and create customer over‑promising.
- Current 5.5 plan not aligned with cloud requirements.
- Architect/engineering-owned FRDs may perpetuate solution-first bias and friction.

## Open questions

- What exact set of multi-tenancy gaps must be resolved for cloud GA readiness?
- Which core features require redesign to be tenant-aware (e.g., data spaces, auth, replication)?
- What cloud design qualifiers will be mandatory vs optional for FRDs?
- How will authority and ownership be balanced between PM and the architect/engineering groups for cloud work?
- What changes are needed in the 5.5 plan to align with cloud timelines?
- What is the intended cloud pricing model and how will it be operationalized?

> Next meeting (if any): (none)

---

<!-- ai:transcript:start -->

## Transcript (auto)

```text
[00:00:00.05]  Jason ValleryIt's kind of good just making the tour and meeting folks and introducing myself finding out what everybody does. So that's been my morning so far. Lots of interesting folks lots of interesting things I've learned about how process works, how the development lifecycle works. So I was just talking to the XAI team learning how they manage customer success so Very impressive organization you've asked with all of the different dimensions and types of customers, so we're impressed.

[00:00:30.93]   RemoteYeah. Yeah, no, I mean, there's a lot, and I mean, we have customers with such different profiles that, yeah. I mean, you know, from the ex-AIs to, you know, enterprise, highly regulated and whatever, which you need to do a good job there, but, or a better job there, but I mean, the big differences.

[00:00:58.94]  Jason Vallery- I met LaRoz and y'all independently this morning, y'all tried to help and kind of got there. perspective on the planning, phase gates, release management workflow, um, yeah, I came away with it, like how product on this side sits working with those folks and where ownership lies around like definitions and architecture and stuff. I also touched Sahar about that yesterday too. Maybe I'll just ask your take before I give any opinions. What's working well there and what's not working?

[00:01:42.94]   RemoteI think it's kind of the same. What works, what's working well and what's not working well is kind of the same thing. I guess we we're able to to have releases with content that that seem to be right for for where we are for customers to enable deals and and we'll have you right so if uh if if we're talking about, you know, decisions on roadmap and features and all that. So, from one aspect that works well, but it's very chaotic, and it's the bottom, I mean, bottom line always used to come from Shahar, regardless of what we say. Now, he delegated to, not now, but in the last couple of years, he delegated to Noah and Eyal, and so we're working with them on content, and then they go and make the case to Shahar, so I mean, things are more predictable, and we have better. planning and you know regular cadences and we're in sync less surprises but it's not how it should be it's not that bm is really deciding on what's going on um but uh but i'm curious to hear your opinion and i don't know that you were asking about that aspect of product management or engineering collaboration or other aspects?

[00:03:27.80]  Jason ValleryLet me give you my takeaway. So what I've taken from the conversations I've had is that the way it works today is you and your team are at a higher level. What's the requirement coming from the but then it kind of gets handed over to y'all and Noah to drive it through a SaaS team into an architecture, drive it through the dev team to cost it and figure out how it can kind of fit within a given release, and then ultimately, you know, the decision flows around what's in and what's out for a major release, and I just look at that from a, you know, I'm obviously bringing the Microsoft workflow to my knowledge, but, you know, in my mind, that all sits with the PM, and so, you know, this notion that--

[00:04:20.85]   Remote- In my mind as well.

[00:04:22.13]  Jason Vallery- Yeah, this notion that like the architecture and the, you know, detailed specification release planning and all of that sitting with an independent like with a separate group feels like a friction point that can emerge and so just kind of curious like how did we get there and is that a good working relationship and is that right the right way to do it or did we evolve?

[00:04:52.81]   RemoteSo that's what I was referring to where I mentioned that we have an opportunity to drive things differently on your end, right, on the cloud side, because it's a new area of serious investment. I mean, we have invested, but in the cloud, where it wasn't serious. So now that we get serious, let's do it right in the model that you know. and I know from previous companies, and that's the model I came with when I joined VAST. That's the PM organization that I had in mind for VAST as the company grows, and, you know, with that mode that, you know, we're used to, right? you know, that friction is essentially eliminated because the PM organization takes care of that and things are maintained there. As you can probably understand, right, we're four PMs on like 400 engineers. There's no way we can go deep on stuff, right? And... So, how do we, I mean, I can explain further, but when I joined VAST, it was after my predecessor tried to build a PM organization, tried to work in a mode that, you know, that we're used to, right, with product management and the interface. with engineering, again, as common in the industry, that didn't work. You left after a year, right? It was, well, I don't know if I mentioned, but I heard from my direct reports that all the calls, and the company was much smaller then, but all the calls where decisions were being taken and But they were just sitting and watching him, his name is David, he's the VP at Dell right now. But anyway, he was sitting, Shahar and him were just arguing and everyone was sitting aside waiting for that fight to end so they can move on. But that was it, right? And I realized how things are done. there were several situations where I thought we work, I'm talking early on, right? I thought we work as we should, and then things would just flip in the last minute. I mean, you know, decisions like, yeah, you make something, you define it, whatever, you got a different outcome on it, or it's out of the release or whatever, and I figured, to be honest, I made the decision. I made a decision and we had a meeting in New York, Shafar, Renan, Jeff, and myself, and we defined that that's the model we're working in, and there's a lot to do on the field side that we'll focus more on that than when there's product definitions, specific definitions need to be taken, we'll bring in the architect team to the conversation, but we'll stay at the business and prioritization of what's going on in the release. With that, I can tell you that for important items, myself, others in the team really deep on specifics, right, but we can't do that for everything and we don't, we're not the ones who are writing the FRDs, we co-offer them or comment or add user stories to FRDs, because FRDs tend to be really, again, you know, solution-oriented, not problem-oriented. So there's statements there's no um I don't know there's no no no like p.m type of of thinking there so so p.m it's vast right I can't tell you that you know again I'll be honest right that's not what I envisioned myself doing when I joined best and it was a decision either I leave you know like after three months look for something else or stay and do and have a different take on things and that's how we got to where we are today and it actually works way way better than the previous mode where it was just constant because Shafar is very opinionated he would have a meeting with a customer I mean you can have a feature on in in the river release, everything is, you know, phase gates, everything is committed, whatever, right? And release comes in, the feature is not there. Why? Oh, I spoke with John and he said that they'll deploy in a year, so they don't need it now. Oh, but what about the 20 other customers I spoke with in the meantime that you were not aware of, right? We had like, I can give you like tons of concrete examples on where. Things didn't work. I didn't have any way to enforce discipline. Shachar, again, you know, verifinated it. Co-founder, Jeff, really doesn't care, and, you know, he's not in the loop, and, again, there was enough to do across everything. So right now we're really, I mean the main thing we do is focus on the prioritization of the features based on the actual business and the siding that is done mainly by Eyal with the teams there. I'm involved in some of those. customers I'm involved even further with actual definitions and another thing is well I mean there's many things but but we we add an another aspect to all the core features we add an aspect that that you won't find in engineering and also because we're having a lot of customer conversations those more generics rather than one-offs, right? Because again, we have a broader view across customers and use cases and deployment options, things like that.

[00:11:04.61]  Jason VallerySo, certainly don't want to get into any individual's names when I ask this question, so I'll be high level. It's a small... So it's like it's hard to do that when you have such a small team, but like let me preface this with just talking a little bit about my experience at Microsoft with with building out a product management team, and I'll actually even up level that you just say, like Microsoft culture around this. There's kind of two types of product managers, you'll find at Microsoft, you'll find somebody who. came from a very technical, deep background with domain knowledge. Often, what you're talking about is somebody who made the transition from software developer into product, and they have a really solid understanding of how systems come together. I mean, in the storage world, distributed systems, they know the storage world, they know all of that. and then they make a transition in the product manager. So that's kind of like persona A, and then persona B is like, oh, they went to MBA school and they know how to price things and they know customer value propositions and they're good wearing a suit and you can go have a conversation with the customer, right? But when it comes to how am I gonna go architect a solution and how do these things come together and what's the actual workload? and like they're often needing a lot of support from the rest of the team, right? And so you've got these two different types of product managers that end up coexisting in a product management team, and, you know, they each bring their own value, right? Like, you know, one's got MBA background, gonna be able to think about pricing models and they're gonna be thinking about like, you know, value propositions and product marketing and all of those fun things, and then you've got the PM who's like, I can define an S3 over RDMA protocol against the hierarchical namespace. Two different personas. How do you see those two different personas reflected in the product management team at Vast? that within the folks in Tel Aviv that are pseudo product managers like you and how do you see that like evolving and shifting and what do we need there?

[00:13:19.79]   RemoteYeah, so the current the current team I have, they're all the former, right, the first profiling described, they're all people with technical experience, either supporting similar products, implementing, you know, being in the trenches, the IT personnel, and then evolve, you know, work for a vendor, and then we want to have you right. So this is the current team is that right is people that are that are technical and hands on the one of the challenges is that if there's there's different levels of technical right and from from from shoppers perspective and and you know anyone in Tel Aviv almost no one is technical enough and I'll you know you'll you'll find that out right it's very very difficult difficult to hire someone who is technical enough to write an FRD-type document or even a PRD-type document that people will follow and say, "Oh, this is serious. We need to do that." Right? It's impossible, and because what they see as, you know, what needs to come from product management, it's is really not the norm in the industry and I've been in places right it's it's uh in in I mean they what the people Asaf and and his team are more like you know technical product managers but they're really engineering oriented they won't look at again taking five steps back and and trying to solve what others are doing. Sometimes they'll check, sometimes not, and all that. So going from, long answer to your question, but the team today is technical hands-on, but anything they ever wrote it, and that's why I stopped at when I joined, anything they ever wrote, and I can show you some examples from like three years ago or something. Sometimes, I mean, some of it wasn't good because they were forced to cover areas they weren't good at, but a lot was really good content, but it was considered not technical enough, and, you know, and I know, I'm technical, I'm hands-on, I coded, I deployed, you know, whatever so anyway there's this circle of trust and and like really deep technical expertise they're looking for but that is really difficult to to match with kind of a solution and and starting from the problem type approach that that you know you'll be looking at for a PM to do. At least that's my experience and again I mean you can you can have a different take on this and especially when it comes to to cloud again. Cloud is, you know, started from scratch. There is no... Asab is not a cloud expert. He is super expert for everything I'm speaking with him about, but he's not an expert for cloud. He can, you know, he can design, he can tell you what would be a theoretical performance over blah, blah, blah, whatever, if you give him the instance type. But he was... I mean, even on that, he would... was orders of magnitude wrong with the first rollout we had. So anyway, if you have, if you'll have cloud experts, I mean, you're an expert, but more experts in your team that will tell engineering what to do, that could stick in my case, or. For everything else, it's very difficult to impossible.

[00:17:20.09]  Jason ValleryAnd there's going to be a lot of overlap. So, you know, the next topic I wanted to bring up was, you know, I'm going through product learning and understanding constraints and capabilities of the platform, and, you know, one of the key learnings I had today is some of the limitations around multi-tenancy. and just like how many of the features don't work or don't work in a Same way when you start looking at multi-tenancy and so, you know, obviously going to the cloud The key goal is multi-tenancy. Yeah, we can't be successful in the cloud without a multi-tenancy offering Like that is all core product We're going to have to figure out our working relationship in terms of what areas I'm focused on versus what you're focused on, and how that all gets along. We can have some sit-downs with Jeff around this, but what I'm quickly learning is a bunch of the things that I'm going to be asking for to make the cloud successful are corporate. They're not Yancey's team.

[00:18:22.82]   RemoteI'm glad you're here because I told Yossi that he was like, you know, he was optimistic with time with everything and things that he can do whatever, but if Roni won't deliver and if you don't have the, like I said, the multi-tenancy features you need, then, you know, nothing will happen.

[00:18:45.33]  Jason VallerySo, yeah, but I interrupted you. The example that I learned today was, you know, data spaces can't be configured at the tenant level, it's configured at the cluster level, right? So, if you're trying to configure, hey, I'm customer A, and I've got an on-prem environment, I've got a cloud environment, but the cloud environment is an ultimate tenant, like I can't wire that, it's done.

[00:19:04.45]   RemoteYeah, yeah, of course.

[00:19:05.33]  Jason VallerySo, like in- Yeah, we-

[00:19:07.83]   RemoteWe made some design decisions based on the actual customer implementations that we targeted. Yeah, I mean, there's a lot of that, even not just global namespace, but replication as well, right? I mean, we-- yeah, anyway, I don't have to be specific.

[00:19:24.67]  Jason ValleryI learned there were some issues in authentication around this. So I guess, you know, the macro question--

[00:19:31.67]   Remoteis like. Who did you have a conversation about this by the way? Because there's

[00:19:35.93]  Jason Valleryso y'all mentioned something actually I was on a call with Leora and one of the SEEs who brought up a scenario and then I had Iki I was talking to Iki about the authentication one so like I've heard this in three conversations about different feature areas. So clearly there's clear, like maybe over-promised in terms of what our multi-tenancy capabilities are today, you know, in my mind, and so my first area, I think, go ahead.

[00:20:06.83]   Remote- So yeah, no, I think multi-tenancy currently is enough to get by with the- current implementations. We still I mean still there's a lot missing but and that's that's the thing across you know every feature right it's we it's rare that we take care of all the aspects needed for like in in this case real multi-tenancy or real like quality of service that covers everything and and we just we don't have an MVP best cases we had a little bit after that MVP and if that's enough we keep it that way if not you know we stay with the MVP but it's it's it's not that I can sit and that's another difference I don't know how you're used to but to drive those things but it's not - Now that I can sit and plan, you know, like. from zero to a hundred like here's everything we need for multi-tenancy you know start from start from the the north star go back and decide what we're implementing right it it doesn't work like that right we have core weave that needs multi-tenancy so we'll do this and then someone else that needs another thing so that will be the roadmap for multi-tenancy whatever and then if enough people complain we'll increase the scale and whatever right that's that's how things operate so so i wouldn't say there is a to be honest i mean if if i'm looking from the mode that we've been operating there's no issue with multi-tenancy if there were and they were critical enough we wouldn't fix them to get more revenue but we don't right so if you're the cloud business unit coming in and says like I in order to sell you know billion-dollar I need this you know you'll be like core week what I guess

[00:21:59.50]  Jason ValleryI'm getting to is like I see well first I looked at the five five plan and I don't actually see any of these things in So, you know, we've got timelines for the cloud and I don't think that aligns with what the core team is focused on at the moment. I mean, obviously, these are things I need to talk to Sahar about and kind of get reprioritization and thinking about it.

[00:22:23.61]   RemoteYeah.

[00:22:24.61]  Jason ValleryYeah. What I would love to get to...

[00:22:26.61]   RemoteYou need to get a lot of face time with him in Tel Aviv.

[00:22:28.98]  Jason ValleryYeah.

[00:22:30.40]   Remoteas much as you can, yeah, what you'd love to.

[00:22:33.65]  Jason Vallery- Is there a set of design principles that we need to push into, maybe it's a soft, probably a soft, like in terms of, as we move forward, everything that we add to the platform must be multi-tenant aware as a principle. You know, those kinds of... what's the backlog of things that we need to go revisit in terms of technical debt to bring it in compliance?

[00:22:58.72]   Remote- Yeah.

[00:22:59.60]  Jason Vallery- I almost feel like there's some sort of sit down we have to have around this to figure out what the state of the platform is against that set of requirements, and I mean, I'm still learning and so I don't really know what I don't know here. use a little help because I mean you've kind of run into these things and you know it better than yeah - yeah done in any way I missed the last I'm like has anyone really sat down and looked at this this backlog of tech no no and I'll

[00:23:32.77]   RemoteTell you so I mean I think you mentioned two things so first is that that principal or this guy and we're doing that for so we need to have more additional kind of yes/no decisions for I don't know how to call it but qualifiers whatever for for each feature so we do that today I'll give you the simplest example call home right do we need instrumentation to get for a feature right doesn't need to be in call home does it not you know does it do we need GUI analytics do we need this to answer so so does it need to you know so so the cloud has to have a list of things that are you know interesting or critical or nice to have or whatever and then we need to measure those and add every FRD, you know, content in every FRD according to those. If it's a yes, then how? If it's no, then it's not relevant. It's, it's, and we're saying that, so that list, one of the items on that cloud list is multi-tenancy, right? But I, I, I don't think multi-tenancy will get to that level without cloud because multi-tenancy right now is a feature driven by customer demand, not by a strategic initiative. I assume this is

[00:24:55.98]  Jason ValleryMostly a CoreWeave-centric feature, right? Are they the only ones doing multi-tenancy?

[00:24:59.60]   RemoteNo, we have Lambda is having multi-tenancy, for example, Caruso I think is now and just there's there's a there's a good list I can I mean in the various

[00:25:16.78]  Jason ValleryStages I mean I guess generally like it's the new clouds and frankly their requirements look a lot like the clouds right I mean the whole point is

[00:25:23.54]   RemoteMulti-tenancy so yeah yes but there are some other implementations and or other reasons to use multi-tenancy, and, I mean, there's multi-tenancy with self-management, right, so manage the, you know, tenants manage their own tenancy on VaaS, and that's kind of more, you know, closer to cloud models, but there's tenants, multi-tenants for admin usage, and we have, you know, enterprise customers that, let's say, need to have a... different, I don't know, encryption key for a data set or something, right? So they can add another tenant. I mean, there's other ways to do that, but they can have another space, right, for a project, a data set, whatever, they attach it to an EKM, EKM assign a different key to that tenant and things like that, right? So there's other reasons to use multi-tenancy. We have a lot of those, right? but it doesn't need to be, and that's what I'm saying, right? I mean, it's very, it varies a lot, right? You can guess that an admin that manages multiple tenants for those enterprise-related reasons is very different than a tenant logging in to a vast interface and is restricted. By what the admin has assigned to them right and and and all the those set of features, which are way way more advanced So Yeah

[00:26:51.82]  Jason ValleryWell, I Don't know what your schedule looks like I obviously we're at time now. I yeah, I actually have a hard stop I have a couple other topics we should find some time around. I wanna talk about the pricing model conversation one-on-one with you. I'd love to get a demo from you on how you use Salesforce. Like I have no experience with Salesforce, frankly, and so I just love to kind of see how you use it in your workflow, how you're finding like dashboards, how you go and view the features requests coming in or the request for engineering coming in. So those are great questions. Those are kind of two top of mind topics. Maybe I can try to find some time on Friday if you're available.

[00:27:28.02]   Remote- Yeah, I'll go for it. So Friday, we're gonna be a little bit slower, especially, yeah.

[00:27:36.86]  Jason Vallery- Okay, I'll look for another slot, maybe an hour on Friday or something just to talk about those two things.

[00:27:41.14]   Remote- Yeah, sounds good, okay. Actually, I got one. Cool, I'm glad you're diving into those things. Glad you're here, as I mentioned, and yeah, I mean--

[00:27:54.99]  Jason ValleryIt's fine.

[00:27:55.47]   Remote--as you see, I'm an open book, right? I want this to be successful, and can I have--
```

<!-- ai:transcript:end -->
