"""
merge_sort_module.py

This module demonstrates:
- A full implementation of the Merge Sort algorithm in Python
- Use of helper functions and temporary arrays for in-place merging
- Divide-and-conquer approach to sort an array recursively

Author: Serhad
"""

def merge_sort(array, left, right, tempArray):
    """
    Recursively divides the array into halves and sorts each part.

    Parameters:
        array (list): The original list to sort
        left (int): Start index (inclusive)
        right (int): End index (exclusive)
        tempArray (list): Temporary list used for merging
    """
    if (right - left > 1):  # Base case: single-element range
        mid = (left + right) // 2
        merge_sort(array, left, mid, tempArray)   # Sort left half
        merge_sort(array, mid, right, tempArray)  # Sort right half
        merge(array, left, mid, right, tempArray) # Merge sorted halves

def merge(array, left, mid, right, tempArray):
    """
    Merges two sorted subarrays [left:mid] and [mid:right] into the main array.

    Parameters:
        array (list): Original array containing the subarrays
        left (int): Start index of the first subarray
        mid (int): End index of the first and start of the second
        right (int): End index of the second subarray
        tempArray (list): Temporary list to store merged results
    """
    i = left   # Pointer for left subarray
    j = mid    # Pointer for right subarray
    k = 0      # Pointer for tempArray

    # Merge step: compare elements from both halves
    while i < mid and j < right:
        if array[i] < array[j]:
            tempArray[k] = array[i]
            i += 1
        else:
            tempArray[k] = array[j]
            j += 1
        k += 1

    # Copy remaining elements from left subarray
    tempArray[k:k + (mid - i)] = array[i:mid]

    # Copy remaining elements from right subarray
    tempArray[k:k + (right - j)] = array[j:right]

    # Copy sorted tempArray back to original array segment
    array[left:right] = tempArray[0:right - left]

def helper_merge_sort(array):
    """
    Helper function to call merge_sort with required parameters.

    Parameters:
        array (list): The list to be sorted
    """
    tempArray = [0] * len(array)  # Pre-allocate temp array
    merge_sort(array, 0, len(array), tempArray)

# Example usage
nums = [3, 2, 1, 5, 33, 6]
helper_merge_sort(nums)
print(nums)  # Output will be the sorted list