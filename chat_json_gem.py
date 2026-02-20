from dotenv import load_dotenv
import os
from google.genai import types

load_dotenv() 

api = os.getenv("GEMINI_API_KEY")

from google import genai



client = genai.Client(api_key=api)



response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Extract name and age from: John is 25 years old",
    config=types.GenerateContentConfig(
        response_mime_type="application/json"
    )
)


print("response generated")
print(response.text)