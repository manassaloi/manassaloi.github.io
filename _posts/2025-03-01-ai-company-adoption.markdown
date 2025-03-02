---
layout: post
title:  "AI adoption inside companies"
---

AI can:
* Help ICs do their current work:
    * Better.
        * For a PM, can their spec become better because now they can use tools like Deep Research (OpenAI) for competitor analysis, Deep Search (Twitter) for faster, efficient search? Can AI give insights about customer behavior and point out edge cases that a normal PM would miss?
        * Can a copywriter now come up with dozens of copy variants that are probably far better than anything they could create on their own?
    * Faster.
        * Lead time: Can you cut the lead time to arrive at a spec and prototype? This is easier because you can leverage existing templates, turn notes into first-cut specs faster, and brainstorm with LLMs to think through ideas and stress test them. As a PM, you can work on quick prototypes before you collaborate with a designer on the solution. These will mostly have to be discarded. Tech leads can create their tech specs faster. AI won't do the complete work for them, but previously the planning stage would take a lot of time. Now it is far faster to brainstorm, go broad, and then narrow in on a solution (diamond).
        * Cycle time: Here it is trickier. Landing pages for marketing would be far faster. Marketers can probably do these on their own now. Stand-alone pages. You can create copy faster. If midway through the project execs change their mind, instead of the project being on hold until designers change their designs or add more scope, you can quickly use the designs to create a web prototype, make the changes, and show it, instead of making changes on the actual app. [I wish this did not happen, but ask any company, and they will tell you scope changes and design changes, especially in startups, happen quite a bit.] For a senior engineer, tab tab tab works because even in a big codebase, you are not using the agent to make changes across multiple files. Scaffolding is taken care of. Just don't expect some 90% improvement though. It is not going to happen unless you want to go full Yolo mode and spend months refactoring later.
    * More.
        * If you are doing better and faster work, a person is already delivering more. So they can manage more projects at a time and also take less time per project.
        * Since you can generate potentially infinite variants of copy and designs, you can create far more marketing campaigns than before. You can try many more landing pages. You can test different funnels for different segments. Marissa Mayer used to test 40 shades of blue for a button. AI gives you the same power, without needing the resources of a Google.
        * Empower an IC to take on completely new work not possible before:
            * This is the most exciting part of this AI age.
            * A marketer is now a copywriter.
            * A PM, instead of waiting for a data analyst for complex queries, can do their own analysis.
            * A marketer can create designs for their campaigns using various design tools.
            * A PM can make prototypes while collaborating with their business counterparts or engineers, leaving the designer to do deep work on their current projects.
            * A backend developer working on an internal dashboard does not need to wait for a designer. They can use v0 for it. They don't even need to wait for a front-end dev. They can use v0 again. Do note: These tools are good for standalone projects with smaller code bases. You can't expect these gen AI tools to write scalable code, and as the code base increases, it will hallucinate more and might even want to delete your own codebase for the lols.
        * Help teams coordinate better:
            * There are tons of meeting notes and action item products. No meeting should end without a Minutes of Meeting (MOM) now.
            * People hate writing. An email takes effort. Even a Slack update requires work. Superhuman has autocomplete. Gmail has summaries. You don't need to wait 3 days to reply to an email going forward. Replies might be templated and get shorter, but people will not become bottlenecks (hopefully).
        * Enable Push vs Pull:
            * This is my favorite topic and something I have written a lot about.
            * Push >>>>>>> Pull.
            * All PMs pretend to like data. But no one opens Tableau every day to check data. An email update means you are not pulling data anymore, and it is delivered to your inbox. Earlier you would wait for a data analyst to create a new email, but maybe now you can do it yourself. Or the data analyst can be more productive and create a new insights email and not need a week to get it done.
            * What are the insights people need to do their job better? How can we push them in a timely manner with clear action items? Facebook campaign performance is declining? Is there an email with updates about that, with insights on why that might be happening, along with 5 more suggested campaign ideas?
        * Push 10X more content on your distribution channels:
            * Use your distribution to your advantage. Create more AI-generated videos. Create memes. Post replies on other channels. Maybe create a completely new channel with only AI videos.
            More thoughts:
            * 90% and not 100%:
                * The more specific the output, the harder it is for AI to get it done. It is a next token predictor after all. This is why I can come up with a dozen ideas for a wedding card (yes, I tried this for a friend), and the characters can seem like them, use style and character reference, but for some reason or another, the hands will be messed up on Midjourney. Yes, I can use Replicate and try out more models, but each incremental rerun costs money. This is what companies will learn too. So the best use cases are where you don't need 100% accuracy, but are okay with 90%.
                    * You might want creative ad ideas.
                    * You might want creative landing pages.
                    * You might want nice graphics.
                * But be happy with 90%. If you try to make it 100%, you might end up spending as much time as before on Photoshop and you won't get the productivity gains you were expecting.
            * Workflows:
                * I would do an audit of workflow of each person working for my company and understand how they can leverage these tools to do more work at a faster pace, and can take on adjacent work.
            * Existing tools vs in-house tools:
                * I tried this experiment a while back. I was trying to see if I can create a MiniManas, use AI to write like me. I have 500 blog posts on my site.
                    * I started with just asking all the chat tools to write like me without example.
                    * I then tried to use better prompts.
                    * Asked ChatGPT to update its memory on how to write like me. Used Claude's styles.
                    * Then I gave an example in the prompt. Gave some notes.
                    * Then I tried to give examples of drafts vs final output, and played around with the number of examples and final output.
                    * Then with the help of a friend, I fine-tuned a model and tried the same exercise.
                    * Next would have been to use some RAG-based system to create embeddings of all my written content, chats or blogs, store them in some vector store, and then use different LLMs to write like me. I tried the first part, but the embeddings workflow was failing. And I was too poor to use OpenAI's embeddings API.
                    * I gave up at this point.
                * My point with the above is that you can try all sorts of solutions. But instead of trying to fine-tune some LLM and creating your own workflows, see if you can use an existing tool. You don't need to fine-tune some LLM to write code. You are not JaneStreet who needs Ocaml and needs their in-house tab tab tab. You can just use Cursor. Yes, you might have a particular design system and brand guidelines, but that does not mean you need custom loras to generate images for a brand campaign. You can just try prompt engineering and get 90% there. Post an existing brand image on ChatGPT or Grok. Ask them to describe the image. Use the description and reference image to create more brand images on Midjourney. Take it to Magnific AI to upscale. You can even use a mix of Midjourney + Figma. Instead of creating custom in-house agentic workflow, maybe try some off-the-shelf available agent workflow builders.
            * I particularly love what a founder told me: His goal is to make sure every employee in the middle of the bell curve gets superpowers and can do their job like an A player. I think that is a nice way to think about this transition.
