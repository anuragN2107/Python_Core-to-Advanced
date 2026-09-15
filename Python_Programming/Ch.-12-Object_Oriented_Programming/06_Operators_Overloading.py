# ===============================================================================================================================
#                                       PYTHON OPERATOR OVERLOADING: MASTER GUIDE & NOTES
# ===============================================================================================================================

# -------------------------------------------------------------------------------------------------------------------------------
# WHAT IS OPERATOR OVERLOADING? (CORE DEFINITION)
# -------------------------------------------------------------------------------------------------------------------------------
# Operator Overloading is a feature in Object-Oriented Programming (OOP) that allows the same operator (like +, -, *, ==) 
# to mean different things depending on the context or the data types involved.
#
# Operators in Python can be overloaded using dunder (double-underscore/magic) methods.
# These methods are called automatically when a given operator is used on objects.
#
# How operators map to underlying dunder methods:
# - p1 + p2  ==>  p1.__add__(p2)
# - p1 - p2  ==>  p1.__sub__(p2)
# - p1 * p2  ==>  p1.__mul__(p2)
# - p1 / p2  ==>  p1.__truediv__(p2)
# - p1 // p2 ==>  p1.__floordiv__(p2)
# - p1 == p2 ==>  p1.__eq__(p2)
# - str(obj) ==>  obj.__str__()
# - len(obj) ==>  obj.__len__()
# - p1 += p2 ==>  p1.__iadd__(p2)
# -------------------------------------------------------------------------------------------------------------------------------


# ===============================================================================================================================
# PRACTICAL CODE EXAMPLE: OVERLOADING +, -, ==, +=, len(), AND str()
# ===============================================================================================================================

print("=== OPERATOR OVERLOADING DEMONSTRATION ===")

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 1. Overloading the `str()` function and `print()` behavior
    def __str__(self):
        """Defines how the object looks when printed or converted to a string."""
        return f"Vector({self.x}, {self.y})"  # Output: Vector(2, 3)

    # 2. Overloading the `+` operator (__add__) -> p1 + p2 calls p1.__add__(p2)
    def __add__(self, other):
        """Adds corresponding x and y components of two vectors together."""
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)  # Returns a brand-new Vector object

    # 3. Overloading the `-` operator (__sub__) -> p1 - p2 calls p1.__sub__(p2)
    def __sub__(self, other):
        """Subtracts corresponding x and y components of two vectors."""
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)

    # 4. Overloading the `==` operator (__eq__) -> p1 == p2 calls p1.__eq__(p2)
    def __eq__(self, other):
        """Compares if two vectors have the exact same x and y values."""
        return self.x == other.x and self.y == other.y

    # 5. Overloading the `+=` operator (__iadd__ - Augmented Assignment)
    def __iadd__(self, other):
        """Modifies the current vector in place when using +=."""
        self.x += other.x
        self.y += other.y
        return self  # Must return self for in-place operators to update properly

    # 6. Overloading the `len()` function (__len__)
    def __len__(self):
        """Defines custom length (e.g., returning the total components or magnitude count)."""
        return 2  # A 2D vector always has 2 components (x and y)


# --- Testing Our Overloaded Operators ---

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = Vector(2, 3)

print(f"Vector 1: {v1}")  # Calls __str__
print(f"Vector 2: {v2}")  # Calls __str__

# Testing Addition (+) -> Triggers v1.__add__(v2)
v_sum = v1 + v2
print(f"\nAddition (v1 + v2): {v_sum}")

# Testing Subtraction (-) -> Triggers v2.__sub__(v1)
v_diff = v2 - v1
print(f"Subtraction (v2 - v1): {v_diff}")

# Testing Equality (==) -> Triggers v1.__eq__(v3) and v1.__eq__(v2)
print(f"Is v1 == v3? {v1 == v3}")  # True
print(f"Is v1 == v2? {v1 == v2}")  # False

# Testing In-Place Addition (+=) -> Triggers v1.__iadd__(v2)
print(f"\nBefore +=, v1 is: {v1}")
v1 += v2
print(f"After v1 += v2, v1 is: {v1}")

# Testing len() function -> Triggers v1.__len__()
print(f"Length of vector v1: {len(v1)}")