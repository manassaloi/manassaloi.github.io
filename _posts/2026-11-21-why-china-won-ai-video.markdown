---
layout: post
title:  "Why China Won AI Video"
---

More than 95% of new micro dramas released in China are now made with AI.

The top models on Higgsfield are all Chinese video models.

China has won AI video.

The US built better text models. China built the video models people actually use to make money.

Why couldn't the US compete with China on video?

My hypothesis:

* China approached video models the same way it approached manufacturing
* Video is very different from code
* The demand already existed
* They own the entire stack and the feedback loop

I don't think it's about access to data or copyright.

The easy answer is always copyright: "Chinese labs trained on whatever they wanted while American labs were tied up by lawyers."

I don't think that holds up. American labs trained their text models on huge amounts of copyrighted books, articles and code, and they're being sued for it right now.

And Google, which owns YouTube, the largest library of video ever assembled, has had legal access to more training footage than anyone in history. If data access decided the race, Google would have won it.

But I use Seedance and Kling. Not Veo.

Let's understand why.

Some work rewards rough drafts: speed over quality.

A coding model that's right half the time is worse than useless. You have to review every line and chase down the bugs it left behind. Coding took off with Opus 5.5 because agents could finally work in a verifiable loop: write code, run the tests, fix, repeat. It worked offline. Code gets checked offline, in seconds. Video has a loop too. It's just online, and is checked by people swiping. As I wrote in my other post today, video is driven by taste. There is no perfect video. The feedback only comes once it's out there. That's why owning the feed matters so much. More on that later.

A video clip that's half right is different. The hands look odd, the physics might not make sense, and viewers might tell it's AI. But if the hook lands in the first three seconds, people keep watching. The flaws are visible and cheap, and nothing breaks downstream.

A clip at 50% quality still gets watched, and every view is data.

That is exactly the condition China's manufacturing model was built on.

Shenzhen didn't start out making the best phones. It made cheap phones that were good enough, sold huge numbers of them, learned from every production run and improved faster than anyone else could. Electronics, solar and EVs all followed the same pattern: ship something rough, sell volume, and let the volume tell you what to fix.

The method has one requirement: the market has to buy the rough first version, so the loop can start turning.

Yes, there were subsidies, and Chinese companies have been able to undercut their global peers. But Tesla got subsidies too.

What isn't talked about enough is that Shenzhen built an ecosystem around manufacturing and simply moved faster than the competition. What started as a place to build good-enough things became a center of engineering excellence.

It's the pottery class story from Art & Fear. Half the class was graded on how many pounds of pots they made. The other half was graded on one perfect pot. The best pots all came from the quantity group, because they learned from every bad one.

Quantity and a rapid feedback loop eventually leads to quality as well.

Chinese open-weight coding models get used, mostly where cost matters. But the most valuable coding feedback flows through American tools: Claude Code, Codex, OpenRouter (even when it's serving Chinese models).

There isn't enough demand for Chinese coding models.

US models are heavily subsidized. There are national security concerns in the US. And for coding, the bar is very high, as we discussed earlier.

So how is video different?

We already covered one thing: good enough is perfectly fine for video.

But there's more. The demand for what Chinese video models produce already existed.

Micro drama was a booming business in China.

One- to two-minute vertical episodes, 60 to 100 of them per series, built on a small set of plots that reliably keep people watching (the hidden billionaire heir, the contract marriage, the betrayed wife who comes back for revenge).

Viewers pay per episode or watch ads to unlock the next one, and the cliffhangers are designed around that paywall. Traditional crews shot whole series in a week or two on budgets that wouldn't cover a single day on a Hollywood set. The industry's revenue has passed China's box office.

Look at that structure. It's already a factory: standard parts (plot templates), production that looks like an assembly line, ruthless measurement of what keeps viewers watching, and a crowd that tolerates rough work as long as the next episode delivers. The sector had been optimizing for volume and speed for years.

It had a clear demand signal, a clear way to make money and a clear bottleneck: the cost of human production.

AI replaced the stations on the line one by one: scripts, storyboards, characters, scenes, voice, dubbing, editing.

What does that remind you of? Another Shenzhen.

Only this time it's manufacturing content instead of physical goods.

The micro drama industry swapped human labor for generated content.

Once the cost of an episode collapsed, the economics flipped. When a series costs a fraction of what it used to, you can afford to make ten and kill nine. Testing gets cheap, so you test far more. More tests mean more data, the next batch improves faster, and the loop speeds up.

And just like in manufacturing, the whole factory is in China.

A few players control the entire ecosystem. Take ByteDance.

* Its model is Seedance, which even Western aggregator platforms like Higgsfield promote as their most capable.
* Its creation tool is CapCut, where most of the world's short-form video is already edited. The model sits right inside the tool creators already use.
* Its platforms are Douyin at home, TikTok abroad, plus Hongguo, ByteDance's free micro-drama app.
* Monetization runs through ByteDance's own ad network, which pays for free-to-watch drama and buys traffic for paid drama.
* The feedback is every swipe, rewatch, drop-off and unlock across all of it.

So ByteDance doesn't just own a model. It owns the entire loop: from generation through editing, distribution and payment, back to measurement. ByteDance learns what viewers actually watch, how creators actually work, and what should get made next. Each part makes the others faster.

Kuaishou has a smaller version of the same setup: Kling for the model and its own short-video app for distribution. It's no accident that China's two strongest video models come from China's two biggest short-video platforms.

Yes, Kling and Seedance got motion, multi-shot scenes and keeping a character consistent across shots right before most Western models did. But they got there by owning the entire stack and running the loop faster.

When you ship millions of clips, you know exactly what actually matters when it comes to a video output.

AI already makes 95% of new releases, and it's catching up on the hits too. A year ago, AI titles were 7% of China's top 100 micro dramas. By January 2026, they were 38%.

It isn't pretty. Most of these dramas flop. Hit rates are tiny, most producers lose money, and the platforms keep most of the value. There's a lot of slop, and Chinese regulators have already started pushing back.

But that's Shenzhen too. The knockoffs came before BYD. Now DHH's mind is getting blown after sitting in a BYD in China. And Ford's leadership is importing Chinese cars to study and reverse engineer them.

What I've been trying to figure out is why Google failed.

Google has everything ByteDance has. It has YouTube, the largest video library and audience on earth. It has Shorts, a direct competitor to TikTok. It has Veo, which on raw image quality is said to be among the best video models in the world. It has the money, the compute and the research talent.

So why do creators keep choosing Seedance and Kling?

The answer comes from coding. In AI coding, the most valuable position didn't go to whoever had the most code. It went to whoever owned the tool developers actually work in. Cursor proved it first: by sitting inside the developer's workflow, it saw every accept, reject, edit and retry, which is exactly the signal a model needs to improve.

Anthropic took that further by owning both the model and the tool with Claude Code, closing the loop completely. Whoever owns the tool owns the feedback, and whoever owns the feedback improves fastest.

Video works the same way, and ByteDance figured that out. CapCut is effectively the Cursor of video: the place where footage becomes a finished, postable piece, where the model's output gets accepted, cut, rearranged or thrown away. ByteDance put its model in that tool and connected the tool directly to its feed.

Google did put Veo inside Shorts and YouTube Create. But a generate button inside a posting app isn't a production line.

CapCut is a production line, where studios cut 80-episode series. Shorts is where someone makes a quick clip for fun. YouTube still mostly sees finished videos, not how they got made.

Price matters too. On aggregator platforms, Veo is among the most expensive models per clip. A micro-drama studio generating hundreds of variations a day doesn't want the most beautiful model. It wants the cheapest one that's good enough.

YouTube also never had the format. It had no serialized, pay-per-episode, cliffhanger-driven drama business to plug AI into.

ByteDance had Hongguo and an entire micro-drama economy before Seedance shipped. Google had a good model and nowhere in particular to use it.

And Google had a reason to hold back. YouTube's moat is human creators. People watch a creator because they trust that person. If YouTube floods the feed with AI dramas, it eats into the creators who make it valuable, and advertisers get nervous.

This is the reason they are now going after AI content. So is Meta.

ByteDance doesn't have that problem.

The irony is that when creators use Veo, they often use it through someone else's tool, on someone else's platform, so the learning ends up with someone else.

In the end, it comes down to one number. A studio making dozens of episodes a week doesn't care which model tops a benchmark. It cares what it costs to get a shot it can actually use.

China built the factory that keeps pushing that number down.

Google built a great model and is still looking for the factory.
