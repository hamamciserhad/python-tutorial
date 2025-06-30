"""
polymorphism_ducktyping_module.py

This module demonstrates core object-oriented programming (OOP) concepts in Python:
- Polymorphism: Same method name used in different classes with different behavior
- Duck Typing: "If it walks like a duck and quacks like a duck, it's a duck"
- Method Overloading: Simulated using default arguments
- Method Overriding: Redefining parent method in child class
- Operator Overloading: Using special methods like __add__

Author: Serhad
"""

# Polymorphism in basic types
x = 5
print(type(x))  # <class 'int'>
x = "Serhad"
print(type(x))  # <class 'str'>
# Same variable 'x' can hold different types — dynamic typing

# -------------------------
# Duck Typing Example
# -------------------------

# First editor class
class Pycharm:
    def execute(self):
        print("Compiling in Pycharm")
        print("Running in Pycharm")

# Second editor class
class VSCode:
    def execute(self):
        print("Compiling in VSCode")
        print("Running in VSCode")

# The Laptop doesn't care what IDE it receives,
# as long as it has an 'execute' method — this is duck typing
class Laptop:
    def code(self, ide):
        ide.execute()

# Demonstration
ide1 = Pycharm()
ide2 = VSCode()

lap = Laptop()
lap.code(ide1)  # Calls execute() of Pycharm
lap.code(ide2)  # Calls execute() of VSCode

# In statically typed languages like Java,
# you would need an interface (e.g., IDE) that both classes implement.
# Python skips this — it just checks if the method exists at runtime.