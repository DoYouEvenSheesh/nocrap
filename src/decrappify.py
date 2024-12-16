import os, sys
from anthropic import Anthropic 

XAI_API_KEY = os.getenv("XAI_API_KEY")
client = Anthropic(
    api_key=XAI_API_KEY,
    base_url="https://api.x.ai",
)

systemPrompt = """You are an AI bot who will take user input and do the following. Your job is to summarize the users text without any jargon in a simplified form in less words. My job depends on this so follow them perfectly.
                        1. You will not respond as with personal attributes. You will only output the simplified text. 
                        2. You will not use markdown. Only use plain text.
                        2. Limit your response to 50 words or less
                        3. Summarize the text of the user into simple layman terms without any jargon.

                        You will not do these:
                        1. Go off topic and hallucinate. Stay on topic."""

                

def grokOutput(input):
    message = client.messages.create(
        model="grok-beta",
        max_tokens=500,
        system=systemPrompt,
        messages=[
            {
                "role": "user",
                "content" : input,
            },
        ]
    )

    return str(message.content)



grokOutput("""wiped: The School that Banned Smartphones, hosted by Matt and Emma Willis, is based at The Stanway School in Colchester, and challenged a group of Year 8 pupils to give up their smartphones completely for 21 days. 

The experiment, led by Professor Lisa Henderson and Dr Emma Sullivan from the University, saw pupils undergo a series of tests, with experts monitoring their behavioural changes throughout the period, and repeating the tests at the end of the three weeks to conclude what effects giving up your phone really does have on your brain including sleep, wellbeing and cognition.

They found that students in the phone ban group experienced notable improvements in their sleep. On average, they were falling asleep 20 minutes faster than before the ban, and reported getting a full hour of extra rest each nig""")
