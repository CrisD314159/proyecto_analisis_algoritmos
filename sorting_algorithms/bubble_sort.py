"""
This module contains a bubble sort implementation for sorting strings.
"""


class StringBubbleSort:
    """
    A class to perform bubble sort on a list of strings with optional case sensitivity.
    """

    def __init__(self, case_sensitive: bool = True) -> None:
        """
        Initialize the sorter with an option for case sensitivity.

        Args:
            case_sensitive (bool): Whether to consider case when comparing strings.
        """
        self.case_sensitive = case_sensitive

    def compare(self, str1: str, str2: str) -> bool:
        """
        Compare two strings based on the case sensitivity setting.

        Args:
            str1 (str): First string to compare.
            str2 (str): Second string to compare.

        Returns:
            bool: True if str1 > str2, False otherwise.
        """
        if not self.case_sensitive:
            return str1.lower() > str2.lower()
        return str1 > str2

    def sort(self, arr: list[str]) -> list[str]:
        """
        Sort an array of strings using the bubble sort algorithm.

        Args:
            arr (list[str]): List of strings to sort.

        Returns:
            list[str]: Sorted list of strings.
        """
        # Handle edge cases for empty or single-element lists
        if len(arr) <= 1:
            return arr

        # Create a copy to avoid modifying the original array
        result = arr.copy()

        # Outer loop to iterate through the list
        for n in range(len(result) - 1, 0, -1):

            # Initialize swapped to track if any swaps occur
            swapped = False

            # Inner loop to compare adjacent elements
            for i in range(n):
                if self.compare(result[i], result[i + 1]):
                    # Swap elements if they are in the wrong order
                    result[i], result[i + 1] = result[i + 1], result[i]
                    swapped = True

            # If no swaps occurred, the list is already sorted
            if not swapped:
                break

        return result
