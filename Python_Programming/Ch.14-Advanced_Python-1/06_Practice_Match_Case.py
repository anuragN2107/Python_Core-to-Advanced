# ===============================================================================================================================
#                                       PRACTICE EXERCISES: MATCH...CASE STATEMENT
# ===============================================================================================================================
# This file contains 6 practice exercises with solutions and brief explanations based on Structural Pattern Matching.


# ===============================================================================================================================
# QUESTION 1: Basic Day Categorization
# ===============================================================================================================================
# Question: Write a function `categorize_day` that takes a string representing a day of the week. 
# Use `match...case` to return "Weekday" for Monday through Friday, "Weekend" for Saturday and Sunday, 
# and "Invalid Day" for anything else.

def categorize_day(day: str) -> str:
    match day.lower():
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return "Weekday"
        case "saturday" | "sunday":
            return "Weekend"
        case _:
            return "Invalid Day"

print(f"Q1 Result: {categorize_day('Monday')}")


# ===============================================================================================================================
# QUESTION 2: Role-Based Access Control
# ===============================================================================================================================
# Question: Write a function `check_access` that takes a user role string ("Admin", "Editor", "Viewer"). 
# Return "Full Access" for Admin, "Edit Access" for Editor, "Read-Only Access" for Viewer, 
# and "Access Denied" for any other unknown role.

def check_access(role: str) -> str:
    match role:
        case "Admin":
            return "Full Access"
        case "Editor":
            return "Edit Access"
        case "Viewer":
            return "Read-Only Access"
        case _:
            return "Access Denied"

print(f"Q2 Result: {check_access('Editor')}")


# ===============================================================================================================================
# QUESTION 3: Numerical Range Evaluation with Guards
# ===============================================================================================================================
# Question: Write a function `evaluate_temperature` that takes a numeric temperature value. 
# Use `match...case` with `if` guards to classify it: 
# - Above 35: "Hot"
# - Between 20 and 35 (inclusive): "Pleasant"
# - Below 20: "Cold"

def evaluate_temperature(temp: float) -> str:
    match temp:
        case t if t > 35:
            return "Hot"
        case t if 20 <= t <= 35:
            return "Pleasant"
        case _:
            return "Cold"

print(f"Q3 Result: {evaluate_temperature(28)}")


# ===============================================================================================================================
# QUESTION 4: Tuple Shape Unpacking (2D vs 3D Points)
# ===============================================================================================================================
# Question: Write a function `analyze_point` that accepts a tuple. 
# If it has 2 elements `(x, y)`, return "2D Point". If it has 3 elements `(x, y, z)`, return "3D Point". 
# Otherwise, return "Unknown Dimension".

def analyze_point(point: tuple) -> str:
    match point:
        case (x, y):
            return "2D Point"
        case (x, y, z):
            return "3D Point"
        case _:
            return "Unknown Dimension"

print(f"Q4 Result: {analyze_point((10, 20, 30))}")


# ===============================================================================================================================
# QUESTION 5: Dictionary Mapping Pattern Matching
# ===============================================================================================================================
# Question: Write a function `parse_json_event` that takes a dictionary event. 
# If the event is `{"type": "click", "x": value, "y": value}`, return a string describing the click coordinates. 
# If it is `{"type": "keypress", "key": value}`, return a string showing the pressed key. 
# Otherwise, return "Unknown Event".

def parse_json_event(event: dict) -> str:
    match event:
        case {"type": "click", "x": x, "y": y}:
            f_str = f"Mouse click at coordinates X: {x}, Y: {y}"
            return f_str
        case {"type": "keypress", "key": key}:
            return f"Key pressed: {key}"
        case _:
            return "Unknown Event"

print(f"Q5 Result: {parse_json_event({'type': 'click', 'x': 100, 'y': 250})}")


# ===============================================================================================================================
# QUESTION 6: List Matching with Rest/Wildcards (`*`)
# ===============================================================================================================================
# Question: Write a function `process_list` that checks a list of integers:
# - If the list is empty `[]`, return "Empty list".
# - If it has exactly one item `[single]`, return "Single item: value".
# - If it has multiple items, unpack the first item and use `*rest` to capture the remaining items, 
#   returning the head element and the count of remaining elements.

def process_list(items: list) -> str:
    match items:
        case []:
            return "Empty list"
        case [single]:
            return f"Single item: {single}"
        case [first, *rest]:
            return f"First item is {first}, with {len(rest)} remaining items."

print(f"Q6 Result: {process_list([10, 20, 30, 40])}")