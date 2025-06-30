"""

This module demonstrates:
- Element-wise operations on NumPy arrays
- Applying mathematical functions like log and min
- Array concatenation
- Difference between shallow copy (`view()`) and deep copy (`copy()`)

Author: Serhad
"""

import numpy as np

# Create two NumPy arrays
arr = np.array([1, 2, 3, 4, -1, 5])
arr2 = np.array([12, 22, 23, 42, 12, 25])

# Element-wise addition with scalar
arr = arr + 3  # Adds 3 to each element
print(arr)

# Element-wise addition with another array (must be same shape)
arr3 = arr + arr2
print(arr3)

# Apply mathematical functions on the array
print(np.log(arr))  # Natural log of each element
print(np.min(arr))  # Minimum value in the array

# Concatenate two arrays along axis 0 (default)
arrCon = np.concatenate((arr, arr2), axis=0)
print(arrCon)

# ----------------------------
# Copying arrays (shallow vs deep)
# ----------------------------

# Shallow copy using view() → shares memory
arrCopy = arr.view()
arr[1] = 8  # This change affects arrCopy too
print(arrCopy)  # arrCopy[1] is also changed
print(id(arrCopy))  # Same memory location as arr (for data)
print(id(arr))      # Still separate Python objects, but share data

# Deep copy using copy() → independent memory
arrDeepCopy = arr.copy()
arr[1] = 9  # This change does NOT affect arrDeepCopy
print(arrDeepCopy)  # arrDeepCopy[1] remains as before
print(id(arrDeepCopy))  # Different memory location
print(id(arr))          # Still different from arr