# -----------------------------------------
# 1. Creating a Tuple
# -----------------------------------------
my_tuple = (10, 20, 30)
print("Tuple:", my_tuple)

# Tuple without parentheses (optional)
another_tuple = 1, 2, 3
print("Tuple without (): ", another_tuple)

# Single-element tuple (comma is required!)
single = (5,)
print("Single-element tuple:", single)

# Using tuple() constructor
from_list = tuple([1, 2, 3])
print("Tuple from list:", from_list)

# -----------------------------------------
# 2. Accessing Elements
# -----------------------------------------
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Slicing
print("Sliced:", my_tuple[1:3])  # (20, 30)

# -----------------------------------------
# 3. Tuple is Immutable
# -----------------------------------------
# my_tuple[0] = 99 ❌ This will raise a TypeError

# -----------------------------------------
# 4. Looping Through Tuple
# -----------------------------------------
for value in my_tuple:
    print("Value:", value)

# -----------------------------------------
# 5. Tuple Unpacking
# -----------------------------------------
person = ("Alice", 25, "New York")
name, age, city = person
print(f"Name: {name}, Age: {age}, City: {city}")

# -----------------------------------------
# 6. Tuple Methods
# -----------------------------------------
numbers = (1, 2, 3, 2, 2, 4)

print("Count of 2:", numbers.count(2))  # 3
print("Index of 3:", numbers.index(3))  # 2

# -----------------------------------------
# 7. Nested Tuple
# -----------------------------------------
nested = ((1, 2), (3, 4))
print("Nested Tuple:", nested)
print("Access nested element:", nested[1][0])  # 3

# -----------------------------------------
# 8. Tuple vs List
# -----------------------------------------
# Tuples are:
# - Faster than lists
# - Cannot be modified (immutable)
# - Often used for fixed data (e.g., coordinates)

# Example use case: coordinates
point = (10.5, 20.3)

# -----------------------------------------
# Summary:
# - Tuples are immutable and ordered.
# - Use for fixed or read-only collections.
# - Support indexing, slicing, unpacking, and looping.
# -----------------------------------------
