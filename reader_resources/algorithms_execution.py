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
from sorting_algorithms.quick_sort import QuickSort
from sorting_algorithms.radix_sort import RadixSort
from sorting_algorithms.selection_sort import SelectionSort
from sorting_algorithms.tim_sort_algorithm import TimSort
from sorting_algorithms.tree_sort import tree_sort
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
        arr_copy = arr
        BinaryInsertionSort.sort_in_place(arr_copy)
        return "Binary Insertion Sort"

    @staticmethod
    def run_bitonic(arr):
        """
        Run method for Bitonic Sort algorithm.
        """
        arr_copy = arr
        BitonicSort.sort(arr_copy)
        return "Bitonic Sort"

    @staticmethod
    def run_bucket(arr):
        """
        Run method for Bitonic Sort algorithm.
        """
        arr_copy = arr
        BucketSort.bucket_sort(arr_copy)
        return "Bucket Sort"

    @staticmethod
    def run_comb(arr):
        """
        Run method for Bitonic Sort algorithm.
        """
        arr_copy = arr
        CombSort.comb_sort(arr_copy)
        return "Comb Sort"

    @staticmethod
    def run_gnome(arr):
        """
        Run method for Bitonic Sort algorithm.
        """
        arr_copy = arr
        GnomeSort.gnome_sort(arr_copy)
        return "Gnome Sort"

    @staticmethod
    def run_heap(arr):
        """
        Run method for Bitonic Sort algorithm.
        """
        arr_copy = arr
        HeapSort.heap_sort(arr_copy)
        return "Heap Sort"

    @staticmethod
    def run_pingeon(arr):
        """
        Run method for Bitonic Sort algorithm.
        """
        arr_copy = arr
        PingeonSort.pigeonhole_sort(arr_copy)
        return "Pingeon Sort"

    @staticmethod
    def run_quick(arr):
        """
        Run method for Bitonic Sort algorithm.
        """
        arr_copy = arr
        QuickSort.quick_sort(arr_copy)
        return "Quick Sort"

    @staticmethod
    def run_radix(arr):
        """
        Run method for Bitonic Sort algorithm.
        """
        arr_copy = arr
        RadixSort.sort(arr_copy)
        return "Radix Sort"

    @staticmethod
    def run_selection(arr):
        """
        Run method for Bitonic Sort algorithm.
        """
        arr_copy = arr
        SelectionSort.selection_sort(arr_copy)
        return "Selection Sort"

    @staticmethod
    def run_tim(arr):
        """
        Run method for Bitonic Sort algorithm.
        """
        arr_copy = arr
        tim = TimSort()
        tim.run_tim_sort(arr_copy)
        return "Tim Sort"

    @staticmethod
    def run_tree(arr):
        """
        Run method for Bitonic Sort algorithm.
        """
        arr_copy = arr
        tree_sort(arr_copy)
        return "Tree Sort"

    @staticmethod
    def execute_algorithms(arr):
        """
        Execute all sorting algorithms.
        """
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
            AlgorithmsExecution.run_tim
        ]

        # TODO: Fix the tree sort algorithm
        times = []
        algorithms_names = []

        for algorithm in algorithms:
            start = time.time()
            name = algorithm(arr)
            end = time.time()
            exec_time = (end - start) * 1000
            algorithms_names.append(name)
            times.append(exec_time)

        plotter = ExecutionTimePlotter(
            algorithms=algorithms_names, times=times)
        plotter.plot_execution_times(
            'Execution time of the sorting algorithms for the article titles array')
