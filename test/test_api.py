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

# === Generate paragraph ===
model = genai.GenerativeModel("models/gemini-2.5-flash")

prompt = (
    "Write a short paragraph (2–3 sentences) describing the biggest challenge "
    "students face with manual or paper-based election processes."
)

response = model.generate_content(prompt)
ai_answer = response.text.strip()

print("AI-generated answer:\n", ai_answer)


