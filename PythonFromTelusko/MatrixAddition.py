"""


This module demonstrates two ways of performing matrix addition in Python:
1. Using NumPy's `matrix` class for element-wise addition.
2. Manually adding two matrices represented as nested lists, with validation.

Author: Serhad
"""

from numpy import *

# Using NumPy's matrix class for clean and efficient matrix addition
m1 = matrix([[1, 2, 3], [4, 5, 6]])
m2 = matrix([[7, 8, 9], [10, 11, 12]])

print(m1 + m2)  # Automatically performs element-wise matrix addition

# ---------------------
# Manual matrix addition using nested lists
# ---------------------

a = [[1, 2, 3], [4, 5, 6]]
b = [[7, 8, 9], [10, 11, 12]]
res = [[0, 0, 0], [0, 0, 0]]  # Initialize result matrix with zeros

try:
    # Check that the number of rows match
    if len(a) != len(b):
        raise Exception("Row counts of the matrices are not equal.")

    # Check each row's column count
    for i in range(len(a)):
        if len(a[i]) != len(b[i]):
            raise Exception(f"Column counts do not match in row {i}.")

    # Perform element-wise addition
    for i in range(len(a)):
        for j in range(len(b[0])):
            res[i][j] = a[i][j] + b[i][j]

    # Print resulting matrix
    for e in res:
        print(e)

except Exception as e:
    print(e)