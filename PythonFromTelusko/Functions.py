"""
function_basics_module.py

This module demonstrates:
1. How to define and call simple functions
2. How a Python function can return multiple values using tuples

Author: Serhad
"""

# A simple function that prints a greeting
def greet():
    print("Hello")

# Calling the greet function twice
greet()
greet()

# A function that returns both sum and difference of two numbers
# In Python, functions can return multiple values separated by commas
# These are automatically packed into a tuple
def add_sub(x, y):
    return x + y, x - y

# Call add_sub and print the returned tuple
print(add_sub(1, 2))  # Output: (3, -1)