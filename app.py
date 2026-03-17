import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv(dotenv_path=".env")

print("Loaded API Key:", os.getenv("OPENAI_API_KEY"))

# Create OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("AI Sales Call Analyzer")

transcript = st.text_area(
    "Paste a sales call transcript",
    height=300
)

def analyze_transcript(transcript):

    prompt = f"""
You are an expert AI sales coach.

Analyze the transcript and return:

## Call Summary
## Customer Objections
## Buying Signals
## Recommended Next Steps
## Deal Risk Score (Low / Medium / High)
## Reason for Risk Score
## Draft Follow-Up Email

Transcript:
{transcript}
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text


if st.button("Analyze Call"):
    if transcript.strip():
        result = analyze_transcript(transcript)
        st.markdown(result)
    else:
        st.warning("Please paste a transcript first.")