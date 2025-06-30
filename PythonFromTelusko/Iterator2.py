"""

This module demonstrates:
- How to implement a custom iterator class in Python
- How `__iter__()` and `__next__()` methods work together
- The one-time nature of iterators (they get exhausted after use)

Author: Serhad
"""

class TopTen:
    def __init__(self):
        self.num = 1  # Start from 1

    def __iter__(self):
        return self  # The object itself is the iterator

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1  # Move to the next number
            return val
        else:
            raise StopIteration  # Ends the iteration when limit is reached

# Create an iterator object from TopTen class
values = TopTen()

# First call to next() — prints 1
print(next(values))

# This loop continues from where the iterator was left (starts from 2)
# Because the iterator object is now at num = 2
for i in values:
    print(i)