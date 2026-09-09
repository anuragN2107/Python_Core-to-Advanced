# ==============================================================================
#      MATHEMATICAL & FORMULA-BASED PYTHON PROGRAMS (INPUT DRIVEN)
# Each program takes user input and uses loops to compute the result.
# ==============================================================================


# ------------------------------------------------------------------------------
# 1. FACTORIAL OF A NUMBER (n!)
# Formula: n! = 1 * 2 * 3 * ... * n
# ------------------------------------------------------------------------------
print("--- 1. Factorial ---")
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"Factorial of {n} = {fact}\n")


# ------------------------------------------------------------------------------
# 2. SEPARATE ODD AND EVEN NUMBERS UP TO N
# ------------------------------------------------------------------------------
print("--- 2. Odd and Even Numbers up to N ---")
n = int(input("Enter upper limit (N): "))
evens = []
odds = []
for i in range(1, n + 1):
    if i % 2 == 0:
        evens.append(i)
    else:
        odds.append(i)
print(f"Even numbers up to {n}: {evens}")
print(f"Odd numbers up to {n}: {odds}\n")


# ------------------------------------------------------------------------------
# 3. SUM OF SQUARES OF FIRST N NATURAL NUMBERS
# Formula: 1^2 + 2^2 + 3^2 + ... + n^2
# ------------------------------------------------------------------------------
print("--- 3. Sum of Squares ---")
n = int(input("Enter N: "))
sum_squares = 0
for i in range(1, n + 1):
    sum_squares += i**2
print(f"Sum of squares of first {n} numbers = {sum_squares}\n")


# ------------------------------------------------------------------------------
# 4. SUM OF CUBES OF FIRST N NATURAL NUMBERS
# Formula: 1^3 + 2^3 + 3^3 + ... + n^3
# ------------------------------------------------------------------------------
print("--- 4. Sum of Cubes ---")
n = int(input("Enter N: "))
sum_cubes = 0
for i in range(1, n + 1):
    sum_cubes += i**3
print(f"Sum of cubes of first {n} numbers = {sum_cubes}\n")


# ------------------------------------------------------------------------------
# 5. SUM OF FIRST N WHOLE NUMBERS
# Whole numbers start from 0: 0 + 1 + 2 + ... + (n - 1)
# ------------------------------------------------------------------------------
print("--- 5. Sum of First N Whole Numbers ---")
n = int(input("Enter count of whole numbers (N): "))
whole_sum = 0
for i in range(n):  # Starts from 0 up to n - 1
    whole_sum += i
print(f"Sum of first {n} whole numbers = {whole_sum}\n")


# ------------------------------------------------------------------------------
# 6. CHECK IF A NUMBER IS PRIME
# ------------------------------------------------------------------------------
print("--- 6. Prime Number Check ---")
num = int(input("Enter a number: "))
if num <= 1:
    print(f"{num} is NOT a prime number.\n")
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is NOT a prime number.\n")
            break
    else:
        print(f"{num} is a PRIME number.\n")


# ------------------------------------------------------------------------------
# 7. FIBONACCI SERIES UP TO N TERMS
# Sequence: 0, 1, 1, 2, 3, 5, 8, 13...
# ------------------------------------------------------------------------------
print("--- 7. Fibonacci Series ---")
terms = int(input("Enter number of terms: "))
a, b = 0, 1
print(f"First {terms} terms of Fibonacci series:")
for _ in range(terms):
    print(a, end=" ")
    a, b = b, a + b
print("\n")


# ------------------------------------------------------------------------------
# 8. REVERSE AN INTEGER NUMBER
# Example: 1234 -> 4321
# ------------------------------------------------------------------------------
print("--- 8. Reverse a Number ---")
num = int(input("Enter an integer: "))
temp = abs(num)
rev = 0
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10
rev = -rev if num < 0 else rev
print(f"Reversed number = {rev}\n")


# ------------------------------------------------------------------------------
# 9. CHECK PALINDROME NUMBER
# Example: 121 -> Palindrome, 123 -> Not Palindrome
# ------------------------------------------------------------------------------
print("--- 9. Palindrome Number Check ---")
num = int(input("Enter a number: "))
temp = num
rev = 0
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

if num >= 0 and rev == num:
    print(f"{num} is a PALINDROME.\n")
else:
    print(f"{num} is NOT a palindrome.\n")


# ------------------------------------------------------------------------------
# 10. CHECK ARMSTRONG NUMBER (OF N DIGITS)
# Example: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
# ------------------------------------------------------------------------------
print("--- 10. Armstrong Number Check ---")
num = int(input("Enter a number: "))
power = len(str(abs(num)))
temp = abs(num)
armstrong_sum = 0

while temp > 0:
    digit = temp % 10
    armstrong_sum += digit**power
    temp //= 10

if armstrong_sum == abs(num):
    print(f"{num} is an ARMSTRONG number.\n")
else:
    print(f"{num} is NOT an Armstrong number.\n")


# ------------------------------------------------------------------------------
# 11. SUM OF DIGITS OF A NUMBER
# Example: 452 -> 4 + 5 + 2 = 11
# ------------------------------------------------------------------------------
print("--- 11. Sum of Digits ---")
num = int(input("Enter a number: "))
temp = abs(num)
digit_sum = 0
while temp > 0:
    digit_sum += temp % 10
    temp //= 10
print(f"Sum of digits = {digit_sum}\n")


# ------------------------------------------------------------------------------
# 12. POWER / EXPONENTIATION WITHOUT USING ** OPERATOR (Base^Exponent)
# ------------------------------------------------------------------------------
print("--- 12. Power Calculation (Base^Exp) ---")
base = int(input("Enter base: "))
exp = int(input("Enter exponent (non-negative): "))
result = 1
for _ in range(exp):
    result *= base
print(f"{base}^{exp} = {result}\n")


# ------------------------------------------------------------------------------
# 13. GREATEST COMMON DIVISOR (GCD / HCF)
# ------------------------------------------------------------------------------
print("--- 13. GCD / HCF of Two Numbers ---")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
x, y = abs(a), abs(b)
while y != 0:
    x, y = y, x % y
print(f"GCD of {a} and {b} = {x}\n")


# ------------------------------------------------------------------------------
# 14. LEAST COMMON MULTIPLE (LCM)
# Formula: LCM(a, b) = (|a * b|) / GCD(a, b)
# ------------------------------------------------------------------------------
print("--- 14. LCM of Two Numbers ---")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
max_num = max(abs(a), abs(b))
while True:
    if max_num % abs(a) == 0 and max_num % abs(b) == 0:
        lcm = max_num
        break
    max_num += 1
print(f"LCM of {a} and {b} = {lcm}\n")


# ------------------------------------------------------------------------------
# 15. CHECK PERFECT NUMBER
# A number equal to sum of its proper positive divisors (e.g., 6 = 1 + 2 + 3)
# ------------------------------------------------------------------------------
print("--- 15. Perfect Number Check ---")
num = int(input("Enter a number: "))
divisors_sum = 0
for i in range(1, num):
    if num % i == 0:
        divisors_sum += i

if divisors_sum == num and num > 0:
    print(f"{num} is a PERFECT number.\n")
else:
    print(f"{num} is NOT a perfect number.\n")