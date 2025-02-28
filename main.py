from scrappers.ScopusScrapper import ScopusScraper
from scrappers.ACMScrapper import ACMScrapper
from scrappers.acm_undetected import ACMSUndetectedScrapper
from utils.utils import Utils


undetect = ACMSUndetectedScrapper(use_undetected=True)
undetect.run()

# utils = Utils()
# utils.move_downloaded_files()
