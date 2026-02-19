import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv() 

api = os.getenv("OPENAI_API_KEY")


client = OpenAI(
  api_key=api
)

response = client.responses.create(
  model="gpt-5-nano",
  input="write a gmail reply to HR in 45 words for promotion",
  store=True,
)

print(response.output_text)



