"""

This module demonstrates the usage of `continue` and `pass` statements in Python.

Topics Covered:
1. Skipping certain iterations in a while loop using `continue`.
2. Using `pass` as a placeholder in a control structure.

Author: Serhad Hamamci
"""

# Example 1: Using `continue` to skip numbers divisible by 3 or 5
x = int(input("Get a number: "))
i = 1
while i <= x:
    if i % 3 == 0 or i % 5 == 0:
        i += 1
        continue  # Skip the rest of the loop and go to the next iteration
    print(i)
    i += 1


# Example 2: Using `pass` as a placeholder for an empty block
for i in range(1, 12):
    if (i % 2 != 0):
        pass  # We don't want to print odd numbers, but we need a statement here
    else:
        print(i)  # Print even numbers only