---
layout: post
title:  "[Stand-ups][IPM][Sprints] Running Stand-up, Sprints and Iteration Planning Meetings"
---

## Stand-up

- 10.45-10.55 AM = Booking experience stream's stand-up
- 11.00-11.10 AM = Booking flexibility stream's stand-up
- Everyone including the PM talks about what they did the previous day, the plan for the current day, as well as blockers in their work
- Only in exceptional cases, the stand-up extends to talk about the blockers. And only the relevant people stay back
- If there is a longer meeting needed to close the blocker/open item, then a separate meeting is scheduled in the day

## IPM

I run weekly Iteration Planning Meetings (IPMs) for the sub-streams I run inside the Transport team of Gojek. There are multiple ways to run an IPM. Here is how I do it

- Tuesday 11.30 AM - 12.30 PM = Booking experience stream's IPM
- Wednesday 11.30 AM - 12.30 PM = Booking flexibility stream's IPM
- Since I can't show you my own sheets, please go through the [sheets in the fake Twitter PM sheet](https://docs.google.com/spreadsheets/d/1FbGVvFG4bPkazM-7AJb4Ukjv7X4Ho8oZStT1lJX23sI/edit#gid=0)
- First 15 mins of the IPM, we do a [retrospective](https://manassaloi.com/2020/03/29/retrospectives.html)
- We close the sprint, check the velocity and add it to the Retro doc
- In the next 10 mins, we go through the [projects prioritization & allocation sheet](https://docs.google.com/spreadsheets/d/1FbGVvFG4bPkazM-7AJb4Ukjv7X4Ho8oZStT1lJX23sI/edit#gid=642287720). I like to make sure the priorities of each team member is clear. Note that this sheet only contains projects under development. It is a subset of the projects mentioned in the [product development checklist sheet](https://docs.google.com/spreadsheets/d/1FbGVvFG4bPkazM-7AJb4Ukjv7X4Ho8oZStT1lJX23sI/edit#gid=1191664602)
- The next 5 mins involve quickly updating the team on the status of the projects in the pipeline, and not under dev; go through the product development checklist
- I request the TL/EM to update the [team work view sheet](https://docs.google.com/spreadsheets/d/1FbGVvFG4bPkazM-7AJb4Ukjv7X4Ho8oZStT1lJX23sI/edit#gid=203120845)
- I open the floor for team members to discuss blockers if any
- Most of the times we are done within 40-45 mins. In that case, I end the meeting early. I hate doing meetings for the sake of it, and instead of expanding the meeting to fit the time slot, I prefer people going back to their work
- Note that we don't discuss Jira during the IPM. For me as a PM, I generally just care about whether we are meeting timelines for each milestone of the project. I don't like obsessing over each story of a sprint. I let the developers cut their own stories with their TL. Over planning a sprint as well as micromanaging on a daily level has never given me any joy
- I update all the trackers that I maintain async. Read my rules for [Project management](https://manassaloi.com/2020/04/26/rules-project-management.html)

## Sprints

- One week sprints
- Backlog grooming meeting 1 day before IPM
- Dev stories created by devs
- Estimation of stories done jointly by dev and TL
- Stories added to backlog
- Jira board divided into
  - Up next
  - Blocked
  - In progress
  - Code review/Pending deployment
  - Pending in QA
  - Done/ In Production
- Blocked = Any card which is blocked due to dependency on external teams, or some other reason
- Done = Shipped to Production
- Moving something to Integration != Done
- Epics map to [Dev milestones](https://docs.google.com/document/d/1RvslTOIHBHknK54ftASaHcFEnK4ytueJ5_4jCjvDZkg/edit?usp=sharing)
- Sprints are independent or milestones, which in turn are independent of client releases
- Milestones for a feature might stretch across multiple sprints
- Completed features get shipped in the next release


Stay up to date with my latest posts/tweets here: [@manas_saloi](http://twitter.com/manas_saloi)
