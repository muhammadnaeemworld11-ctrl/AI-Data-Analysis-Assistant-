import os
from openai import OpenAI

# Client ko yahan par initialize NAHI karein. 
# Streamlit Cloud par yeh crash karta hai app start hone par.

def get_client():
    """Yeh function sirf tab chalega jab AI ki zaroorat ho."""
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        return None
    else:
        return OpenAI(
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1",
            http_client=None  # <--- YEH LINE ADD KAREIN!
        )
def ask_ai(question, dataset_summary):
    # Client ko yahan initialize karein, jab user sawal pooche
    client = get_client()
    
    if client is None:
        return "API Key missing. Add OPENROUTER_API_KEY in Streamlit Secrets"
        
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

def get_ai_filter(user_request, columns):
    """Translates natural language into a Pandas query string."""
    # Client ko yahan bhi initialize karein
    client = get_client()
    
    if client is None:
        return None
        
    try:
        response = client.chat.completions.create(
            model="meta-llama/llama-3.1-8b-instruct",
            max_tokens=100,
            temperature=0.1, 
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a Python data expert. Your job is to convert a user's natural language request into a valid Pandas DataFrame query string. "
                        "The DataFrame is named 'df' and has these columns: " + str(columns) + ". "
                        "Output ONLY the query string that goes inside df.query('...'). "
                        "Do not include df.query(), do not include quotes around the whole thing, do not add explanations. "
                        "If the user request is vague or cannot be filtered, output exactly: None"
                    )
                },
                {
                    "role": "user",
                    "content": f"User Request: {user_request}"
                }
            ]
        )
        result = response.choices[0].message.content.strip()
        if result.lower() == "none" or result == "":
            return None
        return result
        
    except Exception as e:
        return None
