# ===============================================================================================================================
#                               CHAPTER 1: INTRODUCTION TO ERRORS, EXCEPTIONS, AND BASIC HANDLING
# ===============================================================================================================================

# -------------------------------------------------------------------------------------------------------------------------------
# 1. WHAT IS AN EXCEPTION? (CORE DEFINITION)
# -------------------------------------------------------------------------------------------------------------------------------
# - Error vs. Exception:
#   * Syntax Errors: Mistakes in the grammar of your code (e.g., missing a colon `:` or parenthesis). The program won't run at all.
#   * Exceptions: Errors that occur *during* the execution (runtime) of a program, even if the syntax is completely correct. 
#     For example: trying to divide a number by zero (`ZeroDivisionError`) or trying to open a file that doesn't exist (`FileNotFoundError`).
#
# - Why Do We Need Exception Handling?
#   If an exception occurs, Python normally crashes and stops the entire program immediately. 
#   Exception handling allows your program to "catch" the error gracefully, deal with it, and keep running instead of crashing.
# -------------------------------------------------------------------------------------------------------------------------------


# ===============================================================================================================================
# BASIC SYNTAX: TRY AND EXCEPT
# ===============================================================================================================================
# - `try` block: Place the code here that *might* cause an error.
# - `except` block: Place the fallback code here that runs *only if* an error happens in the try block.
#
# Syntax Template:
#   try:
#       # Risky code goes here
#   except ExceptionType:
#       # Recovery or fallback code goes here

print("=== CHAPTER 1: BASIC EXCEPTION HANDLING ===")

# Example: Handling a ZeroDivisionError
print("\n--- Example 1: Handling Division by Zero ---")
try:
    num = 10 / 0  # This will trigger a ZeroDivisionError
    print("This line will print only if no error occurs.")
except ZeroDivisionError:
    print("[Caught Error]: You cannot divide a number by zero!")

print("Program continues running safely past the error block.\n")


# Example: Handling Multiple / Specific Exceptions
print("--- Example 2: Handling Multiple Exception Types ---")
try:
    # User tries to convert a string to an integer, or divide
    user_input = "abc"
    result = int(user_input)
except ValueError:
    print("[Caught Error]: Invalid conversion! Please enter a valid number.")
except TypeError:
    print("[Caught Error]: Type mismatch error occurred.")