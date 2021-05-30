---
layout: post
title:  "Thoughts on Google Duplex"

---

![Source](https://1.bp.blogspot.com/-WdgRuOg6lwc/WvEZTDLYg_I/AAAAAAAACsM/QNLSl4Yid9wKij_2KNpCRiXjiyeptu9vgCLcBGAs/s1600/rnn_big.png)

The rounds of Hello’s and Good Mornings in my office have been replaced by “have you seen the Google Duplex demo?”. In case you have not seen the demo or read about it you can check it out here: [Google duplex blog post](https://ai.googleblog.com/2018/05/duplex-ai-system-for-natural-conversation.html)

The video is here: [Google Duplex Demo from Google IO 2018](https://www.youtube.com/watch?v=bd1mEm2Fy08)

After my initial excitement over this video subsided, I thought a lot over the implications of this. Now I take back my excitement. Here is why:

Most software (whether AI based or not) are just trying to help you improve your workflow. In the beginning of time humans did everything with their hands. Then came tools. Rapid industrialisation led to automation in factories/offices which replaced most things human used to do. Since then we have been automating various workflows. AI is nothing but automation but which has a rapid feedback loop based on data its efficiency improves massively.

Now coming to the demo, I was most impressed with the human like quality of the automated voice (which is a massive breakthrough in itself). I can think of so many crazy possibilities with this, example:

1) Accessibility. Anyone who has visually disabled can now use Google Assistant’s voice feature for their day to day tasks, and the voice won’t seem robotic

2) Large scale production of audio books. Imagine Google launching an Audible competitor where John Legend narrates any book you want!

There will be countless more.

But when we talk about doing everything through Google Assistant (GA) or any universal AI assistant, I think yesterday changed nothing.

Reason: How many times do you actually call someone to book/reserve something? You use various apps to book movies/ flight tickets and everything. Even table booking is an one click process on Zomato.

Example workflow: Booking tickets through Bookmyshow. This can be done using just the chat on Google Assistant itself without any human intervention involved (if Bookmyshow APIs are integrated and you have already shared authentication token). You don’t need voice for that. Just good NLP. This is not the 1990s where you book movie tickets using telephone. I doubt Bookmyshow would start call centres suddenly because people want to use Google Duplex to book tickets.

Even if they did support it and you want to go through Google Duplex, the call will still take 3–4 mins till you get to the OTP part. Chat is much faster. Chat queries can bypass the voice and the feedback will be 10X faster due to absence of chat to voice translation.

On both cases, all you are doing is using NLP engine of Google. And NLP is hard.

The only use case here is where the other person is not on any existing platform/app and you have to manually call that person to book a slot. In that case this would help. But I don’t remember the last time I called anyone to book anything. Okay, lets say in US you will do it. The 2nd video where the restaurant person is Asian(?) I am sure half of the times it wont be able to convert voice to text properly for NLP to parse.

In the product demoed you have:

A <-> B

A is you just writing something on GA’s app, which is being parsed using Google’s NLP engine and then spoken by Google’s Assistant bot. What you are missing is that Google needs to understand what B is saying too. It is not just understanding B’s accent, how normally B speaks but also the background. If there is static, if there are interruptions. B can be a Salon, Restaurant any SMB. Now say Google has a lot of data on how Salon owners speak (the generic data I spoke of earlier) or say it has a lot of data on how a particular salon X’s owner speaks. That does not mean A will always talk to X’s owner. It might speak to X’s son who is also a stylist and taking over from X’s owner for the day. These are just examples. In an ideal world this sounds terrific. And no doubt I am impressed by the demo. But all I am saying is there are lot of issues too for which it might have less than the effect that it had on its demo.

And I am sure vs that call, 100s of other calls were failure. Pichai said it himself during the demo.

What about fault tolerance? What if Google Assistant fails to understand the exact date for reservation? What is the failsafe? Do you as an user intervene then and somehow continue the call? That means you are anyway listening to the call in case the call fails to go as expected. This is not saving your time or replacing your secretary if you were thinking of replacing him/her with GA voice assistant.

Lets ignore B2C use cases now. I think the biggest potential for this is to replace call centres for companies. Basically a B2B play. A lot of players have come into this space. In B2B though, the major considerations are:

1. Is it cheaper than the existing solution

At scale obviously using a voice API is better than using humans

2. Is it more efficient

Yes in an ideal world. Humans take breaks. They don’t work 24*7. They have mood swings, off days. Machines never have off days. You can scale it to handle as many customer calls as possible.

But that was in an ideal world. In today’s world you need to think of fault tolerance too; and fall back scenarios. A lot of players came in the last few years to replace customer support through chat for companies using AI. Most have failed. Including a start up I personally know. The B2B case of duplex is just a voice layer on top of chat.

Big businesses can’t risk losing valuable customers in case the AI works just 60% of the times (assume this is best case scenario). What if a big client which could have used your tool came to ask for pricing and that conversation fell into 40% of the chats which failed. So till now you always have actual employees who still monitor the chats. Which have not lead to 1 and 2 points mentioned above.

Also for AI to work you need a lot of data points. Google might have that. But it is still hard. Just see countless of jokes about fails of Alexa, Siri and Google Assistant itself on Twitter/Facebook. It is cute when it mistakes your query when you ask a question on something. Not that cute if your business would lose millions of dollars of business because you could not interpret some potential customer request.

The CEO of the AI based B2B customer support chat startup I talked to recently, told me that with time they had become a services company with separate pilots running tackling specific use cases. To be an AI first company with minimal human intervention you need a lot of data. If the data is generic it is usable. Example: variations of the “who is X”, “get me more info on y”

When when you are talking about customer support data/call center data, the use cases of which I was discussing , the support logs of say company X will have very similarity to Y. It is not scalable. If you have GBs of logs of X you can create a model which tackles say 70% of incoming customer requests. But thinking you have logs of X does not help you in tacking customer requests for Y. The key here: How reusable the data is.

This was just what I felt after reading + thinking + talking to a lot people working on this domain. My personal opinion. I love Google. I have seen how they have leveraged AI in their own products (Google photos etc) and their work on building platforms + sdks which can help other third party devs leverage AI. But then again I stand by my comment that most APIs provided by both Google Cloud as well as Amazon are still primitive. There is a lot of work to be done. I was talking to a friend of mine who is working for an interactive live streaming product where user can communicate via voice. Think HQTrivia where you answer using your own voice instead of touch input. They are using Google Clouds’s API (from what I remember) and they have also tested out all voice APIs out there in the market. I cant share numbers but a lot of the times the voice to text translation is less than stellar.

I am not saying I was not impressed by the advances in work related to ML that Google has done. The ML models Google has built on Android P to save battery is super cool. My main points around the call centre replacement tweets that I am seeing a lot on Twitter. When someone says things like DeepMind AI reduces Google Data Centre Cooling Bill by 40%, I am amazed. That is crazy impressive! I am just not ready to go wow over this voice call use case yet. I might be proved wrong with time. And I’ll be happy if that happens.

I know this might seem like cherry picking tweets to suit my agenda but here is another interesting thread which discusses use cases of Duplex: [Benedict Evan’s thread](https://twitter.com/BenedictEvans/status/994249765490589697?s=19)

If you have been thinking about this as much as as have, why not join the discussion and leave your opinion! Would love to learn your views too.
