"""
  Main module of the project
"""
from scrappers.ScopusScrapper import ScopusScraper
from scrappers.acm_undetected import ACMSUndetectedScrapper
from utils.utils import Utils
from scrappers.sage_scrapper import SageScraper


utils = Utils()

routes = utils.list_chrome_profiles()
default_path = routes[0]['path']

scopus = ScopusScraper()
scopus.run()

sage = SageScraper()

sage.run()

acm = ACMSUndetectedScrapper(
    use_undetected=True, profile_path=default_path)
acm.run()

utils.move_downloaded_files()
