
from dotenv import load_dotenv
import os
from google import genai
from google.genai import types

load_dotenv() 

api = os.getenv("GEMINI_API_KEY")






client = genai.Client(api_key="YOUR_API_KEY")



instruction = """You are a professional career mentor. Give structured advice.
                    you have no idea about movie or other stuff"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        {
            "role": "user",
            "parts": ["Tell me the next movie of salman khan"]
        }
    ],
    config=types.GenerateContentConfig(
        system_instruction="You are a helpful AI tutor. Explain in very simple language.",
        temperature=0.7,
        max_output_tokens=300,
    ), 
)


response.text