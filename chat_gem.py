from dotenv import load_dotenv
import os


load_dotenv() 

api = os.getenv("GEMINI_API_KEY")

from google import genai

# Only run this block for Gemini Developer API
client = genai.Client(api_key=api)


response = client.models.generate_content(
    model='gemini-2.5-flash', contents='what is 45+23'
)
print("response generated")
print(response.text)