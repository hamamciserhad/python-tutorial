"""


This module demonstrates:
- How to define and use an inner class in Python
- Creating a `Student` class with a nested `Comp` (Computer) class
- How to initialize and access inner class objects both internally and externally

Author: Serhad
"""

class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

        # Create a Comp object when a Student object is created
        self.comp = self.Comp("HP", "i5", 8)

    def show(self):
        # Display student info and inner Comp object info
        print(self.name, self.rollno)
        self.comp.show()

    # Inner class defined inside Student — useful if only Student uses it
    class Comp:
        def __init__(self, brand, cpu, ram):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram

        def show(self):
            # Display computer configuration
            print(self.brand, self.cpu, self.ram)

# Creating a Student object
s1 = Student("Sam", 2)
s1.show()  # Outputs: Sam 2 + HP i5 8

# Directly creating an inner class object externally
Student.Comp("HP", "i5", 8).show()  # Outputs: HP i5 8