
from dotenv import load_dotenv
import os
from google.genai import types

load_dotenv() 

api = os.getenv("GEMINI_API_KEY")

from google import genai



client = genai.Client(api_key=api)






response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Extract product name and price from: The iPhone offering a sleek design, powerful performance, high-resolution display, advanced camera system, long battery life, costs 800 dollars , regular software updates, strong security features, and seamless integration with the broader ecosystem of devices and services.",
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema={
            "type": "object",
            "properties": {
                "product": {"type": "string"},
                "price": {"type": "number"}
            }
        }
    )
)

print(response.text)
