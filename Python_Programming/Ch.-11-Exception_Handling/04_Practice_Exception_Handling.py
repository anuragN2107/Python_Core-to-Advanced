# ===============================================================================================================================
#                                       EXCEPTION HANDLING: PRACTICE SET 
# ===============================================================================================================================


# ===============================================================================================================================
# PRACTICE QUESTION 1: Basic try-except (ZeroDivisionError & ValueError)
# Question: Ask the user for two numbers, divide them, and handle zero division and conversion errors.
# ===============================================================================================================================

print("--- Practice 1 Solution ---")
try:
    num1 = float(input("Enter numerator: "))
    num2 = float(input("Enter denominator: "))
    result = num1 / num2
    print(f"Result: {result}")
except ZeroDivisionError:
    print("[Error]: You cannot divide by zero!")
except ValueError:
    print("[Error]: Please enter valid numerical values.")
print()


# ===============================================================================================================================
# PRACTICE QUESTION 2: else and finally blocks
# Question: Convert a string to int, use an 'else' block to print its square, and a 'finally' block for cleanup.
# ===============================================================================================================================

print("--- Practice 2 Solution ---")
try:
    val = int("100")
except ValueError:
    print("Conversion failed.")
else:
    square = val ** 2
    print(f"Success! Square of {val} is {square}")
finally:
    print("Execution Complete")
print()


# ===============================================================================================================================
# PRACTICE QUESTION 3: Using the raise keyword
# Question: Write a function that raises a ValueError if a password has fewer than 6 characters.
# ===============================================================================================================================

print("--- Practice 3 Solution ---")
def check_password_length(password):
    if len(password) < 6:
        raise ValueError("Password must be at least 6 characters long.")
    print("Password is valid.")

try:
    check_password_length("abc")
except ValueError as e:
    print(f"[Caught Exception]: {e}")
print()


# ===============================================================================================================================
# PRACTICE QUESTION 4: Custom Exception Class
# Question: Create a custom exception class 'InvalidAgeError' and raise it if age < 18.
# ===============================================================================================================================

print("--- Practice 4 Solution ---")

class InvalidAgeError(Exception):
    """Custom exception raised for invalid voting ages."""
    pass

def validate_voting_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older to vote.")
    print("Eligible to vote!")

try:
    validate_voting_age(15)
except InvalidAgeError as err:
    print(f"[Custom Error Caught]: {err}")
print()


# ===============================================================================================================================
# PRACTICE QUESTION 5: Context Manager / with statement for Files
# Question: Safely read a file using the 'with' statement and handle the case where it doesn't exist.
# ===============================================================================================================================

print("--- Practice 5 Solution ---")

try:
    # Using 'with' ensures resource cleanup (closing the file) automatically
    with open("notes.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("[Error]: The file 'notes.txt' was not found. Cleanup handled automatically.")
print()


# ===============================================================================================================================
# PRACTICE QUESTION 6: Custom Context Manager Class
# Question: Build a custom context manager class 'Timer' with __enter__ and __exit__ methods.
# ===============================================================================================================================

print("--- Practice 6 Solution ---")

class Timer:
    def __enter__(self):
        print("Timer Started...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Timer Stopped.")
        return False  # Let exceptions pass through normally if any occur

# Testing the custom context manager
with Timer():
    print("Executing code block inside context manager...")