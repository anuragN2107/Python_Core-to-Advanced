# ==============================================================================
#                 PYTHON BASICS: LOOP CONTROL STATEMENTS
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. SUMMARY CHEAT SHEET: BREAK vs CONTINUE vs PASS
# ------------------------------------------------------------------------------
# | Statement  | Action                                    | Loop Behavior       |
# |------------|-------------------------------------------|---------------------|
# | break      | Exits the entire loop immediately         | Loop stops          |
# | continue   | Skips current iteration and moves to next | Loop keeps running  |
# | pass       | Does nothing (syntactic placeholder)      | Loop runs unaffected|


# ------------------------------------------------------------------------------
# 2. THE `break` STATEMENT
# ------------------------------------------------------------------------------
# Terminates the enclosing loop entirely when a condition is met.
# Code execution jumps straight to the first line outside the loop.

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        break  # Loop terminates when fruit is "banana"
    print(fruit)

# Output:
# apple

# Exercise with String:
name = "Anurag"
for n in name:
    if n == "u":
        break  # Stops when reaching 'u'
    print(n)

# Output:
# A
# n


# ------------------------------------------------------------------------------
# 3. THE `continue` STATEMENT
# ------------------------------------------------------------------------------
# Skips the remaining code inside the current iteration and jumps directly
# to the next cycle of the loop.

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        continue  # Skips printing "banana" and moves to "cherry"
    print(fruit)

# Output:
# apple
# cherry

for num in range(1, 6):
    if num == 3:
        continue  # Skips number 3
    print(num)

print("Loop ended")
# Output:
# 1
# 2
# 4
# 5
# Loop ended


# ------------------------------------------------------------------------------
# 4. THE `pass` STATEMENT
# ------------------------------------------------------------------------------
# A null operation (placeholder). Used when Python syntax requires a code block,
# but no actual action needs to be performed yet (prevents IndentationError).

for num in range(1, 6):
    if num == 3:
        pass  # Placeholder: do nothing and continue regular execution
    print(num)

# Output:
# 1
# 2
# 3
# 4
# 5

# Common use cases for `pass`:
# 1. Empty functions to implement later:
def calculate_tax():
    pass

# 2. Empty class definitions:
class CustomUserError(Exception):
    pass


# ------------------------------------------------------------------------------
# 5. `break` WITH NESTED LOOPS
# ------------------------------------------------------------------------------
# `break` terminates ONLY the innermost loop it belongs to; the outer loop continues.

for outer in range(1, 4):
    for inner in range(1, 4):
        if inner == 2:
            break  # Exits only the inner loop
        print(f"outer={outer}, inner={inner}")

# Output:
# outer=1, inner=1
# outer=2, inner=1
# outer=3, inner=1
# ==============================================================================