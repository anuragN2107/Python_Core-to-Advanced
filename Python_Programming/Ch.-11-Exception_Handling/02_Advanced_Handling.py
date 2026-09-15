# ===============================================================================================================================
#                               CHAPTER 2: ADVANCED EXCEPTION HANDLING (ELSE, FINALLY, RAISE, & CUSTOM)
# ===============================================================================================================================

# -------------------------------------------------------------------------------------------------------------------------------
# 1. THE ELSE AND FINALLY BLOCKS
# -------------------------------------------------------------------------------------------------------------------------------
# - `else`: Runs *only if* the `try` block succeeds without any errors.
# - `finally`: Runs *no matter what*—whether an error occurred or not. It is typically used for cleanup tasks (like closing files or database connections).
# -------------------------------------------------------------------------------------------------------------------------------

print("=== CHAPTER 2: ADVANCED EXCEPTION HANDLING ===")

print("\n--- Example 1: Using try, except, else, and finally ---")
try:
    x = 10 / 2  # Successful operation
except ZeroDivisionError:
    print("Error: Division by zero.")
else:
    print("Success! No exceptions occurred. Result is:", x)
finally:
    print("Cleanup: This block always executes, error or no error.")


# -------------------------------------------------------------------------------------------------------------------------------
# 2. THE RAISE KEYWORD (MANUALLY TRIGGERING EXCEPTIONS)
# -------------------------------------------------------------------------------------------------------------------------------
# You can use the `raise` keyword to force an exception to happen if a specific condition is met 
# (e.g., stopping a function if an invalid age or negative balance is provided).

print("\n--- Example 2: Using the 'raise' keyword ---")
def set_age(age):
    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120!")
    print(f"Age successfully set to {age}")

try:
    set_age(150)  # Will trigger our manual ValueError
except ValueError as error:
    print(f"[Caught Custom Raise]: {error}")


# -------------------------------------------------------------------------------------------------------------------------------
# 3. CREATING CUSTOM / USER-DEFINED EXCEPTIONS
# -------------------------------------------------------------------------------------------------------------------------------
# You can create your own specialized error types by making a new class that inherits from Python's built-in `Exception` class.
#
# Syntax Template:
#   class CustomErrorName(Exception):
#       pass

print("\n--- Example 3: User-Defined Custom Exception ---")

# Defining a custom exception class
class InsufficientFundsError(Exception):
    """Raised when an account withdrawal exceeds the available balance."""
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            # Raising our custom exception with a helpful error message
            raise InsufficientFundsError(f"Attempted to withdraw ${amount}, but balance is only ${self.balance}.")
        self.balance -= amount
        print(f"Successfully withdrew ${amount}. Remaining balance: ${self.balance}")

# Testing the custom exception
my_account = BankAccount(100)

try:
    my_account.withdraw(50)   # Valid withdrawal
    my_account.withdraw(200)  # Invalid withdrawal -> Triggers InsufficientFundsError
except InsufficientFundsError as custom_err:
    print(f"[Financial Alert Caught]: {custom_err}")