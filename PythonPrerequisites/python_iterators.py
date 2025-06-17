# -----------------------------------------
# 1. Built-in Iterator Example
# -----------------------------------------

nums = [10, 20, 30]

# Get iterator from iterable
it = iter(nums)

print(next(it))  # Output: 10
print(next(it))  # Output: 20
print(next(it))  # Output: 30

# print(next(it))  # ❌ Raises StopIteration

# -----------------------------------------
# 2. Custom Iterator using a Class
# -----------------------------------------

class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self  # returns the iterator object

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            num = self.current
            self.current += 1
            return num

counter = Counter(1, 5)

for num in counter:
    print(num)  # Output: 1 2 3 4 5

# -----------------------------------------
# 3. Custom Reverse Iterator
# -----------------------------------------

class ReverseList:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

rl = ReverseList(["a", "b", "c", "d"])

for ch in rl:
    print(ch)  # Output: d c b a

# -----------------------------------------
# 4. Using next() Safely with Default
# -----------------------------------------

nums = [100, 200]
it = iter(nums)
print(next(it, "Default"))  # 100
print(next(it, "Default"))  # 200
print(next(it, "Default"))  # Default

# -----------------------------------------
# Summary:
# - Iterators must implement `__iter__()` and `__next__()`.
# - Use `iter()` and `next()` for manual iteration.
# - Custom iterators help define specific iteration behavior.
# -----------------------------------------
