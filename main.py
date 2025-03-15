"""
  Main module of the project
"""
from scrappers.ScopusScrapper import ScopusScraper
from scrappers.acm_undetected import ACMSUndetectedScrapper
from utils.utils import Utils
from scrappers.sage_scrapper import SageScraper
from reader_resources.reader_implementation import ReaderImplementation
from sorting_algorithms.bucket_sort import BucketSort


utils = Utils()

# scopus = ScopusScraper()
# scopus.run()

# sage = SageScraper()
# sage.run()

# acm = ACMSUndetectedScrapper(
#     use_undetected=True)
# acm.run()

utils.move_downloaded_files()


reader = ReaderImplementation()
reader.read_bib_files()

arr = ["apple", "banana", "date", "strawberry", "kiwi", "orange", "grape",
       "cherry", "mango", "pear", "peach", "plum", "watermelon", "melon"]

radix = BucketSort()
lista = radix.bucketSort(arr)
print(lista)
