"""
print_non_multiples_of_5.py

This script prints numbers from 1 to 19 that are **not divisible by 5**.

Author: Serhad Hamamci
"""

for i in range(1, 20):  # Loop from 1 to 19
    if(i % 5 != 0):     # If i is NOT divisible by 5
        print(i)        # Then print it