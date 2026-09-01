# ==============================================================================
#                 PYTHON BASICS: WHILE LOOPS REFERENCE
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. WHAT IS A WHILE LOOP?
# ------------------------------------------------------------------------------
# A while loop repeatedly executes a target block of code as long as a given
# condition evaluates to True.
#
# Execution Flow:
# 1. The condition is evaluated first (Entry-controlled loop).
# 2. If True, the code block runs.
# 3. If False, the loop terminates and moves to the next lines of code.
#
# Syntax:
#   while condition:
#       statement(s)


# ------------------------------------------------------------------------------
# 2. BASIC WHILE LOOP EXAMPLE
# ------------------------------------------------------------------------------
# Three essential components:
# 1. Initialization : Define and set starting value of the counter/variable.
# 2. Condition      : Evaluated before every iteration (stops when False).
# 3. Step/Update    : Increment/decrement variable to avoid infinite loops.

i = 0  # 1. Initializing variable
while i < 5:  # 2. Condition check
    print(i)
    i += 1  # 3. Incrementing i by 1 (i = i + 1)

print("Hello, World!")
# Output:
# 0
# 1
# 2
# 3
# 4
# Hello, World!


# ------------------------------------------------------------------------------
# 3. ITERATING OVER A LIST USING A WHILE LOOP
# ------------------------------------------------------------------------------
fruits = ["apple", "banana", "cherry", 1, False, "Dog"]  # len(fruits) = 6

i = 0  # Start at the first index (0)
while i < len(fruits):  # Runs while index is valid (0 to 5)
    print(fruits[i])
    i += 1  # Move to the next index

# Output:
# apple
# banana
# cherry
# 1
# False
# Dog


# ------------------------------------------------------------------------------
# 4. INFINITE LOOPS & HOW TO PREVENT THEM
# ------------------------------------------------------------------------------
# An infinite loop occurs when the condition NEVER becomes False.
# This usually happens when the update step (i += 1) is forgotten.

# Example of an intentional infinite loop with break:
count = 0
while True:
    print("Running count:", count)
    count += 1
    if count >= 3:
        break  # Safely exits the infinite loop


# ------------------------------------------------------------------------------
# 5. WHILE-ELSE BLOCK (PYTHON SPECIFIC FEATURE)
# ------------------------------------------------------------------------------
# The `else` block runs when the while condition becomes False naturally,
# but it is SKIPPED if the loop is terminated by a `break` statement.

n = 1
while n <= 3:
    print("Count:", n)
    n += 1
else:
    print("While loop finished successfully without break!")

# Output:
# Count: 1
# Count: 2
# Count: 3
# While loop finished successfully without break!
# ==============================================================================