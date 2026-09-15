# ===============================================================================================================================
#                                       PYTHON POLYMORPHISM: MASTER GUIDE & NOTES
# ===============================================================================================================================

# -------------------------------------------------------------------------------------------------------------------------------
# WHAT IS POLYMORPHISM? (CORE DEFINITION)
# -------------------------------------------------------------------------------------------------------------------------------
# The word "Polymorphism" comes from Greek: **Poly** means "many" and **morph** means "forms". 
# 
# Definition:
# In Object-Oriented Programming (OOP), polymorphism refers to the ability of different classes to have methods with the 
# **same name**, but execute different behaviors depending on the object calling them.
# 
# Real-World Analogy:
# Think of a button called "Press". 
# - If you press a **Doorbell**, it rings a chime.
# - If you press an **Elevator Button**, it lights up and calls an elevator.
# - If you press a **Light Switch**, it turns the lights on/off.
# The action is the *same* ("Press"), but the outcome depends entirely on *who* receives the action!
#
# Why Use Polymorphism?
# 1. Code Flexibility: Allows you to write generic functions that can handle objects of different types seamlessly.
# 2. Reduced Complexity: You don't need massive `if-else` blocks to check what type an object is before calling a method.
# -------------------------------------------------------------------------------------------------------------------------------


# ===============================================================================================================================
# TYPES OF POLYMORPHISM IN PYTHON
# ===============================================================================================================================
# Python achieves polymorphism mainly through two approaches:
# 1. Method Overriding (Inheritance-based Polymorphism): A child class provides its own specific implementation of a method 
#    that is already defined in its parent class.
# 2. Duck Typing (Dynamic Polymorphism): Python cares more about what methods an object *has* than what class it *belongs to*. 
#    ("If it walks like a duck and quacks like a duck, it's a duck.")
# -------------------------------------------------------------------------------------------------------------------------------


# ===============================================================================================================================
# PRACTICAL EXAMPLE 1: POLYMORPHISM THROUGH METHOD OVERRIDING (INHERITANCE)
# ===============================================================================================================================

print("=== 1. METHOD OVERRIDING POLYMORPHISM ===")

class Animal:
    def make_sound(self):
        """Base method to be overridden by child classes."""
        print("Some generic animal sound...")

class Dog(Animal):
    # Overriding the parent method
    def make_sound(self):
        print("Dog barks: Woof! Woof!")

class Cat(Animal):
    # Overriding the parent method
    def make_sound(self):
        print("Cat meows: Meow! Meow!")

class Cow(Animal):
    # Overriding the parent method
    def make_sound(self):
        print("Cow moos: Moo! Moo!")


# A polymorphic function that accepts *any* animal object and calls its sound method
def animal_party(animal_object):
    animal_object.make_sound()  # Python automatically figures out which version to call!

# Testing Method Overriding
d = Dog()
c = Cat()
w = Cow()

animal_party(d)  # Output: Dog barks: Woof! Woof!
animal_party(c)  # Output: Cat meows: Meow! Meow!
animal_party(w)  # Output: Cow moos: Moo! Moo!
print()


# ===============================================================================================================================
# PRACTICAL EXAMPLE 2: POLYMORPHISM THROUGH DUCK TYPING
# ===============================================================================================================================
# Duck typing means Python does not check the class type explicitly. As long as the object 
# has the expected method name, Python will execute it successfully without requiring inheritance.

print("=== 2. DUCK TYPING POLYMORPHISM ===")

class PDFDocument:
    def print_document(self):
        print("Printing PDF file layout...")

class WordDocument:
    def print_document(self):
        print("Printing Microsoft Word document layout...")

class Photo:
    # Notice: Photo has NO relation to PDF or Word, but shares the same method name!
    def print_document(self):
        print("Printing high-resolution image...")


# A polymorphic function using Duck Typing (Fixed missing 'def' keyword here)
def print_job(doc):
    # It doesn't care what class doc belongs to, as long as it has 'print_document'
    doc.print_document()

# Testing Duck Typing
pdf = PDFDocument()
word = WordDocument()
pic = Photo()

print_job(pdf)   # Works perfectly!
print_job(word)  # Works perfectly!
print_job(pic)   # Works perfectly because it 'walks like a duck' (has the method)!
print()


# ===============================================================================================================================
# PRACTICAL EXAMPLE 3: BUILT-IN POLYMORPHISM (LEN FUNCTION & OPERATORS)
# ===============================================================================================================================
# Python uses polymorphism built right into its core functions and operators.
# For example, the `len()` function changes behavior depending on the data type passed:

print("=== 3. BUILT-IN POLYMORPHISM ===")

# 1. String length
print("Length of string 'Python':", len("Python"))  # Counts characters (6)

# 2. List length
print("Length of list [1, 2, 3, 4, 5]:", len([1, 2, 3, 4, 5]))  # Counts items (5)

# 3. Dictionary length
print("Length of dictionary:", len({"a": 1, "b": 2}))  # Counts key-value pairs (2)

# Behind the scenes, `len()` is simply calling the `__len__()` dunder method unique to each object type!