from google.genai import types


from dotenv import load_dotenv
import os
from google.genai import types

load_dotenv() 

api = os.getenv("GEMINI_API_KEY")

from google import genai



client = genai.Client(api_key=api)



function = types.FunctionDeclaration(
    name="get_current_weather",
    description="Get the current weather in a given city",
    parameters_json_schema={
        "type": "object",
        "properties": {
            "name": {
                "type": "string",
                "description": "Function name"
            },
            "city": {
                "type": "string",
                "description": "City name"
            },
            "temperature": {
                "type": "string",
                "description": "Current temperature of the city"
            }
        },
        "required": ["name", "city", "temperature"]
    },
)

tool = types.Tool(function_declarations=[function])


response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What is the weather like in Chandigarh?",
    config=types.GenerateContentConfig(
        tools=[tool],
        temperature=0.2
    ),
)

print(response.candidates[0].content.parts[0].function_call)


