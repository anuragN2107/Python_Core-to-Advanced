# ==============================================================================
#                      PYTHON BASICS: SET METHODS 
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. ADDING & UPDATING ELEMENTS
# ------------------------------------------------------------------------------

# add(elem): Adds a single element to the set
s4 = set()
s4.add(1)
s4.add(2)
s4.add(3)
print("1. add():", s4)  # Output: {1, 2, 3}

# update(iterable): Adds multiple elements from any iterable
s5 = set()
s5.update([1, 2, 3, 4, 5])
print("2. update():", s5)  # Output: {1, 2, 3, 4, 5}


# ------------------------------------------------------------------------------
# 2. REMOVING ELEMENTS (remove vs. discard vs. pop vs. clear)
# ------------------------------------------------------------------------------
# - remove(val)  : Removes the item; raises KeyError if the item is not found!
# - discard(val) : Removes the item; does nothing (safe) if the item is not found.
# - pop()        : Removes and returns an arbitrary item (raises KeyError if empty).
# - clear()      : Removes all elements from the set.

s6 = {1, 2, 3, 4, 5}
s6.remove(2)     # Removes 2
s6.discard(4)    # Removes 4
s6.discard(99)   # Safe: 99 is not present, no error raised
print("3. remove/discard:", s6)  # Output: {1, 3, 5}

s26 = {1, 2, 3, 4, 5}
popped_val = s26.pop()
print("4. pop():", popped_val, "| Remaining:", s26)

s7 = {1, 2, 3, 4, 5}
s7.clear()
print("5. clear():", s7)  # Output: set()


# ------------------------------------------------------------------------------
# 3. SET OPERATIONS: RETURNING A NEW SET (Methods vs. Operators)
# ------------------------------------------------------------------------------
# Note:
# - Methods (e.g. .union()) accept ANY iterable (list, tuple, string, dict).
# - Operators (|, &, -, ^) require BOTH sides to be actual `set` instances.

A = {1, 2, 3, 4, 5}
B = {2, 3, 4, 5, 6}

# Union (|): Combines elements from both sets
print("6. Union (A | B):", A.union(B))  # Output: {1, 2, 3, 4, 5, 6}

# Intersection (&): Keeps elements present in BOTH sets
print("7. Intersection (A & B):", A.intersection(B))  # Output: {2, 3, 4, 5}

# Difference (-): Keeps elements in A that are NOT in B
print("8. Difference (A - B):", A.difference(B))  # Output: {1}

# Symmetric Difference (^): Keeps elements in A or B, but NOT in both
print("9. Symmetric Difference (A ^ B):", A.symmetric_difference(B))  # Output: {1, 6}


# ------------------------------------------------------------------------------
# 4. IN-PLACE UPDATE METHODS (Modifies the original set)
# ------------------------------------------------------------------------------

# difference_update (-=): Removes all elements found in the second set
s_diff = {1, 2, 3, 4, 5}
s_diff.difference_update({2, 3, 4, 5, 6})
print("10. difference_update (-=):", s_diff)  # Output: {1}

# intersection_update (&=): Retains only common elements
s_inter = {1, 2, 3, 4, 5}
s_inter.intersection_update({2, 3, 4, 5, 6})
print("11. intersection_update (&=):", s_inter)  # Output: {2, 3, 4, 5}

# symmetric_difference_update (^=): Keeps elements in either, but not both
s_sym = {1, 2, 3, 4, 5}
s_sym.symmetric_difference_update({2, 3, 4, 5, 6})
print("12. symmetric_difference_update (^=):", s_sym)  # Output: {1, 6}

# update (|=): In-place union
s_union = {1, 2, 3}
s_union |= {3, 4, 5}
print("13. update (|=):", s_union)  # Output: {1, 2, 3, 4, 5}


# ------------------------------------------------------------------------------
# 5. SET COMPARISONS & RELATIONSHIPS (Returns Boolean)
# ------------------------------------------------------------------------------
s_a = {1, 2, 3}
s_b = {1, 2, 3, 4, 5}
s_c = {7, 8, 9}

# isdisjoint(): True if two sets share NO common elements
print("14. isdisjoint (s_a, s_b):", s_a.isdisjoint(s_b))  # Output: False
print("    isdisjoint (s_a, s_c):", s_a.isdisjoint(s_c))  # Output: True

# issubset (<=): True if all elements of s_a exist in s_b
print("15. issubset (s_a <= s_b):", s_a.issubset(s_b))    # Output: True

# issuperset (>=): True if s_b contains all elements of s_a
print("16. issuperset (s_b >= s_a):", s_b.issuperset(s_a))  # Output: True

# Proper Subset (<) and Proper Superset (>):
# A proper subset means s_a is a subset of s_b, but s_a != s_b
print("17. Proper Subset (s_a < s_b):", s_a < s_b)          # Output: True
print("    Proper Superset (s_b > s_a):", s_b > s_a)        # Output: True


# ------------------------------------------------------------------------------
# 6. UTILITY METHODS & OPERATOR DUNDER MAPPING
# ------------------------------------------------------------------------------
# Copying
s_orig = {1, 2, 3}
s_copy = s_orig.copy()
print("18. copy():", s_copy)  # Output: {1, 2, 3}

# Membership test (in / not in -> calls __contains__)
print("19. Membership (1 in s_orig):", 1 in s_orig)  # Output: True

# Length (calls __len__)
print("20. Length:", len(s_orig))  # Output: 3

# Iteration (calls __iter__)
print("21. Iteration: ", end="")
for x in s_orig:
    print(x, end=" ")
print()

# Note on Hashing:
# Standard sets are mutable and UNHASHABLE (calling hash(set()) raises TypeError).
# If you need a hashable set, use `frozenset()`.
# ==============================================================================