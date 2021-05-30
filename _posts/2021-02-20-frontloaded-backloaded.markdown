---
layout: post
title:  "Frontloaded, not backloaded"
---

When I was a dev I would start working on the backend APIs without prior discussion with my frontend devs. I would create the APIs needed for a new feature and then share a doc with them. Meanwhile, the front-end devs would write their code first using static data, then using dummy data from APIs, and finally test them with production data. Close to release, we would find out that the PM has decided to go down another direction, and we would have to repeat the whole process. Missing edge cases was a common theme. So was changing entire flows to handle them. Even QAs entered the game pretty late. It was chaos. A lot of critical things used to happen at the end of the product dev cycle; you can say the process was backloaded. Even documentation was written after development was done.

Mistakes at the beginning are easy to correct. So catch them at the beginning. Make your processes front-loaded with most of the items done at the beginning than the end.

As a PM, I have tried to front-load the process dev process than backload it. Executive alignment happens before we decided to pick up a project. A feature is broken into detailed milestones before we design for a single one. Kick-off with all members of the team (PM + QA + front end + back end devs) happens before we close implementation details. RFCs are floated early, comments are invited from team members. People escalate their concerns during the beginning and not the end. Questions around the WHY behind a feature are answered while writing the spec and not close to shipping something on Production.

In simple words: Do things at the beginning than at the end of the dev process to avoid waste.
