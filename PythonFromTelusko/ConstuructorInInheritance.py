"""

This module demonstrates:
- Constructors in inheritance
- Multiple inheritance in Python
- Method Resolution Order (MRO)
- Usage of `super()` in multi-class scenarios

Author: Serhad
"""

# Helper function to print a visual separator line
def line():
    print("-" * 40)

# Base class A
class A:
    def __init__(self):
        print("in A init")  # Constructor of class A

    def feature1(self):
        print("feature1 from A")

    def feature2(self):
        print("feature2 from A")

# Base class B
class B:
    def __init__(self):
        # In multiple inheritance, this ensures proper constructor chaining
        super().__init__()
        print("in B init")  # Constructor of class B

    def feature1(self):
        print("feature1 from B")  # Overrides A's method if B is first in MRO

    def feature3(self):
        print("feature3 from B")

    def feature4(self):
        print("feature4 from B")

# Derived class C inherits from both A and B
class C(A, B):  # Python uses Method Resolution Order (MRO) — A comes before B
    def __init__(self):
        # Calls the constructor of A due to MRO (A is first in the inheritance list)
        super().__init__()
        print("in C init")  # Constructor of class C

    def feat(self):
        # Explicitly calls feature2 from A via super()
        super().feature2()

# Let's create an instance of class C and observe the constructor calls
line()
a1 = C()  # Triggers constructors: A → then C (B's constructor is skipped due to MRO unless B uses cooperative super() chain)
line()

# feature1 exists in both A and B.
# Since A comes first in MRO, A's version of feature1 will be used.
a1.feature1()
a1.feat()
line()