"""
  Main module of the project
"""
# from scrappers.ScopusScrapper import ScopusScraper
# from utils.utils import Utils
# from scrappers.sage_scrapper import SageScraper
# from reader_resources.reader_implementation import ReaderImplementation
# from scrappers.iee_scrapper import IeeeScrapper
# from abstract_text_preprocessing.text_preprocessing import TextPreprocessing
from fastapi import FastAPI
from api.endpoints import statics
from api.endpoints import abstracts_comparasion
from api.endpoints import algorithms
from api.endpoints import word_counting
from api.endpoints import filtering_results


app = FastAPI(title="Proyecto Final Análisis de algoritmos")

app.include_router(
    algorithms.router, prefix="/algorithmsExecution",
    tags=["Algorithms execution (Requirement 1)"])

app.include_router(
    statics.router, prefix="/articlesStatistics",
    tags=["Statistics (Requirement 2)"])

app.include_router(
    word_counting.router, prefix="/wordCounting",
    tags=["Co-word netword and wordclouds  (Requirement 3)"])

app.include_router(
    abstracts_comparasion.router, prefix="/abstractComparasion",
    tags=["Abstracts Comparasion (Requirement 5)"])

app.include_router(
    filtering_results.router, prefix="/filteringResults",
    tags=["Filtering results"])


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
