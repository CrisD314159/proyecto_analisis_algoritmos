"""
  This module is used to plot the execution time of the algorithms.
"""
import os
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")


class ExecutionTimePlotter:
    """
    A class that plots the execution time of the algorithms.
    """

    def __init__(self, algorithms, times):
        self.algorithms = algorithms
        self.execution_times = times

    def plot_execution_times(self, title):
        """
        Plot the execution times of the algorithms.
        Uses the algoritms names and execution times lists
        received in the class constructor to plot bar graphs
        """

        project_dir = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '../../images'))
        research_files_dir = os.path.join(
            project_dir, "algorithms_execution_plotting")
        os.makedirs(research_files_dir, exist_ok=True)

        file_path = os.path.join(research_files_dir, f"{title}_plotting.png")
        plt.figure(figsize=(12, 6))
        plt.bar(self.algorithms, self.execution_times)
        plt.xlabel('Algoritmos')
        plt.ylabel('Tiempo de ejecución (ms)')
        plt.title(
            f"Tiempo de ejecución de los algoritmos para la variable: {title}")
        plt.tight_layout()
        plt.savefig(file_path)
        plt.close()

        return file_path
