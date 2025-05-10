---
layout: post
title:  "ChatGPT Voice to text"
---

I don't like the new OpenAI voice-to-text input.

The earlier version had a more thoughtful flow:
- Active listening indicator: You saw a timer and microphone animation, which gave feedback that it was capturing your voice.
- Transcription preview: After you spoke, the transcription was visible before sending. You could edit any mistakes.
- Explicit submit step: You were in control of when the message was finalised and sent.

Now:
- There's no clear indication of how long you've been speaking. It just says listening, then the state changes to transcribing, and then it just blasts off the query.
- It auto sends the transcript without confirmation. And once the response comes you realise it could not understand your accent and wrongly transcribed like 5 critical words that changes the entire context of the query.
- If the model mishears you, you can't correct it unless you manually redo the entire message. Or correct after ChatGPT responds to your first message with typos.
- And God forbid it throws errors like "I didn't catch that", especially during longer recordings, there's no option to retry, and you'll have to repeat everything you just said.

This "faster but dumber" flow works if everything goes perfectly, but when it doesn't, it's frustrating. Claude does something similar. No intermediate correction step, does not let you correct the transcription. Thankfully it still shows the timer.

Some PM at OpenAI probably optimised for speed and simplicity (1 tap voice interface), without realising voice messages are different from voice to text query sent to an LLM. The new UX assumes high transcription accuracy and fast LLM turnaround, which isn't always true, especially with accents, ambient noise, and longer thoughts.
