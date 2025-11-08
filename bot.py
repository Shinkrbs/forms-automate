from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time


class FormBot:
    def __init__(self, driver, wait, model, prompts, ratings):
        self.driver = driver
        self.wait = wait
        self.model = model
        self.prompts = prompts
        self.ratings = ratings
        self.response = ""

    def run(self):

        # First Section
        print("Page 1: Consenting...")
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@role='radio' and contains(@aria-label, 'I consent and wish to proceed')]"))).click()
        time.sleep(0.5)
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='Next']/ancestor::div[@role='button']"))).click()

        time.sleep(1.5)

        # Second Section
        print("Page 2: Filling role, experience, and first question...")
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@role='radio' and contains(@aria-label, 'Student Organization Executive Officer')]"))).click()
        time.sleep(0.5)

        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@role='checkbox' and contains(@aria-label, 'Smartphone')]"))).click()
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@role='checkbox' and contains(@aria-label, 'Laptop / Desktop')]"))).click()
        time.sleep(1)

        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@role='radio' and contains(@aria-label, 'Helped organize / count votes')]"))).click()

        print("  Generating Answer 1...")
        self.response = self.model.generate_content(self.prompts[0])
        ai_answer = self.response.text.strip()
        print("  Answer One:\n  ", ai_answer.replace("\n", "\n  "))

        text_box = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//textarea[@aria-label='Your answer']")))
        text_box.send_keys(ai_answer)
        time.sleep(1)

        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='Next']/ancestor::div[@role='button']"))).click()
        time.sleep(1.5)

        # Third Section
        print("Page 3: Filling ratings and text questions...")
        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@aria-label, 'Election Creation') and @role='radiogroup']")))

        print("  Filling feature ratings...")
        for feature, score in self.ratings.items():
            try:
                xpath = f"//div[@role='radiogroup' and contains(@aria-label, '{feature}')]//div[@role='radio' and @data-value='{score}']"
                element = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, xpath)))
                element.click()
                time.sleep(0.5)
            except (TimeoutException, NoSuchElementException):
                print(
                    f"  Warning: Could not find rating for '{feature}'. Skipping.")

        text_boxes = self.wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//textarea[@aria-label='Your answer']")))

        print("  Generating Answer 2...")
        self.response = self.model.generate_content(self.prompts[1])
        ai_answer = self.response.text.strip()
        print("  Answer Two:\n  ", ai_answer.replace("\n", "\n  "))
        text_boxes[0].send_keys(ai_answer)
        time.sleep(1)

        print("  Generating Answer 3...")
        self.response = self.model.generate_content(self.prompts[2])
        ai_answer = self.response.text.strip()
        print("  Answer Three:\n  ", ai_answer.replace("\n", "\n  "))
        text_boxes[1].send_keys(ai_answer)
        time.sleep(1)

        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='Next']/ancestor::div[@role='button']"))).click()
        time.sleep(1.5)

        # Fourth Section
        # self.wait.until(EC.element_to_be_clickable(
        #     (By.XPATH, "//div[@role='radio' and contains(@aria-label, 'Once per academic year')]"))).click()
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@role='radio' and contains(@aria-label, 'Twice per academic year (once per semester)')]"))).click()
        # self.wait.until(EC.element_to_be_clickable(
        #     (By.XPATH, "//div[@role='radio' and contains(@aria-label, 'Rarely / only for special elections')]"))).click()
        time.sleep(0.5)
        # wait.until(EC.element_to_be_clickable(
        #     (By.XPATH, "//div[@role='radio' and contains(@aria-label, 'No, we only use paper ballots and manual counting')]"))).click()
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@role='radio' and contains(@aria-label, 'Yes, we use Google Forms')]"))).click()
        # wait.until(EC.element_to_be_clickable(
        #     (By.XPATH, "//div[@role='radio' and contains(@aria-label, 'Yes, we use other online survey tools')]"))).click()
        time.sleep(0.5)
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@role='radio' and contains(@aria-label, '3')]"))).click()
        time.sleep(0.5)
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@role='radio' and contains(@aria-label, 'Pay-per-election (One payment for each election created)')]"))).click()
        time.sleep(0.5)

        # wait.until(EC.element_to_be_clickable(
        #     (By.XPATH, "//div[@role='radio' and contains(@aria-label, 'Free')]"))).click()
        # wait.until(EC.element_to_be_clickable(
        #     (By.XPATH, "//div[@role='radio' and contains(@aria-label, 'Less than 100')]"))).click()
        # wait.until(EC.element_to_be_clickable(
        #     (By.XPATH, "//div[@role='radio' and contains(@aria-label, '100-300')]"))).click()
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@role='radio' and contains(@aria-label, '301-500')]"))).click()
        # wait.until(EC.element_to_be_clickable(
        #     (By.XPATH, "//div[@role='radio' and contains(@aria-label, 'More than 500')]"))).click()
        time.sleep(0.5)

        print("  Clicking final checkboxes...")
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@role='checkbox' and contains(@aria-label, 'Price')]"))).click()
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@role='checkbox' and contains(@aria-label, 'Features')]"))).click()
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@role='checkbox' and contains(@aria-label, 'Ease of use')]"))).click()
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@role='checkbox' and contains(@aria-label, 'Performance and Reliablity')]"))).click()
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@role='checkbox' and contains(@aria-label, 'Security and Privacy')]"))).click()
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@role='checkbox' and contains(@aria-label, 'Customer Support')]"))).click()
        time.sleep(1)

        # Final Section
        print("Submitting the form...")
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='Submit']/ancestor::div[@role='button']"))).click()
        print("Successfully submitted form!")
