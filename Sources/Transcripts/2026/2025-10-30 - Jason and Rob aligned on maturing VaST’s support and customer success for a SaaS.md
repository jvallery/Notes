---
entities:
  people:
  - '[[Rob Banga]]'
type: transcript
source_type: unknown
date: '2025-10-30'
---

# 1:1 — Rob Banga — 2025-10-30

> [!info] Purpose
> Build trust, surface and remove blockers, align on priorities, coach & grow.

## Summary

Jason and Rob aligned on maturing VaST’s support and customer success for a SaaS/cloud model. They discussed building a proactive TAM/CSM function, defining premium support tiers with SLAs/SLOs and billing, establishing data sovereignty/government-cleared support capabilities, instituting metrics-driven operations, and documenting the end-to-end customer lifecycle. Jason will leverage Azure experience to propose models and share candidate referrals; Rob will push org/process changes and charging for dedicated resources. They plan to connect in person around Supercomputing in St. Louis.

## Key facts learned

- Jason spent 13 years on Azure Storage and led product management for Microsoft’s object storage platform.
- Rob has been at VaST ~3 years; customer org grew from ~20 to ~130 and added a NOC (2 per shift).
- Goal: evolve to an ERA SaaS platform for storage with VaST owning end-to-end operations.
- Current model lacks cloud-caliber incident management; no developer on-call rotations.
- CSMs are mainly reactive (tickets, weekly calls, incidents) with limited proactive adoption/roadmap work.
- No formal premium support tiers; dedicated support has been delivered ad hoc without charge.
- Time tracking/billing and SKUs for premium services do not exist yet.
- Significant opportunity and requirements for government/sovereign customers (clearances, in-region staff).
- Data sovereignty/access controls and cleared coverage are not yet in place.
- Preference to staff SREs with strong VaST DNA and train cloud specifics; CSMs should blend soft skills with deep technical ability.
- Jason reports to JF; possible in-person sync at Supercomputing in St. Louis.

## Outcomes

- Agreed to draft a job description for a proactive TAM/CSM-like role.
- Aligned on defining premium support/services tiers with clear SLAs/SLOs and charging for dedicated coverage.
- Agreed to build a customer lifecycle flowchart and clarify roles/hand-offs across stages.
- Jason to review LinkedIn and send candidate recommendations for CSM/SRE profiles.
- Consensus to institute metrics reviews and data-driven operations.
- Recognized need to plan for developer on-call and cloud-grade incident management.

## Decisions

- Recruit SREs with strong VaST product knowledge and train cloud nuances rather than hiring cloud-only outsiders.
- Shift CSM scope to include proactive engagement; create a paid, premium services model for customers that require it.

## Action items (for Rob Banga)

- [x] Draft job description for a proactive TAM/CSM role (hands-on, customer-facing, proactive adoption/roadmap). @Rob Banga ⏫ ✅ 2025-11-08
- [x] Send candidate referrals (CSM/SRE profiles) after reviewing LinkedIn. @Jason Vallery 🔼 ✅ 2025-11-08
- [x] Document the end-to-end customer lifecycle and ownership flow (pre-sales to expansion) and review with Rob. @Jason Vallery ⏫ ✅ 2025-11-08
- [x] Propose tiered premium support/services model with defined SLAs/SLOs and staffing assumptions. @Jason Vallery ⏫ ✅ 2025-11-08
- [x] Stand up time tracking and billing processes and define SKUs/pricing for premium services. @Rob Banga ⏫ ✅ 2025-11-08
- [x] Assess data sovereignty and government-cleared support gaps; propose a plan for in-region, cleared coverage. @Rob Banga ⏫ ✅ 2025-11-08
- [x] Establish weekly metrics reviews and dashboards for support/NOC/CSM (SLOs, MTTR, backlog, adoption). @Rob Banga 🔼 ✅ 2025-11-08
- [x] Define developer on-call rotation and cloud-grade incident management process. @Jason Vallery 🔼 ✅ 2025-11-08
- [x] Identify internal VaST engineers suitable for SRE rotations and plan training for cloud specifics. @Rob Banga 🔼 ✅ 2025-11-08
- [x] Schedule an in-person sync around Supercomputing in St. Louis. @Jason Vallery 🔼 ✅ 2025-11-08

## Follow-ups

- [x] Share any existing documentation on current engagement/lifecycle to inform the flowchart. @Rob Banga 🔼 ✅ 2025-11-08
- [x] Confirm whether Jason should attend AOP or other November meetings. @Jason Vallery 🔽 ✅ 2025-11-08
- [x] Confirm customer requests for dedicated resources and initiate chargeable engagements. @Rob Banga ⏫ ✅ 2025-11-08
- [x] Coordinate time and location for the St. Louis in-person meeting. @Jason Vallery 🔼 ✅ 2025-11-08

## Risks

- Operating without data sovereignty controls and cleared personnel for government work creates compliance and delivery risk.
- Continuing ad hoc, non-billed dedicated support strains budgets and is unsustainable.
- Lack of product and program management increases coordination gaps and slows maturity.
- No developer on-call or cloud-grade incident process increases MTTR and customer impact.
- Absence of clear lifecycle ownership leads to reactive firefighting and inconsistent customer experience.

## Open questions

- What precise SLAs/SLOs and response times will differentiate each premium tier?
- Which systems will support time tracking, billing, and SKU management for services?
- How will ownership split between SEs, CSMs, and the proactive TAM role across the lifecycle?
- What compliance and access-control changes are required for data sovereignty and cleared operations?
- Which customer segments (e.g., federal, Singapore, EU) should be prioritized for sovereign offerings?
- What meetings and governance forums should Jason participate in during ramp-up?

> Next meeting (if any): (none)

---

<!-- ai:transcript:start -->

## Transcript (auto)

```text
[00:00:00.00]   Remote(keyboard clicking)BLANK (mouse clicking) You you you youBLANK you Hello. Ah, hello sir. Sorry, I am tardy. I had to get some breakfast. No worries at all. How's it going?

[00:04:58.58]  Jason ValleryHow's things?

[00:04:59.58]   RemoteWelcome to the company. Yeah. I'm on week two. Fun times.

[00:05:03.58]  Jason ValleryHow about you, Alex? How's it going?

[00:05:05.63]   RemoteI'm good, thanks. How are you?

[00:05:07.58]  Jason ValleryI'm good, thanks. How long have you been here?

[00:05:29.16]   RemoteThree years, a little over three years.

[00:05:31.10]  Jason ValleryOh, okay. I just linked in and stopped to see your background, but maybe we could do a little bit more formal intro. What do you do here? What do you do here? What's the scoop? Where do you come from?

[00:05:41.84]   RemoteMy job is to make happy customers. Yeah. So, we do that through support, PS. account management, CSMs, TAMs, we have tools and automation team and some program managers, and now we have something called the NOC. So we have two people per shift and they are watching all the alerts and responding to things quickly and responding to slacks. So we have all the people over three years, we've gone from 20 to 130. We'll end up this year probably like 140, 150, and we're building towards 1,000 customer scale. When I got here, we were 100 customers, so like great 10X, 1,000 customers, and I told Brandon, probably 10X the people-ish, right? So 180, 200 people. So we're generally on track there. I think... I think as we were talking about the cloud stuff today, I'm like, oh yeah, this is very much familiar to me with OCI and everything we did there, and I've been trying to cloudify our support model a little bit, and this beast does not understand that at all, and I have been making some changes, which is good, so we have the NOC now, which everybody everyone understands that's beneficial. But we don't do cloud caliber incident management. We don't do, like you put the developers on rotation, right, you're on, you wrote it, you're supporting it. We don't do that here, and so as we were talking about the hyperscaler stuff today, I was enthused to hear people having those thought processes, which I thought was good.

[00:07:07.62]  Jason ValleryRight? Yeah, I mean, I don't know about me, but I spent the last 13 years on Azure Storage and product role, you know, left there as product management lead for Microsoft's object storage platform, and, you know, that was a key journey that I've been on, which is how to think about Microsoft's field, Microsoft's go-to-market, Microsoft's positioning for object storage, the support model, how that related to our engineering teams, SREs, live sites, operations, capacity management, all of those things kind of come into play.

[00:07:45.34]   RemoteAll that stuff.

[00:07:46.33]  Jason ValleryAnd so, you know, the goal that Jeff and Brandon have shared with me is that we want to get ERA SaaS platform for storage, and fundamentally, that means your tape on all of those things. Like those all responsibilities of VaST to, um, you know, support and run. So yeah, there's a lot, there's a lot of maturity we have to bring to VaST. There's a platform to be done. There's, it's going to be a fun and wild ride, um, you know, to get to that vision. So yeah, I'm looking forward to doing it.

[00:08:15.14]   RemoteSo, I come from startup land, as well as corporate land, so I had background in OCI, TomCast, EMC, and so there's a lot of good stuff that happened to those big companies, and one of the things that at this company we rail against is, we're like, "We're a startup." I'm like, "Well, we're not really a startup, we're like 1,000 people." that's not a startup anymore, and so there's complexity that occurs at scale. Like you need some program management, you need some change controls, you need some process for metrics and reviewing the metrics on a weekly basis, and so we haven't done that, and so we're starting to push some of that forward, and I think you and I are gonna have to do a bunch of. of pushing in terms of metrics reviews and using data to make decisions and that sort of stuff. 'Cause right now, it's just whoever screams loudest wins, which is not productive.

[00:09:11.77]  Jason Vallery- Well, it's also a moment and inflection point for the company where it's a transition, a boxed product in a certain sense. I mean, it's unique because of hardware components and then there's operations in that hardware, but you know. It's sold like a box product to go to the cloud is just a fundamentally different operating model because you're taking on so much of the responsibility that was historically owned by the customer and you have to have an end-to-end service behind it, and those are all data-driven operations, as you say, too, knowing where you've got pain points and where to put pressure on things, react quickly, all of that. comes from running these systems at scale. That's, I'm still learning that. But it's probably not something that there's a muscle around here today.

[00:09:57.23]   Remote>> No, not at all. Do you have any recommendations for good SREs or good CSMs that are from Atter? Because I would like to poach a couple of good ones.

[00:10:08.71]  Jason Vallery>> There are a lot of people looking for jobs. >> Oops, I lost you. >> My phone was ringing and I needed to put it on silent. You know, like I said on the F3 side, what we really want. It's the vast DNA piece, like I agree with Lior on that point of you've got three different cloud providers. The fundamentals of the clouds are kind of similar just architecturally, but you'll have all these nuances on each of the cloud providers. I think that's largely trainable, but knowing the vast pieces of it. where you're gonna have real SRV type work. So I you know I think a good VAST engineer that we can make sure they have an understanding of the cloud is the better path there from an education versus if I went and took you know one of the Azure guys I know or something they would be clueless about how to go debug a VAST issue. Obviously, every SRE structure we put in place will have upstream support from the CSPs when on their knowledge base. So I'm not sure that's where I would approach, but on the pre-sale, not pre-sales, on the customer success side, I think there's probably folks that know that engagement model better. You're solving for the soft skills, the operational excellence, the folks that you know how to go and work with a customer and do solution selling and upselling who are also very technical or are you, do I need somebody who is super deep on the cloud, but like that other layer of skills is something that we've got other support for, and my take here is really, you need somebody who's. It kind of got a little bit of that, the true customer success DNA where they're a little bit more, you know, they know how to influence for impact. They know how to be empathetic and listen to the customers. They know how to ask the right questions, but they also are just super deep technical under the hood. Like to me, that's the persona of the person you really want to go find, and I can think of some of those. pursue my LinkedIn a little bit and refresh my memory of who I would recommend, but I can tell you there are certainly a lot of people at Microsoft that are hungry to leave at the moment because the culture over there is going downhill.

[00:12:35.74]   RemoteI get it. I get it. Probably first thing to do is to go write a job description, a line on that and then we can start an update. Okay, that makes sense. Good times. How can I help you?

[00:12:48.27]  Jason ValleryYeah. I mean, I'm trying to understand the current end-to-end engagement model. I've actually been reading folks and asking this question. But, you know, the life cycle of a customer in the past today from pre-sales, through onboarding, production, through post-production, expansion, through you know, where are all the key touch points and you know how does that all play together. I still have a lot of work around that and maybe I can get your take on it. I chuckle because as soon as I got here within

[00:13:27.03]   RemoteThe first six months I was like you know what we need to go build a life cycle. customer flowchart and then like this so that people know who's who in the zoo and when to engage what person as opposed to running around making a bunch of noise and saying oh my god I need help no you don't you're right here you need this person stop making noise we didn't do that for a variety of reasons it is I think in as we go to the cloud we're gonna definitely need to do that It's funny. I don't have a good answer for you on that. We need to build it.

[00:13:57.01]  Jason ValleryWe need to build it. Well, I mean, going back to my point of customer success, and I'm looking at it from the Microsoft lens and how we approached it in Microsoft's field, it, you know, it's evolved over the 13 years I was there, and it's, you know, there's kind of like this action of the customer success role that's happened multiple times over those 13 years. You know, going from very workload focused customer success to platform focused to pushing it to pre-sales to going to premium and premier models where it's a paid resource and looks more like consulting to return back to the, and so I've seen all of the different kinds of models play out, because Microsoft is certainly experimented with this extensively. So I'm just kind of really curious about what VAST has done there and what we think we need to evolve to. The key points being one of the trends that if I look at the early years of a, we're going to swarm the customer with technical folks who know the cloud and can look at on-prem workloads and make technical recommendations about those workloads migrating to Azure, and that was a free, like part of almost the sales team, and actually in early days, they sat as part of the sales organization and, you know, they were. customer success, and then that model evolved to okay now we're going to have that disconnected a little bit from the sales cycle and these folks will be more of a pooled resource that we can pull in on specific engagements and the opportunity and hunting and sort of like all of that moves back into a traditional sales role. we've got a pooled customer success team we can tap for specific engagements and then that model evolved to chip these are highly valuable expensive folks and how are we demonstrating ROI for them we're going to turn this into effectively paid consultancy where now we're going to actually charge back their time to the customer we'll bring them in on specific engagements and them to be hands on keyboard, meaning instead of I'm going to show up and give a whiteboard conversation and, you know, do a pitch on the platform, I'm actually going to bring these folks in and have them get next to the customer, maybe even badge them as the customer and let them work, but we're going to charge the customer for that to actually, we're kind of in a full pivot now where Microsoft is going back. with the AI opportunities, and changing workloads, and looking to expand, and you know bringing in more resources at the front of the sales cycle. So you know kind of curious how that journey's

[00:16:40.63]   Remoteup here and where you think about that. That's a that's a big question. that today we don't have CSMs doing proactive work. They're all doing support work and doing reactive work. None of it's proactive, and so they're running the weekly calls, they're making sure all the tickets are getting followed up on, they're doing major incident management. They're not doing roadmap reviews. they're not doing feature adoption and they're not doing understanding like what the roadmaps will look like in the future and making sure that we're building all the right features for that. That generally falls on the SEs and some of the Octoguys but it doesn't, no one really owns that and so we have differing levels of engagement from the SEs. Some SEs are great at proactive and great at roadmap, and the other ones are not, and so, I think we are going to need to write a role for proactive, that's what I think, and I think that the proactive stuff is going to need to be a combo of pre-sales and CSM. need to be technical hands on keyboard and so I think having them badged on the customer site is a good thing. I think having giving them access to customer resources is a good thing.

[00:18:10.42]  Jason VallerySo let me let me add another couple qualifying statements too. SD versus CSM, you know titles may be slightly different with Microsoft but yeah. For me, what you're describing sounds mostly like what Microsoft would have called a team. Yes, correct.

[00:18:31.33]   RemoteThat's exactly right.

[00:18:32.40]  Jason ValleryAnd those are always paid resources. So those are not free to the customer. The customer comes along and says, "I'd like an average support contract, and I'm going to pay you a premium for a premium support experience." you know those are all build hourly resources that they manage other escalation engineers that can come in and swarm a support situation versus the mainstream support and so ultimately what you're getting behind that is different SLAs on turnaround time, on incident response and you know that's you get out of one of those contracts, but they're always, Microsoft's calls it Premier Services, like you're paying a very hefty premium for that, and it frankly, the throat to choke kind of thing when you're a CTO that pays up for it.

[00:19:22.87]   RemoteCorrect. I chuckle because when I was at OCI, I had to navigate Microsoft's premium support, whether not it was it was brutal the people who had premium support it was great i got super fast access and if not i had to wait a couple days for like the right person to pick up the ticket it was terrible we don't we don't have the concept of premium support we just everyone's the same caliber of support and we certainly don't have the billing or the time tracking mechanisms for that i think we need to get to the point where we're doing premium services. Not everybody is going to be the same. Frankly, not everybody needs it, and so we need to fund these sorts of premium experiences. That's one thing. Second thing is I think we need to be able to do the time tracking and the billing for that kind of stuff, and we have to skew it up. We have not put any-- I think one thing you're going to learn here is that we have no product management. and I are the product managers, and so we're gonna have to go do all of that product management work that we're both used to having others do. At this company, we don't believe in product managers or program management.

[00:20:28.17]  Jason Vallery- Well, I guess that's why I'm here. So today, like I buy a VAST license. as part of that contract there's no additional line item on the bill and you will give the same level of support to XAI that you'll give to you know random 100 terabyte customer in the club or not random one yeah

[00:20:55.02]   Remoteuh kind of kind of like what happens with what happened with XAI is is we determined they needed a better level of support and we just did it. We figured it out, we created a pod, we created some enhanced tooling, we added some more people on SOC, and then we just did it. Do we charge them for it? No. Should we? Yes, but we don't, and we're getting to the point now where customers are asking for dedicated resources, and we're, I just got off a call today where I'm like, we have to charge for this. I can't fund this through my run rate budget.

[00:21:29.66]  Jason Vallery- Yeah, I think that's right. Are there SLA's and SLO's that we issue? Like ideally what you're coming to is, here's the experience you get. We're going to quantify it for free. you, but if you really want our full attention 24/7/365 and you want to make sure somebody's there with the escalation engineer within 15 minutes of

[00:21:54.02]   RemoteYou reporting a challenge, this is what you should do. Correct. That's correct, and so at OCI we did that for ByteDance and they wanted developer plus support guy plus incident manager within 15 minutes. As soon as the ticket was done within 15 minutes. 15 minutes that doesn't matter whether it's p1 p2 p3 15 minutes all three guys on the we had to build teams to do that and we charged them a buttload of money for it it was like okay if you want developers like we have to have these people cost money it's good incident managers cost money and good support people cost money and we need it for all three shifts and we need a little bit of buffer so that when people are out sick and whatnot that we have coverage, and so you have to charge for that kind of stuff. Here we've not, we've done it through

[00:22:35.75]  Jason ValleryHeroics, but we have to evolve beyond Heroics. - And I know we have federal customers and otherwise. I wonder about like, do you have a premium model for like US NAT cleared folks? Because that's something we dealt with at the time. You're a sovereign customer, you're a government customer, you're the government of Singapore, you want people in time zone, cleared, have security, like does that...

[00:23:04.17]   RemoteThat's super funny. Yes, it does come up. No, the mothership does not have any understanding that that's a thing, and so when we pay... two, three hundred, four hundred thousand dollars for a federal resource. They are like, "Why can't you do this in India?" It's like, "Oh my god, because they need clearance, they need to live in America, and they need to be skilled." You need to find somebody cheaper. You won't find someone cheaper because they won't have the clearance, and if they are cheap, and they have clearance, they're usually no good. So, and as we get into government stuff, like we're doing Singapore government, I had to hire a guy who was super expensive because he had the clearances and he's a Singaporean national. We're going to have more of that as we do Israeli government, EU government, all the other governments. We're going to need to charge for that.

[00:23:49.72]  Jason ValleryYeah, exactly.

[00:23:51.56]   RemoteAlso, those people are going to have to be on call.

[00:23:54.12]  Jason ValleryYeah, and then how that works out, I was talking about this earlier, but all the different rules around data management, data custodian, and then what that means even for like hot picks engineers and you know, yes, yes, yes, those folks still like if they're going to come in and look at a system and look at log files, we need somebody that you know, we can count on can look at those log files and not be... I can't. I will... I will tell you...

[00:24:24.70]   RemoteWe do almost all of our engineering is Israeli, there's a handful of Israeli citizens that are now US citizens, but we don't have, and we have like a small number of people that are doing the federal build. But in terms of data sovereignty, data access, all that stuff, we are not set up. We are not set up for that. If anyone tells you that we are, they're lying, I will tell you that right now.

[00:24:45.53]  Jason ValleryRight now. Yeah, but there's so much opportunity there as a business. So I don't want that. I mean, actually, maybe you saw the Nvidia announcement yesterday, but there's like seven big federal labs that are getting supercomputers, and, you know, the DoD is going to be interested. I haven't met. I believe there's a ton of opportunity there. So we have to focus.

[00:25:03.04]   RemoteYeah, we have to skew up all the offerings. Yeah.

[00:25:08.00]  Jason ValleryWell, I mean, here's what I was like. I know how we did it in Azure. I know what we built there. I know all the challenges we faced. I'm happy to bring that tribal knowledge here flip side for me. Take you up on that getting how we work together in terms of what the product and platform needs to deliver and you know, learning from you on the challenges you guys have faced.

[00:25:30.49]   RemoteSounds good. Are you, um, who, who, who do you, what organization do you roll up into?

[00:25:36.18]  Jason ValleryI report to JF.

[00:25:38.94]   RemoteSo will you be at the AOP meetings in November in St. Louis?

[00:25:44.75]  Jason ValleryUh, I'm going to go to the Supercomputing in St. Louis. Is there an AOP meeting?

[00:25:47.89]   RemoteNo. Okay, yeah. Yeah, yeah, there is. Okay, that's just for Rick's team. They're probably not invited to that. Okay. I'm just trying to figure out when you and I can spend some in-person time together.

[00:25:55.64]  Jason ValleryWell, what I'll say is I don't know what meetings I'm supposed to be at yet. I literally started last week and maybe Jeff didn't tell me there's a meeting I'm supposed to be at. But yeah, I don't know. Maybe it is just Rick's team.

[00:26:06.49]   RemoteSounds good. Yeah, we'll figure it out. We'll figure it out. Cool. Welcome to the chaos.

[00:26:12.18]  Jason ValleryYeah, sounds good. Thanks. Nice meeting you, man.

[00:26:14.16]   RemoteGood stuff. All right. Take care. Thanks, bye. Thank you.
```

<!-- ai:transcript:end -->
