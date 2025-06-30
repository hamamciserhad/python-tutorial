"""

This script demonstrates:
- Using nested `while` loops in Python
- Controlling output formatting with `end=""` to print on the same line
- Resetting the inner loop (`j`) inside the outer loop (`i`)

Author: Serhad
"""

i = 1  # Initialization for outer loop

while (i < 5):  # Outer loop condition
    print("Serhad", end=" ")  # Print on the same line

    j = 1  # Initialization for inner loop
    while (j < 5):  # Inner loop condition
        print("Rocks", end=" ")  # Print without newline
        j = j + 1  # Increment inner loop

    i += 1  # Increment outer loop
    print()  # Newline after inner loop finishes