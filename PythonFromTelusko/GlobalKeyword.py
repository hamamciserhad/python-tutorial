"""
global_variables_module.py

This module demonstrates:
- The difference between global and local variables
- How to use the `global` keyword to modify a global variable inside a function
- How to use the `globals()` dictionary to access and update global variables dynamically

Author: Serhad
"""

# Global variable — accessible inside functions unless shadowed by local variables
a = 10

def something():
    global a  # Declaring that we are referring to the global 'a', not creating a new local one
    a = 12    # Modifies the global 'a'
    print("in func", a)

something()
print("outside", a)  # Global 'a' was updated → prints 12

# More advanced case: using 'globals()' to access and update global variables from inside a function

b = 10
c = 11

print(id(b))  # Memory address of global 'b'

def something2():
    b = 13  # This is a local variable 'b', shadowing the global one
    x = globals()["b"]  # Get the global 'b' using the globals() dictionary
    print(id(x))        # Should match the global 'b'
    x = 12              # This does NOT change the global 'b' — just reassigns local 'x'
    globals()["b"] = 15 # This line actually updates the global 'b'
    print("in func", b) # Still refers to local 'b', which is 13

something2()
print("outside", b)  # Global 'b' was changed to 15 using globals()