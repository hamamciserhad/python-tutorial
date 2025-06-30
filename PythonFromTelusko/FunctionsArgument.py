"""

This module explains Python's function argument behavior.
Contrary to some languages, Python does NOT use:
- "Pass by Value" (like in Java primitives)
- "Pass by Reference" (like in C++ references)

Instead, Python uses **"Pass by Object Reference"**:
- All variables are **references to objects**.
- For immutable objects (e.g., int, str), you can't change the original object.
- For mutable objects (e.g., list, dict), modifications inside the function affect the original object.

Author: Serhad
"""

# Function that takes an immutable type (int)
def update(x):
    print(id(x))  # Shows memory address of x (same as 'a' initially)
    x = 8         # New int object assigned → creates a new object in memory
    print(id(x))  # Different memory address after assignment
    print("x:", x)

a = 10
print(id(a))      # Memory address of 'a'
update(a)         # Function tries to change 'x', but 'a' remains unchanged
print("a:", a)    # Still 10 → int is immutable

# Function that takes a mutable type (list)
def updateMutable(x):
    print(id(x))     # Same memory address as 'a'
    x[1] = 2         # Modifies the list in-place
    print(id(x))     # Still same address → change affects original list
    print("x:", x)

a = [3, 4, 5, 6]
print(id(a))         # Memory address of list
updateMutable(a)     # Modifies the second element
print("a:", a)       # Reflects the change → [3, 2, 5, 6]