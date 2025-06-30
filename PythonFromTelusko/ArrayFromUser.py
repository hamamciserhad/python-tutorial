"""

This module demonstrates basic usage of the built-in 'array' module in Python.

Steps:
1. Create an empty integer array.
2. Ask the user to define the length of the array.
3. Populate the array via user input using a loop.
4. Print the array contents.
5. Ask the user to enter a number to search for.
6. Find and display the index of the number (if present).

Author: Serhad Hamamci
"""

import array  # Importing Python's built-in array module

# Creating an empty integer array (type code 'i' stands for signed int)
arr = array.array('i', [])

# Step 1: Ask the user for the desired length of the array
n = int(input("Enter length of array: "))

# Step 2: Populate the array with numbers from user input
for i in range(n):
    # Dynamic prompt using .format() — shows "Enter number 1", "Enter number 2", etc.
    arr.append(int(input("Enter number {}: ".format(i + 1))))

# Step 3: Print the entire array object
print(arr)

# Step 4: Ask the user to enter a number to search for
val = int(input("Enter number search: "))

# Step 5: Manually search for the number's index in the array
for i in range(n):
    if arr[i] == val:
        print(i)

# Note: Alternatively, you can directly use the built-in method:
# print(arr.index(val))

# Reminder:
# Python does not have built-in 2D arrays like other languages.
# For advanced array handling (e.g., 2D or matrix), consider using NumPy library.