# ==============================================================================
#         HIGHER-ORDER FUNCTIONS, CLOSURES & DECORATORS
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. FIRST-CLASS FUNCTIONS (FUNCTIONS AS DATA)
# ------------------------------------------------------------------------------
# In Python, functions are "first-class citizens". This means you can:
#   1. Assign functions to variables.
#   2. Pass functions as arguments to other functions.
#   3. Return functions from other functions.
#   4. Store functions in data structures (lists, dicts, etc.).

def shout(text):
    return text.upper()

# A. Assigning function to a variable (without parentheses `()`):
yell = shout
print("--- 1. First-Class Functions ---")
print(yell("hello world"))  # Output: HELLO WORLD

# B. Passing a function as an argument:
def apply_operation(func, value):
    return func(value)

print(apply_operation(shout, "python"))  # Output: PYTHON

# C. Returning a function from another function:
def get_greeter():
    return shout

my_func = get_greeter()
print(my_func("welcome"))  # Output: WELCOME


# ------------------------------------------------------------------------------
# 2. CLOSURES (RETAINING ENCLOSING STATE)
# ------------------------------------------------------------------------------
# A closure is an inner function that remembers and retains access to variables
# from its outer enclosing scope, even after the outer function has completed.
#
# Three Rules for a Closure:
#   1. Must have a nested (inner) function.
#   2. The inner function must reference a variable from the outer scope.
#   3. The outer function must return the inner function object.

def multiplier_of(factor):
    """Outer function defining an enclosing state 'factor'."""
    def multiply(number):
        """Inner function remembering 'factor'."""
        return number * factor
    return multiply

double = multiplier_of(2)  # Remembers factor = 2
triple = multiplier_of(3)  # Remembers factor = 3

print("\n--- 2. Closures ---")
print(f"Double of 7: {double(7)}")  # Output: 14
print(f"Triple of 7: {triple(7)}")  # Output: 21


# ------------------------------------------------------------------------------
# 3. DECORATORS (MODIFYING BEHAVIOR DYNAMICALLY)
# ------------------------------------------------------------------------------
# A decorator is a design pattern used to extend or modify the behavior of a
# function or method without altering its original source code.
# The `@decorator_name` syntax is shorthand (syntactic sugar) for:
#   function = decorator_name(function)

from functools import wraps
import time

# --- Example A: Performance Timing Decorator ---
def execution_timer(func):
    """Decorator to measure how long any function takes to execute."""
    @wraps(func)  # Preserves original function name and docstring
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_ms = (end_time - start_time) * 1000
        print(f"[LOG] {func.__name__}() took {elapsed_ms:.4f} ms to complete.")
        return result
    return wrapper


@execution_timer
def compute_heavy_sum(n):
    """Computes sum of squares up to n."""
    return sum(i * i for i in range(n))

print("\n--- 3. Decorator Examples ---")
ans = compute_heavy_sum(500_000)
print(f"Calculation Result: {ans}")


# --- Example B: Simple Logging / Debug Decorator ---
def logger(func):
    """Decorator to log function execution calls."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[CALL] Running {func.__name__} with args: {args}")
        val = func(*args, **kwargs)
        print(f"[DONE] {func.__name__} returned: {val}")
        return val
    return wrapper

@logger
def add(a, b):
    return a + b

add(10, 25)
# Output:
# [CALL] Running add with args: (10, 25)
# [DONE] add returned: 35
# ==============================================================================