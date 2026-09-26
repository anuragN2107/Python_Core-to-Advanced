# ===============================================================================================================================
#                                       MASTER NOTES: DICTIONARY MERGE OPERATOR (|)
# ===============================================================================================================================

# ===============================================================================================================================
# PART 1: DEFINITION & HISTORY
# ===============================================================================================================================
# - Definition: The Dictionary Merge Operator (`|`) is used to combine two dictionaries into a brand-new dictionary.
# - Introduced in: Python 3.9 (PEP 584).
# - Why it was added: Before Python 3.9, merging dictionaries required clunky workarounds like `{**dict1, **dict2}` 
#   or using `.update()`, which mutated existing dictionaries. The `|` operator provides a clean, native syntax.


# ===============================================================================================================================
# PART 2: HOW IT WORKS & BEHAVIOR
# ===============================================================================================================================
# - Syntax: `new_dict = dict1 | dict2`
# - Key Overlapping Rule: If both dictionaries share the exact same key, the value from the 
#   **right-hand dictionary** will overwrite the value from the left-hand dictionary.
# - Immutability: Neither `dict1` nor `dict2` is modified; a completely new dictionary object is returned in memory.

print("=== DEMO: Dictionary Merge Operator (|) ===")

dict_a = {"apple": 1, "banana": 2}
dict_b = {"banana": 5, "cherry": 3}  # "banana" is an overlapping key

# Merging dict_a and dict_b using the merge operator
merged_dict = dict_a | dict_b

print(f"Original Dict A: {dict_a}")
print(f"Original Dict B: {dict_b}")
print(f"Merged Result:   {merged_dict}")
# Notice that "banana" took the value 5 from dict_b because right-hand side wins!