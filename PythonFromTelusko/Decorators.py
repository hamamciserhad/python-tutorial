"""


This module demonstrates how to use decorators in Python to modify the behavior
of an existing function without changing its source code.

Use Case:
- You want to make sure the larger number is always the numerator during division.
- Instead of modifying the original `div` function, you can wrap it with a decorator.

Author: Serhad
"""


def div(a, b):
    """
    Performs division of two numbers. 
    Originally assumes that a >= b for meaningful output.

    Parameters:
        a (int or float): Numerator
        b (int or float): Denominator

    Returns:
        float: Result of a / b
    """
    if a < b:
        a, b = b, a  # Swap to ensure numerator is larger
    return a / b


def smart_div(func):
    """
    A decorator that wraps a division function and ensures that
    the larger number is always used as the numerator.

    Parameters:
        func (function): The original function to decorate

    Returns:
        function: A wrapped version of the function
    """

    def inner(a, b):
        if a < b:
            a, b = b, a  # Swap if needed
        return func(a, b)

    return inner


# Normally, if you want to modify behavior, you'd touch the function code.
# But with decorators, you can alter logic externally.

# Decorating the 'div' function with 'smart_div' without modifying it directly
div1 = smart_div(div)

# Output will always be a larger number divided by smaller, regardless of input order
print(div1(2, 4))  # Output: 2.0