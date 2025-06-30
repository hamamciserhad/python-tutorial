"""


This module demonstrates:
- How to use lambda functions with `filter()`, `map()`, and `reduce()`
- How to build a simple data processing pipeline in Python
- The difference between `map()` and `reduce()`

Author: Serhad
"""

from functools import reduce

# Sample helper function (not used)
def even(x):
    return x % 2 == 0  # True if x is even

# Sample list to process
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Step 1: Use filter() with a lambda to get even numbers only
b = filter(lambda x: x % 2 == 0, a)

# Note: filter() returns an iterator. If you do 'list(b)' once,
# you can't use it again. Best practice is to cast to list if needed.

# Step 2: Use map() with a lambda to multiply each even number by 2
# Example: [2, 4, 6] → [4, 8, 12]
def carp(x):
    return x * 2  # Not used, just for explanation

c = map(lambda x: x * 2, b)

# Step 3: Use reduce() to sum all elements in the mapped list
# Unlike map(), reduce() combines all values into one result using a binary function
def add_all(a, b):
    return a + b  # Not used, lambda is used instead

# Final result: sum of all doubled even numbers
d = reduce(lambda a, b: a + b, c)

print(d)  # Output: 2+4+6+8+10 = 30 → doubled → 60