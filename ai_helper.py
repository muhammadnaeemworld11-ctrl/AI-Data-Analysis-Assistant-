import os
import streamlit as st
from openai import OpenAI

try:
    api_key = st.secrets["OPENROUTER_API_KEY"]
except:
    from dotenv import load_dotenv
    load_dotenv()
    api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    client = None
else:
    client = OpenAI(
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1",
        default_headers={
            "HTTP-Referer": "https://your-streamlit-app-url.com", 
            "X-Title": "AI Data Analysis Assistant"
        }
    )

def ask_ai(question, dataset_summary):
    if client is None:
        return "API Key missing. Add OPENROUTER_API_KEY to Streamlit Cloud Secrets (or local .env file)."
        
    try:
        response = client.chat.completions.create(
            model="meta-llama/llama-3.1-8b-instruct", 
            max_tokens=500, 
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert Data Analysis Assistant. "
                        "Analyze datasets, explain insights, and provide useful suggestions. "
                        "Keep your answers brief and to the point."
                    )
                },
                {
                    "role": "user",
                    "content": f"""
Dataset Summary:
{dataset_summary}

Question:
{question}

Answer clearly and briefly.
"""
                }
            ],
            temperature=0.3
        )
        return response.choices[0].message.content
        
    except Exception as e:
        return f"AI Error: {e}"
