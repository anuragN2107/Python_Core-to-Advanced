# ===============================================================================================================================
#                                       MASTER NOTES: STRUCTURAL PATTERN MATCHING (match...case)
# ===============================================================================================================================
# This file covers Python's match...case statement, introduced in Python 3.10, structured sequentially.


# ===============================================================================================================================
# PART 1: WHAT IS `match...case`? (Definition & History)
# ===============================================================================================================================
# - Definition: Structural Pattern Matching (`match...case`) allows you to compare a value (the "subject") 
#   against multiple patterns. It is much more powerful than a traditional `switch-case` statement found in 
#   languages like C++ or Java because it can inspect data types, shapes, and contents.
# - Introduced in: Python 3.10 (Released in 2021, proposed via PEP 634, 635, and 636).
# - Purpose: To replace long, messy `if-elif-else` chains when checking complex data structures.


# ===============================================================================================================================
# PART 2: BASIC SYNTAX & LITERAL MATCHING
# ===============================================================================================================================
# Syntax Structure:
# match subject_variable:
#     case pattern1:
#         # code block
#     case pattern2:
#         # code block
#     case _:
#         # default catch-all block

print("=== DEMO 1: Basic Literal Matching ===")

def check_status(status_code: int) -> str:
    match status_code:
        case 200:
            return "OK: Success"
        case 400 | 404:  # Using the OR operator (|) for multiple patterns
            return "Client Error: Not Found or Bad Request"
        case 500:
            return "Server Error: Internal Issue"
        case _:  # The wildcard symbol acts as the default catch-all
            return "Unknown Status Code"

print(check_status(200))
print(check_status(404))
print(check_status(500))
print()


# ===============================================================================================================================
# PART 3: ADVANCED FEATURES (Guards, Sequences, and Mappings)
# ===============================================================================================================================

print("=== DEMO 2: Pattern Guards (Conditional Cases) ===")
# You can add `if` guards to a case statement for extra conditional filtering.
def evaluate_score(score: int) -> str:
    match score:
        case s if s >= 90:
            return "Grade: A (Excellent)"
        case s if 75 <= s < 90:
            return "Grade: B (Good)"
        case s if 50 <= s < 75:
            return "Grade: C (Average)"
        case _:
            return "Grade: F (Needs Improvement)"

print(evaluate_score(85))


print("\n=== DEMO 3: Sequence Matching (Tuples & Lists) ===")
# You can match the exact shape and unpack elements of lists or tuples.
def process_coordinates(coord: tuple) -> str:
    match coord:
        case (0, 0):
            return "Origin point (0, 0)"
        case (x, 0):
            return f"Point lies on the X-axis at x = {x}"
        case (0, y):
            return f"Point lies on the Y-axis at y = {y}"
        case (x, y):
            return f"Point located at coordinates X: {x}, Y: {y}"
        case _:
            return "Invalid coordinate format"

print(process_coordinates((0, 5)))
print(process_coordinates((3, 4)))


print("\n=== DEMO 4: Mapping Matching (Dictionaries) ===")
# You can match dictionary keys and extract their values directly.
def handle_command(command: dict) -> str:
    match command:
        case {"action": "start", "target": target}:
            return f"Executing start sequence for target: {target}"
        case {"action": "stop"}:
            return "Executing emergency stop sequence."
        case _:
            return "Unrecognized command structure."

print(handle_command({"action": "start", "target": "Server_Alpha"}))