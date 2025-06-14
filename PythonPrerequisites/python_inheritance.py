# -----------------------------------------
# 1. Basic Inheritance
# -----------------------------------------
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Dog inherits from Animal
class Dog(Animal):
    def bark(self):
        print(f"{self.name} says Woof!")

# Creating object of subclass
dog1 = Dog("Buddy")
dog1.speak()   # Inherited method
dog1.bark()    # Subclass method

# -----------------------------------------
# 2. Method Overriding
# -----------------------------------------
class Cat(Animal):
    def speak(self):  # Overrides Animal's speak method
        print(f"{self.name} says Meow!")

cat1 = Cat("Whiskers")
cat1.speak()  # Will use Cat's version of speak()

# -----------------------------------------
# 3. Using super() to Call Parent Methods
# -----------------------------------------
class Bird(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # Call parent constructor
        self.color = color

    def speak(self):
        super().speak()  # Call parent method
        print(f"{self.name} tweets and is {self.color}.")

bird1 = Bird("Tweety", "Yellow")
bird1.speak()

# -----------------------------------------
# 4. Multi-level Inheritance
# -----------------------------------------
class Vehicle:
    def drive(self):
        print("Driving a vehicle")

class Car(Vehicle):
    def fuel(self):
        print("Car uses petrol or diesel")

class ElectricCar(Car):
    def fuel(self):
        print("Electric car uses battery")

tesla = ElectricCar()
tesla.drive()  # Inherited from Vehicle
tesla.fuel()   # Overridden in ElectricCar

# -----------------------------------------
# 5. Multiple Inheritance
# -----------------------------------------
class Father:
    def skills(self):
        print("Father: gardening, carpentry")

class Mother:
    def skills(self):
        print("Mother: cooking, painting")

class Child(Father, Mother):
    def skills(self):
        print("Child:", end=" ")
        Father.skills(self)
        Mother.skills(self)

child = Child()
child.skills()

# -----------------------------------------
# Summary:
# - Inheritance enables code reuse and hierarchy modeling.
# - Use `super()` to call parent class methods.
# - Python supports single, multi-level, and multiple inheritance.
# -----------------------------------------
