# ==============================================================================
#                       PYTHON BASICS: STRINGS MASTER GUIDE
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. WHAT IS A STRING?
# ------------------------------------------------------------------------------
# A string is an immutable sequence of Unicode characters enclosed in quotes:
# - Single quotes : 'Hello'
# - Double quotes : "Hello"
# - Triple quotes : '''Hello''' or """Hello""" (supports multi-line strings)
#
# Note on quotes: In Python, single and double quotes function identically.
# Using double quotes allows easy embedding of single quotes (e.g., "It's fine"),
# and single quotes allow embedding double quotes (e.g., 'He said "Hi"').


# ------------------------------------------------------------------------------
# 2. ESCAPE SEQUENCES IN PYTHON
# ------------------------------------------------------------------------------
# An escape sequence consists of a backslash (\) followed by a specific character.
# It is used to insert characters that are illegal, reserved, or non-printable in strings.
#
# Common Escape Sequences:
# | Escape Sequence | Description                          | Example / Output Preview            |
# |-----------------|--------------------------------------|-------------------------------------|
# | \n              | Newline (line break)                 | "Hello\nWorld" -> 2 lines           |
# | \t              | Horizontal Tab (indentation)         | "Name:\tAnurag" -> Name:    Anurag  |
# | \\              | Backslash                            | "C:\\path\\file" -> C:\path\file    |
# | \'              | Single quote inside single quotes    | 'It\'s easy' -> It's easy           |
# | \"              | Double quote inside double quotes    | "He said \"Hi\"" -> He said "Hi"    |
# | \b              | Backspace (erases previous char)     | "Hello \bWorld" -> "HelloWorld"     |
# | \r              | Carriage Return (returns to start)   | "Python\rHi" -> "Hithon"            |
# | \a              | ASCII Bell (alert sound / beep)      | "\a"                                |
# | \ooo            | Octal value (e.g., \110 is 'H')      | "\110\145\154\154\157" -> "Hello"   |
# | \xhh            | Hex value (e.g., \x48 is 'H')        | "\x48\x65\x6c\x6c\x6f" -> "Hello"   |
# | \N{name}        | Unicode character by database name   | "\N{SNAKE}" -> 🐍                  |
# | \uxxxx / \Uxxxxxxxx | 16-bit / 32-bit Unicode hex code | "\u03B1" -> α, "\U0001F600" -> 😀  |

# --- Code Examples of Escape Sequences ---
print("--- ESCAPE SEQUENCES DEMO ---")

# 1. Newline (\n) and Tab (\t)
print("Line 1\nLine 2")
print("Item\tPrice\nApple\t$1.50")

# 2. Escaping quotes (\', \")
print('It\'s a sunny day!')
print("She said, \"Python is awesome!\"")

# 3. Escaping Backslash (\\)
print("File path: C:\\Users\\Anurag\\Documents")

# 4. Backspace (\b) and Carriage Return (\r)
print("Hello \bWorld")   # Removes the trailing space before World
print("abcdef\r123")     # Overwrites "abc" with "123" -> Output: 123def

# 5. Unicode Escape Sequences (\N{}, \u, \U)
print("Unicode by Name: \N{GRINNING FACE}")   # Output: 😀
print("Unicode 16-bit:  \u03C0")              # Output: π (pi)
print("Unicode 32-bit:  \U0001F40D")          # Output: 🐍 (snake)


# ------------------------------------------------------------------------------
# 3. STRING TYPES & LITERAL PREFIXES
# ------------------------------------------------------------------------------

# Standard String with Escape Sequences evaluated:
normal_str = "Hello\nWorld"
print(normal_str)
# Output:
# Hello
# World

# Raw String (r"..." or R"..."): Ignores all escape sequences; treats \ literally
raw_str = r"Hello\nWorld"
print(raw_str)  # Output: Hello\nWorld

regex_or_path = r"C:\new_folder\test.txt"  # Prevents \n and \t from triggering
print(regex_or_path)  # Output: C:\new_folder\test.txt

# Multi-line String: Preserves line breaks and formatting without explicit \n
multi_line_str = """This is line 1.
This is line 2."""
print(multi_line_str)

# Unicode String (Default in Python 3, explicit 'u' prefix is optional)
unicode_str = u"Hello, 你好, مرحبا"

# Formatted String (f-string - Python 3.6+): Embed expressions with {}
name = "Anurag"
age = 25
print(f"Hello, my name is {name} and I am {age} years old.")
# Output: Hello, my name is Anurag and I am 25 years old.

# Byte String (b"..." or B"..."): Sequence of raw 8-bit bytes (ASCII values)
byte_str = b"Hello, World!"
print(byte_str)       # Output: b'Hello, World!'
print(type(byte_str)) # Output: <class 'bytes'>
print(byte_str[0])    # Output: 72 (ASCII integer for 'H')


# ------------------------------------------------------------------------------
# 4. CORE STRING CHARACTERISTICS & BASIC OPERATIONS
# ------------------------------------------------------------------------------

# Immutability: Strings CANNOT be modified in place after creation
text = "Anurag"
# text[0] = "B"  # Raises TypeError: 'str' object does not support item assignment
text = "B" + text[1:]  # Correct approach: creates a brand-new string "Bnurag"

# String Length: len(str)
print("Length:", len("Hello, World!"))  # Output: 13

# Concatenation (+) and Repetition (*)
print("Hello" + " " + "World")  # Output: Hello World
print("Python! " * 3)           # Output: Python! Python! Python! 

# Indexing (Positive: 0 to n-1 | Negative: -1 to -n)
#   Index:   0   1   2   3   4
#   Char:    H   e   l   l   o
#  -Index:  -5  -4  -3  -2  -1
word = "Hello"
print(word[0])   # Output: H (first character)
print(word[-1])  # Output: o (last character)

# Slicing: [start : stop : step] (stop is exclusive)
s = "Hello, World!"
print(s[0:5])    # Output: Hello (index 0 to 4)
print(s[:5])     # Output: Hello (starts from index 0 by default)
print(s[7:])     # Output: World! (goes till the end)
print(s[::2])    # Output: Hlo ol! (step by 2)
print(s[::-1])   # Output: !dlroW ,olleH (reverses string)

# Membership Operators (in / not in)
print("World" in "Hello, World!")       # Output: True
print("Python" not in "Hello, World!")  # Output: True

# Iteration
for char in "Code":
    print(char, end=" ")  # Output: C o d e
print()


# ------------------------------------------------------------------------------
# 5. STRING COMPARISON (LEXICOGRAPHICAL / ASCII ORDER)
# ------------------------------------------------------------------------------
# Strings are compared character by character based on their ASCII/Unicode values.
str1 = "Apple"
str2 = "Banana"
print(str1 == str2)  # Output: False
print(str1 < str2)   # Output: True ('A' has ASCII 65, 'B' has ASCII 66)


# ------------------------------------------------------------------------------
# 6. STRING METHODS: CASE TRANSFORMATIONS
# ------------------------------------------------------------------------------
sample = "hello, WORLD!"
print(sample.upper())       # Output: HELLO, WORLD!
print(sample.lower())       # Output: hello, world!
print(sample.capitalize())  # Output: Hello, world! (capitalizes first character only)
print(sample.title())       # Output: Hello, World! (capitalizes first char of each word)
print(sample.swapcase())    # Output: HELLO, world! (inverts upper/lower cases)


# ------------------------------------------------------------------------------
# 7. STRING METHODS: SEARCHING & COUNTING
# ------------------------------------------------------------------------------
# Difference between find() and index():
# - find()  : Returns the lowest index if found; returns -1 if NOT found.
# - index() : Returns the lowest index if found; raises ValueError if NOT found.

search_str = "Hello, World!"

print(search_str.find("World"))   # Output: 7
print(search_str.find("Python"))  # Output: -1 (safe, does not crash)

print(search_str.index("World"))  # Output: 7
# print(search_str.index("Python")) # Raises ValueError: substring not found

print(search_str.count("l"))       # Output: 3 (counts occurrences of 'l')
print(search_str.startswith("He")) # Output: True
print(search_str.endswith("!"))    # Output: True


# ------------------------------------------------------------------------------
# 8. STRING METHODS: CLEANING & MODIFICATION
# ------------------------------------------------------------------------------
raw_input_text = "  Python Programming  "
print(raw_input_text.strip())   # Output: 'Python Programming' (removes outer spaces)
print(raw_input_text.lstrip())  # Output: 'Python Programming  ' (removes left spaces)
print(raw_input_text.rstrip())  # Output: '  Python Programming' (removes right spaces)

msg = "Hello, World!"
print(msg.replace("World", "Python"))  # Output: Hello, Python!


# ------------------------------------------------------------------------------
# 9. STRING SPLITTING & JOINING
# ------------------------------------------------------------------------------
# split(sep): Splits string into a list of substrings based on delimiter
csv_line = "apple,banana,cherry"
fruits = csv_line.split(",")
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# separator.join(iterable): Joins list elements into a single string
joined_dash = "-".join(fruits)
joined_space = " ".join(fruits)
joined_comma = ",".join(fruits)
joined_custom = " | ".join(fruits)
print(joined_dash)   # Output: apple-banana-cherry
print(joined_space)  # Output: apple banana cherry
print(joined_comma)  # Output: apple,banana,cherry
print(joined_custom) # Output: apple | banana | cherry


# ------------------------------------------------------------------------------
# 10. STRING VALIDATION METHODS (RETURNS BOOLEAN)
# ------------------------------------------------------------------------------
print("Python3".isalnum())        # Output: True  (alphanumeric: letters + digits)
print("Python".isalpha())         # Output: True  (alphabet only)
print("12345".isdigit())          # Output: True  (digits only)
print("   ".isspace())            # Output: True  (whitespace only: spaces, tabs, newlines)
print("var_name".isidentifier())  # Output: True  (valid variable name format)


# ------------------------------------------------------------------------------
# 11. STRING ALIGNMENT & PADDING
# ------------------------------------------------------------------------------
title = "Python"
print(title.center(20, "-"))  # Output: -------Python-------
print(title.ljust(20, "-"))   # Output: Python--------------
print(title.rjust(20, "-"))   # Output: --------------Python
print("42".zfill(5))          # Output: 00042 (pads left with zeros)


# ------------------------------------------------------------------------------
# 12. STRING ENCODING & DECODING
# ------------------------------------------------------------------------------
# Converting string (str) <-> binary (bytes)
text_data = "Hello, World!"
encoded_bytes = text_data.encode("utf-8")
print(encoded_bytes)  # Output: b'Hello, World!'

decoded_text = encoded_bytes.decode("utf-8")
print(decoded_text)   # Output: Hello, World!
# ==============================================================================