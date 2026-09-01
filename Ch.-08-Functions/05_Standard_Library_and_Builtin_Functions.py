# ==============================================================================
#           PYTHON BUILT-IN & STANDARD LIBRARY FUNCTIONS 
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. len()
# ------------------------------------------------------------------------------
# Returns the total number of items in an object (list, tuple, string, dict, set).
# Syntax: len(object)
print("--- 1. len() ---")
numbers = [10, 20, 30]
print(len(numbers))  # Output: 3


# ------------------------------------------------------------------------------
# 2. type()
# ------------------------------------------------------------------------------
# Returns the data type/class of an object.
# Syntax: type(object)
print("\n--- 2. type() ---")
numbers = [10, 20, 30]
print(type(numbers))  # Output: <class 'list'>


# ------------------------------------------------------------------------------
# 3. print()
# ------------------------------------------------------------------------------
# Prints objects to the text stream/console with customizable separator and ending.
# Syntax: print(*objects, sep=' ', end='\n')
print("\n--- 3. print() ---")
print("Hello, world!")  # Output: Hello, world!
print("Python", "Rust", "Go", sep=" | ")  # Output: Python | Rust | Go


# ------------------------------------------------------------------------------
# 4. max() and min()
# ------------------------------------------------------------------------------
# max(): Returns the largest item in an iterable or between arguments.
# min(): Returns the smallest item in an iterable or between arguments.
# Syntax: max(iterable, key=...), min(iterable, key=...)
print("\n--- 4. max() & min() ---")
numbers = [10, 20, 30]
print("Max:", max(numbers))  # Output: 30
print("Min:", min(numbers))  # Output: 10


# ------------------------------------------------------------------------------
# 5. sum()
# ------------------------------------------------------------------------------
# Sums the items of an iterable from left to right and returns the total.
# Syntax: sum(iterable, start=0)
print("\n--- 5. sum() ---")
numbers = [10, 20, 30]
print(sum(numbers))           # Output: 60
print(sum(numbers, start=10)) # Output: 70


# ------------------------------------------------------------------------------
# 6. any() and all()
# ------------------------------------------------------------------------------
# any(): Returns True if AT LEAST ONE item in the iterable is Truthy.
# all(): Returns True ONLY if ALL items in the iterable are Truthy.
# Syntax: any(iterable), all(iterable)
print("\n--- 6. any() & all() ---")
numbers = [1, 2, 3, 4, 5]
is_any_even = any(number % 2 == 0 for number in numbers)
print("Any even?", is_any_even)  # Output: True

is_all_even = all(number % 2 == 0 for number in numbers)
print("All even?", is_all_even)  # Output: False


# ------------------------------------------------------------------------------
# 7. sorted()
# ------------------------------------------------------------------------------
# Returns a brand-new sorted list from the elements of any iterable.
# Syntax: sorted(iterable, key=None, reverse=False)
print("\n--- 7. sorted() ---")
numbers = [5, 2, 8, 1, 9]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 2, 5, 8, 9]


# ------------------------------------------------------------------------------
# 8. enumerate()
# ------------------------------------------------------------------------------
# Returns an iterator yielding pairs containing a count/index and the value.
# Syntax: enumerate(iterable, start=0)
print("\n--- 8. enumerate() ---")
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Fruit {index}: {fruit}")
# Output:
# Fruit 0: apple
# Fruit 1: banana
# Fruit 2: cherry


# ------------------------------------------------------------------------------
# 9. zip()
# ------------------------------------------------------------------------------
# Aggregates elements from multiple iterables into tuples up to the shortest length.
# Syntax: zip(*iterables)
print("\n--- 9. zip() ---")
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3]
zipped = list(zip(fruits, numbers))
print(zipped)  # Output: [('apple', 1), ('banana', 2), ('cherry', 3)]


# ------------------------------------------------------------------------------
# 10. reversed()
# ------------------------------------------------------------------------------
# Returns a reverse iterator over values of an ordered sequence.
# Syntax: reversed(sequence)
print("\n--- 10. reversed() ---")
fruits = ["apple", "banana", "cherry"]
reversed_fruits = list(reversed(fruits))
print(reversed_fruits)  # Output: ['cherry', 'banana', 'apple']


# ------------------------------------------------------------------------------
# 11. range()
# ------------------------------------------------------------------------------
# Generates an immutable sequence of numbers on demand.
# Syntax: range(stop) or range(start, stop[, step])
print("\n--- 11. range() ---")
for number in range(1, 6):
    print(number, end=" ")
print()
# Output: 1 2 3 4 5


# ------------------------------------------------------------------------------
# 12. map()
# ------------------------------------------------------------------------------
# Applies a function to all items in an iterable and returns an iterator.
# Syntax: map(function, iterable)
print("\n--- 12. map() ---")
def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]


# ------------------------------------------------------------------------------
# 13. filter()
# ------------------------------------------------------------------------------
# Constructs an iterator from elements of an iterable for which a function returns True.
# Syntax: filter(function, iterable)
print("\n--- 13. filter() ---")
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # Output: [2, 4]


# ------------------------------------------------------------------------------
# 14. functools.reduce()
# ------------------------------------------------------------------------------
# Cumulatively applies a function of two arguments to elements to reduce down to a single value.
# Syntax: reduce(function, iterable[, initializer])
from functools import reduce

print("\n--- 14. functools.reduce() ---")
def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
total = reduce(add, numbers)
print("Total sum:", total)  # Output: 15


# ------------------------------------------------------------------------------
# 15. itertools.zip_longest()
# ------------------------------------------------------------------------------
# Aggregates elements in parallel, padding shorter iterables with a fillvalue.
# Syntax: zip_longest(*iterables, fillvalue=None)
from itertools import zip_longest, chain

print("\n--- 15. itertools.zip_longest() ---")
fruits = ["apple", "banana", "cherry", "date"]
numbers = [1, 2]
zipped_longest = list(zip_longest(fruits, numbers, fillvalue="missing"))
print(zipped_longest)
# Output: [('apple', 1), ('banana', 2), ('cherry', 'missing'), ('date', 'missing')]


# ------------------------------------------------------------------------------
# 16. isinstance() & issubclass()
# ------------------------------------------------------------------------------
# Type-checking and inheritance validation utilities.
# Syntax: isinstance(obj, class_or_tuple), issubclass(class, class_or_tuple)
print("\n--- 16. isinstance() & issubclass() ---")
print(isinstance(5, int))              # Output: True
print(isinstance("hello", (int, str))) # Output: True (Matches any in tuple)
print(issubclass(bool, int))           # Output: True (bool subclasses int)


# ------------------------------------------------------------------------------
# 17. round(), abs(), and divmod()
# ------------------------------------------------------------------------------
# abs()   : Returns absolute (non-negative) magnitude.
# round() : Rounds a floating-point number to n digits precision.
# divmod(): Computes integer quotient and remainder simultaneously: (a // b, a % b).
# Syntax: abs(x), round(number[, ndigits]), divmod(a, b)
print("\n--- 17. Numeric Helpers (abs, round, divmod) ---")
print("abs(-15.5):       ", abs(-15.5))         # Output: 15.5
print("round(3.14159, 2):", round(3.14159, 2))  # Output: 3.14
print("divmod(17, 5):    ", divmod(17, 5))      # Output: (3, 2)


# ------------------------------------------------------------------------------
# 18. itertools.chain()
# ------------------------------------------------------------------------------
# Chains multiple iterables together into a single continuous stream.
# Syntax: chain(*iterables)
print("\n--- 18. itertools.chain() ---")
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
combined = list(chain(list1, list2))
print(combined)  # Output: [1, 2, 3, 'a', 'b', 'c']
# ==============================================================================