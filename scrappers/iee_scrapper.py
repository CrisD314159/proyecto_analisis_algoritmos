"""
Module for ieee scrapper
"""

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv


class IeeeScrapper:
    """
        This class contains all the sage scrapper methods
    """

    def __init__(self):
        load_dotenv()
        self.password = os.getenv("MAIL_PASSWORD")
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--start-maximized")
        self.options.add_experimental_option("detach", True)
        self.options.add_argument("--window-size=1920,1080")
        self.options.add_argument(
            "--disable-blink-features=AutomationControlled")
        self.browser = webdriver.Chrome(options=self.options)
        self.browser.implicitly_wait(60)

    def open_library(self):
        """
        Locates and opens the Scopus database
        """
        self.browser.get("https://library.uniquindio.edu.co/databases")
        wait = WebDriverWait(self.browser, 10)
        science_direct_div = self.browser.find_element(
            By.CSS_SELECTOR, "#facingenieraieeeinstituteofelectricalandelectronicsengineersdescubridor")
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

    def iee_search(self):
        """
        Search for articles on IEEE database
        """
        # Search for computational thinking
        time.sleep(5)
        search_input = self.browser.find_element(
            By.CLASS_NAME, "Typeahead-input")
        search_input.send_keys("computational thinking")
        search_input.send_keys(Keys.RETURN)
        time.sleep(5)

        # close the cookies warning pop-up
        self.browser.find_element(
            By.CLASS_NAME, "osano-cm-save").click()

        # Clicks the items per page button
        combo_button = self.browser.find_element(By.ID, "dropdownPerPageLabel")
        combo_button.click()
        time.sleep(2)

        # Choose the 100 items per page option
        options_container = self.browser.find_element(
            By.CLASS_NAME, "dropdown-menu")
        options_container.find_elements(By.TAG_NAME, "button")[4].click()

        time.sleep(5)

        # Selects all the results (100 in total)
        select_all_checkbox = self.browser.find_element(
            By.CLASS_NAME, "results-actions-selectall-checkbox")
        select_all_checkbox.click()

        try:
            self.process_page()
        except Exception as e:
            print(e)
        # Process 1000 Articles
        for i in range(0, 9):
            print(f"Indexing page {i +1}")
            try:
                next_button_container = self.browser.find_element(
                    By.CLASS_NAME, "next-btn")
                next_button_container.find_element(
                    By.TAG_NAME, "button").click()
                time.sleep(8)

                self.process_page()
            except Exception as e:
                pass
        self.browser.quit()

    def process_page(self):
        """
        Index and downloads 100 articles per page
        """
        select_all_checkbox = self.browser.find_element(
            By.CLASS_NAME, "results-actions-selectall-checkbox")
        select_all_checkbox.click()

        # Clicks the export button
        export_button_list_item = self.browser.find_element(
            By.CLASS_NAME, "export-filter")
        export_button_list_item.find_element(By.TAG_NAME, "button").click()

        # Choose the citations tab
        citations_nav_container = self.browser.find_element(
            By.CLASS_NAME, "nav-tabs")
        citations_nav_item = citations_nav_container.find_elements(
            By.TAG_NAME, "li")[1]

        citations_nav_item.find_element(By.TAG_NAME, "a").click()

        # Selects the citations form container
        citations_form = self.browser.find_element(
            By.CLASS_NAME, "export-form")

        # Selects the bibtext option
        citation_options_cont = citations_form.find_element(
            By.CLASS_NAME, "row")
        citation_section = citation_options_cont.find_elements(By.TAG_NAME, "section")[
            0]
        section_div = citation_section.find_element(By.TAG_NAME, "div")
        button_label = section_div.find_elements(By.TAG_NAME, "label")[1]
        bib_button = button_label.find_element(By.TAG_NAME, "input")
        bib_button.click()

        time.sleep(5)

        # Clicks the download button
        download_button = self.browser.find_element(
            By.CLASS_NAME, "stats-SearchResults_Citation_Download")
        download_button.click()

        time.sleep(3)

        try:

            self.browser.find_element(
                By.CLASS_NAME, "modal").send_keys(Keys.ESCAPE)
        except Exception as e:
            print(e)

        time.sleep(2)

    def run(self):
        """
        This method executes the scrapper
        """
        self.open_library()
        self.google_login()
        self.iee_search()
