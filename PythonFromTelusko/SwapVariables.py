"""


This module demonstrates 3 ways to swap the values of two variables in Python:
1. Using a temporary variable
2. Using arithmetic operations (without a third variable)
3. Using Python's tuple unpacking (most Pythonic)

Author: Serhad
"""

# ------------------------
# 1. Using a temporary variable
# ------------------------
a = 5
b = 6

temp = a
a = b
b = temp

print(a)  # 6
print(b)  # 5
print(temp)  # 5 (old value of 'a')

# ------------------------
# 2. Using arithmetic operations
# ------------------------
c = 3
d = 8

c = c + d  # c = 11
d = c - d  # d = 3
c = c - d  # c = 8

print(c)  # 8
print(d)  # 3

# ------------------------
# 3. Using tuple unpacking (Pythonic way)
# ------------------------
f = 8
g = 7

f, g = g, f  # Swap in one line

print(f)  # 7
print(g)  # 8