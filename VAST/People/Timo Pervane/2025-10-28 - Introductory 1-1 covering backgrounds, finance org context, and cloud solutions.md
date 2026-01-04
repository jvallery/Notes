---
type: "1-1"
created: { { DATE } }
status: "done"
counterpart: "[[Timo]]"
role: ""
team: ""
company: ""
series: "1-1/Timo"
cadence: "Weekly"
meeting_mode: "Video"
location_or_link: ""
calendar_url: ""
start_time: ""
duration_min: "30"
privacy: "internal"
ai_extracted: true
transcript_path: "00 Inbox/Transcripts/20251028 1306 Parallels Transcription.txt"
tags: [meeting, "1-1"]
---

# 1:1 — Timo — 2025-10-28

> [!info] Purpose
> Build trust, surface and remove blockers, align on priorities, coach & grow.

## Summary

Introductory 1-1 covering backgrounds, finance org context, and cloud solutions strategy. Timo outlined his role leading corporate finance and the plan to hire a dedicated finance business partner for Cloud Solutions. Jason shared his Azure/OpenAI background and vision: evolve beyond marketplace VM-limited offerings, pursue exabyte-scale use cases with hyperscalers, and build a unified data platform across on-prem, multi-cloud, and neo-clouds. They discussed investor valuation (growth-adjusted ARR), current pricing shortcomings, and exploring a unit-based model with strong discount discipline.

## Key facts learned

- Timo leads Corporate Finance: FP&A, planning, IR, corp dev; joined ~11 months ago under CFO Amy Shapiro.
- Finance bandwidth is constrained; Amy is the first CFO and company is ~1100 people.
- Hiring a finance business partner for Cloud Solutions; candidate from a hyperscaler, interviewed by Yancey and meeting Renan later this week.
- Boston hub has ~40–45 employees (incl. CMO Marian Budnick, CAO Jason Ainsworth, data leader Joe Stevens).
- Investor lens for next ~3 years: growth-adjusted ARR multiple.
- Current pricing: $/TB (historical) and $/compute added mid-Q2; discounting discipline is poor with wide price dispersion.
- Risk of customer backlash and contraction due to inconsistent pricing and peer comparisons.
- Jason’s strategy: move beyond VM-limited marketplace; target exabyte-scale customers to unlock hyperscaler hardware; help address Azure control plane challenges; build common data namespace across environments.
- Unit-based pricing ("VAST units") could normalize pricing across storage/compute and on-prem/cloud and ease migration to new model.

## Outcomes

- Alignment to explore a unit-based pricing model and tie it to ARR-centric investor metrics.
- Agreement to enforce stronger discount discipline, especially for cloud SKUs and overall deal control.
- Plan for Timo to share business metrics/valuation framework and pricing data; continue collaboration on pricing evolution.
- Acknowledgment that a dedicated finance business partner will be embedded with Cloud Solutions once hired.

## Decisions

- (none)

## Action items (for Timo)

- [x] Draft a unit-based pricing proposal (with Databricks/Snowflake references) including ARR impact modeling and discount guardrails. @Jason Vallery ⏫ ✅ 2025-10-28
- [x] Share investor valuation framework and metrics (how ARR is defined/measured and implications for Cloud Solutions). @Timo ⏫ ✅ 2025-10-28
- [x] Provide current pricing/discounting analysis (price-paid scatter by cohort) to inform normalization plan. @Timo 🔼 ✅ 2025-10-28
- [x] Define discounting policy and controls to prevent deal-level leakage when cloud SKUs are undiscountable. @Timo ⏫ ✅ 2025-10-28
- [x] Progress hiring of Finance Business Partner for Cloud Solutions and embed them with the Cloud Solutions leadership team. @Timo ⏫ ✅ 2025-10-28
- [x] Identify and prioritize exabyte-scale customers to pursue hyperscaler hardware commitments and escalation path. @Jason Vallery 🔼 ✅ 2025-10-28
- [x] Align messaging with finance to brief Brennan and Jeff on the pricing evolution rationale and ARR impact. @Jason Vallery ⏫ ✅ 2025-10-28

## Follow-ups

- [x] Schedule a deep-dive session on business metrics and ARR framework. @Jason Vallery 🔼 ✅ 2025-10-28
- [x] Send pricing scatter/discounting data set and initial insights. @Timo 🔼 ✅ 2025-10-28
- [x] Update on finance business partner hiring status after Renan interview. @Timo 🔽 ✅ 2025-10-28

## Risks

- Pricing inconsistency leading to customer dissatisfaction and revenue contraction.
- Deal-level discount leakage offsetting non-discountable cloud SKUs.
- Founder-driven resistance to changing legacy pricing positions (Brennan, Jeff).
- Finance coverage constraints until a Cloud Solutions business partner is hired.
- Dependency on hyperscaler cooperation for hardware footprint and control plane changes.
- Time-to-market risk if pricing model and guardrails are not implemented promptly.

## Open questions

- What exact unit definitions and conversions (storage/compute; on‑prem/cloud) should the pricing model use?
- Which revenue streams will qualify as ARR for Cloud Solutions under the investor lens?
- What approval thresholds and guardrails will govern discounting and deal-level leakage?
- Which exabyte-scale customers will anchor hyperscaler hardware asks, and what is the executive escalation path?
- What is the target timeline to brief Brennan and Jeff on the pricing proposal?
- How will the common data namespace be phased across on‑prem, multi‑cloud, and neo‑cloud environments?

> Next meeting (if any): (none)

---

<!-- ai:transcript:start -->

## Transcript (auto)

```text
[00:00:00.04]  Jason ValleryYou doing good? Apologies for being a few minutes late there.

[00:00:03.08]   RemoteI was wrapping up another call. No worries, no worries. I think we're all just having calls with each other. Yeah, it's you know

[00:00:10.35]  Jason ValleryBouncing around and figure this all out. So it's fun times, you know. Yeah, for sure, for sure. So cool. I'm glad we have a

[00:00:18.87]   RemoteLittle one on one time together. It's nice to meet you. Yeah.

[00:00:22.55]  Jason ValleryThat was my goal. Obviously we've been on a few calls together and today is a week and a day into this role. I'm hitting the ground running, lots of things going on, fire hose, all of those metaphors, but I just wanted to make sure I get some sort of one-on-one relationship established, kind of understand your roles, responsibilities, priorities. I see you as our finance counterpart primarily, but I would like to know more about that and I'd be sure more about my background. So yeah.

[00:00:55.39]   RemoteThat sounds awesome. Yeah. I mean, I'll give you a brief intro, kind of my background, what I do, et cetera, and then, you know, I'd love to also hear. I'll just give you like a set of bullets to start, so from the Boston area, still live here, lived in Europe for about six years in the middle, early part of my career, London, Munich, Brussels, business school, summer in Beijing, and then I was like, I'm good, so yeah, brief background, mechanical engineer by training, so I was actually more of a computer programmer growing up, studied mechanical engineering, so kind of the most dangerous kind of engineer, which is, you know, trained in it, never practiced it. I got interested in business, so yeah, background includes consulting, entrepreneurship, co-founded two companies, one very small, short-lived, the other larger, kind of became a major corporate joint venture in the space of telematics, so connected cars. was an area that Microsoft was deep in for a time period. So, but I'm probably dating myself. This was the late '90s, early 2000s. Back to consulting, I was a partner at Oliver Wyman, kind of reached the point where it's like, you know, like I did everything I wanted to, kind of learning curve is slow, but I'm like kind of getting bored, wanted to get back into operating. So went and actually joined Amy at Shopify. So Amy Shapiro, our CFO was the CFO of Shopify, and she, I've known her for like 15, 16, She's a client of mine from way back in the day, created a ton of value together, and so was a business unit CFO at Shopify, super fun, rocket ship, very exciting, enjoyed the role a lot. So had fun, CFO role has changed over time, you know, when I was younger, it was sort of more. accounting, backward-looking, kind of like scorekeeper, has become much more strategic, operational, forward-looking, you know, and so, in addition to the other stuff. So, I enjoyed that. Did a couple of short, smaller ones, kind of the joys of uncontrollable, early-stage risk, and then joined Amy here about... Almost a year ago. Um Amy's been here for like a year and a month or something like that, and I think I've been here for like 11 months So, um, I Yeah lead corporate finance so cover a things. So, corporate FP&A, so overall model, annual planning, long range planning, FP&A, investor relations, corp dev. you know, strong word kind of stuff, and, and so that's my role. You know, with regard to hyperscalers. I'm actually trying to currently trying to hire in somebody who would serve as the business partner. to cloud solutions and be able to be like I think you probably noticed from the various calls we've had we've had like a lot of different finance people on the calls and funnily enough that's actually because of a lack of coverage and bandwidth and so uh really what we need to to do in the person i'm trying to hire fingers crossed, would be able to actually be your primary business partner and would interface, serve on the cloud solutions leadership team and kind of be able to provide all the financial analytics support insight, et cetera.

[00:05:37.60]  Jason Valleryin mind already you've got a good lead on someone have a good lead on someone yeah uh yancey's met

[00:05:44.00]   RemoteThem um they are interviewing with renan um later this week so um yeah they should be great they come from a hyperscaler um they're a hyperscaler now so um should be really good um So, fingers crossed. Yeah, that was kind of a rambling, hopefully not too rambling, overview and intro. Yeah, we'd love to hear kind of your story too.

[00:06:16.33]  Jason ValleryYeah, that's an interesting background to go from mechanical engineering to finance in that way. So, yeah, fascinating.

[00:06:22.67]   Remote- Yeah.

[00:06:23.45]  Jason Vallery- So since you're in Boston, it sounds like maybe there's a center of gravity of folks there, 'cause you know, Wolfie's there, right?

[00:06:29.89]   Remote- Oh yeah, there's, you know, there's a fair, there's maybe like, I don't know, 40, 45 people here. Our, yeah, Wolfie is here. Marian Budnick, who's our CMO is here. Jason Ainsworth, who you met, who's our chief accounting officer. is here. Joe Stevens who runs data is here. There's a good little, a good little group. Yeah. I think on the East Coast, sorry?

[00:06:57.19]  Jason ValleryDo you have an opportunity to get together or work in any sort of collaborative way? I see areas of overlap that probably don't make sense.

[00:07:04.72]   RemoteWe've talked about it a lot. We're all running, so. hard. Like we've had we've had like breakfast once and I think lunch once over a year and so yeah it's every like we're so finance here and so this is like vast has done this might give some insight so vast basically has done what most startups do. which is essentially focused only on building a great product and selling a great product, and like minimal other, and so, like, Amy's the first CFO, and we're 1100 people, like, if I turn the clock back to when I started, like, there's been market progress in terms of just what we have, and we're not even close to where we need to be, and so it's been very, very minimal, and you'll see that in other areas of the company too, like on the GNA side of things, it's just very minimal, and so as a result, just full candor, everybody who's joined finance, like myself, has been just pretty strapped. So we've talked about like, Oh, like, you know, get like a we work for a day and I'll work there or whatever, but it just hasn't happened. So

[00:08:24.31]  Jason Valleryas things go, I mean, a lot of people just prefer to be at home anyway. So it is. It is a little Yeah. Well, let's see. So first decade of my career, I was a software developer. I'm highly hands on kind of guy, I still try to get my hands dirty where I can. That was the end of that stint was right as I was moving to transition into the GSI specifically Avanade, I don't know if you're familiar with it, but they're like Microsoft Accenture's partnership, and so I was leading a team at Avanade doing line of business. development in a consulting fashion for like Fortune 100 kind of companies and at that moment in time Microsoft was pushing really hard on what at that time was incubation and Azure at that time didn't even have virtual machines. It was a cloud development platform where you could go, you know, write some .NET code, Microsoft's dev platform and publish. publishing it, and then they would host it for you, and there's a fun back story around Azure. You haven't got to that point, but I'll save it for drink someday. But anyway, they were looking for somebody to kind of come over and do this for Microsoft. So I made the transition into Microsoft kind of just seeing the writing on the wall that the cloud was the future and specifically cloud native. So, you know, very anti-lift-and-shift, this is Greenfield projects, how do you architect and build an application to scale it and leverage these like fragile primitives that are on the cloud? So, I was early days Azure, I came over and then, you know, the data part of that was a key focus area for me. So, and I worked very closely with the Azure storage team. who also owned, so at the time the only service was blob storage, and a table storage service, which was kind of their database scale for the cloud Azure tables. I joined the product team for blob and tables, and I've been there up until two weeks ago. That's 13 years of growing from We were excited to get our first couple of customers, our first Pebibyte customer to literally hundreds of exabytes, and through that journey, I wore a lot of hats from owning various features and areas, pricing models, whale customer engagement, leaving that role as your product manager, owning our forward looking. strategy for AI. Along that journey I got a phone call in 2018 and saying hey Microsoft's making this investment in this little 501c3 in the Bay Area called OpenAI. Would you like to meet with them? Help them figure out how to get some data on the platform. So my first meeting with OpenAI in 2018 like a freaking... No way! That's awesome! ago. There was like 25 people at OpenAI at the time, and so myself and my team owned the relationship with OpenAI from then until again a few weeks ago. You know, I watched them grow on the platform, so I was their key storage counterpart, worked hands-on with the OpenAI leadership team, you know, grew them from, you know, not being, having any whatsoever anywhere to their tens of exabytes that they've got on the platform and there was why here? Why did I make that career jump to come to a startup? We're not really a startup at best,

[00:11:51.26]   RemoteBut it's a different world. Certainly more so than Microsoft.

[00:11:55.32]  Jason ValleryYeah, exactly. Why that's? Well, the writing on the wall with OpenAI. I changed the day-to-day. The relationship with Microsoft went south earlier this year. A lot of internal Microsoft politics and infighting. Azure itself has been kind of, I'll say, corrupted in the leadership levels. The whole team is kind of collapsing. Just the politics got the better of me. I assume you've probably heard of or know Glenn Lockwood. He came over in July. One of my early, one of my tasks actually at Microsoft in the last few months was the competitive analysis. Like, I've been well aware of VAST and the capabilities it brings, and so I did a lot of deep dive work to make sure there was position to compete with VAST, and, you know, I really, you know, storage engineer at heart and really a deep technical guy, I became very convicted that Microsoft doesn't have the right roadmap to be successful and the right talent and setup, and I'm very convicted that Vast has already made the right set of investments to be successful. I also see, and I talked about this, I don't know if you saw the podcast that I did earlier. last week, but I also see like the repatriation of data and the proliferation of Neo clouds and the sort of sentiment coming out of the enterprise customers that Microsoft had unlocked to be a trend that says, you know, we're tired of cloud economics in the sense that we don't want to be stuck. we're tied, you know, we're on your roadmap. We're on, you control our destiny. So all of those things came together to me saying like, look, it's an interesting opportunity to go take some risks but also go like do something different and still really leverage all of those experiences in a meaningful way. So that's what got me here.

[00:13:47.60]   Remote- Awesome. Welcome. That's awesome. What an amazing story.

[00:13:51.43]  Jason Vallery- Yeah.

[00:13:52.87]   RemoteCool, cool, cool, very cool. Yeah, no, I think it's terrific that you joined. I mean, as you're probably getting the sense, I'd be curious to get, I mean, but like overall, I would say the cloud solutions business is an interesting one, or vast, because it's... because it is clearly necessary. It's also where a lot of the kind of, I'll just say like old way of operating runs into very sophisticated needs, and so, I don't know, for example, pricing, like the pricing discussion that we had on Monday, It was like, my impression was clearly this needs a lot more thought, like, this is like, we're not gonna get where we need to get with this, like, we need a lot more thought, and I think you're, I think you're, you know, my guess is you're probably going to find that across a bunch of areas, and that's kind of like the nice thing about cloud solutions. is I think it's a bit of a forcing function, but it's an important business in its own right, for sure. Like we have to be successful at it, but it's also a nice bit of a forcing function where it's like, oh, this is like a more sophisticated business. It forces a higher level of sophistication, which I think is a good thing.

[00:15:19.55]  Jason Vallery- I said some initial thoughts last night to Tomer and Yancey, you alluded to it earlier. I have a lot of thoughts on how we need to evolve the pricing model, based up my limited knowledge of the institution around here. It sounds like it's going to be a bit of an uphill battle with Brennan and Jeff, but I hope we can come armed with a conversation and convince them they have to change their minds, change their way of thinking about this problem. The key opportunity in the cloud is not what we're going out with right now in the marketplace. Running on VMs and being limited by the resources that provides and the pricing model that provides will always hold us back from the first party offerings that the cloud providers have today, and therefore you're always going to be kind of an afterthought. You're really not going to win the share that you deserve. But in order to actually break through that, you need to actually become effectively a competitor with the hyperscalers themselves, and that's not a near incentive, and so it's going to require us to leverage Vast's reputation and the customer base that are demanding. the kinds of performance and scalability that BAST has already demonstrated on-premises, and so, you know, my key lever to try and unlock that is Microsoft data, opening, UK data. Like, those customers, these Exabyte-class customers that have a set of requirements that you're never going to deliver through the marketplace in the current way, hopefully initially need to go and unlock, you know, conversations at higher levels of Microsoft to give us the hardware footprint we need. I think there's also components around this which I could get into around strategy from the way Microsoft deploys infrastructure and manages it, like there's a bunch of things they've got in terms of challenges around their control plane that we can help them solve. So, you know, if I didn't see that as being the lever in the door and I thought I was coming here to manage a marketplace offering, I would probably turn this job down, frankly, because it's not going to hit the targets that Renan's given me. The second piece of this is going back to my point around proliferation of data in the cloud. One of the things we talked about in Azure all of the time, for most of my time in Azure, is this concept that data has gravity. you know, really what that structure was is that the data would sit in the hyperscaler and then they would bring compute to it and then the compute and the services attach themselves to the data. That, like, I am 100% believer that we're in an inflection point where that just no longer flies. For the reasons I articulated, like, enterprise customers don't like the cloud lock-up, the proliferation of infrastructure. infrastructure build out, the Neo clouds, the need to bring data to wherever inferencing is happening, which could be, you know, on-prem, robotics, satellites and orbit, like all over the place, right? And so the data platform has to evolve to support that, and that's what I'm super excited about is the vision of taking and combining the on-prem customer base, the. multi-cloud customers, the proliferation of neo-clouds, and being able to tie that all together with a common data namespace, that has got to be part of our key strategy in how we attack the cloud. So those two things together bring me confidence that Vast is well-positioned, and we are well-positioned to kind of seize on this next level of infrastructure investments.

[00:18:43.29]   Remote>> Yeah, no, for sure, and it is, that's very cool. Very cool. Obviously, we'll have a lot of talking along the way. Like anyways, I can be helpful to you now as you're kind of onboarding and any questions I can answer for you, or I don't know, I mentioned on the call earlier, I could talk you through the various metrics that we use for the business.

[00:19:07.97]  Jason ValleryThat's probably the most important thing, how we think about accounting, all of this. What I'll need, certainly as we evolve the pricing model discussion, is the right set of financial motivators. How do we think about revenue reporting and how does that reflect out into the investor community and obviously IPOs? things that are in the future potentially, like if we're building up revenue model in our pricing model, like if we can build evidence from the financial lens that'll help unblock Jeff and Brennan's thinking on this topic, you know, that'll help make an ally out of you and we can go with one consolidated voice on how this has to evolve.

[00:19:48.97]   RemoteYeah. I mean, I'll share this, uh, and happy to take you through the, like. what investors will value us on and stuff like that. I mean, the simple answer is like for the next, well, for the next, call it three years or whatever, within an IPO timeframe, we're going to be valued on a growth-adjusted ARR multiple, and so it'll be a multiple of ARR and then adjusted for our higher growth, and we can talk about how that will flow through into thinking about cloud solutions, etc. But I'll share on pricing, because I really liked your thinking around units, and part of the reason why I liked it is because of one of the... I mentioned on a couple of the calls, so we currently have a fairly simple, it's dollars per terabyte. Historically, we introduced dollars per compute in Q2, like mid-Q2, which is great and it's simple and it's elegant and all those good things. but we have terrifically bad pricing discipline, and so like the, if you look at it, it's kind of like the classic, I don't know, I've done in my past life, I did a ton of pricing work and like you always kind of get for a company that hasn't really been thoughtful about pricing, you always get kind of like a shotgun. blast, when you look at the actual prices paid, and we have a very bad shotgun blast. So if you look at actual price paid per terabyte across a set of customers that are similar-- so similar size, they're buying similar amounts. It varies from-- I'm kind of making these numbers. up, but it varies from like, you know, a dollar to $20, and so, um, simply because there's been no discounting discipline, it's just really get what you can get, you know, kind of whether that's like much higher or much lower. Well, what happens in any market is you have customers who talk to each other, or you have people who move jobs. I was the head of infrastructure at Hedge Fund X. I move, and now I'm the head of infrastructure at Hedge Fund Y, and I'm like, "The fuck

[00:22:24.95]  Jason ValleryAre you guys paying?" Or you break the infrastructure for XAI, and now you're running infrastructure for OpenAI. knows where you charge them. Yeah, kind of has an idea, right? And so, and I've seen this in like

[00:22:35.73]   Remotea ton of markets and you even get like, this won't happen to us, I think initially, but you get little consulting companies that spring up and they're like, Oh, we'll help you to, you know,

[00:22:44.21]  Jason ValleryEven out your software bill and just have a database around that with Azure. Like there's like these boutique firms that have their own software. they go to do crowd pricing and then they do negotiations for you like as the end customer i can say okay you go negotiate with microsoft for me yeah it's ridiculous yeah any market big

[00:23:03.44]   RemoteEnough you get this you get this in like any market where it's like big enough there's an upcoming store they're like yeah and literally all they're doing they just have a database of what everybody's paying and they're like oh okay well we know this so um long story short So there's contraction risk there and also piss off your customer risk because no one likes to find out they've been paying whatever a lot more than their peers, and so one of the things I did like about your unit idea is, you know, a fairly wholesale pricing model change is a good. way it's a labor intensive but good way to deal with that risk because it kind of gives you an opportunity to reset a little bit. You can't move people too far too fast obviously but like you can reset a little bit. If it was something like for example you know across that full data space that you talked about you get units whatever they are. vast units which convert into, I don't know, X terabytes on-prem and Y terabytes in the cloud and X CPU, X cores on this and Y cores on that. All of a sudden, A, you've given some value to the customer because it's like, "Look, you can use what you want where you want it. optimize it for yourself, but B it also may solve a pricing challenge that we have, which is, you know, it gives us an opportunity to say, oh, well, your unit, you know, for the folks who are way down here, it's like, well, you know, you happen to be getting a great deal, you know, much better than your peers, and when we translate you, it's, it's actually this, and we're not going to get you up there overnight, but we'll stair-step you towards that, you know, over time, and then for others, like, you never want to come down, obviously. But, like, sometimes you're like, look, you know, we're going to get you here over time kind of thing, and so it just gives us a little opportunity to normalize. So anyways, I thought that might be helpful. I'm happy to help. One thing you will note, and we're both probably over time, so we need to go. One thing that you will notice here, which is not super unusual for startup-y, strong founder-driven companies, is there is that dynamic of like, "Oh, Brennan said X three years ago, so therefore we will never ever consider it." or X, and it's like, well, good to know, but a lot of change happened in three years and X might make a lot of sense, and so let's at least think about it. Let's put together a case around it, and to your point, we can support that case with financial analytics that will tie it to. of the performance metrics that he cares about. So yeah, it's a long story short. That context is potentially helpful. The other issue we will have to face just as a note on the discounting front is if we end up in a situation like, for example, And Yahtzee is very on board with discounting discipline, which I love, is a cloud SKU. Like, we don't want to discount that. Awesome. We still need to make sure that the rest of the deal is not discounted to accommodate that discount, if that makes sense. So it's like, oh, OK, great. This is an undiscountable SKU. Awesome, and by the way, our overall deal discount just went up by five.

[00:26:41.32]  Jason ValleryAnyways, well, the confidence in the model, take a look at what Databricks snowflake others do. I mean, we have a similar set of constraints. I'm not reinventing any wheels here. This is, this is what's been proven out by the industry already, and I think it's a good way for us to follow.

[00:26:58.05]   RemoteYeah. I love that you're bringing the thoughtfulness. Yeah, I think there's clearly a sophisticated business, more so than historical vast,
```

<!-- ai:transcript:end -->
