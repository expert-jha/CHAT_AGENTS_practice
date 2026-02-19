from dotenv import load_dotenv
import os
from google.genai import types

load_dotenv() 

api = os.getenv("GEMINI_API_KEY")

from google import genai

# Only run this block for Gemini Developer API
client = genai.Client(api_key=api)

instruction = """You are my AI assistant 
                    You are mathematics expert who helps in mathematical problem only
                    Your name is OSAMA"""    ### system prompt

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="explain AI",
    config=types.GenerateContentConfig(
        system_instruction=instruction,
        temperature=1
    )
)

print(response.text)
