---
entities:
  people:
  - '[[Eyal Traitel]]'
type: transcript
source_type: unknown
date: '2025-10-29'
---

# 1:1 — Eyal — 2025-10-29

> [!info] Purpose
> Build trust, surface and remove blockers, align on priorities, coach & grow.

## Summary

Jason and Eyal discussed VAST’s release intake, planning, and execution model, including how majors, minors, service packs, and hotfixes are managed and tested. They aligned on the challenge of moving toward SaaS agility, with key multi-tenancy gaps on the cluster side (notably authentication providers) blocking progress. Eyal will send the multi-tenancy gap list, and they plan to meet during Jason’s Tel Aviv visit and schedule another call.

## Key facts learned

- Eyal joined VAST in Dec 2024; Noa is a veteran (around employee 19).
- Noa manages major releases; Eyal plans minor releases.
- Intake sources: leadership (e.g., S3 RDMA), architects (Asaf, Sagi), and SE requests via Salesforce tied to opportunities.
- Field requests triage: Tomer Haggai’s team, with Jonathan Hayes assigned; bi‑weekly reviews of top requests.
- Phase-gate and release ops led by Shelly Martin and Liraz (R&D).
- Urgent customer asks (e.g., Tesla) frequently reallocate teams and shift scope.
- Release managers (separate roles) run day-to-day for majors and minors; Eyal collaborates on minors.
- Service packs and hotfixes: driven by vForce (Roy Sterman) and Dafna’s team; ensure backport/forward-port of fixes.
- Minors are treated as full releases with extensive regression and performance testing; weekly content/testing reviews.
- Not yet full SaaS; Polaris/Icelandic team owns control plane; significant cluster multi-tenancy gaps remain.
- Key gap: auth providers limited to 8 and configured at cluster level, not tenant; large effort to scale/tenantize.
- 5.6 targeted to GA in July next year; 5.4 released, 5.5 upcoming; cadence roughly ~2–2.5 majors/year recently.
- Jason’s goals: bring VAST to cloud/SaaS with strong durability, security, availability; improve agility vs traditional slow storage upgrades.
- Jason will be in Tel Aviv 2025-11-23 to 2025-11-26.

## Outcomes

- Shared understanding of current release intake, planning, and testing processes.
- Alignment that minors act as full releases with rigorous regression and performance testing.
- Agreement for Eyal to send the multi-tenancy gap Confluence page.
- Plan to schedule another call and meet in person during Jason’s Tel Aviv visit.

## Decisions

- (none)

## Action items (for Eyal)

- [x] Send Confluence page with the current multi-tenancy gaps list @Eyal Traitel ⏫ ✅ 2025-11-08
- [x] Schedule a follow-up call to continue SaaS and release process discussion @Jason Vallery 🔼 ✅ 2025-11-08
- [x] Coordinate an in-person meeting during Tel Aviv visit (2025-11-23 to 2025-11-26) @Jason Vallery 🔼 ✅ 2025-11-08

## Follow-ups

- [x] Review the multi-tenancy gaps list and identify priorities for cloud/SaaS readiness @Jason Vallery 🔼 ✅ 2025-11-08
- [x] Sync with Polaris/Icelandic team on which gaps can be addressed in control plane vs cluster @Jason Vallery 🔼 ✅ 2025-11-08
- [x] Confirm backport/forward-port plan when delivering features to customers on hotfix builds @Eyal Traitel 🔽 ✅ 2025-11-08

## Risks

- Continuous urgent field requests disrupt planned work and timelines.
- Auth provider limit (max 8, cluster-configured) blocks scalable multi-tenancy and SaaS readiness.
- Multiple parallel release streams strain teams and tooling.
- Hotfixes undergo less regression, increasing quality risk if not carefully managed.
- Long lead times for major releases reduce ability to deliver large features quickly.

## Open questions

- What is the complete prioritized list of multi-tenancy and full SaaS gaps, and estimated effort for each?
- How can VAST accelerate delivery of large multi-tenancy changes (e.g., auth providers) ahead of the next major?
- Who will own defining and driving the agile/SaaS release model for the cluster side, and what are the stage gates?
- What criteria determine when a customer need becomes a hotfix vs inclusion in the next minor release?
- What is the target forward cadence for majors and minors as VAST moves toward SaaS?

> Next meeting (if any): (none)

---

<!-- ai:transcript:start -->

## Transcript (auto)

```text
[00:00:00.04]  Jason Vallery>> Hi, Jason. Nice to meet you. >> Nice to meet you. I've heard a lot about you. Finally, a face to the name everyone talks about.

[00:00:22.85]   RemoteThat's good, but be always careful because we are seven Eyals in Vast.

[00:00:27.78]  Jason ValleryEverybody says Eyal Traitel, so I'm assuming it's you. Yeah, that's me. That's you.

[00:00:33.60]   RemoteThat's me. My family name also is very unique in the world, so I'm probably the only Eyal Traitel. So, nice to meet you. No, I could not make it, so... We'll get to meet her at another time.

[00:00:49.29]  Jason ValleryYeah.

[00:00:49.69]   RemoteI'll introduce a little bit what both me and her are doing in Vaast, and she realized, actually, I sent you slides about Vaast on cloud, which don't answer the questions that you were asking on release process and so on. So I'll-- We don't have good slides on that. I'll describe to you how how the magic of releasing

[00:01:12.23]  Jason VallerySoftware in vast works. Yeah, I'll just a little bit. I think that's what before we go to burn I did meet also with the or not the or um the roz, uh, and she kind of walked me through some of it I'm getting more context as I go. But yeah, okay. Okay, cool. Okay

[00:01:26.71]   RemoteSo I joined in december 24. So almost a year in VAST. Noah is a veteran of VAST. I think she's employee 19 or something like that, and both of us are in the release planning side of things. We are now still working. She came back from a long vacation. So I planned the releases most of the time that I'm here. Now that she's back, she's back to managing major releases and I'm probably gonna continue to plan minor releases. A little bit background on how it's working in Vaast. So first of all, quests of what to develop come in through different routes. Leadership is one route, one route like that. For example, there are discussions and different people have discussions with NVIDIA, for example, and we want to go for S3 RDMA. get this from the top, okay, we have to do S3 RDMA in the next major release. So some big items, they come in directly. Directly could be from Shachar. It could be also, in some cases, from architects. We have a team of architects. They talk a lot with customers, and yeah, it's Asaf and his team, it's Sagi. So we know type of thing that we need to do these things, so they come in directly. Some come directly from the cities, however, we do have a process now, more organized. process where we push back SEs to file requests in Salesforce. They did that in the past, but there is a revived process, and they file in a request, they have to tie it to opportunity. That gets to Tomer Haggai's team, and as of last few weeks, we're doing it in a more organized way. He assigned Jonathan Hayes from his team to go through these. We have bi-weekly meetings to review the top ones that come out of this process to make sure that we follow up on them. Some of these, they came directly to us already through the... means. You know, SCs know, both Noah and myself, they would approach us. It either comes from architects. So, all of this together end up to be, I would say, a candidate list for releases, and then we do the planning side, to scope, okay, how much work it is, a lot of the features here tie to different development teams. For example, if you want to develop something that has user, I mean, most features have something to do with the GUI, so you have to have, let's say it's a database feature, so you need the database. team, and you need the GUI team, and you need the backend API team, and you have to make sure they provide us effort estimations. We calculate whether it's in the-- I mean, we plan major releases, and we have urgent requests, and how does it impact?

[00:05:16.46]  Jason ValleryThe major features and you know all of this mess. So let me ask a clarifying question about that. So if I hear this right, Tomer and his team are primarily interfacing with the field and the customers. They're triaging incoming requirements, requests, deal blockers, so forth. So I'm handing off to you and Noah the statement of what the requirement looks like, and then you're working with the architects, the devs, to define how it will be built, define how it fits into the release cadence, really build that next level of clarity. Are you responsible, then, for going ahead and making sure that all of that is clear? all the different component teams and costing it and kind of coming up with a full analysis of how much work this is and then pushing that through stage gates that the Ross manages like the phased stage gates. Is that kind of you bring that to that forum or so?

[00:06:19.75]   RemoteSo there's, there's a. So, in general, yes, things don't always align time wise, meaning by the time we start phase gate one, for example, for 5.6, some of the features will already be in motion, because we are planning it beforehand. planning in VaST is very challenging because it's very dynamic. There's a lot of moving parts, changing parts, not moving parts, but changing parts. For example, you have surprises almost every other day, where, for example, we have an ongoing relationship with Tesla, and we gave them a bill to try some things, and then they say, "Okay, we like it. Oh, but..." but we also need this, we also need that, we also need this and we also need that, and some of these things are three weeks, three main weeks to develop plus some QA time. So there are, you know, considerable amount of work and those teams that get to develop these urgent things. well, we took them out from something else, right? So it's changing on a constant basis. It's very, very challenging. So by the time you get to the phase gates, some things were, you know, what happens in between, there's a lot of things happening in between, but there is a process behind it driven by ops teams. team, Shelly Martin and Liraz from R&D, they are the main ones driving this whole process to make it into something more organized where we documented what have we committed to in the release. But we end up developing, if you look at what was committed in the Basegate 1 versus the final content, you know, it's a Venn diagram. Some things got deferred, some, I mean, will get deferred in the release, and there's many things that will end up being developed that were not thought of before because they were requested during the release. Right now we are deflecting. I mean, we started earlier this year, we started the minor releases process to cover In a faster way, the more immediate requests. But there's constant Blood of such requests that are, you know, everything is as soon as possible. So it is challenging to meet that.

[00:09:10.24]  Jason ValleryHow do, like, hotfixes, security patches, those sorts of things get into the process and released?

[00:09:22.66]   RemoteSo first of all, for each major release, we have a release manager. That's not me and Noah, they're other roles that manage the ongoing work with the dev and QA teams. For the minor releases, there is another release manager. I'm working with on the minor releases, and he's keeping track of minor releases, and mostly big hotfixes that in some cases we have to close some gaps or a deal or an install, and it doesn't align well with the timing we have for the minor releases. Even they are not quick enough. So we deviate to large hotfixes that do have features. They're not really hotfixes. They don't fix anything. It's just we deviate this work to be split from the regular cycle. For service packs and hotfixes, this activity driven mostly by basically two teams, Vforce, which I assume you've heard about. So Roy Sterman and his team are, they're basically the front R&D arm in front of CS and customers, and they would, issue the urgent fixes, and in some cases, they will initiate the need to backport something from future release to some customers, and they will request hotfixes, and they work with another person, which I don't know if you've met, Dafna. Daphna is also reporting to Shachar, same as Roy Sturman, myself, and Noa, and Daphna and her team are managing, you know, this entire activity of fixed builds, fixes, and not builds, but more fixes and service packs. work with Royster and they would combine specific fixes to a service pack and she is a person that makes sure that he's responsible for issuing hot fixes and also making sure they also go one day upstream to later regular bills. like minor releases and so on. So there's an activity, there's an entire activity around, you know, service specs and hotfixes, and this is mostly not related to myself and Noah, because this is all driven by vForce and Daphne's team. They manage these things. But in some cases we do, first of all, we sit together. We're very close to each other and we collaborate in some cases. For example, we need to develop a feature for a customer. That customer is already running a hotfix. We develop it in a minor, but they can't directly upgrade to that minor. We have to make sure that all of their existing fixes, which were provided on a side hotfix, are going upstream to that same miner so they could upgrade. Otherwise they will lose fixes. So we are, you know, there's an entire management around that area.

[00:12:55.50]  Jason Vallery- How do you make sure customers... - The QA cycle against that and your integration testing and all of that was that those get back ported or forward ported.

[00:13:07.73]   RemoteIt's a complex arrangement. There's a lot of automated testing in VAST. There are regression tests. So service specs and outfixes, I believe, are going through less regressions because they are mostly about fixes that were already done in other releases. Not always, but-- in many cases. Minor releases, they are really really regular releases. They go through a lot of a lot of testing and a lot of regression tests. So once a branch is opened for a minor release, it starts to get regression tests, and this we have a weekly meeting with all of the parties to review the content and the current state of testing. performance testing also, so they go through a lot of scrutiny. That's the big change. Before the time I joined, in cases where we had, like, urgent requests from the field, they would develop them. They did develop them in the past as well. But they did that. some hotfix and they've not tested enough, and that was the big change with minor releases, that we will treat them as full releases. They have to go through a lot of regression tests. You know, there are test plans, there are test plan reviews. It's like mini-me of the big releases.

[00:14:37.75]  Jason Valleryin a way. I don't know what you know about me and what my goals are so maybe I'll just take a minute and kind of share that and where I see us going. So I just joined last week reporting to Jeff as owning cloud product management and I came from Microsoft most recently. I ran product management for Azure Blob Storage, Microsoft's object storage platform, and I was on that team for 13 years. So, kind of took it from nothing to hundreds of exabytes, kind of a wild ride, and I'm really excited about, you know, the set of capabilities that AST brings because I think it'll enable us to unlock multi-cloud, hybrid, on-prem burst. burst from cloud, a repatriation, all of those scenarios with the Neo clouds like data spaces and just data movement are a key strength here. One of the goals that Jeff has given me is really, how do we get to the point where we're effectively on the cloud? And that's a very different operating model, and that's a very different release management model and just will require a rethink of a lot of these processes you just described. I'd just be curious your take on, what's it going to look like to try to get to a world where we're much more agile, we're able to deploy into a multi-tenanted environment, all of that infrastructure in the cloud. It's a lot. What's your take?

[00:16:13.73]   RemoteSo, first of all, I'm involved in the planning and discussions we have with the Polaris team, the Icelandic team, and also the other teams on the cluster side that work on Vaston Cloud. We didn't even get to the... the point of thinking about the word "agile" yet. I mean, right now we're focused on the initial milestones where this is not all SaaS, as we call it, not yet. This is still the same Vaston Cloud or not the same one, but maybe a more organized, I called it internally. tickets vast on cloud 2.0. It's like a more organized than the initial wave, but it's still not full SaaS. There's no nightly builds or anything like that. I think the agility is more on the Polaris, the console side, the cloud part of the software, the part that the Icelandic team is developing. is more of cloud-native application. The cluster side, we are still struggling with gaps we have on the cluster code side. We call it multi-tenancy gaps, or additional gaps that relate to things full SaaS. So we're not even thinking yet on what you mentioned, on how do we, how do we issue cloud, sorry, cluster side changes much quicker. But it's definitely good because I am, I mean, we have discussions between myself and Noah and Shachar. and the team here, the R&D team on how to make things better. The minor releases killed us, and they're very challenging because you take very complex release machine here and you ask it to release more frequently, and in some cases in parallel, oh, well, in actually in all cases. it is in parallel with other releases, so we have a lot of these streams running in parallel, and now you're going to ask it, "Hey, I want to have a build every night that's working in production." That's a very different mentality. So I think this will require, this will be a challenge. definitely on the cluster side of the code. We'll have to see, I think we will have to start thinking about it. I mean we're I think eventually that that layer of the stack. The most important part. you want it to be 100% reliable, right? Availability, utmost availability, and you will not need new functionality on a daily basis, I think.

[00:19:20.29]  Jason Vallery- Not on a daily basis, but you want to be able to be responsive. - Yeah. - What I think about what RP0 was in Azure Storage, it's a durability. security and availability being the three core tenets that are just infallible so you know there's a lot to go and do there when you're doing upgrades you got to make sure you're not out you know destroying customers data

[00:19:42.83]   Remoteof course of course but in the like in this if you if you will compare the It's not equivalent, I'm sure, to Azure Blob, but if you think of the cluster side of the stack that we have invested on cloud in full SaaS when we get there, how quickly did you have to make code changes or develop something new on the storage layer side of Azure Blob?

[00:20:15.40]  Jason VallerySo what I would just say is on our side, not our side, I'm on Vas's side now. On Microsoft's deployment release schedule, a new storage build goes out once every six months. But that's the reality. It's very slow moving. It's very painful. I think our opportunity is to do better than that. But when you're talking about upgrading hundreds of ex-- bytes of storage clusters. It's very intentional, very slow, very methodical, just because of the risks associated with it, and when I think about, like, we're committed with SaaS, you know, Yancey's team is going to do a lot on the control plane, certainly important to get us into the marketplace, but I think, you know, many of the things we need to build here at Avast to make this successful are in the core, you know, cluster. more cost-effective on the cloud, more performing on the cloud, to bring new capabilities. One of the things I think I just learned is that data spaces doesn't work multi-tenant. You can't pair two clusters together in a multi-tenant way. Those sorts of capabilities are going to be critical, so there's a bunch that I'm already starting to uncover. We're going to have to push through into the core platform. to get to the state we want to be. Offload to object is key, those sorts of things. So, yeah, we'll be working together quite a bit on all of that.

[00:21:33.59]   Remote- Yeah, I mean, today we have an entire list of multi-tenancy gaps that we have. A lot of the gaps are shared with what full SaaS. requires. It's almost the same list. In some cases, some things may not be required or could be argued as not required for full SAS because the control plane can manage some things that we don't have on the cluster side. We have to sync with the Polaris team on these items. The list is required both for on-prem, multi-tenancy, already today coming from customer requests and so on, and we just, you know, we are overbooked by design here. So we can't develop all of these gaps together. So we do have-

[00:22:24.97]  Jason Vallery- I'd love to see the gap list. If you've got it right up-

[00:22:28.82]   Remote- I can send you the conference page. that I start to gather. I don't want to commit that this is the ultimate list. We do have more gaps than this, but it will give you some good idea. Probably one of the bigger ones in terms of effort estimation is providers. Today, we only support up to eight, and you cannot configure-- this is authentication providers like Active Directory, you cannot configure them from the tenant side. So you configure them from the hosting cluster side and allocate them to tenants, which is arguably something that you can potentially live on. The control plane could you know, receive the settings and set them up for you from the cluster side. I'm pretty sure if Ike was here, he wouldn't be, he wouldn't want to do it that way. But we only support up to eight. So in the first place, that limits you to have a, you know, full SaaS. But the ratio is eight customers on a cluster. faster. That's not good. Yeah, but it doesn't scale. Yeah. Yeah, and both both scaling it up and making it tenant tenant based are very large tasks. So we could not accommodate them in the coming in the coming major. So it's a today it's a challenge to meet these things, and when, you know, NOAA is kind of wrapping up on 5.6 release, this is a release that will GAA in July next year. So you see the challenge. If you come now and say, "Hey, I need this and that." And if it's not a small thing that we can somehow shove in the plans for minor releases, you're already looking at the... next major after. So we are, we need to accelerate it in some way and Shachar already is thinking about it and yeah we are discussing different ways to to accommodate at least some of these

[00:24:37.74]  Jason ValleryGaps in a faster way. Is your experience, I ask LaRosna, but I'll ask your take, is it roughly you're making a major release historically? So there were complaints by

[00:24:50.09]   RemoteVeterans here when I looked at it and calculated it as the newcomer maybe it was two three months ago in two in the last two years we did release six releases so you have basically more or less three majors a year.

[00:25:11.28]  Jason ValleryWhat's criteria two years that were good?

[00:25:15.03]   RemoteYeah, that were around six releases. If you look at it, I'm I joined in December, I'll have to drop another call. But I joined December. Last year, we released five, three just released 5.4 and we will release 5.5 uh a little bit beyond my annual well yeah a few months after we will release the third release so it's like two and a maybe two and a half per year

[00:25:47.50]  Jason ValleryMakes sense so um i'll let you go to the other call lots more questions and I'll be in Tel Aviv 23rd through 26th of November, so I'm sure we'll get a chance to meet in person.

[00:25:57.21]   RemoteOkay, cool. Yeah, you'll get to see me. Awesome, and then feel free to schedule another call, and I'll send you the conference page for multi-tenancy. Yeah.

[00:26:05.85]  Jason ValleryAppreciate that. Thanks for your time. Great meeting you.

[00:26:07.61]   RemoteOkay, cool. Bye. Bye. Cheers.
```

<!-- ai:transcript:end -->
