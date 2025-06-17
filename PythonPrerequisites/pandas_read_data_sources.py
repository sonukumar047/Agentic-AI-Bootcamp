import pandas as pd
import sqlite3

# -----------------------------------------
# 1. Read CSV File
# -----------------------------------------
# Make sure 'data.csv' exists in the same directory.
csv_df = pd.read_csv('data.csv')
print("CSV Data:\n", csv_df.head())

# -----------------------------------------
# 2. Read Excel File
# -----------------------------------------
# Requires: pip install openpyxl
excel_df = pd.read_excel('data.xlsx', sheet_name=0)
print("\nExcel Data:\n", excel_df.head())


# # create_data_excel.py

# # Create sample data
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
#     'Age': [25, 30, 35, 40, 28],
#     'Department': ['HR', 'IT', 'HR', 'Finance', 'IT'],
#     'Salary': [50000, 60000, 70000, 80000, 55000]
# }

# df = pd.DataFrame(data)

# # Write to Excel file
# df.to_excel('data.xlsx', index=False)

# print("data.xlsx created successfully!")

# -----------------------------------------
# 3. Read JSON File
# -----------------------------------------
# JSON should be an array of objects
json_df = pd.read_json('data.json')
print("\nJSON Data:\n", json_df.head())

# -----------------------------------------
# 4. Read from SQL Database
# -----------------------------------------
# Using SQLite for demonstration
conn = sqlite3.connect('my_database.db')
sql_df = pd.read_sql_query("SELECT * FROM employees", conn)
print("\nSQL Data:\n", sql_df.head())
conn.close()

# create_my_database.py

# import sqlite3

# # Connect to SQLite DB (creates file if not exists)
# conn = sqlite3.connect('my_database.db')
# cursor = conn.cursor()

# # Create a table named 'employees'
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS employees (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT,
#     age INTEGER,
#     department TEXT,
#     salary REAL
# )
# """)

# # Insert sample records
# sample_data = [
#     ('Alice', 25, 'HR', 50000),
#     ('Bob', 30, 'IT', 60000),
#     ('Charlie', 35, 'HR', 70000),
#     ('David', 40, 'Finance', 80000),
#     ('Eve', 28, 'IT', 55000)
# ]

# cursor.executemany("INSERT INTO employees (name, age, department, salary) VALUES (?, ?, ?, ?)", sample_data)

# # Commit and close
# conn.commit()
# conn.close()

# print("my_database.db created with 'employees' table.")


# -----------------------------------------
# 5. Read HTML Tables from Website
# -----------------------------------------
# Requires: pip install lxml
url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'
html_tables = pd.read_html(url)
print("\nFirst Table from HTML:\n", html_tables[0].head())

# -----------------------------------------
# 6. Read Data from Clipboard (e.g., from Excel)
# -----------------------------------------
# Copy a table and run this
# clipboard_df = pd.read_clipboard()
# print("\nClipboard Data:\n", clipboard_df.head())

# -----------------------------------------
# 7. BONUS: Read Google Sheets using URL (Public only)
# -----------------------------------------
# This is a public CSV export link of a Google Sheet
# Replace with your own link
google_sheet_url = 'https://docs.google.com/spreadsheets/d/<SHEET_ID>/export?format=csv'
# gsheet_df = pd.read_csv(google_sheet_url)
# print("\nGoogle Sheet Data:\n", gsheet_df.head())

# -----------------------------------------
# Summary:
# - Use `read_csv()`, `read_excel()`, `read_json()` for local files.
# - Use `read_sql_query()` for databases (needs a connection).
# - Use `read_html()` for scraping tables from web pages.
# - `read_clipboard()` for quick Excel/Web copy-paste.
# - Google Sheets can be read using shared public CSV links.
# -----------------------------------------
