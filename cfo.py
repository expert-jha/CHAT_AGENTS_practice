import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()
api = os.getenv("GEMINI_API_KEY")

MODEL_NAME = "gemini-2.5-flash"

client = genai.Client(api_key=api)

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="AI CFO Revenue Forecaster",
    page_icon="📈",
    layout="wide"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #1f4037, #99f2c8);
    color: white;
}
.big-title {
    font-size: 50px;
    font-weight: 800;
    text-align: center;
    color: #ffffff;
}
.subtitle {
    text-align: center;
    font-size: 20px;
    margin-bottom: 30px;
}
.glass-card {
    background: rgba(255, 255, 255, 0.15);
    padding: 25px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    margin-bottom: 20px;
}
button[kind="primary"] {
    background-color: #ff4b4b;
    color: white;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown('<div class="big-title">📊 AI CFO Revenue Forecast Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Generate Strategic 2025 Revenue Forecast with AI</div>', unsafe_allow_html=True)

# ---------- INPUT SECTION ----------
col1, col2, col3 = st.columns(3)

with col1:
    revenue_2024 = st.number_input("Revenue 2024 (in Millions)", value=20)

with col2:
    growth_1 = st.slider("Growth Year -1 (%)", 0, 100, 30)

with col3:
    growth_2 = st.slider("Growth Year -2 (%)", 0, 100, 25)

# ---------- GENERATE FORECAST ----------
if st.button("🚀 Generate AI Forecast"):

    prompt = f"""
    You are a CFO.
    Revenue 2024: {revenue_2024}M.
    Growth last 2 years: {growth_1}%, {growth_2}%.
    Forecast 2025 revenue.
    Create 3 scenarios:
    - Conservative
    - Moderate
    - Aggressive
    Provide projected revenue with explanation.
    """

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("📈 AI Forecast Results")
    st.write(response.text)
    st.markdown('</div>', unsafe_allow_html=True)

    # ---------- SIMPLE VISUAL ESTIMATION ----------
    avg_growth = (growth_1 + growth_2) / 2 / 100
    estimated_2025 = revenue_2024 * (1 + avg_growth)

    st.markdown("### 📊 Quick Mathematical Projection")
    st.metric(
        label="Estimated 2025 Revenue (Based on Avg Growth)",
        value=f"{round(estimated_2025,2)} M"
    )