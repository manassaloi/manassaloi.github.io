---
layout: post
title:  "Google's agentic future"
---

I've been thinking a lot about agentic software lately and how it's going to transform our workplaces. While everyone's experimenting with AI assistants and cobbling together solutions with tools like LangChain and Crew AI, I believe Google actually has the best shot at making AI agents a seamless part of our daily work lives. Let me explain why.

Think about Google's product ecosystem for a second. You've got Gmail, Meet, Drive, Docs, Sheets, Slides - all these powerful tools operating on the same layer. But what's missing is a meta layer above all of these - an orchestration layer that ties everything together. Essentially, an operating system for work.

Picture a knowledge worker (like a product manager) operating primarily from this layer rather than jumping between individual apps. This orchestration view would give you:
* A unified task list
* Recently updated documents
* Contextual recommendations
* A single place to instruct your AI agents

Consequently, without this layer, your work remains fragmented across multiple apps, and you're constantly moving context around manually. With it, you get a cohesive workspace where information flows naturally.

Ultimately, this will be the unified view for the product manager. Not Slack. Not Drive. Not Jira.

How Would This Actually Work?

Let's walk through a couple of concrete examples:

Example 1: Propagating strategic updates

Your CEO holds an all-hands meeting where she announces a major change: "We're shifting our revenue growth target from 10% to 20% for the next fiscal year."

Current workflow: You attend the meeting, take notes, and then manually update numerous documents - your roadmap spreadsheet, business models, planning docs, and presentation decks. You hunt down each relevant file, make changes one by one, and hope you haven't missed anything.

With an agentic layer: You simply tag the key insight from the Meet transcript: "Growth target increased to 20% from 10%." Your Google agent then:
1. Identifies all relevant documents using Google's powerful search capabilities
2. Drafts updates to your roadmap in Sheets
3. Modifies growth projections in your business models
4. Updates planning documents in Docs
5. Presents all these changes for your review in a unified interface (it can be inside the Meet client, how you can accept changes inside a file on Cursor, or because it will take time, you can just leave Meet, and just accept the changes at the OS view (equivalent to Composer view on Cursor))

You review the suggested updates, approve them (perhaps with some tweaks), and the changes propagate across your workspace. What might have taken hours now takes minutes.

Example 2: Creating Product Specs on the Fly

Now let's look at how this might work within Google Docs specifically.
Imagine you're a product manager tasked with creating a spec for a new feature that will help hit that ambitious 20% growth target. You open a blank Google Doc to start drafting.

Current workflow: You manually gather context from multiple sources - you open your business projections spreadsheet in another tab, pull up design mockups, reference competitor analysis docs, check the technical limitations from engineering notes, and try to keep all this context in your head while writing a coherent spec from scratch.

With the agentic assistant: Just like how Cursor has Composer chat always available on the right-hand side for coding, Google Docs would have an always-present AI sidebar. There you can ask the agent to co-work with you on the spec. You start by telling it:

"I need to create a spec for our new Premium tier feature. This needs to contribute to our new 20% growth target."
The assistant responds: "I can help with that. What information should we incorporate?"

You reply: "Let's use the Q3 business projections spreadsheet, the competitive analysis from last month, and those new mockups the design team shared yesterday." You can even tag the relevant files like you do on Cursor.

The assistant then:
1. Instantly pulls in the relevant data from your linked spreadsheet
2. Analyzes the competitive landscape from your previous doc
3. References the design mockups and their annotations

It then drafts a complete product spec including:
* Feature overview
* Success metrics (directly tied to the 20% growth target)
* Technical requirements
* Timeline recommendations
* Revenue impact projections (pulled right from your spreadsheet)

You review it section by section, making tweaks and giving feedback like: "The timeline is too aggressive here," or "Add more detail about the user flow." The assistant refines its work based on your guidance.

When you're satisfied, you accept the changes - just like in Cursor Composer - and your polished spec is ready to share with stakeholders, complete with all the right references and metrics aligned to your company's new growth targets.

Google is uniquely positioned to build this future for several key reasons:
1. Complete product ecosystem - They already own the full suite of workplace tools where most knowledge work happens
2. Best-in-class search - Google's core competency is finding relevant information, which is essential for agents to locate the right documents to modify
3. Gemini's massive context window - Unlike competitors, Google's Gemini can hold multiple large documents in context simultaneously, allowing it to make coherent, cross-document updates. No other model comes close
4. Native integration potential - No "duct tape" solutions needed - Google can build agents directly into their existing products. Their RAG flow will always be better because they have access to all your relevant documents
5. Treasure trove of user work data - Google already has access to how you work, collaborate, and use their tools. This data is gold for building agents that adapt to your specific workflow patterns. Sure, you could duct tape together various agentic solutions, but they won't have this rich history of your work habits to draw from.

This gets even more powerful when you add MCP to the mix. This approach would allow the Google orchestration layer to extend beyond just Google products.

Your agent could use MCP servers to communicate with tools like:
* Jira for project management
* Asana for task tracking
* Dozens of other workplace tools
* Slack for status updates

All from that same unified interface. Imagine saying "Update our roadmap to reflect the 20% growth target and make the changes on Asana" and having it all happen automatically.

And for large enterprises with thousands of files? Only Google's approach would scale. While having a huge context window is helpful, Google's real superpower is their ability to index, search, and prioritize information at massive scale. Again, they can fetch the files relevant for a particular task. They don't need new permissions because your data is already with them. Over time their model to predict which files are needed for the task only becomes better because millions of workplaces already use Google.

Furthermore, even if your organization has files spread across hundreds of teams and departments, Google's infrastructure is already designed to handle exactly this kind of complexity. The search giant would excel at finding the needle in your organizational haystack and identifying the information that needs updating when new information comes in.

For knowledge workers, this represents a fundamental shift in how we spend our time:
* Less manual information movement between tools
* Reduced busywork updating documents
* More time for creative thinking and strategic decision-making
* Fewer things falling through the cracks

In essence, the agent becomes your second brain - remembering context, suggesting actions, and handling routine tasks while you focus on the work that truly requires human judgment.

I believe we're moving toward a world where our digital work life isn't spread across dozens of disconnected apps. Instead, we'll operate from an orchestration layer that gives us a cohesive view of our work while agents handle much of the manual labor behind the scenes.

Google, with its integrated workspace, massive context windows, and search capabilities, has everything needed to make this vision a reality. The question isn't if this will happen, but when - and which companies will be quick enough to adapt.

As these agentic systems mature, the productivity gains will be enormous. The companies that embrace this shift earliest will have a significant competitive advantage. And based on what I'm seeing, Google is perfectly positioned to lead the way.

P.S Yes, Microsoft can build this too. Eventually OpenAI might also figure out long context, and Microsoft has a product suite like Google. Since I have always used Google suite, this was more about how I see my workflow evolving.
