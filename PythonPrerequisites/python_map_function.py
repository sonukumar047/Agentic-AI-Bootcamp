# -----------------------------------------
# 1. Basic Syntax
# map(function, iterable)
# -----------------------------------------

# Define a simple function
def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]

# Apply map
squared = map(square, numbers)

# Convert to list to see result
print("Squared:", list(squared))  # [1, 4, 9, 16, 25]

# -----------------------------------------
# 2. Using map() with lambda
# -----------------------------------------
nums = [10, 20, 30]
doubled = map(lambda x: x * 2, nums)
print("Doubled:", list(doubled))  # [20, 40, 60]

# -----------------------------------------
# 3. Using map() with multiple iterables
# -----------------------------------------
a = [1, 2, 3]
b = [4, 5, 6]

# Add items from both lists
added = map(lambda x, y: x + y, a, b)
print("Element-wise sum:", list(added))  # [5, 7, 9]

# -----------------------------------------
# 4. map() with built-in functions
# -----------------------------------------
words = ["hello", "world", "python"]

# Convert all words to uppercase
uppercased = map(str.upper, words)
print("Uppercased:", list(uppercased))  # ['HELLO', 'WORLD', 'PYTHON']

# -----------------------------------------
# 5. map() returns an iterator
# -----------------------------------------
# Once consumed, it can't be reused
squares = map(lambda x: x ** 2, range(3))
print(list(squares))  # [0, 1, 4]
# print(list(squares))  # [] ← this will print an empty list again

# -----------------------------------------
# Summary:
# - `map()` applies a function to every item in an iterable.
# - Returns an iterator → convert to list/tuple to view.
# - Common with `lambda`, `def`, and built-in functions.
# - Works with one or more iterables.
# -----------------------------------------
