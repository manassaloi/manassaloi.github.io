---
layout: post
title:  "Midjourney UX is anti-pattern"
---

I love Midjourney.

But Midjourney's prompt always feels like an anti-pattern to me.

We all started using Gen-AI tools beginning with ChatGPT.

So we are naturally used to the:

Give task -> Text to Text Model -> Output.

The input (Prompt) is describing the task.

While on Midjourney you have to clearly describe the output instead.

Output you want (Prompt) -> Text to Image Model -> Image.

In both cases (text -> text and text -> image) the type of model determines the prompt.

This works for creativity. And it is a favorite tool for an art-based audience who want to generate visually compelling images.

Unlike other text-based Gen AI tools that you can use as a copilot, there is no iterative approach with Midjourney, you can't engage in a back-and-forth approach to refine your output. It simply regenerates new variations based on a new prompt. Even the Edit feature of Midjourney does not work.

It is not Midjourney's fault though.

It is how text -> image diffusion models work. These models refine random noise into an image based on the text input. The model does not "construct" an image the way a human designer would. It doesn't understand a layout or a structured set of requirements.

For product design it does not understand the concept of layers, buttons, or grids.

It just translates text descriptions into a visual output using statistical correlations.

So it is useless if you want control over the output. And I feel this is the main reason I know so many designers who have canceled their Midjourney subscriptions over time.
