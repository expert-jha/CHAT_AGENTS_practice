from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment variables
load_dotenv()

api = os.getenv("OPENAI_API_KEY")

# Initialize client ONLY once
client = OpenAI(api_key=api)

print("Loaded successfully")

resume = """
Govind Jha 
Indirapuram, Ghaziabad  
Linkedin| Github |📞 9355550031 

Core Teaching Skills 
• Instructor-Led Classroom & Online Training 
• Curriculum Design & Structured Lesson Planning 
• Capstone Project Mentorship 
• AI/ML Model Implementation Guidance 
• Real-world Case Study Based Teaching 
• Doubt Solving & Academic Mentorship 
• Student Performance Evaluation 
• Portfolio & GitHub Project Development 

Technical Subjects Taught 
• Advanced Excel
• Power BI
• Tableau
• SQL
• Python
• Machine Learning
• Generative AI
"""

response = client.chat.completions.create(
    model="gpt-5-nano",
    messages=[
        {
            "role": "system",
            "content": "You are a resume parser. Extract structured information strictly in valid JSON."
        },
        {
            "role": "user",
            "content": f"""
            Extract the candidate name and all technical + teaching skills from the resume below.

            Return JSON in this format:
            {{
                "name": "",
                "skills": []
            }}

            Resume:
            {resume}
            """
        }
    ],
    response_format={"type": "json_object"}
)

print(response.choices[0].message.content)