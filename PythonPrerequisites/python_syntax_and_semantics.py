# -----------------------------------------
# Python Syntax (Structure/Rules)
# -----------------------------------------

# 1. Proper indentation is required in Python (usually 4 spaces)
# Incorrect indentation leads to a SyntaxError
def say_hello():
    print("Hello, world!")  # This line is indented, part of the function

# 2. Colons are used to define blocks (like functions, if statements, loops)
if True:
    print("This block will run.")  # Syntax requires colon and indentation

# 3. Statements do not need semicolons (optional)
x = 5
y = 10
print(x + y)  # You can write: print(x + y); but it's not required


# -----------------------------------------
# Python Semantics (Meaning of code)
# -----------------------------------------

# The following code is syntactically correct but may not be semantically correct.

# Example 1: Division by zero (Semantic Error)
# z = 10 / 0  # This will crash the program (ZeroDivisionError)

# Example 2: Using an undefined variable
# print(a)  # NameError because 'a' is not defined

# Example 3: Correct syntax and semantics
name = "Alice"
age = 30
print(name + " is " + str(age) + " years old.")  # Works fine

# -----------------------------------------
# Summary:
# Syntax → Structure of code (rules, like indentation)
# Semantics → Meaning of code (what it does)
# -----------------------------------------
