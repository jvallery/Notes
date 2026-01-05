---
entities:
  people:
  - '[[Liraz Ben Or]]'
type: transcript
source_type: unknown
date: '2025-10-29'
---

# 1:1 — Liraz — 2025-10-29

> [!info] Purpose
> Build trust, surface and remove blockers, align on priorities, coach & grow.

## Summary

Intro 1-1 where Liraz walked Jason through VAST’s non-traditional release management process, org structure, and tooling. Covered phase gates, QA cycles, overlapping releases, prioritization driven by field/customer needs, and artifacts (wiki, QTest, weekly status). Liraz shared 5.4 materials. Agreed to follow up and meet in person during Jason’s Nov Tel Aviv trip.

## Key facts learned

- Liraz is Head of Program Management; team of three; deeply involved in release management and phase gates
- Releases follow waterfall with four phase gates: 1) scope review, 2) plan and change management, 3) code freeze and beta readiness, 4) release
- QA runs three cycles per release: Phase 1 (all tests), Phase 2 (re-run failed), Golden Run (all tests again)
- Target QA success rate is ~96–97%
- Release cadence is roughly every five months
- Org split: core dev focuses on future major releases; vForce handles all field releases and escalations
- Active trains: 5.4 released last week; 5.5 in progress; 5.6 planning starting; older trains (5.3, 5.2) still maintained; 5.1 only hotfixes
- 5.2 minors being released due to upgrade issues in the field
- Overlap: during 5.5 code freeze, some devs move to 5.6 planning; release managers alternate (e.g., Orly and Roy/Ory) across planning and execution
- Phase Gate 1 for 5.6 is targeted in about two weeks
- Architects write FRDs; PRD follows FRD; product (e.g., Tomer, Jeff) curates customer-driven feature lists
- Prioritization is strongly field/customer driven; change management used to drop or stretch features; anchor features get beta customers and early drops
- Artifacts: per-release wiki pages (status, owners, dates), Gantt (often Excel), QA in QTest, and weekly internal status decks
- Example: Tesla requirements drove expedited milestones on 5.4

## Outcomes

- Shared 5.4 phase gate materials and status links with Jason
- Aligned on follow-up discussion next week and in-person sync during Jason’s Tel Aviv trip (Nov 23–26)

## Decisions

- (none)

## Action items (for Liraz)

- [x] Review shared 5.4 phase gate materials and status wiki @Jason Vallery 🔼 ✅ 2025-11-08
- [x] Send 5.5 status wiki and current Gantt links @Liraz 🔼 ✅ 2025-11-08
- [x] Schedule a follow-up 1-1 next week to go deeper on process @Jason Vallery 🔼 ✅ 2025-11-08
- [x] Plan an in-person sync in Tel Aviv during Nov 23–26 @Jason Vallery 🔽 ✅ 2025-11-08
- [x] Connect with Asaf/architecture to align thematic roadmap for cloud-driven features entering core product @Jason Vallery 🔼 ✅ 2025-11-08
- [x] Confirm access to QTest and weekly release status decks @Jason Vallery 🔽 ✅ 2025-11-08

## Follow-ups

- [x] Confirm invitation and attendance for 5.6 Phase Gate 1 @Jason Vallery 🔼 ✅ 2025-11-08
- [x] Collect links to 5.5 status wiki and Gantt (if not already received) @Jason Vallery 🔼 ✅ 2025-11-08
- [x] Align with product (Tomer, Jeff, Noah) on how customer asks roll into PRD/FRD for upcoming releases @Jason Vallery 🔼 ✅ 2025-11-08
- [x] Discuss documenting the phase gate process (RACI, artifacts, exit criteria) to reduce tribal knowledge @Jason Vallery 🔽 ✅ 2025-11-08
- [x] Clarify support policy (e.g., major minus two) and explicit EOL for 5.1/5.2 @Jason Vallery 🔽 ✅ 2025-11-08
- [x] Coordinate with field on potential beta customers for 5.5 anchor features relevant to cloud @Jason Vallery 🔽 ✅ 2025-11-08

## Risks

- Process is largely tribal knowledge; lack of formal documentation for phase gates
- Strong customer-by-customer prioritization may complicate product surface and architecture
- Maintaining older releases increases overhead and slows migration (e.g., 5.2 upgrade issues, 5.1 hotfix-only)
- Code freeze timing not fully aligned with QA Golden Run can create planning ambiguity
- 5.4 not yet fully stable; pushing customers mainly to 5.3 for now

## Open questions

- Who owns formal documentation of the phase gate process and exit criteria?
- What is the definitive support policy (major minus two) and EOL schedule for older trains?
- Who is the primary point of contact leading vForce/escalations?
- Should cloud client components adopt the same release phase gates and QA cycles as core?
- Can we establish a thematic roadmap to balance customer-driven asks with coherent architecture?

> Next meeting (if any): (none)

---

<!-- ai:transcript:start -->

## Transcript (auto)

```text
[00:00:00.04]  Jason ValleryYeah, Jason's good. Hi, I just wanted to set up some time and introduce myself and kind of get to know you in your role after kind of our earlier connections. So nothing too formal, just saying hello and meeting the team. How's it going?

[00:00:14.67]   RemoteI'm fine, I'm working at VAST for almost six years, five, yeah in March it will be six years. Yeah, I'm a head of program management here, so I'm doing like the major releases. We switch, what do you call it, the job description from time to time because we are growing, so it's not enough, so I have a team of three people now, and we have like a release manager usually they are doing the planning phase, and my team, they are doing the execution. I'm very not standard program management. So I'm very involved in the release management also, and also responsible for the Faithgate, if you notice. The meetings that I invited you, yes. So we are doing. four phases during a release time frame for example now 5.5 is on this and in the making so we have like four phases there that we basically uh development uh present the status of the release the content at first phase then in second phase if we have changed management if we are not able to meet the list of features that we committed to and then report progress and then

[00:01:36.00]  Jason ValleryRelease it. I've heard a little bit about this release management process and the release manager and all of those pieces from the team but maybe you could just walk me through the lifecycle so I understand where those gates sit, what feeds into each gate, who's making which decisions, like it would be helpful if there's some sort of overview you could provide around all of that.

[00:01:56.75]   RemoteSo, we are, again, we are not very traditional because we have a lot of people involved in one release, so can you see the board? Yeah, I can. So, master is usually like the... and like at some point we catch the 5/5 for example okay we had 4/4, 5/4 and we have 5/3 by the way we released 5/4 like last week okay and then we start to release minors okay so we have like 5/4/1 the next one to be released and now we are releasing 5/3/4 Okay, yeah, five three was like a I think half a year ago some something like that So but we keep maintaining the old releases. Okay, how far back like is there so we Basically a five two five two. We didn't really want to release more Minors, but we have two last ones. So right now we have five to, how do you call it, 524, I think, we are making like two related there. We didn't plan to have at 5.2 but a field, usually we are very, very field-oriented. So what happened, a lot of upgrades are not working well right now, so we are listing 5.2 minor for all the upgrades

[00:03:30.05]  Jason ValleryFixes that we have so is it we support the backwards support statement is it just until everyone's off of that release or is there so I think 5/1 we

[00:03:39.20]   RemoteHave customers it's 5/1 I'm not I'm not into that into details in the older versions because what happened I have a my my role of responsibilities and when the major, I'm part of the major releases, but I'm already familiar with the whole process, but like, for example, I had involvement in 5-4 until it was released. Then it's going to the V-Force, by the way, if you are aware of this saying. not so maybe you can yeah yeah yeah we have a lot of so basically the chief r and uh chief r and d officer okay so i understand how what he did he built like a development yeah okay so he has development and q quality basically quality okay so development is there you'll give you the I think the VP of R&D. Yeah, and here is the duty, right? Okay. But on top of this, he has a lot of more teams. So for example, I'm also here, that's the program, and you have like vForce, okay? He has a lot of more people, but so vForce are responsible for all the releases. Basically, what happened, we saw a lot of action going on in the past, I think, something like three years, that he decided to have, it's a development organization, that is separate from them. Okay? Developers are responsible for the major future releases. I'm sorry, you see what I'm writing?

[00:05:18.88]  Jason Vallery- Yeah, yeah, I can see just fine.

[00:05:20.55]   Remote- Yeah. So he divided the development group into two parts, basically, one is the major, it's a massive part that you'll get every responsible and they're responsible for future releases, the majors.

[00:05:36.12]  Jason Vallery- Yeah.

[00:05:37.60]   Remote50 features per release and because I feel the older versions take a lot of effort, we build a separate group. It's developers that switch from this group to this and sometimes we rotate them. People love it. Sometimes people love it so they stay there for years. First you need to motivate people because it's like a long hours, you know, expected to get calls in the middle of the night, so it's a lot of stress.

[00:06:06.50]  Jason ValleryYeah.

[00:06:07.15]   RemoteAnd this, by the way, is the Weishtermann. Okay. Okay? Yeah, he's very escalation-oriented, very escalation-oriented, okay? So they are responsible on all the releases. We have still on the field, by the way, 5.1, okay? We have 5.1 in the field. We do not release, unless it's a hotfix, we do not release their version.

[00:06:34.23]  Jason Vallery- Got it.

[00:06:35.06]   Remote- It's very hard. We basically want to maintain a major minus two, but because Rust is not that strong, we let the customers keep. the old versions so what we are doing we are doing hotfixes if they want yeah I

[00:06:52.48]  Jason ValleryWould assume it's like breaking bugs security hotfixes I mean yeah it's very

[00:06:59.60]   RemoteHard to move the some of the customers to a new or latest and now our focus is to move to 5.3 that's the main goal It's 5-3 when we release 5-4, you know, because 5-4 is not stable enough. At some point it will be stable and then we push more towards 5-4. But now in the process we are 5-5. So I'm part of 5-5. So I'm doing a lot of stuff. It's moving parts. So release management, so failgate, so they aren't planning the releases, okay? So they basically, we have Noah, Noah Cohen, and the Traveler, okay? They are kind of, it's funny, it's internal product, okay? Because we have, I'm calling it internal product for you to understand, because I do not know what title even, because we have product, we have Tomer and we have like Jeff, they are doing more of the customer space thing, talking with the customers, actually they are also involved in, they're having a list of features that they want to have in the next release. Now we are talking about 5.6 for example, the content there, okay. So product basically have kind of a list of features. of features that we want. They give the names of the customers to see what weight each feature. Based on that, we decide what's the content, and then it's going to release management. We have now Oi, Tzu, and Oli that are sharing releases, okay? So they are doing the lower level. So once you have in phase gate one we propose the content, phase gate two we said what we can commit or change management basically, okay? And they are doing the lower level detail plan, yeah? Then development, 'cause we are... We are working, not in IJAL, we are working in Waterfall.

[00:09:03.03]  Jason Vallery- Yeah, so phase gate one is requirements review, phase gate two is costing and architecture.

[00:09:09.41]   Remote- It's a change, how do we call it? Phase gate one is scope review, and phase gate two is the plan and development and change management, basically. The timeline, we're talking about the timeline. and what we see that we can commit and what's not, or if there is new deals or something. So it's called change management, that we are talking about what's in and what's out, OK? So that's the second one. The third one is the-- wait, I'll open it to you. The third one called a code freeze and beta readiness. OK, and the fourth one is restricted. Basically, the fourth one, when we release. So in phase gate 3, we are sharing the success rate, the coverage, the open issues that we had beta customers. get to usually i'm raising a question i want from field to get better customers so for us to gain more confident about the feature about the release we are looking for better customers that early drops basically the release so usually we have like a top feature that we call anchor features okay that uh We're pushing to have a customer on it for sales and everything, and then we gave them early drop off. It was in 5/4, and we do the same 5/5.

[00:10:42.35]  Jason VallerySo when you think about timeline across those four phases, is there any sort of fixed calendar approach to that? Or is it just as each month goes by, then it's very--

[00:10:53.26]   RemoteOnce every two so I think the last release was five months something like that five yeah I have statistics I have a one of my team members she is the collecting the statistics we released them something like around five months every release okay so we have a phase get toward so the last two it's easy for me to say the first gate uh four is when we release it three and the first gate is when we start the golden amount so basically what we have right in waterfall we have a feature called freeze I mean it's called freezeinaudible So we are not aligned. We call code phrase a golden line, okay? Because in QA, code phrase is not really here.

[00:11:51.80]  Jason Vallery>> It's like 2.5 or something.

[00:11:56.22]   Remote>> What?

[00:11:57.56]  Jason Vallery>> It happens.

[00:11:57.98]   Remote>> No, because we have three side. than QA. We have first cycle, second cycle, and golden run. Okay? So first cycle is running all the tests. Okay? Second cycle is they are running only the failed test. Okay? Because in order to improve the success, and the golden run running all the tests again. So we have... three cycles in a release. Yes. So yeah so usually the cost freeze is not aligned with the golden run. It's a bit before in phase two because we didn't make a pass two because we wanted to stabilize to improve the success rate. So usually here the success rate is okay. Here it's very low and then it's back up to 96 percent. We are aiming to... for 96, 97% success rate.

[00:12:48.31]  Jason ValleryDo we have a document that describes each one of these milestone steps and what happens in between each one? Like, is this written down anywhere and something that I can consume? Or is it just kind of knowledge, so to speak?

[00:13:00.42]   RemoteI think it's trial knowledge, unless somebody is writing. I didn't write anything.

[00:13:04.80]  Jason ValleryGot it. You know, I was just kind of trying to track it in my head. ahead and seeing a bunch of different nuance around how this will happen and play out. So I want to make sure I'm following you.

[00:13:14.52]   RemoteOK.

[00:13:16.44]  Jason VallerySo how much of this overlaps between releases? So my assumption would be that 5.6 planning is happening concurrently with earlier phase gates in 5.5. How does that happen?

[00:13:28.42]   RemoteSo usually-- let's see. so so if we going back to 5/4 okay this is 5/4 okay 5/4 had one phase gate I think it was somewhere 5/5 okay this is what 5/4 usually here I think phase gate 1 so when

[00:13:51.05]  Jason ValleryYou're heading three in the pre... release, the next release you're probably hitting phase 1 at that same milestone.

[00:13:59.32]   RemoteYes, exactly. Yes, but we need to be better because 5/6th, for example, phase gate 1, if you notice, is in two weeks from now, 5/6th, and we are not even close of 5/5. This is 5/5 and this is 5/6. So usually in Cospreys of 5/5 we need to do a face date of 5/6. Yes, but we are, but it's not a, it's not a stone. It's not written in stone.

[00:14:35.22]  Jason ValleryHow much overlap are the dead? that are focused on you know costing and architecture between the different releases like can you partition that work out such that you're not distracting the devs that are trying to get to code freeze with asking questions to go plan the next release like how much so usually what yes so you're right

[00:14:56.41]   Remoteso usually in code freeze we are starting working on the the next release, so around here, okay? Developers, we count, like we mark, we mark developers that are out of 5.4 and doing 5.5. We mark, especially the anchor feature. Most of the feature are not, but it cost me something like that. We release developers. we mark them as the next release and they are working on the next release because 5.4 it was released last week okay and then we have already almost feature freeze in 5.5 so that's the overlap usually around this code freeze people are going out it depends by the way because it's a It's very storage, it's very heavy features, like feature, you can write feature for a year, you know, like Sync, I think Ripple was written for a year, you know, support me like series v3 a new hardware. It's a year project. Yeah, but you use your anchor feature is roughly around a quad of the current release, we pull out people to work on the code for the next release.

[00:16:21.55]  Jason ValleryAnd then to that point of these multi-release cadence features, these big rock features, how do those get planned? Are they out of the release planning process? I assume because if it's a year or longer feature, you don't necessarily know which release.

[00:16:33.94]   RemoteNot here you're usually like it so that's why we have a alternate two release managers like for example Orly worked on 5.4 so and Roy took 5.5 okay now 5.4 is out Orly is working on 5.5 and Orly took 5.6 so we have two parallel people working on the releases okay so Orly now is focusing on planning 5.6 to see what is going in and out. what and Ory focusing on execution of it, like to get to reach to code freeze now, sorry not code freeze, feature freeze now in 5.5. So Ory is aiming for feature freeze in 5.5, okay, and Orly

[00:17:08.08]  Jason Valleryis doing the planning for 5.6. I guess what I'm asking is are there features that are in flight you don't actually know which release it's going to land in because it's going to take such a long time. You don't want to commit it to a specific release.

[00:17:23.39]   Remote- Yes. So usually it's like a very new hardware, like a completely new Rack Series V3. It's like a few, it's almost a year project. So you really don't know where it is landing. Yeah, but I. I do not know if we have such a thing in the software right now. I'm not familiar if we have a long plan, but we do. We had before. Because I'm focused a lot on execution, I'm less into planning now.

[00:17:54.37]  Jason ValleryYeah.

[00:17:54.82]   RemoteI used to be. Now it's like... Because now, for example, I'm getting to hardware. I'm doing the NPI from the development side. So you'll see everything that is like, has no ownership. So, okay, let us do it.

[00:18:10.69]  Jason Vallery- Got it, got it. So Noah and you all, you kind of described them more as product managers. I have a meeting with you all. you know how do how do they are they taking like and writing down a requirement stock and just handing that over during phase 1. Like where do they.

[00:18:31.44]   Remote>> JOLYNN BERGE: So we have so yeah so they have a requirement documentation that the architects are writing. Like they are doing the high level and we have architects Staff Levy by the way is doing the lower lower level FRDs. OK. We have. of FRD. PRD is after FRD.

[00:18:50.23]  Jason ValleryAnd so you mentioned, like, it's internal product versus external product. Is that primarily, like, just housekeeping kind of features? How do you define--

[00:19:01.59]   RemoteSo wait-- that's my kid here, so-- Come to say hi, Avi. Hi.

[00:19:11.06]  Jason ValleryOh, hey, buddy. Nice to meet you.LAUGHS How's it going? How are you doing? Hi.LAUGHS

[00:19:21.51]   RemoteINAUDIBLE So I'm describing as an intern. It's not their title, OK? It's not their title. anyone because the Tomer is the head of product and everything but just to explain to you today so what happened is that Noah I think is doing the feature to get the list I'm guessing from Tomer because Tomer is talking with customers so I think they get the input from them Shachar also talk a lot with customers a lot Yeah, it's very involved also in support and we have the backlog what is described as a tech depth or Minors we put it back. So Trident also has a list that they aiming like for now they are planning five Okay, so we're released 5.4 and already Planning the 5.4.1 the minor of 5.4.1 and we will release 5.4.2 risks for so we have like a bucket he has like a bucket of requests usually from customers and we get the the right priority not always but we try to understand the heat of the temperature of the customer the size of the deal it's very it has a major impact on the decision of course and then we really build it, building blocks.

[00:20:40.95]  Jason Vallery- So at phase gate one, when you're making the decisions around what's going to be in the release and what's out, I would assume you've gone through some sort of costing exercise that says, this feature is going to take so many dev weeks. This feature is going to take this many dev weeks. You've kind of figured out.

[00:20:56.00]   Remote- Yeah, yeah, we are doing that. Yeah, but I'm not sure that we present it. sure that in the face that we present it I think it's something internally that we are doing internally to see the sizes and we report what we can do and what it stretch okay we usually gave you the anchor features we understand that it's important it will happen and then we have stretch features I shared I can share with you the like for five more if you want maybe that will be the easiest you to get it. Yeah, 'cause if I for we had had all the phases so I can share with you

[00:21:29.83]  Jason ValleryLike five for that would be good. We would have done this at Microsoft is that that phase we would have called it, you know, a tough cuts investments at a glance review and ultimately that would sit with leadership to kind of look at. Here's what's in. Here's what's out. stack ranked it this way who's who's kind of presenting and reviewing and making those decisions at that milestone is there usually it's had ahead of time

[00:21:56.92]   RemoteLike it's usually a Jason Valerie right yes that's me yeah Wait, I'm just sending you the, wait, I'm giving you the share, okay, give me one minute. So, you're asking how to impact features.

[00:22:30.70]  Jason ValleryI'm just kind of looking at who's making the tough decisions, right? Because you're inevitably going to be at a milestone there where there's things that you really want to do, but you don't have to have resources for once costing is kind of in place. Who's setting the stack rank set of priorities and

[00:22:46.02]   RemoteDeciding what's in and out and kind of really- >> So, usually it's a development, Like, it's Shachar with the product, product present at the pressure or the need, you know, but eventually if it's a must, it's a must. We will do that. But usually it's Shachar, if it's something complicated, like you described, it's usually Shachar getting into involved, because usually we managed, like we understand. that the concern if like product if Tomer come to us and say listen we have like five customers that want that so we will make it happen. So we usually we are trying to to um trying to align with the field. By the way I never saw a development that is very field oriented like that okay. Yeah yeah. Very field-oriented, yes. If we come-- by the way, for example, now with Tesla-- OK, that's it. I sent you all the four for 5.4, for example. For example, Tesla-- Tesla has a huge deal now. We are doing everything we can to meet their requirements. So we basically-- they are in production in 5.4. 4, 5, 4 was released one month before. If you have a huge deal, we are doing everything we can. We decide which release is going and make it happen. So what happened with Tesla, we delivered three milestones and we have two more to go. So what we did, we split it. We had a feature that was not in the list for 5, 4, we start working on it, and we delivered already three milestones, and we have two more to go.

[00:24:27.68]  Jason ValleryWho's looking, I mean, I guess this is Asaf, and I can take this to him, but who's trying to do this in a little bit more thematic way? You know, what I got from Tomer and what I'm hearing from you is it is very much customer A wants feature X and will prioritize doing that. But then you kind of end up in a state, in my experience, where customers are really just defining the shape of your product, and then you get a very complicated product surface. So is there anyone like taking a look at, we've got a set of requirements that are in a particular area, I don't know, make it up, like security or authentication or whatever. How do we architect that in a way that meets all of the customer requirements, and sort piece of way. Is there anybody, is that a soft team, like who's doing it?

[00:25:11.70]   RemoteYes, yes, that's a soft team, yeah. They have very strong people there, a lot of strong people there. So for example, a database, Gordon, Eyal Gordon, is database oriented. They are meeting customers, they are meeting, they are talking, they have wiki pages per requirement of customers and then they are trying to do something that meets a lot of them the needs. A lot of time by the way what they are saying eventually it's not what they happen and we are changing during time but we are doing a lot of customer work ahead of time to decide on the relevant architect. We're doing that. are doing that's a staff team completely like a high level like they are talking Tom and Noah title they're talking high level and then we it's come to design it's a stuff got it and it's happened it happened that we have need to change stuff or happen a lot got it well

[00:26:11.94]  Jason ValleryThis was super helpful uh it's the first kind of opportunity i've seen see the different release gates. Yeah, I don't know if there's any other sort of reviews of documentation or other milestones, like how do you, actually let me say, you've got these phase gate meetings that I've been invited to, is there like a planning dashboard, like Qanban boards,

[00:26:32.40]   RemoteLike is it all in Gmail? So we have, it depends how much we have. have wiki page so it's called five five status by four status you have that's the wiki page you want for five five or share with you yeah but then like the release manager when they are drilled down you'll find it or you want me to

[00:26:54.34]  Jason VallerySend you the link for example um yeah I mean I just got the ones you sent me I'll have to go and like to organize but yeah I just I guess is there like oh is the wiki page of the status at a glance and is there like weekly rhythm of business and tracking around the status or how does that all work?

[00:27:09.57]   RemoteSo yes we have internal uh oh we have a lot uh so this is the so we have wiki page per release I

[00:27:18.85]  Jason ValleryCan show you like take for example, and do you have like sub pages for each milestone? or in each sub-release.

[00:27:25.04]   Remote- So there is the high level of who is the architect. You see QA DevOwner, we have all this data here.

[00:27:31.50]  Jason Vallery- Yeah, yeah.

[00:27:32.29]   Remote- By those, the date, okay, and then they have Gantz, I think now it's in Excel, or Rui, too, if you want in 5.5, you can share it with you if you want. as a gant. I see. Yeah, on top of that we have QA. Okay, QA has their own tool that's called Q-test. Yeah, this is the Q-test. They are doing, usually they are like one or two legs behind. development. You see, so 5.5, so you have the test, you see, you have here, for example, phase one, look, we have 21,000 tests, okay? Yes, so we just, they are just building it, 5.5, they are just building, you see, phase one, Phase 2 and Golden Run. Usually, we have Staffs Phase 1, adding all the relevant tests, the planning-- that's the planning, basically, of UA, and then we have weekly meetings internally with the stakeholders. Then going over, we have slides. That's also in my team that we are-- for example, I do not know if we have-- and let's see if we have released it for example that was last week but we have a presentation that we are doing every week it depends on what's what's going on so you see we are going over the date it's just the end of the release the documentation, I'm also monitoring the documentation, the beta, see, the hardware status and it's QA, you see, success rate, the potential rate, the feature that are problematic, we are talking about it, okay, that's internally, once a week we are doing that in the development.

[00:29:34.76]  Jason ValleryBut that milestone, like if there's some problematic feature. You may move forward with a release and then push a given feature to the next release. Does that happen?

[00:29:43.75]   RemoteYeah, that's called change management. That's what I told you. Yes, that's called change management. Yeah

[00:29:49.27]  Jason ValleryWell, I appreciate the time. Obviously, there's a lot more for me to learn. I'm a weekend So this was this is the best review I've had so far of the process. So I really appreciate you walking me through this next week we can do another one if you want. Yeah, I'll reach out. I'm gonna be in Tel Aviv actually, I think the 23rd through 26th of November so we'll find some time face-to-face as well and we'll kind of, they're a little bit more on the process. So you're joining the, so you're part of Tomer's team? I'm reporting to Jeff, I'm focused on on cloud product. We're kind of figuring out organizational things still, but yeah.

[00:30:27.17]   Remote- Oh, okay. 'Cause cloud, also, it's a...

[00:30:31.79]  Jason Vallery- It's a whole separate thing.

[00:30:33.71]   Remote- No, they are part of release. Everything that is not part of release is not good for us. It's like, it's 'cause then it's a fluid, you know? Like, we have all the client, you know, the Terraform and the... all the clients, the plugins that we are doing. So that's, they are not part of the release, and then it's like, okay, whatever they were already, they are releasing it, and it's not, it's not, I think everybody has to stay, they have the same stops, stop sign, stop bus, how do you call the bus stops?

[00:31:04.61]  Jason Vallery- And what I'll say is like, as we evolve the product for the client. Cloud, there's a lot of stuff that will sit outside of Yancey's team that will go into the core product itself for data offload and some of the networking things and how data structures will be stored. So I imagine a lot of the work that my team will drive will be pushed into the core product versus pushed into the control plane that Yancey and team are building. So we're going to work together quite a bit.

[00:31:30.61]   RemoteYeah, yeah, but I think it will be, if you are pushing the product, it will be more of like NOAA, TriTel, ASAF, you'll probably talk a lot with ASAF, because we do that, like Tabular, for example, database, also Bok, by the way, all the clouds, they are part and release, so we have regression for it, we have QA for it, we have like, it's a part of R&D, part of Shachar's team that's working on it. So we have the core, but now we have a lot of, basically we want to be a one-stop shop, right? So now we're developing the database of our own, so they are part of Relief, they have their own content, but it's also part of the Relief. They need to meet the criteria, the success rate, and everything. Yeah. the AWS Cloud that we did and GCP. They are part, completely part, yeah.

[00:32:23.30]  Jason Vallery>> I appreciate the time, Niraz. We'll talk soon. Thank you.

[00:32:27.56]   Remote>> Bye-bye.

[00:32:28.38]  Jason Vallery>> Bye.
```

<!-- ai:transcript:end -->
