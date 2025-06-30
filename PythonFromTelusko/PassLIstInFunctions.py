"""


This module demonstrates:
- Counting even and odd numbers in a given list
- Returning multiple values using a tuple
- Tuple unpacking when receiving the result

Author: Serhad
"""

def count(lst):
    """
    Counts the number of even and odd integers in a list.

    Parameters:
        lst (list of int): The list to analyze

    Returns:
        tuple: (even_count, odd_count)
    """
    even = 0
    odd = 0

    for item in lst:
        if item % 2 == 0:
            even += 1
        else:
            odd += 1

    return (even, odd)  # Returns a tuple

# Call the function and unpack the result
cift, tek = count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Print the result using formatted string
print("Even: {} and Odd: {}".format(cift, tek))