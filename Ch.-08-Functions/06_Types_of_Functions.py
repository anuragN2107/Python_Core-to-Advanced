# ==============================================================================
#                  TYPES OF FUNCTIONS & RECURSION
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. BUILT-IN FUNCTIONS
# ------------------------------------------------------------------------------
# Predefined functions provided directly by Python without requiring any imports.
numbers = [10, 20, 30]
print("--- 1. Built-in Functions ---")
print("len(): ", len(numbers))   # 3
print("sum(): ", sum(numbers))   # 60
print("max(): ", max(numbers))   # 30
print("type():", type(numbers))  # <class 'list'>


# ------------------------------------------------------------------------------
# 2. USER-DEFINED FUNCTIONS
# ------------------------------------------------------------------------------
# Functions created by developers using the `def` keyword to encapsulate reusable logic.
print("\n--- 2. User-Defined Functions ---")
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Hello, Alice!


# ------------------------------------------------------------------------------
# 3. LAMBDA FUNCTIONS (ANONYMOUS FUNCTIONS)
# ------------------------------------------------------------------------------
# Small, single-line functions created with the `lambda` keyword.
print("\n--- 3. Lambda Functions ---")
add = lambda x, y: x + y
print("Lambda Add (2, 3):", add(2, 3))  # 5


# ------------------------------------------------------------------------------
# 4. INSTANCE METHODS (OOP METHODS)
# ------------------------------------------------------------------------------
# Functions defined inside a class that take `self` to operate on individual object instances.
print("\n--- 4. Instance Methods ---")
class CircleInstance:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

circle = CircleInstance(5)
print("Instance Method Area:", circle.area())  # 78.5


# ------------------------------------------------------------------------------
# 5. CLASS METHODS
# ------------------------------------------------------------------------------
# Bound to the class rather than instance; marked with `@classmethod` and takes `cls`.
# Commonly used as alternative constructors / factory methods.
print("\n--- 5. Class Methods ---")
class CircleClassMethod:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

c_from_diam = CircleClassMethod.from_diameter(10)
print("Class Method (radius from diameter):", c_from_diam.radius)  # 5.0


# ------------------------------------------------------------------------------
# 6. STATIC METHODS
# ------------------------------------------------------------------------------
# Utility functions housed inside a class using `@staticmethod` that do NOT require
# access to `self` (instance state) or `cls` (class state).
print("\n--- 6. Static Methods ---")
class CircleStatic:
    @staticmethod
    def area(radius):
        return 3.14 * (radius ** 2)

print("Static Method Area:", CircleStatic.area(5))  # 78.5


# ------------------------------------------------------------------------------
# 7. DECORATORS
# ------------------------------------------------------------------------------
# Functions that take another function as an argument, wrap/modify its behavior,
# and return the wrapped function.
print("\n--- 7. Decorators ---")
def decorator_greet(func):
    def wrapper():
        return f"Hello, {func()}!"
    return wrapper

@decorator_greet
def get_user_name():
    return "Alice"

print(get_user_name())  # Hello, Alice!


# ------------------------------------------------------------------------------
# 8. GENERATORS (USING `yield`)
# ------------------------------------------------------------------------------
# Functions that yield values lazily one at a time on demand rather than storing
# the entire collection in memory.
print("\n--- 8. Generators ---")
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
print(next(fib))  # 0
print(next(fib))  # 1
print(next(fib))  # 1
print(next(fib))  # 2


# ------------------------------------------------------------------------------
# 9. ASYNCHRONOUS FUNCTIONS (`async` / `await`)
# ------------------------------------------------------------------------------
# Functions used for non-blocking I/O tasks managed by an event loop.
import asyncio

async def fetch_data():
    await asyncio.sleep(0.01)
    return {"name": "Alice", "age": 25}

data = asyncio.run(fetch_data())
print("\n--- 9. Async Functions ---")
print("Async Output:", data)  # {'name': 'Alice', 'age': 25}


# ------------------------------------------------------------------------------
# 10. CLOSURES
# ------------------------------------------------------------------------------
# Inner functions that retain access to variables in their enclosing scope even after
# the outer function has finished execution.
print("\n--- 10. Closures ---")
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

my_counter = counter()
print("Closure Call 1:", my_counter())  # 1
print("Closure Call 2:", my_counter())  # 2
print("Closure Call 3:", my_counter())  # 3


# ------------------------------------------------------------------------------
# 11. PROPERTY DECORATORS & GETTER/SETTER DESCRIPTORS
# ------------------------------------------------------------------------------
# Enables accessing and updating method returns using standard attribute syntax.
print("\n--- 11. Property Decorators & Setters ---")
class CircleProperty:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.14 * (self._radius ** 2)

    @area.setter
    def area(self, value):
        self._radius = (value / 3.14) ** 0.5

circle_prop = CircleProperty(5)
print("Initial area:", circle_prop.area)  # 78.5
circle_prop.area = 314
print("Radius after setting area:", circle_prop._radius)  # 10.0


# ------------------------------------------------------------------------------
# 12. ITERATORS
# ------------------------------------------------------------------------------
# Objects implementing `__iter__()` and `__next__()` protocols. Iterated through loops.
print("\n--- 12. Iterators ---")
fruits = ["apple", "banana", "cherry"]
fruit_iter = iter(fruits)
print(next(fruit_iter))  # apple
print(next(fruit_iter))  # banana


# ------------------------------------------------------------------------------
# 13. CONSTRUCTORS (`__init__`) & DESTRUCTORS (`__del__`)
# ------------------------------------------------------------------------------
# - `__init__`: Automatically runs when a new object instance is allocated.
# - `__del__` : Automatically runs when an object is garbage-collected or deleted.
print("\n--- 13. Constructors & Destructors ---")
class ResourceTracker:
    def __init__(self, resource_id):
        self.resource_id = resource_id
        print(f"Resource {self.resource_id} allocated")

    def __del__(self):
        print(f"Resource {self.resource_id} cleaned up")

res = ResourceTracker(101)
del res  # Output: Resource 101 cleaned up


# ------------------------------------------------------------------------------
# 14. HIGHER-ORDER FUNCTIONS
# ------------------------------------------------------------------------------
# Functions that accept other functions as parameters or return functions as results.
print("\n--- 14. Higher-Order Functions ---")
def apply_twice(func, x):
    return func(func(x))

def square(x):
    return x * x

print("apply_twice(square, 3):", apply_twice(square, 3))  # 81


# ------------------------------------------------------------------------------
# 15. PURE VS. IMPURE FUNCTIONS
# ------------------------------------------------------------------------------
# Pure Function: Deterministic (same inputs -> same output) with NO external side effects.
# Impure Function: Relies on external state or triggers side effects (I/O, printing, mutation).
print("\n--- 15. Pure vs Impure Functions ---")
def pure_add(x, y):
    return x + y  # Pure: no side effects, deterministic

def impure_add(x):
    print("Printing inside function")  # Impure: side effect (I/O)
    return x + 10

print("Pure Add:", pure_add(2, 3))


# ------------------------------------------------------------------------------
# 16. RECURSION (DEEP DIVE)
# ------------------------------------------------------------------------------
# Recursion is a technique where a function calls itself to solve smaller subproblems.
#
# Every recursive function MUST have two critical components:
# 1. Base Case    : Condition that stops recursion (prevents RecursionError / stack overflow).
# 2. Recursive Case: The function calling itself with a modified, smaller input.

print("\n--- 16. Recursion Examples ---")

# --- Example A: Factorial ---
# Mathematical definition:
# n! = n * (n - 1)!
# Base case: 0! = 1, 1! = 1
def factorial(n):
    """Calculates n! recursively."""
    if n < 0:
        return "Undefined for negative numbers"
    if n == 0 or n == 1:
        return 1  # Base Case
    return n * factorial(n - 1)  # Recursive Case

print(f"Factorial of 5: {factorial(5)}")  # 120
print(f"Factorial of 0: {factorial(0)}")  # 1


# --- Example B: Sum of First N Natural Numbers ---
# Mathematical definition:
# sum(n) = n + sum(n - 1)
# Base case: sum(1) = 1
def sum_natural(n):
    """Calculates the sum of numbers from 1 to n recursively."""
    if n <= 1:
        return n  # Base Case
    return n + sum_natural(n - 1)  # Recursive Case

print(f"Sum of first 5 natural numbers: {sum_natural(5)}")  # 15
# ==============================================================================