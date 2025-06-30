"""


This module demonstrates:
- Basic exception handling in Python using `try`, `except`, and `finally`
- Catching specific exceptions like ZeroDivisionError and ValueError
- Ensuring that cleanup actions (like closing a resource) always happen

Author: Serhad
"""

a = 0
b = 0

# First try block: handles division by zero
try:
    print("Resource open")  # Simulate opening a resource
    print(a / b)  # Will raise ZeroDivisionError since b = 0
except ZeroDivisionError as e:
    print(f"Division error: {e}")  # Custom error message

# Second try block: handles invalid input conversion
try:
    k = int(input("Enter num:"))  # User input should be convertible to int
    print(k)
except ValueError as e:
    print(f"Invalid number entered: {e}")  # Handle non-integer input
finally:
    # This block will execute no matter what — exception or not
    print("Resource closed")  # Simulate releasing a resource