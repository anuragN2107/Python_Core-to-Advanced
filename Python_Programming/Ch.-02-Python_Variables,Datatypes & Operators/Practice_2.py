# ==============================================================================
#                 PYTHON PRACTICE QUESTIONS & SOLUTIONS
# ==============================================================================

# ------------------------------------------------------------------------------
# Q.1 Write a python program to add two numbers.
# ------------------------------------------------------------------------------
# Ans1
a = 545
b = 169
print("Sum of two numbers is: ", a + b)  # Output: 714 , Sum of two numbers is: <sum of a and b>


# ------------------------------------------------------------------------------
# Q.2 Write a python program to find remainder of two numbers using input() function.
# ------------------------------------------------------------------------------
# Ans2
x = int(input("Enter a number 1: "))
y = int(input("Enter a number 2: "))
print("Remainder of two numbers is: ", x % y)  # Output: 1 , Remainder of two numbers is: <remainder of x and y>


# ------------------------------------------------------------------------------
# Q.3 Check the type of variable assigned using input() function.
# ------------------------------------------------------------------------------
# Ans3
name = input("Enter your name: ")
print("Hello, " + name + "!")  # Output: Hello, <name>!
print(type(name))              # Output: <class 'str'>


# ------------------------------------------------------------------------------
# Q.4 Use comparison operator to find out whether a given variable 'y' is greater than 'z' or not.
# ------------------------------------------------------------------------------
# Ans4
y = int(input("Enter the first number: "))
z = int(input("Enter the second number: "))
print("Is y greater than z? ", y > z)  # Output: True or False


# ------------------------------------------------------------------------------
# Q.5 Write a python program to find the average of two numbers entered by the user.
# ------------------------------------------------------------------------------
# Ans5
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
average = (num1 + num2) / 2
print("The average of the two numbers is: ", average)  # Output: Average of two numbers


# ------------------------------------------------------------------------------
# Q.6 Write a python program to find the square and cube of a number entered by the user.
# ------------------------------------------------------------------------------
# Ans6
num = float(input("Enter a number: "))
print("The square of the number is: ", num ** 2)  # Output: Square of the number
print("The cube of the number is: ", num ** 3)    # Output: Cube of the number
# ==============================================================================