"""
    This module uses a class to scrape the Scopus Database
"""
import os
import time
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from dotenv import load_dotenv


class ScopusScraper:
    """
        This class contains all the scopus scrapper methods
    """

    def __init__(self, use_undetected=True, profile_path=None):
        """
        Initialize the scrapper
        """
        load_dotenv()
        self.password = os.getenv("MAIL_PASSWORD")
        if use_undetected:
            # Use undetected-chromedriver which is built to bypass detections
            if profile_path:
                self.options = uc.ChromeOptions()
                self.options.add_argument(f"--user-data-dir={profile_path}")
                self.browser = uc.Chrome(options=self.options)
            else:
                self.browser = uc.Chrome()
        else:
            # Original approach with added protections
            self.options = webdriver.ChromeOptions()

            # Add user data directory if provided
            if profile_path:
                self.options.add_argument(f"--user-data-dir={profile_path}")

            # Standard anti-detection measures
            self.options.add_argument("--start-maximized")
            self.options.add_experimental_option("detach", True)

            # Add realistic user agent
            self.options.add_argument(
                "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

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
            self.options.add_experimental_option(
                "useAutomationExtension", False)

            # Add additional arguments that may help
            self.options.add_argument("--no-sandbox")
            self.options.add_argument("--disable-dev-shm-usage")

            # Add preferences to mimic human browser settings
            prefs = {
                "profile.default_content_setting_values.notifications": 2,
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
                "profile.default_content_settings.popups": 0
            }
            self.options.add_experimental_option("prefs", prefs)

            self.browser = webdriver.Chrome(options=self.options)

            # Execute scripts to avoid detection
            self.browser.execute_script(
                "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            self.browser.execute_script(
                "Object.defineProperty(navigator, 'maxTouchPoints', {get: () => 5});")
            self.browser.execute_script(
                "Object.defineProperty(navigator, 'hardwareConcurrency', {get: () => 8});")

            # Additional anti-detection scripts
            self.browser.execute_script(
                "Object.defineProperty(navigator, 'plugins', {get: function() { return [1, 2, 3, 4, 5]; }});")
            self.browser.execute_script(
                "Object.defineProperty(navigator, 'languages', {get: function() { return ['en-US', 'en']; }});")

        self.browser.implicitly_wait(10)
        self.action_chains = ActionChains(self.browser)

    def open_library(self):
        """
        Locates and opens the Scopus database
        """
        self.browser.get("https://library.uniquindio.edu.co/databases")
        wait = WebDriverWait(self.browser, 10)
        science_direct_div = self.browser.find_element(
            By.CSS_SELECTOR, "#facingenierasciencedirectconsorciocolombiadescubridor")
        divlink = wait.until(
            lambda browser: science_direct_div.find_element(By.CSS_SELECTOR, "a"))
        self.browser.get(divlink.get_attribute("href"))

    def google_login(self):
        """
        Logs into google account
        """
        self.browser.find_element(By.ID, "btn-google").click()
        self.browser.find_element(By.TAG_NAME, "input").send_keys(
            "cristiand.vargasl@uqvirtual.edu.co")
        self.browser.find_element(By.ID, "identifierNext").find_element(
            By.TAG_NAME, "button").click()
        self.browser.find_element(By.NAME, "Passwd").send_keys(self.password)
        self.browser.find_element(By.ID, "passwordNext").find_element(
            By.TAG_NAME, "button").click()

    def search_articles(self):
        """
        Searches for articles in the database related to computational thinking
        """
        # Set up explicit wait
        wait = WebDriverWait(self.browser, 30)

        time.sleep(20)
        search_input = self.browser.find_element(By.ID, "qs")
        search_input.send_keys("computational thinking")
        search_input.send_keys(Keys.RETURN)

        time.sleep(5)

        # Set to show 100 results per page
        load_more_list = self.browser.find_element(
            By.CLASS_NAME, "ResultsPerPage")
        list_items = load_more_list.find_elements(By.TAG_NAME, "li")
        find_100_a = list_items[2].find_element(By.TAG_NAME, "a")
        find_100_a.click()

        time.sleep(5)

        # Process first page
        try:
            self.process_page()
        except Exception as e:
            print(f"Error processing first page: {e}")

        # Process subsequent pages
        for i in range(0, 10):
            try:
                print(f"Processing page {i+1}")

                # Scroll to bottom of page to find pagination
                self.browser.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(4)

                # Find and click next page button
                pagination_list = wait.until(
                    lambda browser: browser.find_element(
                        By.CLASS_NAME, "next-link")
                )
                list_pagination = pagination_list.find_element(
                    By.TAG_NAME, "a")
                list_pagination.click()

                # Wait for page to load
                time.sleep(8)

                # Process the new page
                self.process_page()

            except Exception as e:
                print(f"Error on page {i+1}: {e}")
                # Take screenshot for debugging
                continue

        time.sleep(2)
        self.browser.quit()

    def process_page(self):
        """
        Process a single page of results - select all, export, and uncheck
        """
        wait = WebDriverWait(self.browser, 30)

        # Find and click the checkbox to select all
        try:
            checkbox_container = wait.until(
                lambda browser: browser.find_element(
                    By.CLASS_NAME, "result-header-controls-container")
            )
            checkbox = checkbox_container.find_element(By.TAG_NAME, "span")
            wait.until(lambda browser: checkbox.is_displayed())
            checkbox.click()
            print("Selected all items")
        except Exception as e:
            print(f"Error selecting all items: {e}")
            raise

        time.sleep(2)

        # Click export button
        try:
            export_button = wait.until(
                lambda browser: browser.find_element(
                    By.CLASS_NAME, "export-all-link-button")
            )
            export_button.click()
            print("Clicked export button")
        except Exception as e:
            print(f"Error clicking export button: {e}")
            raise

        time.sleep(5)

        # Click bibtex export option
        try:

            time.sleep(10)
            export_dialog = wait.until(
                lambda browser: browser.find_element(
                    By.CLASS_NAME, "ExportCitationOptions")
            )
            export_options_container = export_dialog.find_element(
                By.CLASS_NAME, "preview-body")

            export_buttons = export_options_container.find_elements(
                By.TAG_NAME, "button")

            if len(export_buttons) >= 3:
                export_buttons[2].click()  # [1] for ris, 2 for bibtex
                print("Clicked bibtex export button")
            else:
                print(
                    f"Not enough export buttons found. Found {len(export_buttons)}")
                raise Exception("Export buttons not found")
        except Exception as e:
            print(f"Error during export: {e}")
            raise

        time.sleep(3)

        # Uncheck the "select all" checkbox
        try:
            checkbox_container = wait.until(
                lambda browser: browser.find_element(
                    By.CLASS_NAME, "result-header-controls-container")
            )
            checkbox = checkbox_container.find_element(By.TAG_NAME, "span")
            checkbox.click()
            print("Unchecked all items")
        except Exception as e:
            print(f"Error unchecking items: {e}")
            # Don't raise here, as we want to continue to the next page

        time.sleep(2)

    def run(self):
        """
        Runs the scrapper
        """
        self.open_library()
        self.google_login()
        self.search_articles()
