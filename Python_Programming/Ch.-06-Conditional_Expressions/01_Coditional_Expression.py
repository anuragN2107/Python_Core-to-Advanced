# ==============================================================================
#                 PYTHON BASICS: CONDITIONAL STATEMENTS
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. WHAT ARE CONDITIONAL STATEMENTS?
# ------------------------------------------------------------------------------
# Conditionals allow a program to make decisions and execute specific blocks of
# code based on whether a condition evaluates to True or False.
#
# Key Concepts:
# - `if`   : Evaluates the initial condition.
# - `elif` : Short for "else if". Checks subsequent conditions only if previous ones were False.
# - `else` : Fallback block executed if NONE of the preceding conditions evaluate to True.
# - Indentation (4 spaces) defines the body/scope of each condition block.


# ------------------------------------------------------------------------------
# 2. RELATIONAL & LOGICAL OPERATORS IN CONDITIONS
# ------------------------------------------------------------------------------
# Relational (Comparison):
#   == (Equal to)             != (Not equal to)
#   >  (Greater than)         >= (Greater than or equal to)
#   <  (Less than)            <= (Less than or equal to)

# Logical Operators:
#   and : Returns True if BOTH conditions are True
#   or  : Returns True if AT LEAST ONE condition is True
#   not : Inverts the boolean result (True -> False, False -> True)


# ------------------------------------------------------------------------------
# 3. TYPE 1: SIMPLE `if` STATEMENT
# ------------------------------------------------------------------------------
# Executes the block only if the condition evaluates to True.

x = 9

if x > 0:
    print("x is positive")  # Output: x is positive

if x < 0:
    print("x is negative")

if x == 0:
    print("x is zero")

if x != 0:
    print("x is not zero")  # Output: x is not zero


# ------------------------------------------------------------------------------
# 4. TYPE 2: DUAL-BRANCH (`if-else`) STATEMENT
# ------------------------------------------------------------------------------
# Executes one block if True, and an alternative fallback block if False.

x = -10
if x > 0:
    print("x is positive")
else:
    print("x is not positive")  # Output: x is not positive


# Real-World Example: Voting Eligibility
voter_age = int(input("Enter your age: "))
if voter_age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


# ------------------------------------------------------------------------------
# 5. TYPE 3 & 4: MULTI-BRANCH LADDER (`if-elif-else`)
# ------------------------------------------------------------------------------
# Evaluates conditions sequentially. Once the first matching True branch runs,
# all subsequent `elif` and `else` branches are skipped immediately (Short-circuiting).

x = 8
if x > 0:
    print("x is positive")  # Output: x is positive
elif x < 0:
    print("x is negative")
else:
    print("x is zero")


# Chained Multi-Condition Check:
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")  # Output: Grade: B
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: Fail")


# ------------------------------------------------------------------------------
# 6. TYPE 5: NESTED CONDITIONALS
# ------------------------------------------------------------------------------
# Placing `if`, `elif`, or `else` blocks inside another conditional block.

weather = "sunny"
temp = 35

if weather == "rainy":
    print("Take an umbrella.")
elif weather == "snowy":
    print("Wear a heavy jacket.")
elif weather == "sunny":
    if temp > 30:
        print("Go swimming at the beach!")  # Output: Go swimming at the beach!
    else:
        print("Go for a picnic in the park!")
else:
    print("Enjoy your day indoors!")


# ------------------------------------------------------------------------------
# 7. TYPE 6: TERNARY CONDITIONAL EXPRESSION (INLINE `if-else`)
# ------------------------------------------------------------------------------
# Syntax: value_if_true if condition else value_if_false
# Assigns or returns a value on a single line based on a condition.

age = 17
status = "Adult" if age >= 18 else "Minor"
print("Status:", status)  # Output: Minor


# ------------------------------------------------------------------------------
# 8. TYPE 7: STRUCTURAL PATTERN MATCHING (`match-case` - Python 3.10+)
# ------------------------------------------------------------------------------
# Acts as a modern, clean alternative to long if-elif-else ladders (similar to switch-case).
# `case _` serves as the wildcard/default fallback.

command = input("Enter a command (start/stop/restart): ")

match command:
    case "start":
        print("System starting...")
    case "stop":
        print("System shutting down...")
    case "restart":
        print("System restarting...")
    case _:
        print("Unknown command")  # Default case if no pattern matches
# ==============================================================================