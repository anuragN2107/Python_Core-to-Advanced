# ==============================================================================
#                      PYTHON BASICS: SET OPERATIONS
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. CORE SET OPERATIONS & COMPARISONS
# ------------------------------------------------------------------------------
# 1. Union (|)                  : Combines all unique elements from both sets.
# 2. Intersection (&)           : Keeps only elements present in BOTH sets.
# 3. Difference (-)             : Elements in the first set but NOT in the second.
# 4. Symmetric Difference (^)   : Elements in either set, but NOT in both.
# 5. issubset (<=)              : Checks if all elements of Set A exist in Set B.
# 6. issuperset (>=)            : Checks if Set A contains all elements of Set B.
# 7. isdisjoint ()              : Checks if two sets have NO elements in common.

s20 = {1, 2, 3, 4, 5}
s21 = {2, 3, 4, 5, 6}
s22 = {1, 2, 3, 4, 5, 6}

# Union (|)
print("Union (method):         ", s20.union(s21))         # {1, 2, 3, 4, 5, 6}
print("Union (operator |):     ", s20 | s21)             # {1, 2, 3, 4, 5, 6}

# Intersection (&)
print("Intersection (method):  ", s20.intersection(s21))  # {2, 3, 4, 5}
print("Intersection (operator &):", s20 & s21)           # {2, 3, 4, 5}

# Difference (-)
print("Difference (method):    ", s20.difference(s21))    # {1}
print("Difference (operator -):", s20 - s21)             # {1}

# Symmetric Difference (^)
print("Sym. Diff (s20, s22):   ", s20.symmetric_difference(s22))  # {6}
print("Sym. Diff (s20, s21):   ", s20 ^ s21)                      # {1, 6}

# Subset, Superset, and Disjoint Checks
print("Is s20 a subset of s21?   ", s20.issubset(s21))    # False (or: s20 <= s21)
print("Is s22 a superset of s20? ", s22.issuperset(s20))  # True  (or: s22 >= s20)
print("Are s20 and s21 disjoint? ", s20.isdisjoint(s21))  # False (they share 2, 3, 4, 5)

s_disjoint = {7, 8, 9}
print("Are s20 and s_disjoint disjoint? ", s20.isdisjoint(s_disjoint))  # True


# ------------------------------------------------------------------------------
# 2. CRITICAL RULE: METHODS VS OPERATORS WITH OTHER DATA TYPES
# ------------------------------------------------------------------------------
# - Tuples, lists, strings, and dicts DO NOT have set methods like .union() directly.
# - However, SET METHODS (like set.union()) accept ANY iterable (tuple, list, str, dict).
# - SET OPERATORS (|, &, -, ^) require BOTH operands to be actual `set` objects.

base_set = {1, 2, 3}


# --- A. Set Operations with Tuples ---
t1 = (3, 4, 5)

# Pass tuple directly into set methods:
print("\n--- Sets with Tuples ---")
print("Set + Tuple Union:       ", base_set.union(t1))         # {1, 2, 3, 4, 5}
print("Set + Tuple Intersection:", base_set.intersection(t1))  # {3}
print("Set + Tuple Difference:  ", base_set.difference(t1))    # {1, 2}
# Using operator requires explicit conversion: base_set | set(t1)


# --- B. Set Operations with Lists ---
l1 = [3, 4, 5]

print("\n--- Sets with Lists ---")
print("Set + List Union:        ", base_set.union(l1))         # {1, 2, 3, 4, 5}
print("Set + List Intersection: ", base_set.intersection(l1))  # {3}
print("Set + List Difference:   ", base_set.difference(l1))    # {1, 2}


# --- C. Set Operations with Strings ---
# Treats string as an iterable of unique characters
str_set = {"H", "e", "l", "o"}
word = "World"

print("\n--- Sets with Strings ---")
print("String Union:            ", str_set.union(word))         # {'H', 'e', 'l', 'o', 'W', 'r', 'd'}
print("String Intersection:     ", str_set.intersection(word))  # {'l', 'o'}
print("String Difference:       ", str_set.difference(word))    # {'H', 'e'}


# --- D. Set Operations with Dictionaries ---
# Passing a dictionary operates on its KEYS by default.
dict_set = {"name", "age"}
d1 = {"name": "John", "age": 25, "city": "New York"}
d2 = {"age": 26, "city": "New York", "country": "USA"}

print("\n--- Sets with Dictionaries ---")
# Union of keys:
print("Dict Keys Union:         ", set(d1).union(d2))          # {'name', 'age', 'city', 'country'}
# Common keys:
print("Dict Keys Intersection:  ", set(d1).intersection(d2))   # {'age', 'city'}
# Keys only in d1:
print("Dict Keys Difference:    ", set(d1).difference(d2))     # {'name'}


# ------------------------------------------------------------------------------
# 3. IN-PLACE SET UPDATE METHODS (MUTATING THE CALLER SET)
# ------------------------------------------------------------------------------
# Instead of creating a new set, these modify the original set in-place:
# - s.update(other)                  : In-place Union (|=)
# - s.intersection_update(other)      : In-place Intersection (&=)
# - s.difference_update(other)        : In-place Difference (-=)
# - s.symmetric_difference_update(other): In-place Symmetric Difference (^=)

num_set = {1, 2, 3}
num_set.update([3, 4, 5])  # Modifies num_set in place
print("\nIn-place updated set: ", num_set)  # Output: {1, 2, 3, 4, 5}
# ==============================================================================