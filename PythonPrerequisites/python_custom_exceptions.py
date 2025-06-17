# -----------------------------------------
# 1. Creating a Basic Custom Exception
# -----------------------------------------

class MyCustomError(Exception):
    """Custom Exception for general purpose"""
    pass

def do_something(x):
    if x < 0:
        raise MyCustomError("Negative value is not allowed!")

try:
    do_something(-5)
except MyCustomError as e:
    print("Caught custom exception:", e)

# -----------------------------------------
# 2. Custom Exception with Constructor
# -----------------------------------------

class AgeTooSmallError(Exception):
    def __init__(self, age, message="Age must be at least 18"):
        self.age = age
        self.message = message
        super().__init__(self.message)

def verify_age(age):
    if age < 18:
        raise AgeTooSmallError(age)
    else:
        print("Age is valid.")

try:
    verify_age(16)
except AgeTooSmallError as e:
    print(f"Custom Error: {e} (Provided: {e.age})")

# -----------------------------------------
# 3. Multiple Custom Exceptions
# -----------------------------------------

class LowBalanceError(Exception):
    pass

class ExceedLimitError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise LowBalanceError("Insufficient balance!")
    elif amount > 10000:
        raise ExceedLimitError("Withdrawal limit exceeded!")
    else:
        print(f"Withdrawn: ₹{amount}")

try:
    withdraw(5000, 15000)
except LowBalanceError as e:
    print("LowBalanceError:", e)
except ExceedLimitError as e:
    print("ExceedLimitError:", e)

# -----------------------------------------
# 4. Custom Exceptions with `__str__()`
# -----------------------------------------

class InvalidPasswordError(Exception):
    def __init__(self, password):
        self.password = password

    def __str__(self):
        return f"'{self.password}' is an invalid password!"

try:
    raise InvalidPasswordError("123")
except InvalidPasswordError as e:
    print("Error:", e)

# -----------------------------------------
# Summary:
# - Create custom exceptions by subclassing `Exception`.
# - Use `__init__()` for custom messages or arguments.
# - Use `__str__()` to define how your exception appears.
# - Helpful for domain-specific error handling.
# -----------------------------------------
