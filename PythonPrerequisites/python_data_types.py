# -----------------------------------------
# Python Built-in Data Types (Core Ones)
# -----------------------------------------

# 1. Numeric Types
integer_num = 10           # int
floating_num = 3.14        # float
complex_num = 1 + 2j       # complex

print(type(integer_num))   # <class 'int'>
print(type(floating_num))  # <class 'float'>
print(type(complex_num))   # <class 'complex'>


# 2. Text Type
text = "Hello, Python!"    # str
print(type(text))          # <class 'str'>


# 3. Boolean Type
is_active = True
is_closed = False
print(type(is_active))     # <class 'bool'>


# 4. Sequence Types
my_list = [1, 2, 3, 4]     # list (mutable)
my_tuple = (1, 2, 3, 4)    # tuple (immutable)
my_range = range(5)        # range object

print(type(my_list))       # <class 'list'>
print(type(my_tuple))      # <class 'tuple'>
print(type(my_range))      # <class 'range'>


# 5. Set Types
my_set = {1, 2, 3, 3, 4}   # set (unique items, unordered)
print(my_set)              # Output: {1, 2, 3, 4}
print(type(my_set))        # <class 'set'>


# 6. Mapping Type
my_dict = {"name": "Alice", "age": 25}  # dict
print(type(my_dict))       # <class 'dict'>


# 7. None Type
no_value = None
print(type(no_value))      # <class 'NoneType'>


# -----------------------------------------
# Type Conversion (Casting)
# -----------------------------------------

a = "123"
b = int(a)    # Convert str to int
print(b, type(b))  # 123 <class 'int'>

x = 3.75
y = str(x)    # Convert float to string
print(y, type(y))  # "3.75" <class 'str'>


# -----------------------------------------
# Type Checking (again)
# -----------------------------------------
print(isinstance(my_list, list))     # True
print(isinstance(text, str))         # True
print(isinstance(floating_num, int)) # False


# -----------------------------------------
# Summary:
# Common Python Data Types:
# - int, float, complex
# - str
# - bool
# - list, tuple, range
# - set, frozenset
# - dict
# - NoneType
# -----------------------------------------
