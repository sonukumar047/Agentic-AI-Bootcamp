# -----------------------------------------
# 1. Basic Syntax
# lambda arguments: expression
# -----------------------------------------

# Traditional function
def add(a, b):
    return a + b

# Lambda function equivalent
add_lambda = lambda a, b: a + b

print("Add (normal):", add(5, 3))
print("Add (lambda):", add_lambda(5, 3))

# -----------------------------------------
# 2. Lambda with One Argument
# -----------------------------------------
square = lambda x: x * x
print("Square of 4:", square(4))

# -----------------------------------------
# 3. Lambda Inside Another Function
# -----------------------------------------
def make_multiplier(n):
    return lambda x: x * n

double = make_multiplier(2)
triple = make_multiplier(3)

print("Double 5:", double(5))
print("Triple 5:", triple(5))

# -----------------------------------------
# 4. Lambda with Built-in Functions
# -----------------------------------------

# Using lambda with map()
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, nums))
print("Squares using map:", squares)

# Using lambda with filter()
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers using filter:", evens)

# Using lambda with sorted()
students = [("Alice", 85), ("Bob", 75), ("Clara", 95)]
# Sort by score (index 1)
sorted_students = sorted(students, key=lambda student: student[1])
print("Sorted by score:", sorted_students)

# -----------------------------------------
# 5. Lambda vs Def
# -----------------------------------------
# Use `def` when:
# - The function is complex
# - You need multiple lines
# - You want reusability and readability

# Use `lambda` when:
# - You need a simple function
# - Used only once or short-term
# - Typically passed as argument to other functions

# -----------------------------------------
# Summary:
# - `lambda` creates anonymous one-line functions.
# - Often used with `map()`, `filter()`, `sorted()`, etc.
# - Not suitable for complex logic — use `def` instead.
# -----------------------------------------
