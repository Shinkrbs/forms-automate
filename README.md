# Google Form Automation Bot

This project is a Python bot that automatically fills out a specific Google Form multiple times. It uses Selenium for web browser automation and the Google Gemini API to generate unique, human-like answers for the text-based questions.

## Features

* **Automated Form Submission**: Fills out a multi-page Google Form from start to finish.

* **AI-Powered Answers**: Uses the Google Gemini API to generate unique responses for open-ended questions.

* **Multi-Run Capability**: The main script can be configured to run `N` times, submitting the form multiple times in a row.

* **Handles Various Inputs**: Fills out radio buttons, checkboxes, multi-selects, text areas, and grid-based ratings.

* **Clean Code Structure**: The project is split into logical files:

  * `main.py`: The main entry point. Handles setup, teardown, and looping.

  * `bot.py`: Contains the `FormBot` class with all the core automation logic.

  * `config.py`: Stores all constants like the form URL, AI prompts, and ratings.

  * `utils.py`: Contains helper functions for setting up the AI model and Selenium driver.

## Tech Stack

* [Python](https://www.python.org/)

* [Selenium](https://www.selenium.dev/) for browser automation.

* [google-generativeai](https://pypi.org/project/google-generativeai/) for access to the Gemini API.

* [python-dotenv](https://pypi.org/project/python-dotenv/) for managing environment variables.

* **Firefox** & **Geckodriver**

## Setup and Installation

### 1. Clone the Repository
```
git clone [https://github.com/Shinkrbs/forms-automate.git](https://github.com/Shinkrbs/forms-automate.git)
cd forms-automate
```

### 2. Install Python Dependencies

It's highly recommended to use a virtual environment:

```
# Create a virtual environment (macOS/Linux)
python3 -m venv venv
source venv/bin/activate

# Create a virtual environment (Windows)
python -m venv venv
.\venv\Scripts\activate

# Install the required packages
pip install -r requirements.txt
```

### 3. Install the Web Driver (Geckodriver)

This script is configured to use **Firefox**, so you need `geckodriver`.

1. **Download**: Download the latest `geckodriver` for your operating system from the [official releases page](https://github.com/mozilla/geckodriver/releases).

2. **Install**: Unzip the file and move the `geckodriver` executable to a location in your system's `PATH`.

   * **macOS/Linux**: A good place is `/usr/local/bin/`.

     ```
     sudo mv geckodriver /usr/local/bin/
     
     
     
     ```

   * **Windows**: You can add the folder where you extracted `geckodriver` to your system's "Environment Variables" PATH.

**IMPORTANT**: Your `geckodriver` version **must** be compatible with your installed Firefox version. If you get errors, the first thing to check is this mismatch.

## Configuration

Before running the script, you must provide your Google Gemini API key.

1. Create a new file named `.env` in the root of the project directory.

2. Add your API key to this file:

```
GEMINI_API_KEY="your_actual_api_key_goes_here"
```

## Adapting for Your Own Survey

**This bot is hard-coded to work with a *specific* Google Form.**

If you want to run this bot on your own survey, you will need to:

1. **Update `config.py`**: Change the `FORM_URL` to your new form's URL. You should also update the `PROMPTS` and `RATINGS` variables to match the questions on your form.

2. **Modify `bot.py`**: This is the most important step. You must open `bot.py` and change the `By.XPATH` strings in the `run()` method to match the elements on your new form. You will need to inspect your form's HTML to find the correct `aria-label`, `data-value`, or text for each element.

## How to Run

With your virtual environment active and your `.env` file in place, simply run `main.py`:

```
python main.py
```
Specify how many times you want the script to run by changing num_runs in 'main.py'.