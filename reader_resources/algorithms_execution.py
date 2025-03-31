"""
  This module executes the different sorting algorithms 
  for the article titles array
"""
import time
from sorting_algorithms.binary_insertion import BinaryInsertionSort
from sorting_algorithms.bitonic_sort import BitonicSort
from sorting_algorithms.bucket_sort import BucketSort
from sorting_algorithms.comb_sort import CombSort
from sorting_algorithms.gnome_sort import GnomeSort
from sorting_algorithms.heap_sort import HeapSort
from sorting_algorithms.pingeon_sort import PingeonSort
from sorting_algorithms.quick_sort import StringQuickSort
from sorting_algorithms.radix_sort import RadixSort
from sorting_algorithms.selection_sort import SelectionSort
from sorting_algorithms.tim_sort_algorithm import TimSort
from sorting_algorithms.tree_sort import TreeSort
from reader_resources.execution_time_plotter import ExecutionTimePlotter


class AlgorithmsExecution:
    """
    A class that executes the different sorting algorithms for the article titles array.
    """

    @staticmethod
    def run_binary(arr):
        """
        Run method for Binary Search algorithm.
        """
        try:

            arr_copy = arr
            BinaryInsertionSort.sort_in_place(arr_copy)
            return "Binary", arr_copy
        except RecursionError:
            print("Error executing the Binary insertion algorithm")
            return -1

    @staticmethod
    def run_bitonic(arr):
        """
        Run method for Bitonic Sort algorithm.
        """
        try:
            arr_copy = arr
            BitonicSort.sort(arr_copy)
            return "Bitonic", arr_copy
        except RecursionError:
            print("Error on recusion Bitonic sort method")
            return -1
        except IndexError:
            print("Error executing the Bitonic Sort algorithm (Index out of range)")
            return -1

    @staticmethod
    def run_bucket(arr):
        """
        Run method for Bucket Sort algorithm.
        """
        try:
            arr_copy = arr
            bucket = BucketSort()
            result = bucket.sort(arr_copy)
            return "Bucket", result
        except IndexError:
            print("Error executing the Bucket tree algorithm (Index out of range)")
            return -1

    @staticmethod
    def run_comb(arr):
        """
        Run method for Comb Sort algorithm.
        """
        try:
            arr_copy = arr
            CombSort.comb_sort(arr_copy)
            return "Comb", arr_copy
        except IndexError:
            print("Error executing the Comb Sort algorithm (Index out of range)")
            return -1

    @staticmethod
    def run_gnome(arr):
        """
        Run method for Gnome Sort algorithm.
        """
        try:
            arr_copy = arr
            gnome = GnomeSort()
            result = gnome.sort(arr_copy)
            return "Gnome", result
        except IndexError:
            print("Error executing the Gnome Sort algorithm (Index out of range)")
            return -1

    @staticmethod
    def run_heap(arr):
        """
        Run method for Heap Sort algorithm.
        """
        try:
            arr_copy = arr
            HeapSort.heap_sort(arr_copy)
            return "Heap", arr_copy
        except IndexError:
            print("Error executing the Heap Sort algorithm (Index out of range)")
            return -1

    @staticmethod
    def run_pingeon(arr):
        """
        Run method for Pingeon Sort algorithm.
        """
        try:
            arr_copy = arr
            PingeonSort.pigeonhole_sort(arr_copy)
            return "Pingeon", arr_copy
        except IndexError:
            print("Error executing the Pingeon algorithm (Index out of range)")
            return -1

    @staticmethod
    def run_quick(arr):
        """
        Run method for Bitonic Sort algorithm.
        """
        try:
            arr_copy = arr
            quicksort = StringQuickSort()
            result = quicksort.run_quick_sort(arr_copy)
            return "Quick", result
        except RecursionError:
            print("Error executing the Quick Sort algorithm")
            return -1
        except IndexError:
            print("Error executing the Quick Sort algorithm (Index out of range)")
            return -1

    @staticmethod
    def run_radix(arr):
        """
        Run method for Radix Sort algorithm.
        """
        try:
            arr_copy = arr
            radix = RadixSort(arr=arr_copy)
            result = radix.sort()
            return "Radix", result
        except IndexError:
            print("Error executing the Radix algorithm (Index out of range)")
            return -1

    @staticmethod
    def run_selection(arr):
        """
        Run method for Selection Sort algorithm.
        """
        try:
            arr_copy = arr
            SelectionSort.selection_sort(arr_copy)
            return "Selection", arr_copy
        except IndexError:
            print("Error executing the Selection Sort algorithm (Index out of range)")
            return -1

    @staticmethod
    def run_tim(arr):
        """
        Run method for Tim Sort algorithm.
        """
        try:
            arr_copy = arr
            tim = TimSort()
            tim.run_tim_sort(arr_copy)
            return "Tim", arr_copy
        except IndexError:
            print("Error executing the Tim algorithm (Index out of range)")
            return -1

    @staticmethod
    def run_tree(arr):
        """
        Run method for Tree Sort algorithm.
        """
        try:

            arr_copy = arr
            tree = TreeSort(arr_copy)
            result = tree.sort()
            return "Tree", result
        except RecursionError:
            print("Error executing the Tree sort algorithm")
            return -1
        except IndexError:
            print("Error executing the Tree Sort algorithm (Index out of range)")
            return -1

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
            name, result = algorithm(arr)
            end = time.time()  # used to calculate the execution time
            # Converts the execution to milisecs
            exec_time = (end - start) * 1000
            if name != -1:  # if returns a -1, that means there was an error in the execution
                print(
                    f"Algorithm {name} executed in {exec_time} ms for the variable {plotter_name}")
                algorithms_names.append(name)
                times.append(exec_time)

        plotter = ExecutionTimePlotter(
            algorithms=algorithms_names, times=times)
        plotter.plot_execution_times(plotter_name)
