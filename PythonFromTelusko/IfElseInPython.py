"""


This module demonstrates:
- How to use `if`, `elif`, and `else` blocks in Python
- The importance of correct indentation (block structure)
- Nested `if` statements within another `if` block

Author: Serhad
"""

x = int(input("Enter a number: "))  # Prompt the user for a number

# First condition: check if the number is even
if x % 2 == 0:
    print("cift")  # "Even" in Turkish — this is inside the first if block

    # Nested if inside the even check
    if x > 5:
        print("great")  # If even and greater than 5
    else:
        print("not great")  # If even but not greater than 5

# Second condition: runs only if the first if fails
elif x % 1 == 0:  # All integers satisfy x % 1 == 0 — acts like an "else" here
    print("tek")  # "Odd" in Turkish (though logic isn't perfect here)

# Outside all condition blocks
print("Bitti")  # Means "Finished"