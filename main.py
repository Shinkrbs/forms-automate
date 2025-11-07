from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import time
import google.generativeai as genai

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSeH2B8F02QPETKaw27JlJtXsdME85-eumQyE-DEpt_2Fz15bA/viewform?usp=header&hl=en"

# Setup Gemini AI
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file.")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("models/gemini-2.5-flash")


def main():

    # Setup Firefox Driver
    driver = webdriver.Firefox()
    driver.get(FORM_URL)
    wait = WebDriverWait(driver, 20)

    # Prompts
    prompts = [
        "Imagine you are a student leader in visayas state university, provide a simple response (1-2 sentences) to the question: What is the biggest challenge you face with the current manual / paper-based election process?",
        "Imagine you are a student leader in visayas state university, provide a simple response (1) to the question: Are there any missing features that should included? If yes, please describe the feature(s). The features was Election Creation, Voter List Management, Candidate Registration, Partylist Management, Position Templates, Position Requirements, Voter Authentication, Code Distribution, Secure Voting, Preventing Double Votes, Automatic Tallying, Live Results Display, Election Status Page, and Official Reports. If you think the features are good indicate None do not overcomplicate the features you suggest just make it simple",
        "Imagine you are a student leader in visayas state university, provide a simple response (1-2 sentences) to this question: What is you biggest concern about switching to this new online election system? Make the response human-like and don't use deep words make it seem like a random student just answerd the question"
    ]

    ratings = {
        "Election Creation": "5 (Essential)",
        "Voter List Management": "5 (Essential)",
        "Candidate Registration": "5 (Essential)",
        "Partylist Management": "5 (Essential)",
        "Position Templates": "5 (Essential)",
        "Position Requirements": "5 (Essential)",
        "Voter Authentication": "5 (Essential)",
        "Code Distribution": "5 (Essential)",
        "Secure Voting": "5 (Essential)",
        "Preventing Double Votes": "5 (Essential)",
        "Automatic Tallying": "5 (Essential)",
        "Live Results Display": "5 (Essential)",
        "Election Status Page": "5 (Essential)",
        "Official Reports": "5 (Essential)"
    }

    response = ""
    process(wait, prompts, response, model, ratings)
    driver.quit()


def process(wait, prompt, response, model, ratings):

    # First Section
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@role='radio' and contains(@aria-label, 'I consent and wish to proceed')]"))).click()
    time.sleep(0.5)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='Next']/ancestor::div[@role='button']"))).click()

    time.sleep(1.5)

    # Second Section
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@role='radio' and contains(@aria-label, 'Student Organization Executive Officer')]"))).click()

    # wait.until(EC.element_to_be_clickable(
    #     (By.XPATH, "//div[@role='radio' and contains(@aria-label, 'Student Organization Executive Member')]"))).click()
    time.sleep(0.5)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@role='checkbox' and contains(@aria-label, 'Smartphone')]"))).click()
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@role='checkbox' and contains(@aria-label, 'Laptop / Desktop')]"))).click()
    # wait.until(EC.element_to_be_clickable(
    #     (By.XPATH, "//div[@role='checkbox' and contains(@aria-label, 'Tablet')]"))).click()
    time.sleep(1)

    # wait.until(EC.element_to_be_clickable(
    #     (By.XPATH, "//div[@role='radio' and contains(@aria-label, 'Voted in person (paper ballot)')]"))).click()
    # wait.until(EC.element_to_be_clickable(
    #     (By.XPATH, "//div[@role='radio' and contains(@aria-label, 'Run as candidate')]"))).click()
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@role='radio' and contains(@aria-label, 'Helped organize / count votes')]"))).click()
    # wait.until(EC.element_to_be_clickable(
    #     (By.XPATH, "//div[@role='radio' and contains(@aria-label, 'I have not participated in any VSU student organization election')]"))).click()

    response = model.generate_content(prompt[0])
    ai_answer = response.text.strip()
    print("Answer One:\n", ai_answer)

    text_box = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//textarea[@aria-label='Your answer']")))
    text_box.send_keys(ai_answer)
    time.sleep(1)

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='Next']/ancestor::div[@role='button']"))).click()
    time.sleep(1.5)

    # Third Section
    # wait for the first rating to load
    wait.until(EC.presence_of_element_located(
        (By.XPATH, "//div[contains(@aria-label, 'Election Creation') and @role='radiogroup']")))
    for feature, score in ratings.items():
        xpath = f"//div[@role='radiogroup' and contains(@aria-label, '{feature}')]//div[@role='radio' and @data-value='{score}']"
        element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()
        time.sleep(0.5)

    text_boxes = wait.until(EC.presence_of_all_elements_located(
        (By.XPATH, "//textarea[@aria-label='Your answer']")))

    response = model.generate_content(prompt[1])
    ai_answer = response.text.strip()
    print("Answer Two:\n", ai_answer)
    text_boxes[0].send_keys(ai_answer)
    time.sleep(1)

    response = model.generate_content(prompt[2])
    ai_answer = response.text.strip()
    print("Answer Three:\n", ai_answer)
    text_boxes[1].send_keys(ai_answer)
    time.sleep(1)

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='Next']/ancestor::div[@role='button']"))).click()
    time.sleep(1.5)

    # Fourth Section
    # wait.until(EC.element_to_be_clickable(
    #     (By.XPATH, "//div[@role='radio' and contains(@aria-label, 'Once per academic year')]"))).click()
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@role='radio' and contains(@aria-label, 'Twice per academic year (once per semester)')]"))).click()
    # wait.until(EC.element_to_be_clickable(
    #     (By.XPATH, "//div[@role='radio' and contains(@aria-label, 'Rarely / only for special elections')]"))).click()
    time.sleep(0.5)
    # wait.until(EC.element_to_be_clickable(
    #     (By.XPATH, "//div[@role='radio' and contains(@aria-label, 'No, we only use paper ballots and manual counting')]"))).click()
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@role='radio' and contains(@aria-label, 'Yes, we use Google Forms')]"))).click()
    # wait.until(EC.element_to_be_clickable(
    #     (By.XPATH, "//div[@role='radio' and contains(@aria-label, 'Yes, we use other online survey tools')]"))).click()
    time.sleep(0.5)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@role='radio' and contains(@aria-label, '3')]"))).click()
    time.sleep(0.5)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@role='radio' and contains(@aria-label, 'Pay-per-election (One payment for each election created)')]"))).click()
    time.sleep(0.5)

    # wait.until(EC.element_to_be_clickable(
    #     (By.XPATH, "//div[@role='radio' and contains(@aria-label, 'Free')]"))).click()
    # wait.until(EC.element_to_be_clickable(
    #     (By.XPATH, "//div[@role='radio' and contains(@aria-label, 'Less than 100')]"))).click()
    # wait.until(EC.element_to_be_clickable(
    #     (By.XPATH, "//div[@role='radio' and contains(@aria-label, '100-300')]"))).click()
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@role='radio' and contains(@aria-label, '301-500')]"))).click()
    # wait.until(EC.element_to_be_clickable(
    #     (By.XPATH, "//div[@role='radio' and contains(@aria-label, 'More than 500')]"))).click()
    time.sleep(0.5)

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@role='checkbox' and contains(@aria-label, 'Price')]"))).click()
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@role='checkbox' and contains(@aria-label, 'Features')]"))).click()
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@role='checkbox' and contains(@aria-label, 'Ease of use')]"))).click()
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@role='checkbox' and contains(@aria-label, 'Performance and Reliablity')]"))).click()
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@role='checkbox' and contains(@aria-label, 'Security and Privacy')]"))).click()
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@role='checkbox' and contains(@aria-label, 'Customer Support')]"))).click()
    time.sleep(1)

    print("Submitting the form...")
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='Submit']/ancestor::div[@role='button']"))).click()

    # Final Section
    wait.until(EC.presence_of_element_located(
        (By.XPATH, "//*[contains(text(), 'Your response has been recorded')]")))
    print("Successfully submitted form!")


if __name__ == "__main__":
    main()
