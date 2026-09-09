# ==============================================================================
#                 PYTHON BASICS: type(), CONVERSION & CASTING
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. THE type() FUNCTION
# ------------------------------------------------------------------------------
# The built-in type() function returns the class/type of an object.

a = 5
print(type(a))  # Output: <class 'int'>

b = 3.14
print(type(b))  # Output: <class 'float'>

c = "Anurag"
print(type(c))  # Output: <class 'str'>

d = True
print(type(d))  # Output: <class 'bool'>


# ------------------------------------------------------------------------------
# 2. TYPE CONVERSION VS. TYPE CASTING
# ------------------------------------------------------------------------------
# Type Conversion (Implicit):
# - Automatic process performed by Python interpreter.
# - Prevents data loss by promoting lower data types to higher data types
#   (e.g., int -> float).

# Type Casting (Explicit):
# - Manual process performed by the programmer using constructor functions
#   like int(), float(), str(), bool(), list(), tuple(), set().
# - May cause loss of precision or raise ValueError if the format is incompatible.


# ------------------------------------------------------------------------------
# 3. IMPLICIT TYPE CONVERSION (AUTOMATIC)
# ------------------------------------------------------------------------------
num_int = 10     # int
num_float = 5.5  # float

# Python automatically converts num_int to float before addition to avoid data loss
result = num_int + num_float

print("Implicit Result:", result)        # Output: 15.5
print("Result Type:", type(result))      # Output: <class 'float'>


# ------------------------------------------------------------------------------
# 4. EXPLICIT TYPE CASTING (MANUAL)
# ------------------------------------------------------------------------------

# String to Integer / Float
num_str = "20"
num_int = int(num_str)                   # Converts "20" -> 20
print("Converted Integer:", num_int)     # Output: 20
print("Type after casting:", type(num_int))  # Output: <class 'int'>

float_str = "3.14"
num_converted_float = float(float_str)   # Converts "3.14" -> 3.14

# Float to Integer (Trims decimal places / truncates toward zero)
pi_val = 3.14
int_pi = int(pi_val)
print("Truncated int:", int_pi)          # Output: 3

# Number to String
val = 5
str_val = str(val)
print("String representation:", str_val) # Output: '5'
print("Type:", type(str_val))            # Output: <class 'str'>


# ------------------------------------------------------------------------------
# 5. COMMON TYPE CASTING EXCEPTIONS & PITFALLS
# ------------------------------------------------------------------------------
# 1. Casting a decimal string directly to an int raises ValueError:
#    invalid_str = "3.14"
#    int(invalid_str)  # Raises ValueError!
#    Correct approach: int(float("3.14")) -> 3

# 2. Casting non-numeric strings raises ValueError:
#    int("Anurag")     # Raises ValueError!

# 3. Boolean casting rules (Truthy vs Falsy):
#    bool("") -> False | bool("hello") -> True
#    bool(0)  -> False | bool(1)       -> True
#    bool([]) -> False | bool([1, 2])  -> True
# ==============================================================================