# -----------------------------------------
# 1. Basic Function
# -----------------------------------------
def greet():
    print("Hello, welcome to Python!")

greet()  # Call the function


# -----------------------------------------
# 2. Function with Parameters
# -----------------------------------------
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Alice")


# -----------------------------------------
# 3. Function with Return Value
# -----------------------------------------
def add(a, b):
    return a + b

result = add(10, 5)
print("Sum is:", result)


# -----------------------------------------
# 4. Default Parameter Value
# -----------------------------------------
def welcome(name="Guest"):
    print(f"Welcome, {name}!")

welcome()             # Uses default
welcome("Sonu")       # Overrides default


# -----------------------------------------
# 5. Keyword Arguments
# -----------------------------------------
def profile(name, age):
    print(f"Name: {name}, Age: {age}")

profile(age=30, name="Bob")  # Order doesn’t matter


# -----------------------------------------
# 6. Variable-Length Arguments
# -----------------------------------------

# *args → non-keyword variable arguments (tuple)
def total_sum(*args):
    print("Args:", args)
    return sum(args)

print("Total:", total_sum(1, 2, 3, 4))

# **kwargs → keyword variable arguments (dictionary)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=28, city="Mumbai")


# -----------------------------------------
# 7. Nested Functions
# -----------------------------------------
def outer():
    print("Outer function")

    def inner():
        print("Inner function")

    inner()

outer()


# -----------------------------------------
# 8. Lambda Function (Anonymous Function)
# -----------------------------------------
square = lambda x: x * x
print("Square of 5:", square(5))

# Another example
add = lambda a, b: a + b
print("Lambda add:", add(3, 4))


# -----------------------------------------
# 9. Function with Type Hints (Optional)
# -----------------------------------------
def multiply(a: int, b: int) -> int:
    return a * b

print("Multiply:", multiply(3, 4))


# -----------------------------------------
# Summary:
# - Define a function with `def`.
# - Use `return` to return a value.
# - Use `*args` for many positional args, `**kwargs` for many keyword args.
# - Use `lambda` for small, one-line functions.
# -----------------------------------------
