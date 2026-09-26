# ===============================================================================================================================
#                                       PRACTICE EXERCISES: DICTIONARY MERGE & UPDATE
# ===============================================================================================================================
# This file contains practice exercises covering both `|` and `|=` operators with clear comments.


# ===============================================================================================================================
# EXERCISE 1: Basic Non-Destructive Merge
# ===============================================================================================================================
# Problem: Merge two configuration dictionaries (`default_config` and `user_config`) using `|`. 
# Ensure that the original dictionaries remain unchanged.

default_config = {"theme": "light", "notifications": True, "timeout": 30}
user_config = {"theme": "dark", "timeout": 60}

# Merging into a new dictionary
final_config = default_config | user_config

print(f"Exercise 1 Result - Final Config: {final_config}")
print(f"Exercise 1 Check - Default Unchanged: {default_config['theme'] == 'light'}\n")


# ===============================================================================================================================
# EXERCISE 2: In-Place Profile Update
# ===============================================================================================================================
# Problem: You have an active user session dictionary. Update it in-place using `|=` with 
# newly fetched account details from a database.

session_data = {"user_id": 402, "role": "Guest", "active": True}
db_updates = {"role": "Administrator", "last_login": "2026-09-26"}

# Mutate session_data in-place
session_data |= db_updates

print(f"Exercise 2 Result - Updated Session: {session_data}\n")


# ===============================================================================================================================
# EXERCISE 3: Merging Multiple Dictionaries
# ===============================================================================================================================
# Problem: Combine three separate tracking data sources into a single unified report dictionary 
# using chained merge operators (`|`).

source_one = {"visitors": 1500}
source_two = {"clicks": 320, "visitors": 1800}  # Overlaps visitors
source_three = {"conversions": 45}

# Chaining the merge operator (evaluated left-to-right)
unified_report = source_one | source_two | source_three

print(f"Exercise 3 Result - Unified Report: {unified_report}\n")


# ===============================================================================================================================
# EXERCISE 4: Updating with Key-Value Tuples
# ===============================================================================================================================
# Problem: The `|=` operator can also accept an iterable of key-value pairs (like a list of tuples). 
# Update a inventory dictionary using a list of tuple updates.

inventory = {"apples": 10, "bananas": 15}
restock_tuples = [("bananas", 30), ("oranges", 25)]

# Updating inventory in-place using tuples
inventory |= restock_tuples

print(f"Exercise 4 Result - Restocked Inventory: {inventory}")