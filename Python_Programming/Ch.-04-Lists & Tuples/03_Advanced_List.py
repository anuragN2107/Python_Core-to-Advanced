# ==============================================================================
#                 PYTHON ADVANCED: LIST COMPREHENSIONS
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. WHAT IS A LIST COMPREHENSION?
# ------------------------------------------------------------------------------
# A concise, Pythonic syntax to construct a new list from an existing iterable.
# It runs faster than equivalent standard `for` loops because the iteration is
# executed at C-speed internally within CPython bytecode.
#
# General Syntax:
#   [expression for item in iterable]


# Standard loop vs List Comprehension:
# Traditional for-loop:
squares_loop = []
for x in range(1, 6):
    squares_loop.append(x**2)

# List comprehension equivalent:
squares = [x**2 for x in range(1, 6)]
print("Basic Comprehension:", squares)  # Output: [1, 4, 9, 16, 25]


# ------------------------------------------------------------------------------
# 2. FILTERING WITH AN `if` CONDITION
# ------------------------------------------------------------------------------
# Syntax: [expression for item in iterable if condition]
# The `if` at the end acts as a filter: only elements matching the condition are kept.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers:
evens = [x for x in numbers if x % 2 == 0]
print("Filtered Evens:     ", evens)  # Output: [2, 4, 6, 8, 10]

# Filter and transform strings (words longer than 3 characters converted to uppercase):
words = ["cat", "house", "dog", "python", "sun"]
long_upper = [w.upper() for w in words if len(w) > 3]
print("Transformed Words:  ", long_upper)  # Output: ['HOUSE', 'PYTHON']


# ------------------------------------------------------------------------------
# 3. CONDITIONAL VALUE SELECTION (TERNARY / `if-else` EXPRESSION)
# ------------------------------------------------------------------------------
# Syntax: [val_if_true if condition else val_if_false for item in iterable]
#
# RULE OF THUMB:
# - To FILTER items out    -> Put `if` at the END.
# - To TRANSFORM item val  -> Put `if-else` at the BEGINNING.

# Label each number as 'Even' or 'Odd':
labels = ["Even" if x % 2 == 0 else "Odd" for x in range(1, 6)]
print("Ternary if-else:    ", labels)  # Output: ['Odd', 'Even', 'Odd', 'Even', 'Odd']

# Multiple conditions (chained ternary):
scores = [95, 82, 67, 45]
grades = ["A" if s >= 90 else ("B" if s >= 80 else "C") for s in scores]
print("Chained Grades:     ", grades)  # Output: ['A', 'B', 'C', 'C']


# ------------------------------------------------------------------------------
# 4. NESTED FOR-LOOPS IN LIST COMPREHENSIONS
# ------------------------------------------------------------------------------
# Syntax: [expression for outer in list1 for inner in list2]
# Order of clauses reads left-to-right, exactly matching nested loop indentation.

# Example A: Cartesian Product (Combinations)
suits = ["♠", "♥"]
ranks = ["A", "K"]
deck = [f"{r}{s}" for s in suits for r in ranks]
print("Cartesian Product:  ", deck)  # Output: ['A♠', 'K♠', 'A♥', 'K♥']

# Equivalent Traditional Loop:
# deck = []
# for s in suits:
#     for r in ranks:
#         deck.append(f"{r}{s}")


# Example B: Flattening a 2D Matrix into a 1D List
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened = [item for row in matrix for item in row]
print("Flattened Matrix:   ", flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]


# ------------------------------------------------------------------------------
# 5. CREATING NESTED LISTS (2D MATRICES / GRIDS)
# ------------------------------------------------------------------------------
# Nest a full list comprehension INSIDE the output expression of another.

# Create a 3x3 identity matrix where diagonal is 1 and others are 0:
identity_matrix = [[1 if r == c else 0 for c in range(3)] for r in range(3)]
print("3x3 Matrix:")
for row in identity_matrix:
    print(" ", row)
# Output:
#  [1, 0, 0]
#  [0, 1, 0]
#  [0, 0, 1]

# Transpose a matrix (swap rows and columns):
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("Transposed Matrix:  ", transposed)  # Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]


# ------------------------------------------------------------------------------
# 6. BEST PRACTICES & COMMON PITFALLS
# ------------------------------------------------------------------------------
# 1. Readability First (PEP 8):
#    Avoid overly complex comprehensions with more than 2 loops/conditions.
#    Use standard loops when logic becomes hard to read at a glance.

# 2. Large Datasets (Memory Optimization):
#    List comprehensions create the ENTIRE list in memory immediately.
#    For massive data (millions of elements), use Generator Expressions `(x for x in ...)`
#    to compute values lazily one-by-one with O(1) memory overhead.
large_gen = (x**2 for x in range(1_000_000))  # Takes almost 0 memory!
# ==============================================================================