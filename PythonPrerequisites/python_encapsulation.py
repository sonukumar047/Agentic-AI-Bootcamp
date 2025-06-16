# -----------------------------------------
# 1. Basic Encapsulation
# -----------------------------------------
class Person:
    def __init__(self, name, age):
        self.name = name       # public attribute
        self._age = age        # protected attribute (convention)
        self.__ssn = "123-45"  # private attribute (name mangling)

    def get_ssn(self):         # public getter
        return self.__ssn

    def set_ssn(self, new_ssn):  # public setter
        if isinstance(new_ssn, str):
            self.__ssn = new_ssn

# Creating object
p = Person("Alice", 30)

# Accessing public
print("Name:", p.name)

# Accessing protected (convention: avoid direct use)
print("Age (protected):", p._age)

# Accessing private directly will raise error
# print(p.__ssn)  # ❌ AttributeError

# Correct way: use getter/setter
print("SSN (private via getter):", p.get_ssn())
p.set_ssn("987-65")
print("Updated SSN:", p.get_ssn())

# -----------------------------------------
# 2. Name Mangling for Private Variables
# -----------------------------------------
# You can still access private variables like this (not recommended)
print("Access private manually:", p._Person__ssn)

# -----------------------------------------
# 3. Setter/Getter with Property Decorators
# -----------------------------------------
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private

    @property
    def balance(self):     # Getter
        return self.__balance

    @balance.setter
    def balance(self, amount):  # Setter
        if amount >= 0:
            self.__balance = amount

acc = BankAccount(1000)
print("Balance:", acc.balance)

acc.balance = 1500  # using setter
print("Updated Balance:", acc.balance)

# acc.balance = -200  # won't update due to check
# print(acc.balance)

# -----------------------------------------
# Summary:
# - `_var` = protected (convention only)
# - `__var` = private (name mangling)
# - Use getter/setter methods or `@property` for controlled access
# -----------------------------------------
