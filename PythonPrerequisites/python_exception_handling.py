# -----------------------------------------
# 1. Basic try-except block
# -----------------------------------------
try:
    x = 10 / 0  # This will raise ZeroDivisionError
except ZeroDivisionError:
    print("You cannot divide by zero!")

# -----------------------------------------
# 2. Catching multiple exceptions
# -----------------------------------------
try:
    a = int("abc")  # Will raise ValueError
    b = 10 / 0      # Would raise ZeroDivisionError
except ValueError:
    print("Invalid conversion to integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

# -----------------------------------------
# 3. Using else block
# -----------------------------------------
try:
    num = int("5")
except ValueError:
    print("Invalid number!")
else:
    print("Conversion successful, number:", num)

# -----------------------------------------
# 4. finally block (always executes)
# -----------------------------------------
try:
    f = open("example.txt", "r")
    data = f.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("This will always run (cleanup, logging, etc.)")

# -----------------------------------------
# 5. Catching all exceptions (not recommended unless necessary)
# -----------------------------------------
try:
    # risky code
    result = 100 / int("0")
except Exception as e:
    print("An error occurred:", e)

# -----------------------------------------
# 6. Raising Custom Exceptions
# -----------------------------------------
def divide(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b

try:
    print(divide(5, 0))
except ValueError as ve:
    print("Custom Exception:", ve)

# -----------------------------------------
# 7. Creating Your Own Exception Class
# -----------------------------------------
class AgeTooSmallError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise AgeTooSmallError("Age is below 18!")

try:
    check_age(15)
except AgeTooSmallError as e:
    print("Custom class exception:", e)

# -----------------------------------------
# Summary:
# - Use try-except to catch runtime errors.
# - Use else for success logic, finally for cleanup.
# - You can raise or define custom exceptions.
# -----------------------------------------
