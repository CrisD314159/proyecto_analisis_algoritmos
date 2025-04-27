"""
  Main module of the project
"""
from scrappers.ScopusScrapper import ScopusScraper
from utils.utils import Utils
from scrappers.sage_scrapper import SageScraper
from reader_resources.reader_implementation import ReaderImplementation
from scrappers.iee_scrapper import IeeeScrapper
from abstract_text_preprocessing.text_preprocessing import TextPreprocessing


# utils = Utils()

# scopus = ScopusScraper()
# scopus.run()

# sage = SageScraper()
# sage.run()

# # acm = ACMSUndetectedScrapper(  Deprecated module due to database problems
# #     use_undetected=True)
# # acm.run()

# iee = IeeeScrapper()
# iee.run()

# utils.move_downloaded_files()


reader = ReaderImplementation()
reader.read_bib_files()
