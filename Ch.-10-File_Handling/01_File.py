# ==============================================================================
#             CHAPTER 10 (PART 1): FILE I/O - BASICS & MANUAL WORKFLOW
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. MEMORY FUNDAMENTALS: WHY DO WE NEED FILES?
# ------------------------------------------------------------------------------
# When a Python program runs, all its variables and data structures exist in RAM.
# To keep data permanently even after the program stops or the computer shuts down,we store it in files on non-volatile storage (HDD/SSD).
#
# Memory Concepts:
# - RAM (Random Access Memory) : Volatile (data is lost when powered off), ultra-fast.
# - HDD / SSD (Storage)        : Non-volatile (data is permanently saved), mass storage.
#
# Definition of a File:
# A file is a named container on storage (HDD/SSD) used to store and persist data.
# Note:- Difference between HDD and SSD: HDD is slower but more durable, SSD is faster but less durable.
#
# Data Flow:
#   Python Program (RAM)  ---> [Write / Save] --->  File on Disk (Storage)
#   Python Program (RAM)  <--- [Read / Load]  <---  File on Disk (Storage)


# ------------------------------------------------------------------------------
# 2. TYPES OF FILES IN PYTHON
# ------------------------------------------------------------------------------
# 1. Text Files (.txt, .py, .csv, .json, .log, .md):
#    - Stores human-readable characters encoded in standard formats like UTF-8.(#UTF-8 is the most common encoding standard for text files.)
#
# 2. Binary Files (.jpg, .png, .mp4, .pdf, .zip, .exe):
#    - Stores raw bytes (0s and 1s) representing custom structures.
#    - Handled using binary flags ("rb", "wb", "ab").


# ------------------------------------------------------------------------------
# 3. FILE OPENING MODES CHEAT SHEET
# ------------------------------------------------------------------------------
# Syntax: file = open("filename.ext", "mode")
#
# | Mode  | Description                 | Pointer  | Creates If Missing? | Overwrites Existing? |
# |-------|-----------------------------|----------|---------------------|----------------------|
# | "r"   | Read Only (Default)         | Start    | No (Raises Error)   | No                   |
# | "w"   | Write Only (Truncate)       | Start    | Yes                 | Yes (Erases content) |
# | "a"   | Append Only (Add to end)    | End      | Yes                 | No (Preserves data)  |
# | "x"   | Exclusive Creation          | Start    | Yes (Errors if exists)| No                 |
# | "r+"  | Read and Write              | Start    | No (Raises Error)   | No (Overwrites text) |
# | "w+"  | Write and Read              | Start    | Yes                 | Yes (Truncates)      |
# | "a+"  | Append and Read             | End      | Yes                 | No (Preserves data)  |
# | "rb"  | Read Binary                 | Start    | No (Raises Error)   | No                   |
# | "wb"  | Write Binary                | Start    | Yes                 | Yes (Truncates)      |


# ------------------------------------------------------------------------------
# 4. HOW TO CREATE A FILE IN PYTHON
# ------------------------------------------------------------------------------
# There are three primary modes to create a file:
# 1: "w" mode (Write Mode): Opens file for writing, creates it if missing, or overwrites/erases existing content.
# 2: "a" mode (Append Mode): Opens file for appending to the end, creates it if missing, and preserves old content.
# 3: "x" mode (Exclusive Creation Mode): Creates a brand new file, but raises an error if the file already exists.
# 4: "+" mode (Modifier/Read and Write): Opens file for reading and writing, creates it if missing, and preserves old content.
# 5: "rb" mode (Read Binary): Opens file for reading in binary mode, creates it if missing, and preserves old content.
# 6: "wb" mode (Write Binary): Opens file for writing in binary mode, creates it if missing, and overwrites existing content.
# 7: "rt" mode (Read Text): Opens file for reading in text mode, creates it if missing, and preserves old content.
# 8: "wt" mode (Write Text): Opens file for writing in text mode, creates it if missing, and overwrites existing content.

# Method 1: Creating with "w" mode (Write Mode) 
file_w = open("created_with_w.txt", "w")
file_w.write("Created using write mode.")
file_w.close()

# Method 2: Creating with "a" mode (Append Mode)
file_a = open("created_with_a.txt", "a")
file_a.write("Created using append mode.")
file_a.close()

# Method 3: Creating with "x" mode (Uncomment if file doesn't exist yet) (Exclusive Creation Mode)
file_x = open("created_with_x.txt", "x")
file_x.write("Created exclusively using 'x' mode.")
file_x.close()

# Method 4: Creating with "+" mode (Read and Write)
file_rw = open("created_with_rw.txt", "+")
file_rw.write("Created using read and write mode.")
file_rw.close()

# Method 5: Creating with "rb" mode (Read Binary)
file_rb = open("created_with_rb.txt", "rb")
file_rb.write("Created using read binary mode.")
file_rb.close()

# Method 6: Creating with "wb" mode (Write Binary)
file_wb = open("created_with_wb.txt", "wb")
file_wb.write(b"Created using write binary mode.")
file_wb.close()

# Method 7: Creating with "rt" mode (Read Text)
file_rt = open("created_with_rt.txt", "rt")
file_rt.write("Created using read text mode.")
file_rt.close()

# Method 8: Creating with "wt" mode (Write Text)
file_wt = open("created_with_wt.txt", "wt")
file_wt.write("Created using write text mode.")
file_wt.close()
# ------------------------------------------------------------------------------
# 5. BASIC MANUAL WORKFLOW: open(), write(), read(), close()
# ------------------------------------------------------------------------------

# --- Step A: Writing to a File ("w") ---
file = open("sample.txt", "w")
file.write("Hello, World!\nWelcome to Python File I/O.\nThird line of sample file.")
file.close()  # Flushes buffer and releases system lock

# --- Step B: Reading the Entire File ("r") ---
file = open("sample.txt", "r")
content = file.read()  # Loads entire file content as a single string
print("--- 1. Entire File Content (file.read()) ---")
print(content)
file.close()

# --- Step C: Appending to a File ("a") ---
file = open("sample.txt", "a")
file.write("\nThis fourth line was appended safely.")
file.close()


# ------------------------------------------------------------------------------
# 6. METHODS FOR READING FILES
# ------------------------------------------------------------------------------

# Method 1: read(size) - Reads a specific number of characters
file = open("sample.txt", "r")
first_five_chars = file.read(5)
print("\n--- 2. Reading Partial Characters ---")
print("First 5 characters:", first_five_chars)  # "Hello"
file.close()

# Method 2: readline() - Reads one single line at a time
file = open("sample.txt", "r")
print("\n--- 3. Reading Line-by-Line (file.readline()) ---")
print("Line 1:", file.readline().strip())
print("Line 2:", file.readline().strip())
file.close()

# Method 3: readlines() - Reads all lines and returns a LIST of strings
file = open("sample.txt", "r")
lines_list = file.readlines()
print("\n--- 4. Reading All Lines as List (file.readlines()) ---")
print("Lines as list:", lines_list)
file.close()

# Method 4: Looping directly over the file object (Memory-efficient)
file = open("sample.txt", "r")
print("\n--- 5. Direct Loop over File Object ---")
for line in file:
    print(line.strip())
file.close()

