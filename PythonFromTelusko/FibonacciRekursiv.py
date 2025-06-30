"""


This module demonstrates:
- Recursive implementation of the Fibonacci sequence
- Exception handling for negative inputs using `raise`
- Printing a sequence of Fibonacci numbers and a specific nth Fibonacci number

Author: Serhad
"""

def fibonacci(n):
    """
    Recursively calculates the nth Fibonacci number.

    Parameters:
        n (int): The position in the Fibonacci sequence (0-based index)

    Returns:
        int: The nth Fibonacci number

    Raises:
        ValueError: If n is negative

    Example:
        >>> fibonacci(0) -> 0
        >>> fibonacci(1) -> 1
        >>> fibonacci(5) -> 5
    """
    if n < 0:
        raise ValueError("Fibonacci is undefined for negative numbers.")
    elif n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Get input from user and print a sequence of Fibonacci numbers
x = int(input("Bir sayi girin: "))  # "Enter a number:"
for i in range(x):
    print(fibonacci(i))

# Get another input and print only the nth Fibonacci number
y = int(input("Bir sayi girin: "))  # "Enter a number:"
print(fibonacci(y))