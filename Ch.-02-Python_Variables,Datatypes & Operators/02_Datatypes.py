# ==============================================================================
#                 PYTHON BASICS: DATA TYPES, MEMORY & MUTABILITY
# ==============================================================================
import sys

# ------------------------------------------------------------------------------
# 1. WHAT IS A DATA TYPE?
# ------------------------------------------------------------------------------
# A data type tells Python what kind of value a variable holds and what operations
# can be done with it.
#
# Memory Note:
# In Python, variables do not store raw numbers directly. They store a reference
# (pointer/address) pointing to an object in heap memory.


# ------------------------------------------------------------------------------
# 2. CORE DATA TYPES & REAL MEMORY OVERHEAD
# ------------------------------------------------------------------------------
# Why are sizes larger than C/Java?
# Every Python object (PyObject) has built-in metadata:
#   1. Reference count (tracks memory cleanup)
#   2. Type information (e.g., int vs str)
#   3. Value / capacity data

# 1. Integer (int) -> IMMUTABLE
# - Space: Starts at ~28 bytes (base overhead) on 64-bit systems.
# - Range: UNLIMITED (arbitrary precision). Python expands memory as digits grow.
#   (Note: -2,147,483,648 to 2,147,483,647 is a 32-bit C/Java limit, not Python's limit).
a = 1

# 2. Float (float) -> IMMUTABLE
# - Space: ~24 bytes (base overhead + 8-byte C double).
# - Range: ~ -1.79e+308 to +1.79e+308 (64-bit IEEE 754).
# - Note: Python uses float for all decimals; there is no separate 'double' keyword.
b = 2.5

# 3. String (str) -> IMMUTABLE
# - Space: ~49 bytes (header) + 1 to 4 bytes per character.
c = "Hello"

# 4. Boolean (bool) -> IMMUTABLE
# - Space: ~28 bytes (subclass of int; True=1, False=0).
d = True

# 5. List (list) -> MUTABLE
# - Space: ~56 bytes (empty list) + 8 bytes per pointer + pre-allocated buffer slots.
e = [1, 2, 3]

# 6. Tuple (tuple) -> IMMUTABLE
# - Space: ~40 bytes (fixed size, cannot add/remove items; less overhead than lists).
f = (1, 2, 3)

# 7. Set (set) -> MUTABLE
# - Space: ~216 bytes (starts larger due to internal hash table for O(1) lookups).
g = {1, 2, 3}

# 8. Dictionary (dict) -> MUTABLE
# - Space: ~64 bytes (empty dict) + hash table storage for key-value pairs.
h = {"name": "Anurag", "age": 25}

# 9. NoneType (None) -> IMMUTABLE
# - Space: ~16 bytes (singleton object representing 'no value').
i = None


# ------------------------------------------------------------------------------
# 3. SPACE COMPLEXITY (BIG-O) QUICK REFERENCE
# ------------------------------------------------------------------------------
# Space Complexity measures how memory scales as data size grows (n = items/length):
#
# | Data Type | Space Complexity | Explanation                                      |
# |-----------|------------------|--------------------------------------------------|
# | int       | O(log n) / O(1)  | Constant O(1) for normal numbers; grows with digits|
# | float     | O(1)             | Fixed 64-bit precision                            |
# | str       | O(n)             | Linear: grows with number of characters           |
# | bool      | O(1)             | Fixed single value                                |
# | list      | O(n)             | Linear: stores n element pointers + growth buffer |
# | tuple     | O(n)             | Linear: stores exact n element pointers           |
# | set       | O(n)             | Linear: stores n unique hashed elements           |
# | dict      | O(n)             | Linear: stores n key-value pairs in hash table    |
# | NoneType  | O(1)             | Fixed singleton                                   |


# ------------------------------------------------------------------------------
# 4. MUTABLE VS IMMUTABLE (EASY TEST WITH id())
# ------------------------------------------------------------------------------
# id(x) returns the unique memory address of object x.

# --- IMMUTABLE TEST ---
x = 10
old_address = id(x)
x = x + 1  # Cannot change 10 in place; creates a NEW integer (11)
print(f"Immutable (int) changed address? {id(x) != old_address}")  # True

# --- MUTABLE TEST ---
my_list = [1, 2]
old_address = id(my_list)
my_list.append(3)  # Modifies existing list in place
print(f"Mutable (list) changed address?  {id(my_list) != old_address}")  # False


# ------------------------------------------------------------------------------
# 5. PRACTICAL MEMORY INSPECTION WITH sys.getsizeof()
# ------------------------------------------------------------------------------
# Outputs real byte allocations on a standard 64-bit Python setup:

print(f"int (1):          {sys.getsizeof(1)} bytes")  # ~28 bytes
print(f"float (2.5):      {sys.getsizeof(2.5)} bytes")  # ~24 bytes
print(f"str ('Hello'):    {sys.getsizeof('Hello')} bytes")  # ~54 bytes (49 + 5 chars)
print(f"list ([1, 2, 3]): {sys.getsizeof([1, 2, 3])} bytes")  # ~88 bytes (56 + pointers)
print(f"None:             {sys.getsizeof(None)} bytes")  # ~16 bytes
# ==============================================================================