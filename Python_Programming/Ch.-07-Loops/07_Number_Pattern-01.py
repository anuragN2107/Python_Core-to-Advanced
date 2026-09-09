# ==============================================================================
# NUMBER PATTERNS IN PYTHON: FOR LOOP & WHILE LOOP COMPARISON
# Change 'n' to adjust the size of the patterns.
# ==============================================================================

# ==============================================================================
# PATTERN 1: REPEATING ROW NUMBERS
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# ==============================================================================
n = 5
print("=== PATTERN 1: Repeating Row Numbers ===")

# --- Using FOR Loop ---
print("\n[Using FOR Loop]")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()

# --- Using WHILE Loop ---
print("\n[Using WHILE Loop]")
i = 1
while i <= n:
    j = 1
    while j <= i:
        print(i, end=" ")
        j += 1
    print()
    i += 1


# ==============================================================================
# PATTERN 2: INCREASING COLUMN NUMBERS
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# ==============================================================================
n = 5
print("\n=== PATTERN 2: Increasing Column Numbers ===")

# --- Using FOR Loop ---
print("\n[Using FOR Loop]")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# --- Using WHILE Loop ---
print("\n[Using WHILE Loop]")
i = 1
while i <= n:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i += 1


# ==============================================================================
# PATTERN 3: INVERTED NUMBER TRIANGLE
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
# ==============================================================================
n = 5
print("\n=== PATTERN 3: Inverted Number Triangle ===")

# --- Using FOR Loop ---
print("\n[Using FOR Loop]")
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# --- Using WHILE Loop ---
print("\n[Using WHILE Loop]")
i = n
while i >= 1:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i -= 1


# ==============================================================================
# PATTERN 4: INVERTED REPEATING ROW NUMBERS
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1
# ==============================================================================
n = 5
print("\n=== PATTERN 4: Inverted Repeating Row Numbers ===")

# --- Using FOR Loop ---
print("\n[Using FOR Loop]")
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()

# --- Using WHILE Loop ---
print("\n[Using WHILE Loop]")
i = n
while i >= 1:
    j = 1
    while j <= i:
        print(i, end=" ")
        j += 1
    print()
    i -= 1


# ==============================================================================
# PATTERN 5: FLOYD'S TRIANGLE (CONTINUOUS COUNTING)
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# ==============================================================================
n = 4
print("\n=== PATTERN 5: Floyd's Triangle ===")

# --- Using FOR Loop ---
print("\n[Using FOR Loop]")
num = 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()

# --- Using WHILE Loop ---
print("\n[Using WHILE Loop]")
num = 1
i = 1
while i <= n:
    j = 1
    while j <= i:
        print(num, end=" ")
        num += 1
        j += 1
    print()
    i += 1


# ==============================================================================
# PATTERN 6: 0-1 ALTERNATING BINARY TRIANGLE
# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1
# ==============================================================================
n = 5
print("\n=== PATTERN 6: 0-1 Binary Triangle ===")

# --- Using FOR Loop ---
print("\n[Using FOR Loop]")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if (i + j) % 2 == 0:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()

# --- Using WHILE Loop ---
print("\n[Using WHILE Loop]")
i = 1
while i <= n:
    j = 1
    while j <= i:
        if (i + j) % 2 == 0:
            print(1, end=" ")
        else:
            print(0, end=" ")
        j += 1
    print()
    i += 1


# ==============================================================================
# PATTERN 7: CENTERED NUMBER PYRAMID
#     1
#    1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5
# ==============================================================================
n = 5
print("\n=== PATTERN 7: Centered Number Pyramid ===")

# --- Using FOR Loop ---
print("\n[Using FOR Loop]")
for i in range(1, n + 1):
    # Print leading spaces
    print(" " * (n - i), end="")
    # Print numbers with trailing space
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# --- Using WHILE Loop ---
print("\n[Using WHILE Loop]")
i = 1
while i <= n:
    # Print leading spaces
    print(" " * (n - i), end="")
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i += 1


# ==============================================================================
# PATTERN 8: PALINDROMIC NUMBER PYRAMID
#         1
#       1 2 1
#     1 2 3 2 1
#   1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1
# ==============================================================================
n = 5
print("\n=== PATTERN 8: Palindromic Number Pyramid ===")

# --- Using FOR Loop ---
print("\n[Using FOR Loop]")
for i in range(1, n + 1):
    # Spaces for alignment
    print("  " * (n - i), end="")
    # Increasing part (1 to i)
    for j in range(1, i + 1):
        print(j, end=" ")
    # Decreasing part (i-1 down to 1)
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()

# --- Using WHILE Loop ---
print("\n[Using WHILE Loop]")
i = 1
while i <= n:
    # Spaces for alignment
    print("  " * (n - i), end="")
    
    # Increasing part
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
        
    # Decreasing part
    k = i - 1
    while k >= 1:
        print(k, end=" ")
        k -= 1
        
    print()
    i += 1