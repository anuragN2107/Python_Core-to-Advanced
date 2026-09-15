# ===============================================================================================================================
#                                       MASTER NOTES: PYTHON CONSTRUCTORS & DECORATORS
# ===============================================================================================================================


# ===============================================================================================================================
# PART 1: PYTHON CONSTRUCTORS (__init__ method)
# ===============================================================================================================================

# WHAT IS A CONSTRUCTOR?
# A constructor is a special magic method in Python named `__init__`. 
# Its primary job is to initialize (assign initial values to) the attributes of an object 
# the moment that object is created from a class. Think of it like filling out a 
# registration form automatically whenever a new user profile is created.

# HOW `self` WORKS:
# `self` represents the *current instance* (the specific object) you are working with. 
# When you write `self.name = name`, Python attaches the passed value to that specific object.

class Student:
    # This is a Parameterized Constructor (accepts arguments besides self)
    def __init__(self, name, age, course="Computer Science"):
        # Initializing instance attributes
        self.name = name
        self.age = age
        self.course = course  # Parameter with a default value (optional argument)

    def display_info(self):
        print(f"Student: {self.name}, Age: {self.age}, Course: {self.course}")

# Creating objects triggers the __init__ constructor automatically
s1 = Student("Alice", 20)                 # Uses default course ("Computer Science")
s2 = Student("Bob", 22, "Data Science")   # Overrides default course

s1.display_info()
s2.display_info()

# KEY RULE FOR CONSTRUCTORS:
# The constructor must NOT return anything (it implicitly returns `None`). 
# If you try to write `return self.name` inside `__init__`, Python will raise a TypeError.
print()


# ===============================================================================================================================
# PART 2: BUILT-IN CLASS DECORATORS (@staticmethod, @classmethod, @property)
# ===============================================================================================================================
# Python provides built-in decorators to modify how methods behave inside a class.
# The three most important ones are @staticmethod, @classmethod, and @property (Getters & Setters).

print("=== PART 2: BUILT-IN CLASS DECORATORS ===")

class BankAccount:
    bank_name = "Global National Bank"  # Class attribute (shared by all accounts)

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute (hidden from direct outside access)

    # -------------------------------------------------------------
    # 1. @staticmethod
    # -------------------------------------------------------------
    # - Does NOT take 'self' or 'cls'. 
    # - It behaves like a normal function, but lives inside the class namespace because 
    #   it is logically related to the class. Use it when you don't need access to object or class data.
    #Syntax: @staticmethod
    #   def method_name(*args, **kwargs):
    #       ...
    @staticmethod
    def bank_rules():
        print("Rule: Always keep your PIN secure and report lost cards immediately.")

    # -------------------------------------------------------------
    # 2. @classmethod
    # -------------------------------------------------------------
    # - Takes 'cls' instead of 'self'. 
    # - It can access and modify class-level attributes across all instances.
    #Syntax: @classmethod
    #   def method_name(cls, *args, **kwargs):
    #       ...
    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name


# --- Demonstration of @staticmethod ---
print("\n--- [Demo] @staticmethod ---")
class MathUtils:
    @staticmethod
    def add_numbers(a, b):
        """A utility method that doesn't rely on class or instance state."""
        return a + b

# Calling static method directly on the class (recommended)
print("Sum via Class:", MathUtils.add_numbers(10, 20))

# Calling static method on an object instance (possible, but passes no self/cls)
math_obj = MathUtils()
print("Sum via Instance:", math_obj.add_numbers(5, 15))


# Demonstration of @classmethod with Employee scope
class Employee:
    a = 1  # Class attribute shared across all instances

    @classmethod
    def show(cls):  
        print(f"The class attribute of a is {cls.a}")

e = Employee() 
e.a = 45  # Creating an instance-level attribute 'a' (does not affect the class attribute 'a')
e.show()  # Calling the class method using the object (Outputs: 1, because cls references the class level)


# -------------------------------------------------------------
# 3. @property (Getter & Setter Decorators)
# -------------------------------------------------------------
# - Getter (@property): Allows a method to be accessed like a normal variable attribute (without parentheses `()`).
# - Setter (@property.setter): Controls how attributes are modified, allowing validation logic before updating private data.
#Syntax: @property
#   def getter_method(self):
#       ...
#   @property.setter
#   def setter_method(self, new_value):
#       ...

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price  # Triggers the setter method automatically upon initialization

    # --- GETTER ---
    @property
    def price(self):
        """Retrieves the private price value safely."""
        return self._price

    # --- SETTER ---
    @price.setter
    def price(self, new_price):
        """Validates the price before assignment to ensure data integrity."""
        if new_price < 0:
            print(f"[Validation Error]: Price '{new_price}' cannot be negative! Setting default to 0.")
            self._price = 0
        else:
            self._price = new_price


# --- Executing Built-in Decorators ---
print("\n--- Executing Built-in Decorators ---")
BankAccount.bank_rules()  # Called directly on the class

BankAccount.change_bank_name("Future Trust Bank")
print("Updated Bank Name:", BankAccount.bank_name)

acc = BankAccount("Charlie", 10000)
print("Account Owner:", acc.owner)

# Testing @property Getter and Setter with Product class
p = Product("Laptop", 1200)
print(f"Product: {p.name}, Price: ${p.price}")  # Accessed as variable (Getter)

print("\nAttempting to set an invalid negative price:")
p.price = -500  # Triggers the Setter validation
print(f"Corrected Price: ${p.price}")
print()


# ===============================================================================================================================
# PART 3: CUSTOM FUNCTION DECORATORS
# ===============================================================================================================================

# WHAT IS A DECORATOR?
# A decorator is a design pattern that allows you to wrap another function to 
# extend or alter its behavior *without modifying the original function's actual code*.
# To understand decorators, you must first understand two foundational concepts in Python:


# CONCEPT A: Functions are "First-Class Citizens"
# This means functions can be treated like regular variables—passed into other functions, 
# assigned to variables, or returned.

def say_hello(name):
    return f"Hello, {name}!"

greet_variable = say_hello  # Assigning function to a variable
print("First-Class Citizen Test:", greet_variable("David"))


# CONCEPT B: Nested Functions (Functions inside Functions)
# A function can be defined inside another function. The inner function has access 
# to variables of the outer function (this forms the basis of closures).

def outer_message(message):
    def inner_printer():
        print(f"Nested Output: {message}")
    return inner_printer  # Returning the function itself, not calling it

my_printer = outer_message("Python decorators are powerful!")
my_printer()  # Executes the inner function
print()


# =====================================================================
# BUILDING A COMPLETE CUSTOM DECORATOR
# =====================================================================
# A standard custom decorator follows this exact structure:
# 1. Takes a function as an argument.
# 2. Defines an inner wrapper function that adds extra logic.
# 3. Calls the original function inside the wrapper.
# 4. Returns the wrapper function.

from functools import wraps

def execution_timer_decorator(func):
    """
    This is a decorator that measures how long a function takes to execute,
    while keeping the original function's metadata intact using @wraps.
    """
    @wraps(func)  # CRITICAL: Preserves original function's __name__ and __doc__
    def wrapper(*args, **kwargs):  # *args and **kwargs allow any function parameters to pass through
        print(f"\n[LOG] Starting execution of function: '{func.__name__}'")
        
        # Execute the actual original function
        result = func(*args, **kwargs)
        
        print(f"[LOG] Finished execution of function: '{func.__name__}'")
        return result  # Return whatever the original function calculated
    
    return wrapper


# Applying the decorator using syntactic sugar '@'
@execution_timer_decorator
def calculate_factorial(n):
    """Calculates the factorial of a given number n."""
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


# --- Execution and Verification ---
output = calculate_factorial(5)
print("Factorial Result:", output)

# Verifying that @wraps successfully preserved the function's metadata
print("Function Name:", calculate_factorial.__name__)     # Output: calculate_factorial
print("Function Docstring:", calculate_factorial.__doc__) # Output: Calculates the factorial of a given number n.