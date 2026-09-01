# ==============================================================================
#                      PYTHON BASICS: VARIABLES & DATA TYPES
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. WHAT IS A VARIABLE?
# ------------------------------------------------------------------------------
# A variable is a named reference to a memory location used to store data values.
# In Python, variables are dynamically typed (no explicit type declaration needed).

# Example 1: Numeric Operations
a = 7       # Integer
b = 2.1     # Float
print(a + b)  # Output: 9.1

# Example 2: String Operations
c = "harry"  # String
print(c + " is a good boy")  # Output: harry is a good boy


# ------------------------------------------------------------------------------
# 2. RULES FOR NAMING VARIABLES / IDENTIFIERS
# ------------------------------------------------------------------------------
# An identifier is a name given to entities like classes, functions, and variables.

# [Allowed]
# - Letters (a-z, A-Z), digits (0-9), and underscores (_)
# - Must start with a letter or an underscore (_)
# - Case-sensitive: `age`, `Age`, and `AGE` are three distinct variables

# [Forbidden]
# - Cannot start with a digit (e.g., `1variable` is invalid)
# - Cannot contain whitespace (use `snake_case` instead: `user_name`)
# - Cannot contain special characters (e.g., @, #, $, %, !)
# - Cannot use reserved Python keywords (e.g., `for`, `def`, `class`)

# Best Practice: Choose meaningful, descriptive names (e.g., `student_count` vs `sc`).


# ------------------------------------------------------------------------------
# 3. KEYWORDS
# ------------------------------------------------------------------------------
# Keywords are reserved words with predefined meanings in Python syntax.
# They cannot be redefined or used as identifiers.

# Complete standard keyword set:
# and       as        assert    async     await     break     class     continue
# def       del       elif      else      except    finally   for       from
# global    if        import    in        is        lambda    nonlocal  not
# or        pass      raise     return    try       while     with      yield


# ------------------------------------------------------------------------------
# 4. BUILT-IN DATA TYPES
# ------------------------------------------------------------------------------
# A data type specifies the type of value an object holds and what operations
# can be performed on it.

# - Numeric:   int (e.g., 10), float (e.g., 3.14), complex (e.g., 2 + 3j)
# - Text:      str (e.g., "Hello")
# - Sequence:  list (e.g., [1, 2]), tuple (e.g., (1, 2)), range
# - Mapping:   dict (e.g., {"key": "value"})
# - Set:       set (e.g., {1, 2}), frozenset
# - Boolean:   bool (True, False)
# - None:      NoneType (None)
# ==============================================================================