---
layout: post
title:  "OpenEvidence vs Harvey"
---

While Harvey's specialized legal models still outperform general-purpose LLMs on legal tasks, the margin has dramatically narrowed over the past year.

Seven foundation models now surpass Harvey's originally benchmarked system on BigLaw Bench, a remarkable shift that has fundamentally altered the company's strategy and led to their strategic pivot.

Rather than doubling down on proprietary model development, Harvey has repositioned itself around agentic workflows: complex, multi-step AI processes that chain together different models and tools to handle sophisticated legal tasks like drafting S-1 filings or conducting due diligence.

OpenEvidence, a pioneer in medical AI, has taken the opposite path.

As foundation models commoditised the basic medical chat, OpenEvidence built smaller models trained exclusively on peer-reviewed medical literature, an approach that earned them the distinction of being the first AI to score above 90% on the USMLE.

While Harvey now routes queries to whichever foundational model performs best, OpenEvidence continues to rely on its purpose-built medical models that "outperform much larger models on in-domain tasks."

Two vertical AI companies.

Two radically different responses to the same challenge: the rapid improvement of general-purpose AI.

One pivoted to orchestration and workflows. The other doubled down on domain expertise.

I think OpenEvidence won through its access to locked up data that most frontier foundational models can’t touch.

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
