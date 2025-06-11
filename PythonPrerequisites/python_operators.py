# -----------------------------------------
# 1. Arithmetic Operators
# -----------------------------------------
a = 10
b = 3

print("Addition:", a + b)        # 13
print("Subtraction:", a - b)     # 7
print("Multiplication:", a * b)  # 30
print("Division:", a / b)        # 3.333...
print("Floor Division:", a // b) # 3
print("Modulus:", a % b)         # 1
print("Exponent:", a ** b)       # 1000


# -----------------------------------------
# 2. Comparison Operators
# -----------------------------------------
x = 5
y = 10

print("x == y:", x == y)   # False
print("x != y:", x != y)   # True
print("x > y:", x > y)     # False
print("x < y:", x < y)     # True
print("x >= y:", x >= y)   # False
print("x <= y:", x <= y)   # True


# -----------------------------------------
# 3. Assignment Operators
# -----------------------------------------
num = 5
num += 3   # Same as num = num + 3
print("After +=:", num)   # 8

num *= 2   # 8 * 2 = 16
print("After *=:", num)   # 16

num -= 4   # 16 - 4 = 12
print("After -=:", num)   # 12

num /= 3   # 12 / 3 = 4.0
print("After /=:", num)   # 4.0


# -----------------------------------------
# 4. Logical Operators
# -----------------------------------------
a = True
b = False

print("AND:", a and b)   # False
print("OR:", a or b)     # True
print("NOT a:", not a)   # False


# -----------------------------------------
# 5. Identity Operators
# -----------------------------------------
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print("x is y:", x is y)     # True (same object)
print("x is z:", x is z)     # False (different objects with same content)
print("x == z:", x == z)     # True (values are equal)


# -----------------------------------------
# 6. Membership Operators
# -----------------------------------------
colors = ['red', 'green', 'blue']
print("'red' in colors:", 'red' in colors)     # True
print("'yellow' not in colors:", 'yellow' not in colors)  # True


# -----------------------------------------
# 7. Bitwise Operators (Advanced)
# -----------------------------------------
x = 5       # 0101 in binary
y = 3       # 0011 in binary

print("x & y:", x & y)   # 1 (0001)
print("x | y:", x | y)   # 7 (0111)
print("x ^ y:", x ^ y)   # 6 (0110)
print("~x:", ~x)         # -6 (inverts all bits)
print("x << 1:", x << 1) # 10 (shifts bits left)
print("x >> 1:", x >> 1) # 2  (shifts bits right)


# -----------------------------------------
# Summary:
# Types of Operators:
# 1. Arithmetic
# 2. Comparison
# 3. Assignment
# 4. Logical
# 5. Identity
# 6. Membership
# 7. Bitwise
# -----------------------------------------
