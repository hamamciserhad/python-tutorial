"""

This module demonstrates how to implement the Bubble Sort algorithm in Python.

Steps:
1. Compare each pair of adjacent items.
2. Swap them if they are in the wrong order.
3. Repeat the process until the array is sorted.

Author: Serhad Hamamci
"""

def bubble_sort(array):
    """
    Sorts the input list in ascending order using the Bubble Sort algorithm.

    Parameters:
        array (list of int): The list to sort.

    Returns:
        None: The list is sorted in-place.

    Example:
        >>> arr = [4, 1, 3]
        >>> bubble_sort(arr)
        >>> print(arr)
        [1, 3, 4]
    """
    for i in range(len(array) - 1):  # Outer loop runs n-1 times
        for j in range(len(array) - i - 1):  # Inner loop shrinks each pass
            if array[j] > array[j + 1]:  # Swap if elements are out of order
                array[j], array[j + 1] = array[j + 1], array[j]

# Sample array to sort
array = [5, 6, 1, 3]

# Call the sorting function
bubble_sort(array)

# Print sorted elements
for i in range(len(array)):
    print(array[i])