# ==============================================================================
#              PYTHON BASICS: USER INPUT & BASE CONVERSIONS
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. WHAT IS THE input() FUNCTION?
# ------------------------------------------------------------------------------
# The input() function pauses execution and waits for the user to type input.
#
# CRITICAL RULE:
# input() ALWAYS returns data as a string (str), regardless of what is typed.
# You must explicitly convert (typecast) it if you need numeric values.

name = input("Enter your name: ")
print("Hello, " + name + "!")
print("Type of input:", type(name))  # Output: <class 'str'>


# ------------------------------------------------------------------------------
# 2. STRING CONCATENATION VS. NUMERIC ADDITION
# ------------------------------------------------------------------------------
# Example: What happens without type conversion?

p = input("Enter number 1: ")  # User enters: 5  -> p = "5"
q = input("Enter number 2: ")  # User enters: 10 -> q = "10"

print("Number 1 is:", p)
print("Number 2 is:", q)

# Without conversion: `+` concatenates strings ("5" + "10" = "510")
print("Before conversion (String concat):", p + q)  # Output: 510

# After conversion: `+` performs mathematical addition (5 + 10 = 15)
p = int(p)
q = int(q)
print("After conversion (Math addition):  ", p + q)  # Output: 15


# ------------------------------------------------------------------------------
# 3. DIRECT TYPECASTING ON INPUT (STANDARD PRACTICE)
# ------------------------------------------------------------------------------
# Wrap input() directly inside int() or float() for clean, readable code.

# Integer input
num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))
print("Integer Sum:", num1 + num2)

# Float (decimal) input
r = float(input("Enter a decimal number 1: "))  # e.g., 5.0
s = float(input("Enter a decimal number 2: "))  # e.g., 14.0
print("Float Sum:", r + s)                     # Output: 19.0


# ------------------------------------------------------------------------------
# 4. ADVANCED int() CONVERSION: NUMBER SYSTEM BASES
# ------------------------------------------------------------------------------
# Syntax: int(string_value, base)
# Converts a string representation of a number in a given base to base-10 (decimal).

# --- Hexadecimal (Base 16: digits 0-9, A-F) ---
# "FF" in base 16 = (15 * 16^1) + (15 * 16^0) = 240 + 15 = 255
hex_val = int("FF", 16)
print("Hex 'FF' to decimal:", hex_val)  # Output: 255

# --- Octal (Base 8: digits 0-7) ---
# "20" in base 8 = (2 * 8^1) + (0 * 8^0) = 16 + 0 = 16
oct_val_1 = int("20", 8)
print("Octal '20' to decimal:", oct_val_1)  # Output: 16

# "100" in base 8 = (1 * 8^2) + (0 * 8^1) + (0 * 8^0) = 64 + 0 + 0 = 64
oct_val_2 = int("100", 8)
print("Octal '100' to decimal:", oct_val_2)  # Output: 64

# --- Binary (Base 2: digits 0-1) ---
# "100" in base 2 = (1 * 2^2) + (0 * 2^1) + (0 * 2^0) = 4 + 0 + 0 = 4
bin_val = int("100", 2)
print("Binary '100' to decimal:", bin_val)  # Output: 4

# NOTE ON BASE 2 ERROR:
# int("FF", 2) will raise a ValueError because 'F' is NOT a valid binary digit (0 or 1).


# ------------------------------------------------------------------------------
# 5. TAKING MULTIPLE INPUTS ON A SINGLE LINE
# ------------------------------------------------------------------------------
# Use .split() and map() to capture multiple inputs from one line of input.

# Example: Read two integers separated by space (e.g., user types "10 20")
# x, y = map(int, input("Enter two numbers separated by space: ").split())
# print(f"x: {x}, y: {y}, Sum: {x + y}")


# ------------------------------------------------------------------------------
# 6. SAFE INPUT HANDLING (PREVENTING CRASHES)
# ------------------------------------------------------------------------------
# If a user enters "hello" when int() is expected, Python raises a ValueError.
# Use try-except to handle unexpected input gracefully:

user_entry = input("Enter an integer safely: ")
try:
    valid_int = int(user_entry)
    print("Valid integer entered:", valid_int)
except ValueError:
    print(f"Error: '{user_entry}' cannot be converted to an integer!")
# ==============================================================================