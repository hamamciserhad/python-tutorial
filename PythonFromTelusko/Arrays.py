"""

This module demonstrates advanced operations using Python's built-in 'array' module.

Operations shown:
1. Creating and printing an array.
2. Accessing array metadata using `buffer_info()` and `typecode`.
3. Reversing the array.
4. Iterating through array elements.
5. Creating a new array using generator expressions.

Author: Serhad
"""

import array

# Creating an integer array with both positive and negative values
arr = array.array('i', [1, 2, 3, 4, -1, 5])

# Print the array
print(arr)

# Print buffer information: (memory address, number of elements)
print(arr.buffer_info())

# Print the type code of the array ('i' means signed int)
print(arr.typecode)

# Reverse the array in-place
arr.reverse()
print(arr)

# Print each element of the reversed array
for i in range(len(arr)):
    print(arr[i])

# Create a new array by squaring numbers from 0 to len(arr) - 1
# The typecode is inherited from the original array
newArray = array.array(arr.typecode, (a * a for a in range(0, len(arr))))

# Print each element of the new array
for i in range(len(newArray)):
    print(newArray[i])