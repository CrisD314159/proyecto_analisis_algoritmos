"""
Module for shell sort.
"""


class ShellSort:
    """
    Class for the Shell Sort algorithm.
    """

    @staticmethod
    def shellsort_strings(strings: list[str]) -> list[str]:
        """
        Sort a list of strings using the Shell Sort algorithm.

        Args:
            strings (list[str]): The list of strings to sort.

        Returns:
            list[str]: The sorted list of strings.
        """
        # Get the length of the list
        n = len(strings)

        # Initialize the gap size
        gap = n // 2

        # Perform the Shell Sort
        while gap > 0:
            for i in range(gap, n):
                # Current string to be compared
                current_string = strings[i]
                j = i

                # Compare strings lexicographically and shift elements
                while j >= gap and strings[j - gap] > current_string:
                    strings[j] = strings[j - gap]
                    j -= gap

                # Place the current string in its correct position
                strings[j] = current_string

            # Reduce the gap size
            gap //= 2

        return strings
