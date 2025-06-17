import logging
import os

# -----------------------------------------
# 1. Set up Logging Configuration
# -----------------------------------------

# Ensure logs folder exists
os.makedirs("logs", exist_ok=True)

# Basic configuration
logging.basicConfig(
    filename='logs/app.log',              # Log file location
    level=logging.DEBUG,                  # Minimum level to log
    format='%(asctime)s - %(levelname)s - %(message)s',  # Format
    filemode='w'                          # Overwrite log on each run (use 'a' for append)
)

# -----------------------------------------
# 2. Logging at Different Levels
# -----------------------------------------
logging.debug("This is a DEBUG message (for troubleshooting)")
logging.info("This is an INFO message (general info)")
logging.warning("This is a WARNING message (non-critical issue)")
logging.error("This is an ERROR message (serious problem)")
logging.critical("This is a CRITICAL message (system may crash)")

# -----------------------------------------
# 3. Function with Logging
# -----------------------------------------
def divide(a, b):
    logging.info(f"Dividing {a} by {b}")
    try:
        result = a / b
        logging.debug(f"Result is {result}")
        return result
    except ZeroDivisionError as e:
        logging.exception("Tried to divide by zero")
        return None

divide(10, 2)
divide(5, 0)

# -----------------------------------------
# 4. Logging in a Class
# -----------------------------------------
class Calculator:
    def __init__(self):
        logging.info("Calculator initialized")

    def multiply(self, x, y):
        logging.info(f"Multiplying {x} * {y}")
        return x * y

calc = Calculator()
result = calc.multiply(3, 4)
logging.debug(f"Multiplication result: {result}")

# -----------------------------------------
# 5. Print log file content to verify
# -----------------------------------------
print("\n--- Log File Content ---")
with open("logs/app.log", "r") as f:
    print(f.read())

# -----------------------------------------
# Summary:
# - Use `basicConfig()` to configure log file, level, and format.
# - Use `logging.debug/info/warning/error/critical` based on severity.
# - Use `logging.exception()` in except blocks to include stack trace.
# - Log within functions and classes for better traceability.
# -----------------------------------------
