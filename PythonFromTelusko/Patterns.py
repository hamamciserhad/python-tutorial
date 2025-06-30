"""

This script prints a reverse left-aligned triangle using nested loops.

Author: Serhad
"""

for j in range(5):  # Outer loop for rows
    for k in range(4 - j):  # Inner loop for decreasing number of '#' per row
        print("#", end=" ")  # Print hash without newline
    print()  # Move to next line after each row