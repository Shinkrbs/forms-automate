import os
import google.generativeai as genai
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def setup_gemini(model_name):
    # Setup Gemini AI
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in .env file.")

    genai.configure(api_key=api_key)

    try:
        model = genai.GenerativeModel(model_name)
        return model
    except Exception as e:
        print(f"Error initializing model '{model_name}': {e}")
        print("Falling back to 'gemini-1.5-pro-latest'")
        return genai.GenerativeModel("gemini-1.5-pro-latest")


def setup_driver(form_url, wait_timeout=20):
    # Setup Firefox Driver
    driver = webdriver.Firefox()
    driver.get(form_url)
    wait = WebDriverWait(driver, wait_timeout)
    return driver, wait
