"""

This module demonstrates how to use Python's built-in `zip()` function to combine multiple sequences.

Key Concepts:
- `zip()` takes iterables (e.g., lists, tuples) and aggregates them into tuples.
- The length of the resulting iterable matches the shortest input sequence.
- The result can be converted to list, set, or dict depending on your needs.

Author: Serhad
"""

# === Step 1: Define two sequences ===
names = ("Navin", "Serhad", "Ali")
comps = ("Dell", "Apple", "MS")

# === Step 2: Use zip() to combine elements pairwise ===
zipped = list(zip(names, comps))
print("Zipped list of pairs:", zipped)

# === Step 3: Convert the zipped object into a set ===
# Note: Sets are unordered and only hold unique pairs
setted = set(zip(names, comps))
print("Zipped set of pairs:", setted)

# === Step 4: Convert the zipped object into a dictionary ===
# 'names' → keys, 'comps' → values
dictionary = dict(zip(names, comps))
print("Zipped dictionary:", dictionary)