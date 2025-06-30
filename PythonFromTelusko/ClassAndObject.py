"""

This module demonstrates how to define a class in Python, including:
- Class variables and methods
- The constructor method (__init__)
- Object creation and method invocation
- The use of f-strings for string formatting

Author: Serhad
"""

class Computer:
    # A class in Python contains variables and methods.
    # The constructor is defined using __init__.
    # The 'self' keyword refers to the instance (similar to 'this' in Java).

    def __init__(self, cpu, ram, gb):
        self.cpu = cpu     # Instance variable for CPU type
        self.ram = ram     # Instance variable for RAM size
        self.gb = gb       # Instance variable for memory (e.g., SSD/HDD)

    def config(self):
        """
        Prints the configuration of the computer using f-string formatting.
        f-strings allow embedding expressions inside string literals.
        """
        print(f"{self.cpu}, {self.ram} gb ram, {self.gb} Memory")

        # Note: self refers to the instance calling the method.
        # For example, calling com1.config() is internally like Computer.config(com1)


# Example of a basic string object (also an instance of a class)
a = "i"
print(type(a))  # Shows that 'a' is of type 'str'

# Creating an instance of the Computer class
com1 = Computer("m2", 16, "1 tb")  # Object with specified parameters

print(type(com1))  # Shows that com1 is an instance of Computer

# Calling a method on the instance
com1.config()