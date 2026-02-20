import streamlit as st
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables
load_dotenv()
api = os.getenv("GEMINI_API_KEY")

# Save model name
MODEL_NAME = "gemini-2.5-flash"

# Initialize client
client = genai.Client(api_key=api)

# Function to extract product info
def extract_product_info(text):
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=f"Extract product name and price from: {text}",
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema={
                "type": "object",
                "properties": {
                    "product": {"type": "string"},
                    "price": {"type": "number"}
                },
                "required": ["product", "price"]
            }
        )
    )
    return response.text


# ---------------- Streamlit UI ---------------- #

st.set_page_config(page_title="Product Extractor AI", page_icon="🤖")

st.title("🛍️ Product & Price Extractor (Gemini AI)")
st.write("Enter a sentence like: *iPhone costs 800 dollars*")

user_input = st.text_input("Enter Product Description")

if st.button("Extract"):
    if user_input:
        result = extract_product_info(user_input)
        st.subheader("Extracted JSON")
        st.json(result)
    else:
        st.warning("Please enter some text.")