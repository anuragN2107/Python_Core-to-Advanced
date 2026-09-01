# ==============================================================================
#          SPECIAL / FAMOUS MATHEMATICAL NUMBER PROGRAMS IN PYTHON
# Unique number-theory programs commonly asked in practicals and interviews.
# ==============================================================================


# ------------------------------------------------------------------------------
# 1. STRONG NUMBER (Krishnamurthy / Peterson Number)
# A number whose sum of factorials of its digits equals the number itself.
# Example: 145 = 1! + 4! + 5! = 1 + 24 + 120 = 145
# ------------------------------------------------------------------------------
print("--- 1. Strong Number ---")
num = int(input("Enter a number: "))
temp = num
total_sum = 0

while temp > 0:
    digit = temp % 10
    # Calculate factorial of the digit
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    total_sum += fact
    temp //= 10

if total_sum == num and num > 0:
    print(f"{num} is a STRONG number.\n")
else:
    print(f"{num} is NOT a strong number.\n")


# ------------------------------------------------------------------------------
# 2. HARSHAD NUMBER (Niven Number)
# A number that is completely divisible by the sum of its digits.
# Example: 18 -> 1 + 8 = 9 -> 18 is divisible by 9
# ------------------------------------------------------------------------------
print("--- 2. Harshad Number ---")
num = int(input("Enter a number: "))
temp = num
digit_sum = 0

while temp > 0:
    digit_sum += temp % 10
    temp //= 10

if digit_sum != 0 and num % digit_sum == 0:
    print(f"{num} is a HARSHAD number.\n")
else:
    print(f"{num} is NOT a Harshad number.\n")


# ------------------------------------------------------------------------------
# 3. SPY NUMBER
# A number where the sum of its digits equals the product of its digits.
# Example: 123 -> Sum = 1+2+3 = 6, Product = 1*2*3 = 6
# ------------------------------------------------------------------------------
print("--- 3. Spy Number ---")
num = int(input("Enter a number: "))
temp = num
d_sum = 0
d_prod = 1

while temp > 0:
    digit = temp % 10
    d_sum += digit
    d_prod *= digit
    temp //= 10

if d_sum == d_prod:
    print(f"{num} is a SPY number.\n")
else:
    print(f"{num} is NOT a Spy number.\n")


# ------------------------------------------------------------------------------
# 4. AUTOMORPHIC NUMBER
# A number whose square ends in the same digits as the number itself.
# Example: 25^2 = 625 (ends in 25), 76^2 = 5776 (ends in 76)
# ------------------------------------------------------------------------------
print("--- 4. Automorphic Number ---")
num = int(input("Enter a number: "))
square = num * num
num_str = str(num)
sq_str = str(square)

if sq_str.endswith(num_str):
    print(f"{num} is an AUTOMORPHIC number (Square = {square}).\n")
else:
    print(f"{num} is NOT an Automorphic number (Square = {square}).\n")


# ------------------------------------------------------------------------------
# 5. DISARIUM NUMBER
# Sum of digits powered to their respective position equals the number.
# Example: 135 = 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135
# ------------------------------------------------------------------------------
print("--- 5. Disarium Number ---")
num = int(input("Enter a number: "))
num_str = str(num)
disarium_sum = 0

for index, digit in enumerate(num_str, start=1):
    disarium_sum += int(digit) ** index

if disarium_sum == num:
    print(f"{num} is a DISARIUM number.\n")
else:
    print(f"{num} is NOT a Disarium number.\n")


# ------------------------------------------------------------------------------
# 6. NEON NUMBER
# A number where the sum of digits of its square is equal to the number.
# Example: 9^2 = 81 -> 8 + 1 = 9
# ------------------------------------------------------------------------------
print("--- 6. Neon Number ---")
num = int(input("Enter a number: "))
sq = num * num
sq_digit_sum = 0

while sq > 0:
    sq_digit_sum += sq % 10
    sq //= 10

if sq_digit_sum == num:
    print(f"{num} is a NEON number.\n")
else:
    print(f"{num} is NOT a Neon number.\n")


# ------------------------------------------------------------------------------
# 7. PRONIC NUMBER (Heteromecic Number)
# A number that is the product of two consecutive integers: n = k * (k + 1)
# Example: 12 = 3 * 4, 20 = 4 * 5, 42 = 6 * 7
# ------------------------------------------------------------------------------
print("--- 7. Pronic Number ---")
num = int(input("Enter a number: "))
is_pronic = False

for k in range(int(num**0.5) + 1):
    if k * (k + 1) == num:
        is_pronic = True
        print(f"{num} is a PRONIC number ({k} * {k + 1} = {num}).\n")
        break

if not is_pronic:
    print(f"{num} is NOT a Pronic number.\n")


# ------------------------------------------------------------------------------
# 8. MAGIC NUMBER (Repeated Digital Root = 1)
# A number whose recursive sum of digits eventually equals 1.
# Example: 19 -> 1 + 9 = 10 -> 1 + 0 = 1
# ------------------------------------------------------------------------------
print("--- 8. Magic Number ---")
num = int(input("Enter a number: "))
temp = num

while temp > 9:
    current_sum = 0
    while temp > 0:
        current_sum += temp % 10
        temp //= 10
    temp = current_sum

if temp == 1:
    print(f"{num} is a MAGIC number.\n")
else:
    print(f"{num} is NOT a Magic number (Final single-digit sum = {temp}).\n")


# ------------------------------------------------------------------------------
# 9. DUCK NUMBER
# A positive number containing at least one zero, but NOT starting with zero.
# Example: 204, 3050 (Valid) | 0123 (Not valid)
# ------------------------------------------------------------------------------
print("--- 9. Duck Number ---")
raw_input = input("Enter a number: ").strip()

if raw_input.startswith("0"):
    print(f"{raw_input} is NOT a Duck number (cannot start with 0).\n")
elif "0" in raw_input:
    print(f"{raw_input} is a DUCK number.\n")
else:
    print(f"{raw_input} is NOT a Duck number (contains no zeros).\n")


# ------------------------------------------------------------------------------
# 10. COLLATZ SEQUENCE (3n + 1 Problem)
# If n is even -> n / 2. If n is odd -> 3n + 1. Repeat until it reaches 1.
# ------------------------------------------------------------------------------
print("--- 10. Collatz Sequence (3n + 1) ---")
n = int(input("Enter starting number (n > 0): "))
steps = 0
print(f"Sequence: {n}", end="")

while n > 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    print(f" -> {n}", end="")
    steps += 1

print(f"\nReached 1 in {steps} steps.\n")