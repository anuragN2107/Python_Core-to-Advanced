# ===============================================================================================================================
#                                       CHAPTER 12 - PRACTICE SET: ADVANCED PYTHON
# ===============================================================================================================================
# This file contains solutions for all 5 practice set problems, complete with questions, code implementations, 
# and brief explanations using comments.


# ===============================================================================================================================
# PROBLEM 1: Handling Missing Files Gracefully
# ===============================================================================================================================
# Question: Write a program to open three files 1.txt, 2.txt and 3.txt. If any of these files are not present, 
# a message without exiting the program must be printed prompting the same.

print("=== PROBLEM 1: File Exception Handling ===")

# List of files to attempt opening
files_to_open = ["1.txt", "2.txt", "3.txt"]

for filename in files_to_open:
    try:
        # Attempt to open each file in read mode
        with open(filename, "r") as file:
            print(f"Successfully opened {filename}")
    except FileNotFoundError:
        # Catch the exception so the program doesn't crash/exit, and print a warning message
        print(f"Warning: The file '{filename}' is not present.")

print()


# ===============================================================================================================================
# PROBLEM 2: Using `enumerate` for Specific List Elements
# ===============================================================================================================================
# Question: Write a program to print third, fifth and seventh element from a list using enumerate function.

print("=== PROBLEM 2: Enumerate Function Usage ===")

# Creating a sample list with at least 7 elements
sample_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Enumerate provides both index and item. Remember Python lists are 0-indexed:
# - 3rd element is at index 2
# - 5th element is at index 4
# - 7th element is at index 6
for index, item in enumerate(sample_list):
    if index in [2, 4, 6]:
        print(f"Element at index {index} (Position {index + 1}): {item}")

print()


# ===============================================================================================================================
# PROBLEM 3: List Comprehension for Multiplication Table
# ===============================================================================================================================
# Question: Write a list comprehension to print a list which contains the multiplication table of a user entered number.

print("=== PROBLEM 3: List Comprehension Multiplication Table ===")

# Simulated user input (change or use int(input()) for real interactive execution)
user_number = 5

# List comprehension generates the table values from multiplier 1 to 10
multiplication_table = [user_number * i for i in range(1, 11)]

print(f"Multiplication table of {user_number}: {multiplication_table}\n")


# ===============================================================================================================================
# PROBLEM 4: Handling ZeroDivisionError
# ===============================================================================================================================
# Question: Write a program to display a/b where a and b are integers. If b = 0 display infinite by handling 'ZeroDivisionError'.

print("=== PROBLEM 4: Division with ZeroDivisionError Handling ===")

def safe_division(a: int, b: int):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        # Handle division by zero gracefully and return custom message
        return "infinite"

# Testing the function
print(f"10 / 2 = {safe_division(10, 2)}")
print(f"10 / 0 = {safe_division(10, 0)}")
print()


# ===============================================================================================================================
# PROBLEM 5: Storing Multiplication Tables in a File
# ===============================================================================================================================
# Question: Store the multiplication tables generated in problem 3 in a file named Tables.txt.

print("=== PROBLEM 5: Writing Tables to a File ===")

num_to_table = 5
# Generate table using list comprehension
table_list = [num_to_table * i for i in range(1, 11)]

# Write the formatted table data into 'Tables.txt'
filename = "Tables.txt"
with open(filename, "w") as f:
    f.write(f"--- Multiplication Table of {num_to_table} ---\n")
    for value in table_list:
        f.write(f"{value}\n")

print(f"Successfully wrote the multiplication table of {num_to_table} into '{filename}'.")