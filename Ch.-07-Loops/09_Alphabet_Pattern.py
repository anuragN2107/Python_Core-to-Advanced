# ==============================================================================
#     NUMBER PATTERNS IN PYTHON (BOTH FOR & WHILE LOOPS)
#      Change the value of 'n' to test different sizes.
# ==============================================================================


# ==============================================================================
# PATTERN 1: Counting Numbers Triangle
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# ==============================================================================
n = 5
print("--- 1. Counting Numbers Triangle ---")

# Using FOR loop
print("[Using FOR loop]")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Using WHILE loop
print("\n[Using WHILE loop]")
i = 1
while i <= n:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i += 1


# ==============================================================================
# PATTERN 2: Same Number in Each Row
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# ==============================================================================
n = 5
print("\n--- 2. Same Number in Each Row ---")

# Using FOR loop
print("[Using FOR loop]")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()

# Using WHILE loop
print("\n[Using WHILE loop]")
i = 1
while i <= n:
    j = 1
    while j <= i:
        print(i, end=" ")
        j += 1
    print()
    i += 1


# ==============================================================================
# PATTERN 3: Inverted Number Triangle
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
# ==============================================================================
n = 5
print("\n--- 3. Inverted Number Triangle ---")

# Using FOR loop
print("[Using FOR loop]")
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Using WHILE loop
print("\n[Using WHILE loop]")
i = n
while i >= 1:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i -= 1


# ==============================================================================
# PATTERN 4: Floyd's Triangle (Continuous Numbers)
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# ==============================================================================
n = 4
print("\n--- 4. Floyd's Triangle ---")

# Using FOR loop
print("[Using FOR loop]")
num = 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()

# Using WHILE loop
print("\n[Using WHILE loop]")
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
# PATTERN 5: 0-1 Binary Triangle
# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1
# ==============================================================================
n = 5
print("\n--- 5. Binary (0-1) Triangle ---")

# Using FOR loop
print("[Using FOR loop]")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        # Print 1 if (i + j) is even, else print 0
        if (i + j) % 2 == 0:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()

# Using WHILE loop
print("\n[Using WHILE loop]")
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
# PATTERN 6: Palindromic Number Pyramid
#         1
#       1 2 1
#     1 2 3 2 1
#   1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1
# ==============================================================================
n = 5
print("\n--- 6. Palindromic Number Pyramid ---")

# Using FOR loop
print("[Using FOR loop]")
for i in range(1, n + 1):
    # Spaces
    print("  " * (n - i), end="")
    # Ascending numbers
    for j in range(1, i + 1):
        print(j, end=" ")
    # Descending numbers
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()

# Using WHILE loop
print("\n[Using WHILE loop]")
i = 1
while i <= n:
    # Spaces
    spaces = n - i
    s = 1
    while s <= spaces:
        print("  ", end="")
        s += 1

    # Ascending numbers
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1

    # Descending numbers
    k = i - 1
    while k >= 1:
        print(k, end=" ")
        k -= 1

    print()
    i += 1


# ==============================================================================
# PATTERN 7: Right-Aligned Number Triangle
#         1
#       2 1
#     3 2 1
#   4 3 2 1
# 5 4 3 2 1
# ==============================================================================
n = 5
print("\n--- 7. Right-Aligned Reverse Number Triangle ---")

# Using FOR loop
print("[Using FOR loop]")
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

# Using WHILE loop
print("\n[Using WHILE loop]")
i = 1
while i <= n:
    # Spaces
    s = 1
    while s <= (n - i):
        print("  ", end="")
        s += 1

    # Decreasing numbers
    j = i
    while j >= 1:
        print(j, end=" ")
        j -= 1

    print()
    i += 1