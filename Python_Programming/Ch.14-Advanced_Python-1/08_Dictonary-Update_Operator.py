# ===============================================================================================================================
#                                       MASTER NOTES: DICTIONARY UPDATE OPERATOR (|=)
# ===============================================================================================================================

# ===============================================================================================================================
# PART 1: DEFINITION & DIFFERENCE FROM MERGE (`|`)
# ===============================================================================================================================
# - Definition: The Dictionary Update Operator (`|=`) updates an existing dictionary *in-place* 
#   by adding keys and values from another dictionary or iterable.
# - Introduced in: Python 3.9 (PEP 584), alongside the merge operator.
# - Key Difference from `|`: 
#   - `|` creates and returns a **new** dictionary (non-mutating).
#   - `|=` **mutates/changes** the original dictionary directly in memory and returns `None`.


# ===============================================================================================================================
# PART 2: SYNTAX & EXAMPLES
# ===============================================================================================================================
# - Syntax: `existing_dict |= new_dict`

print("=== DEMO: Dictionary Update Operator (|=) ===")

user_permissions = {"read": True, "write": False}
new_settings = {"write": True, "execute": True}  # "write" will be updated

print(f"Before update: {user_permissions}")

# Performing in-place update using |=
user_permissions |= new_settings

print(f"After update (mutated in-place): {user_permissions}")