"""


This module demonstrates:
- The difference between formal and actual arguments
- The 4 types of actual arguments in Python:
    1. Positional
    2. Keyword
    3. Default
    4. Variable-length (`*args`, `**kwargs`)

Author: Serhad
"""

# -------------------------------
# Example: Default + Keyword Argument
# -------------------------------
def person(name, age=19):  # 'age' has a default value
    print("name:", name)
    print("age:", age + 2)  # Adding 2 just to show logic

# Called using keyword argument
person(name="Serhad")  # Output: name: Serhad, age: 21

# -------------------------------
# Example: Variable-length Arguments
# -------------------------------
def my_sum(a, *b):
    """
    Adds any number of values.
    'a' is a required positional argument,
    '*b' collects the rest as a tuple.
    """
    c = a + sum(b)
    print(c)

# Positional argument 1, followed by variable-length arguments
my_sum(1, 2, 3, 4, 5, 6)  # Output: 21