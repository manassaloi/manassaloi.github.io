---
layout: post
title:  "OpenEvidence vs Harvey"
---

Frontier reasoning models has managed to commodify the legal space.

Almost every major foundational model have beaten Harvey’s in-house legal model on its own BigLaw Bench.

Now Harvey has scraped its vertical model positioning and repositioned itself as an agentic workflow company that chains multiple models and tools together.

OpenEvidence took a different approach.

It focused on smaller, specialized models that continued to perform better than foundational models when it comes to being a trusted copilot for medical professionals.

So why has Harvey's inhouse models failed while OpenEvidence's have succeeded?

I think OpenEvidence has won because it has access to locked up data that most frontier foundational models can’t touch.

It licensed the entire New England Journal of Medicine archive and the JAMA network material, still fenced off behind paywalls and robots files, then tuned an open source model on that corpus and wired in retrieval so every answer is backed by a trusted source.

A general model trained on random web crawl rarely sees that text in full, so it can’t quote dosage tables or the latest NEJM trial with confidence.

General LLMs usually never see those journals completely, so they guess dosage tables or miss a brand new randomized clinical trial.

And clinicians notice. In an era where medical knowledge now doubles every 73 days, the only safe shortcut is a model that reads the journals for doctors, daily, and shows its work.

This moat is hard to copy. Publishers discovered what their PDFs are worth and now sell exclusivity, not bulk feeds. Any challenger must either outbid OpenEvidence or scrape, which fails compliance reviews in hospital IT.

Harvey tried the same trick for law but:
- US case law data already sits in the public domain. Seven million opinions went online via the Caselaw Access Project, free for anyone with a scraper.
- GPT-4, Gemini, Claude, and all other foundational models already trained on that long before Harvey showed up, so Harvey had no unique competitive advantage when it comes to legal data.

Public case opinions are less exclusive than medical journals, but Harvey still leverages pay walled treatises and LexisNexis data through their partnership, so it does have some proprietary sources. However, these sources haven't been enough to build an inhouse model that outperforms foundational models.

Harvey now just layers workflows and retrieval on top of whichever foundation model is SOTA. Its ceiling is the underlying model’s ceiling.

Medicine and law also differ in how knowledge ages. Medical evidence becomes outdated quickly; a new randomized clinical trial can change practice overnight. Legal precedent moves slowly through amendments and scattered rulings, so yesterday’s case often remains relevant tomorrow.

Constant re-ingestion buys less goodwill in law compared to cardiology or oncology. That makes continual licensed ingestion far more valuable in medicine than in law.

Vertical AI doesn’t win just because it’s vertical. It wins when it controls data the horizontal giants can’t touch, and when the field punishes outdated information. Medicine checks both boxes, law only one.

In short, OpenEvidence bought a moat by licensing proprietary, fast-updating data.

I expect the next OpenEvidence-like breakout to come from a field where journals are locked up and the half-life of truth is measured in days, not months.
