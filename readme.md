# 🚀 AI Python Setup Guide

**OpenAI + Gemini AI | Virtual Environment | API Integration**

This README provides a clean, structured, and beginner-friendly guide to setting up a Python environment and integrating:

* 🔹 OpenAI Python SDK
* 🔹 Google AI Studio (Gemini API)
* 🔹 Virtual Environment (venv / Conda)

---

# 📌 1. Create Virtual Environment

Creating a virtual environment keeps your project dependencies isolated and clean.

---

## 🐍 Option 1: Using Python `venv`

### Step 1: Create environment

```bash
python -m venv env_name
```

### Step 2: Activate environment

**Windows**

```bash
env_name\Scripts\activate
```

**Mac/Linux**

```bash
source env_name/bin/activate
```

---

## 🐍 Option 2: Using Anaconda (Conda)

### Step 1: Create environment

```bash
conda create -n env_name python=3.10
```

### Step 2: Activate environment

```bash
conda activate env_name
```

---

# 🔐 2. Create API Keys

You need API keys to authenticate your requests.

---

## 🔹 OpenAI API Key

Create your API key from:

👉 [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)

Platform: OpenAI

---

## 🔹 Gemini API Key

Create your API key from:

👉 [https://aistudio.google.com/api-keys](https://aistudio.google.com/api-keys)

Platform: Google AI Studio
Model Provider: Google

---

# 🔧 3. Install Python SDKs

---

## 📦 Install OpenAI SDK

Official Repository:
👉 [https://github.com/openai/openai-python](https://github.com/openai/openai-python)

```bash
pip install openai
```

---

## 📦 Install Gemini AI SDK

Official Documentation:
👉 [https://googleapis.github.io/python-genai/](https://googleapis.github.io/python-genai/)
Repository:
👉 [https://github.com/googleapis/python-genai](https://github.com/googleapis/python-genai)

```bash
pip install google-genai
```

---

# 🔑 4. Store API Keys Securely (.env Recommended)

Install dotenv:

```bash
pip install python-dotenv
```

Create a `.env` file:

```
OPENAI_API_KEY=your_openai_key_here
GEMINI_API_KEY=your_gemini_key_here
```

---

# 🤖 5. OpenAI Python Example

```python
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.responses.create(
    model="gpt-4.1-mini",
    input="Explain AI in simple terms"
)

print(response.output_text)
```

---

# 🤖 6. Gemini AI Python Example

```python
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain AI in simple words"
)

print(response.text)
```

---

# 🧠 7. Recommended Project Structure

```
ai-project/
│
├── env_name/
├── .env
├── requirements.txt
├── openai_example.py
├── gemini_example.py
└── README.md
```

Generate requirements file:

```bash
pip freeze > requirements.txt
```






-- run a file 
python file_name.py

