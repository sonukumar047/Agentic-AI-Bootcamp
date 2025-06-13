# -----------------------------------------
# 1. Creating a Dictionary
# -----------------------------------------
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print("Person:", person)

# Empty dictionary
empty_dict = {}

# Using dict() constructor
car = dict(brand="Toyota", model="Camry", year=2023)
print("Car:", car)

# -----------------------------------------
# 2. Accessing Values
# -----------------------------------------
print("Name:", person["name"])     # Alice
print("City:", person.get("city")) # New York

# Using get() avoids error if key doesn't exist
print("Country:", person.get("country", "Not Available"))

# -----------------------------------------
# 3. Modifying Dictionary
# -----------------------------------------
person["age"] = 26              # Update existing key
person["country"] = "USA"       # Add new key-value pair
print("Updated person:", person)

# -----------------------------------------
# 4. Removing Items
# -----------------------------------------
person.pop("city")             # Removes 'city'
del person["name"]             # Removes 'name'
print("After removal:", person)

# person.clear()               # Clears all items
# print("Cleared:", person)

# -----------------------------------------
# 5. Looping Through Dictionary
# -----------------------------------------
student = {"name": "John", "marks": 85, "grade": "B"}

# Keys
for key in student:
    print("Key:", key)

# Values
for value in student.values():
    print("Value:", value)

# Key-Value pairs
for key, value in student.items():
    print(f"{key}: {value}")

# -----------------------------------------
# 6. Dictionary Methods
# -----------------------------------------
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# Copying dictionary
new_student = student.copy()
print("Copied:", new_student)

# Merge two dictionaries
extra = {"section": "A", "passed": True}
student.update(extra)
print("After update:", student)

# -----------------------------------------
# 7. Nested Dictionaries
# -----------------------------------------
contacts = {
    "person1": {"name": "Alice", "phone": "1234"},
    "person2": {"name": "Bob", "phone": "5678"}
}
print("Nested name:", contacts["person1"]["name"])  # Alice

# -----------------------------------------
# Summary:
# - Dictionaries store key-value pairs.
# - Keys must be unique and immutable.
# - Supports modification, deletion, and nesting.
# -----------------------------------------
