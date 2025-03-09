"""
  This module is used to plot the execution time of the algorithms.
"""

import matplotlib.pyplot as plt


class ExecutionTimePlotter:
    """
    A class that plots the execution time of the algorithms.
    """

    def __init__(self, algorithms, times):
        self.algorithms = algorithms
        self.execution_times = times

    def plot_execution_times(self):
        """
        Plot the execution times of the algorithms.
        """
        plt. bar(self.algorithms, self.execution_times)
        plt.xlabel('Algoritmos')
        plt.ylabel('Tiempo de ejecución (ms)')
        plt.title(
            'Comparación de Tiempos de Ejecución de Algoritmos de Ordenamiento')
        plt.show()
