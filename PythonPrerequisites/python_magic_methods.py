# -----------------------------------------
# 1. __init__() → Constructor
# -----------------------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 30)
print(p.name, p.age)

# -----------------------------------------
# 2. __str__() → Custom string representation
# -----------------------------------------
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

b = Book("Python 101", "John Doe")
print(b)  # Calls __str__

# -----------------------------------------
# 3. __len__() → Called by len()
# -----------------------------------------
class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

pl = Playlist(["Song A", "Song B", "Song C"])
print("Total songs:", len(pl))

# -----------------------------------------
# 4. __add__() → Operator overloading for +
# -----------------------------------------
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(4, 1)
result = p1 + p2  # Calls __add__
print(result)

# -----------------------------------------
# 5. __eq__(), __lt__(), __gt__() → Comparisons
# -----------------------------------------
class Product:
    def __init__(self, price):
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price

item1 = Product(100)
item2 = Product(150)

print("Equal:", item1 == item2)
print("Less than:", item1 < item2)
print("Greater than:", item1 > item2)

# -----------------------------------------
# 6. __getitem__() and __setitem__() → Index access
# -----------------------------------------
class MyList:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

ml = MyList([10, 20, 30])
print(ml[1])  # Calls __getitem__
ml[1] = 99    # Calls __setitem__
print(ml[1])

# -----------------------------------------
# Summary:
# - Magic methods control built-in operations on custom classes.
# - Common ones: `__init__`, `__str__`, `__add__`, `__len__`, `__eq__`, `__getitem__`
# - Enable powerful, Pythonic behavior for your objects.
# -----------------------------------------
