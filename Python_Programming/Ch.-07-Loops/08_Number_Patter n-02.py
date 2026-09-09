# ==============================================================================
# ALPHABET PATTERNS IN PYTHON: FOR LOOP & WHILE LOOP COMPARISON
# Note: chr(65) = 'A', chr(66) = 'B', chr(67) = 'C', and so on.
# Change 'n' to adjust the number of rows (e.g., n = 5 goes up to 'E').
# ==============================================================================

# ==============================================================================
# PATTERN 1: REPEATING ROW ALPHABETS
# A
# B B
# C C C
# D D D D
# E E E E E
# ==============================================================================
n = 5
print("=== PATTERN 1: Repeating Row Alphabets ===")

# --- Using FOR Loop ---
print("\n[Using FOR Loop]")
for i in range(n):
    char = chr(65 + i)
    for j in range(i + 1):
        print(char, end=" ")
    print()

# --- Using WHILE Loop ---
print("\n[Using WHILE Loop]")
i = 0
while i < n:
    char = chr(65 + i)
    j = 0
    while j <= i:
        print(char, end=" ")
        j += 1
    print()
    i += 1


# ==============================================================================
# PATTERN 2: INCREASING COLUMN ALPHABETS
# A
# A B
# A B C
# A B C D
# A B C D E
# ==============================================================================
n = 5
print("\n=== PATTERN 2: Increasing Column Alphabets ===")

# --- Using FOR Loop ---
print("\n[Using FOR Loop]")
for i in range(n):
    for j in range(i + 1):
        print(chr(65 + j), end=" ")
    print()

# --- Using WHILE Loop ---
print("\n[Using WHILE Loop]")
i = 0
while i < n:
    j = 0
    while j <= i:
        print(chr(65 + j), end=" ")
        j += 1
    print()
    i += 1


# ==============================================================================
# PATTERN 3: INVERTED ALPHABET TRIANGLE
# A B C D E
# A B C D
# A B C
# A B
# A
# ==============================================================================
n = 5
print("\n=== PATTERN 3: Inverted Alphabet Triangle ===")

# --- Using FOR Loop ---
print("\n[Using FOR Loop]")
for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

# --- Using WHILE Loop ---
print("\n[Using WHILE Loop]")
i = n
while i >= 1:
    j = 0
    while j < i:
        print(chr(65 + j), end=" ")
        j += 1
    print()
    i -= 1


# ==============================================================================
# PATTERN 4: CONTINUOUS ALPHABETS (FLOYD'S ALPHABET TRIANGLE)
# A
# B C
# D E F
# G H I J
# ==============================================================================
n = 4
print("\n=== PATTERN 4: Continuous Alphabets ===")

# --- Using FOR Loop ---
print("\n[Using FOR Loop]")
char_code = 65
for i in range(1, n + 1):
    for j in range(i):
        print(chr(char_code), end=" ")
        char_code += 1
    print()

# --- Using WHILE Loop ---
print("\n[Using WHILE Loop]")
char_code = 65
i = 1
while i <= n:
    j = 0
    while j < i:
        print(chr(char_code), end=" ")
        char_code += 1
        j += 1
    print()
    i += 1


# ==============================================================================
# PATTERN 5: CENTERED ALPHABET PYRAMID
#     A
#    A B
#   A B C
#  A B C D
# A B C D E
# ==============================================================================
n = 5
print("\n=== PATTERN 5: Centered Alphabet Pyramid ===")

# --- Using FOR Loop ---
print("\n[Using FOR Loop]")
for i in range(n):
    # Spaces for centering
    print(" " * (n - i - 1), end="")
    for j in range(i + 1):
        print(chr(65 + j), end=" ")
    print()

# --- Using WHILE Loop ---
print("\n[Using WHILE Loop]")
i = 0
while i < n:
    # Spaces for centering
    print(" " * (n - i - 1), end="")
    j = 0
    while j <= i:
        print(chr(65 + j), end=" ")
        j += 1
    print()
    i += 1


# ==============================================================================
# PATTERN 6: PALINDROMIC ALPHABET PYRAMID
#         A
#       A B A
#     A B C B A
#   A B C D C B A
# A B C D E D C B A
# ==============================================================================
n = 5
print("\n=== PATTERN 6: Palindromic Alphabet Pyramid ===")

# --- Using FOR Loop ---
print("\n[Using FOR Loop]")
for i in range(n):
    # Leading spaces for alignment
    print("  " * (n - i - 1), end="")
    
    # Increasing characters (A to current)
    for j in range(i + 1):
        print(chr(65 + j), end=" ")
        
    # Decreasing characters back down to A
    for k in range(i - 1, -1, -1):
        print(chr(65 + k), end=" ")
        
    print()

# --- Using WHILE Loop ---
print("\n[Using WHILE Loop]")
i = 0
while i < n:
    # Leading spaces
    print("  " * (n - i - 1), end="")
    
    # Increasing characters
    j = 0
    while j <= i:
        print(chr(65 + j), end=" ")
        j += 1
        
    # Decreasing characters
    k = i - 1
    while k >= 0:
        print(chr(65 + k), end=" ")
        k -= 1
        
    print()
    i += 1