# ==============================================================================
#                      PYTHON BASICS: SETS 
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. WHAT IS A SET?
# ------------------------------------------------------------------------------
# A set is an unordered, mutable collection of unique, hashable elements.
# Sets are defined using curly braces `{}` or the `set()` constructor.
#
# IMPORTANT DISTINCTION:
# - Standard Sets (`set`) are MUTABLE, which means they are UNHASHABLE.
#   Therefore, a `set` CANNOT be used as a dictionary key or inside another set.
# - If you need an immutable/hashable set to use as a dict key or inside a set, use `frozenset()`.

# Creating a set with duplicate values (duplicates are automatically removed)
fruits = {"apple", "banana", "cherry", "apple"}
print(fruits)  # Output: {'banana', 'apple', 'cherry'} (Order may vary)

# Creating an empty set (CRITICAL RULE)
# Using `{}` creates an empty DICTIONARY, not a set!
empty_dict = {}       # <class 'dict'>
empty_set = set()     # <class 'set'>
print(empty_set)      # Output: set()
print(type(empty_set))  # Output: <class 'set'>


# ------------------------------------------------------------------------------
# 2. KEY CHARACTERISTICS OF SETS
# ------------------------------------------------------------------------------
# - Unordered       : Elements have no fixed index or position (no indexing/slicing).
# - Unique Elements : Duplicate values are automatically discarded.
# - Mutable         : You can add and remove elements freely.
# - Element Types   : Set elements MUST be immutable/hashable (int, float, str, tuple).
#                     Lists, dicts, and sets cannot be elements inside a set.


# ------------------------------------------------------------------------------
# 3. ADDING ELEMENTS: add() VS update()
# ------------------------------------------------------------------------------
s = set()

# add(element): Adds a single item
s.add(1)
s.add(2)
s.add(3)
print("After add():   ", s)  # Output: {1, 2, 3}

# update(iterable): Adds multiple items from any iterable (list, tuple, string, set)
s.update([4, 5, 6])
print("After update():", s)  # Output: {1, 2, 3, 4, 5, 6}


# ------------------------------------------------------------------------------
# 4. REMOVING ELEMENTS: remove() VS discard() VS pop()
# ------------------------------------------------------------------------------
# - remove(val)  : Removes item; RAISES KeyError if item is missing!
# - discard(val) : Removes item; does NOTHING (safe, no error) if item is missing.
# - pop()        : Removes and returns an ARBITRARY item.
# - clear()      : Empties the entire set.

s6 = {1, 2, 3, 4, 5}

# remove() raises error if item is not found
s6.remove(2)     # Removes 2
# s6.remove(99)  # Raises KeyError: 99

# discard() is safe
s6.discard(4)    # Removes 4
s6.discard(99)   # Does nothing, no error raised!

print("After remove & discard:", s6)  # Output: {1, 3, 5}

# pop() removes an arbitrary item
popped_item = s6.pop()
print("Popped item:", popped_item)


# ------------------------------------------------------------------------------
# 5. MATHEMATICAL SET OPERATIONS (UNION, INTERSECTION, DIFFERENCE)
# ------------------------------------------------------------------------------
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# 1. Union (|): All elements from both sets
print("Union (|):               ", A | B)                 # Output: {1, 2, 3, 4, 5, 6}
print("Union (method):          ", A.union(B))

# 2. Intersection (&): Common elements in both sets
print("Intersection (&):        ", A & B)                 # Output: {3, 4}
print("Intersection (method):   ", A.intersection(B))

# 3. Difference (-): Elements in A but not in B
print("Difference (A - B):      ", A - B)                 # Output: {1, 2}
print("Difference (B - A):      ", B - A)                 # Output: {5, 6}

# 4. Symmetric Difference (^): Elements in A or B, but NOT in both
print("Symmetric Difference (^):", A ^ B)                 # Output: {1, 2, 5, 6}


# ------------------------------------------------------------------------------
# 6. MEMBERSHIP, ITERATION, LENGTH & UTILITIES
# ------------------------------------------------------------------------------
s7 = {10, 20, 30, 40, 50}

# Membership test (Extremely fast - O(1) average time complexity)
print(10 in s7)      # Output: True
print(99 in s7)      # Output: False

# Length of a set
print("Set length:", len(s7))  # Output: 5

# Iterating over a set
for item in s7:
    print("Item:", item)

# Shallow copying
s_copy = s7.copy()

# Clearing a set
s_copy.clear()
print("Cleared set:", s_copy)  # Output: set()


# ------------------------------------------------------------------------------
# 7. TYPE CONVERSIONS WITH SETS
# ------------------------------------------------------------------------------
nums = {1, 2, 3, 4, 5}

# Set to List
list_from_set = list(nums)
print("To List: ", list_from_set)   # Output: [1, 2, 3, 4, 5]

# Set to Tuple
tuple_from_set = tuple(nums)
print("To Tuple:", tuple_from_set)  # Output: (1, 2, 3, 4, 5)

# Set to String
str_from_set = str(nums)
print("To String:", str_from_set)   # Output: '{1, 2, 3, 4, 5}'

# Set to Dictionary (Assigning default values via dict.fromkeys)
dict_from_set = dict.fromkeys(nums, None)
print("To Dict:  ", dict_from_set)  # Output: {1: None, 2: None, 3: None, 4: None, 5: None}


# ------------------------------------------------------------------------------
# 8. WHAT IS A FROZENSET? (IMMUTABLE SET)
# ------------------------------------------------------------------------------
# A `frozenset` is an immutable, hashable version of a set.
# Because it cannot be changed after creation, it CAN be used as:
#   1. A dictionary key
#   2. An element inside another set

normal_set = {1, 2, 3}
fs = frozenset(normal_set)
print("Frozenset:", fs)  # Output: frozenset({1, 2, 3})

# fs.add(4)  # Raises AttributeError: 'frozenset' object has no attribute 'add'

# Using frozenset as a dictionary key:
lookup = {fs: "Prime set"}
print("Frozenset as key:", lookup[fs])  # Output: Prime set
# ==============================================================================