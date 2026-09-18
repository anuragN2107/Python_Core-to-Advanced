# ===============================================================================================================================
#                                           PYTHON INHERITANCE
# ===============================================================================================================================

# -------------------------------------------------------------------------------------------------------------------------------
# WHAT IS INHERITANCE? (CORE DEFINITION)
# -------------------------------------------------------------------------------------------------------------------------------
# Inheritance is a core Object-Oriented Programming (OOP) concept. It allows a new class (Child/Derived class) 
# to acquire the properties (attributes) and behaviors (methods) of an existing class (Parent/Base class).
#
# Key Benefits:
# 1. Code Reusability: Write common code once and reuse it across multiple classes.
# 2. Maintainability: Easily manage and update code from a single parent source.
# 3. Extensibility: Child classes can add new attributes/methods or override existing ones.
# -------------------------------------------------------------------------------------------------------------------------------


# ===============================================================================================================================
# PART 1: THE FIVE TYPES OF INHERITANCE 
# ===============================================================================================================================

# -------------------------------------------------------------------------------------------------------------------------------
# 1. SINGLE INHERITANCE
# -------------------------------------------------------------------------------------------------------------------------------
# Definition: A child class inherits from exactly one parent class.
#
# Syntax Template:
#   class Parent:
#       pass
#   class Child(Parent):
#       pass

print("=== 1. SINGLE INHERITANCE ===")

# Example A: Simple Single Inheritance (No Constructor)
print("--- [A] Simple Example ---")
class Animal:
    def eat(self):
        print("Animal is eating.")

class Dog(Animal):
    def bark(self):
        print("Dog is barking.")

d = Dog()
d.eat()   # Inherited
d.bark()  # Child's own

#Output: Animal is eating.
#      Dog is barking.

# Example B: Single Inheritance with Constructor (__init__ & self)
print("--- [B] Constructor Example ---")
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)  # Initializing parent attribute
        self.student_id = student_id

    def display(self):
        print(f"Student: {self.name}, ID: {self.student_id}")

s = Student("Alice", "S101")
s.display() # Output: Student: Alice, ID: S101
print()  # Output: Student: Alice, ID: S101


# -------------------------------------------------------------------------------------------------------------------------------
# 2. MULTIPLE INHERITANCE
# -------------------------------------------------------------------------------------------------------------------------------
# Definition: A single child class inherits from more than one parent class simultaneously.
#
# Syntax Template:
#   class Parent1:
#       pass
#   class Parent2:
#       pass
#   class Child(Parent1, Parent2):
#       pass

print("=== 2. MULTIPLE INHERITANCE ===")

# Example A: Simple Multiple Inheritance (No Constructor)
print("--- [A] Simple Example ---")
class Flyer:
    def fly(self):
        print("Flying in the sky.")

class Swimmer:
    def swim(self):
        print("Swimming in water.")

class Duck(Flyer, Swimmer):
    def quack(self):
        print("Duck says Quack!")

duck = Duck()
duck.fly() # Output: Flying in the sky.
duck.swim() # Output: Swimming in water.
duck.quack() # Output: Duck says Quack!

# Example B: Multiple Inheritance with Constructor (__init__ & self)
print("--- [B] Constructor Example ---")
class Father:
    def __init__(self, father_name):
        self.father_name = father_name

class Mother:
    def __init__(self, mother_name):
        self.mother_name = mother_name

class Child(Father, Mother):
    def __init__(self, child_name, father_name, mother_name):
        self.child_name = child_name
        Father.__init__(self, father_name)
        Mother.__init__(self, mother_name)

    def show_family(self):
        print(f"Child: {self.child_name}, Father: {self.father_name}, Mother: {self.mother_name}")

c = Child("Bob", "Robert", "Mary")
c.show_family() # Output: Child: Bob, Father: Robert, Mother: Mary
print()  # Output: Child: Bob, Father: Robert, Mother: Mary


# -------------------------------------------------------------------------------------------------------------------------------
# 3. MULTILEVEL INHERITANCE
# -------------------------------------------------------------------------------------------------------------------------------
# Definition: A class inherits from a derived class, creating a chain (Grandparent -> Parent -> Child).
#
# Syntax Template:
#   class Grandparent:
#       pass
#   class Parent(Grandparent):
#       pass
#   class Child(Parent):
#       pass

print("=== 3. MULTILEVEL INHERITANCE ===")

# Example A: Simple Multilevel Inheritance (No Constructor)
print("--- [A] Simple Example ---")
class Grandparent:
    def lineage(self):
        print("From Grandparent lineage.")

class Parent(Grandparent):
    def generation(self):
        print("From Parent generation.")

class GrandChild(Parent):
    def identity(self):
        print("I am the GrandChild.")

gc = GrandChild()
gc.lineage() # Output: From Grandparent lineage.
gc.generation() # Output: From Parent generation.
gc.identity() # Output: I am the GrandChild.

# Example B: Multilevel Inheritance with Constructor (__init__ & self)
print("--- [B] Constructor Example ---")
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, fuel_type):
        super().__init__(brand)
        self.fuel_type = fuel_type

class ElectricCar(Car):
    def __init__(self, brand, fuel_type, battery_capacity):
        super().__init__(brand, fuel_type)
        self.battery_capacity = battery_capacity

    def specs(self):
        print(f"Brand: {self.brand}, Fuel: {self.fuel_type}, Battery: {self.battery_capacity}kWh")

ec = ElectricCar("Tesla", "Electric", 100)
ec.specs() # Output: Brand: Tesla, Fuel: Electric, Battery: 100kWh
print()  # Output: Brand: Tesla, Fuel: Electric, Battery: 100kWh


# -------------------------------------------------------------------------------------------------------------------------------
# 4. HIERARCHICAL INHERITANCE
# -------------------------------------------------------------------------------------------------------------------------------
# Definition: Multiple child classes inherit from a single parent class.
#
# Syntax Template:
#   class Parent:
#       pass
#   class Child1(Parent):
#       pass
#   class Child2(Parent):
#       pass

print("=== 4. HIERARCHICAL INHERITANCE ===")

# Example A: Simple Hierarchical Inheritance (No Constructor)
print("--- [A] Simple Example ---")
class Shape:
    def render(self):
        print("Rendering generic shape.")

class Circle(Shape):
    def area_circle(self):
        print("Calculating circle area.")

class Rectangle(Shape):
    def area_rect(self):
        print("Calculating rectangle area.")

cir = Circle()
cir.render() # Output: Rendering generic shape.
cir.area_circle() # Output: Calculating circle area.

rec = Rectangle()
rec.render() # Output: Rendering generic shape.
rec.area_rect() # Output: Calculating rectangle area.

# Example B: Hierarchical Inheritance with Constructor (__init__ & self)
print("--- [B] Constructor Example ---")
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

class CheckingAccount(Account):
    def __init__(self, owner, balance, overdraft_limit):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

sav = SavingsAccount("Charlie", 5000, 4.5)
print(f"Savings Account Owner: {sav.owner}, Balance: {sav.balance}, Interest: {sav.interest_rate}%") # Output: Savings Account Owner: Charlie, Balance: 5000, Interest: 4.5%
print()  # Output: Savings Account Owner: Charlie, Balance: 5000, Interest: 4.5%


# -------------------------------------------------------------------------------------------------------------------------------
# 5. HYBRID INHERITANCE
# -------------------------------------------------------------------------------------------------------------------------------
# Definition: A combination of two or more types of inheritance (e.g., Multilevel + Multiple).
#
# Syntax Template:
#   class Base: pass
#   class Derived1(Base): pass
#   class Derived2(Base): pass
#   class HybridChild(Derived1, Derived2): pass

print("=== 5. HYBRID INHERITANCE ===")

# Example A: Simple Hybrid Inheritance (No Constructor)
print("--- [A] Simple Example ---")
class Device:
    def power_on(self):
        print("Device is powered on.")

class Phone(Device):
    def call(self):
        print("Calling from phone.")

class Camera(Device):
    def snap(self):
        print("Taking photo with camera.")

class SmartPhone(Phone, Camera):
    def smart_features(self):
        print("Running smart applications.")

sp = SmartPhone()
sp.power_on()       # From Device # Output: Device is powered on.
sp.call()           # From Phone # Output: Calling from phone.
sp.snap()           # From Camera # Output: Taking photo with camera.
sp.smart_features() # Own method # Output: Running smart applications.

# Example B: Hybrid Inheritance with Constructor (__init__ & self)
print("--- [B] Constructor Example ---")
class Machine:
    def __init__(self, machine_type):
        self.machine_type = machine_type

class Computer(Machine):
    def __init__(self, machine_type, os):
        super().__init__(machine_type)
        self.os = os

class DisplayUnit:
    def __init__(self, resolution):
        self.resolution = resolution

class SmartTerminal(Computer, DisplayUnit):
    def __init__(self, machine_type, os, resolution, touch_support):
        Computer.__init__(self, machine_type, os)
        DisplayUnit.__init__(self, resolution)
        self.touch_support = touch_support

    def display_specs(self):
        print(f"Type: {self.machine_type}, OS: {self.os}, Resolution: {self.resolution}, Touch: {self.touch_support}")

st = SmartTerminal("Terminal", "Linux", "4K", True)
st.display_specs() # Output: Type: Terminal, OS: Linux, Resolution: 4K, Touch: True
print()  # Output: Type: Terminal, OS: Linux, Resolution: 4K, Touch: True



# ===============================================================================================================================
# PART 2: MISCELLANEOUS EXAMPLE PAGE (Advanced Concepts)
# ===============================================================================================================================

print("=== MISCELLANEOUS EXAMPLES: ADVANCED OOP ===")

# --- Concept A: Method Overriding & super() ---
print("\n[Concept A: Method Overriding]")
class Employee:
    def work(self):
        print("Employee is working.")

class Manager(Employee):
    def work(self):
        super().work()  # Calls parent method
        print("Manager is supervising the team.")

mgr = Manager()
mgr.work()

# --- Concept B: Built-in Inheritance Checks ---
print("\n[Concept B: isinstance() and issubclass()]")
print("Is mgr an instance of Manager?", isinstance(mgr, Manager))       # True
print("Is mgr an instance of Employee?", isinstance(mgr, Employee))     # True
print("Is Manager a subclass of Employee?", issubclass(Manager, Employee)) # True


#Super() is a built-in function in Python that allows you to call methods from a parent class.
#It is commonly used in inheritance to access the parent class's methods and attributes, especially when overriding methods in a child class. 
#The super() function helps maintain the method resolution order (MRO) and ensures that the correct method from the parent class is called.
#The super() function takes the following arguments:
#   1. The name of the method to be called in the child class.
#   2. The object on which the method is called.
#   3. Additional arguments to be passed to the method.

# Example A: super() in a method
print("[Example A: super() in an overridden method]")
class Animal:
    def eat(self):
        print("Animal is eating.")

class Dog(Animal):
    def eat(self):  # Overriding the parent's 'eat' method
        super().eat()  # Calls the parent's (Animal) eat() method first
        print("Dog is also eating kibble.")  # Child's own extra logic

d = Dog()
d.eat()

#Example2: Using __init__ to initialize attributes and super() to call parent methods
print("\n--- [Example 2: Using __init__ to initialize attributes and super() to call parent methods] ---")
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal):
    def __init__(self, name, favorite_food):
        super().__init__(name)  # Calls the parent's __init__ method
        self.favorite_food = favorite_food

    def eat(self):
        super().eat()  # Calls the parent's eat() method
        print(f"{self.name} is also eating {self.favorite_food}.")  # Child's own extra logic

d = Dog("Buddy", "kibble")
d.eat()  # Output: Buddy is eating.
#      Buddy is also eating kibble.