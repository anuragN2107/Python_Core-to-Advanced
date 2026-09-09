# ==============================================================================
#                 PYTHON STRINGS PRACTICE: QUESTIONS & SOLUTIONS
# ==============================================================================

# ------------------------------------------------------------------------------
# Problem 1: Display user entered name followed by "Good Afternoon"
# ------------------------------------------------------------------------------
str1 = "Good Afternoon"
str2 = input("Enter your name: ")
print(str1 + " " + str2)
# Alternative using f-string:
# print(f"Good Afternoon, {str2}!")


# ------------------------------------------------------------------------------
# Problem 2: Fill in a letter template with Name and Date
# ------------------------------------------------------------------------------
letter = """Dear <|Name|>,
You are selected!
<|Date|>"""

name = input("Enter your name: ")
date = input("Enter date (DD/MM/YYYY): ")

# Chain replace() to swap placeholders with user input
letter = letter.replace("<|Name|>", name).replace("<|Date|>", date)

print("\n_______Final Letter_______")
print(letter)


# ------------------------------------------------------------------------------
# Problem 3: Detect double spaces in a string
# ------------------------------------------------------------------------------
# find() returns the first index where "  " appears, or -1 if none is found.
text1 = "Ram is  immortal"
text2 = "Ram is immortal"

print("Index of double space in text1:", text1.find("  "))  # Output: 6
print("Index of double space in text2:", text2.find("  "))  # Output: -1 (No double space)


# ------------------------------------------------------------------------------
# Problem 4: Replace double spaces with single spaces
# ------------------------------------------------------------------------------
text = "Ram is  immortal"
updated_text = text.replace("  ", " ")

print("Original text:", text)
print("Updated text: ", updated_text)


# ------------------------------------------------------------------------------
# Problem 5: Format a letter using escape sequence characters
# ------------------------------------------------------------------------------
# Input string: "Dear Harry, This Python course is nice. Thanks!"
# Using \n (newline) and \t (tab indent)
formatted_letter = "Dear Harry,\n\tThis Python course is nice.\nThanks!"

print(formatted_letter)
# Output:
# Dear Harry,
# 	This Python course is nice.
# Thanks!
# ==============================================================================