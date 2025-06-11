# -----------------------------------------
# 1. Basic if Statement
# -----------------------------------------
age = 18

if age >= 18:
    print("You are eligible to vote.")  # This will run

# -----------------------------------------
# 2. if-else Statement
# -----------------------------------------
marks = 45

if marks >= 50:
    print("You passed the exam.")
else:
    print("You failed the exam.")  # This will run


# -----------------------------------------
# 3. if-elif-else Ladder
# -----------------------------------------
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")  # This will run
elif score >= 60:
    print("Grade: C")
else:
    print("Grade: F")


# -----------------------------------------
# 4. Nested if
# -----------------------------------------
x = 10
y = 20

if x < y:
    if x > 5:
        print("x is less than y and greater than 5")  # This will run


# -----------------------------------------
# 5. One-Line if and if-else (Ternary Operator)
# -----------------------------------------
is_logged_in = True
print("Welcome!") if is_logged_in else print("Please log in.")  # One-liner

# -----------------------------------------
# 6. Using Logical Operators in Conditions
# -----------------------------------------
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful!")  # This will run


# -----------------------------------------
# 7. Comparison Inside Conditions
# -----------------------------------------
a = 10
b = 5

if a != b:
    print("a is not equal to b")  # This will run


# -----------------------------------------
# Summary:
# - if, elif, else are used to control program flow based on conditions.
# - You can use logical and comparison operators in conditions.
# - Nested and one-liner if-statements are also supported.
# -----------------------------------------
