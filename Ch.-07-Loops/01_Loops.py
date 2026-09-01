# ==============================================================================
#                      PYTHON BASICS: LOOPS 
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. WHAT ARE LOOPS?
# ------------------------------------------------------------------------------
# Loops are control flow structures used to execute a block of code repeatedly.
# They automate repetitive tasks without writing duplicate code.
#
# Python provides two primary loop types:
# 1. while loop : Condition-controlled loop (runs while a condition is True).
# 2. for loop   : Collection-controlled loop (iterates over items in a sequence).


# ------------------------------------------------------------------------------
# 2. THE `while` LOOP
# ------------------------------------------------------------------------------
# Executes a code block repeatedly as long as the test condition remains True.
#
# Syntax:
#   while condition:
#       statement(s)
#
# Three Critical Parts of a while loop:
# 1. Initialization : Set a starting value for the loop variable before the loop.
# 2. Condition      : Checked before every iteration; loop stops when False.
# 3. Update/Step    : Increment/decrement to avoid an infinite loop.

i = 0  # 1. Initialization
while i < 5:  # 2. Condition check
    print(i)
    i += 1  # 3. Update (Increment by 1)

print("Hello, World!")
# Output:
# 0
# 1
# 2
# 3
# 4
# Hello, World!


# ------------------------------------------------------------------------------
# 3. THE `for` LOOP & `range()` FUNCTION
# ------------------------------------------------------------------------------
# A for loop iterates directly over the items of any sequence (range, list,
# tuple, string, dictionary, or set).
#
# Syntax:
#   for variable in sequence:
#       statement(s)

# Example using range(stop): generates numbers from 0 up to (stop - 1)
for i in range(5):
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4

# range() Syntax Variations:
# - range(stop)             -> range(5)       : 0, 1, 2, 3, 4
# - range(start, stop)      -> range(1, 6)    : 1, 2, 3, 4, 5
# - range(start, stop, step)-> range(1, 10, 2): 1, 3, 5, 7, 9


# ------------------------------------------------------------------------------
# 4. ITERATING OVER DATA STRUCTURES WITH `for`
# ------------------------------------------------------------------------------

# Iterating over a List:
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

# Iterating over a String:
for char in "Code":
    print(char, end=" ")  # Output: C o d e
print()


# ------------------------------------------------------------------------------
# 5. LOOP CONTROL STATEMENTS: `break`, `continue`, `pass`
# ------------------------------------------------------------------------------

# 1. break: Terminates the loop immediately.
for num in range(1, 6):
    if num == 3:
        break
    print("break demo:", num)  # Prints 1, 2

# 2. continue: Skips the rest of the current iteration and jumps to the next.
for num in range(1, 6):
    if num == 3:
        continue
    print("continue demo:", num)  # Prints 1, 2, 4, 5

# 3. pass: Null statement / placeholder to avoid syntax errors.
for num in range(3):
    pass  # To be implemented later


# ------------------------------------------------------------------------------
# 6. `for-else` & `while-else` (PYTHON SPECIAL FEATURE)
# ------------------------------------------------------------------------------
# The `else` block runs ONLY when the loop finishes normally without hitting a `break`.

for n in range(3):
    print(n)
else:
    print("Loop completed successfully!")
# Output:
# 0
# 1
# 2
# Loop completed successfully!
# ==============================================================================