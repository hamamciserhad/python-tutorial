"""


This module demonstrates:
- Recursive function implementation in Python
- Handling invalid input with `raise` to throw a custom exception

Author: Serhad
"""

def factorial(n):
    """
    Calculates the factorial of a non-negative integer using recursion.

    Parameters:
        n (int): The number to calculate factorial for

    Returns:
        int: Factorial of the number

    Raises:
        ValueError: If the input number is negative

    Example:
        >>> factorial(5)
        120
    """
    if n < 0:
        raise ValueError("Factorial of a negative number is undefined.")
    elif n < 2:
        return 1
    else:
        return n * factorial(n - 1)

# Prompt the user for input and compute the factorial
x = int(input("Bir sayi giriniz:"))  # "Enter a number:"
print(factorial(x))