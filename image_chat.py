from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


path = "https://drive.google.com/file/d/1AZhY3rtYQkeCL-c9Vb6oK0OCQ_-bq_us/view?usp=sharing"

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        types.Part.from_text(text ="What is this image about? Return structured JSON."),
        types.Part.from_uri(
            file_uri=path,
            mime_type="image/jpg"   ### input data type
        )
    ],
    config=types.GenerateContentConfig(
        temperature=0.2,
        response_mime_type="application/json"
    )
)

print(response.text)
