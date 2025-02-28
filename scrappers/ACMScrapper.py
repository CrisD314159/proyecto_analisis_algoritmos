"""
This module uses a class to scrape the ACM Databas for research papers, 
it downloads the papers in a bib file
"""

import time
import random
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv


class ACMScrapper:
    """
      Scrapper class for the ACM Database
    """

    def __init__(self):
        load_dotenv()
        self.password = os.getenv("MAIL_PASSWORD")
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--start-maximized")
        self.options.add_experimental_option("detach", True)

        # Add realistic user agent
        self.options.add_argument(
            "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

        # Add language preferences
        self.options.add_argument("--lang=en-US,en;q=0.9")

        # Set window size to realistic dimensions
        self.options.add_argument("--window-size=1920,1080")

        # Avoid detection
        self.options.add_argument(
            "--disable-blink-features=AutomationControlled")
        self.options.add_argument("--disable-gpu")
        self.options.add_experimental_option(
            "excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option("useAutomationExtension", False)

        self.browser = webdriver.Chrome(options=self.options)
        self.browser.execute_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        # Additional navigator properties to spoof
        self.browser.execute_script(
            "Object.defineProperty(navigator, 'maxTouchPoints', {get: () => 5});")
        self.browser.execute_script(
            "Object.defineProperty(navigator, 'hardwareConcurrency', {get: () => 8});")

        self.browser.implicitly_wait(10)

    def open_library(self):
        """
         Locates a opens the ACM database
        """
        self.browser.get("https://library.uniquindio.edu.co/databases")
        wait = WebDriverWait(self.browser, 10)
        science_direct_div = self.browser.find_element(
            By.CSS_SELECTOR, "#facingenieraacmdigitallibrary")
        divlink = wait.until(
            lambda browser: science_direct_div.find_element(By.CSS_SELECTOR, "a"))
        self.browser.get(divlink.get_attribute("href"))

    def simulate_human_behavior(self):
        """
        Method to wait between page loads
        """
        # Random sleep between actions
        time.sleep(random.uniform(2, 4))

    def acm_search(self):
        """
        Search for computational thinking papers in the ACM database, 
        then it downloads the papers in a bib file
        """
        try:

            # Handle Cloudflare challenge if present
            try:
                cloudflare_checkbox = self.browser.find_element(
                    By.CLASS_NAME, "cb-c")
                print(cloudflare_checkbox.tag_name)
                # Move mouse before clicking to simulate human

                cloudflare_checkbox.find_element(By.TAG_NAME, "input").click()
            except:
                # If the Cloudflare checkbox isn't found, continue
                pass

            # Search with human-like typing
            search_input = WebDriverWait(self.browser, 5).until(
                lambda browser: browser.find_element(By.NAME, "AllField")
            )
            print(search_input.id)
            search_input.send_keys("computational thinking")
            self.simulate_human_behavior()
            search_input.send_keys(Keys.RETURN)

            # Click on the select all

            checkbox_input = self.browser.find_element(
                By.CSS_SELECTOR, "input[name='markall']")
            self.browser.execute_script(
                "arguments[0].click();", checkbox_input)

            self.simulate_human_behavior()
            buttons_div = self.browser.find_element(
                By.CLASS_NAME, "item-results__buttons")
            buttons = buttons_div.find_elements(By.TAG_NAME, "a")
            buttons[0].click()

            self.simulate_human_behavior()
            self.browser.find_element(
                By.CLASS_NAME, "download__btn").click()

            self.simulate_human_behavior()
            self.browser.quit()
        except Exception as e:
            print(f"Error during search: {e}")

    def run(self):
        """
        Method to run the scrapper
        """
        self.open_library()
        self.acm_search()
