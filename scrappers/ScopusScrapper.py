import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv


class ScopusScraper:
    def __init__(self):
        load_dotenv()
        self.password = os.getenv("MAIL_PASSWORD")
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(options=self.options)
        self.browser.implicitly_wait(60)

    def open_library(self):
        self.browser.get("https://library.uniquindio.edu.co/databases")
        wait = WebDriverWait(self.browser, 10)
        scienceDirectDiv = self.browser.find_element(
            By.CSS_SELECTOR, "#facingenierasciencedirectconsorciocolombiadescubridor")
        divlink = wait.until(
            lambda browser: scienceDirectDiv.find_element(By.CSS_SELECTOR, "a"))
        self.browser.get(divlink.get_attribute("href"))

    def google_login(self):
        self.browser.find_element(By.ID, "btn-google").click()
        self.browser.find_element(By.TAG_NAME, "input").send_keys(
            "cristiand.vargasl@uqvirtual.edu.co")
        self.browser.find_element(By.ID, "identifierNext").find_element(
            By.TAG_NAME, "button").click()
        self.browser.find_element(By.NAME, "Passwd").send_keys(self.password)
        self.browser.find_element(By.ID, "passwordNext").find_element(
            By.TAG_NAME, "button").click()

    def search_articles(self):
        searchInput = self.browser.find_element(By.ID, "qs")
        searchInput.send_keys("computational thinking")
        searchInput.send_keys(Keys.RETURN)

        self.browser.find_element(By.CLASS_NAME, "button-primary").click()

        checkbox = self.browser.find_element(
            By.CLASS_NAME, "result-header-controls-container")
        checkbox.find_element(By.TAG_NAME, "span").click()

        self.browser.find_element(
            By.CLASS_NAME, "export-all-link-button").click()
        exportRis = self.browser.find_element(By.CLASS_NAME, "preview-body")
        exportRis.find_elements(By.TAG_NAME, "button")[1].click()

    def run(self):
        self.open_library()
        self.google_login()
        self.search_articles()
