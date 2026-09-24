# ===============================================================================================================================
#                                       MASTER NOTES: TYPE DEFINITION & HINTS IN PYTHON
# ===============================================================================================================================
# This file is structured sequentially to guide you from basic type hints to advanced typing features in Python.


# ===============================================================================================================================
# PART 1: INTRODUCTION & BASICS OF TYPE HINTS
# ===============================================================================================================================

# WHAT ARE TYPE HINTS?
# Introduced via PEP 484 and PEP 526, type hints (or type annotations) allow developers to specify 
# the expected data types of variables, function parameters, and return values.
# IMPORTANT: Python remains a dynamically typed language. Type hints DO NOT enforce types at runtime; 
# they are used by IDEs, linters, and static type-checkers (like `mypy`) to catch bugs early.

# --- 1. Variable Type Annotations ---
# Syntax: variable_name: data_type = value
age: int = 25
name: str = "Anurag"
is_active: bool = True
price: float = 99.99

print(f"User: {name}, Age: {age}, Active: {is_active}, Price: {price}")


# --- 2. Function Parameter & Return Type Annotations ---
# Syntax: def function_name(param: type) -> return_type:
def calculate_area(length: float, width: float) -> float:
    """Calculates the area of a rectangle."""
    return length * width

print(f"Area: {calculate_area(10.5, 2)}")
print()


# ===============================================================================================================================
# PART 2: COLLECTIONS & BUILT-IN GENERICS (Lists, Tuples, Sets, Dicts)
# ===============================================================================================================================

# Starting from Python 3.9+, you can use standard built-in collections directly as generics 
# (e.g., list[int] instead of importing List from typing).

# --- 1. Lists (`list`) ---
# Used to hint homogeneous collections where all items share the same data type.
scores: list[int] = [85, 90, 95]
names_list: list[str] = ["Alice", "Bob", "Charlie"]

# --- 2. Tuples (`tuple`) ---
# Tuples can be annotated in two distinct ways depending on their use case:
#
# A. Fixed-Length Homogeneous Tuples (using an ellipsis `...`):
# Means a tuple containing *any number* of elements, but every single element must be an integer.
point_coordinates: tuple[int, ...] = (10, 20, 30, 40, 50)

# B. Heterogeneous Tuples (Fixed-position / Record style):
# Means a tuple with a strict, exact length where each position has a specific, distinct data type.
user_record: tuple[str, int, float] = ("Anurag", 28, 75.5)

# --- 3. Sets (`set`) ---
# A collection of unique items of a specific type.
unique_tags: set[str] = {"python", "coding", "backend"}

# --- 4. Dictionaries (`dict`) ---
# A mapping of key types and value types.
student_grades: dict[str, int] = {"Alice": 92, "Bob": 88}

print(f"Scores List: {scores}")
print(f"Homogeneous Tuple (Any length ints): {point_coordinates}")
print(f"Heterogeneous Tuple Record: {user_record}")
print(f"Grades for Alice: {student_grades['Alice']}")
print()


# ===============================================================================================================================
# PART 3: ADVANCED TYPE HINTS (Unions, Optional, Any, Literal)
# ===============================================================================================================================

from typing import Union, Optional, Any, Literal

# --- 1. Union Types (`|` operator or Union) ---
# Indicates that a variable or parameter can accept multiple specified types.
# In Python 3.10+, you can use the pipe symbol `|` instead of `Union[...]`.
def process_id(identifier: int | str) -> None:
    print(f"Processing ID: {identifier}")

process_id(1042)
process_id("EMP-992")


# --- 2. Optional Types ---
# `Optional[T]` is shorthand for `T | None` (meaning the value can be of type T or None).
def get_username(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "admin_user"
    return None  # Returns None if user not found


# --- 3. Any Type ---
# `Any` disables type checking for that specific variable or parameter. 
# Use it sparingly when the type is truly dynamic or unknown.
def log_payload(data: Any) -> None:
    print(f"Logging raw data: {data}")


# --- 4. Literal Types ---
# Restricts a parameter or variable to exact specific values (constant values).
def set_server_mode(mode: Literal["development", "staging", "production"]) -> None:
    print(f"Server configuration set to: {mode}")

set_server_mode("production")
print()


# ===============================================================================================================================
# PART 4: ADVANCED CALLABLES & GENERICS (TypeVar)
# ===============================================================================================================================

from typing import Callable, TypeVar

# --- 1. Callable (Typing Functions) ---
# Used when a function accepts another function as an argument.
# Syntax: Callable[[Param1Type, Param2Type], ReturnType]
def execute_operation(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

def add(x: int, y: int) -> int:
    return x + y

result = execute_operation(add, 5, 10)
print(f"Callable Result: {result}")


# --- 2. TypeVar (Creating Generic Functions & Classes) ---
# `TypeVar` allows you to write functions that accept any type while preserving 
# the exact type relationship between inputs and outputs.
T = TypeVar('T')

def get_first_element(items: list[T]) -> T:
    """Returns the first element of any list type while keeping its specific type hint."""
    return items[0]

first_score = get_first_element([99, 85, 70])      # Inferred as int
first_name = get_first_element(["Alice", "Bob"])   # Inferred as str
print(f"First Score: {first_score}, First Name: {first_name}")
print()


# ===============================================================================================================================
# PART 5: STRUCTURAL SUBTYPING (Protocol)
# ===============================================================================================================================

from typing import Protocol

# --- Protocols (Static Duck Typing) ---
# Instead of enforcing inheritance via ABCs (Abstract Base Classes), a Protocol defines 
# a structural interface. Any class that implements the required methods automatically 
# matches the protocol without explicitly inheriting from it.

class Renderable(Protocol):
    def render(self) -> str:
        ...

class PDFDocument:
    def render(self) -> str:
        return "Rendering PDF file..."

class HTMLPage:
    def render(self) -> str:
        return "Rendering HTML page..."

# This function accepts any object that conforms to the 'Renderable' protocol structure
def display_content(item: Renderable) -> None:
    print(item.render())

doc = PDFDocument()
page = HTMLPage()

display_content(doc)  # Works because PDFDocument implements render()
display_content(page) # Works because HTMLPage implements render()