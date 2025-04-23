class BidirectionalStringSort:
    """
    A class that implements bidirectional bubble sort (cocktail sort) for strings.
    This algorithm passes through the list in both directions, sorting elements
    from left to right and then right to left in each iteration.
    """

    def __init__(self, strings=None):
        """Initialize with an optional list of strings."""
        self.strings = strings if strings is not None else []

    def set_strings(self, strings):
        """Set a new list of strings to sort."""
        self.strings = strings

    def get_strings(self):
        """Return the current list of strings."""
        return self.strings

    def sort(self, case_sensitive=True):
        """
        Sort the strings using bidirectional bubble sort (cocktail sort).

        Args:
            case_sensitive (bool): If False, sorting will ignore case. Default is True.

        Returns:
            list: The sorted list of strings.
        """
        if not self.strings:
            return []

        # Make a copy to avoid modifying the original list
        array = self.strings.copy()
        n = len(array)

        # Define compare function based on case sensitivity
        if case_sensitive:
            def compare(a, b): return a > b
        else:
            def compare(a, b): return a.lower() > b.lower()

        swapped = True
        start = 0
        end = n - 1

        while swapped:
            # Reset swapped flag for forward pass
            swapped = False

            # Forward pass (left to right)
            for i in range(start, end):
                if compare(array[i], array[i + 1]):
                    array[i], array[i + 1] = array[i + 1], array[i]
                    swapped = True

            # If no swaps occurred, the array is sorted
            if not swapped:
                break

            # Decrease the end pointer as the largest element is now at the end
            end -= 1

            # Reset swapped flag for backward pass
            swapped = False

            # Backward pass (right to left)
            for i in range(end - 1, start - 1, -1):
                if compare(array[i], array[i + 1]):
                    array[i], array[i + 1] = array[i + 1], array[i]
                    swapped = True

            # Increase the start pointer as the smallest element is now at the beginning
            start += 1

        # Update internal strings list
        self.strings = array
        return array

    def __str__(self):
        """String representation of the current list."""
        return str(self.strings)


# Example usage:
if __name__ == "__main__":
    # Create a sorter instance
    sorter = BidirectionalStringSort()

    # Set some strings to sort
    test_strings = ["banana", "Apple", "cherry",
                    "Date", "elderberry", "fig", "Grape"]
    sorter.set_strings(test_strings)

    # Sort case sensitively (default)
    print("Original list:", sorter.get_strings())
    case_sensitive_result = sorter.sort()
    print("Case sensitive sort:", case_sensitive_result)

    # Sort case insensitively
    sorter.set_strings(test_strings)  # Reset the list
    case_insensitive_result = sorter.sort(case_sensitive=False)
    print("Case insensitive sort:", case_insensitive_result)
