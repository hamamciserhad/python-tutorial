"""

This module demonstrates:
- Taking a list of names as input from the user
- Using a function to count how many names are longer than 5 characters and how many are not
- Returning multiple values from a function as a tuple

Author: Serhad
"""

def count(lst):
    """
    Counts how many strings in the list have length > 5 and how many ≤ 5.

    Parameters:
        lst (list of str): A list of names (strings)

    Returns:
        tuple: (more, less) — more = count of names > 5 characters,
                              less = count of names ≤ 5 characters
    """
    more = 0
    less = 0

    for x in range(len(lst)):
        if len(lst[x]) > 5:
            more += 1
        else:
            less += 1

    return (more, less)

# Collect names from user
lst = []
for i in range(10):
    name = input("Enter name {}:".format(i + 1))
    lst.append(name)

# Count names based on length
more, less = count(lst)

# Print result
print("Less than 5: {} and more than 5: {}".format(more, less))