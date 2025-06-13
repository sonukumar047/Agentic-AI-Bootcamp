# -----------------------------------------
# 1. math – mathematical functions
# -----------------------------------------
import math

print("Square root of 25:", math.sqrt(25))
print("Ceiling of 2.3:", math.ceil(2.3))
print("Pi value:", math.pi)

# -----------------------------------------
# 2. datetime – date and time
# -----------------------------------------
import datetime

now = datetime.datetime.now()
print("Current Date & Time:", now)
print("Year:", now.year)
print("Formatted:", now.strftime("%d-%m-%Y %H:%M:%S"))

# -----------------------------------------
# 3. random – random numbers and choices
# -----------------------------------------
import random

print("Random integer (1–10):", random.randint(1, 10))
print("Random choice from list:", random.choice(['apple', 'banana', 'cherry']))

# -----------------------------------------
# 4. os – interacting with the operating system
# -----------------------------------------
import os

print("Current Working Directory:", os.getcwd())
print("List of files:", os.listdir('.'))

# -----------------------------------------
# 5. sys – system-specific parameters and functions
# -----------------------------------------
import sys

print("Python version:", sys.version)
print("Script name:", sys.argv[0])  # script name if run from terminal

# -----------------------------------------
# 6. json – working with JSON data
# -----------------------------------------
import json

data = {"name": "Alice", "age": 30}
json_str = json.dumps(data)
print("JSON string:", json_str)

parsed = json.loads(json_str)
print("Parsed JSON:", parsed)

# -----------------------------------------
# 7. re – regular expressions
# -----------------------------------------
import re

pattern = r"\d+"
text = "There are 123 apples"
match = re.findall(pattern, text)
print("Digits found:", match)

# -----------------------------------------
# 8. statistics – statistical operations
# -----------------------------------------
import statistics

nums = [1, 2, 3, 4, 5]
print("Mean:", statistics.mean(nums))
print("Median:", statistics.median(nums))

# -----------------------------------------
# 9. collections – advanced data types
# -----------------------------------------
from collections import Counter

fruits = ['apple', 'banana', 'apple', 'orange', 'banana']
count = Counter(fruits)
print("Fruit count:", count)

# -----------------------------------------
# 10. time – sleep, delays, timestamps
# -----------------------------------------
import time

print("Sleeping for 2 seconds...")
time.sleep(2)
print("Awake now!")

# -----------------------------------------
# Summary:
# - Python’s Standard Library saves time by providing ready-made solutions.
# - You’ve explored: math, datetime, random, os, sys, json, re, statistics, collections, time.
# -----------------------------------------
