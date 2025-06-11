# -----------------------------------------
# What is a Variable?
# -----------------------------------------
# A variable is a named location used to store data in memory.

# Syntax:
# variable_name = value

# Example:
x = 10         # Integer
name = "Alice" # String
pi = 3.14      # Float
is_valid = True  # Boolean

# -----------------------------------------
# Dynamic Typing
# -----------------------------------------
# In Python, you don't need to specify the type of variable.
# Python automatically infers the type based on the value assigned.

a = 100      # Now 'a' is an integer
a = "hello"  # Now 'a' becomes a string

# -----------------------------------------
# Variable Naming Rules
# -----------------------------------------
# - Must start with a letter or underscore
# - Cannot start with a number
# - Can contain letters, numbers, and underscores
# - Case-sensitive

# Valid names:
user_name = "Bob"
_user1 = "Tom"
user1 = "Jerry"

# Invalid names (will raise SyntaxError if used):
# 1user = "Error"
# user-name = "Error"

# -----------------------------------------
# Constants (by convention)
# -----------------------------------------
# Python doesn't have true constants, but by convention, 
# we use uppercase variable names for values that shouldn't change.

PI = 3.14159
MAX_USERS = 100

# -----------------------------------------
# Multiple Assignments
# -----------------------------------------
x, y, z = 1, 2, 3
print(x, y, z)

# Assigning the same value to multiple variables
a = b = c = 0
print(a, b, c)

# -----------------------------------------
# Type Checking
# -----------------------------------------
print(type(x))      # <class 'int'>
print(type(name))   # <class 'str'>
print(type(pi))     # <class 'float'>
print(type(is_valid))  # <class 'bool'>

# -----------------------------------------
# Summary:
# - Variables store data
# - No need to declare data types
# - Follows naming rules
# - Python uses dynamic typing
# -----------------------------------------
