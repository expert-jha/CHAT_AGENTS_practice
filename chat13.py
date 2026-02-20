
from google.genai import types


from dotenv import load_dotenv
import os
from google.genai import types

load_dotenv() 

api = os.getenv("GEMINI_API_KEY")

from google import genai



client = genai.Client(api_key=api)



response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Analyze sentiment: Learning DATA SCIENCE was amazing ALthough it was little difficult",
    config=types.GenerateContentConfig(
        response_mime_type="application/json"
    )
)

print(response.text)
