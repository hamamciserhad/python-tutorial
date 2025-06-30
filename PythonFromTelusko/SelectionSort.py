"""


This script demonstrates:
- How to implement the Selection Sort algorithm
- Swapping the minimum element to its correct position in each iteration
- Step-by-step sorting visualization using print statements

Author: Serhad
"""

def selection_sort(array):
    """
    Sorts a list in ascending order using the Selection Sort algorithm.
    In each pass, the smallest unsorted element is placed in its correct position.

    Parameters:
        array (list): The list of numbers to be sorted (in-place)

    Prints:
        The array after each outer loop iteration (visualizing progress)
    """
    n = len(array)

    for i in range(n):
        min_index = i  # Assume current i is the index of the smallest value

        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j  # Found a smaller element

        # Swap the found minimum element with the first unsorted element
        array[i], array[min_index] = array[min_index], array[i]

        print(array)  # Print array after each pass

# Example usage
array = [2, 3, 1, 55, 51, 32, 21, 6]
selection_sort(array)
print(array)  # Final sorted array