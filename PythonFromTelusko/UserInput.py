"""


This script demonstrates:
- Using `input()` and converting input from string to int
- Accessing a single character from input (since Python has no 'char' type)
- Using `eval()` to dynamically evaluate expressions or numbers

Author: Serhad
"""

# --------------------------
# Standard numeric input and casting
# --------------------------

x = int(input("Enter a number: "))  # input() returns a string → convert to int
y = int(input("Enter another number: "))
z = x + y
print(z)

# Alternative: z = int(x) + int(y)  # Also valid if x and y were not pre-cast

# --------------------------
# Simulating character input in Python
# --------------------------

# Python doesn't have a 'char' type — it's just a string of length 1
t = input("Enter a character: ")[0]  # Get first character of the input string
print(t)

# --------------------------
# Using eval() to evaluate input as Python expression
# --------------------------

# eval() can interpret and evaluate Python expressions entered by the user
result = eval(input("Enter a number: "))  # Could also enter math like "2 + 3"
print(result)