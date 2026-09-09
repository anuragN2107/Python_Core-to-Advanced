# ==============================================================================
#         (PART 2): FILE I/O - ADVANCED & CONTEXT MANAGERS
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. BEST PRACTICE: THE `with` STATEMENT (CONTEXT MANAGER)
# ------------------------------------------------------------------------------
# Why use `with`?
# In manual workflows, if your program crashes or you forget to call `file.close()`, 
# the file remains locked in memory, which can lead to data corruption or memory leaks.
# The `with` statement acts as a Context Manager. It automatically handles resource cleanup and ensures `close()` is called safely as soon as the indented block finishes even if an error occurs inside the block.

#What is a Context Manager?
# A Context Manager is a built-in Python object that manages resources, such as files or network connections, in a way that ensures they are properly released, even in the event of an exception.

# Syntax:
#   with open("filename.ext", "mode") as file:
#       # Perform operations on file

print("\n--- 1.(a) Using Context Manager (`with` block) ---")
with open("sample.txt", "r") as file:
    for line_number, line_text in enumerate(file, start=1):
        print(f"Row {line_number}: {line_text.strip()}")
# File is automatically closed here!

#`# To print a specific desired line while using a for loop, use `enumerate()`and to keep track of the line numbers automatically.
print("\n--- 1.(b) Using Context Manager (`with` block) ---")
target_line = int(input("Enter the line number to print: "))
with open("sample.txt", "r") as file:
    for current_line_num, line in enumerate(file, start=1):
        if current_line_num == target_line:
            print(f"Line {target_line}: {line.strip()}")
            break  # Stop looping once the desired line is found`

# ------------------------------------------------------------------------------
# 2. FILE POINTER CONTROL: `tell()` AND `seek()`
# ------------------------------------------------------------------------------
# The file pointer keeps track of where the next read/write action will happen.
# - tell()       : Returns the current byte position of the pointer.
# - seek(offset) : Repositions the pointer to a specific byte index.
# - chunk_size   : When reading in chunks, you can specify how many bytes to read at a time.
print("\n--- 2. tell() & seek() Demo ---")

with open("sample.txt", "r") as file:
    print("Initial pointer position :", file.tell())  # 0

    file.seek(12)  # Moves pointer to byte 12
    print("Position after seek(12)   :", file.tell())  # 12

    file.seek(0)  # Moves pointer back to the beginning of the file
    print("Position after seek(0)    :", file.tell())  # 0

    # Reading from the file pointer
    print("Initial pointer position :", file.tell())  # 0

    chunk = file.read(12)  # Reads 12 characters ("Hello, World")
    print(f"Read text: '{chunk}'")
    print("Position after reading 12:", file.tell())  # 12
    print("Current pointer position :", file.tell())  # 12

    # Reset pointer back to the beginning of the file
    file.seek(0)
    print("Position after file.seek(0) :", file.tell())  # 0
    print("Reread first line          :", file.readline().strip())


# ------------------------------------------------------------------------------
# 3. WRITING MULTIPLE LINES: `writelines()`
# ------------------------------------------------------------------------------
# Writes a list of strings to disk.
# Note: `writelines()` does NOT add newlines automatically; include '\n' manually.

log_entries = [
    "LOG: User logged in\n",
    "LOG: Database connected\n",
    "LOG: Transaction completed\n"
]

with open("app.log", "w") as log_file:
    log_file.writelines(log_entries)

print("\n--- 3. Written Multi-line List to app.log ---")


# ------------------------------------------------------------------------------
# 4. PRACTICAL PRACTICE EXAMPLE
# ------------------------------------------------------------------------------

basic1 = "Anurag Srivastava is going to be top data_analyst"

# Step 1: Write to the file using context manager
with open("myfile.txt", "w") as f:
    f.write(basic1)

# Step 2: Re-open the file in read mode to retrieve data
with open("myfile.txt", "r") as f:
    txt = f.read()

print("\n--- 4. Practical Example Output ---")
print(txt)
