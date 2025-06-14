# -----------------------------------------
# 1. Polymorphism with Methods
# -----------------------------------------

class Cat:
    def sound(self):
        return "Meow"

class Dog:
    def sound(self):
        return "Woof"

# A common interface
def make_sound(animal):
    print(animal.sound())

# Different objects respond differently to the same method
cat = Cat()
dog = Dog()

make_sound(cat)  # Output: Meow
make_sound(dog)  # Output: Woof

# -----------------------------------------
# 2. Polymorphism with Inheritance
# -----------------------------------------

class Animal:
    def speak(self):
        print("Animal speaks")

class Cow(Animal):
    def speak(self):
        print("Cow says Moo")

class Sheep(Animal):
    def speak(self):
        print("Sheep says Baa")

# List of animals
animals = [Cow(), Sheep(), Animal()]

for animal in animals:
    animal.speak()  # Each object calls its own version of speak()

# -----------------------------------------
# 3. Built-in Polymorphism Example
# -----------------------------------------
print(len("Python"))      # Output: 6 (string length)
print(len([1, 2, 3, 4]))   # Output: 4 (list length)
print(len({"a": 1}))       # Output: 1 (dict keys count)

# -----------------------------------------
# 4. Duck Typing (Pythonic Polymorphism)
# -----------------------------------------
# If it walks like a duck and quacks like a duck, it’s a duck

class Duck:
    def walk(self):
        print("Duck walks like a duck")

class Robot:
    def walk(self):
        print("Robot walks like a duck")

def start_walking(entity):
    entity.walk()  # Doesn't care about the class, only the method presence

duck = Duck()
robot = Robot()

start_walking(duck)
start_walking(robot)

# -----------------------------------------
# Summary:
# - Polymorphism allows the same method name to behave differently.
# - Python supports polymorphism via method overriding and duck typing.
# - `len()` is an example of built-in polymorphism.
# -----------------------------------------
