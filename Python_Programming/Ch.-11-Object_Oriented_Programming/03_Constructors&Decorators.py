# ============================================
# MASTER NOTES: PYTHON CONSTRUCTORS & DECORATORS
# ============================================


# ============================================
# PART 1: PYTHON CONSTRUCTORS (__init__ method)
# ============================================

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


# ============================================
# PART 2: BUILT-IN CLASS DECORATORS
# ============================================
# Python provides built-in decorators to modify how methods behave inside a class.
# The three most important ones are @staticmethod, @classmethod, and @property.

class BankAccount:
    bank_name = "Global National Bank"  # Class attribute (shared by all accounts)

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute (hidden from direct outside access)

    # 1. @staticmethod
    # - Does NOT take 'self' or 'cls'. 
    # - It behaves like a normal function, but lives inside the class namespace because 
    #   it is logically related to the class. Use it when you don't need access to object or class data.
    @staticmethod
    def bank_rules():
        print("Rule: Always keep your PIN secure and report lost cards immediately.")

    # 2. @classmethod
    # - Takes 'cls' instead of 'self'. 
    # - It can access and modify class-level attributes across all instances.
    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    # 3. @property (Getter Decorator)
    # - Allows a method to be accessed like a normal variable attribute (without parentheses `()`).
    # - Highly useful for exposing private data safely.
    @property
    def balance(self):
        return self.__balance


# --- Executing Built-in Decorators ---
BankAccount.bank_rules()  # Called directly on the class

BankAccount.change_bank_name("Future Trust Bank")
print("Updated Bank Name:", BankAccount.bank_name)

acc = BankAccount("Charlie", 10000)
print("Account Owner:", acc.owner)
print("Account Balance:", acc.balance)  # Notice: accessed as 'acc.balance', NOT 'acc.balance()'


# ============================================
# PART 3: CUSTOM FUNCTION DECORATORS
# ============================================

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
print(greet_variable("David"))


# CONCEPT B: Nested Functions (Functions inside Functions)
# A function can be defined inside another function. The inner function has access 
# to variables of the outer function (this forms the basis of closures).

def outer_message(message):
    def inner_printer():
        print(f"Nested Output: {message}")
    return inner_printer  # Returning the function itself, not calling it

my_printer = outer_message("Python decorators are powerful!")
my_printer()  # Executes the inner function


# ============================================
# BUILDING A COMPLETE CUSTOM DECORATOR
# ============================================
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