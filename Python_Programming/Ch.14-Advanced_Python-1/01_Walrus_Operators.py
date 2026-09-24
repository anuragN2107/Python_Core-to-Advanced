# ===============================================================================================================================
#                                       MASTER NOTES: THE WALRUS OPERATOR (:=) IN PYTHON
# ===============================================================================================================================

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

simulated_inputs = iter(["hello", "python", "quit"])  # Set up simulated user inputs using an iterator so the code runs automatically

def mock_input(prompt): 
    return next(simulated_inputs)  # Define a fake input function that automatically grabs the next simulated item

#  The Walrus Loop: Assigns the input to 'user_input' and checks if it's "quit" all at once
while (user_input := mock_input("Enter text: ")) != "quit":
    print(f"-> Processed input: {user_input}")    # This runs only if user_input is NOT "quit"

print("Loop exited successfully!\n") #This runs after the loop safely exits

#Output:
# -> Processed input: hello
# -> Processed input: python
# Loop exited successfully!

# ===============================================================================================================================
# STEP 5: USE CASE 2 - AVOIDING REDUNDANT FUNCTION CALLS IN `if` STATEMENTS
# ===============================================================================================================================
print("=== DEMO 2: If Statement Redundancy Reduction ===")

# Simulates fetching a database list (returns a list of 5 items)
def fetch_data():
    return [100, 200, 300, 400, 500]

# Calculates length, saves it to 'count', and checks if it's > 3 all in one step
if (count := len(fetch_data())) > 3:
    # 'count' is safely stored and can be reused inside the print statement
    print(f"-> Warning: Large dataset detected with {count} items!\n")
else:
    print("-> No large dataset detected.\n")

#Output:
# -> Warning: Large dataset detected with 5 items!


# ===============================================================================================================================
# STEP 6: USE CASE 3 - OPTIMIZING LIST COMPREHENSIONS
# ===============================================================================================================================
print("=== DEMO 3: List Comprehension Optimization ===")

# Simulates a heavy calculation (squaring a number)
def expensive_operation(x):
    return x ** 2

# Loops 0 to 7. Computes once, saves it to 'y', checks if y > 20, and builds the list.
results = [y for x in range(8) if (y := expensive_operation(x)) > 20]

print(f"-> Filtered results (> 20): {results}\n")

#Output:
#-> Filtered results (> 20): [25, 36, 49]


# ===============================================================================================================================
# STEP 7: REAL-WORLD EXAMPLE (Regex Log Parsing)
# ===============================================================================================================================
import re

# The text string to analyze
log_message = "CRITICAL_ERROR: Code 503 encountered during server sync."

# Regex pattern: matches "Code", spaces (\s+), and captures digits (\d+)
error_pattern = r"Code\s+(\d+)"

# Simultaneously searches the text and assigns the result to 'match'
if match := re.search(error_pattern, log_message):
    # Retrieve the numbers saved inside the first capture group ()
    error_code = match.group(1)
    print(f"-> Alert! Caught error code number: {error_code}\n")
else:
    print("-> Log file is clean.\n")
#Output:
# -> Alert! Caught error code number: 503

# ===============================================================================================================================
# STEP 8: EXCEPTIONS, LIMITATIONS, & GOTCHAS
# ===============================================================================================================================
print("=== DEMO 5: Variable Scope Leakage Gotcha ===")

# Assigns value and evaluates the condition simultaneously
if (leaked_variable := "I am accessible outside the block!"):
    pass  # 'pass' does nothing, acting as a temporary placeholder

# Python has no block scope; variables created in an 'if' statement survive outside it
print(f"-> Scope Check (Variable survived outside block): {leaked_variable}")

#Output:
#-> Scope Check (Variable survived outside block): I am accessible outside the block!