import logging

# -----------------------------------------
# 1. Logger for General App Logs
# -----------------------------------------
app_logger = logging.getLogger("app_logger")
app_logger.setLevel(logging.INFO)

# File handler for app logs
app_handler = logging.FileHandler("logs/app.log", mode='w')
app_format = logging.Formatter('%(asctime)s - APP - %(levelname)s - %(message)s')
app_handler.setFormatter(app_format)

app_logger.addHandler(app_handler)


# -----------------------------------------
# 2. Logger for Error Logs
# -----------------------------------------
error_logger = logging.getLogger("error_logger")
error_logger.setLevel(logging.ERROR)

# File handler for error logs
error_handler = logging.FileHandler("logs/errors.log", mode='w')
error_format = logging.Formatter('%(asctime)s - ERROR - %(levelname)s - %(message)s')
error_handler.setFormatter(error_format)

error_logger.addHandler(error_handler)


# -----------------------------------------
# 3. Logger for Audit Logs
# -----------------------------------------
audit_logger = logging.getLogger("audit_logger")
audit_logger.setLevel(logging.DEBUG)

# File handler for audit logs
audit_handler = logging.FileHandler("logs/audit.log", mode='w')
audit_format = logging.Formatter('%(asctime)s - AUDIT - %(message)s')
audit_handler.setFormatter(audit_format)

audit_logger.addHandler(audit_handler)


# -----------------------------------------
# 4. Example Usage of All Loggers
# -----------------------------------------
app_logger.info("Application started.")
audit_logger.debug("User logged in: user_id=123")
audit_logger.debug("User updated profile: user_id=123")

try:
    result = 10 / 0
except ZeroDivisionError as e:
    error_logger.error("Division by zero error occurred", exc_info=True)

app_logger.info("Application ended.")

# -----------------------------------------
# 5. Summary:
# - app_logger → logs general info to app.log
# - error_logger → logs only errors to errors.log
# - audit_logger → logs debug-level audit trails to audit.log
# -----------------------------------------