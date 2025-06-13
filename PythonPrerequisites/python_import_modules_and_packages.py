# -----------------------------------------
# 1. Importing a Built-in Module
# -----------------------------------------
import math  # imports entire math module

print("Square root of 16:", math.sqrt(16))
print("Pi:", math.pi)

# Import specific function
from math import pow, factorial
print("2^3:", pow(2, 3))
print("Factorial of 5:", factorial(5))

# Import with alias
import datetime as dt
print("Current time:", dt.datetime.now())

# -----------------------------------------
# 2. Creating and Importing a Custom Module
# -----------------------------------------
# Assume you have a file named `mymodule.py` with the following code:
# def greet(name):
#     return f"Hello, {name}!"

# You can import and use it like this:
# from mymodule import greet
# print(greet("Sonu"))

# OR
# import mymodule
# print(mymodule.greet("Sonu"))

# -----------------------------------------
# 3. Creating and Using Packages
# -----------------------------------------
# Directory structure:
# mypackage/
# ├── __init__.py        # makes it a package
# ├── greetings.py       # contains greet() function
# └── math_utils.py      # contains add(), subtract() functions

# greetings.py
# def greet(name):
#     return f"Hi, {name}!"

# math_utils.py
# def add(a, b): return a + b
# def subtract(a, b): return a - b

# Usage in another script:
# from mypackage.greetings import greet
# from mypackage.math_utils import add, subtract

# print(greet("Alice"))
# print(add(10, 5))
# print(subtract(10, 5))

# -----------------------------------------
# 4. Using dir() and help()
# -----------------------------------------
print("Functions in math module:", dir(math))  # lists all functions
# help(math)  # shows documentation (uncomment to use)

# -----------------------------------------
# 5. reload() a module
# -----------------------------------------
# If you modify a module during runtime, use:
# from importlib import reload
# reload(mymodule)

# -----------------------------------------
# Summary:
# - Modules: single `.py` files to organize functions/variables.
# - Packages: folders with `__init__.py`, can contain multiple modules.
# - Use `import`, `from ... import`, and aliases to use them.
# -----------------------------------------
