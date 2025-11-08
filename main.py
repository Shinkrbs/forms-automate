import time
from config import FORM_URL, PROMPTS, RATINGS, GEMINI_MODEL
from utils import setup_driver, setup_gemini
from bot import FormBot


def run_bot_once(run_number, model):

    driver = None
    print(f"\n--- [Run {run_number}] Starting ---")
    print(f"[Run {run_number}] Setting up Web Driver...")
    driver, wait = setup_driver(FORM_URL)

    bot = FormBot(driver, wait, model, PROMPTS, RATINGS)

    print(f"[Run {run_number}] Bot is running...")
    bot.run()

    if driver:
        print(
            f"[Run {run_number}] Process finished. Closing driver immediately.")
        driver.quit()
    else:
        print(f"[Run {run_number}] Driver failed to initialize.")

    print(f"--- [Run {run_number}] Complete ---")


def main():

    num_runs = 13
    model = setup_gemini(GEMINI_MODEL)

    for i in range(num_runs):
        run_bot_once(i + 1, model)

        if i < num_runs - 1:
            print(f"Pausing for 1 second before next run...")
            time.sleep(1)

    print("\nAll bot runs are complete.")


if __name__ == "__main__":
    main()
