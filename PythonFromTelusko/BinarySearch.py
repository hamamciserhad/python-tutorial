"""

This module implements the binary search algorithm on a sorted list of integers.

Steps:
1. The `binary_search` function takes a sorted list and a target number.
2. It performs binary search to find the index of the target.
3. Returns the index if found, otherwise returns -1.
4. The result is displayed to the user based on input.

Author: Serhad Hamamci
"""

def binary_search(array, numberToFind):
    """
    Perform binary search on a sorted list.

    Parameters:
        array (list of int): The sorted list to search in.
        numberToFind (int): The number to search for.

    Returns:
        int: The index of the number if found, otherwise -1.

    Example:
        >>> binary_search([1, 2, 3, 4], 3)
        2
    """
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2  # Integer division to get middle index

        if array[mid] < numberToFind:
            low = mid + 1
        elif array[mid] > numberToFind:
            high = mid - 1
        else:
            return mid  # Found the number

    return -1  # Not found


# Example array (must be sorted for binary search to work)
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Prompt user to enter a number to search for
i = int(input("Bir sayi giriniz: "))

# Perform binary search and store the result index
index = binary_search(array, i)

# Display result to the user
if index != -1:
    print(f"Number {i} found at index: {index}")
else:
    print(f"Number {i} not found")