# ==============================================================================
#                 CHAPTER 8: PRACTICE SET (FUNCTIONS & RECURSION)
# ==============================================================================

# ------------------------------------------------------------------------------
# Problem 1: Find the greatest of three numbers using a function
# ------------------------------------------------------------------------------
# Approach A: Using built-in max()
def find_greatest1(a, b, c):
    return max(a, b, c)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

greatest = find_greatest1(num1, num2, num3)
print(f"The greatest number is: {greatest}")

# Approach B: Using conditional logic
def find_greatest2(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

greatest2 = find_greatest2(num1, num2, num3)
print(f"The greatest number is: {greatest2}")


# ------------------------------------------------------------------------------
# Problem 2: Temperature conversion functions
# ------------------------------------------------------------------------------
# (a) Celsius to Fahrenheit: (9 * C / 5) + 32
def cel_to_far(cel):
    return (9 * cel / 5) + 32

cel = float(input("Enter the temperature in Celsius: "))
far = cel_to_far(cel)
print(f"Temperature in Fahrenheit: {far}°F")

# (b) Fahrenheit to Celsius: (5 / 9) * (F - 32)
def far_to_cel(far):
    return (5 * (far - 32)) / 9

far_val = float(input("Enter the temperature in Fahrenheit: "))
cel_val = far_to_cel(far_val)
print(f"Temperature in Celsius: {cel_val:.2f}°C")


# ------------------------------------------------------------------------------
# Problem 3: Prevent print() from adding a newline
# ------------------------------------------------------------------------------
# By using the parameter end=" ", we replace the default newline '\n' with a space.
print("Hello", end=" ")
print("World", end=" ")
print("Get ready to fight!")
print("Are You Ready?")


# ------------------------------------------------------------------------------
# Problem 4: Recursive function to calculate sum of first n natural numbers
# ------------------------------------------------------------------------------
# Mathematical Rule: sum(n) = n + sum(n - 1) | Base Case: sum(1) = 1
def sum_natural(n):
    if n <= 1:  # Base case
        return n
    return n + sum_natural(n - 1)  # Recursive case

n = int(input("Enter a positive integer: "))

if n < 1:
    print("Please enter a positive natural number.")
else:
    result = sum_natural(n)
    print(f"The sum of the first {n} natural numbers is: {result}")


# ------------------------------------------------------------------------------
# Problem 5: Recursive functions to print star / hash patterns
# ------------------------------------------------------------------------------
# Pattern A: Inverted Triangle (n down to 1)
# ***
# **
# *
def pattern_inverted(n):
    if n == 0:
        return  # Base case: stop recursion when row size reaches 0
    print("*" * n)  # Print current row with 'n' stars
    pattern_inverted(n - 1)  # Recursive call: shrink star count by 1 for next row

n = int(input("Enter a number: "))
pattern_inverted(n)

# Pattern B: Upright Triangle using an accumulator parameter (1 up to target)
# #
# ##
# ###
def pattern_forward(target, current=1):
    if current > target:
        return  # Base case: stop when current row exceeds target
    print("#" * current)  # Print '#' matching current row count
    pattern_forward(target, current + 1)  # Recursive call: step up by 1

pattern_forward(n)

# Pattern C: Upright Triangle using unwinding call stack
# #
# ##
# ###
def pattern_unwinding(n):
    if n == 0:
        return  # Base case: dive down to 0 first
    pattern_unwinding(n - 1)  # Dive deeper before printing
    print("#" * n)  # Prints upon unwinding: 1, then 2, ..., up to n

pattern_unwinding(n)


# ------------------------------------------------------------------------------
# Problem 6: Convert inches to centimeters
# ------------------------------------------------------------------------------
# Formula: 1 inch = 2.54 cm
def inches_to_cm(inches):
    return inches * 2.54

inches = float(input("Enter length in inches: "))
cm = inches_to_cm(inches)
print(f"{inches} inches = {cm:.2f} cm")


# ------------------------------------------------------------------------------
# Problem 7: Remove a word from a list and strip leading/trailing characters
# ------------------------------------------------------------------------------
def rem(lst, word):
    n = []  # Empty list to store processed items
    for item in lst:
        # Step 1: Skip item if it exactly equals the target word
        if item != word:
            # Step 2: Strip target substring from outer edges and append
            n.append(item.strip(word))
    return n

l = ["Harry", "Rohan", "Sohan", "Mohan", "Shubham", "an"]
print("Cleaned List:", rem(l, "an"))
# Output: ['Harry', 'Roh', 'Soh', 'Moh', 'Shubham']


# ------------------------------------------------------------------------------
# Problem 8: Function to print multiplication table of a given number
# ------------------------------------------------------------------------------
def mult_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

num = int(input("Enter a number: "))
mult_table(num)


# ==============================================================================
# APPENDIX: WHY USE `print()` INSTEAD OF `return` INSIDE A LOOP?
# ==============================================================================
# 1. `return` exits the function immediately.
#    If you write `return f"{n} * {i} = {n * i}"` inside a loop, the function
#    runs for i = 1, returns the single line, and instantly terminates.
#    Iterations 2 through 10 will never execute.
#
# 2. `print()` displays each line to standard output without stopping the loop,
#    allowing the loop to complete all cycles from 1 to 10.
# ==============================================================================