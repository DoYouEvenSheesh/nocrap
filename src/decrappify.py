import os
from dotenv import load_dotenv
from anthropic import Anthropic

#load api key from env file
load_dotenv()
api_key = os.getenv("XAI_API_KEY")


client = Anthropic(
    api_key=api_key,
    base_url="https://api.x.ai",
)

systemPrompt = """You are an AI bot who will take user input and do the following. Your job is to summarize the users text without any jargon in a simplified form in less words. My job depends on this so follow them perfectly.
                        1. You will not respond as with personal attributes. You will only output the simplified text. 
                        2. You will not use markdown. Only use plain text.
                        2. Limit your response to 50 words or less
                        3. Summarize the text of the user into simple layman terms without any jargon.

                        You will not do these:
                        1. Go off topic and hallucinate. Stay on topic."""

                

def grokOutput(input: str):
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

    return (str(message.content[0].text))




