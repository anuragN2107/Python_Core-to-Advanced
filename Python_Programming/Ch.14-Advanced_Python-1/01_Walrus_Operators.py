# ===============================================================================================================================
#                                       MASTER NOTES: THE WALRUS OPERATOR (:=) IN PYTHON
# ===============================================================================================================================
# This file is structured sequentially so you can read, understand, and run every concept step-by-step.


# ===============================================================================================================================
# STEP 1: WHAT IS THE WALRUS OPERATOR? (Definition)
# ===============================================================================================================================
# - Definition: The Walrus Operator (`:=`) is officially called an "Assignment Expression".
# - Purpose: It allows you to assign a value to a variable *inside* an expression (like an if statement, 
#   while loop, or list comprehension) where standard assignment (`=`) is normally forbidden.
# - Why the name?: The symbol `:=` looks sideways like the eyes and tusks of a walrus.


# ===============================================================================================================================
# STEP 2: HISTORY & BACKGROUND
# ===============================================================================================================================
# - Introduced in: Python 3.8 (Released in 2019).
# - Proposed via: PEP 572 (Authored by Chris Angelico, Guido van Rossum, and Nick Coghlan).
# - Why was it added?: To eliminate repetitive code and avoid calculating the same expression twice 
#   (such as calling a heavy function or checking a length twice).


# ===============================================================================================================================
# STEP 3: CORE SYNTAX & RULES
# ===============================================================================================================================
# - General Syntax: (variable := expression)
# - Rule 1: Parentheses are usually required because assignment expressions have very low operator precedence.
# - Rule 2: It cannot be used as a standalone top-level statement (e.g., `x := 5` by itself causes a SyntaxError).
# - Rule 3: Inline type hinting (e.g., `(x: int := 5)`) is NOT supported and will raise a SyntaxError.


# ===============================================================================================================================
# STEP 4: USE CASE 1 - STREAMLINING `while` LOOPS
# ===============================================================================================================================
print("=== DEMO 1: While Loop Streamlining ===")

# Problem: Usually, you have to prompt/get input before the loop and repeat it inside the loop.
# With the Walrus operator, you assign the input and check it in a single line.

# Simulating user inputs using an iterator so the code runs automatically without blocking:
simulated_inputs = iter(["hello", "python", "quit"])

def mock_input(prompt):
    return next(simulated_inputs)

# The actual walrus pattern for a while loop:
# while (user_input := input("Enter text: ")) != "quit":
#     print(f"You entered: {user_input}")

# Executing with our mock function:
while (user_input := mock_input("Enter text: ")) != "quit":
    print(f"-> Processed input: {user_input}")
print("Loop exited successfully!\n")


# ===============================================================================================================================
# STEP 5: USE CASE 2 - AVOIDING REDUNDANT FUNCTION CALLS IN `if` STATEMENTS
# ===============================================================================================================================
print("=== DEMO 2: If Statement Redundancy Reduction ===")

def fetch_data():
    """Simulates a function that returns a collection of items."""
    return [100, 200, 300, 400, 500]

# Without walrus, you might calculate len() twice or assign it on the line above.
# With walrus, we compute len(), store it in `count`, and evaluate it in the condition simultaneously:
if (count := len(fetch_data())) > 3:
    print(f"-> Warning: Large dataset detected with {count} items!\n")


# ===============================================================================================================================
# STEP 6: USE CASE 3 - OPTIMIZING LIST COMPREHENSIONS
# ===============================================================================================================================
print("=== DEMO 3: List Comprehension Optimization ===")

def expensive_operation(x):
    """Simulates a heavy calculation."""
    return x ** 2

# We calculate `y` once using the walrus operator, filter it, and store it directly in the list.
# This prevents calling `expensive_operation(x)` twice per item.
results = [y for x in range(8) if (y := expensive_operation(x)) > 20]
print(f"-> Filtered results (> 20): {results}\n")


# ===============================================================================================================================
# STEP 7: REAL-WORLD EXAMPLE (Regex Log Parsing)
# ===============================================================================================================================
print("=== DEMO 4: Real-World Regex Matching ===")

import re

log_message = "CRITICAL_ERROR: Code 503 encountered during server sync."
error_pattern = r"Code\s+(\d+)"

# Real-world scenario: Check if a regex match exists, and immediately capture its group 
# without executing re.search() twice.
if match := re.search(error_pattern, log_message):
    error_code = match.group(1)
    print(f"-> Alert! Caught error code number: {error_code}\n")
else:
    print("-> Log file is clean.\n")


# ===============================================================================================================================
# STEP 8: EXCEPTIONS, LIMITATIONS, & GOTCHAS
# ===============================================================================================================================
print("=== DEMO 5: Variable Scope Leakage Gotcha ===")

# Gotcha: Variables assigned via the walrus operator do NOT disappear outside their block 
# (unlike block scopes in languages like C++ or Java). They leak into the parent scope.

if (leaked_variable := "I am accessible outside the block!"):
    pass

print(f"-> Scope Check (Variable survived outside block): {leaked_variable}")