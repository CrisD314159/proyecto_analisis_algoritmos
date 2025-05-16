"""
 This module contains a class used to handle and process abstracts extracted from
 the bibtex articles
"""
import re
import time
from tabulate import tabulate
from services.algorithms.algorithms_execution import AlgorithmsExecution
from sorting_algorithms.bubble_sort import StringBubbleSort


class AbstractProcessing:
    """
    Class for article abstract processing
    """

    def __init__(self):
        self.keywords = ["abstraction", "algorithm", "coding", "creativity",
                         "logic", "conditionals", "loops",
                         "motivation", "persistence", "block", "mobile",
                         "application", "programming", "robotic", "scratch"]
        self.keywords_appereances = {'abstraction': 0, 'algorithm': 0, 'coding': 0, 'creativity': 0,
                                     'logic': 0, 'conditionals': 0, 'loops': 0,
                                     'motivation': 0, 'persistence': 0, 'block': 0, 'mobile': 0,
                                     'application': 0, 'programming': 0, 'robotic': 0, 'scratch': 0}

    @staticmethod
    def separate_white_spaces(abstract):
        """
        This method separates the words contained in the article abstract
        string into a string array
        """
        words = re.split(r'[,\s]+', abstract.strip())
        return words

    def filter_keywords(self, abstract_words):
        """
        This method filters the keywords declared in this class init method
        """
        for keyword in self.keywords:
            for word in abstract_words:
                if word.lower() == keyword:
                    self.keywords_appereances[f'{keyword}'] = self.keywords_appereances[f'{keyword}'] + 1

        table_data = [(key, value)
                      for key, value in self.keywords_appereances.items()]

        print(tabulate(table_data, headers=[
              "Keyword", "Repetitions"], tablefmt="grid"))

        print("Total of words", len(abstract_words))
        print("Algorithms will only take first 20000 words")

        # bubble = StringBubbleSort()
        # start = time.time()
        # bubble.sort(abstract_words[:20000])
        # end = time.time()

        # execution = (end - start) * 1000
        # print("Execution for bubble = ", execution)

        AlgorithmsExecution.execute_algorithms(
            abstract_words[:20000], "Abstract")
