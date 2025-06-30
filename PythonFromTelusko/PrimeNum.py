"""

This script checks whether a given number is prime using a for-else loop.

Author: Serhad
"""

num = 2  # Number to check

# Loop from 2 to num-1
for i in range(2, num):
    if num % i == 0:
        print("Not prime")  # Found a divisor → not prime
        break
else:
    # Only runs if loop wasn't broken → number is prime
    print("Prime")