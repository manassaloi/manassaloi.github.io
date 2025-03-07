---
layout: post
title:  "AI coding workflow"
---

I spent 5 hours on Cursor today. Here are some of my findings. Might be obvious to some. But this is the way I will do my next projects to save a lot of pain later.

-----

Make a project plan. Get help from O1.

Go to design inspiration sites. Find a few you like.

Bring them to v0 for inspiration.

Don't take the screenshots to cursor and ask for one shot generation.

Do it step by step.

Define the grid system first.

Create a brand playbook with details on font, colour, spacing, sizing info.

Think responsiveness. Mobile optimised from day one.

Add cursor rule to check existing files before creating new files for every small thing. Example: All css must be on the existing scss file already generated by jekyll. Explain to Cursor what each file does. Maybe add the details to the cursor rules file.

Ask cursor to explain and then code. Especially complex layout pieces.

Before each prompt, ask it to explain the flow. Where is the element defined: which html page, where is the css for this element defined, etc. If there is any JS involved, ask where it is defined again.

Otherwise Cursor will just create a lot of duplicate classes and get confused later.

If styling is not applied, it is probably because of clashing css.

If stuck, use repoprompt and copy/paste the entire codebase to O1 and ask.

Hallucination is a real problem. You'll get stuck in endless loops if you don't understand the details.

Take screenshots of the generation that are not good, ask  Cursor to compare it to the image you were trying to copy, and ask it to explain the difference between the two. Then ask it to code.
