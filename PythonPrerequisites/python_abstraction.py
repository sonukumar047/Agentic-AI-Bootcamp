from abc import ABC, abstractmethod

# -----------------------------------------
# 1. Creating an Abstract Base Class
# -----------------------------------------

class Animal(ABC):  # Inherit from ABC to create abstract class

    @abstractmethod
    def sound(self):
        pass  # Abstract method (must be overridden)

    def eat(self):
        print("This animal eats food.")  # Concrete method

# -----------------------------------------
# 2. Implementing the Abstract Class
# -----------------------------------------

class Dog(Animal):
    def sound(self):
        print("Dog says Woof!")

class Cat(Animal):
    def sound(self):
        print("Cat says Meow!")

# animal = Animal()  # ❌ Error: Can't instantiate abstract class

dog = Dog()
cat = Cat()

dog.sound()
dog.eat()

cat.sound()
cat.eat()

# -----------------------------------------
# 3. Abstract Class with Multiple Abstract Methods
# -----------------------------------------

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starting...")

    def stop(self):
        print("Car stopping...")

car = Car()
car.start()
car.stop()

# -----------------------------------------
# Summary:
# - Abstract class = blueprint for subclasses
# - Use `@abstractmethod` to define required methods
# - Subclasses must implement all abstract methods
# - Use `abc.ABC` as base class
# -----------------------------------------
