"""


This module demonstrates:
- The difference between class variables (shared/static) and instance variables (unique per object)
- How modifying a class variable on an instance actually creates a new instance variable (shadowing)

Author: Serhad
"""

class Car:
    wheels = 4  # Class variable (static) — shared by all instances

    def __init__(self, mil, company):
        self.mil = mil           # Instance variable
        self.company = company   # Instance variable

    def display(self):
        # Displays current object state
        return f"{self.mil}, {self.company}, {self.wheels}"

# ------------------------
# Object 1 modifies class variable via the instance
# ------------------------

c1 = Car(23, 186)
c1.wheels = 5  # Creates an instance-level variable 'wheels' (does NOT modify the class-level one)
print(c1.display())  # Uses c1's own wheels: 5

# ------------------------
# Object 2 does NOT override 'wheels'
# ------------------------

c2 = Car(2, 186)
print(c2.display())  # Uses class-level wheels: 4