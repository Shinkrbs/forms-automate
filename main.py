import time
from config import FORM_URL, PROMPTS, RATINGS, GEMINI_MODEL
from utils import setup_driver, setup_gemini
from bot import FormBot

def main():
    """
    Main function to initialize and run the form-filling bot.
    """
    driver = None  # Initialize driver to None for the 'finally' block
    try:
        print("Setting up Gemini AI...")
        model = setup_gemini(GEMINI_MODEL)
        
        print("Setting up Web Driver...")
        driver, wait = setup_driver(FORM_URL)
        
        # Initialize the bot with all its dependencies
        bot = FormBot(driver, wait, model, PROMPTS, RATINGS)
        
        # Run the main automation process
        print("Bot is starting...")
        bot.run()

    except Exception as e:
        print(f"A critical error occurred in main: {e}")
        if driver:
             # Save a screenshot on error for debugging
            driver.save_screenshot("error_screenshot.png")
            print("Saved 'error_screenshot.png' for debugging.")
    finally:
        if driver:
            print("Process finished. Closing driver in 5 seconds...")
            time.sleep(5)
            driver.quit()
        else:
            print("Driver failed to initialize.")

if __name__ == "__main__":
    main()