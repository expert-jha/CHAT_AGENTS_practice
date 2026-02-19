from dotenv import load_dotenv
import os
from google.genai import types

load_dotenv() 

api = os.getenv("GEMINI_API_KEY")

from google import genai

# Only run this block for Gemini Developer API
client = genai.Client(api_key=api)



response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain overfitting.",
    config=types.GenerateContentConfig(
        system_instruction="You are a senior data science professor. Explain in simple language for beginners.",
        temperature=2
    )
)

print(response.text)
