
#------------------------ IMPORTS---------------------------
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.edge.service import Service
import time
import random


#--------- BROWSER CONFIGURATION - Anti-Detection Setup -----

options = Options()

# Keep browser open after script execution
options.add_experimental_option("detach", True)

# Remove automation indicators
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")

# Mimic real user with standard user-agent
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")


#-------------------- WEBDRIVER INITIALIZATION -----------------------
driver = webdriver.Chrome(options=options)

# Override navigator.webdriver property to avoid bot detection
# use execute_cdp_cmd to ensure this script runs before any page loads
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined
        })
    """
})



# -------- FILE HANDLING - Read Questions from Text File -----------
questions = []
with open('questions.txt','r') as file:
    for line in file:
        question = line.strip()
        if question:
            questions.append(question)


# -------- AUTOMATION LOOP - Search Each Question on Google --------

for question in questions:

    # Navigate to Google homepage
    driver.get('https://google.com/')

    # Locate search box using CSS selector
    search = driver.find_element(By.CSS_SELECTOR,"#APjFqb")
    time.sleep(1)

    # Type the question into search box
    search.send_keys(question)
    time.sleep(1)

    # Trigger search by pressing Enter
    search.send_keys(Keys.ENTER)
    time.sleep(1)

    # Open new tab for next question
    driver.switch_to.new_window('tab')


