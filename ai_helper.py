import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
client = None
init_error = None

if api_key:
    try:
        from openai import OpenAI
        client = OpenAI(
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1",
        )
    except Exception as e:
        # If the library fails to initialize, catch it so the app doesn't crash
        client = None
        init_error = str(e)

def ask_ai(question, dataset_summary):
    if client is None:
        if not api_key:
            return "⚠️ API Key missing. Add OPENROUTER_API_KEY in .env or Streamlit Secrets."
        elif init_error:
            return f"⚠️ AI Client failed to initialize (Library Error): {init_error}"
        
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
        return f"⚠️ AI Error: {e}"
