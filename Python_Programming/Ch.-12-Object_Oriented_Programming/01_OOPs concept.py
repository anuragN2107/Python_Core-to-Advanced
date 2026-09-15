# ==========================================
# OBJECT-ORIENTED PROGRAMMING (OOP) - BASICS
# ==========================================

# 1. WHAT IS OOP?
# Object-Oriented Programming is a programming style that uses "objects" to represent real-world things (like a Car, a User, or a Bank Account).
# It helps organize code using the DRY (Don't Repeat Yourself) principle, making large programs easier to maintain, scale, and understand.


# 2. CORE CONCEPTS: CLASSES, OBJECTS, ATTRIBUTES, AND METHODS
# A. CLASSES
# - Class: A blueprint, template, or design for creating objects (e.g., a House blueprint).
# - Object: An actual physical instance built from that blueprint (e.g., House #405).
#   Multiple objects can be created from a single class.

# B. OBJECTS
# - Objects are instances of classes, which are blueprints for creating objects.
#   Objects are created from classes using the class's constructor (special method).

# C. ATTRIBUTES AND METHODS
# Every object consists of two main components:
# - Attributes: Variables that store data or properties (e.g., height, color, weight).
# - Methods: Functions defined inside a class that represent actions or behaviors (e.g., walk(), speak()).


# 3. SIMPLE EXAMPLE OF A CLASS IN PYTHON
class Dog:
    
    # Constructor: Special method used to set up initial attributes
    def __init__(self, name, breed):
        self.name = name    # Attribute (Data)
        self.breed = breed  # Attribute (Data)

    # Method: Behavior/Action the object can perform
    def bark(self):
        print(f"{self.name} says Woof!")


# Creating an object (Instance) from the Dog class
my_dog = Dog("Buddy", "Golden Retriever")

# Accessing attributes and calling methods
print(my_dog.name)   # Output: Buddy
print(my_dog.breed)  # Output: Golden Retriever
my_dog.bark()        # Output: Buddy says Woof!


# 4. THE 4 PILLARS OF OOP
# B. Encapsulation (Data Hiding and Bundling)
# - Wrapping data (attributes) and methods into a single unit (class).
# - It restricts direct access to some components to protect data from accidental changes.

# C. Inheritance (Code Reusability)
# - Allows a new class (Child/Subclass) to adopt attributes and methods 
#   from an existing class (Parent/Superclass), avoiding repeated code.
# - Example: Class 'ElectricCar' can inherit basic features from class 'Car'.

# D. Polymorphism (Many Forms)
# - Allows different classes to have methods with the same name 
#   but perform different tasks based on the object calling them.
# - Example: A 'Dog' object and a 'Cat' object both have a `make_sound()` method, 
#   but Dog outputs "Bark" while Cat outputs "Meow".

# E. Abstraction (Hiding Complexity)
# - Hiding complex background details and showing only the essential features to the user.
# - Example: When driving a car, you press the accelerator to go faster 
#   without needing to know how the fuel injection and engine cylinders work.