# ==============================================================================
#      CHAPTER 8: VARIABLE SCOPE (LEGB), LAMBDA & FUNCTIONAL TOOLS
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. VARIABLE SCOPE & THE LEGB RULE
# ------------------------------------------------------------------------------
# Scope defines the region of a program where a variable is recognized and accessible.
# When a variable is accessed, Python searches scopes in strict LEGB order:
#   L: Local      -> Names assigned inside the current function/lambda.
#   E: Enclosing  -> Names in the local scope of enclosing/outer functions (closures).
#   G: Global     -> Names assigned at the top level of the module/script.
#   B: Built-in   -> Pre-assigned built-in names (e.g., print, len, range, sum).

print("--- 1. Variable Scope (Local vs. Global) ---")

app_name = "SuperChat"  # Global Scope (Module level)

def show_welcome():
    user_name = "Alice"  # Local Scope (Accessible only inside show_welcome)
    print(f"Welcome {user_name} to {app_name}!")

show_welcome()
# print(user_name)  # Raises NameError: name 'user_name' is not defined


# ------------------------------------------------------------------------------
# 2. MODIFYING SCOPES: `global` AND `nonlocal`
# ------------------------------------------------------------------------------
# By default, functions can READ global variables but CANNOT modify them.
# - global   : Binds a local variable directly to the module-level global variable.
# - nonlocal : Binds a variable in a nested function to its outer enclosing function.

# --- Example A: Modifying Global Variables with `global` ---
counter = 0

def increment_global():
    global counter  # Declares intention to modify the global 'counter'
    counter += 1

increment_global()
print(f"Updated global counter: {counter}")  # Output: 1


# --- Example B: Modifying Enclosing Variables with `nonlocal` ---
def outer_function():
    count = 10

    def inner_function():
        nonlocal count  # Targets 'count' from outer_function (Enclosing scope)
        count += 5

    inner_function()
    print(f"Updated enclosing count: {count}")  # Output: 15

outer_function()


# ------------------------------------------------------------------------------
# 3. LAMBDA FUNCTIONS (ANONYMOUS FUNCTIONS)
# ------------------------------------------------------------------------------
# A small, inline function defined without a name using the `lambda` keyword.
# It can accept any number of arguments, but can only contain ONE expression.
#
# Syntax:
#   lambda arguments : expression

print("\n--- 2. Lambda Functions ---")

# Basic Lambda:
square = lambda x: x * x
print(f"Square of 5: {square(5)}")  # Output: 25

# Lambda with multiple arguments:
add = lambda a, b: a + b
print(f"Sum (3 + 4): {add(3, 4)}")  # Output: 7

# Custom Sorting using Lambda as a `key`:
students = [("Alice", 85), ("Bob", 98), ("Charlie", 72)]
# Sort by marks (index 1) descending:
students_sorted = sorted(students, key=lambda student: student[1], reverse=True)
print(f"Ranked Students: {students_sorted}")
# Output: [('Bob', 98), ('Alice', 85), ('Charlie', 72)]


# ------------------------------------------------------------------------------
# 4. BUILT-IN FUNCTIONAL PROGRAMMING TOOLS
# ------------------------------------------------------------------------------
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# 1. map(func, iterable):
# Applies a function to every item in an iterable.
squared_nums = list(map(lambda x: x ** 2, numbers))
print(f"\nMap (Squares):   {squared_nums}")  # Output: [1, 4, 9, 16, 25, 36]

# 2. filter(func, iterable):
# Keeps only items for which the test function returns True.
even_nums = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Filter (Evens):  {even_nums}")  # Output: [2, 4, 6]

# 3. reduce(func, iterable):
# Cumulatively applies a function to elements from left to right to reduce to a single value.
sum_total = reduce(lambda acc, val: acc + val, numbers)
print(f"Reduce (Sum):    {sum_total}")  # Output: 21

# 4. sorted(iterable, key=..., reverse=...):
# Returns a brand-new sorted list without modifying the original iterable.
unordered = [5, 2, 8, 1, 9]
print(f"Sorted Copy:     {sorted(unordered)}")  # Output: [1, 2, 5, 8, 9]

# 5. any() and all():
# - any(): Returns True if AT LEAST ONE element is Truthy.
# - all(): Returns True ONLY if EVERY element is Truthy.
print(f"Any number > 5:  {any(n > 5 for n in numbers)}")  # Output: True
print(f"All numbers > 0:  {all(n > 0 for n in numbers)}")  # Output: True
# ==============================================================================