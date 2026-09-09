# ==============================================================================
#                  FUNCTION CONTROL FLOW (PRINT vs. RETURN)
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. SUMMARY COMPARISON CHEAT SHEET
# ------------------------------------------------------------------------------
# | Feature       | print()                                | return                                 |
# |---------------|----------------------------------------|----------------------------------------|
# | Primary Goal  | Outputs text/data to console screen    | Passes value back to caller            |
# | Function Exit | Does NOT exit; continues execution     | Exits function IMMEDIATELY             |
# | Return Value  | Returns `None` implicitly              | Returns specified object/expression    |
# | Reusability   | Cannot be chained or stored in memory  | Result can be stored, passed, or saved |


# ------------------------------------------------------------------------------
# 2. THE `print()` TRAP: STORING RESULTS FAILS
# ------------------------------------------------------------------------------
def add_with_print(x, y):
    print(f"Result inside function: {x + y}")

print("--- 2. The print() Trap ---")
saved_val = add_with_print(5, 10)  # Prints: Result inside function: 15
print(f"Stored Variable Value: {saved_val}")  # Prints: None

# Attempting arithmetic on a printed function result crashes:
# total = saved_val + 5  # Raises TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'


# ------------------------------------------------------------------------------
# 3. THE `return` POWER: STORING & REUSING RESULTS
# ------------------------------------------------------------------------------
def add_with_return(x, y):
    return x + y  # Passes computation back to caller and exits

print("\n--- 3. Capturing and Chaining return Values ---")
total = add_with_return(5, 10)       # Captures integer 15 into variable 'total'
final_bill = total * 1.18            # Reusable in downstream calculations
print(f"Final Bill with Tax: {final_bill:.2f}")  # Output: 17.70


# ------------------------------------------------------------------------------
# 4. BEHAVIOR INSIDE LOOPS: `print()` vs `return`
# ------------------------------------------------------------------------------

# A. print() executes on EVERY iteration without interrupting the loop:
print("\n--- 4A. print() inside a Loop ---")
def count_with_print():
    for i in range(1, 4):
        print(f"Count: {i}")

count_with_print()
# Output:
# Count: 1
# Count: 2
# Count: 3


# B. return TERMINATES the function immediately on the FIRST encounter:
print("\n--- 4B. return inside a Loop ---")
def count_with_return():
    for i in range(1, 4):
        return f"Count: {i}"  # Immediately exits the function on i = 1

print(count_with_return())  # Output: Count: 1


# ------------------------------------------------------------------------------
# 5. RETURNING MULTIPLE VALUES (TUPLE UNPACKING)
# ------------------------------------------------------------------------------
# Python functions can return multiple values separated by commas, packaged as a tuple.

def get_min_max(numbers):
    """Returns minimum and maximum elements simultaneously."""
    return min(numbers), max(numbers)

min_val, max_val = get_min_max([12, 45, 2, 89, 34])  # Unpacking tuple
print(f"\nMinimum: {min_val}, Maximum: {max_val}")     # Output: Minimum: 2, Maximum: 89


# ------------------------------------------------------------------------------
# 6. EARLY EXIT / GUARD CLAUSES (CLEAN CODE PATTERN)
# ------------------------------------------------------------------------------
# `return` without an expression returns `None` and acts as a quick guard clause.

def process_age(age):
    if age < 0:
        print("Invalid age entered.")
        return  # Early exit stops further execution
    
    print(f"Processing valid age: {age}")

process_age(-5)  # Triggers early exit
process_age(21)  # Continues normally
# ==============================================================================