"""


This module demonstrates:
- Syntactic sugar in Python (e.g., `a + b` is actually `int.__add__(a, b)`)
- Operator overloading using special methods like `__add__`, `__sub__`, `__gt__`, and `__str__`
- How to control the string representation of custom objects

Author: Serhad
"""

# Regular addition of integers
a = 5
b = 5
print(a + b)               # Regular syntax
print(int.__add__(a, b))   # Same as above — syntactic sugar

# ----------------------------
# Custom class with operator overloading
# ----------------------------

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        # Overloads the + operator
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        return Student(m1, m2)

    def __sub__(self, other):
        # Overloads the - operator
        m1 = self.m1 - other.m1
        m2 = self.m2 - other.m2
        return Student(m1, m2)

    def __gt__(self, other):
        # Overloads the > operator
        return (self.m1 + self.m2) > (other.m1 + other.m2)

    def __str__(self):
        # Controls what is printed when print(student) is called
        return "{} {}".format(self.m1, self.m2)

# Creating student objects
s1 = Student(12, 23)
s2 = Student(24, 22)

# Add two Student objects
s3 = s1 + s2  # Internally calls Student.__add__(s1, s2)
print(s3.m1, s3.m2)

# Subtract two Student objects
s4 = s1 - s2  # Internally calls Student.__sub__(s1, s2)
print(s4.m1, s4.m2)

# Compare two Student objects
if s1 > s2:
    print("S1 wins")
else:
    print("S2 wins")

# Demonstrating __str__ customization
a = 0
print(a)              # Calls int.__str__()
print(str(a))         # Explicitly calls str
print(a.__str__())    # Directly calls method

print(s1)             # Calls Student.__str__(), prints marks instead of memory address

# Notes:
# - Operator overloading allows custom classes to behave like built-in types.
# - Only types like int, str, etc. have operators predefined — we define them manually for custom types.