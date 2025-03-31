"""
 This module contains a class used to handle and process abstracts extracted from
 the bibtex articles
"""
import re
import time
from reader_resources.algorithms_execution import AlgorithmsExecution


class AbstractProcessing:
    """
    Class for article abstract processing
    """

    def __init__(self):
        self.keywords = ["abstraction", "algorithm", "coding", "creativity",
                         "logic", "conditionals", "loops",
                         "motivation", "persistence", "block", "mobile",
                         "application", "programming", "robotic", "scratch"]
        self.keywords_appereances = []

    @staticmethod
    def separate_white_spaces(abstract):
        """
        This method separates the words contained in the article abstract
        string into a string array
        """
        words = re.split(r'[,\s]+', abstract.strip())
        return words

    @staticmethod
    def execute_algorithms(arr, plotter_name):
        """
            Execute all sorting algorithms.
            """

        # List that contains the algorithms to execute
        algorithms = [
            AlgorithmsExecution.run_binary,
            AlgorithmsExecution.run_bitonic,
            AlgorithmsExecution.run_bucket,
            AlgorithmsExecution.run_comb,
            AlgorithmsExecution.run_gnome,
            AlgorithmsExecution.run_heap,
            AlgorithmsExecution.run_pingeon,
            AlgorithmsExecution.run_quick,
            AlgorithmsExecution.run_radix,
            AlgorithmsExecution.run_selection,
            AlgorithmsExecution.run_tim,
            AlgorithmsExecution.run_tree
        ]

        times = []  # list to store the execution times
        algorithms_names = []  # list to store the algorithms name

        for algorithm in algorithms:
            start = time.time()  # used to calculate the execution time
            # TODO make each algorithm return an arraoy witrh two values [name, results]
            name, result = algorithm(arr)
            end = time.time()  # used to calculate the execution time
            # Converts the execution to milisecs
            exec_time = (end - start) * 1000
            if name != -1:  # if returns a -1, that means there was an error in the execution
                print(
                    f"Algorithm {name} executed in {exec_time} ms for the variable {plotter_name}")
                algorithms_names.append(name)
                times.append(exec_time)
