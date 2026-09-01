# ==============================================================================
#                 CHAPTER 8: FUNCTIONS & ARGUMENTS 
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. WHAT IS A FUNCTION?
# ------------------------------------------------------------------------------
# A function is a reusable, named block of code that performs a specific task.
# It executes only when explicitly called (invoked).
#
# Key Advantages:
# - Reusability   : Write once, use multiple times (DRY: Don't Repeat Yourself).
# - Modularity     : Breaks large, complex logic into small, manageable units.
# - Maintainability: Fix bugs or update behavior in one central location.
#
# Syntax:
#   def function_name(parameters):
#       """Optional docstring explaining the function."""
#       statement(s)
#       return value
#
# Terminology:
# - def keyword  : Declares the start of a function definition.
# - Parameters   : Placeholder variables defined in the function signature.
# - Arguments    : Actual values/data passed into the function when calling it.
# - return       : Exits the function and passes a value back to the caller.
#                  (If omitted, the function returns None by default).


# ------------------------------------------------------------------------------
# 2. CORE EXAMPLES: PRINT vs RETURN
# ------------------------------------------------------------------------------

# --- Example A: Function that Prints (No Return Value) ---
def greet(name):
    """Prints a greeting message for the given name."""
    print(f"Hello, {name}!")

# Calling the function multiple times:
greet("Alice")    # Output: Hello, Alice!
greet("Bob")      # Output: Hello, Bob!
greet("Charlie")  # Output: Hello, Charlie!


# --- Example B: Function that Returns a Value (Best Practice) ---
def get_goodday_message(name):
    """Returns a greeting string so it can be saved or reused."""
    return f"Goodday, {name}!"

# Storing and printing the returned value:
greeting_text = get_goodday_message("Sara")
print(greeting_text)  # Output: Goodday, Sara!


# --- Example C: Multiple Parameters ---
def greet_user_fullname(first_name, last_name):
    """Combines first and last names into a polite greeting."""
    return f"Hey! {first_name} {last_name}, have a nice day."

print(greet_user_fullname("John", "Doe"))  # Output: Hey! John Doe, have a nice day.


# --- Example D: Mathematical Calculation ---
def calculate_average(a, b, c, d, e):
    """Calculates and returns the arithmetic mean of 5 numbers."""
    return (a + b + c + d + e) / 5

result_avg = calculate_average(10, 20, 30, 40, 50)
print(f"Average: {result_avg}")  # Output: Average: 30.0


# ------------------------------------------------------------------------------
# 3. TYPES OF ARGUMENTS
# ------------------------------------------------------------------------------

# 1. Positional Arguments:
# Matched strictly by the order in which they are passed.
def make_coffee_positional(size, roast):
    print(f"Brewing a {size} cup of {roast} roast.")

make_coffee_positional("Large", "Dark")
# Output: Brewing a Large cup of Dark roast.


# 2. Default / Optional Arguments:
# Provides a fallback value if the argument is omitted during the function call.
# RULE: Non-default parameters MUST come before default parameters!
# Valid:   def fn(a, b=2):
# Invalid: def fn(a=1, b):  -> SyntaxError
def make_coffee_default(size, roast="Medium"):
    print(f"Brewing a {size} cup of {roast} roast.")

make_coffee_default("Small")          # Uses default roast -> 'Medium'
make_coffee_default("Large", "Dark")  # Overrides default  -> 'Dark'


# 3. Keyword / Named Arguments:
# Passed explicitly using `name=value`. Order does not matter.
def make_coffee_keyword(size, roast):
    print(f"Brewing a {size} cup of {roast} roast.")

make_coffee_keyword(roast="Light", size="Medium")
# Output: Brewing a Medium cup of Light roast.


# ------------------------------------------------------------------------------
# 4. INTERACTIVE EXAMPLES (Terminal Input)
# ------------------------------------------------------------------------------

def run_interactive_prompts():
    # Prompt 1: Single argument
    user_name = input("Enter your name: ")
    print(get_goodday_message(user_name))

    # Prompt 2: Two arguments
    user_first = input("Enter your first name: ")
    user_last = input("Enter your last name: ")
    print(greet_user_fullname(user_first, user_last))

    # Prompt 3: Average calculation
    n1 = int(input("Enter number 1: "))
    n2 = int(input("Enter number 2: "))
    n3 = int(input("Enter number 3: "))
    n4 = int(input("Enter number 4: "))
    n5 = int(input("Enter number 5: "))
    print("Calculated Average:", calculate_average(n1, n2, n3, n4, n5))


# Uncomment to run interactively:
# run_interactive_prompts()
# ==============================================================================