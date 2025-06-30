"""

This script demonstrates:
- How to use `sys.argv` to read command-line arguments
- Parsing arguments as integers and using them in calculations

Author: Serhad

Usage:
$ python scriptname.py 5 7
Output:
12
"""

import sys

# sys.argv is a list where:
# sys.argv[0] is the script name itself
# sys.argv[1] is the first argument (after script name)
# sys.argv[2] is the second argument

# Convert command-line arguments to integers
x = int(sys.argv[1])
y = int(sys.argv[2])

# Simple addition
z = x + y
print(z)