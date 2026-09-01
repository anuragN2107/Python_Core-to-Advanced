# ==============================================================================
#                 PYTHON PRACTICE: LISTS & TUPLES (SOLUTIONS)
# ==============================================================================

# ------------------------------------------------------------------------------
# Problem 1: Store seven fruits in a list entered by the user
# ------------------------------------------------------------------------------
fruits = []
f1 = input("Enter fruit 1: ")
fruits.append(f1)
f2 = input("Enter fruit 2: ")
fruits.append(f2)
f3 = input("Enter fruit 3: ")
fruits.append(f3)
f4 = input("Enter fruit 4: ")
fruits.append(f4)
f5 = input("Enter fruit 5: ")
fruits.append(f5)
f6 = input("Enter fruit 6: ")
fruits.append(f6)
f7 = input("Enter fruit 7: ")
fruits.append(f7)

print("The list of fruits is:", fruits)


# ------------------------------------------------------------------------------
# Problem 2: Accept marks of 6 students and display them in a sorted manner
# ------------------------------------------------------------------------------
# Note: Cast inputs to int/float so numeric sorting occurs rather than alphabetical sorting
marks = []
m1 = int(input("Enter marks for student 1: "))
marks.append(m1)
m2 = int(input("Enter marks for student 2: "))
marks.append(m2)
m3 = int(input("Enter marks for student 3: "))
marks.append(m3)
m4 = int(input("Enter marks for student 4: "))
marks.append(m4)
m5 = int(input("Enter marks for student 5: "))
marks.append(m5)
m6 = int(input("Enter marks for student 6: "))
marks.append(m6)

print("Original marks list:             ", marks)

# Sort ascending
marks.sort()
print("Sorted marks (Ascending):        ", marks)

# Sort descending
marks.sort(reverse=True)
print("Sorted marks (Descending):       ", marks)


# ------------------------------------------------------------------------------
# Problem 3: Check that a tuple type cannot be modified (Immutability check)
# ------------------------------------------------------------------------------
x = (2, 6, "Harry", 4.6, True)
print("The type of x is:", type(x))

# Attempting item assignment raises a TypeError:
# x[2] = "John"  # TypeError: 'tuple' object does not support item assignment


# ------------------------------------------------------------------------------
# Problem 4: Sum a list containing 4 numbers
# ------------------------------------------------------------------------------
A = [2, 6, 8, 24]
print("The sum of the list is:", sum(A))  # Output: 40


# ------------------------------------------------------------------------------
# Problem 5: Count the number of zeros in the tuple
# ------------------------------------------------------------------------------
A = (7, 0, 0, 8, 0, 9)
print("The number of zeros in the tuple is:", A.count(0))  # Output: 3
# ==============================================================================