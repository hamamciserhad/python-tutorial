"""

This module demonstrates:
- How to create a custom iterator class in Python using `__iter__()` and `__next__()`
- How the `StopIteration` exception is used to signal the end of iteration
- The difference between iterable and iterator objects

Author: Serhad
"""

class EvenNumbers:
    def __init__(self, limit, number=0):
        self.limit = limit  # Upper bound for even numbers
        self.number = number  # Starting point (default: 0)

    def __iter__(self):
        return self  # The object itself is its own iterator

    def __next__(self):
        if self.number < self.limit:
            result = self.number
            self.number += 2  # Move to next even number
            return result
        else:
            raise StopIteration  # Signals that iteration is complete

# Create an instance of EvenNumbers with limit 10
nums = EvenNumbers(10)

# Create an iterator from the object (technically calls nums.__iter__())
it = iter(nums)

# Use a while loop with try-except to exhaust the iterator
while True:
    try:
        print(next(it))  # Equivalent to it.__next__()
    except StopIteration:
        print("Bitti.")  # "Finished." — end of iteration
        break