---
type: people
title: Andy Bernstein
created: '2026-01-03'
last_contact: '2025-10-27'
auto_created: true
tags:
- type/people
- needs-review
---

# Andy Bernstein

## Contact Information

| Field | Value |
|-------|-------|
| **Role** |  |
| **Company** |  |
| **Department** | _Unknown_ |
| **Email** | _Unknown_ |
| **Phone** | _Unknown_ |
| **LinkedIn** | _Unknown_ |
| **Location** | _Unknown_ |

## Relationship

_How do you work with this person? What is your dynamic?_

## Background

_Career history, expertise, interests, personal details shared..._


## Projects

_What projects are you collaborating on with this person?_

```dataview
LIST
FROM "VAST/Projects" OR "Personal/Projects"
WHERE contains(file.outlinks, this.file.link)
```


## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed AND contains(text, "Andy Bernstein")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@AndyBernstein") AND !completed
SORT due ASC
```

## Key Facts

- OpenAI alignment session is deferred until OpenAI engages/commits.
- Cloud priority is Microsoft first; Google TPU partnership is viewed as a major opportunity.
- On-prem average utilization is ~30%; broad consumption pricing could reduce prepaid revenue and force difficult on-prem utilization conversations.
- Brett is anti-consumption pricing (especially on-prem) and is the ultimate vote on the model.
- Uniform pricing across cloud and on-prem is seen as advantageous for customer commitment regardless of deployment location.
- Tech Summit content is led by Rob Benoit (Global Sales Engineering).
- Travel/events: Tel Aviv trip planned (fly on the 21st), Tech Summit (Orlando), and Supercomputing with extensive meeting schedule; Jason to set a small-group with Nidhi.
- Lior has sell-to obligations including Microsoft AI research/MapFalcon engagement (~16,000 GPUs).
- Org changes moving people under Jason’s scope are imminent and sensitive.

## Topics Discussed

Cloud alignment and synthesized pipeline/requirements across major clouds, Microsoft prioritization and ROI narrative, Google TPU partnership strategy and competitive positioning vs Google first-party storage, OpenAI engagement timing and deferring alignment, Pricing/consumption model vs prepaid commitments; on-prem utilization risk, Org structure changes and meeting cadence/1:1s, Slack presence and internal channels (pre-sales, cloud deployment threads), Tech Summit content ownership and expectations, Supercomputing meeting planning and small-group with Nidhi, Tel Aviv agenda planning via Shachar

## Recent Context

- 2025-10-27: [[2025-10-27 - Jason and Jeff aligned on near-term focus synthesize a cloud pipeline view and]] - Weekly 1:1 between Jason Vallery and Jeff Denworth aligning near-term cloud priorities: build a synt... (via Jeff Denworth)

## Profile

**Relationship**: Internal collaborator

**Background**:
- Runs a CTO meeting rhythm; can advise which Slack channels/meetings to join; described as an amazing person and key guide to internal cadence.

## Key Decisions

- ✅ Do not run an OpenAI alignment session until OpenAI engages.
- ✅ Primary focus is Microsoft while simultaneously investing in a Google TPU strategy.
- ✅ Lior Genzel focuses on hyperscalers and also has sell-to obligations; Mordechai Blaunstein covers second-tier clouds.
- ✅ Pricing/consumption discussion must include Brett.

## Related Projects

- [[Cloud]]

## Related




---
*Last updated: *