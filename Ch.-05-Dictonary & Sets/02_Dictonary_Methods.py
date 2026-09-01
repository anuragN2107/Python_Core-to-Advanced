# ==============================================================================
#                 PYTHON BASICS: DICTIONARY METHODS 
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. clear()
# ------------------------------------------------------------------------------
# Removes all key-value pairs, leaving the dictionary completely empty ({}).
d3 = {"name": "John", "age": 25, "city": "New York"}
d3.clear()
print("1. clear():", d3)  # Output: {}


# ------------------------------------------------------------------------------
# 2. copy()
# ------------------------------------------------------------------------------
# Returns a shallow copy (an independent dictionary container in memory).
d4 = {"name": "John", "age": 25, "city": "New York"}
d5 = d4.copy()
print("2. copy():", d5)  # Output: {'name': 'John', 'age': 25, 'city': 'New York'}


# ------------------------------------------------------------------------------
# 3. fromkeys(keys_iterable, default_value=None)
# ------------------------------------------------------------------------------
# Creates a new dictionary from a list/sequence of keys, all set to the same value.
d6 = dict.fromkeys(["name", "age", "city"], "New York")
print("3. fromkeys():", d6)
# Output: {'name': 'New York', 'age': 'New York', 'city': 'New York'}


# ------------------------------------------------------------------------------
# 4. get(key, default=None)
# ------------------------------------------------------------------------------
# Safely returns the value for a key. If the key is missing, returns None
# (or the optional custom default value) instead of crashing with a KeyError.
d7 = {"name": "John", "age": 25, "city": "New York"}
print("4a. get('name'):", d7.get("name"))              # Output: John
print("4b. get('gender'):", d7.get("gender"))          # Output: None
print("4c. get('gender', default):", d7.get("gender", "Not Known"))  # Output: Not Known


# ------------------------------------------------------------------------------
# 5. keys()
# ------------------------------------------------------------------------------
# Returns a dynamic view object (`dict_keys`) containing all dictionary keys.
d9 = {"name": "John", "age": 25, "city": "New York"}
print("5. keys():", d9.keys())  # Output: dict_keys(['name', 'age', 'city'])

for key in d9.keys():
    print("  Key:", key)


# ------------------------------------------------------------------------------
# 6. values()
# ------------------------------------------------------------------------------
# Returns a dynamic view object (`dict_values`) containing all dictionary values.
d15 = {"name": "John", "age": 25, "city": "New York"}
print("6. values():", d15.values())  # Output: dict_values(['John', 25, 'New York'])

for value in d15.values():
    print("  Value:", value)


# ------------------------------------------------------------------------------
# 7. items()
# ------------------------------------------------------------------------------
# Returns a dynamic view object (`dict_items`) containing (key, value) tuples.
d8 = {"name": "John", "age": 25, "city": "New York"}
print("7. items():", d8.items())
# Output: dict_items([('name', 'John'), ('age', 25), ('city', 'New York')])

for key, value in d8.items():
    print(f"  {key}: {value}")


# ------------------------------------------------------------------------------
# 8. pop(key, default)
# ------------------------------------------------------------------------------
# Removes the specified KEY and returns its value.
# Note: Dictionaries use keys, NOT positional index numbers (e.g. pop(0) fails unless 0 is a key).
d10 = {"name": "John", "age": 25, "city": "New York"}
removed_name = d10.pop("name")
print("8. pop('name') returned:", removed_name)  # Output: John
print("   d10 after pop:", d10)                  # Output: {'age': 25, 'city': 'New York'}

# Using a fallback to prevent KeyError if key doesn't exist:
missing = d10.pop("salary", "N/A")
print("   pop with fallback:", missing)          # Output: N/A


# ------------------------------------------------------------------------------
# 9. popitem()
# ------------------------------------------------------------------------------
# Removes and returns the LAST inserted (key, value) pair as a tuple (LIFO order).
# Raises KeyError if the dictionary is already empty.
d11 = {"name": "John", "age": 25, "city": "New York"}
last_item = d11.popitem()
print("9. popitem() returned:", last_item)  # Output: ('city', 'New York')
print("   d11 after popitem:", d11)         # Output: {'name': 'John', 'age': 25}


# ------------------------------------------------------------------------------
# 10. setdefault(key, default=None)
# ------------------------------------------------------------------------------
# Returns the value of a key if it exists.
# If the key DOES NOT exist, it inserts the key with the specified default value.
d12 = {"name": "John", "age": 25, "city": "New York"}

# Key 'gender' does not exist -> inserts 'gender': 'Not Known' and returns it:
print("10a. setdefault (new key):", d12.setdefault("gender", "Not Known"))  # Output: Not Known

# Key 'gender' now exists -> returns existing value 'Not Known' (does NOT overwrite):
print("10b. setdefault (existing):", d12.setdefault("gender", "Male"))      # Output: Not Known
print("    d12:", d12)
# Output: {'name': 'John', 'age': 25, 'city': 'New York', 'gender': 'Not Known'}


# ------------------------------------------------------------------------------
# 11. update(other_dict_or_iterable)
# ------------------------------------------------------------------------------
# Updates the dictionary with key-value pairs from another dictionary or iterable.
# Overwrites values for existing keys and inserts new keys.
d13 = {"name": "John", "age": 25, "city": "New York"}
d14 = {"name": "John", "age": 26, "country": "USA"}

d13.update(d14)
print("11. update():", d13)
# Output: {'name': 'John', 'age': 26, 'city': 'New York', 'country': 'USA'}

# Dictionary merge operator alternative (Python 3.9+):
# merged_dict = d13 | d14
#Example:
# d13 = {"name":"John", "age":25, "city":"New York"}
# d14 = {"name":"John", "age":26, "city":"New York"}
# d13 | d14 #prints {'name': 'John', 'age': 26, 'city': 'New York'}
# ==============================================================================