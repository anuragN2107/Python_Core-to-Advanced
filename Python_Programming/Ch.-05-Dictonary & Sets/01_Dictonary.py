# ==============================================================================
#                 PYTHON BASICS: DICTIONARIES MASTER GUIDE
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. WHAT IS A DICTIONARY?
# ------------------------------------------------------------------------------
# A dictionary is a built-in data structure that stores data in key-value pairs.
# It uses curly braces `{}` with keys and values separated by a colon `:`,
# and pairs separated by commas `,`.
#
# Analogies:
# - Hash Map / Hash Table (C++ / Java)
# - Object / Associative Array (JavaScript / PHP)

my_dict = {
    "name": "John",
    "age": 25,
    "city": "New York"
}
print(my_dict["name"])  # Output: John
print(my_dict["age"])   # Output: 25
print(my_dict["city"])  # Output: New York
print(type(my_dict))    # Output: <class 'dict'>


# ------------------------------------------------------------------------------
# 2. KEY CHARACTERISTICS OF DICTIONARIES
# ------------------------------------------------------------------------------
# - Ordered       : Preserves insertion order (standard since Python 3.7+).
# - Mutable       : Can add, edit, or remove key-value pairs in place.
# - Unique Keys   : Keys cannot be duplicated. A duplicate key overwrites the old value.
# - Key Rules     : Keys MUST be immutable/hashable (str, int, float, tuple).
#                   Lists and sets CANNOT be used as keys.
# - Any Value     : Values can be of ANY data type (integers, strings, lists, dicts).
# - Fast Lookups  : Key search, insertion, and deletion operate in O(1) average time.


# ------------------------------------------------------------------------------
# 3. COMPLETE CRUD CHEAT SHEET (CREATE, READ, UPDATE, DELETE)
# ------------------------------------------------------------------------------

# --- 1. CREATE ---
empty_dict_1 = {}           # Standard literal syntax
empty_dict_2 = dict()       # Using dict() constructor
user = {
    "name": "Alice",
    "age": 25,
    "role": "Developer"
}

# --- 2. READ (Access Data) ---
# Direct indexing (Raises KeyError if key does NOT exist):
print(user["name"])         # Output: Alice

# .get(key, default) (Safer: Returns None or fallback value instead of crashing):
print(user.get("age"))                 # Output: 25
print(user.get("salary"))              # Output: None (no crash)
print(user.get("salary", "Not Found")) # Output: Not Found

# --- 3. UPDATE / ADD ---
user["age"] = 26             # Updates existing key
user["email"] = "a@test.com" # Adds new key-value pair

# Using .update() to add/update multiple items at once:
user.update({"city": "Berlin", "age": 27})

# --- 4. DELETE ---
removed_role = user.pop("role")   # Removes key 'role' and returns its value
del user["email"]                 # Deletes key 'email' directly
last_item = user.popitem()        # Removes & returns last inserted pair (key, value)
# user.clear()                    # Empties the entire dictionary: {}


# ------------------------------------------------------------------------------
# 4. ESSENTIAL DICTIONARY METHODS & ITERATION
# ------------------------------------------------------------------------------
sample = {"a": 1, "b": 2, "c": 3}

# Viewing Keys, Values, and Pairs:
print(sample.keys())    # Output: dict_keys(['a', 'b', 'c'])
print(sample.values())  # Output: dict_values([1, 2, 3])
print(sample.items())   # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])

# Iterating over a dictionary:
print("\n--- Iteration Demo ---")
for key, value in user.items():
    print(f"{key}: {value}")


# ------------------------------------------------------------------------------
# 5. MEMBERSHIP & EXISTENCE CHECKS
# ------------------------------------------------------------------------------
d1 = {"name": "John", "age": 25, "city": "New York"}
del d1["name"]  # d1 is now: {'age': 25, 'city': 'New York'}

# 1. Check if a KEY exists (searches keys by default):
if "name" in d1:
    print("name is present in d1")
else:
    print("name is not present in d1")  # Executes

# 2. Check if a VALUE exists:
if 25 in d1.values():
    print("Value 25 is present in d1")

# 3. Check if key exists AND its value is not None:
if "name" in d1 and d1["name"] is not None:
    print("name is present and value is not None")
else:
    print("name is missing or value is None")  # Executes

# 4. Check if dictionary is empty or has items:
if d1:
    print(f"Dictionary has {len(d1)} items")  # len() gives total key-value pairs
else:
    print("Dictionary is empty")


# ------------------------------------------------------------------------------
# 6. NESTED DICTIONARIES
# ------------------------------------------------------------------------------
# Dictionaries can store other dictionaries to represent complex, structured data.
employees = {
    "emp1": {"name": "Anurag", "role": "Engineer"},
    "emp2": {"name": "Harry", "role": "Trainer"}
}

print(employees["emp1"]["name"])  # Output: Anurag
# ==============================================================================