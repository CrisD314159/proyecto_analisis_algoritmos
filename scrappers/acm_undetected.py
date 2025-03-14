"""
This is the acm scrapper version that uses undetected-chromedriver
 to bypass the cloudflare detection
"""
import time
import random
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class ACMSUndetectedScrapper:
    """
      Scrapper class for the ACM Database with improved Cloudflare bypass
    """

    def __init__(self, use_undetected=True, profile_path=None):
        """
        Initialize the scrapper
        """
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
         Locates and opens the ACM database
        """
        try:
            self.browser.get("https://library.uniquindio.edu.co/databases")
            self.simulate_human_behavior()

            # Wait for the specific element
            wait = WebDriverWait(self.browser, 15)
            science_direct_div = self.browser.find_element(
                By.CSS_SELECTOR, "#facingenieraacmdigitallibrary")
            divlink = wait.until(
                lambda browser: science_direct_div.find_element(By.CSS_SELECTOR, "a"))
            # Simulate human scrolling to the element
            self.browser.execute_script(
                "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", divlink)
            self.simulate_human_behavior(1, 2)

            # Get the href and navigate
            href = divlink.get_attribute("href")
            self.simulate_human_behavior(0.5, 1)
            self.browser.get(href)

            # Add extra wait after loading the new page
            self.simulate_human_behavior(3, 5)

        except Exception as e:
            print(f"Error opening library: {e}")
            raise

    def simulate_human_behavior(self, min_time=2, max_time=4):
        """
        Method to simulate human-like behavior with randomized actions
        """
        # Random sleep between actions
        time.sleep(random.uniform(min_time, max_time))

        # Occasionally perform random mouse movements
        if random.random() < 0.7:  # 70% chance
            # Generate random coordinates within the viewport
            width = self.browser.execute_script("return window.innerWidth;")
            height = self.browser.execute_script("return window.innerHeight;")

            # Create random points for mouse movement
            points = [(random.randint(0, width), random.randint(0, height))
                      for _ in range(3)]

            for x, y in points:
                self.action_chains.move_by_offset(x, y).perform()
                time.sleep(random.uniform(0.1, 0.3))
                # Reset position to (0,0) to avoid moving off-screen
                self.action_chains.move_by_offset(-x, -y).perform()

        # Occasionally scroll the page a bit
        if random.random() < 0.5:  # 50% chance
            scroll_amount = random.randint(100, 300)
            self.browser.execute_script(
                f"window.scrollBy(0, {scroll_amount});")
            time.sleep(random.uniform(0.5, 1))

            # Sometimes scroll back up a bit
            if random.random() < 0.3:  # 30% chance
                self.browser.execute_script(
                    f"window.scrollBy(0, -{scroll_amount/2});")
                time.sleep(random.uniform(0.5, 1))

    def handle_cloudflare(self, max_wait=30):
        """
        Handle Cloudflare challenges specifically
        """
        try:
            # Wait for Cloudflare challenge to appear
            start_time = time.time()
            while time.time() - start_time < max_wait:
                # Check for Cloudflare challenge iframe
                iframes = self.browser.find_elements(By.TAG_NAME, "iframe")
                cloudflare_detected = False

                for iframe in iframes:
                    src = iframe.get_attribute("src")
                    if src and ("cloudflare" in src.lower() or "challenges" in src.lower()):
                        cloudflare_detected = True
                        print("Cloudflare challenge detected. Attempting to solve...")

                        # Switch to the iframe
                        self.browser.switch_to.frame(iframe)

                        try:
                            # Look for checkbox or other interactive elements
                            checkbox = WebDriverWait(self.browser, 5).until(
                                EC.element_to_be_clickable(
                                    (By.CSS_SELECTOR, ".checkbox, .rc-checkbox, .recaptcha-checkbox"))
                            )

                            # Move mouse realistically to the checkbox
                            self.action_chains.move_to_element(checkbox).pause(
                                random.uniform(0.1, 0.3)).click().perform()
                            print("Clicked on Cloudflare checkbox")

                            # Switch back to main content
                            self.browser.switch_to.default_content()

                            # Wait for the challenge to be completed
                            time.sleep(random.uniform(5, 10))
                            break

                        except Exception as e:
                            print(
                                f"Error interacting with Cloudflare element: {e}")
                            self.browser.switch_to.default_content()

                if not cloudflare_detected:
                    # If we don't detect Cloudflare, we can proceed
                    break

                # If Cloudflare is detected but we couldn't interact with it, wait a bit and retry
                time.sleep(2)

            return True
        except Exception as e:
            print(f"Error handling Cloudflare: {e}")
            return False

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
            search_input.send_keys("computational thinking")
            self.simulate_human_behavior()
            search_input.send_keys(Keys.RETURN)

            time.sleep(4)

            # Click on the select all

            try:

                allow_cookies = self.browser.find_element(
                    By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
                allow_cookies.click()
                time.sleep(2)
            except:
                pass

            range_slider = self.browser.find_element(
                By.ID, "range-slider-start")
            range_slider.clear()
            range_slider.send_keys("2024")
            range_slider.send_keys(Keys.RETURN)

            time.sleep(5)

            checkbox_input = self.browser.find_element(
                By.CSS_SELECTOR, "input[name='markall']")
            self.browser.execute_script(
                "arguments[0].click();", checkbox_input)

            self.simulate_human_behavior()
            buttons_div = self.browser.find_element(
                By.CLASS_NAME, "item-results__buttons")
            buttons = buttons_div.find_elements(By.TAG_NAME, "a")
            buttons[0].click()

            all_button = self.browser.find_element(
                By.ID, "allResults")
            all_button.click()

            time.sleep(5)

            all_results_div = self.browser.find_element(
                By.CLASS_NAME, "all-results-tab-container")
            all_results_div.find_element(
                By.TAG_NAME, "a").click()

            # Increased wait time with progress logging
            print("Waiting for download preparation...")
            for i in range(12):  # 12 * 10 = 120 seconds total wait
                time.sleep(10)
                print(f"Still waiting... {(i+1)*10} seconds elapsed")

            print("Attempting to find download button...")

            # Use a more robust approach to find the button
            results_div = WebDriverWait(self.browser, 20).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "searchCiteExport-popup__body"))
            )

            # Debug what's visible in the results div
            print(f"Found results div with content: {results_div.text}")

            # Explicit wait checking for disabled attribute
            print("Waiting for download button to be enabled...")
            max_wait = 120  # 2 minutes
            start_time = time.time()

            while time.time() - start_time < max_wait:
                try:
                    download_container = self.browser.find_element(
                        By.ID, "exportDownloadReady")
                    download_link = download_container.find_element(
                        By.TAG_NAME, "a")
                    if download_link.is_enabled() and download_link.is_displayed():
                        disabled = download_link.get_attribute("disabled")
                        aria_disabled = download_link.get_attribute(
                            "aria-disabled")

                        print(
                            f"Button state - disabled: {disabled}, aria-disabled: {aria_disabled}")

                        if not disabled and aria_disabled != "true":
                            print("Download button appears to be enabled!")
                            # Add a small delay and then click using JavaScript
                            self.simulate_human_behavior(3, 5)
                            self.browser.execute_script(
                                "arguments[0].click();", download_link)
                            print("Clicked download button via JavaScript")

                            # Wait for download to start
                            print("Waiting for download to complete...")
                            self.simulate_human_behavior(20, 30)
                            print("Download waiting period completed")
                            return
                except Exception as e:
                    print(f"Error checking button: {e}")

                print("Button not ready yet, waiting...")
                time.sleep(5)

            print("Timed out waiting for download button to be enabled")

            # Take screenshot for debugging if possible
            try:
                self.browser.save_screenshot("acm_download_timeout.png")
                print("Saved screenshot as acm_download_timeout.png")
            except Exception as e:
                print(f"Failed to save screenshot: {e}")

        except Exception as e:
            print(f"Error during search: {str(e)}")
            # Take screenshot on error
            try:
                self.browser.save_screenshot("acm_error.png")
                print("Saved error screenshot as acm_error.png")
            except:
                pass

        except Exception as e:
            print(f"Error during search: {e}")

    def run(self):
        """
        Method to run the scraper
        """
        try:
            self.open_library()
            self.acm_search()
            print("Scraping completed successfully")
        except Exception as e:
            print(f"Error running the scraper: {e}")
