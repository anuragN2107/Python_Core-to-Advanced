# ==============================================================================
#                      PYTHON BASICS: TUPLES MASTER GUIDE
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. WHAT IS A TUPLE?
# ------------------------------------------------------------------------------
# A tuple is an immutable, ordered sequence of elements enclosed in parentheses ().
#
# Key Differences from Lists:
# - Lists are mutable `[]` (can grow, shrink, or change elements).
# - Tuples are immutable `()` (cannot be changed after creation, faster & memory efficient).

tuple5 = (1, "Hello", 3.14, True, (1, 2, 3), ("Hello", "World"))
print(tuple5)
print(type(tuple5))  # Output: <class 'tuple'>


# ------------------------------------------------------------------------------
# 2. KEY CHARACTERISTICS OF TUPLES
# ------------------------------------------------------------------------------
# - Ordered       : Items maintain their exact defined order.
# - Immutable     : Cannot add, modify, or delete elements once created.
# - Allows Copies : Can store duplicate values.
# - Heterogeneous : Can store multiple data types together.

tuple1 = (1, 2, 3, 4, 5)                    # Integers
tuple2 = ("Hello", "World")                 # Strings
tuple3 = (1, "Hello", 3.14, True)           # Mixed data types
tuple4 = (1, "Hello", 3.14, True, (1, 2, 3)) # Nested tuple


# ------------------------------------------------------------------------------
# 3. CRITICAL SYNTAX RULE: SINGLE-ELEMENT TUPLE
# ------------------------------------------------------------------------------
# To create a tuple with only ONE element, you MUST include a trailing comma.
# Without a comma, Python evaluates the parentheses as a standard expression.

not_a_tuple = ("apple")
print(type(not_a_tuple))  # Output: <class 'str'>

single_tuple = ("apple",)
print(type(single_tuple)) # Output: <class 'tuple'>


# ------------------------------------------------------------------------------
# 4. INDEXING, SLICING & MUTABILITY WORKAROUND
# ------------------------------------------------------------------------------
colors = ("red", "green", "blue", "yellow")

# Positive Indexing
print(colors[0])   # Output: red

# Negative Indexing
print(colors[-1])  # Output: yellow (last item)

# Slicing [start:stop] (stop is exclusive)
print(colors[1:3]) # Output: ('green', 'blue')

# How to modify a tuple (Workaround via List conversion):
# 1. Start with tuple -> 2. Convert to list -> 3. Modify -> 4. Convert back
temp = list(colors)
temp[0] = "orange"
colors = tuple(temp)
print("Modified tuple:", colors)  # Output: ('orange', 'green', 'blue', 'yellow')


# ------------------------------------------------------------------------------
# 5. TUPLE PACKING, UNPACKING & ASTERISK (*) OPERATOR
# ------------------------------------------------------------------------------

# Basic Unpacking (Variables must match element count)
x, y = (10, 20)
print(f"x = {x}, y = {y}")  # x = 10, y = 20

# Extended Unpacking using Asterisk (*)
#What is the asterisk (*) operator in Python?
# The asterisk (*) operator in Python is used for unpacking iterables, allowing you to capture multiple elements into a single variable. It can be used in tuple unpacking, function arguments, and more. When used in unpacking, it collects all remaining items from the iterable into a list.
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print("First: ", first)   # Output: 1
print("Middle:", middle)  # Output: [2, 3, 4] (captured as a list)
print("Last:  ", last)    # Output: 5

# Returning Multiple Values from a Function (Functions return tuples by default)
def get_min_max(nums):
    return min(nums), max(nums)  # Packs into tuple (min, max)

minimum, maximum = get_min_max([10, 25, 3, 89])
print(f"Min: {minimum}, Max: {maximum}")  # Output: Min: 3, Max: 89


# ------------------------------------------------------------------------------
# 6. BUILT-IN TUPLE METHODS (ONLY 2 METHODS)
# ------------------------------------------------------------------------------
# Because tuples are immutable, they only have 2 dedicated instance methods:

sample_tuple = (1, 2, 3, 3, 4, 5)

# 1. count(value): Returns how many times a value appears
print("Count of 3:", sample_tuple.count(3))  # Output: 2

# 2. index(value): Returns the index of the first occurrence
print("Index of 3:", sample_tuple.index(3))  # Output: 2


# ------------------------------------------------------------------------------
# 7. BUILT-IN GENERAL FUNCTIONS WITH TUPLES
# ------------------------------------------------------------------------------
num_tuple = (4, 1, 3, 2)

# len(): Returns number of items
print("len():", len(num_tuple))  # Output: 4

# min() and max()
print("min():", min(num_tuple))  # Output: 1
print("max():", max(num_tuple))  # Output: 4

# sum()
print("sum():", sum(num_tuple))  # Output: 10

# tuple(): Converts an iterable (like list or string) into a tuple
print("tuple([10, 20]):", tuple([10, 20]))  # Output: (10, 20)

# Reversing a tuple using slicing
print("Reversed tuple:  ", num_tuple[::-1])  # Output: (2, 3, 1, 4)

# Sorting a tuple using sorted() (Returns a NEW list)
# Note: Tuples do NOT have a .sort() method because .sort() modifies in-place.
sorted_asc = tuple(sorted(num_tuple))
print("Sorted Ascending: ", sorted_asc)  # Output: (1, 2, 3, 4)

sorted_desc = tuple(sorted(num_tuple, reverse=True))
print("Sorted Descending:", sorted_desc) # Output: (4, 3, 2, 1)


# ------------------------------------------------------------------------------
# 8. WHY USE TUPLES OVER LISTS?
# ------------------------------------------------------------------------------
# 1. Performance: Tuples are allocated in a single memory block; faster to iterate.
# 2. Safety: Data is write-protected (prevents accidental modification/bugs).
# 3. Dictionary Keys: Tuples can be used as keys in dictionaries (lists cannot
#    because they are unhashable).
# ==============================================================================