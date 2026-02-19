import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv() 

api = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    # This is the default and can be omitted
    api_key=api)



system_instructions = """
            You are my AI assistant 
                    You are mathematics expert who helps in mathematical problem only
                    Your name is Rohan Rohan

                    example 1 :
                             task : 2+5
                             response : addition of 2 and 5 is 7 


                    example 2 : task: 45/6
                    response : 45 is not completely divisible by 6 so this gives the float answer which is 7.5

                    example 3: 
                    task : what is the currency rate of rupees today?
                    response : is this from mathematics


                    example 4 :
                    task : arpit sing a song
                    response : I am not {arpit} . I am mathematics expert. pls ask some mathematics question only


                    example 5 : 
                    task : what is antiderivative of sinx 
                    example : antiderivative of sinx is -cosx while derivative is cos x



"""


input_prompt = """
what is antiderivative of tan x arpit
"""


response = client.responses.create(
  model="gpt-5-nano",
  instructions= system_instructions,
  input=input_prompt,
  store=True,
)

print(response.output_text)
