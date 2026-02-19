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
            "content": "You are a helpful math tutor."
        },
        {
            "role": "user",
            "content": "What is 10 + 5?"
        },
        {
            "role": "assistant",
            "content": "10 + 5 equals 15."
        },
        {
            "role": "user",
            "content": "Now multiply it by 2."
        }

    ]
)


print(response.choices[0].message.content)