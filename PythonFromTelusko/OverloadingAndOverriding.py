"""


This module demonstrates:
- Why Python does not support traditional method overloading (same method, different signatures)
- How to simulate overloading using default arguments and conditional logic
- How method overriding works in Python via inheritance

Author: Serhad
"""

class Student:
    # Python does NOT support method overloading based on parameter count or type
    # So we use default arguments (None) and conditional logic
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):
        """
        Simulates method overloading:
        - If 3 arguments → return a + b + c
        - If 2 arguments → return a + b
        - If only 1 argument → return a
        """
        if a is not None and b is not None and c is not None:
            return a + b + c
        elif a is not None and b is not None:
            return a + b
        else:
            return a

# Create student instances
s1 = Student(23, 11)
s2 = Student(24, 12)

# Simulated method overloading — only 1 argument passed
print(s1.sum(23))  # Output: 23

# ----------------------------
# Method Overriding Example
# ----------------------------

class A:
    def show(self):
        print("in a show")

class B(A):
    def show(self):
        # Overrides A's method
        print("in b show")

a1 = B()
a1.show()  # Output: "in b show" (method from B overrides A's version)