# ==============================================================================
#                      PYTHON BASICS: OPERATORS
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. WHAT ARE OPERATORS?
# ------------------------------------------------------------------------------
# Operators are special symbols in Python that carry out arithmetic or logical
# computation on values (operands).

# ------------------------------------------------------------------------------
# 2. TYPES OF OPERATORS IN PYTHON
# ------------------------------------------------------------------------------
# 1. Arithmetic Operators  : Perform mathematical calculations (+, -, *, /, %, **, //)
# 2. Comparison Operators  : Compare two values, return bool (==, !=, <, >, <=, >=)
# 3. Logical Operators     : Combine conditions, return bool (and, or, not)
# 4. Bitwise Operators     : Operate at the binary bit level (&, |, ^, ~, <<, >>)
# 5. Assignment Operators  : Assign/modify variable values (=, +=, -=, *=, /=, %=, etc.)
# 6. Identity Operators    : Check if two variables point to same memory address (is, is not)
# 7. Membership Operators  : Check if an item exists within a sequence (in, not in)


# ------------------------------------------------------------------------------
# 3. ARITHMETIC OPERATORS
# ------------------------------------------------------------------------------
a = 10
b = 3

print(a + b)   # Addition         -> Output: 13
print(a - b)   # Subtraction      -> Output: 7
print(a * b)   # Multiplication   -> Output: 30
print(a / b)   # Division (float) -> Output: 3.3333333333333335
print(a % b)   # Modulus (rem.)   -> Output: 1
print(a ** b)  # Exponentiation   -> Output: 1000 (10^3)
print(a // b)  # Floor Division   -> Output: 3 (rounds down to nearest whole number)


# ------------------------------------------------------------------------------
# 4. COMPARISON OPERATORS (RELATIONAL)
# ------------------------------------------------------------------------------
x = 5
y = 10

print(x == y)  # Equal to                 -> Output: False
print(x != y)  # Not equal to             -> Output: True
print(x < y)   # Less than                -> Output: True
print(x > y)   # Greater than             -> Output: False
print(x <= y)  # Less than or equal to    -> Output: True
print(x >= y)  # Greater than or equal to -> Output: False


# ------------------------------------------------------------------------------
# 5. LOGICAL OPERATORS & TRUTH TABLES
# ------------------------------------------------------------------------------
# Truth Tables:
# | A     | B     | A and B | A or B | not A |
# |-------|-------|---------|--------|-------|
# | True  | True  | True    | True   | False |
# | True  | False | False   | True   | False |
# | False | True  | False   | True   | True  |
# | False | False | False   | False  | True  |

p = True
q = False

print(p and q)  # Logical AND -> Output: False (Both must be True)
print(p or q)   # Logical OR  -> Output: True  (At least one must be True)
print(not p)    # Logical NOT -> Output: False (Inverts boolean state)


# ------------------------------------------------------------------------------
# 6. BITWISE OPERATORS (BINARY MANIPULATION)
# ------------------------------------------------------------------------------
a = 5  # Binary: 0b0101
b = 3  # Binary: 0b0011

print(a & b)   # Bitwise AND  -> Output: 1  (0b0001: 1 only if both bits are 1)
print(a | b)   # Bitwise OR   -> Output: 7  (0b0111: 1 if either bit is 1)
print(a ^ b)   # Bitwise XOR  -> Output: 6  (0b0110: 1 if bits differ, 0 if same)
print(~a)      # Bitwise NOT  -> Output: -6 (Formula: -(a + 1) via two's complement)
print(a << 1)  # Left Shift   -> Output: 10 (Shifts bits left: multiplies by 2^n)
print(a >> 1)  # Right Shift  -> Output: 2  (Shifts bits right: integer divides by 2^n)


# ------------------------------------------------------------------------------
# 7. ASSIGNMENT OPERATORS (COMPOUND SHORTCUTS)
# ------------------------------------------------------------------------------
x = 5
x += 3   # x = x + 3  -> Output: 8
print(x)
x -= 2   # x = x - 2  -> Output: 6
print(x)
x *= 4   # x = x * 4  -> Output: 24
print(x)
x /= 3   # x = x / 3  -> Output: 8.0 (converts to float)
print(x)
x %= 5   # x = x % 5  -> Output: 3.0
print(x)


# ------------------------------------------------------------------------------
# 8. IDENTITY OPERATORS & id() FUNCTION
# ------------------------------------------------------------------------------
# id(object) returns the unique memory address integer of an object.
# `is` checks: id(a) == id(b)  [Same memory location]
# `==` checks: a == b          [Same value/content]

a = [1, 2, 3]
b = a          # Copies memory pointer, not the list data
c = [1, 2, 3]  # Creates a distinct new list object in heap memory

print(a is b)      # Output: True  (Both variables point to the same memory address)
print(a is c)      # Output: False (Different memory objects, even with identical values)
print(a == c)      # Output: True  (Values are equal)
print(a is not c)  # Output: True  (Confirms they are distinct objects)


# ------------------------------------------------------------------------------
# 9. MEMBERSHIP OPERATORS
# ------------------------------------------------------------------------------
# Tests element containment in sequences (list, tuple, string, set, dict).
my_list = [1, 2, 3, 4, 5]

print(3 in my_list)      # Output: True  (3 is an element of my_list)
print(6 not in my_list)  # Output: True  (6 is absent from my_list)


# ------------------------------------------------------------------------------
# 10. KEY CONCEPT COMPARISONS
# ------------------------------------------------------------------------------
# Difference: Identity vs Membership
# - Identity   (`is`, `is not`): Compares memory addresses (id).
# - Membership (`in`, `not in`): Checks if an item exists inside a container.

# Difference: `==` vs `=`
# - `=`  : Assignment operator (stores the right-hand value into the left-hand variable).
# - `==` : Relational operator (checks equality between two operands and returns bool).


# ------------------------------------------------------------------------------
# 11. OPERATOR PRECEDENCE (ORDER OF OPERATIONS)
# ------------------------------------------------------------------------------
# Highest to Lowest Precedence:
# 1. Parentheses: ()
# 2. Exponentiation: **
# 3. Unary / Bitwise NOT: +x, -x, ~x
# 4. Multiplication, Division, Modulus, Floor Div: *, /, %, //
# 5. Addition, Subtraction: +, -
# 6. Bitwise Shifts: <<, >>
# 7. Bitwise AND: &
# 8. Bitwise XOR: ^
# 9. Bitwise OR: |
# 10. Comparison & Identity & Membership: ==, !=, <, >, <=, >=, is, in
# 11. Logical NOT: not
# 12. Logical AND: and
# 13. Logical OR: or
# 14. Assignment Operators: =, +=, -=, etc.


# ------------------------------------------------------------------------------
# 12. VS CODE PRODUCTIVITY TIP: MULTI-CURSOR EDITING
# ------------------------------------------------------------------------------
# Multi-cursor lets you edit multiple lines or matching words simultaneously.
#
# Shortcuts:
# - Add cursor anywhere        : Alt + Click (Windows/Linux) | Option + Click (Mac)
# - Add cursor above / below   : Ctrl + Alt + Up/Down (Win)   | Option + Cmd + Up/Down (Mac)
# - Select next matching word  : Ctrl + D (Windows)           | Cmd + D (Mac)
# - Select all matching words  : Ctrl + Shift + L (Windows)   | Cmd + Shift + L (Mac)
# ==============================================================================