# ==============================================================================
#                     COMPLETE ASCII TABLE & ENCODING REFERENCE
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. WHAT IS ASCII?
# ------------------------------------------------------------------------------
# ASCII (American Standard Code for Information Interchange) is a 7-bit character 
# encoding standard representing 128 characters (decimal values 0 to 127).
#
# Sections Breakdown:
# - Decimal   0 to  31 & 127 : Control Characters (non-printable commands)
# - Decimal  32 to  47       : Punctuation & Symbols (Part 1) [32 = Space]
# - Decimal  48 to  57       : Digits ('0' through '9')
# - Decimal  58 to  64       : Punctuation & Symbols (Part 2)
# - Decimal  65 to  90       : Uppercase Letters ('A' through 'Z')
# - Decimal  91 to  96       : Punctuation & Symbols (Part 3)
# - Decimal  97 to 122       : Lowercase Letters ('a' through 'z')
# - Decimal 123 to 126       : Punctuation & Symbols (Part 4)


# ------------------------------------------------------------------------------
# 2. COMPLETE ASCII LOOKUP TABLE (DEC | HEX | OCT | CHAR)
# ------------------------------------------------------------------------------
# +-----+----+-----+--------+  +-----+----+-----+------+  +-----+----+-----+------+  +-----+----+-----+------+
# | Dec |Hex | Oct | Char   |  | Dec |Hex | Oct | Char |  | Dec |Hex | Oct | Char |  | Dec |Hex | Oct | Char |
# +-----+----+-----+--------+  +-----+----+-----+------+  +-----+----+-----+------+  +-----+----+-----+------+
# |   0 | 00 | 000 | NULL   |  |  32 | 20 | 040 | space|  |  64 | 40 | 100 | @    |  |  96 | 60 | 140 | `    |
# |   1 | 01 | 001 | SOH    |  |  33 | 21 | 041 | !    |  |  65 | 41 | 101 | A    |  |  97 | 61 | 141 | a    |
# |   2 | 02 | 002 | STX    |  |  34 | 22 | 042 | "    |  |  66 | 42 | 102 | B    |  |  98 | 62 | 142 | b    |
# |   3 | 03 | 003 | ETX    |  |  35 | 23 | 043 | #    |  |  67 | 43 | 103 | C    |  |  99 | 63 | 143 | c    |
# |   4 | 04 | 004 | EOT    |  |  36 | 24 | 044 | $    |  |  68 | 44 | 104 | D    |  | 100 | 64 | 144 | d    |
# |   5 | 05 | 005 | ENQ    |  |  37 | 25 | 045 | %    |  |  69 | 45 | 105 | E    |  | 101 | 65 | 145 | e    |
# |   6 | 06 | 006 | ACK    |  |  38 | 26 | 046 | &    |  |  70 | 46 | 106 | F    |  | 102 | 66 | 146 | f    |
# |   7 | 07 | 007 | BEL    |  |  39 | 27 | 047 | '    |  |  71 | 47 | 107 | G    |  | 103 | 67 | 147 | g    |
# |   8 | 08 | 010 | BS     |  |  40 | 28 | 050 | (    |  |  72 | 48 | 110 | H    |  | 104 | 68 | 150 | h    |
# |   9 | 09 | 011 | TAB    |  |  41 | 29 | 051 | )    |  |  73 | 49 | 111 | I    |  | 105 | 69 | 151 | i    |
# |  10 | 0a | 012 | LF     |  |  42 | 2a | 052 | *    |  |  74 | 4a | 112 | J    |  | 106 | 6a | 152 | j    |
# |  11 | 0b | 013 | VT     |  |  43 | 2b | 053 | +    |  |  75 | 4b | 113 | K    |  | 107 | 6b | 153 | k    |
# |  12 | 0c | 014 | FF     |  |  44 | 2c | 054 | ,    |  |  76 | 4c | 114 | L    |  | 108 | 6c | 154 | l    |
# |  13 | 0d | 015 | CR     |  |  45 | 2d | 055 | -    |  |  77 | 4d | 115 | M    |  | 109 | 6d | 155 | m    |
# |  14 | 0e | 016 | SO     |  |  46 | 2e | 056 | .    |  |  78 | 4e | 116 | N    |  | 110 | 6e | 156 | n    |
# |  15 | 0f | 017 | SI     |  |  47 | 2f | 057 | /    |  |  79 | 4f | 117 | O    |  | 111 | 6f | 157 | o    |
# |  16 | 10 | 020 | DLE    |  |  48 | 30 | 060 | 0    |  |  80 | 50 | 120 | P    |  | 112 | 70 | 160 | p    |
# |  17 | 11 | 021 | DC1    |  |  49 | 31 | 061 | 1    |  |  81 | 51 | 121 | Q    |  | 113 | 71 | 161 | q    |
# |  18 | 12 | 022 | DC2    |  |  50 | 32 | 062 | 2    |  |  82 | 52 | 122 | R    |  | 114 | 72 | 162 | r    |
# |  19 | 13 | 023 | DC3    |  |  51 | 33 | 063 | 3    |  |  83 | 53 | 123 | S    |  | 115 | 73 | 163 | s    |
# |  20 | 14 | 024 | DC4    |  |  52 | 34 | 064 | 4    |  |  84 | 54 | 124 | T    |  | 116 | 74 | 164 | t    |
# |  21 | 15 | 025 | NAK    |  |  53 | 35 | 065 | 5    |  |  85 | 55 | 125 | U    |  | 117 | 75 | 165 | u    |
# |  22 | 16 | 026 | SYN    |  |  54 | 36 | 066 | 6    |  |  86 | 56 | 126 | V    |  | 118 | 76 | 166 | v    |
# |  23 | 17 | 027 | ETB    |  |  55 | 37 | 067 | 7    |  |  87 | 57 | 127 | W    |  | 119 | 77 | 167 | w    |
# |  24 | 18 | 030 | CAN    |  |  56 | 38 | 070 | 8    |  |  88 | 58 | 130 | X    |  | 120 | 78 | 170 | x    |
# |  25 | 19 | 031 | EM     |  |  57 | 39 | 071 | 9    |  |  89 | 59 | 131 | Y    |  | 121 | 79 | 171 | y    |
# |  26 | 1a | 032 | SUB    |  |  58 | 3a | 072 | :    |  |  90 | 5a | 132 | Z    |  | 122 | 7a | 172 | z    |
# |  27 | 1b | 033 | ESC    |  |  59 | 3b | 073 | ;    |  |  91 | 5b | 133 | [    |  | 123 | 7b | 173 | {    |
# |  28 | 1c | 034 | FS     |  |  60 | 3c | 074 | <    |  |  92 | 5c | 134 | \    |  | 124 | 7c | 174 | |    |
# |  29 | 1d | 035 | GS     |  |  61 | 3d | 075 | =    |  |  93 | 5d | 135 | ]    |  | 125 | 7d | 175 | }    |
# |  30 | 1e | 036 | RS     |  |  62 | 3e | 076 | >    |  |  94 | 5e | 136 | ^    |  | 126 | 7e | 176 | ~    |
# |  31 | 1f | 037 | US     |  |  63 | 3f | 077 | ?    |  |  95 | 5f | 137 | _    |  | 127 | 7f | 177 | DEL  |
# +-----+----+-----+--------+  +-----+----+-----+------+  +-----+----+-----+------+  +-----+----+-----+------+


# ------------------------------------------------------------------------------
# 3. COMMON CONTROL CODES QUICK MEANINGS
# ------------------------------------------------------------------------------
# - NULL (0)   : Null character (string terminator in C)
# - BEL  (7)   : Terminal bell alert sound
# - BS   (8)   : Backspace (\b)
# - TAB  (9)   : Horizontal tab (\t)
# - LF   (10)  : Line feed / Newline (\n)
# - CR   (13)  : Carriage return (\r)
# - ESC  (27)  : Escape key code
# - DEL  (127) : Delete


# ------------------------------------------------------------------------------
# 4. KEY ASCII MEMORIZATION SHORTCUTS & OFFSETS
# ------------------------------------------------------------------------------
# - '0' to '9' : Dec 48 to 57  (Hex 0x30 to 0x39)
# - 'A' to 'Z' : Dec 65 to 90  (Hex 0x41 to 0x5A)
# - 'a' to 'z' : Dec 97 to 122 (Hex 0x61 to 0x7A)
#
# Crucial Conversion Rule:
# - Difference between uppercase and lowercase letters is exactly 32 (0x20 / 2^5).
#   ord('a') - ord('A') = 97 - 65 = 32
# - Bitwise lowercase trick: chr(ord('A') | 32) -> 'a'
# - Bitwise uppercase trick: chr(ord('a') & ~32) -> 'A'


# ------------------------------------------------------------------------------
# 5. PYTHON BUILT-INS: ord(), chr(), hex(), oct()
# ------------------------------------------------------------------------------

# ord(c) -> Gets integer ASCII/Unicode code point of a character
print("ord('A'):", ord('A'))       # Output: 65
print("ord('a'):", ord('a'))       # Output: 97
print("ord('0'):", ord('0'))       # Output: 48

# chr(i) -> Gets character string for a given integer ASCII code point
print("chr(65): ", chr(65))        # Output: A
print("chr(10): ", repr(chr(10)))  # Output: '\n' (Newline)

# Converting ASCII value to Hex and Octal strings:
code = ord('A')                    # 65
print("Hex representation: ", hex(code))  # Output: 0x41
print("Octal representation:", oct(code)) # Output: 0o101
# ==============================================================================