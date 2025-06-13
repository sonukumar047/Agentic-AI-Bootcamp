# -----------------------------------------
# 1. Creating a Set
# -----------------------------------------

# Using curly braces
my_set = {1, 2, 3, 4}
print("Set:", my_set)

# Using set() constructor
mixed_set = set([1, "hello", 3.14])
print("Mixed set:", mixed_set)

# Duplicates are automatically removed
dup_set = {1, 2, 2, 3, 4, 4, 5}
print("No duplicates:", dup_set)  # {1, 2, 3, 4, 5}

# -----------------------------------------
# 2. Adding & Removing Elements
# -----------------------------------------
my_set.add(6)          # Add single element
my_set.update([7, 8])  # Add multiple elements
print("After adding:", my_set)

my_set.remove(3)       # Removes 3, raises error if not found
my_set.discard(100)    # Removes 100 if exists (no error)
popped = my_set.pop()  # Removes random element
print("After removing:", my_set)
print("Popped:", popped)

# -----------------------------------------
# 3. Set Operations
# -----------------------------------------
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union - elements from both sets
print("Union:", set1 | set2)  # or set1.union(set2)

# Intersection - common elements
print("Intersection:", set1 & set2)  # or set1.intersection(set2)

# Difference - elements in set1 but not in set2
print("Difference:", set1 - set2)

# Symmetric Difference - elements in either set, not both
print("Symmetric Difference:", set1 ^ set2)

# -----------------------------------------
# 4. Set Functions
# -----------------------------------------
print("Length of set1:", len(set1))
print("Is 2 in set1?", 2 in set1)

# Clear all items
set1.clear()
print("After clear:", set1)  # Empty set

# -----------------------------------------
# 5. Frozen Set (Immutable Set)
# -----------------------------------------
frozen = frozenset([1, 2, 3])
print("Frozen Set:", frozen)

# frozen.add(4)  ❌ Error: 'frozenset' object has no attribute 'add'

# -----------------------------------------
# Summary:
# - Sets store unique, unordered elements.
# - Supports operations: union, intersection, difference, etc.
# - Mutable, except for frozenset.
# -----------------------------------------

