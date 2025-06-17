# -----------------------------------------
# 1. Function Copy (Assign function to another variable)
# -----------------------------------------

def greet(name):
    return f"Hello, {name}!"

say_hello = greet  # Copy function reference

print(greet("Sonu"))      # Original
print(say_hello("Kumar")) # Copied

# -----------------------------------------
# 2. Closures
# -----------------------------------------
# A closure is a function that retains access to variables from its enclosing scope.

def outer_function(msg):
    def inner_function():
        print("Message:", msg)  # msg is from outer scope
    return inner_function

my_closure = outer_function("Python is awesome")
my_closure()  # Output: Message: Python is awesome

# Another example with counter

def make_counter():
    count = 0
    def counter():
        nonlocal count  # Modify outer variable
        count += 1
        return count
    return counter

counter1 = make_counter()
print(counter1())  # 1
print(counter1())  # 2
print(counter1())  # 3

# -----------------------------------------
# 3. Decorators
# -----------------------------------------
# A decorator is a function that wraps another function and adds behavior.

def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hi():
    print("Hi!")

say_hi()

# -----------------------------------------
# 4. Decorator with Arguments
# -----------------------------------------

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet_user():
    print("Welcome!")

greet_user()  # Will print 3 times

# -----------------------------------------
# 5. Decorator for Measuring Execution Time
# -----------------------------------------
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.4f} sec")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(1)
    print("Done with slow task.")

slow_function()

# -----------------------------------------
# Summary:
# - Function copy assigns the reference, not a new function.
# - Closures retain access to enclosing scope variables.
# - Decorators add behavior to functions (logging, auth, timing).
# - Use `@decorator` syntax or manually wrap functions.
# -----------------------------------------
