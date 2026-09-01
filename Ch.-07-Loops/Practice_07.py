# ==============================================================================
#                 CHAPTER 7: PRACTICE SET (LOOPS & PATTERNS)
# ==============================================================================

# ------------------------------------------------------------------------------
# Problem 1: Multiplication table of a given number using a FOR loop
# ------------------------------------------------------------------------------
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} * {i} = {n * i}")


# ------------------------------------------------------------------------------
# Problem 2: Filtering names in a list
# ------------------------------------------------------------------------------
# Note:
# - startswith() checks if the string starts with the given substring.
# - endswith() checks if the string ends with the given substring.
# - lower() converts the string to lowercase to make the check case-insensitive.

# (i) Greet names in list 'l' that start with 'S'
l = ["Harry", "Soham", "Sachin", "Rahul", "Shalu"]
for name in l:
    if name.startswith("S"):
        print(f"Hello {name}")

# (ii) Greet names in list 'l2' that end with 'y' (Case-insensitive)
l2 = ["Harry", "Soham", "Sachin", "Rahul", "Shalu", "Vicky", "Nicky", "LuckY"]
for name in l2:
    if name.lower().endswith("y"):
        print(f"Hello {name}")


# ------------------------------------------------------------------------------
# Problem 3: Multiplication table using a WHILE loop
# ------------------------------------------------------------------------------
n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{n} * {i} = {n * i}")
    i += 1


# ------------------------------------------------------------------------------
# Problem 4: Check if a number is Prime or not
# ------------------------------------------------------------------------------
# Mathematical Note: Prime numbers must be > 1. Negative numbers, 0, and 1 are not prime.

# Method A: Using FOR-ELSE loop
num = int(input("Enter a number: "))
if num <= 1:
    print(f"{num} is not a prime number.")
else:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break  # Stops loop immediately since a factor was found
    else:
        print(f"{num} is a prime number.")

# Method B: Using WHILE loop
num = int(input("Enter a number: "))
if num <= 1:
    print(f"{num} is not a prime number.")
else:
    i = 2
    while i < num:
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
        i += 1
    else:
        print(f"{num} is a prime number.")


# ------------------------------------------------------------------------------
# Problem 5: Sum of first n natural numbers using a WHILE loop
# ------------------------------------------------------------------------------
# Approach 1: Iterative accumulation
n = int(input("Enter a number: "))
total_sum = 0
i = 1
while i <= n:
    total_sum += i
    i += 1
print(f"The sum of first {n} natural numbers is: {total_sum}")

# Approach 2: Direct formula verification [n * (n + 1) // 2]
# print(f"Formula check: {n * (n + 1) // 2}")


# ------------------------------------------------------------------------------
# Problem 6: Factorial of a given number
# ------------------------------------------------------------------------------

# Method A: Using WHILE loop
num = int(input("Enter a number: "))
product = 1
i = 1
while i <= num:
    product *= i
    i += 1
print(f"The factorial of {num} is {product}.")

# Method B: Using FOR loop
num = int(input("Enter a number: "))
product = 1
for i in range(1, num + 1):
    product *= i
print(f"The factorial of {num} is {product}.")


# ------------------------------------------------------------------------------
# Problem 7: Centered Pyramid Star Pattern (for height n)
# ------------------------------------------------------------------------------
# Example for n = 3:
#   *
#  ***
# *****

n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")      # Leading spaces
    print("*" * (2 * i - 1), end="")  # Odd number of stars (1, 3, 5, ...)
    print("")                         # Moves to next line

# Explanation:
# - " " * (n - i) pushes stars right to keep the pyramid symmetrical and centered.
# - "*" * (2 * i - 1) calculates the count of stars for row i.
# - print("") provides a line break after each row.


# ------------------------------------------------------------------------------
# Problem 8: Hollow Square Star Pattern (for size n)
# ------------------------------------------------------------------------------
# Example for n = 3:
# ***
# * *
# ***

# Method A: Using FOR loop
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    if i == 1 or i == n:
        print("*" * n)  # Top and bottom rows are solid
    else:
        print("*" + " " * (n - 2) + "*")  # Boundary stars with hollow middle

# Method B: Using WHILE loop
n = int(input("Enter a number: "))
i = 1
while i <= n:
    if i == 1 or i == n:
        print("*" * n)
    else:
        print("*" + " " * (n - 2) + "*")
    i += 1


# ------------------------------------------------------------------------------
# Problem 9: Right-Angled Triangle Star Pattern
# ------------------------------------------------------------------------------
# Example for n = 3:
# *
# **
# ***

n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print("*" * i)


# ------------------------------------------------------------------------------
# Problem 10: Multiplication Table in Reversed Order (10 down to 1)
# ------------------------------------------------------------------------------

# Method A: Using step = -1 in range()
n = int(input("Enter a number: "))
for i in range(10, 0, -1):
    print(f"{n} * {i} = {n * i}")

# Method B: Using formula (11 - i)
# n = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{n} * {11 - i} = {n * (11 - i)}")


# ------------------------------------------------------------------------------
# APPENDIX: HOW `print()` AND `end` WORK
# ------------------------------------------------------------------------------
# - Default behavior: print() automatically appends a newline character (`\n`).
# - `end=" "`        : Overrides the newline, keeping the next output on the SAME line separated by space.
# - `end=""`         : Glues consecutive print outputs directly together without spaces.
# - `print("")`      : Prints an empty line (equivalent to pressing Enter).

# Demo:
for i in range(1, 4):
    print(i, end=" ")
print("")  # Moves cursor to the next line
print("Done!")
# Output:
# 1 2 3 
# Done!
# ==============================================================================
