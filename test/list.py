import os
from dotenv import load_dotenv
import google.generativeai as genai

# === Load .env ===
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file!")

# === Configure Gemini ===
genai.configure(api_key=api_key)

# === List Models ===
print("--- Finding models you can use with 'generate_content' ---")
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)
print("---------------------------------------------------------")
print("\nCopy one of the model names above (e.g., 'models/gemini-1.5-flash-latest')")
print("and paste it into your 'test_api.py' file.")