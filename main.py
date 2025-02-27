from scrappers.ScopusScrapper import ScopusScraper
from scrappers.ACMScrapper import ACMScrapper
from utils.utils import Utils


scopus = ScopusScraper()

scopus.run()


acm = ACMScrapper()
acm.run()


# utils = Utils()
# utils.move_downloaded_files()
