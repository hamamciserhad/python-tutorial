"""
Tutorial: Working with NumPy Arrays and Matrices in Python
Author: Serhad Hamamci

This script demonstrates various operations using NumPy, a powerful numerical computing library in Python.
Topics covered:
- Creating 2D arrays
- Accessing array properties (dtype, ndim, shape, size)
- Flattening a 2D array into 1D
- Reshaping a 1D array into 3D
- Using the matrix class
- Extracting diagonals
- Matrix multiplication
"""
import numpy

# Create a 2D NumPy array
arr = numpy.array([[1, 2, 3, 32, 4, 5], [4, 5, 3, 2, 1, 6]])
# Print array data type, number of dimensions, shape, and total number of elements
print(arr.dtype)
print(arr.ndim)
print(arr.shape)
print(arr.size)

# Flatten the 2D array into a 1D array
arr2 = arr.flatten()
print(arr2)

# Reshape the 1D array into a 3D array (2x2x3)
arr3 = arr2.reshape(2, 2, 3)
print(arr3)

# Create NumPy matrices using the matrix class
m = numpy.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m1 = numpy.matrix([[1, 3], [1, 3], [4, 5]])
# Print the matrix
print(m)
# Extract the diagonal elements from the matrix
print(m.diagonal())
# Find the maximum value in the matrix
print(m.max())
# Perform matrix multiplication
print(m * m1)
