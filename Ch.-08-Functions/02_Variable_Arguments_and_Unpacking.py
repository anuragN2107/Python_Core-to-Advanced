# ==============================================================================
#                 CHAPTER 8: ARBITRARY ARGUMENTS (*args & **kwargs)
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. WHAT ARE *args AND **kwargs?
# ------------------------------------------------------------------------------
# They allow a function to accept a dynamic/variable number of arguments when
# you do not know beforehand how many inputs will be passed.
#
# Quick Rule of Thumb:
# - *args   : Packs extra positional arguments into a TUPLE.
# - **kwargs: Packs extra keyword arguments (key=value) into a DICTIONARY.
#
# Note: The words 'args' and 'kwargs' are conventions (PEP 8). The asterisks
# (* and **) are what actually define the variable-length behavior.


# ------------------------------------------------------------------------------
# 2. `*args` (VARIABLE POSITIONAL ARGUMENTS)
# ------------------------------------------------------------------------------
# Collects any number of positional arguments into a single tuple.

def sum_numbers(*args):
    """Sums all numbers passed as arbitrary positional arguments."""
    # args behaves as a tuple: (1, 2, 3, 4, 5)
    total = 0
    for num in args:
        total += num
    return total

print("--- 1. *args Examples ---")
print("Sum (2 numbers):", sum_numbers(1, 2))              # Output: 3
print("Sum (5 numbers):", sum_numbers(1, 2, 3, 4, 5))     # Output: 15
print("Sum (0 numbers):", sum_numbers())                  # Output: 0
print()


# ------------------------------------------------------------------------------
# 3. `**kwargs` (VARIABLE KEYWORD ARGUMENTS)
# ------------------------------------------------------------------------------
# Collects any number of named arguments (key=value) into a single dictionary.

def print_user_profile(**kwargs):
    """Prints arbitrary key-value details of a user."""
    # kwargs behaves as a dictionary: {"name": "Sara", "role": "Admin", ...}
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("--- 2. **kwargs Example ---")
print_user_profile(name="Sara", role="Admin", country="Canada")
# Output:
#   name: Sara
#   role: Admin
#   country: Canada
print()


# ------------------------------------------------------------------------------
# 4. STRICT PARAMETER ORDERING RULE
# ------------------------------------------------------------------------------
# When mixing argument types in a function signature, you MUST follow this exact order:
#   1. Standard positional parameters
#   2. *args
#   3. Default / Keyword-only parameters
#   4. **kwargs

def log_event(event_type, *tags, level="INFO", **details):
    """Demonstrates combining positional, *args, default, and **kwargs."""
    print(f"[{level}] Event: {event_type}")
    print(f"  Tags:    {tags}")
    print(f"  Details: {details}")

print("--- 3. Combined Signature Example ---")
log_event(
    "User_Login",
    "auth", "security",              # Captured by *tags as a tuple
    level="WARNING",                 # Overrides default 'level' parameter
    user_id=101, ip="192.168.1.1"    # Captured by **details as a dict
)
# Output:
# [WARNING] Event: User_Login
#   Tags:    ('auth', 'security')
#   Details: {'user_id': 101, 'ip': '192.168.1.1'}
print()


# ------------------------------------------------------------------------------
# 5. UNPACKING COLLECTIONS USING `*` AND `**`
# ------------------------------------------------------------------------------
# Asterisks can also be used during the FUNCTION CALL to unpack iterables:
# - `*iterable` : Unpacks elements of a list/tuple into separate positional args.
# - `**dict`     : Unpacks key-value pairs of a dictionary into keyword args.

def describe_pet(name, animal_type, age):
    print(f"{name} is a {age}-year-old {animal_type}.")

print("--- 4. Unpacking Collections Example ---")

# Unpacking a List / Tuple with *
pet_list = ["Buddy", "Dog", 5]
describe_pet(*pet_list)  # Equivalent to: describe_pet("Buddy", "Dog", 5)
# Output: Buddy is a 5-year-old Dog.

# Unpacking a Dictionary with **
pet_dict = {"name": "Milo", "animal_type": "Cat", "age": 3}
describe_pet(**pet_dict)  # Equivalent to: describe_pet(name="Milo", animal_type="Cat", age=3)
# Output: Milo is a 3-year-old Cat.
# ==============================================================================