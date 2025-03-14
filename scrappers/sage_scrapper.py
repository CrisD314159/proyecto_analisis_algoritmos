"""
This module uses a class to scrape the Sage Database
"""
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from selenium.webdriver.support.ui import Select


class SageScraper:
    """
        This class contains all the sage scrapper methods
    """

    def __init__(self):
        load_dotenv()
        self.password = os.getenv("MAIL_PASSWORD")
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(options=self.options)
        self.browser.implicitly_wait(60)

    def open_library(self):
        """
        Locates and opens the Scopus database
        """
        self.browser.get("https://library.uniquindio.edu.co/databases")
        wait = WebDriverWait(self.browser, 10)
        science_direct_div = self.browser.find_element(
            By.CSS_SELECTOR, "#facingenierasagerevistasconsorciocolombiadescubridor")
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

        cookies_btn = self.browser.find_element(
            By.ID, "onetrust-accept-btn-handler")
        cookies_btn.click()

        search_input = self.browser.find_element(
            By.ID, "AllField35ea26a9-ec16-4bde-9652-17b798d5b6750")
        search_input.send_keys("computational thinking")
        search_input.send_keys(Keys.RETURN)

        time.sleep(5)

        cookies_btn2 = self.browser.find_element(
            By.ID, "onetrust-accept-btn-handler")
        cookies_btn2.click()

        checkbox = self.browser.find_element(By.ID, "action-bar-select-all")
        checkbox.click()

        time.sleep(3)

        export_btn = self.browser.find_element(
            By.CLASS_NAME, "export-citation")
        export_btn.click()

        time.sleep(3)

        select_element = self.browser.find_element(By.NAME, "citation-format")
        select = Select(select_element)
        select.select_by_visible_text("BibTeX")

        time.sleep(8)

        form_div = self.browser.find_element(By.CLASS_NAME, "form-buttons")
        form_div.find_element(By.TAG_NAME, "a").click()

        time.sleep(2)

        close_button_div = self.browser.find_element(
            By.CLASS_NAME, "modal__header")
        close_button_div.find_element(
            By.TAG_NAME, "button").click()

        for i in range(0, 10):
            print(i)
            self.browser.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(4)
            next_element = self.browser.find_element(
                By.CLASS_NAME, "hvr-forward")
            next_element.click()

            time.sleep(6)

            checkbox = self.browser.find_element(
                By.ID, "action-bar-select-all")
            checkbox.click()

            time.sleep(3)

            export_btn = self.browser.find_element(
                By.CLASS_NAME, "export-citation")
            export_btn.click()

            time.sleep(3)

            select_element = self.browser.find_element(
                By.NAME, "citation-format")
            select = Select(select_element)
            select.select_by_visible_text("BibTeX")

            time.sleep(8)

            form_div = self.browser.find_element(By.CLASS_NAME, "form-buttons")
            form_div.find_element(By.TAG_NAME, "a").click()

            time.sleep(2)
            close_button_div = self.browser.find_element(
                By.CLASS_NAME, "modal__header")
            close_button_div.find_element(
                By.TAG_NAME, "button").click()
        time.sleep(5)
        self.browser.quit()

    def run(self):
        """
          Runs the scrapper
        """
        self.open_library()
        self.google_login()
        self.search_articles()
