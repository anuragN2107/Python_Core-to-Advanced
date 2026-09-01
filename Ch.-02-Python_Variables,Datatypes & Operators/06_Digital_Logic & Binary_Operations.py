# ==============================================================================
#                 DIGITAL LOGIC & BINARY ARITHMETIC 
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. BINARY ARITHMETIC RULES
# ------------------------------------------------------------------------------
# +----------------------------------------------------------------------------+
# | Rule | Addition       | Subtraction                 | Multi.   | Division  |
# |------|----------------|-----------------------------|----------|-----------|
# | i)   | 0 + 0 = 0      | 0 - 0 = 0                   | 0 * 0 = 0| 0 / 1 = 0 |
# | ii)  | 0 + 1 = 1      | 1 - 0 = 1                   | 0 * 1 = 0| 1 / 1 = 1 |
# | iii) | 1 + 0 = 1      | 1 - 1 = 0                   | 1 * 0 = 0| 0 / 0 = NA|
# | iv)  | 1 + 1 = 10     | 0 - 1 = 1 (with borrow 1)   | 1 * 1 = 1| 1 / 0 = NA|
# |      | (0, carry 1)   | [10 - 1 = 1 in binary]      |          | (invalid) |
# +----------------------------------------------------------------------------+


# ------------------------------------------------------------------------------
# 2. WORKED BINARY ARITHMETIC EXAMPLES
# ------------------------------------------------------------------------------

# --- A. Binary Addition ---
#    1   1 1 1       <- (Carry bits)
#    1 0 1 0 0 1 1   (Decimal: 83)
#  + 1 1 0 0 1 1 1   (Decimal: 103)
#  ----------------
#    1 0 1 1 1 0 1 0 (Decimal: 186)

bin_add_1 = 0b1010011
bin_add_2 = 0b1100111
print("Addition Result:    ", bin(bin_add_1 + bin_add_2)[2:])  # Output: 10111010


# --- B. Binary Subtraction ---
#        0 2         <- (Borrow bits)
#    1 1 1 0 1 1     (Decimal: 59)
#  - 1 0 0 1 1 1     (Decimal: 39)
#  ----------------
#    0 1 0 1 0 0     (Decimal: 20)

bin_sub_1 = 0b111011
bin_sub_2 = 0b100111
print("Subtraction Result: ", bin(bin_sub_1 - bin_sub_2)[2:].zfill(6))  # Output: 010100


# --- C. Binary Multiplication ---
#          1 1 0 1 1   (Decimal: 27)
#        x     1 1 0   (Decimal: 6)
#        -----------
#          0 0 0 0 0
#        1 1 0 1 1 x
#      + 1 1 0 1 1 x x
#      -------------
#      1 0 1 0 0 0 1 0 (Decimal: 162)

bin_mul_1 = 0b11011
bin_mul_2 = 0b110
print("Multiplication Res: ", bin(bin_mul_1 * bin_mul_2)[2:])  # Output: 10100010


# --- D. Binary Division ---
#          1 0 0       <- (Quotient = 4 in decimal)
#        _______
#  1 0 1 ) 1 0 1 1 1   (Dividend: 23, Divisor: 5)
#        - 1 0 1
#        -------
#          0 1 1       <- (Remainder = 3 in decimal)

dividend = 0b10111
divisor = 0b101
quotient = dividend // divisor
remainder = dividend % divisor
print(f"Quotient: {bin(quotient)[2:]}, Remainder: {bin(remainder)[2:]}")  # Q: 100, R: 11


# ------------------------------------------------------------------------------
# 3. LOGIC GATES & TRUTH TABLES (TABLE 4.9)
# ------------------------------------------------------------------------------

# 1. AND Gate: Output is 1 only when BOTH inputs are 1.
# Formula: y = A . B  (or AB)
# Truth Table:
# | A | B | y = AB |
# |---|---|--------|
# | 0 | 0 |   0    |
# | 0 | 1 |   0    |
# | 1 | 0 |   0    |
# | 1 | 1 |   1    |

# 2. OR Gate: Output is 1 when AT LEAST ONE input is 1.
# Formula: y = A + B
# Truth Table:
# | A | B | y = A + B |
# |---|---|-----------|
# | 0 | 0 |     0     |
# | 0 | 1 |     1     |
# | 1 | 0 |     1     |
# | 1 | 1 |     1     |

# 3. NOT Gate (Inverter): Inverts the input bit.
# Formula: y = A' (or A_bar)
# Truth Table:
# | A | y = A' |
# |---|--------|
# | 0 |   1    |
# | 1 |   0    |

# 4. NAND Gate: Inverted AND gate (Output is 0 only when both are 1).
# Formula: y = (AB)'
# Truth Table:
# | A | B | y = (AB)' |
# |---|---|-----------|
# | 0 | 0 |     1     |
# | 0 | 1 |     1     |
# | 1 | 0 |     1     |
# | 1 | 1 |     0     |

# 5. NOR Gate: Inverted OR gate (Output is 1 only when both are 0).
# Formula: y = (A + B)'
# Truth Table:
# | A | B | y = (A+B)' |
# |---|---|------------|
# | 0 | 0 |     1      |
# | 0 | 1 |     0      |
# | 1 | 0 |     0      |
# | 1 | 1 |     0      |

# 6. EX-OR Gate (XOR): Output is 1 when inputs are DIFFERENT.
# Formula: y = A ⊕ B = (A'B + AB')
# Truth Table:
# | A | B | y = A ⊕ B |
# |---|---|-----------|
# | 0 | 0 |     0     |
# | 0 | 1 |     1     |
# | 1 | 0 |     1     |
# | 1 | 1 |     0     |

# 7. EX-NOR Gate (XNOR): Output is 1 when inputs are SAME.
# Formula: y = A ⊙ B = (AB + A'B')
# Truth Table:
# | A | B | y = A ⊙ B |
# |---|---|-----------|
# | 0 | 0 |     1     |
# | 0 | 1 |     0     |
# | 1 | 0 |     0     |
# | 1 | 1 |     1     |
# ==============================================================================