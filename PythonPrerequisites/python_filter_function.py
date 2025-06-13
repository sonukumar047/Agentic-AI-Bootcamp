# -----------------------------------------
# 1. Basic Syntax
# filter(function, iterable)
# -----------------------------------------

# Define a function to check even numbers
def is_even(n):
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]

# Use filter to get even numbers
evens = filter(is_even, numbers)

# Convert to list
print("Even numbers:", list(evens))  # [2, 4, 6]

# -----------------------------------------
# 2. Using filter() with lambda
# -----------------------------------------

# Filter out numbers greater than 10
nums = [5, 10, 15, 20, 25]
greater_than_10 = filter(lambda x: x > 10, nums)
print("Greater than 10:", list(greater_than_10))  # [15, 20, 25]

# -----------------------------------------
# 3. filter() with strings
# -----------------------------------------

# Filter words longer than 4 characters
words = ["hi", "hello", "world", "python", "is", "fun"]
long_words = filter(lambda w: len(w) > 4, words)
print("Long words:", list(long_words))  # ['hello', 'world', 'python']

# -----------------------------------------
# 4. filter() returns an iterator
# -----------------------------------------

# You must convert to list or tuple to see results
vowels = ['a', 'e', 'i', 'o', 'u']
letters = "education"

# Filter only vowels from string
filtered_vowels = filter(lambda ch: ch in vowels, letters)
print("Vowels in 'education':", list(filtered_vowels))  # ['e', 'u', 'a', 'i', 'o']

# -----------------------------------------
# 5. Comparison: map() vs filter()
# -----------------------------------------

# map(): transforms each item
print("Mapped:", list(map(lambda x: x * 2, [1, 2, 3])))  # [2, 4, 6]

# filter(): selects items based on condition
print("Filtered:", list(filter(lambda x: x % 2 == 0, [1, 2, 3])))  # [2]

# -----------------------------------------
# Summary:
# - `filter()` selects items that meet a condition (function returns True).
# - Often used with `lambda`.
# - Returns an iterator → convert to list/tuple.
# -----------------------------------------
