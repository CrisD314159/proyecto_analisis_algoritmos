"""
    This module uses a class to scrape the Scopus Database
"""
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from dotenv import load_dotenv


class ScopusScraper:
    """
        This class contains all the scopus scrapper methods
    """

    def __init__(self):
        load_dotenv()
        self.password = os.getenv("MAIL_PASSWORD")
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.options.add_argument("--window-size=1920,1080")
        self.browser = webdriver.Chrome(options=self.options)
        self.browser.implicitly_wait(60)
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

        time.sleep(20)
        search_input = self.browser.find_element(By.ID, "qs")
        search_input.send_keys("computational thinking")
        search_input.send_keys(Keys.RETURN)

        time.sleep(5)

        load_more_list = self.browser.find_element(
            By.CLASS_NAME, "ResultsPerPage")
        list_items = load_more_list.find_elements(By.TAG_NAME, "li")
        find_100_a = list_items[2].find_element(By.TAG_NAME, "a")
        find_100_a.click()

        time.sleep(5)

        checkbox = self.browser.find_element(
            By.CLASS_NAME, "result-header-controls-container")
        checkbox.find_element(By.TAG_NAME, "span").click()

        self.browser.find_element(
            By.CLASS_NAME, "export-all-link-button").click()
        export_ris = self.browser.find_element(By.CLASS_NAME, "preview-body")
        export_ris.find_elements(By.TAG_NAME, "button")[
            2].click()  # [1] for ris, 2 for bibtex

        count = 0
        while count < 3:
            count += 1

            self.browser.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(4)
            pagination_list = self.browser.find_element(
                By.CLASS_NAME, "next-link")
            list_pagination = pagination_list.find_element(By.TAG_NAME, "a")
            list_pagination.click()
            time.sleep(6)
            self.browser.refresh()
            checkbox = self.browser.find_element(
                By.CLASS_NAME, "result-header-controls-container")
            checkbox.find_element(By.TAG_NAME, "span").click()

            self.browser.find_element(
                By.CLASS_NAME, "export-all-link-button").click()
            export_ris = self.browser.find_element(
                By.CLASS_NAME, "preview-body")
            export_ris.find_elements(By.TAG_NAME, "button")[
                2].click()  # [1] for ris, 2 for bibtex

        time.sleep(2)

    def run(self):
        """
        Runs the scrapper
        """
        self.open_library()
        self.google_login()
        self.search_articles()
