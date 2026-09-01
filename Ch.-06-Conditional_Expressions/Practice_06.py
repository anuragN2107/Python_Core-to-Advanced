# ==============================================================================
#                 CHAPTER 6: PRACTICE SET (CONDITIONALS)
# ==============================================================================

# ------------------------------------------------------------------------------
# Problem 1: Find the greatest of four numbers entered by the user
# ------------------------------------------------------------------------------
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))

if (num1 >= num2) and (num1 >= num3) and (num1 >= num4):
    print("The greatest number is:", num1)
elif (num2 >= num1) and (num2 >= num3) and (num2 >= num4):
    print("The greatest number is:", num2)
elif (num3 >= num1) and (num3 >= num2) and (num3 >= num4):
    print("The greatest number is:", num3)
else:
    print("The greatest number is:", num4)


# ------------------------------------------------------------------------------
# Problem 2: Check pass/fail (Requires >= 40% total and >= 33% in each subject)
# ------------------------------------------------------------------------------
sub1 = int(input("Enter marks of first subject: "))
sub2 = int(input("Enter marks of second subject: "))
sub3 = int(input("Enter marks of third subject: "))

total_percentage = (sub1 + sub2 + sub3) / 3
print(f"The total percentage is: {total_percentage:.2f}%")

if sub1 >= 33 and sub2 >= 33 and sub3 >= 33 and total_percentage >= 40:
    print(f"Passed! Your percentage is {total_percentage:.2f}%")
else:
    print("Failed!")


# ------------------------------------------------------------------------------
# Problem 3: Detect spam keywords in a comment
# ------------------------------------------------------------------------------
comment = input("Enter your comment: ").lower()

if (
    ("make a lot of money" in comment)
    or ("buy now" in comment)
    or ("subscribe this" in comment)
    or ("click this" in comment)
):
    print("This is a spam comment!")
else:
    print("This comment is clean.")


# ------------------------------------------------------------------------------
# Problem 4: Check if a username contains less than 10 characters
# ------------------------------------------------------------------------------
username = input("Enter your username: ")

if len(username) < 10:
    print("Username contains less than 10 characters")
else:
    print("Username contains 10 or more characters")


# ------------------------------------------------------------------------------
# Problem 5: Check if a given name is present in a list
# ------------------------------------------------------------------------------
lst = [
    "ram",
    "lakshman",
    "bharat",
    "shatrughan",
    "ravana",
    "indrajit",
    "kumbhkaran",
    "vibhisan",
    "dasratha",
]
name = input("Enter a name: ").lower()

if name in lst:
    print("Name is present in the list.")
else:
    print("Name is not present in the list.")


# ------------------------------------------------------------------------------
# Problem 6: Calculate student grade based on marks
# ------------------------------------------------------------------------------
# Scheme:
# 90 - 100 => Ex
# 80 - 90  => A
# 70 - 80  => B
# 60 - 70  => C
# 50 - 60  => D
# < 50     => F

marks = float(input("Enter your marks: "))

if 90 <= marks <= 100:
    grade = "Ex"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print("Your grade is:", grade)


# ------------------------------------------------------------------------------
# Problem 7: Check if a post mentions "Harry" (Case-insensitive check)
# ------------------------------------------------------------------------------
post = input("Enter the post text: ").lower()

if "harry" in post:
    print("Yes! This post is talking about Harry")
else:
    print("No! This post is NOT talking about Harry")
# ==============================================================================