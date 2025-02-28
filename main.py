"""
  Main module of the project
"""
from scrappers.ScopusScrapper import ScopusScraper
from scrappers.acm_undetected import ACMSUndetectedScrapper
from utils.utils import Utils


scopus = ScopusScraper()
scopus.run()

acm = ACMSUndetectedScrapper(
    use_undetected=True, profile_path="/Users/cristiandavidvargasloaiza/Library/Application Support/Google/Chrome/Default")
acm.run()


utils = Utils()
utils.move_downloaded_files()
