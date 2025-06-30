"""
for_else_module.py

This module demonstrates how to use Python's `for-else` construct,
which is often misunderstood or overlooked by beginners.

Key Concept:
- The `else` block after a `for` loop runs **only if the loop completes normally** (i.e., not interrupted by `break`).
- Useful for search operations — e.g., finding a matching item in a list.

Author: Serhad Hamamci
"""

nums = [1, 2, 3, 4, 5]

# Check if any number in the list is divisible by 5
for num in nums:
    if num % 5 == 0:
        print(num)
        break  # If found, break out of the loop

# This else belongs to the for-loop, not the if-statement
# It executes only if the loop wasn't interrupted by break
else:
    print("Not found")

# Notes:
# - This is similar to a "not found" case in Java using a flag variable
# - Python's for-else is a clean way to express this search pattern