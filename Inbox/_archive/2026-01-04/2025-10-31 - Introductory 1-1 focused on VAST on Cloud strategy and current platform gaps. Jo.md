---
entities:
  people:
  - '[[Josh Wentzell]]'
type: transcript
source_type: unknown
date: '2025-10-31'
---

# 1:1 — Josh Wentzell — 2025-10-31

> [!info] Purpose
> Build trust, surface and remove blockers, align on priorities, coach & grow.

## Summary

Introductory 1-1 focused on VAST on Cloud strategy and current platform gaps. Josh outlined multi-tenancy API/GUI limitations, VOC deployment friction, and automation tooling gaps (Terraform coverage, no official Ansible). He noted strong CSI adoption and increasing CoSy interest. Jason shared priorities: marketplace offers across clouds, improving price/performance via cloud primitives and potential ODM hardware in CSP DCs, and enabling a multi-cloud data space for durable, globally distributed access to large data lakes. Josh sent the loopback OVA link; Jason will get hands-on and attend Tech Summit.

## Key facts learned

- Josh’s role: automation/DevOps and lab tooling; customer-facing API automation; previously handled AWS VOC until Carl joined.
- Multi-tenancy gaps: unclear tenant-scoped APIs, tenant admin lacks needed privileges, limited tenant visibility (e.g., VIP pool selection/filters).
- VOC deployment is not streamlined; lacks preflight checks/wizard; failures can occur late in the process.
- Automation usage: large customers prefer Terraform/Ansible; direct REST used when Terraform lacks coverage, causing state-management pain.
- No official Ansible module; a beta exists but is not maintained; the Do team prioritizes Terraform provider maturity.
- CSI adoption is common; CoSy requests have increased recently; Rob Gerard manages CSI/CoSy.
- Customers often build internal front-ends for buckets, policies, and S3 key rotation to enforce approvals and guardrails.
- Jason’s 12‑month focus: cloud marketplace offers, price/performance via cloud primitives and ODM hardware in CSPs, and multi-region/multi-cloud data spaces to move data efficiently to GPUs.
- Loopback OVA can be spun up via AWX/Cosmodrome in OCI; Josh sent the link.

## Outcomes

- Introductions and alignment on VAST on Cloud pain points and priorities.
- Loopback OVA link shared for Jason’s hands-on work.
- Agreement to share further feedback on VOC and multi-tenancy gaps.

## Decisions

- (none)

## Action items (for Josh Wentzell)

- [x] Spin up OVA in home lab and/or loopback instance to get hands-on with VAST @Jason Vallery 🔼 ✅ 2025-11-08
- [x] Review flight school materials and attend Tech Summit @Jason Vallery 🔼 ✅ 2025-11-08
- [x] Share additional learning links/docs as needed (loopback link sent) @Josh Wentzell 🔽 ✅ 2025-11-08
- [x] Engage with Rob Gerard to align on CSI/CoSy status and roadmap @Jason Vallery 🔼 ✅ 2025-11-08
- [x] Connect with Carl on VAST on Cloud deployment nuances @Jason Vallery 🔽 ✅ 2025-11-08
- [x] Define and implement tenant admin capabilities and tenant-scoped visibility (e.g., VIP pools); clarify tenant APIs @VAST Product/Engineering ⏫ ✅ 2025-11-08
- [x] Add VOC deployment preflight checks and a guided wizard to prevent late failures @VAST Product/Engineering ⏫ ✅ 2025-11-08
- [x] Expand Terraform provider to cover missing endpoints to avoid REST fallbacks @Do team ⏫ ✅ 2025-11-08
- [x] Evaluate plan and resourcing for an official Ansible collection once Terraform stabilizes @Do team 🔼 ✅ 2025-11-08

## Follow-ups

- [x] Confirm Jason received and used the loopback link; share any additional setup tips @Josh Wentzell 🔽 ✅ 2025-11-08
- [x] Report initial findings from OVA hands-on and list of VOC pain points @Jason Vallery 🔼 ✅ 2025-11-08
- [x] Provide timeline for Terraform provider parity and decision on official Ansible module @Do team 🔼 ✅ 2025-11-08
- [x] Clarify CSI vs. CoSy adoption patterns and any gaps to address @Rob Gerard 🔼 ✅ 2025-11-08
- [x] Share marketplace offer plan and timelines across AWS/Azure/GCP with stakeholders @Jason Vallery 🔼 ✅ 2025-11-08

## Risks

- Multi-tenancy limitations may block a true SaaS, multi-tenant cloud offering.
- VOC deployment complexity can stall customer adoption.
- Incomplete Terraform coverage and lack of an official Ansible module hinder automation at scale.
- Tenant admins requiring cluster admin intervention reduces autonomy and increases operational load.
- Marketplace VM shapes may yield poor price/performance for VAST.

## Open questions

- What is the timeline to close Terraform provider gaps to avoid REST fallbacks?
- Will VAST fund and own an official Ansible collection, and when?
- When will tenant admin permissions and tenant-scoped visibility (e.g., VIP pools) be addressed?
- What is the plan and ETA for VOC deployment preflight checks and a guided wizard?
- How strong is CoSy demand across customers, and what is the roadmap for VAST’s CoSy support?
- What is the schedule for marketplace offers across AWS/Azure/GCP, and how will price/performance be addressed?
- How will data spaces deliver multi-region durability and efficient data mobility across CSPs and on-prem?

> Next meeting (if any): (none)

---

<!-- ai:transcript:start -->

## Transcript (auto)

```text
[00:00:00.04]  Jason ValleryI don't have a camera ready I'm good how are you worries yeah I'm good I wonder why I reached out thought it would be good to introduce myself and I heard your name from a few folks So I just started last week reporting to Jeff looking at cloud and what it means to get Vast on cloud. It came from Microsoft, been running Microsoft object storage for the last 13 years and so you know this is a fun journey for me to kind of step into Vast and you know I was reaching out and talking to various folks and I said, "Where do I learn about VAST in the most hands-on way?" And I'm a very hands-on kind of learner and a deep technical guy and everybody said, "You're the one to talk to about the OVA." And I had a good chat with Andy yesterday and he kind of gave me a bunch of advice, so maybe I don't have as many questions for you, but I still thought I'd say hello and get to know you. yeah okay sounds good so why don't you tell me about yourself what do you uh what do you do at vast what are your uh great what do you do i do it fast yeah um i do a lot of things at vast

[00:01:21.62]   RemoteYeah um so i think what they hired me on for three years ago was kind of a lab manager And what that meant at the time was maintaining lab environments, working with ops teams for rotating out systems. As you may or may not know, we don't own any of the hardware that we run in the labs. It's on kind of a burn-in period from our manufacturers. So I worked with -- so, well, let me back up a little bit. So prior to that, I was an automations engineer or DevOps engineer, and so what I came in to kind of do is try to fix a lot of the way we were doing things in the lab. A lot of it was, all of it was manual. There was no automated pipelines in place. for building out systems, maintaining systems, et cetera. So that's a lot of what I did when I first came on was just, you know, getting a handle of things, wrangling it into something more manageable. Back then it was maybe 50 to 75 SEs, whereas now we're a couple hundred. a few hundred. So it was more maintainable back then to have something that we did ad hoc, but as we grew, it didn't scale. So I worked on building out systems to make that a little, a little better. But what I actually prefer to do is real automations type work, DevOps type work. So I've been doing a lot of that type of work with customers, specifically anytime they need to interface with our API and they want to add us into their automation platforms. I typically am the one that gets on calls with these customers and walks through what they're doing, what they want to do, and kind of give them a workflow do it best with VAST. So that's a lot of what I do on the customer facing side, as well as also as well as prior to Carl coming on, I did most of the AWS, VOC, VAST on cloud discussions. I'm not doing those so much anymore now that Carl's around. So I'm thankful for that because that could take up. lot of time sometimes. But and then a lot of also just what I'm working on is I built a lot of tools, dev tools, ways for us to interact with the systems, way for SEs to interact with the systems and building out just various different workflows and demos so that We can enable our sales teams to be able to showcase our environments a lot easier and make it more producible and, again, automated so that there's less work for SEs that aren't as tech savvy, if you will.

[00:04:25.64]  Jason ValleryMakes sense. Well, maybe instead of asking you all about the lab and you'll be good to go. since Andy gave me such a good brain dump yesterday. I'll ask you a little more on the Vast on Cloud side. So my charter and goals is to make Vast on Cloud a huge success, and the vision that Jeff and Yancey and others have shared with me is really to get to the point where we are fully multi-tenant at SAS, running in a Vast on tenant in all of the hyperscale. and manage everything for the customer in that way. So clearly you've got a lot of experience with the current set of capabilities that the BaaS API provides, Terraform automation, all of those things. I mean, what's your, like, if you had to say where are the biggest pain points, gaps in the platform as it exists today, challenges with getting from where we're at to that vision, say they are.

[00:05:16.28]   RemoteFast on cloud specifically?

[00:05:18.29]  Jason ValleryWell, like vast multi-tenanted stats, like the true Holy Grail of fast on cloud, where everything is abstracted away from the customer and all we're doing is exposing an end point into the customer's cloud tenant.

[00:05:31.71]   RemoteI see.

[00:05:32.23]  Jason ValleryIn that world, like, I mean, I'm already running into various feature gaps and multi-tenancy gaps that I've. learned about in my first, you know, week and a half here or two weeks here, but you know, clearly you understand the API service, how it all works, you know, automation, so you must be thinking about the same problem. What are the pain

[00:05:50.64]   RemotePoints of VaST today? So, I guess I'll speak specifically to multi-tenancy. Just since, so I haven't been super involved in our multi-tenancy as of late, well, until as of late, because we've recently started introducing multi-tenants on our lab systems to break it up into different regions so that that way not every SE and every group of SEs are hitting the same endpoint, and now we can kind of track who does things on systems, who's breaking things, and then when it comes specifically to the API, it's kind of hard to, it's not intuitive right now as to when you're managing the tenant to be able to do API calls against that tenant. So that's, that's one thing. One, obviously better documentation on that and then maybe just. better APIs directly to multi-tenancy. So, and then that comes along even in the GUI, whenever you have an admin who is managing something multi-tenancy, if you are a tenant admin, there still seems to be gaps, I think at least, in what... what you should be able to manage as a tenant admin, as opposed to just a cluster admin, and I think that's gonna come to be something that might be an issue in the cloud whenever we are trying to be actual tenant provider to people. I think companies like CoreWeave and stuff are gonna see that relatively soon since they are big in doing that currently with fast. Well, they might not see it as much since I think they're managing everything, but if we get to the point where we have, let's take it out of the cloud for a minute, just companies that are doing tenant admins for their organization, I just think there's a lot of areas where they still need to reach out to the cluster admin. when I think it could be done by the tenant. Even seeing things such as what VIP pools are available to your tenant, that's not easily able to be seen right now, and then maybe they're not showing it because they don't have a filter for how to show just that tenant as opposed to everything. I think you can see it if you go and create a view and pick what pool you want to use for that. Those are just nitpicks in my mind, and then as far as Fast on Cloud, the virtual instance deployment of it isn't very straightforward. Like, I've sat on calls for an hour plus. with customers when we were early days AWS maybe it's better now it's been a while since I've stood one up and we don't really have any type of wizard if you will for somebody who's doing it in a GUI who would where it could really walk them through and make sure they have things set up and they may think they have things set up right and then they start start to deployment of it and it'll fail 50 minutes into it when it's a check it could have done in the first five minutes see if proper networking was set up so there's just things like that that aren't streamlined so those are kind of things I've had a lot of people who've wanted to use fast on cloud but were unable to just because of the new nuances with it and difficulty with it, and it wasn't always, it's not scalable again for, at the time, it was just me getting on calls with customers doing VOC installs and VOC troubleshooting. So yeah, I think just tightening up those type of installs, again, this is, I think this is outside of what you were asking about, but we do have use cases. where people would want just their own DOC instance in the cloud as opposed to it being managed by their provider, and so, yeah, I just think there are some issues with actual deployment.

[00:09:59.25]  Jason Vallery- Do we have a lot of customers that use the VAST management APIs directly?

[00:10:07.67]   Remote- I'd say the, maybe not the majority. I'd say most, especially ones we're getting into these really big multimillion dollar deals, they're multi-clusters. They're all managing via Terraform or Ansible. Ansible, we don't have a module for it, an official module for it, so. Everybody's just writing their own custom modules using just the REST API with Ansible, and then our Terraform's not fully fledged out yet either. There's things we can't do in Terraform that we have to revert back to using the API. So then it becomes a pain mixing in those technologies because you'd want to ideally do everything. everything with Terraform, or everything with Ansible, and not have to do this bit with a straight REST API call, and then this with Terraform, because then you lose the state management that you get with Terraform whenever you have to revert to using APIs for certain things. So yeah, in that area, there are things where, we're lacking again in what we're doing with with our APIs or in this case Terraform specifically where it's keeping customers from being able to go

[00:11:26.75]  Jason ValleryAll in on that. What are the scenarios where they use Ansible and Terraform versus like the CSI driver?

[00:11:38.92]   RemoteUm, well, so this would be where CSI driver is going to be going to be something separate. So say, for example, Tesla was somebody I recently worked with. They give their end users the ability on their previous platforms to be able to create their own buckets, get a bucket policies, things like that, and they do that. in their own custom front end that they give access to end users. So that way the end users don't get direct access to NetApp or Vast or whatever. They have a GUI in front of that, maybe like on their intranet that they go to and they can log in. It obviously has their username and everything already. set of boundaries for them as to what they can create, how big they can create, et cetera, without it going through any type of approval processes, and so that's a way that a lot of customers, and I was actually a customer before I joined VAST. So I did some of this stuff as well. A customer of VAST where we would just, removed things that we would want end users to be able to do. S3 key rotation was again one of those things. I wrote a front-end so that users could log in, see what their key was, rotate it out whenever they needed to, create new ones, etc. So these are all different ways where Companies are giving some autonomy to their employees or their department heads, where they are then leveraging APIs from their DevOps team or whoever that wrote these front-end or tools so that they can interface with VaST without being actual admins of VaST. that's probably the biggest thing other than just straight up provisioning of the clusters, so anytime they have a new view, new department, etc., you know, they're ideally going to want to do that with some type of code as opposed to logging into a frontend, so then that way it's reproducible very easily, obviously.

[00:13:52.74]  Jason ValleryI can imagine like the most sophisticated customers have good use cases for this, particularly if they're like, you know, CoreWeave or your example of XAI where they've got multiple different providers and different solutions and they're trying to aggregate them into

[00:14:04.75]   RemoteOne place.

[00:14:05.72]  Jason ValleryMy experience isn't that, but that isn't a common customer scenario. Is it, is it happening because we don't have good enough? or granular enough roles and access controls in terms of who can do what within our interfaces, or like, is that kind of just a one-off use case that you're seeing at XAML? Like, are there others that are abstracting and creating their own front-ends?

[00:14:31.01]   RemoteWell, I think there are actually quite a few that are doing it, maybe not quite to the level that like XAI and Tesla, et cetera, doing. But like, for example, my old company, StillVast Customer, they do everything with Terraform or APIs, other than very basic maintenance on the clusters. They're trying to do everything with Terraform, just because that's their-- protocol. We were always an infrastructure as code first company. So in that way, it was mainly for checks and balances. So we'd write our code, we'd submit a PR, somebody would have to prove that PR before it would go into the system. Whereas if we just gave somebody free range, just be able to log into VMS, they could make that change without any checks and balances and approvals. So a lot of times it's really based on that as well, just to make sure somebody doesn't screw up the system without other eyes at least on it.

[00:15:33.33]  Jason ValleryI guess, and I'm just kind of running this through my head real time here, for me I would think automation, Terraform, Ansible, whatever you're going to use, would come into play. play when you're talking about the life cycle of a resource like a bucket or share volume or whatever, and the provisioning and deprovisioning of that, and so that totally makes sense for me why you'd want to automate that as part of the life cycle of your deployment. But I'm more on the lens of like cluster configuration and setup and management. being very different use cases, do you see primarily it being around the life cycle of a given bucket share volume, or is it more on the management of the actual vast cluster that you see automation happening?

[00:16:25.79]   RemoteBoth, and I'll pay Y for the configuration. of it. So it's not just going to be a one-time stand-up and the cluster's done. If you're expanding and you want cluster B in San Francisco data center to be the same as cluster A in Ashburn, Virginia, if you already have the code written for Ashburn, you can just change a couple names on the on the code and push it Cluster B and now it's essentially the same exact cluster, just different named, and without having to really sit and work at it for days. Like for example, when I do these rotations of clusters in the lab, whenever it was a manual thing, it was a few hour process, and now whenever we do rotation, I just fire off my job gets the cluster ready in about a half hour for me, and then SEs are able to use it again. Now that's a very edge case 'cause our customers aren't rotating systems like that, but we do have customers who they may have a dev cluster where they are building it up to tear it down, build it up, tear it down for, you know, seeing how they would test against it. instead of going to their prod system and then they can easily rebuild that system or reapply the configurations to it without it being a tedious process whenever it's something in code they can just run whatever job it is. Settle up, redact it, etc. - Yeah, I'd say it's a lot of both scenarios, and whenever I'm doing automation for what we are doing in the labs, it's the same thing. It's the configuration of it and maintaining.

[00:18:16.03]  Jason Vallery- On the other side of it, the volume creation share. creation. Are customers adopting Cozy and CSI? I mean, I can tell you on the Microsoft site that adoption, particularly of Cozy, was basically non-existent. CSI was being used primarily because it was being pushed heavily by our Kubernetes team. What's that look like here? Do customers

[00:18:37.31]   RemoteLeverage it? Oh yeah, for sure. The guy to talk to that about, and I think he's paternity leave would be Rob Gerard. He's our CSI Project Manager, Program Manager. He's also part of my team, the OCTO team. He's who is pretty much always on all those calls. Like I know, I think it was Lowe's or maybe Walmart or both. That was one of the big things that we need. to overcome with them, and I think it was Cozy specifically, I think it might have been Flows, where we had to get that flushed out for them. But yeah, I think most of our customers are using CSI in one way or another. I know my company, and then my company split into two companies. They were both heavily relied on the CSI driver and that was a big thing whenever we came from Pure to Vast because we had to pay for it and it didn't come with Pure or Vast, we just got it. So yeah, I'd say most customers, if any customer is doing any type of pod work in Kubernetes, they're leveraging our CSI driver.

[00:19:57.21]  Jason ValleryYeah, CSI is pretty common on Microsoft. It's the CoSy side that I've seen very little adoption on. Interesting.

[00:20:05.18]   RemoteYeah, and CoSy I've only seen recently here. I don't know if we just weren't doing it. This would be a Rob question again, since I'm kind of it, but I have been seeing it more commonly requested in the last, I'd say, two to three months.

[00:20:23.97]  Jason ValleryWhat's the status of that we don't have any Ansible, is somebody building one?

[00:20:30.57]   RemoteI built one, but I'm only one person, so I can't maintain it very well. I've had a couple of customers who are okay with-- trying using a beta application, and they've used it and they like it, but we really, I think it's mainly, we have one team, it's called the Do team, and they're the ones who maintain the Terraform provider, and I think the idea is likely going to be once they feel like they've got the Terraform provider in a good enough place where it's going to be just minor improvements here and there, where as opposed to they are not rebuilding, but they're really restructuring the Terraform provider often enough where I think they need most of their cycles on that, but once it's to a place where it's managing all the endpoints that people requesting, 'cause like I mentioned, there's plenty of endpoints where we can't manage with Terraform yet where we should be. But once they have that wrapped up, then I think, 'cause there have been enough Ansible requests where I think we have justification for it. But yeah, I think it's mainly just manpower and... the amount of requests for it. I think Terraform won out in the amount of requests as opposed to Ansible.

[00:21:51.51]  Jason ValleryYeah. Well, look, I appreciate the time. I don't have any other questions. I'm trying to learn as much as I can. If there's any suggestions you have on where I can learn more, I'd appreciate any links or documentation. Personally, I'm planning on spinning up the OVIM. my home lab and trying to kick the tires on that thing and try to get a little more hands-on with the product, learn where all the pain points are. So that's

[00:22:16.69]   RemoteKind of where I'm at in my journey. Cool. Have you seen the loopback cluster in, I think they spin it up in OCI. You can do it. Were you on that, were you on any, or have you had any... what do they call them, flight school sessions?

[00:22:33.00]  Jason ValleryI don't know if you're going to have to go through that. - No, I mean, I've got the links. I haven't gone through them all yet. I've got, and I'm also going to Tech Summit. I'm hoping to learn a lot more there. So, yeah, that's kind of what I'm doing.

[00:22:42.39]   Remote- Okay. So the loopback cluster is the OVA that you can spin up via AWX, or Cosmodrome is what they call it here, you can get a cloud hosted version of it not fast on cloud but the actual OVA spun up as an instance in OCI so that way you can spin them up spin up whatever release you wanted to and test against it as well as your home lab if you wanted to do that as well just so you could get it spun up quicker you can would help me get to that, I would appreciate it. Yeah, yeah I'll find it and uh shoot it,

[00:23:20.15]  Jason VallerySlack it over to you here in a minute. Well thank you. Uh, any uh thing you want to know from me? What can I tell you about Microsoft's object storage platform that you're curious about,

[00:23:31.42]   Remoteor anything like that? That's what I know. Uh, well, okay, I guess. - I guess it's more on the vast side. What's your goals here in the next, like, I don't know, this feels like I'm interviewing you, but like six months to a year, what do you kind of see us doing in the clouds?

[00:23:52.87]  Jason Vallery- Well, I mean, there's a bunch of things that have to happen in parallel. First priority is getting marketplace offers out and automated. for all of the hyperscalers, Amazon, Google, like that's pretty one, and that gets a whole lot of other side tasks kick off as part of that, like rethinking business models, pricing models, support structures, you know, compliance, networking challenges, all kinds of different things spin up as a result of that. But the problem with the marketplace... as I'm sure you're aware, they run on VMs that are the wrong shape for what VAST needs to be price performant, and so then the next phase, how do we get a price performant offering into the clouds? And there's two dimensions of solving that. One is leveraging cloud primitives in a more efficient way, meaning being able to offload capacity to native object storages from the various providers, and then two is actually even pushing on to the CSPs the idea that we can leverage ODM hardware, but be able to deploy it into their data centers. So I think both of those would be in flight. Then layering on top of that, my vision is certainly how do we get to a world where data spaces enables customers to exist in a multi-cloud way across hyperscalers, but also then connect Neo clouds, connecting back on-prem, connecting back even into, you know, one common data space across the planet, right? Because one of the things that really, the only hyperscaler that has this today is Google with our multi-region storage. Amazon and Google, or sorry, Amazon and particularly Microsoft struggle here, and so I think customers are very interested in a multi-region. region storage class that ensures durability and then brings the data to wherever their compute is. There's a lot to do there. I could go into details like Rem because I owned the storage relationship with OpenAI for Microsoft for many years and their architecture is very much like big central data lakes and then they get GPU from the planet so they need to be able to sort of real-time bring data to the GPUs and I think data space is a unique capability here so putting all of those puzzle pieces together into a much more competitive offering would be the goal for I would say 12 months. Okay yeah it's good to

[00:26:09.89]   RemoteKnow just what what people are working on whenever they come we're hiring so many people these days we're in new positions so so it's nice to hear what the plan is.

[00:26:19.59]  Jason Vallery>> Yeah, certainly the thing that I'm most excited about, becoming a common data platform across clouds, Neo clouds, on-prem, and being able to efficiently move data between where central data lakes exist in the clouds, 'cause you're talking about like many, many exabytes of data that you're not going to really repatriate. just not a viable path in most cases, but then being able to efficiently stream that data to wherever the GPUs are on the planet, which are going to be all over the place. So that's the core underlying problem for the scale AI systems. Okay. Yeah, cool. Well, look, thanks for your time, If you have any thoughts on Vast on Cloud, I'd love to hear 'em, and if you're on any pain points that you just think products should be aware of, bring 'em my way, and hopefully we get to work together more and I appreciate any of the learning links that you share.

[00:27:12.95]   Remote- Sounds good. I did just send you that loopback link for how to spin that up, and then if I don't talk to you, I'll see you at Tech Summit in a week or so.

[00:27:20.64]  Jason Vallery- Yeah, I look forward to it. See you, Josh.

[00:27:22.99]   Remote- Have a good one, bye.

[00:27:45.50]  Jason ValleryWe probably wouldn't compare this outside of an NDA, but it is something I would have historically shared with a customer under NDA.

[00:28:08.09]   Remote(silence) (keyboard clicking) (keyboard clicking) (keyboard clacking) (keyboard clacking) (keyboard clacking) YouBLANK You (silence) Hey folks. - That was good.

[00:31:49.29]  Jason Vallery- We're doing it.
```

<!-- ai:transcript:end -->
