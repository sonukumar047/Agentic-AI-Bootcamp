# -----------------------------------------
# 1. Basic Generator Function
# -----------------------------------------
def number_generator():
    yield 1
    yield 2
    yield 3

gen = number_generator()

print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
# print(next(gen))  # ❌ StopIteration

# -----------------------------------------
# 2. Generator with Loop
# -----------------------------------------
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for num in count_up_to(5):
    print(num)

# Output: 1 2 3 4 5

# -----------------------------------------
# 3. Generator Expression (like list comprehension)
# -----------------------------------------
squares = (x * x for x in range(5))
for val in squares:
    print(val)

# -----------------------------------------
# 4. Comparing Generator vs List (Memory Efficient)
# -----------------------------------------
import sys

def gen_nums():
    for i in range(1000):
        yield i

nums_list = [i for i in range(1000)]

print("List size in bytes:", sys.getsizeof(nums_list))
print("Generator size in bytes:", sys.getsizeof(gen_nums()))

# -----------------------------------------
# 5. Generator with `send()` and `yield` as expression
# -----------------------------------------
def echo():
    while True:
        value = yield
        print("Received:", value)

e = echo()
next(e)  # Prime the generator
e.send("Hello")
e.send("World")

# -----------------------------------------
# Summary:
# - Use `yield` instead of `return` to create generators.
# - Generators produce items lazily (on-demand).
# - More memory efficient than lists for large sequences.
# - Generator expressions use `()` instead of `[]`.
# -----------------------------------------
