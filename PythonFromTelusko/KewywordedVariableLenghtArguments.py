"""

This module demonstrates:
- How to use `**kwargs` to accept arbitrary keyword arguments in a function
- How to iterate through those key-value pairs dynamically

Author: Serhad
"""

def person(name, **data):
    """
    Prints a person's name followed by any number of additional keyword details.

    Parameters:
        name (str): The person's name
        **data: Arbitrary keyword arguments representing additional information

    Example:
        person("Navin", age=23, city="Mumbai", mob=2343)
    """
    print(name)  # Print the name

    # Iterate over all additional keyword arguments
    for key, value in data.items():
        print(key, value)

# Calling the function with variable keyword arguments
person("Navin", age=23, city="Mumbai", mob=2343)