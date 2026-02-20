import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv() 

api = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    # This is the default and can be omitted
    api_key=api)


response = client.chat.completions.create(
    model="gpt-5-nano",
    messages=[
        {
            "role": "system",
            "content": "You are a strict technical interviewer. Ask one question at a time."
        },
        {
            "role": "user",
            "content": "I want to practice Python interview."
        }
    ]
)


print(response.choices[0].message.content)