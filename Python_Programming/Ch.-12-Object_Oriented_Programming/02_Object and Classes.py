# ==========================================
# OBJECT-ORIENTED PROGRAMMING (OOP) - CLASSES & OBJECTS
# ==========================================

# ==========================================
# 1. WHAT IS A CLASS?
# ==========================================
# A class is a template or a blueprint for creating objects. 
# It defines the attributes (data) and methods (behaviors) that objects of that class will have.
# Note: The class name should follow the PascalCase naming convention (e.g., MyClass, Dog, Car).

# Syntax:
# class ClassName:
#     attribute1 = value1
#     ...
#     def method1(self, arg1, ...):
#         pass


# ==========================================
# 2. MODELLING A PROBLEM IN OOP
# ==========================================
# - Noun    -> Class Name (e.g., Dog, Person) or Object Name (e.g., my_dog, anurag)
# - Adjective -> Attribute / Property (e.g., name, breed, age, role)
# - Verb    -> Method / Behavior (e.g., bark, speak, display)


# ==========================================
# 3. WHAT IS AN OBJECT?
# ==========================================
# - An object is an instance of a class. It is a specific realization of the class with its own set of attributes and methods.
# - A class is a placeholder/blueprint, and an object is the actual instance created from that blueprint.
# - Objects can invoke methods and access attributes defined in the class.

# Syntax: 
# object_name = ClassName(arguments)


# ==========================================
# 4. EXAMPLE OF A BASIC CLASS AND OBJECT
# ==========================================
class Person:        # Class name: Person
    name = "Anurag Srivastva"  # Class attribute (Data)
    age = 28
    role = "Data_Analyst" 
    skill1 = "Python"
    skill2 = "SQL"
    skill3 = "Power Bi"
    skill4 = "Tableau"
    skill5 = "Machine_Learning"

anurag = Person()  # Object name: anurag
print(anurag.name)   # Output: Anurag Srivastva
print(anurag.age)    # Output: 28
print(anurag.role)   # Output: Data_Analyst
print(anurag.skill1) # Output: Python

# Modifying and Adding Attributes on an Instance:
anurag.salary = 100000  # Salary is an instance attribute (specific to 'anurag', not shared by other Person objects)
anurag.age = 29         # Modifying an existing attribute (instance attribute overrides class attribute preference)
print(anurag.salary)    # Output: 100000


# ==========================================
# 5. CONSTRUCTOR AND THE __init__ METHOD
# ==========================================
# - What is a constructor? A special method automatically called when a new object of a class is created.
# - Primary Use: To initialize the attributes of the object with initial values.
# - What is __init__? A dunder (double underscore) or magic method automatically called upon object creation.

# Syntax:
# def __init__(self, arg1, arg2, ...):
#     self.attribute1 = arg1
#     self.attribute2 = arg2


# ==========================================
# 6. WHAT IS THE 'self' PARAMETER?
# ==========================================
# - The 'self' parameter is a reference to the current instance of the class.
# - It is used to access variables and methods associated with the current object.
# - It is automatically passed with a function call from an object.
# (Note: In the user prompt snippet reference: def __init__(self, self, ...) was a typo note; standard signature is def __init__(self, arg1, ...)).


# ==========================================
# 7. EXAMPLE: USING CONSTRUCTOR AND METHODS
# ==========================================
class PersonDetailed:
    def __init__(self, name, age, role, skills):
        self.name = name
        self.age = age
        self.role = role
        self.skills = skills

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Role: {self.role}")
        print(f"Skills: {self.skills}")


# ==========================================
# 8. CREATING OBJECTS USING ARGUMENTS
# ==========================================
class Dog:
    def __init__(self, name, breed):
        self.name = name    # Instance Attribute
        self.breed = breed  # Instance Attribute

    def bark(self):
        print(f"{self.name} says Woof!")

my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.name)   # Output: Buddy
print(my_dog.breed)  # Output: Golden Retriever
my_dog.bark()        # Output: Buddy says Woof!


# ==========================================
# 9. CLASS ATTRIBUTES VS INSTANCE ATTRIBUTES
# ==========================================
# - Class Attributes: Static data that belongs to the class itself and is shared by all instances of the class.
# - Instance Attributes: Data specific to each individual instance (object) of a class. Not shared.
# - Precedence: Instance attributes take precedence over class attributes during assignment and retrieval. 
#   If an instance attribute has the same name as a class attribute, it overrides it for that specific instance.

class DogWithClassAttr:
    species = "Canis familiaris"  # Class attribute

    def __init__(self, name, breed):
        self.name = name        # Instance attribute
        self.breed = breed      # Instance attribute

print(DogWithClassAttr.species) # Output: Canis familiaris


# ==========================================
# 10. TYPES OF METHODS IN PYTHON CLASSES
# ==========================================

# A. Instance Methods
# - Methods defined within a class that are associated with a specific instance (object).
# - They take 'self' as their first parameter and can modify or access object state.
# Syntax: object_name.method_name(arg1, arg2, ...)


# B. Class Methods
# - Methods that belong to the class itself rather than any single object.
# - Defined using the @classmethod decorator and take 'cls' as their first parameter.
class DogWithClassMethod:
    species = "Canis familiaris"

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    @classmethod
    def get_species(cls):
        return cls.species

print(DogWithClassMethod.get_species())  # Output: Canis familiaris


# C. Static Methods
# - Methods that belong to a class but do NOT have access to instance (self) or class (cls) variables.
# - Defined using the @staticmethod decorator.
# - Used primarily for utility or helper functions that do not require access to object or class data.

# Syntax:
# @staticmethod
# def method_name(arg1, arg2, ...):

class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        return x / y

print(MathUtils.add(10, 5))  # Output: 15