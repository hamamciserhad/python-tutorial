"""
generator_examples_module.py

This module demonstrates:
- How Python generator functions work using `yield`
- The difference between a generator function (`yield`) and a regular function (`return`)
- How generators are memory-efficient and return values one at a time using iterators

Author: Serhad
"""

# Generator function: yields values one at a time
def topten():
    # Unlike return, yield pauses the function and saves its state
    yield 4  # First yielded value
    yield 1  # Second
    yield 3  # Third

# Regular function: returns a single value and exits
def topten2():
    return 4

# Generator function to yield squares of numbers from 1 to 10
def sqr():
    n = 1
    while n <= 10:
        yield n * n  # Generates next square value
        n += 1

# topten() creates a generator object
value = topten()
print(value)  # Shows generator object (memory address)

# topten2() is just a normal return value
values = topten2()
print(values)  # Output: 4

# Get first value using __next__()
print(value.__next__())  # Output: 4

# Remaining values from the generator
for i in value:
    print(i)  # Output: 1, then 3

# Generator for squares from 1 to 10
valuee = sqr()
for i in valuee:
    print(i)  # Outputs 1, 4, 9, ..., 100