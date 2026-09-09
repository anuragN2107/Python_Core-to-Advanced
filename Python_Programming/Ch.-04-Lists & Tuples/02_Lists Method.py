# ==============================================================================
#                 PYTHON BASICS: LIST METHODS & OPERATIONS
# ==============================================================================

# Initial sample list
list1 = ["Ram", "Bibhu", 1, 4, False, 4.6]


# ------------------------------------------------------------------------------
# 1. append(item)
# ------------------------------------------------------------------------------
# Adds a single element to the very end of the list (Modifies in-place).
list1.append("Anurag")
print("1. append():", list1)
# Output: ['Ram', 'Bibhu', 1, 4, False, 4.6, 'Anurag']


# ------------------------------------------------------------------------------
# 2. extend(iterable)
# ------------------------------------------------------------------------------
# Iterates over another collection and adds each item to the end of the list.
list2 = ["Harry", "John"]
list1.extend(list2)
print("2. extend():", list1)
# Output: ['Ram', 'Bibhu', 1, 4, False, 4.6, 'Anurag', 'Harry', 'John']


# ------------------------------------------------------------------------------
# 3. insert(index, item)
# ------------------------------------------------------------------------------
# Inserts an element at a specific index, shifting existing items to the right.
list1.insert(2, "Harry")  # Inserts "Harry" at index 2
print("3. insert():", list1)
# Output: ['Ram', 'Bibhu', 'Harry', 1, 4, False, 4.6, 'Anurag', 'Harry', 'John']


# ------------------------------------------------------------------------------
# 4. remove(value)
# ------------------------------------------------------------------------------
# Removes the FIRST occurrence of a specified value (raises ValueError if not found).
list1.remove("Harry")  # Removes the first "Harry" at index 2
print("4. remove():", list1)
# Output: ['Ram', 'Bibhu', 1, 4, False, 4.6, 'Anurag', 'Harry', 'John']


# ------------------------------------------------------------------------------
# 5. pop(index=-1)
# ------------------------------------------------------------------------------
# Removes and returns the element at the specified index.
# If no index is given, it removes and returns the LAST element (default).
removed_first = list1.pop(0)  # Removes and returns element at index 0 ('Ram')
print("5. pop(0) returned:", removed_first)
print("   list1 after pop:", list1)
# Output: ['Bibhu', 1, 4, False, 4.6, 'Anurag', 'Harry', 'John']


# ------------------------------------------------------------------------------
# 6. index(value, start=0, stop=len)
# ------------------------------------------------------------------------------
# Returns the zero-based index of the first occurrence of a value.
# Raises ValueError if the item is not present.
idx = list1.index("Harry")
print("6. index('Harry'):", idx)  # Output: 6


# ------------------------------------------------------------------------------
# 7. count(value)
# ------------------------------------------------------------------------------
# Returns the total number of times an element appears in the list.
cnt = list1.count("Harry")
print("7. count('Harry'):", cnt)  # Output: 1


# ------------------------------------------------------------------------------
# 8. sort(key=None, reverse=False) vs sorted(iterable)
# ------------------------------------------------------------------------------
# - list.sort()   : Sorts the original list IN-PLACE (returns None).
# - sorted(list)  : Returns a BRAND-NEW sorted list (leaves original unchanged).
# Note: Elements must be comparable (sorting ints + strings raises a TypeError).

list3 = [6, 4, 8, 11, 85, 96]

# Ascending order
list3.sort()
print("8a. sort() Ascending: ", list3)  # Output: [4, 6, 8, 11, 85, 96]

# Descending order
list3.sort(reverse=True)
print("8b. sort() Descending:", list3)  # Output: [96, 85, 11, 8, 6, 4]

# Using sorted() for non-destructive sorting
list_a = [4, 1, 3, 2]
new_sorted_list = sorted(list_a)
print("8c. sorted() New List:", new_sorted_list)  # Output: [1, 2, 3, 4]
print("    Original list_a: ", list_a)           # Output: [4, 1, 3, 2]


# ------------------------------------------------------------------------------
# 9. reverse()
# ------------------------------------------------------------------------------
# Reverses the elements of the list IN-PLACE.
list1.reverse()
print("9. reverse():", list1)
# Output: ['John', 'Harry', 'Anurag', 4.6, False, 4, 1, 'Bibhu']


# ------------------------------------------------------------------------------
# 10. copy()
# ------------------------------------------------------------------------------
# Creates a shallow copy of the list (independent container in memory).
list_copy = list1.copy()
print("10. copy():", list_copy)


# ------------------------------------------------------------------------------
# 11. clear()
# ------------------------------------------------------------------------------
# Removes all items from the list, leaving it completely empty ([]).
list1.clear()
print("11. clear():", list1)  # Output: []


# ------------------------------------------------------------------------------
# 12. BUILT-IN UTILITY FUNCTIONS FOR LISTS: max(), min(), len(), sum()
# ------------------------------------------------------------------------------
list4 = [10, 45, 2, 89, 23]

print("12. max():", max(list4))  # Largest item  -> Output: 89
print("13. min():", min(list4))  # Smallest item -> Output: 2
print("14. len():", len(list4))  # Total count   -> Output: 5
print("15. sum():", sum(list4))  # Total sum     -> Output: 169


# ------------------------------------------------------------------------------
# 13. MODIFYING ELEMENTS IN A LIST (MUTABILITY)
# ------------------------------------------------------------------------------
# Assign a new value to a specific index using the assignment operator (=).
list5 = [1, 2, 3, 4, 5]
list5[0] = 10  # Changes index 0 from 1 to 10
print("16. Modified List:", list5)  # Output: [10, 2, 3, 4, 5]
# ==============================================================================