# ==============================================================================
#                 PYTHON STRINGS: INDEXING & SLICING 
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. WHAT IS INDEXING & SLICING?
# ------------------------------------------------------------------------------
# Indexing: Accesses a single character by its exact position.
# Slicing : Extracts a sub-sequence using the syntax: sequence[start:stop:step]
#
# Key Rules:
# - start : Index where the slice starts (INCLUDED). Default is 0 (or -1 if step < 0).
# - stop  : Index where the slice ends (EXCLUDED).
# - step  : Stride/increment between indices. Default is 1.


# ------------------------------------------------------------------------------
# 2. INDEX POSITION MAP FOR: "Hello Anurag" (Length = 12)
# ------------------------------------------------------------------------------
#  Positive Index:   0   1   2   3   4   5   6   7   8   9  10  11
#  Character:        H   e   l   l   o       A   n   u   r   a   g
#  Negative Index: -12 -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1
# ------------------------------------------------------------------------------

Str1 = "Hello Anurag"


# ------------------------------------------------------------------------------
# 3. POSITIVE & NEGATIVE SLICING EXAMPLES
# ------------------------------------------------------------------------------

# [0:5] -> Indices 0, 1, 2, 3, 4
slc1 = Str1[0:5]
print("Str1[0:5]:   ", slc1)  # Output: Hello

# [1:4] -> Indices 1, 2, 3
slc2 = Str1[1:4]
print("Str1[1:4]:   ", slc2)  # Output: ell

# [-4:-1] -> Indices -4, -3, -2 (letters 'u', 'r', 'a')
slc3 = Str1[-4:-1]
print("Str1[-4:-1]: ", slc3)  # Output: ura

# [2:10:2] -> Indices 2, 4, 6, 8 ('l', 'o', 'A', 'u')
slc4 = Str1[2:10:2]
print("Str1[2:10:2]:", slc4)  # Output: loAu


# ------------------------------------------------------------------------------
# 4. SINGLE CHARACTER ACCESS (NEGATIVE INDEXING)
# ------------------------------------------------------------------------------

print(Str1[-1])  # Last element        -> Output: g
print(Str1[-2])  # Second-last element -> Output: a
print(Str1[-3])  # Third-last element  -> Output: r


# ------------------------------------------------------------------------------
# 5. STEP PARAMETER & REVERSAL TRICKS
# ------------------------------------------------------------------------------

# [:6] -> Extracts first 6 characters (indices 0 to 5)
print(Str1[:6])  # Output: Hello 

# [1::2] -> Starts at index 1 and steps by 2 (all odd-indexed characters)
print(Str1[1::2])  # Output: el nra

# [::-1] -> Reverses the entire string
print(Str1[::-1])  # Output: garunA olleH

# [-1::-1] -> Same as [::-1], explicitly starting from the last index
print(Str1[-1::-1])  # Output: garunA olleH

# [-2::-1] -> Starts from second-last character ('a') and goes backwards
print(Str1[-2::-1])  # Output: arunA olleH
# ==============================================================================