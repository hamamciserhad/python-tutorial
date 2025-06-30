"""


This module demonstrates:
- How to implement a basic linear search in Python
- How to return the index of a value if found, otherwise return -1

Author: Serhad
"""

def search(array, index):
    """
    Searches for a given value in the list using linear search.

    Parameters:
        array (list of int): The list to search in
        index (int): The value to search for

    Returns:
        int: The index of the value if found, otherwise -1
    """
    for i in range(len(array)):
        if array[i] == index:
            return i  # Return the index as soon as it's found
    else:
        return -1  # If loop completes, value was not found

# Sample list
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Call the search function
index = search(array, 8)

# Print the result
print(index)  # Output: 7