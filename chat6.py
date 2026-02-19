from dotenv import load_dotenv
import os
from openai import OpenAI


load_dotenv() 

api = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    
    api_key=api)





print("loaded successfully")




client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-5-nano",
    messages=[
        {
            "role": "system",   ### system role
            "content": """
You are a Senior Python Architect with 10+ years of experience.
You specialize in:
- Async programming
- CPython internals
- Performance optimization
- Clean architecture
- Production-grade backend systems

Rules:
- Provide clear explanations.
- Include code examples.
- Mention edge cases.
- Keep answers concise but technically deep.
- Follow PEP8 standards.
"""
        },
        {
            "role": "developer",
            "content": """
When answering:
- Explain concept first.
- Then show simple example.
- Then show advanced example.
- Mention performance considerations.
"""
        },
        {
            "role": "user",
            "content": "how does query execute in mysql "
        }
    ],
)


print(completion.choices[0].message.content)