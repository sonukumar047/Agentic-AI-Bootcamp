# -----------------------------------------
# 1. Creating a List
# -----------------------------------------
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]

print(fruits)
print(numbers)

# -----------------------------------------
# 2. Accessing Elements
# -----------------------------------------
print(fruits[0])   # apple
print(fruits[-1])  # cherry (last item)

# -----------------------------------------
# 3. Modifying List
# -----------------------------------------
fruits[1] = "blueberry"  # Replace "banana"
print(fruits)

# -----------------------------------------
# 4. List Methods
# -----------------------------------------
fruits.append("orange")       # Add to end
fruits.insert(1, "mango")     # Insert at index 1
fruits.remove("apple")        # Remove by value
popped = fruits.pop()         # Remove last item
fruits.sort()                 # Sort alphabetically
print(fruits)
print("Popped item:", popped)

# -----------------------------------------
# 5. Looping Through a List
# -----------------------------------------
for fruit in fruits:
    print("Fruit:", fruit)

# -----------------------------------------
# 6. Check if Item Exists
# -----------------------------------------
if "cherry" in fruits:
    print("Cherry is in the list.")

# -----------------------------------------
# 7. List Length
# -----------------------------------------
print("List length:", len(fruits))

# -----------------------------------------
# 8. List Slicing
# -----------------------------------------
print(numbers[1:4])    # [2, 3, 4]
print(numbers[:3])     # [1, 2, 3]
print(numbers[::2])    # [1, 3, 5]

# -----------------------------------------
# 9. Nested Lists (2D List)
# -----------------------------------------
matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix[1][0])  # 3

# -----------------------------------------
# 10. List Comprehension
# -----------------------------------------

# Basic syntax: [expression for item in iterable if condition]

# Example 1: Create a list of squares
squares = [x**2 for x in range(6)]
print("Squares:", squares)  # [0, 1, 4, 9, 16, 25]

# Example 2: Filter even numbers
evens = [x for x in range(10) if x % 2 == 0]
print("Even numbers:", evens)

# Example 3: Create list of fruits with length > 5
long_fruits = [fruit for fruit in fruits if len(fruit) > 5]
print("Long fruits:", long_fruits)

# Example 4: Convert list of strings to uppercase
upper_fruits = [fruit.upper() for fruit in fruits]
print("Uppercase fruits:", upper_fruits)

# -----------------------------------------
# Summary:
# - Lists are ordered, mutable collections.
# - Use indexing, slicing, and methods to work with them.
# - List comprehensions offer a clean way to create new lists.
# -----------------------------------------
