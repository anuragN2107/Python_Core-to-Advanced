# ==============================================================================
#                 PYTHON BASICS: SHORT-CIRCUIT EVALUATION
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. WHAT IS SHORT-CIRCUIT EVALUATION?
# ------------------------------------------------------------------------------
# Short-circuit evaluation is an optimization where Python stops evaluating a
# compound logical expression as soon as the overall outcome is guaranteed.
#
# Core Rules:
# | Expression | Condition to Stop             | Evaluated Action                      |
# |------------|-------------------------------|---------------------------------------|
# | A or B     | If A is Truthy                | Stops & returns A (B is skipped)      |
# | A or B     | If A is Falsy                 | Evaluates and returns B               |
# | A and B    | If A is Falsy                 | Stops & returns A (B is skipped)      |
# | A and B    | If A is Truthy                | Evaluates and returns B               |


# ------------------------------------------------------------------------------
# 2. BASIC COMPARISON EXAMPLES
# ------------------------------------------------------------------------------
x = 5
y = 10

print(x < y)            # Output: True  (5 < 10)
print(x > y and x < y)  # Output: False (x > y is False -> stops immediately)
print(x > y or x < y)   # Output: True  (x > y is False -> evaluates x < y -> True)


# ------------------------------------------------------------------------------
# 3. SHORT-CIRCUIT IN PRACTICE (AVOIDING EXPENSIVE OPERATIONS)
# ------------------------------------------------------------------------------

def check_database_for_ticket():
    """Simulates a heavy operation like a network call or database query."""
    print("  [Database checked]")
    return True


print("--- Case 1: `or` with First Condition True ---")
has_vip_pass = True
# 'has_vip_pass' is True -> Short-circuits (database is NOT checked)
if has_vip_pass or check_database_for_ticket():
    print("Welcome to the event!")
# Output:
# Welcome to the event!


print("\n--- Case 2: `or` with First Condition False ---")
has_vip_pass = False
# 'has_vip_pass' is False -> Evaluates the second condition (runs database check)
if has_vip_pass or check_database_for_ticket():
    print("Welcome to the event!")
# Output:
#   [Database checked]
# Welcome to the event!


print("\n--- Case 3: `and` with First Condition True ---")
has_vip_pass = True
# 'has_vip_pass' is True -> Must evaluate second condition to confirm overall truth
if has_vip_pass and check_database_for_ticket():
    print("Welcome to the event!")
# Output:
#   [Database checked]
# Welcome to the event!


print("\n--- Case 4: `and` with First Condition False ---")
has_vip_pass = False
# 'has_vip_pass' is False -> Short-circuits (database is NOT checked)
if has_vip_pass and check_database_for_ticket():
    print("Welcome to the event!")
# Output: (No output because condition fails immediately)


# ------------------------------------------------------------------------------
# 4. CRITICAL REAL-WORLD USES: GUARD PATTERNS & DEFAULT VALUES
# ------------------------------------------------------------------------------

# 1. Guarding Against ZeroDivisionError / IndexError / NoneType Error
# The left-hand condition protects the right-hand expression from crashing.
divisor = 0
# divisor != 0 is False -> expression short-circuits before running (10 / 0)
if divisor != 0 and (10 / divisor) > 1:
    print("Division succeeded")
else:
    print("Prevented crash: Divisor is 0")

# 2. Setting Default / Fallback Values using `or`
user_input = ""  # Empty string is Falsy
default_name = "Guest"
active_user = user_input or default_name
print("Active User:", active_user)  # Output: Guest

# 3. What Values `and` / `or` Actually Return:
# Python logical operators return the actual operand object, not just True/False:
print("apple" or "banana")  # Output: 'apple'  (First truthy value)
print("" or "banana")       # Output: 'banana' (Evaluates second value)
print("apple" and "banana") # Output: 'banana' (Evaluates second value)
print("" and "banana")      # Output: ''       (First falsy value)
# ==============================================================================