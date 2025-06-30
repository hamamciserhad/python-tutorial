"""
multiple_inheritance_module.py

This module demonstrates:
- How to define classes and methods in Python
- How multiple inheritance works (a class inheriting from two base classes)
- How to create objects and call inherited methods

Author: Serhad Hamamci
"""

# Base class A
class A:
    def feature1(self):
        print("Feature 1")

    def feature2(self):
        print("Feature 2")

# Base class B (this class is not inheriting anything)
class B:
    def feature3(self):
        print("Feature 3")

    def feature4(self):
        print("Feature 4")

# Class C inherits from both A and B → multiple inheritance
class C(A, B):
    def feature5(self):
        print("Feature 5")

# Create object of class A and call its method
a1 = A()
a1.feature1()

# Create object of class B and call its method
b1 = B()
b1.feature3()

# Create object of class C (inherits from A and B)
c1 = C()
c1.feature1()  # Inherited from A