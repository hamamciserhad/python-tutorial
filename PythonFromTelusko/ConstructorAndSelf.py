"""

This module demonstrates:
- Creating class instances using constructors
- Displaying object attributes with a method
- Comparing two objects based on their attributes (not their memory addresses)

Author: Serhad Hamamci
"""

class Computer:
    def __init__(self, name, age, height):
        """
        Constructor to initialize a Computer object.

        Parameters:
            name (str): Name of the person or machine.
            age (int): Age value.
            height (int): Height in cm (or any unit).
        """
        self.name = name
        self.age = age
        self.height = height

    def display(self):
        """
        Displays the attributes of the object.
        """
        print(self.name, self.age, self.height)

    def compare(self, other):
        """
        Compares this object with another Computer object.
        The comparison is based on attribute values, not memory addresses.

        Parameters:
            other (Computer): Another object to compare with.

        Returns:
            bool: True if all attributes match, False otherwise.
        """
        return (
            self.age == other.age and
            self.height == other.height and
            self.name == other.name
        )


# Creating two objects with the same attribute values
c1 = Computer("Serhad", 23, 186)
c1.display()

c2 = Computer("Serhad", 23, 186)
c2.display()

# Comparing based on values, not memory addresses
if c1.compare(c2):
    print("equal")
else:
    print("not equal")