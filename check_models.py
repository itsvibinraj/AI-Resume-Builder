# check_models.py
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

try:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    print("Successfully configured API key.")
    print("-" * 20)
    print("Available models:")

    for m in genai.list_models():
        # Check if the model supports the 'generateContent' method
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)

except Exception as e:
    print(f"An error occurred: {e}")