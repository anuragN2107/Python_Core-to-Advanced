# ==============================================================================
#                      PYTHON BASICS: LISTS MASTER GUIDE
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. WHAT IS A LIST?
# ------------------------------------------------------------------------------
# A list is a built-in, mutable data structure that holds an ordered collection
# of items. Elements are enclosed in square brackets `[]` and separated by commas.

list1 = ["Ram", "Bibhu", 1, 4, False, 4.6]
print(list1)
print(type(list1))  # Output: <class 'list'>


# ------------------------------------------------------------------------------
# 2. KEY CHARACTERISTICS OF PYTHON LISTS
# ------------------------------------------------------------------------------
# - Ordered       : Elements maintain their defined insertion order.
# - Mutable       : You can modify, add, replace, or delete items in place.
# - Allows Copies : Lists can contain duplicate elements.
# - Heterogeneous : Can store mixed data types together (even other lists).
# - Dynamic Size  : Automatically grows and shrinks as items are added/removed.

# A list of integers
numbers = [1, 2, 3, 4, 5]

# A list of strings
fruits = ["apple", "banana", "cherry"]

# A list with mixed data types
mixed_list = [42, "hello", 3.14, True]

# A nested list (list inside a list)
list2 = [1, "Ram", True, [1, 2, 3]]
print(list2)

# An empty list
empty_list = []
# Alternative: empty_list = list()


# ------------------------------------------------------------------------------
# 3. LIST INDEXING (POSITIVE & NEGATIVE)
# ------------------------------------------------------------------------------
# Positive indexing starts from 0 (left-to-right).
# Negative indexing starts from -1 (right-to-left).
#
# Index Map for list1:
# Values:         ["Ram", "Bibhu",   1,     4,   False,  4.6 ]
# Positive Index:    0       1       2      3      4      5
# Negative Index:   -6      -5      -4     -3     -2     -1

list1 = ["Ram", "Bibhu", 1, 4, False, 4.6]

# Positive Indexing
print(list1[0])   # Output: Ram
print(list1[1])   # Output: Bibhu
print(list1[2])   # Output: 1
print(list1[3])   # Output: 4
print(list1[4])   # Output: False
print(list1[5])   # Output: 4.6

# Negative Indexing
print(list1[-1])  # Output: 4.6
print(list1[-2])  # Output: False
print(list1[-3])  # Output: 4
print(list1[-4])  # Output: 1


# ------------------------------------------------------------------------------
# 4. LIST SLICING: list[start : stop : step]
# ------------------------------------------------------------------------------
# - start : Starting index (included)
# - stop  : Ending index (excluded)
# - step  : Increment step size (default is 1)

print(list1[0:2])  # Output: ['Ram', 'Bibhu']
print(list1[2:4])  # Output: [1, 4]
print(list1[4:6])  # Output: [False, 4.6]
print(list1[::2])  # Output: ['Ram', 1, False] (every 2nd item)
print(list1[::-1]) # Output: [4.6, False, 4, 1, 'Bibhu', 'Ram'] (reverses list)


# ------------------------------------------------------------------------------
# 5. DEMONSTRATING MUTABILITY (IN-PLACE MODIFICATION)
# ------------------------------------------------------------------------------
# Unlike strings and tuples, list items can be changed directly.

items = ["A", "B", "C"]
items[0] = "Z"     # Updating an element
print(items)       # Output: ['Z', 'B', 'C']


# ------------------------------------------------------------------------------
# 6. ESSENTIAL LIST METHODS & OPERATIONS
# ------------------------------------------------------------------------------
demo = [10, 20, 30]

# Adding elements
demo.append(40)          # Adds 40 to the end -> [10, 20, 30, 40]
demo.insert(1, 15)       # Inserts 15 at index 1 -> [10, 15, 20, 30, 40]
demo.extend([50, 60])    # Merges another list -> [10, 15, 20, 30, 40, 50, 60]

# Removing elements
demo.remove(15)          # Removes first occurrence of value 15 # Output: None
popped_val = demo.pop()  # Removes and returns the last element (60) # Output: 60
popped_val = demo.pop(1) # Removes and returns the element at index 1 (20) # Output: 20 
# del demo[0]            # Deletes item at index 0

# Utility methods
print("Length of list:", len(demo))       # Number of elements # Output: 7
print("Max value:     ", max(demo))       # Maximum value      # Output: 60
print("Min value:     ", min(demo))       # Minimum value      # Output: 10
print("Count of 20:   ", demo.count(20))   # Frequency of value # Output: 2
print("Index of 30:   ", demo.index(30))   # Position of value # Output: 2
# ==============================================================================