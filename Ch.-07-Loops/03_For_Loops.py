# ==============================================================================
#                 PYTHON BASICS: FOR LOOPS & RANGE() REFERENCE
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. WHAT IS A FOR LOOP?
# ------------------------------------------------------------------------------
# A for loop in Python is used to iterate over a sequence (list, tuple, string,
# dictionary, set, or range) and execute a block of code for each element.
#
# Syntax:
#   for variable in sequence:
#       statement(s)


# ------------------------------------------------------------------------------
# 2. ITERATING OVER SEQUENCES & DATA STRUCTURES
# ------------------------------------------------------------------------------

# --- A. Iterating over a List ---
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry

# Iterating over a mixed data-type list:
items = ["apple", "banana", "cherry", 1, False, "Dog"]
for item in items:
    print(item)

# --- B. Iterating over a String ---
for char in "Python":
    print(char)
# Output:
# P
# y
# t
# h
# o
# n

# Another String Example:
name = "Anurag"
for n in name:
    print(n)

# --- C. Iterating over a Tuple ---
numbers_tuple = (10, 20, 30)
for num in numbers_tuple:
    print(num)

# --- D. Iterating over a Dictionary ---
user = {"name": "Anurag", "role": "Developer"}
for key, value in user.items():
    print(f"{key} -> {value}")


# ------------------------------------------------------------------------------
# 3. THE `range()` FUNCTION
# ------------------------------------------------------------------------------
# `range()` is a built-in immutable sequence type that generates numbers on demand.
#
# Syntax Variations:
# 1. range(stop)              : Starts at 0, ends at (stop - 1), step = 1
# 2. range(start, stop)       : Starts at 'start', ends at (stop - 1), step = 1
# 3. range(start, stop, step) : Starts at 'start', increments by 'step'

# Example 1: range(stop)
print("--- range(5) ---")
for i in range(5):
    print(i)  # Prints: 0, 1, 2, 3, 4

# Example 2: range(start, stop)
print("--- range(0, 5) ---")
for i in range(0, 5):
    print(i)  # Prints: 0, 1, 2, 3, 4

# Example 3: range(start, stop, step) - Step increment
print("--- range(0, 5, 2) ---")
for i in range(0, 5, 2):
    print(i)  # Prints: 0, 2, 4

# Example 4: Negative Step (Reverse Counting)
print("--- range(5, 0, -1) ---")
for i in range(5, 0, -1):
    print(i)  # Prints: 5, 4, 3, 2, 1


# ------------------------------------------------------------------------------
# 4. FOR LOOP WITH `else` BLOCK (PYTHON SPECIFIC FEATURE)
# ------------------------------------------------------------------------------
# The `else` block executes ONLY if the for loop finishes all iterations naturally.
# If the loop is terminated early with a `break` statement, the `else` block is SKIPPED.

# Case 1: Normal loop completion (else runs)
for i in range(5):
    print(i)
else:
    print("Loop completed successfully")
# Output:
# 0
# 1
# 2
# 3
# 4
# Loop completed successfully

# Case 2: Early termination via `break` (else is skipped)
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("This will NOT print because loop was broken early.")


# ------------------------------------------------------------------------------
# 5. BONUS ESSENTIAL LOOP HELPER: `enumerate()`
# ------------------------------------------------------------------------------
# `enumerate()` yields both the index and value simultaneously while iterating.

colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"Index {index}: {color}")
# Output:
# Index 0: red
# Index 1: green
# Index 2: blue
# ==============================================================================