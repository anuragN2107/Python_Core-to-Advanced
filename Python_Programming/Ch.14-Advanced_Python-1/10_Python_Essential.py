# ===============================================================================================================================
#                                       MASTER NOTES: PYTHON ADVANCED ESSENTIALS (PAGE 51)
# ===============================================================================================================================
# This file contains detailed, copyable notes and examples for:
# 1. If __name__ == '__main__' in Python
# 2. The Global Keyword
# 3. Enumerate Function in Python
# 4. List Comprehensions


# ===============================================================================================================================
# PART 1: IF __NAME__ == '__MAIN__' IN PYTHON
# ===============================================================================================================================

# DEFINITION & BEHAVIOR:
# - The special variable `__name__` evaluates to the name of the module in Python from where the program is run[cite: 1].
# - If the module is being run directly from the command line/terminal, `__name__` is set to the string "__main__"[cite: 1].
# - Usage: This behavior is used to check whether a module is being executed directly or being imported into another file[cite: 1].

def main_demo_function():
    print("-> This function runs inside the main module execution block.")

if __name__ == "__main__":
    print("=== PART 1: __name__ == '__main__' Demo ===")
    print(f"Current module __name__ value is: {__name__}")
    main_demo_function()
    print()


# ===============================================================================================================================
# PART 2: THE GLOBAL KEYWORD
# ===============================================================================================================================

# DEFINITION & USAGE:
# - The `global` keyword is used to modify a variable outside of the current local scope[cite: 1] 
#   (i.e., allowing a function to modify a global variable defined at the module level).

counter_variable = 10  # Global variable

def modify_global_variable():
    global counter_variable  # Declaring intention to modify the global scope variable
    counter_variable = 50    # Modifying the global variable directly

print("=== PART 2: The Global Keyword Demo ===")
print(f"Before function call, counter_variable: {counter_variable}")
modify_global_variable()
print(f"After function call, counter_variable: {counter_variable}\n")


# ===============================================================================================================================
# PART 3: ENUMERATE FUNCTION IN PYTHON
# ===============================================================================================================================

# DEFINITION & USAGE:
# - The `enumerate` function adds a counter/index to an iterable and returns it[cite: 1].
# - It allows you to loop over something and have an automatic index counter at the same time.

print("=== PART 3: Enumerate Function Demo ===")
list1 = ["apple", "banana", "cherry"]

# Using enumerate to track both the index (i) and the item simultaneously
for i, item in enumerate(list1):
    print(f"Index {i}: {item}")  # Prints the items of list 1 with their index[cite: 1]
print()


# ===============================================================================================================================
# PART 4: LIST COMPREHENSIONS
# ===============================================================================================================================

# DEFINITION & USAGE:
# - List Comprehension is an elegant, concise way to create new lists based on existing lists[cite: 1].
# - Syntax: [expression for item in iterable if condition]

print("=== PART 4: List Comprehensions Demo ===")

# Original list containing numbers
list1 = [1, 7, 12, 11, 22]

# Creating a new filtered list using list comprehension (keeping items greater than 8)
list2 = [item for item in list1 if item > 8]

print(f"Original list1: {list1}")
print(f"Filtered list2 (items > 8): {list2}")