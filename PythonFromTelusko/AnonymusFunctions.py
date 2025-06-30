"""

This module demonstrates how to use anonymous (lambda) functions in Python.

Author: Serhad Hamamci
"""


def square(x):
    """
    Calculate the square of a number using a traditional function.

    Parameters:
        x (int or float): The number to square.

    Returns:
        int or float: The square of the input.

    Example:
        >>> square(4)
        16
    """
    return x * x  # Single-line return for squaring


# Using a lambda function to achieve the same result as 'square'
f = lambda a: a * a  # Equivalent to square(a)

# Example usage
if __name__ == "__main__":
    print("Using traditional function:")
    print(square(4))  # Output: 16

    print("Using lambda function:")
    print(f(4))  # Output: 16