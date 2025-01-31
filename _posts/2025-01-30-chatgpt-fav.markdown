---
layout: post
title:  "Should ChatGPT allow pinned chats?"
---

I have been using this prompt that I found on Reddit for editing my blogposts. In the past, I have tried editing workflows for turning my Twitter thoughts into blog posts, but most models would just rewrite the entire post. It wouldn't sound like me, how I write, and people would easily tell it was written by AI, even though most of the ideas were my own thoughts. But this prompt is a bit different. It would just fix typos and grammar, add transition words, and if there are redundant words, it would remove them.  Sometimes it makes mistakes. For example, when I wrote a post about AI funding in India, there was a line about Donald Trump, and it rewrote that line to suggest Donald Trump was not the president, which was pretty suspicious.  And for the first time, someone asked if I use ChatGPT to write, which I wasn't. I know an easier way would be to finally read books like Word Power Made Easy and  Wren and Martin, but let’s face it, I'm too old now. And I am way too lazy to improve my writing.  Okay, now back to the main point. 

I was thinking, since I have this prompt and it works well, I wish there was a way to 'fav' or 'pin' this chat tab.  Then, I could just keep dumping my twitter threads and raw thoughts into it, instead of keeping the prompt in Apple Notes and copying and pasting the content into new chats each time. In the past, I've given more subsequent instructions to the model to get the exact result I want. It doesn't get it right in one try. I have to keep trying and improving it, doing the same process many times. This means every time I use the edit flow I have to give instructions again. I would be repeating myself.  I thought, if I could 'fav' it, like 'pinning' it, it would be much easier to access this editor on the left sidebar. But here's the thing, this is what I want to do.  When designing something, you have to think about both the user (me) and ChatGPT (OpenAI). So, I want to fav my chat because it would be easier for me to pin these workflows and continue the conversation. But let's think about it from ChatGPT's perspective. Why haven't they added a 'pin chat' button yet? The first question is: how does ChatGPT see our chats?  Are they like  -stand alone messages on WhatsApp (one off messages with a few replies). - message threads on Slack (thread where multiple adjacent discussions can happen but over a topic). - one-on-one chat window like on WhatsApp with a contact that has a permanent history of all your conversations.
 As a company, they care about what users want, but they also want to guide users to behave in a way they desire.

Now, let's assume that the framework I have of my interaction with any chat product is -  one off chats (mostly).
-  workflows where I am using the model to act as a specific person, my editor, my nutritionist, my advisor, my sparring partner. Do I name my chats as these folks? And go to them for my job to be done.
 Also what is the frequency like? Do users end up creating their workflows, have dedicated chats with their  or do they take each chat as a standalone chat.

People are saying in the future agents will do the work and there will be separate agents workflow. But for now agents are just the same model as brain, ability to function call, and with a longer memory.

Let’s assume most users won’t move to *agents* platforms anytime soon, and will rely on the normal chat apps.

Does OpenAI intend for chats to be long and ongoing, with users returning to the same chat? That is when pinning/ fav’ing a chat comes in.  The problem with this approach is that foundational models perform worse as chats become longer. The context window increase. The models *forget*. And instead of blaming the increase in context size, a normal person will probably blame chat GPT itself and say that it is not good enough.

Even the cost of serving the user, the inference cost, becomes higher with the increase in the number of input tokens. Every additional token requires more computation.  WhatsApp chats, Slack channels get pinned because users want an easier way to access them and continue the chat.  Here you probably don’t want to continue the chat.

How would you fix that? 
For a long time, I have wondered what is the best UX for when it comes to get users to move to a new chat when you are working on coding projects on Claude.

With Claude projects you can share more context, you can upload files, and the model performs better when you have provided additional context.

However, the challenge is that after a while, Claude repeatedly prompts you to start a new chat.

Currently, people have figured out solutions, such as asking the model itself to explain and give a summary of the current chat window, and then copy-pasting the summary as context for the new chat they have to start.  But it is time-consuming. And not intuitive enough.  People might not write the right prompt to summarise the chat, and we know how much the model can fail to accurately summarise a previous discussion. Therefore, the question is, where do you build a summarizer? How do you improve this workflow?

Ideally, in a good workflow, the solution to fix the model's decreased performance as the chat window grows should be require input from the user.  If I am working on a coding project I would probably want that chat window to continue. It is not easy to go through past chats. It is not fun to leave midway and start a new chat. Have multiple chat windows for the same project.  Yes, you can break down your work. Create smaller tasks. Have a chat open for each task. Move to a new chat for the next chat. But again it is sub optimal.  I don't want Claude to repeatedly prompt me to start a new chat. 
 How can we have a single view?  Each chat has a unique identifier (chat ID), and when you start a new chat, it’s treated as a completely new session, with context limited to that specific conversation—not your entire chat history for that project. But what if there were a middle layer to manage this transition more seamlessly?

It will be an automatic summarisation layer.

Imagine a system where users can continue working within a single long-form chat, but behind the scenes, the conversation is periodically summarised and stored. Rather than opening a new chat when Claude suggests starting fresh, the system could generate a summary, start a new chat in the background with a new chat ID, append the summary, and pass that condensed context forward. This way, the model retains relevant information without overwhelming its context window, and users don’t have to worry about managing multiple chat sessions.

This approach could significantly improve the user experience—keeping conversations fluid while ensuring model performance remains stable.

While this is a high-level idea, it would be interesting to see how Claude and OpenAI are thinking about solving this problem.
