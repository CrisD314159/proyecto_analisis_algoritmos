"""
  Main module of the project
"""
from scrappers.ScopusScrapper import ScopusScraper
from scrappers.acm_undetected import ACMSUndetectedScrapper
from utils.utils import Utils
from scrappers.sage_scrapper import SageScraper
from reader_resources.reader_implementation import ReaderImplementation
from ordering_algorithms.tim_sort_algorithm import TimSort
from ordering_algorithms.comb_sort import CombSort
from ordering_algorithms.tree_sort import tree_sort


utils = Utils()

# scopus = ScopusScraper()
# scopus.run()

# sage = SageScraper()
# sage.run()

# acm = ACMSUndetectedScrapper(
#     use_undetected=True)
# acm.run()

# utils.move_downloaded_files()


# reader = ReaderImplementation()
# reader.run()

arr = ["banana", "apple", "grape", "cherry", "mango", "blueberry"]
tim = CombSort()
tim.run_comb_sort(arr)

print(arr)
