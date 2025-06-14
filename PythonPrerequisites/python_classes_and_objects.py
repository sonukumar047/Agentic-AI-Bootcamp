# -----------------------------------------
# 1. Creating a Class and Object
# -----------------------------------------
class Person:
    # Constructor / initializer
    def __init__(self, name, age):
        self.name = name    # instance variable
        self.age = age

    # Method
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating objects (instances)
p1 = Person("Alice", 30)
p2 = Person("Bob", 25)

# Calling method
p1.greet()
p2.greet()

# -----------------------------------------
# 2. Class with Default Values
# -----------------------------------------
class Dog:
    species = "Canis Familiaris"  # class variable (shared by all)

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof!")

# Create instances
d1 = Dog("Buddy", "Golden Retriever")
d2 = Dog("Max", "Bulldog")

print(d1.name, "-", d1.species)
print(d2.name, "-", d2.species)

d1.bark()

# -----------------------------------------
# 3. Class vs Instance Variables
# -----------------------------------------
class Car:
    wheels = 4  # class variable

    def __init__(self, brand):
        self.brand = brand  # instance variable

car1 = Car("Toyota")
car2 = Car("Honda")

print(car1.brand, "-", car1.wheels)
print(car2.brand, "-", car2.wheels)

# Changing class variable
Car.wheels = 6
print("After modification:", car1.wheels, car2.wheels)

# -----------------------------------------
# 4. Accessing and Modifying Attributes
# -----------------------------------------
car1.color = "Red"  # dynamically adding attribute
print("Car1 color:", car1.color)

# -----------------------------------------
# 5. Deleting Attributes and Objects
# -----------------------------------------
del car1.color        # delete an attribute
del car2              # delete an object

# -----------------------------------------
# Summary:
# - Use `class` keyword to define a class.
# - Use `__init__` for constructor to initialize attributes.
# - Use `self` to refer to instance-specific data.
# - Objects are created by calling the class like a function.
# -----------------------------------------
